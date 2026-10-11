"""
A Tkinter password manager backed by an encrypted SQLite vault.

Install the encryption dependency with: python -m pip install cryptography
The database is saved beside this script in this folder.
Service names and usernames are stored in plain text to allow searching;
password values are encrypted.
If the master password is lost, the encrypted passwords cannot be recovered.
"""

import base64
import binascii
import hashlib
import os
import secrets
import sqlite3
import string
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, simpledialog, ttk

try:
    from cryptography.fernet import Fernet, InvalidToken
except ModuleNotFoundError as error:
    raise SystemExit(
        "Missing dependency. Install it with: python -m pip install cryptography"
    ) from error


DATABASE_PATH = Path(__file__).resolve().parent / "passwords.db"
PBKDF2_ITERATIONS = 600_000
VERIFIER = b"python-password-manager"


def derive_key(master_password, salt):
    key = hashlib.pbkdf2_hmac(
        "sha256",
        master_password.encode("utf-8"),
        salt,
        PBKDF2_ITERATIONS,
        dklen=32,
    )
    return Fernet(base64.urlsafe_b64encode(key))


def generate_password(length=20):
    if length < 12:
        raise ValueError("Password length must be at least 12 characters.")

    groups = (
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        "!@#$%^&*()-_=+",
    )
    password = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    password.extend(secrets.choice(alphabet) for _ in range(length - len(password)))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def open_database(master_password):
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    try:
        os.chmod(DATABASE_PATH, 0o600)
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS metadata (
                key TEXT PRIMARY KEY,
                value TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                encrypted_password TEXT NOT NULL
            );
            """
        )
        metadata = dict(
            connection.execute("SELECT key, value FROM metadata").fetchall()
        )

        if "salt" not in metadata and "verifier" not in metadata:
            if connection.execute("SELECT 1 FROM passwords LIMIT 1").fetchone():
                raise ValueError("The database is missing required vault data.")
            salt = secrets.token_bytes(16)
            cipher = derive_key(master_password, salt)
            connection.executemany(
                "INSERT INTO metadata (key, value) VALUES (?, ?)",
                [
                    ("salt", base64.b64encode(salt).decode("ascii")),
                    ("verifier", cipher.encrypt(VERIFIER).decode("ascii")),
                ],
            )
            connection.commit()
            return connection, cipher

        if "salt" not in metadata or "verifier" not in metadata:
            raise ValueError("The database is missing required vault data.")

        try:
            salt = base64.b64decode(metadata["salt"], validate=True)
            if len(salt) != 16:
                raise ValueError("The database contains an invalid salt.")
            cipher = derive_key(master_password, salt)
            if cipher.decrypt(metadata["verifier"].encode("ascii")) != VERIFIER:
                raise ValueError("Incorrect master password.")
        except InvalidToken as error:
            raise ValueError("Incorrect master password or damaged database.") from error
        except (binascii.Error, UnicodeDecodeError) as error:
            raise ValueError("The database contains invalid vault data.") from error
        return connection, cipher
    except (OSError, sqlite3.Error, ValueError):
        connection.close()
        raise


class PasswordManagerApp:
    def __init__(self, root, connection, cipher):
        self.root = root
        self.connection = connection
        self.cipher = cipher

        root.title("Password Manager")
        root.geometry("720x440")
        root.minsize(520, 320)
        root.protocol("WM_DELETE_WINDOW", self.close)

        container = ttk.Frame(root, padding=16)
        container.pack(fill="both", expand=True)

        ttk.Label(
            container,
            text="Password Manager",
            font=("TkDefaultFont", 18, "bold"),
        ).pack(anchor="w", pady=(0, 12))

        search_frame = ttk.Frame(container)
        search_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(search_frame, text="Search:").pack(side="left", padx=(0, 8))
        self.search_var = tk.StringVar()
        search_box = ttk.Entry(search_frame, textvariable=self.search_var)
        search_box.pack(side="left", fill="x", expand=True)
        self.search_var.trace_add("write", self.refresh_entries)

        table_frame = ttk.Frame(container)
        table_frame.pack(fill="both", expand=True)
        self.entries_table = ttk.Treeview(
            table_frame,
            columns=("service", "username"),
            show="headings",
            selectmode="browse",
        )
        self.entries_table.heading("service", text="Service")
        self.entries_table.heading("username", text="Username")
        self.entries_table.column("service", width=250)
        self.entries_table.column("username", width=350)
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.entries_table.yview
        )
        self.entries_table.configure(yscrollcommand=scrollbar.set)
        self.entries_table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.entries_table.bind("<Double-1>", lambda _event: self.show_password())

        buttons = ttk.Frame(container)
        buttons.pack(fill="x", pady=(12, 0))
        ttk.Button(buttons, text="Add password", command=self.add_entry).pack(
            side="left"
        )
        ttk.Button(buttons, text="Show password", command=self.show_password).pack(
            side="left", padx=8
        )
        ttk.Button(buttons, text="Generate password", command=self.show_generated).pack(
            side="left"
        )
        ttk.Button(buttons, text="Close", command=self.close).pack(side="right")

        self.refresh_entries()
        search_box.focus_set()

    def refresh_entries(self, *_args):
        query = self.search_var.get().strip().casefold()
        for item in self.entries_table.get_children():
            self.entries_table.delete(item)

        try:
            entries = self.connection.execute(
                """
                SELECT id, service, username
                FROM passwords
                ORDER BY service, username
                """
            ).fetchall()
            for entry in entries:
                if (
                    query
                    and query not in entry["service"].casefold()
                    and query not in entry["username"].casefold()
                ):
                    continue
                self.entries_table.insert(
                    "",
                    "end",
                    iid=str(entry["id"]),
                    values=(entry["service"], entry["username"]),
                )
        except sqlite3.Error as error:
            messagebox.showerror("Database error", str(error), parent=self.root)

    def add_entry(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add password")
        dialog.transient(self.root)
        dialog.resizable(False, False)
        dialog.grab_set()

        form = ttk.Frame(dialog, padding=16)
        form.pack(fill="both", expand=True)
        service_var = tk.StringVar()
        username_var = tk.StringVar()
        password_var = tk.StringVar()

        ttk.Label(form, text="Website or service").grid(
            row=0, column=0, sticky="w", pady=5
        )
        ttk.Entry(form, textvariable=service_var, width=38).grid(
            row=0, column=1, columnspan=2, sticky="ew", pady=5
        )
        ttk.Label(form, text="Username or email").grid(
            row=1, column=0, sticky="w", pady=5
        )
        ttk.Entry(form, textvariable=username_var, width=38).grid(
            row=1, column=1, columnspan=2, sticky="ew", pady=5
        )
        ttk.Label(form, text="Password").grid(row=2, column=0, sticky="w", pady=5)
        password_entry = ttk.Entry(form, textvariable=password_var, width=26)
        password_entry.grid(row=2, column=1, sticky="ew", pady=5)

        def fill_generated_password():
            password_var.set(generate_password())
            password_entry.focus_set()

        ttk.Button(
            form, text="Generate", command=fill_generated_password
        ).grid(row=2, column=2, padx=(8, 0), pady=5)

        def save_entry():
            service = service_var.get().strip()
            username = username_var.get().strip()
            password = password_var.get()
            if not service or not username or not password:
                messagebox.showerror(
                    "Missing information",
                    "Enter a service, username, and password.",
                    parent=dialog,
                )
                return

            try:
                encrypted_password = self.cipher.encrypt(
                    password.encode("utf-8")
                ).decode("ascii")
                self.connection.execute(
                    """
                    INSERT INTO passwords (service, username, encrypted_password)
                    VALUES (?, ?, ?)
                    """,
                    (service, username, encrypted_password),
                )
                self.connection.commit()
                dialog.destroy()
                self.refresh_entries()
            except (sqlite3.Error, OSError) as error:
                messagebox.showerror("Could not save password", str(error), parent=dialog)

        actions = ttk.Frame(form)
        actions.grid(row=3, column=0, columnspan=3, sticky="e", pady=(12, 0))
        ttk.Button(actions, text="Cancel", command=dialog.destroy).pack(side="right")
        ttk.Button(actions, text="Save", command=save_entry).pack(
            side="right", padx=(0, 8)
        )
        form.columnconfigure(1, weight=1)
        dialog.bind("<Return>", lambda _event: save_entry())
        dialog.bind("<Escape>", lambda _event: dialog.destroy())
        dialog.wait_window()

    def selected_entry_id(self):
        selection = self.entries_table.selection()
        if not selection:
            messagebox.showinfo(
                "Select an account",
                "Select an account first.",
                parent=self.root,
            )
            return None
        return int(selection[0])

    def show_password(self):
        entry_id = self.selected_entry_id()
        if entry_id is None:
            return

        try:
            entry = self.connection.execute(
                """
                SELECT service, username, encrypted_password
                FROM passwords
                WHERE id = ?
                """,
                (entry_id,),
            ).fetchone()
            if entry is None:
                self.refresh_entries()
                return
            password = self.cipher.decrypt(
                entry["encrypted_password"].encode("ascii")
            ).decode("utf-8")
        except InvalidToken:
            messagebox.showerror(
                "Could not read password",
                "The saved password is damaged or cannot be decrypted.",
                parent=self.root,
            )
            return
        except (sqlite3.Error, UnicodeDecodeError) as error:
            messagebox.showerror(
                "Could not read password",
                str(error),
                parent=self.root,
            )
            return

        messagebox.showinfo(
            f"{entry['service']} — {entry['username']}",
            f"Password: {password}",
            parent=self.root,
        )

    def show_generated(self):
        password = generate_password()
        dialog = tk.Toplevel(self.root)
        dialog.title("Generated password")
        dialog.transient(self.root)
        dialog.resizable(False, False)

        content = ttk.Frame(dialog, padding=16)
        content.pack(fill="both", expand=True)
        ttk.Label(content, text="Generated password:").pack(anchor="w", pady=(0, 6))
        password_var = tk.StringVar(value=password)
        password_entry = ttk.Entry(
            content, textvariable=password_var, width=38, state="readonly"
        )
        password_entry.pack(fill="x")
        password_entry.selection_range(0, "end")

        def copy_password():
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo(
                "Copied",
                "Password copied to the clipboard.",
                parent=dialog,
            )

        actions = ttk.Frame(content)
        actions.pack(fill="x", pady=(12, 0))
        ttk.Button(actions, text="Copy", command=copy_password).pack(side="left")
        ttk.Button(actions, text="Close", command=dialog.destroy).pack(side="right")

    def close(self):
        self.connection.close()
        self.root.destroy()


def get_master_password(root, is_new_vault):
    if not is_new_vault:
        return simpledialog.askstring(
            "Unlock password manager",
            "Master password:",
            show="*",
            parent=root,
        )

    while True:
        password = simpledialog.askstring(
            "Create password manager",
            "Create a master password (at least 12 characters):",
            show="*",
            parent=root,
        )
        if password is None:
            return None
        if len(password) < 12:
            messagebox.showerror(
                "Master password too short",
                "Use at least 12 characters.",
                parent=root,
            )
            continue
        confirmation = simpledialog.askstring(
            "Confirm master password",
            "Enter the master password again:",
            show="*",
            parent=root,
        )
        if confirmation is None:
            return None
        if password == confirmation:
            return password
        messagebox.showerror(
            "Passwords do not match",
            "Enter and confirm the same master password.",
            parent=root,
        )


def main():
    root = tk.Tk()
    root.withdraw()
    master_password = get_master_password(root, not DATABASE_PATH.exists())
    if master_password is None:
        root.destroy()
        return

    try:
        connection, cipher = open_database(master_password)
    except (OSError, sqlite3.Error, ValueError) as error:
        messagebox.showerror(
            "Could not open password manager",
            str(error),
            parent=root,
        )
        root.destroy()
        return

    PasswordManagerApp(root, connection, cipher)
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()

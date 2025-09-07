import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, messagebox
from pathlib import Path

tasutavari = "#f4f7fb"
nappi = "#2b7cff"
fontti = ("Helvetica", 11)

root = tk.Tk()
root.title("Joku appi")
root.geometry("480x360")
root.configure(bg=tasutavari)
root.resizable(False, False)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TFrame", background=tasutavari)
style.configure("TLabel", background=tasutavari, font=fontti)
style.configure("TButton", font=fontti, padding=6)
style.configure("Accent.TButton", background=nappi, foreground="white")
style.map("Accent.TButton",
          background=[("active", "#1a5fd6")])

tiedosto = Path.home() / "paivakirja.txt"
tiedosto.touch(exist_ok=True)

def tallenna():
    teksti = txt.get("1.0", "end-1c").strip()
    if not teksti:
        messagebox.showinfo("Info", "Ei tallennettavaa tekstiä.")
        return
    with tiedosto.open("a", encoding="utf-8") as tiedosto:
        tiedosto.write(teksti + "\n")
    txt.delete("1.0", "end")
    lbl.config(text="Viimeisin tallennus: " + teksti[:60] + ("..." if len(teksti) > 60 else ""))
    print("tiedot tallennettu")

def nayta():
    if not tiedosto.exists():
        lbl.config(text="Ei tallennettua tekstiä.")
        return
    with tiedosto.open("r", encoding="utf-8") as tiedosto:
        content = tiedosto.read().strip()
    lbl.config(text=content if content else "Ei tallennettua tekstiä.")

def tyhjenna():
    if messagebox.askyesno("Vahvista", "Haluatko tyhjentää kaikki tallenteet?"):
        with tiedosto.open("w", encoding="utf-8") as tiedosto:
            tiedosto.truncate(0)
        lbl.config(text="")
        print("Tyhjennetty")

main = ttk.Frame(root, padding=12)
main.pack(fill="both", expand=True)

txt = scrolledtext.ScrolledText(main, height=6, width=50, wrap="word", font=fontti)
txt.pack(pady=(0, 8))

btn_frame = ttk.Frame(main)
btn_frame.pack(fill="x", pady=(0, 8))

btn_save = ttk.Button(btn_frame, text="Tallenna", command=tallenna, style="Accent.TButton")
btn_save.pack(side="left", padx=6)

btn_show = ttk.Button(btn_frame, text="Näytä teksti", command=nayta)
btn_show.pack(side="left", padx=6)

btn_clear = ttk.Button(btn_frame, text="Tyhjennä tiedosto", command=tyhjenna)
btn_clear.pack(side="left", padx=6)

lbl = ttk.Label(main, text="", wraplength=440)
lbl.pack(fill="x")

if __name__ == "__main__":
    root.mainloop()
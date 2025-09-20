import tkinter
import webbrowser
import json
from tkinter import *
from tkinter import messagebox

# windown after login
def main():
    root = tkinter.Tk()
    root.geometry("800x800")
    root.title("app")

    text = tkinter.StringVar()
    text.set("Welcome to the operating system \n")
    
    label = tkinter.Label(root, textvariable=text, font=("Arial", 25, "bold"))
    label.pack(pady=30)

    def on_click():
        webbrowser.open("https://www.google.com")

    btn = Button(root, text = 'Open browser', command = on_click) 
    btn.pack()

    root.mainloop()

# login
def login(username_entry, password_entry):
    userid = username_entry.get()
    password = password_entry.get()

    # validation 
    with open("/home/lenni/home/koodit/python/.venv/main/kayttojarjestelmaThinker/users.json", "r") as f:
        data = json.load(f)
        for key, value in data.items():
            for d in value:
                if d["username"] == userid and d["password"] == password:
                    l.destroy()
                    main()
                else:
                    messagebox.showerror("Login Failed", "Invalid username or password")

l = tkinter.Tk()
l.geometry("800x800")
l.title("app")

username_label = tkinter.Label(l, text="Userid:")
username_label.pack()

username_entry = tkinter.Entry(l)
username_entry.pack()

password_label = tkinter.Label(l, text="Password:")
password_label.pack()

password_entry = tkinter.Entry(l, show="*")  
password_entry.pack()

l.protocol("WM_DELETE_WINDOW", login)

login_button = tkinter.Button(l, text="Login", command=lambda: login(username_entry, password_entry))
login_button.pack()

l.mainloop()


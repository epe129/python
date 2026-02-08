import tkinter as tk
import random

root = tk.Tk()
root.title("ArvaaNumeroPeli")
root.geometry("700x200")
root.configure(bg="#1e1e2e")

luku_var=tk.StringVar()
my_string_var=tk.StringVar()

numero = random.randint(1, 100)

def laheta():
    luku=luku_var.get()
    print("Arvaus: " + luku)
    luku_var.set("")
    try:
        if int(luku) < numero:
            my_label.place(x=350, y=45)
            my_string_var.set("suurempi")
            my_label.config(fg="#FFD700")
        elif int(luku) > numero:
            my_label.place(x=350, y=45)
            my_string_var.set("pienenpi")
            my_label.config(fg="#FFD700")
        else:
            my_label.place(x=350, y=45)
            my_string_var.set(f"oikein {numero}")
            my_label.config(fg="#00FF41")
    except:
        my_label.place(x=190, y=45)
        my_string_var.set("Annoit kirjaimia tai tyhjän inputin")
        my_label.config(fg="#FF6B6B")

luku_label = tk.Label(root, text = 'Arvaaluku:', font=('calibre',20, 'bold'), fg="#00D9FF", bg="#1e1e2e")
luku_entry = tk.Entry(root, textvariable = luku_var, font=('calibre',20,'normal'), width=5, bg="#2d2d3d", fg="#00FF41", insertbackground="#00FF41")
luku_label.place(x=180, y=5)
luku_entry.place(x=350, y=5)

my_string_var.set("")
my_label = tk.Label(root, textvariable = my_string_var, font=('calibre',15,'normal'), bg="#1e1e2e")
my_label.place(x=350, y=45)

sub_btn=tk.Button(root, text = 'Submit', command = laheta, bg="#00D9FF", fg="#1e1e2e", activebackground="#00FF41", activeforeground="#1e1e2e", font=('calibre',10,'bold'))
sub_btn.place(x=450, y=8)

root.mainloop()
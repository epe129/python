import tkinter as tk
 
root = tk.Tk()
root.title("Joku appi")
root.geometry("400x400")

def tallenna():
    teksti = txt.get("1.0", "end-1c")
    with open("käyttäjän_syöte", "a") as tiedoto:
        tiedoto.write(f" {teksti}")
    print("tiedot tallenettu")

def näytä():
    with open("käyttäjän_syöte", "r") as tiedoto:
        lbl.config(text=f"{tiedoto.read()}")


# otta input käyttäjältä
txt = tk.Text(root, height=2, width=40)
txt.pack()

nappi = tk.Button(root,text="tallenna",command=tallenna)
nappi.pack()

nappi_näytä = tk.Button(root, text="näytä teksti", command=näytä)
nappi_näytä.pack()

lbl = tk.Label(root, text="")
lbl.pack()

if __name__=="__main__":
    root.mainloop()
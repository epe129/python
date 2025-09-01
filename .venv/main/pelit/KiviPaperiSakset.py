import random

def KiviPaperiSaksetPeli(): 
    KiviPaperiSakset = ["Kivi", "Paperi", "Sakset"]

    r = random.choice(KiviPaperiSakset)

    kysy = str(input("Kivi, Sakset vai Paperi: ")).capitalize()

    if r == "Kivi" and kysy ==  "Kivi":
        print("------------")
        print(f"tasapeli, {r} + {kysy}")
    elif r == "Kivi" and kysy ==  "Sakset":
        print("------------")
        print(f"Hävisit, {r} + {kysy}")
    elif r == "Kivi" and kysy ==  "Paperi":
        print("------------")
        print(f"Voitit, {r} + {kysy}")
    elif r == "Paperi" and kysy ==  "Paperi":
        print("------------")
        print(f"tasapeli, {r} + {kysy}")
    elif r == "Paperi" and kysy ==  "Kivi":
        print("------------")
        print(f"Hävisit, {r} + {kysy}")
    elif r == "Paperi" and kysy ==  "Sakset":
        print("------------")
        print(f"Voitit, {r} + {kysy}")
    elif r == "Sakset" and kysy ==  "Sakset":
        print("------------")
        print(f"tasapeli, {r} + {kysy}")
    elif r == "Sakset" and kysy ==  "paperi":
        print("------------")
        print(f"Hävisit, {r} + {kysy}")
    elif r == "Sakset" and kysy ==  "Kivi":
        print("------------")
        print(f"Voitit, {r} + {kysy}")
  
    jatkaako = str(input("Haluatko jatkaa pelaamista (kyllä/ei): "))
    if jatkaako == "kyllä":
        KiviPaperiSaksetPeli()
    else:
        print("Heippa")


KiviPaperiSaksetPeli()
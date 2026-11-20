import random

sanat = ["koira", "kissa", "oulu", "tietokone", "ohjelmointi"]

def SanaJahtiPeli():
    sana = random.choice(sanat)
    r = ''.join(random.sample(sana,len(sana)))
    print(f"Arvattava sana: {r}")
    print("----------")
    arvaa = str(input("Arvaa sekoitettu sana: "))
    while arvaa != sana:
        print("----------")
        print(f"väärin, yritä uudelleen {r}: ")
        print("----------")
        arvaa = str(input("Arvaa sekoitettu sana uudelleen: "))
    if arvaa == sana:
        print("----------")
        print("oikein")
        print("----------")
        jatkaa = str(input("Haluatko arvata lisää sanoja (kyllä/ei): "))
        if jatkaa == "kyllä":
            print("----------")
            SanaJahtiPeli()
        else:
            print("----------")
            print("heippa")     

SanaJahtiPeli()

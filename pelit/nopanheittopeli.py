import random

def NopanHeittoPeli():
    numerot = random.randint(1,6)
    print(f"Nopan numero on {numerot}")
    print("-------------------------")
    jatka = str(input("Haluatko heittää uudestaan noppaa (kyllä/ei): "))
    print("-------------------------")
    if jatka == "kyllä":
        NopanHeittoPeli()
    else:
        print("Heippa! ")
NopanHeittoPeli()
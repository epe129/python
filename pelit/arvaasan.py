import random

def ArvausPeli():
    sanat = ["koira", "kissa", "oulu","tietokone","puhelin"]
    print("--------")
    print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
    sana = random.choice(sanat)
    print("--------")
    arvaus = str(input("Arvaa jokin sanoista: "))
    
    while arvaus != sana:
        print("--------")
        print("Väärin")
        print("--------")
        print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
        print("--------")
        arvaus = str(input("Arvaa jokin sanoista: "))
        print("--------")
    
    if arvaus == sana:
        print(f"Oikein {sana}")
        print("--------")
        jatkaa = str(input("Haluatko jatkaa (kyllä/ei) "))
        if jatkaa == "kyllä":
            ArvausPeli2()
        else:
            print("--------")
            print("heippa")

def ArvausPeli2():
    sanat = ["opettaja","lääkäri","palomies","insinööri","taiteilija"]
    print("--------")
    print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
    sana = random.choice(sanat)
    print("--------")
    arvaus = str(input("Arvaa jokin sanoista: "))
    
    while arvaus != sana:
        print("--------")
        print("Väärin")
        print("--------")
        print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
        print("--------")
        arvaus = str(input("Arvaa jokin sanoista: "))
        print("--------")
    
    if arvaus == sana:
        print(f"Oikein {sana}")
        print("--------")
        jatkaa = str(input("Haluatko jatkaa (kyllä/ei) "))
        if jatkaa == "kyllä":
            print("k")
        else:
            print("--------")
            print("heippa")

ArvausPeli()    
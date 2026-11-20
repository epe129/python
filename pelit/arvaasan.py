import random

def ArvausPeli():
    sanat = ["koira","kissa", "oulu","tietokone","puhelin"]
    print("--------")
    print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
    sana = random.choice(sanat)
    print("--------")
    
    while True:
        arvaus = str(input("Arvaa jokin sanoista: "))
        print("--------")
    
        if arvaus == sana:
            print(f"Oikein {sana}")
            print("--------")
            break
        elif arvaus != sana:
            print("väärin")
    print("-----------------------")
    jatkaa = str(input("Haluatko pelata jatkaa? (kyllä/ei): "))
    print("-----------------------")
    if jatkaa == "kyllä":
        ArvausPeli2()
    else:
        print("heippa") 

def ArvausPeli2():
    sanat = ["opettaja","lääkäri","palomies","insinööri","taiteilija"]
    print("--------")
    print(f"Arvaa jokin näistä sanoista rajaton määrä arvauksia:{sanat}")
    sana = random.choice(sanat)
    print("--------")

    while True:
        arvaus = str(input("Arvaa jokin sanoista: "))
        print("--------")
    
        if arvaus == sana:
            print(f"Oikein {sana}")
            kysy()
            break
        elif arvaus != sana:
            print("väärin")

jatka = True

def kysy():
        global jatka
        print("-----------------------")
        jatkaa = str(input("Haluatko pelata jatkaa? (kyllä/ei): "))
        print("-----------------------")
        if jatkaa == "kyllä":
          pass
        else:
            print("heippa") 
            jatka = False

if jatka:
    ArvausPeli()

# tee parempi betti systeemi joskus
import random

def tervetuloa():
    print("Tervetuloa peliin!")
    print("--------------------")
    print("Alku saldosi on 100€")

tervetuloa()

def peli():
    p = True
    kokonaissaldo = 100
    try:
        while p:
            print("--------------------")
            betti = int(input(f"Aseta bettisi {kokonaissaldo}€: "))
            b = kokonaissaldo - betti
            if betti > kokonaissaldo:
                print("--------------------")
                print(f"saldosi on {kokonaissaldo}€")
                print("--------------------")
                betti = int(input(f"Aseta bettisi saldon mukaan: "))
            print("--------------------")
            symbols = [0,10, 5, 0, 8, 0, 6, 0, 4, 0, 12, 0, 2, 0, 15, 0, 20, 0, 1,]
            for i in range(1):
                sr = random.choice(symbols)
                sb = sr * betti
                for i in range(1):
                    sr2 = random.choice(symbols)
                    sb2 = sr2 * betti
                    for i in range(1):
                        sr3 = random.choice(symbols)
                        sb3 = sr3 * betti
            print(f"Voitit {sb}, {sb2}, {sb3}€")
            print("-----------------------")
            kokonaissaldo = sb + sb2 + sb3 + b
            print(f"Kokonais saldosi on {kokonaissaldo}€")    
            print("-----------------------")
            jatkaa = str(input("Haluatko jatkaa (kyllä/ei): "))
            if jatkaa == "kyllä":
                continue
            else:
                print("-----------------------")
                print("heippa")
                p = False
                break
    except ValueError:
        print("Käy vain numerot väliltä 1-100 ei muita merkkejä!")
        betti = input("paina enter mennäksesi takaisin alkuun: ")
        peli()
peli()

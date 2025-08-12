import random
def Arvaaluku():
    ArvauksienMäärä = 0
    kierroset = 0 
    tulokset = []
    try:
        luku = random.randint(1,100)
        while True:
            arvaa = int(input("Arvaa luku väliltä 1-100: "))
            ArvauksienMäärä += 1
            if arvaa < luku:
                print("-------")
                print("Suurempi luku")
                print("-------")
            elif arvaa > luku:
                print("-------")
                print("Pienenpi luku")
                print("-------")        
            else:
                kierroset += 1
                print("-------")
                print(f"Oikein")
                print("-------")
                ka = f"kierros {kierroset}, arvauksien määrä {ArvauksienMäärä}"
                tulokset.append(ka)
                ArvauksienMäärä = 0
                jatkaa = str(input("Haluat jatkaa arvailua (kyllä/ei): "))
                if jatkaa == "kyllä":
                    print("-------")
                    luku = random.randint(1,100)
                    continue
                else:
                    print("-------")
                    print("Heippa")
                    print("-------")
                    for i in tulokset:
                        print(i)
                    break
    except ValueError:
        print("-------")
        print("Pelkästään numeroita 1-100")
        print("-------")
        input("Paina enter päästäksesi takaisin pelaamaan: ")
        print("-------")
        Arvaaluku()
Arvaaluku()
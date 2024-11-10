import random

def Arvaaluku():
    luku = random.randrange(100)
    try:
        arvaa = int(input("Arvaa luku väliltä 1-100: "))
        ArvauksienMäärä = 1
        while arvaa != luku:
            if arvaa < luku:
                print("-------")
                print("Suurempi luku")
                print("-------")
                arvaa = int(input("Arvaa luku väliltä 1-100: "))
                ArvauksienMäärä += 1
            elif arvaa > luku:
                print("-------")
                print("Pienenpi luku")
                print("-------")
                arvaa = int(input("Arvaa luku väliltä 1-100: "))
                ArvauksienMäärä += 1
        if arvaa == luku:
            print("-------")
            print(f"Oikein {luku}, arvauksiasi oli {ArvauksienMäärä}")
            print("-------")
            jatkaa = str(input("Haluat jatkaa arvailua (kyllä/ei): "))
        if jatkaa == "kyllä":
            print("-------")
            Arvaaluku()
        else:
            print("-------")
            print("Heippa")
    except ValueError:
        print("-------")
        print("Pelkästään numeroita 1-100")
        print("-------")
        input("Paina enter päästäksesi takaisin pelaamaan: ")
        print("-------")
        Arvaaluku()
    
        

Arvaaluku()
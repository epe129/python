def laskin():
    try:
        vastaus = int(input("1 antaa luvun kertotaulu, 2 pluslasku, 3 miinuslasku, 4 jakolasku "))
    except ValueError:
        print("Numero väliltä 1-4")
        vastaus = int(input("1 antaa luvun kertotaulu, 2 pluslasku, 3 miinuslasku, 4 jakolasku "))
    if vastaus == 1:
        luku = int(input("Minkä luvun kertotaulun haluaisit? "))
        for i in range(1, 11):
            print(str(luku) + " * " + str(i) + " = " + str(luku * i))
    elif vastaus == 2:
        eka = int(input("luku: "))
        toka = int(input("luku: "))
        print("Vastaus on: " + str(eka + toka))
    elif vastaus == 3:
        eka = int(input("luku: "))
        toka = int(input("luku: "))
        print("Vastaus on: " + str(eka - toka))
    elif vastaus == 4:
        eka = int(input("luku: "))
        toka = int(input("luku "))
        print("Vastaus on: " + str(eka/toka))
    else:
        print("Numero väliltä 1-4")
        laskin()   

laskin()
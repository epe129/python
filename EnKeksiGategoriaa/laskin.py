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
        eka = int(input("Eka luku jonka haluaisit plussata? "))
        toka = int(input("Toinen luku jonka haluaisit plussata? "))
        print("Vastaus on: " + str(eka + toka))
    elif vastaus == 3:
        eka = int(input("Mistä luvusta haluaisit miinustaa? "))
        toka = int(input("Minkä luvun haluaisit siitä miinustaa? "))
        print("Vastaus on: " + str(eka - toka))
    elif vastaus == 4:
        eka = int(input("Mikä luku jaetaan "))
        toka = int(input("Millä jaetaan "))
        print("Vastaus on: " + str(eka/toka))
    elif vastaus != 1 and vastaus != 2 and vastaus != 3 and vastaus != 4:
       print("Numero väliltä 1-4")
       laskin()   

laskin()
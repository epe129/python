def laskin():
    while True:
        global luku1
        global luku2
        try:
            vastaus = int(input("1 antaa luvun kertotaulu, 2 pluslasku, 3 miinuslasku, 4 jakolasku "))
            if vastaus == 1:
                luku = int(input("Minkä luvun kertotaulun haluaisit? "))
                for i in range(1, 11):
                    print(f"{luku} * {i} = {luku * i}")
                break

            luku1 = int(input("luku: "))
            luku2 = int(input("luku: "))
            if vastaus == 2:
                print(f"Vastaus on: {luku1 + luku2}")
            elif vastaus == 3:
                print(f"Vastaus on: {luku1 - luku2}")
            elif vastaus == 4:
                print(f"Vastaus on: {luku1/luku2}")
            else:
                print("Numero väliltä 1-4")
                laskin()
            break
        except ValueError:
            print("ValueError")
            laskin()
laskin()
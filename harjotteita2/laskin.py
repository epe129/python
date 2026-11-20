def laskin():
    while True:
        try:
            lasku = input(": ").strip()
            if not lasku:
                print("Syötä lasku, esim. 5 + 3")
                continue

            osat = lasku.replace(" ", "")
            if osat.count("+") == 1:
                operaatio = "+"
            elif osat.count("-") == 1:
                operaatio = "-"
            elif osat.count("*") == 1:
                operaatio = "*"
            elif osat.count("/") == 1:
                operaatio = "/"
            else:
                raise ValueError("Virheellinen lasku")

            osa1, osa2 = lasku.split(operaatio)
            luku1 = float(osa1.strip())
            luku2 = float(osa2.strip())

            if operaatio == "+":
                tulos = luku1 + luku2
            elif operaatio == "-":
                tulos = luku1 - luku2
            elif operaatio == "*":
                tulos = luku1 * luku2
            elif operaatio == "/":
                if luku2 == 0:
                    print("Nollalla ei voi jakaa.")
                    continue
                tulos = luku1 / luku2

            if isinstance(tulos, float) and tulos.is_integer():
                print(f"Vastaus on: {int(tulos)}")
            else:
                print(f"Vastaus on: {tulos}")

        except ValueError:
            print("Virheellinen syöte. Käytä muotoa: 5 + 3")
        except ZeroDivisionError:
            print("Nollalla ei voi jakaa.")

        vastaus = input("1 jatka, 2 lopeta: ")
        if vastaus == "2":
            break


laskin()

class tehtavat:
    def __init__(self):
        self.tehtavat = []
        self.lataaTehtavat()
    
    def lisaaTehtava(self, lisattava):
        self.tehtavat.append(lisattava)
        print("Tehtävä lisätty")

    def PoistaTehtavat(self, poista):
        if 1 <= poista <= len(self.tehtavat):
            poistettu_tehtava = self.tehtavat.pop(poista - 1)
            print(f"Tehtävä '{poistettu_tehtava}' poistettu.")
        else:
           print("Virhe: Tuntematon tehtävän numero!")

    def KatsoTehtavat(self):
        if self.tehtavat:
            print("Tässä ovat nykyiset tehtävät:")
            for i, lisattava in enumerate(self.tehtavat, start=1):
                print(f"{i}. {lisattava}")
        else:
            print("Ei tehtäviä.")

    def lataaTehtavat(self):
        try:
            with open("tehtavat.txt", "r") as f:
                self.tehtavat = f.read().splitlines()
                print("Tehtävät ladattu tiedostoon")
        except FileNotFoundError:
            print("Tiedostoa ei löytynyt")

    def tallennaTehtavat(self):
        with open("tehtavat.txt", "w") as f:
            for tehtava in self.tehtavat:
                f.write(tehtava + "\n")
        print("Tehtävät tallennettu")


def main():
    tehtava = tehtavat()

    while True:
        kysy = str(input("1 Lisää tehtävä, 2 poista tehtävä, 3 katso tehtävät, 4 poistu: "))

        if kysy == "1":
            lisattava = str(input("Minkä tehtävän haluaisit lisätä: "))
            tehtava.lisaaTehtava(lisattava)
        if kysy == "2":
            poista = int(input("Anna poistettavan tehtävän numero: "))
            tehtava.PoistaTehtavat(poista)
        if kysy == "3":
            tehtava.KatsoTehtavat()
            input("paina enter mennnäksesi valikkoon: ")
        if kysy == "4":
            tehtava.tallennaTehtavat()
            break
    


if __name__ == "__main__":
    main()

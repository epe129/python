class Todo:
    def __init__(self):
        self.tasks = []

    def lisaa_tehtava(self, tehtava):
        self.tasks.append(tehtava)
        print("Tehtävä lisätty")

    def poista_tehtava(self, tehtavan_numero):
        if 1 <= tehtavan_numero <= len(self.tasks):
            poistettu_tehtava = self.tasks.pop(tehtavan_numero - 1)
            print(f"Tehtävä '{poistettu_tehtava}' poistettu.")
        else:
            print("Virhe: Tuntematon tehtävän numero!")

    def nayta_tehtavat(self):
        if self.tasks:
            print("Tässä ovat nykyiset tehtävät:")
            for i, tehtava in enumerate(self.tasks, start=1):
                print(f"{i}. {tehtava}")
        else:
            print("Ei tehtäviä.")

def main():
    todo = Todo()

    while True:
        print("\n1. Lisää tehtävä")
        print("2. Poista tehtävä")
        print("3. Näytä tehtävät")
        print("4. Lopeta")

        valinta = input("Valitse toiminto (1/2/3/4): ")

        if valinta == "1":
            tehtava = input("Syötä uusi tehtävä: ")
            todo.lisaa_tehtava(tehtava)
        elif valinta == "2":
            tehtava_numero = int(input("Syötä poistettavan tehtävän numero: "))
            todo.poista_tehtava(tehtava_numero)
        elif valinta == "3":
            todo.nayta_tehtavat()
            input("Paina Enter palataksesi päävalikkoon")
        elif valinta == "4":
            print("Sovellus suljetaan")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    main()

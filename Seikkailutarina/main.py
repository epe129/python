import random

def intro():
    print("Tervetuloa mystiseen seikkailuun!")
    print("Heräät keskellä metsää, kuulet kahinaa pensaikossa.")
    print("Mitä teet?")
    print("1. Tutki ääni")
    print("2. Juokse vastakkaiseen suuntaan")
    choice = input("> ")

    if choice == "1":
        investigate_noise()
    elif choice == "2":
        run_away()
    else:
        print("Et tehnyt mitään. Jokin lähestyy...")
        game_over("Sinut siepattiin!")

def investigate_noise():
    print("\nLähestyt ääntä ja huomaat vanhan, puhuvan ketun!")
    print("Kettu kysyy: 'Haluatko seurata minua vai etsiä omaa tiesi?'")
    print("1. Seuraa kettua")
    print("2. Mene omaa tietäsi")
    choice = input("> ")

    if choice == "1":
        follow_fox()
    elif choice == "2":
        own_path()
    else:
        game_over("Jäät paikalle ja eksyt metsään.")

def run_away():
    print("\nJuokset niin nopeasti kuin pystyt, mutta kompastut kiveen.")
    print("Heräät hämärässä luolassa. Edessäsi on kaksi tunnelia.")
    print("1. Vasemmanpuoleinen")
    print("2. Oikeanpuoleinen")
    choice = input("> ")

    if choice == "1":
        dragon_encounter()
    elif choice == "2":
        treasure_room()
    else:
        game_over("Et valinnut mitään ja jäit ikuisesti pimeään.")

def follow_fox():
    print("\nKettu johdattaa sinut salaiseen metsäkylään.")
    ending = random.choice(["Kylän asukkaat kruunaavat sinut kuninkaaksi!", 
                            "Kylä osoittautuu ansaksi – jäät vangiksi!"])
    game_over(ending)

def own_path():
    print("\nLöydät kartan maasta. Kartta näyttää aarteen sijainnin!")
    print("1. Seuraa karttaa")
    print("2. Heitä kartta pois ja jatka vaeltamista")
    choice = input("> ")

    if choice == "1":
        treasure_room()
    else:
        game_over("Eksyt suohon ja joudut kääntymään takaisin... liian myöhään.")

def dragon_encounter():
    print("\nTunnelissa nukkuu lohikäärme! Voit joko hiipiä ohi tai hyökätä.")
    print("1. Hiivi ohi")
    print("2. Hyökkää")
    choice = input("> ")

    if choice == "1":
        game_over("Onnistut hiipimään – ja löydät ulospääsyn!")
    else:
        game_over("Lohikäärme herää ja syöksee tulta – seikkailusi päättyy.")

def treasure_room():
    print("\nSaavut kammioon, joka on täynnä kultaa!")
    ending = random.choice(["Otat aarteen ja palaat sankarina kotiin!", 
                            "Kun kosket kultaa, huone romahtaa..."])
    game_over(ending)

def game_over(message):
    print("\n--- TARINA PÄÄTTYY ---")
    print(message)
    print("------------------------")

# Käynnistä peli
if __name__ == "__main__":
    intro()

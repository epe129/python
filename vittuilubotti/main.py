import json
import random

def kysy_tiedot():
    nimi = input("Mikä sun nimi on? ")
    paikka = input("Mistä päin olet? ")
    print("Valitse vittuilun taso:\n1 = Kevyt naljailu\n2 = Normivittuilu\n3 = Täysrähinä")
    while True:
        try:
            taso = int(input("Syötä taso (1–3): "))
            if taso in [1, 2, 3]:
                break
        except:
            pass
        print("Yritä nyt edes laittaa numero, nero...")
    return nimi, paikka, str(taso)

def hae_vittuilu(nimi, paikka, taso):
    try:
        with open("vittuilut.json", "r", encoding="utf-8") as f:
            kaikki_vittuilut = json.load(f)
        vaihtoehdot = kaikki_vittuilut.get(taso, [])
        if not vaihtoehdot:
            return "No nyt meni hiljaiseksi. Vittuilut puuttuu tältä tasolta."
        valittu = random.choice(vaihtoehdot)
        return valittu.format(nimi=nimi, paikka=paikka)
    except Exception as e:
        return f"Virhe vittuilua haettaessa: {e}"

# Pääohjelma
if __name__ == "__main__":
    nimi, paikka, taso = kysy_tiedot()
    vastaus = hae_vittuilu(nimi, paikka, taso)
    print("\n🤖 Feikki-AI sanoo:\n")
    print(vastaus)

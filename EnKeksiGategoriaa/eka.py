import datetime

#kysyy miten menee
kysymykset = {
    "meneekö hyvin " : None,
    "onko koodaaminen kivaa" : None,
}

for kysymys in kysymykset:
    vastaus = input(kysymys + "\nVastaus (kyllä/ei): ") #lower muuttaa vastuksen pieniksi kirjaimiksi
    while vastaus not in ["kyllä", "ei"]:
        vastaus = input("vastaa kyllä tai ei: ")
    kysymykset[kysymys] = vastaus



#seuraava pressa
def tarkista_presidentti():
    oikea_vastaus = "Stubb"
    vastaus = input("Kuka on Suomen seuraava presidentti Stubb vai haavisto?\nVastaus: ")
    print("      ")
    if vastaus.lower() == oikea_vastaus.lower():
        print("aiva oikein Stubb suomen 13 presidentti 53% äänistä.")
    else:
        print("haavisto ei voittanut.")
    print("          ")
if __name__ == "__main__":
    tarkista_presidentti()


#suomen eka pressa
def tarkista_eka_presidentti():
    oikea_vastaus = "Ståhlberg"
    vastaus = input("Kuka on Suomen ensimmäinen presidentti? Tässä vaihto ehtoja Mannerheim,Ståhlberg vai Kekkonen\nVastaus: ")
    print("          ")
    if vastaus.lower() == oikea_vastaus.lower():
        print("oikein.")
    else:
        print("Väärin Ståhlberg on Suomen ensimmäinen presidentti.")

if __name__ == "__main__":
    tarkista_eka_presidentti()

#peli kysymys joka vaikea
def vaikea_kysymys_peli():
    vaikea_kysymys = "Mikä on maailman suurin yksittäinen eläin?"
    print("            ")
    vastaus = input(f"{vaikea_kysymys}\nVastaus: ")
    print("          ")
    if vastaus.lower() == "sinivalas":
        print("oikein.")
    else:
        print("Väärin sinivalas on oikea.")

if __name__ == "__main__":
    vaikea_kysymys_peli()
print("         ")
# vitutus aste peli
def vitutusaste_peli():
    oikea_vastaus = 100

    print("Tervetuloa vitutusasteen peliin!")
    print("Kuinka vituttaa tänään? (0-100)")

    try:
        vastaus = int(input("Anna vitutusasteesi: "))
        
        if vastaus == oikea_vastaus:
            print("Oikein! Täsmälleen sama vitutusaste.")
        else:
            print(f"Väärin! Vitutusaste ei ollut {vastaus}, vaan {oikea_vastaus}.")
    except ValueError:
        print("Virheellinen syöte! Syötä kokonaisluku väliltä 0-100.")

if __name__ == "__main__":
    vitutusaste_peli()

#suomi tietovisa
def laske_oikein_vastatut_kysymykset(kysymykset):
    oikein_vastatut = 0
    kayttajan_vastaukset = {}
    for kysymys, oikea_vastaus in zip(kysymykset, oikeat_vastaukset):
        yritykset = 1
        while yritykset > 0:
            vastaus = input(kysymys + " ")
            kayttajan_vastaukset[kysymys] = vastaus.lower()
            if vastaus.lower() == oikea_vastaus.lower():
                oikein_vastatut += 1
                break
            else:
                yritykset -= 1
                print("väärin")
    return oikein_vastatut

def tulosta_oikeat_vastaukset(kysymykset, oikeat_vastaukset):
    for kysymys, vastaus in zip(kysymykset, oikeat_vastaukset):
        print(f"Kysymys: {kysymys}")
        print(f"Oikea vastaus: {vastaus}")
        print()

kysymykset = ["Suomen pääministeri", "Suomen presidentti"]
oikeat_vastaukset = ["Petteri Orpo", "Stubb"]

oikein_vastatut = laske_oikein_vastatut_kysymykset(kysymykset)
print("oikein oli", oikein_vastatut)
print("   ")
tulosta_oikeat_vastaukset(kysymykset, oikeat_vastaukset)

def tepornt_peli():
    oikea_vastaus = 4

    try:
        vastaus = int(input("paljon on 2+2: "))
        
        if vastaus == oikea_vastaus:
            print("Oikein.")
        else:
            print(f"Väärin! {vastaus}, vaan {oikea_vastaus}.")
    except ValueError:
        print("osaatko syöttää lukua.")

if __name__ == "__main__":
    tepornt_peli()
x = datetime.datetime.now()
print("tänään on,", x.strftime("%c"))



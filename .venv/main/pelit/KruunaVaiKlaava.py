# Tämä projekti simuloi kolikon heittoa ja antaa sinulle tuloksen, 
# onko se "kruuna" vai "klaava". 
# Voit tehdä tästä interaktiivisen ohjelman, 
# jossa käyttäjä voi valita kuinka monta kertaa kolikko heitetään, 
# ja ohjelma laskee kuinka monta kertaa kumpikin puoli tulee esille.
import random

def KruunaVaiKlaava():
    MaksimiMääräArvata = 11
    KK = ["Kruuna", "Klaava"]
    vastaus = str(input("Kumpi Kruuna vai Klaava: ").capitalize())
    print("--------")
    monta = int(input("Kuinka monta kertaa haluat arvata? maksimimäärä 10: "))
    arvata = 0
    oikeinMeni = 0
    väärinMeni = 0
    if monta > MaksimiMääräArvata or monta == 11:
        print("--------")
        print("Maksimi sallittu 10")
        print("--------")
        str(input("Paina enter jatkaaksesi, menee automaattisesti kymmeneksi luku: "))
        monta = 10
    while monta > arvata: 
        arvata += 1
        jompiKumpi = random.choice(KK)
        if vastaus == jompiKumpi:
            print(f"Oikein {jompiKumpi}")
            oikeinMeni += 1
        elif vastaus != jompiKumpi:
            print(f"Oikeavastaus oli {jompiKumpi}")
            väärinMeni += 1
    print("--------")
    print(f"Oikein meni {oikeinMeni}")
    print(f"Väärin meni {väärinMeni}")
    print("--------")
    KysymysUudelleen = str(input("Haluatko arvata uudeleen (kyllä/ei): "))
    print("--------")
    if KysymysUudelleen == "kyllä":
        KruunaVaiKlaava()
    else:
        print("Heippa")



KruunaVaiKlaava()
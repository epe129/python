import random

def tervehdys(käyttäjänimi):
    tervehdysvaihtoehdot = ["MORO", "TERVE", "HELLUREI", "MOII"]
    return random.choice(tervehdysvaihtoehdot) + " " + käyttäjänimi

def ohjelma():
    print("Tervetuloa chatbottiin")
    nimi = input("Anna nimesi ")
    print(tervehdys(nimi))

def numero():
    arvauskerrrat = 0
    oikea_numero = random.randrange(100)
    while True:
        arvaus = input("Arvaa numero 0-100 ")
        if not arvaus.isdigit():
            print("vain numeroita")
            continue
        arvaus = int(arvaus)
        arvauskerrrat += 1
        if arvaus < oikea_numero:
            print("liianpieni ")
        elif arvaus > oikea_numero:
           print("Liiansuuri ")
        elif arvaus == oikea_numero:
           print("OIKEIN!!", arvauskerrrat, "arvauksella ")
           break
        
        
            

sanat = ["auto", "kissa", "tietokone", "kukka", "koulu", "aurinko", "ranta", "koira", "maapallo"]


sr = random.choice(sanat)

def arvaa_sanat():
    print("Tervetuloa sanaselityspeliin!")
    print("Näistä sanoista auto, kissa, tietokone, kukka, koulu, aurinko, ranta, koira, maapallo ")
    print("Sanan pituus: ", len(sr) * "_ ")
    arvauskerrat = 0
    while True:
        arvaus = input("arvaa sana: ")
        arvauskerrat += 1
        if arvaus.lower() == sr:
            print(f"Oikein!! yrityksellä {arvauskerrat}")
            break
        else:
            print("väärin!!!!!! yritä uudelleen ")

def vitsit():

    vitsejä = [
        "Miksi kana ylitti tien? Saadakseen toiselle puolelle!",
        "Miksi kutsutaan nauravaa limakalvoa? HA-hengitykseksi!",
        "Miksi tietokone oli surullinen? Se oli kaatunut.",
    ]
    
    while vitsejä:
        Haluaako = input("haluat kuulla vitsejä (kyllä/ei):")
        if Haluaako == "ei":
            print("harmi")
            break
        print(vitsejä[0])
        vitsejä.pop(0)
        if not vitsejä:
            print("vitsit loppuvat")
        
            
if __name__ == "__main__":
    ohjelma()
    numero()
    arvaa_sanat()
    vitsit()
        
    
    

    



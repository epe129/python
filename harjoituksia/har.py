# Kirjoita ratkaisu tähän
def luvut():
    luvut = []
    harjoitukset_luvut = []
    pisteet_luvut = []
    pisteet = 0
    harjoitukset = 0
    laskuri = 0
    while True:
        maara = input("Koepisteet ja harjoitusten määrä: ")
        if maara == "":
            break
        luvu = list(map(int, maara.split()))
        pisteet += luvu[0]
        harjoitukset += luvu[1]
        har = luvu[1]
        pist = luvu[0]
        pisteet_luvut.append(pist)
        harjoitukset_luvut.append(har)
        laskuri += 1

    luvut.append(pisteet)
    luvut.append(harjoitukset)
    luvut.append(laskuri)
    luvut.append(harjoitukset_luvut) 
    luvut.append(pisteet_luvut)
    print("Tilasto:")
    # print(luvut)
    return luvut

def harjoituspisteet(luvut):
    harjoitukset = luvut[3]
    harjoitus_pisteet = []
    for i in harjoitukset:
        luku = int(i)
        piste = luku // 10
        harjoitus_pisteet.append(piste)

    # print(harjoitus_pisteet)
    
    return harjoitus_pisteet
     

def keskiarvo(luvut, har_pisteet):
    kaikki_pisteet_har = luvut[4]

    pisteet = luvut[0]
    laskuri = luvut[2]
    kaikki_pisteet_har = 0
    
    for i in har_pisteet:
        kaikki_pisteet_har += i
    
    pisteiden_keskiarvo = kaikki_pisteet_har +  pisteet 
    print(f"Pisteiden keskiarvo: {pisteiden_keskiarvo / laskuri }")


def hyväksymisprosentti(luvut, har_pisteet):
    pisteet = luvut[0]
    harjoitukset = luvut[1]
    laskuri = luvut[2]
    harjoitukset_luvut = luvut[3]
    kaikki_pisteet = luvut[4]
   
    kaikki_har_pisteet = 0
    harjoitus = 0

    for x in har_pisteet:
        kaikki_har_pisteet += x
    
    for c in harjoitukset_luvut:
        harjoitus += c /100
       
    kaikki = pisteet + kaikki_har_pisteet
    
    hyväksymis_prosentti =  harjoitus

    if pisteet <= 10:
        hyväksymis_prosentti = 0.0

    print(f"Hyväksymisprosentti: {hyväksymis_prosentti*100}")

def arvosanajakauma(luvut, har_pisteet):
    kaikki_pisteet_har = luvut[4]
    pisteet = luvut[0]
    laskuri = luvut[2]
    pisteiden_keskiarvo = 0
    # kaikki_pisteet_har = 0
    keskiarvot = []
    for x in kaikki_pisteet_har:
        for i in har_pisteet:
            pisteiden_keskiarvo += x
            pisteiden_keskiarvo += i
        jako = pisteiden_keskiarvo / laskuri 
        keskiarvot. append(jako)
        pisteiden_keskiarvo = 0
    
    print("Arvosanajakauma:")                 
    viisi = "5:"
    neljä = "4:"
    kolme = "3:"
    kaksi = "2:"
    yksi =  "1:"
    nolla = "0:"
    
    for z in keskiarvot:
        # print(z)
        if z < 15:
            nolla += " *"
        if z > 14 and z < 18:
            yksi += " *" 
        if z > 17 and z < 21:
            kaksi += " *"
        if z > 20 and z < 24:
            kolme += " *"
        if z > 23 and z < 28:
            neljä += " *"
        if z > 27 and z < 31:
            viisi += " *"        
    print(viisi)
    print(neljä)
    print(kolme)
    print(kaksi)
    print(yksi)
    print(nolla)
    
        

def main():
    syötteet = luvut()
    har_pisteet = harjoituspisteet(syötteet)
    keskiarvo(syötteet, har_pisteet)
    hyväksymisprosentti(syötteet, har_pisteet)
    arvosanajakauma(syötteet, har_pisteet)
main()

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
    laskuri = luvut[2]
    pisteet = luvut[0]
    harjoitukset = luvut[3]
    for i in harjoitukset:
        pass
    kaikki_pisteet = luvut[4]
    maksimi_pistemäärä = []
    pist = 0
    har = 0
    maksimi_pistemäärä_luku = 0
    kaikki_har_pisteet = 0
    kaikki = 0
    n = 0
    j = 0
    # tässä ongelma
    while n < laskuri:
        n += 1    
        for x in har_pisteet:
            pist += x
            kaikki_har_pisteet += x
        for i in kaikki_pisteet:
            pist += i
        for c in harjoitukset:
            har += c
            j = har/pist        
        maksimi_pistemäärä.append(j)
        pist = 0
        har = 0
                

    

    print(maksimi_pistemäärä)

    for q in maksimi_pistemäärä:
        maksimi_pistemäärä_luku += q
    
    print(maksimi_pistemäärä_luku*100)

    # kaikki = pisteet + kaikki_har_pisteet

    # hyväksymis_prosentti = maksimi_pistemäärä_luku / kaikki 
    
    # print(f"Hyväksymisprosentti: {hyväksymis_prosentti*100}")

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
        print(z)
        if z <= 14:
            nolla += "*"
        if z >= 15 and z <= 17:
            yksi += "*" 
        if z >= 16 and z <= 20:
            kaksi += "*"
        if z >= 21 and z <= 23:
            kolme += "*"
        if z >= 24 and z <= 27:
            neljä += "*"
        if z >= 28:
            viisi += "*"        
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

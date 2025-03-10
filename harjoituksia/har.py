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

    return luvut

def harjoituspisteet(luvut):
    harjoitukset = luvut[3]
    harjoitus_pisteet = []
    for i in harjoitukset:
        luku = int(i)
        piste = luku // 10
        harjoitus_pisteet.append(piste)
    
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
    kaikki_pisteet = luvut[4]
    
    hyväksytyt = 0
    hylätty = 0
    
        
    for i in kaikki_pisteet:
        if i >= 10:
            hyväksytyt += 1 
        else:
            hylätty += 1


    # print(hylätty, hyväksytyt)
        
    
    hyväksymis_prosentti = ((hyväksytyt/laskuri) * 100) 
    
    print(f"Hyväksymisprosentti: {round(hyväksymis_prosentti, 1)}")


def arvosanajakauma(luvut, har_pisteet):
    kaikki_pisteet = luvut[4]
    laskuri = luvut[2]
    
    pisteiden_keskiarvo = 0
    jako = 0
    k = []
    h = []
    arvot = []

    print("Arvosanajakauma:")                 
    viisi = "5: "
    neljä = "4: "
    kolme = "3: "
    kaksi = "2: "
    yksi =  "1: "
    nolla = "0: "

    for i in har_pisteet:
        h.append(i)
    
    for x in kaikki_pisteet:
        if x <= 9:
            pisteiden_keskiarvo += 0         
        else:
            pisteiden_keskiarvo += x         
        jako = pisteiden_keskiarvo 
        k.append(jako)
        pisteiden_keskiarvo = 0
    
    for p in range(len(h)):
        for z in range(len(k)):
            if z == p:
                arvo = h[p] + k[z]
                arvot.append(arvo)

    for q in arvot:
        # print(q)
        if q <= 14:
            nolla += "*"
        elif q >= 15 and q <= 17:
            yksi += "*"
        elif q >= 18 and q <= 20:
            kaksi += "*"
        elif q >= 21 and q <= 23:
            kolme += "*"
        elif q >= 24 and q <= 27:
            neljä += "*"           
        elif q >= 28:
            viisi += "*"
    print(viisi)
    print(neljä)
    print(kolme)
    print(kaksi)
    print(yksi)
    print(nolla)

syötteet = luvut()
har_pisteet = harjoituspisteet(syötteet)
keskiarvo(syötteet, har_pisteet)
hyväksymisprosentti(syötteet, har_pisteet)
arvosanajakauma(syötteet, har_pisteet)



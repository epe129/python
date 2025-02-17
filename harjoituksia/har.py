# Kirjoita ratkaisu tähän
def luvut():
    luvut = []
    harjoitukset_luvut = []
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
        harjoitukset_luvut.append(har)
        laskuri += 1
    luvut.append(pisteet)
    luvut.append(harjoitukset)
    luvut.append(laskuri)
    luvut.append(harjoitukset_luvut) 
    print("Tilasto:")
    # print(luvut)
    return luvut

def harjoituspisteet(luvut):
    harjoitukset = luvut[3]
    harjoitus_pisteet = 0
    for i in harjoitukset:
        # print(i)
        if i == 0:
            continue
        elif i == 10:
            harjoitus_pisteet += 1
        elif i == 20 or i <= 25:
            harjoitus_pisteet += 2
        elif i == 30 or i <= 35:
            harjoitus_pisteet += 3
        elif i == 40 or i <= 45:
            harjoitus_pisteet += 4
        elif i == 50 or i <= 55:
            harjoitus_pisteet += 5
        elif i == 60 or i <= 65:
            harjoitus_pisteet += 6
        elif i == 70 or i <= 75:
            harjoitus_pisteet += 7
        elif i == 80 or i <= 85:
            harjoitus_pisteet += 8
        elif i == 90 or i <= 95:
            harjoitus_pisteet += 9
        elif i == 100:
            harjoitus_pisteet += 10
    # print(harjoitus_pisteet)
    
    return harjoitus_pisteet
     

def keskiarvo(luvut, har_pisteet):
    pisteet = luvut[0]
    laskuri = luvut[2]
    pisteiden_keskiarvo = har_pisteet +  pisteet 
    print(f"Pisteiden keskiarvo: {pisteiden_keskiarvo / laskuri }")


def hyväksymisprosentti(luvut):
    pisteet = luvut[0]
    harjoitukset = luvut[1]
    laskuri = luvut[2]
    hyväksymis_prosentti = harjoitukset + pisteet / laskuri
    print(f"Hyväksymisprosentti: {hyväksymis_prosentti}")

def arvosanajakauma(luvut):
    print(print(""""Arvosanajakauma:
                5:
                4:
                3:
                2:
                1: """))

def main():
    syötteet = luvut()
    har_pisteet = harjoituspisteet(syötteet)
    keskiarvo(syötteet, har_pisteet)
    hyväksymisprosentti(syötteet)
    arvosanajakauma(syötteet)
main()

# opiskelija rekisteri

def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    opiskelijat[nimi].append(suoritus)
    nähty = {}
    for c,x in opiskelijat.items():
        for a in x:
            q,w = a
            if q not in nähty and w > 0:
                nähty[q] = w
        if q in nähty:
            edlli=w
            e = q
            for avain,w in nähty.items():
                if w > edlli and avain == e:
                    nähty[q] = w
                if w < edlli and avain == e:
                    nähty[q] = edlli                
        else:
            pass



def tulosta(opiskelijat: dict, nimi: str):
    if nimi not in opiskelijat:
        print(f"ei löytynyt ketään nimellä {nimi}") 
    for avain, arvot in opiskelijat.items():
        if avain == nimi:
            print(f"{avain}:")
            if arvot == "":
                print(" ei suorituksia")
            else:
                nähdytArvot = {}
                keskiarvo = 0
              
                
                for avain2,arvot2 in arvot:
                    nähdytArvot[avain2] = arvot2
                suoritukset = len(nähdytArvot)
                
                for a,s in nähdytArvot.items():
                    keskiarvo += s
              
                if suoritukset == 0:
                    print(" ei suorituksia")
                else:
                    print(f" suorituksia {suoritukset} kurssilta:") 
                
                for a,s in nähdytArvot.items():
                    print(f"  {a} {s}")
                
                if keskiarvo == 0:
                    pass
                else:
                    print(f" keskiarvo {keskiarvo/len(nähdytArvot)}")
                
   

def kooste(opiskelijat: dict):
    print(f"opiskelijoita {len(opiskelijat)}")
    edellinen = 0
    keskiarvot = {}
    summa = 0
    e = 0
    for avaint,arvot in opiskelijat.items():
        if len(arvot) > edellinen:
            edellinen = len(arvot)
        for nimi,numero in arvot:
            summa += numero
        keskiarvot[avaint] = summa
        summa = 0
    for w,i in keskiarvot.items():
        if i > e:
            e = i
    print(f"eniten suorituksia",len(arvot),avaint)
    print("paras keskiarvo",i/len(arvot) ,w)
        

if __name__=="__main__":
    opiskelijat = {}
    lisaa_opiskelija(opiskelijat, "emilia")
    lisaa_opiskelija(opiskelijat, "pekka")
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 4))
    lisaa_suoritus(opiskelijat, "emilia", ("ohpe", 5))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 3))
    lisaa_suoritus(opiskelijat, "pekka", ("lama", 0))
    lisaa_suoritus(opiskelijat, "pekka", ("tira", 2))
    lisaa_suoritus(opiskelijat, "pekka", ("jtkt", 1))
    lisaa_suoritus(opiskelijat, "pekka", ("ohtu", 3))
    kooste(opiskelijat)
    print(opiskelijat)


# sudoku oikein

def sudoku_oikein(sudoku: list):
    rv = 0
    sk = 0
    
    paikat = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    
    for z in paikat:
        laskuri = 0
        nelio = []
        nähty = []
        rv,sk = z
        # print(rv, sk)       
        if sk == 0:
            pituus = 3
        else:
            pituus = sk
        for rivi1 in range(len(sudoku)):
            if rivi1 == rv:
                for x in range(len(sudoku[rivi1])):
                    nelio.append(sudoku[rivi1][x])
                    while pituus <= sk*2 - 1:
                        pituus += 1
                # print(nelio[sk:pituus])
                for numerot in nelio[sk:pituus]:
                    if numerot == 1 or numerot == 2 or numerot == 3 or numerot == 4 or numerot == 5 or numerot == 6 or numerot == 7 or numerot == 8 or numerot == 9:
                        if numerot in nähty:
                            return False
                        else: 
                            nähty.append(numerot)
                nelio.clear()
                nähty.clear()
                rv += 1
                laskuri += 1
                if laskuri == 3:
                    break

    riviNähty = [] 
    for i in range(9):
        for rivi in sudoku[i]:
            # print(rivi)
            if rivi in riviNähty:
                return False
            else:
                riviNähty.append(rivi)
        riviNähty.clear()
        
    
    sarakeNähty = []
    for c in range(9):
        for x in range(9):
            sarake = sudoku[x][c]
            if sarake in sarakeNähty:
                return False
            else:
                sarakeNähty.append(sarake)
        sarakeNähty.clear()
        
 
    return True




if __name__=="__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_oikein(sudoku))              

# reseptin haku

# tee ratkaisu tänne
def hae_nimi(tiedosto: str, sana: str):
    resepti = []
    with open(tiedosto) as tiedosto2:
        for i in tiedosto2:
            i = i.replace("\n", "")
            if sana.lower() in i.lower():
                resepti.append(i)
            else:
                continue
    return resepti

def hae_aika(tiedosto: str, aika: int):
    resepti = []
    ajat = []
    nimi = ""
    with open(tiedosto) as tiedosto2:
        for i in tiedosto2:
            i = i.replace("\n", "")
            resepti.append(i)
            try:
                ajat.append(int(i))
                below = max([x for x in ajat if aika > x])           
                for c in resepti:
                    if c.isdigit():
                        continue
                    # print(c)
                    nimi += c            
            except:
                continue    
    
    return f"{nimi}, valmistumisaika {below}"

def hae_raakaaine(tiedosto: str, aine: str):
    pass

if __name__ == "__main__":
    # loydetut = hae_nimi("reseptit1.txt", "pulla")
    loydetut = hae_aika("reseptit1.txt", 20)
    # loydetyt = hae_raakaaine("reseptit1.txt", "maito")

    for resepti in loydetut:
        print(resepti, end="")

# kaupunkipyörät

import math

def hae_asematiedot(tiedosto: str):
    sanakirja = {}
    with open(tiedosto) as tiedot:
        for rivi in tiedot:
            osat = rivi.split(';')
            if osat[3] == "name":
                continue
            sanakirja[osat[3]] = (osat[0], osat[1])
        
    return sanakirja

def etaisyys(asemat: dict, asema1: str, asema2: str):
    for nimi,arvo in asemat.items():
        if nimi == asema1:
            longitude1 = float(arvo[0])
            latitude1 = float(arvo[1])
            # print(nimi, longitude1, latitude1)
        if nimi == asema2:
            longitude2 = float(arvo[0])
            latitude2 = float(arvo[1])
            # print(nimi, longitude2, latitude2)
    x_kilometreina = (longitude1 - longitude2) * 55.26
    y_kilometreina = (latitude1 - latitude2) * 111.2
    etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
    
    return etaisyys

def suurin_etaisyys(asemat: dict):
    for c in asemat:
        toka = c
        print(toka)
    #     if c:
    #         longitude1 = float(a[0])
    #         latitude1 = float(a[1])
    #         # print(c, longitude1, latitude1)
    #     if c:
    #         longitude2 = float(a[0])
    #         latitude2 = float(a[1])
    #         # print(c, longitude2, latitude2)
    # x_kilometreina = (longitude1 - longitude2) * 55.26
    # y_kilometreina = (latitude1 - latitude2) * 111.2
    # etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)
            
    return "asd", "ad", etaisyys

if __name__=="__main__":
    asemat = hae_asematiedot('stations1.csv')
    # print(asemat)
    e = etaisyys(asemat, "Designmuseo", "Hietalahdentori")
    # print(e)
    e = etaisyys(asemat, "Viiskulma", "Kaivopuisto")
    # print(e)
    asema1, asema2, suurin = suurin_etaisyys(asemat)
    print(asema1, asema2, suurin)

# paivakirja

# tee ratkaisu tänne
def paivakirja():
    while True:
        sijainti = "paivakirja.txt"
        valinta = int(input("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta: "))
        if valinta == 1:
            with open(sijainti, "a") as tiedosto:            
                # print(f"Valinta:{valinta}")
                merkinta = input("Anna merkintä: ") 
                tiedosto.write(f"{merkinta}\n")
                print("Päiväkirja tallennettu")
                print()
        elif valinta == 2:
            # print(f"Valinta:{valinta}")
            print("Merkinnät:")
            f = open(sijainti)
            print(f.read(), end="")
        elif valinta == 0:
            # print(f"Valinta: {valinta}")
            print("Heippa!")
            break

paivakirja()

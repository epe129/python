# tee ratkaisu tänne
import re

def suorita(ohjelma):
    endKomento = False
    palautus = []
    muuttujat = {}
    alusta = True
    KäydytKomennot = []
    o = ohjelma
    laskuri = 0
    
    if len(ohjelma) == 0:
        return []
    
    for d in ohjelma:
        if "MOV" in d:
            KäydytKomennot.append(d)
                        
        if ":" in d and "JUMP" not in d:
            teksti = ""
            for t in d:
                if ":" in t:
                    continue
                teksti += t
            KäydytKomennot.append(teksti)

        if "PRINT" in d:
            KäydytKomennot.append(d)
                
        if "ADD" in d:
            KäydytKomennot.append(d)
            
        if "IF" in d:
            KäydytKomennot.append(d)
            
        if "SUB" in d:
            KäydytKomennot.append(d)

        if "MUL" in d:
            KäydytKomennot.append(d)

        if "JUMP" in d and "IF" not in d:
            KäydytKomennot.append(d)

        if "END" in d:
            endKomento = True
            KäydytKomennot.append(d)

    
    for c in KäydytKomennot:
        if c == KäydytKomennot[-1]:
            laskuri += 1   

    while alusta:
        for i, komennot in enumerate(o):
        
            if "PRINT" in komennot:
                PRINT(komennot, muuttujat, palautus)   
    
            if "MOV" in komennot:
                MOV(komennot, muuttujat)
                    
            if "ADD" in komennot:
                ADD(komennot, muuttujat, palautus)
               
            if "IF" in komennot:
                p = komennot.split()
                välimerkki = p[2]
                for avain, arvo in muuttujat.items():
                    if p[1] in avain:
                        if arvo in muuttujat.keys():
                            arvo = muuttujat[arvo]
                        eka = arvo
                    if p[3] in avain:
                        if arvo in muuttujat.keys():
                            arvo = muuttujat[arvo]
                        toka = arvo
                if p[1] not in muuttujat.keys():
                    eka = p[1]

                if p[3] not in muuttujat.keys():
                    toka = p[3]
                
                if välimerkki == "==":
                    if int(eka) == int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                    
                elif välimerkki == "!=":
                    if int(eka) != int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                    
                elif välimerkki == "<":
                    if int(eka) < int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                                
                    
                elif välimerkki == ">":
                    if int(eka) > int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                    
                elif välimerkki == "<=":
                    if int(eka) <= int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                   
                       
                elif välimerkki == ">=":
                    if int(eka) >= int(toka):
                        if p[5] in KäydytKomennot:
                            x = KäydytKomennot.index(p[5])
                            while i != x:
                                if x > i:
                                    i += 1
                                else:
                                    i -= 1
                            if i == x:
                                o = ohjelma[x:]
                                break
                    
            
            if "SUB" in komennot:
                SUB(komennot, muuttujat, palautus)

            if "MUL" in komennot:
                MUL(komennot, muuttujat, palautus)


            if "JUMP" in komennot and "IF" not in komennot:
                a = komennot.split()
                if a[1] in KäydytKomennot:
                    x = KäydytKomennot.index(a[1])
                    while i != x:
                        if x > i:
                            i += 1
                        else:
                            i -= 1
                    if i == x:
                        o = ohjelma[x:]
                        break
            
            # print(i)

            if "END" == komennot:
                return palautus
            
            if laskuri == 2 and len(palautus) <= 2:
                continue
            elif KäydytKomennot[-1] == komennot:
                return palautus


def MOV(komennot, muuttujat):
    muuttuja = komennot.split()
    kirjaimet = re.findall("[A-Z]", muuttuja[1])
    # print(muuttuja)
    if muuttuja[1] in kirjaimet:
        nimi = muuttuja[1] 
        if muuttuja[2] in muuttujat.keys():
            for avain, arvo2 in muuttujat.items():
                if muuttuja[2] == avain:
                    arvo = int(arvo2)     
        else:
            arvo = int(muuttuja[2])

    muuttujat[nimi] = int(arvo)

def PRINT(komennot, muuttujat, palautus):
    a = komennot.split()
    for avain, arvo in muuttujat.items():
        if a[1] in avain:
            palautus.append(int(arvo))
    if a[1] not in muuttujat.keys():
        try:
            palautus.append(int(a[1]))
        except:            
            palautus.append(0)

            

def ADD(komennot, muuttujat, palautus):
    a = komennot.split() 
    for avain, arvo in muuttujat.items():
        if a[1] in avain:
            if a[2] not in muuttujat.keys():
                muuttujat[avain] += int(a[2])
                break    
            muuttujat[avain] += muuttujat[a[2]]
            break
    if a[1] not in avain:
        muuttujat[a[1]] = int(a[2])
        

     
def SUB(komennot, muuttujat, palautus):
    a = komennot.split() 
    for avain, arvo in muuttujat.items():
        if a[1] in avain:
            if a[2] not in muuttujat.keys():
                muuttujat[avain] -= int(a[2])
                break    
            muuttujat[avain] -= muuttujat[a[2]]
            break

def MUL(komennot, muuttujat, palautus):
    a = komennot.split() 
    for avain, arvo in muuttujat.items():
        if a[1] in avain:
            if a[2] not in muuttujat.keys():
                muuttujat[avain] *= int(a[2])
                break    
            muuttujat[avain] *= muuttujat[a[2]]
            break
        
        
if __name__=="__main__":
    ohjelma4 = []
    ohjelma4.append("MOV A 1")
    ohjelma4.append("MOV B 1")
    ohjelma4.append("alku:")
    ohjelma4.append("PRINT A")
    ohjelma4.append("MUL A 2")
    ohjelma4.append("ADD B 1")
    ohjelma4.append("IF B != 101 JUMP alku")
    ohjelma4.append("PRINT A")
    tulos = suorita(ohjelma4)
    print(tulos)
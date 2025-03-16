# tee ratkaisu tänne

def lisaa_opiskelija(opiskelijat: dict, nimi: str):
    opiskelijat[nimi] = []

def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
    suoritukset = []
    suoritukset.append(suoritus)
    for i in suoritukset:
        aine, numero = i
        if numero == 0:
            del i
        else:
            opiskelijat[nimi].append(i)
        
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
                lukuja = 0
                
                for avain2,arvot2 in arvot:
                    keskiarvo += arvot2
                    lukuja += 1
                    nähdytArvot[avain2] = arvot2
                suoritukset = len(nähdytArvot)
                
                if suoritukset == 0:
                    print(" ei suorituksia")
                else:
                    print(f" suorituksia {suoritukset} kurssilta:") 
                
                for a,s in nähdytArvot.items():
                    print(f"  {a} {s}")
                
                if keskiarvo == 0:
                    pass
                else:
                    print(f" keskiarvo {keskiarvo/lukuja}")
                
   

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
    tulosta(opiskelijat, "emilia")
    tulosta(opiskelijat, "pekka")
    print(opiskelijat)
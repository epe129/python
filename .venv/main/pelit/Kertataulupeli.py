# voit harjoitellaa haluamaasi kertataulua

import random
import fontstyle # käyetään että saadaa hieno fontti alkutekstiin

def kertatauluPeli():
    try:
        t = True
        while t:
            oikein = 0
            väärin = 0
            
            print("------------------------------------------------------------------------")
            
            alkuTeksti = fontstyle.apply("""Tervetuloa kertataulu peliin, voit harjoitella haluamaasi kertotaulua. 
    kierroksia pitää laittaa vähintään kaksi, jos on vähemmän laittaa automaattisesti kaksikierrosta.""", 'bold/Italic')
            print(alkuTeksti)
            
            print("------------------------------------------------------------------------")
            m = input("Mitä kertsataulua haluaisit harjoitella?: ")
            
            print("-------------------------------------------------")
            k = int(input("kuinka monta kierrosta haluaisi harjoitella? "))
            print("-------------------------------------------------")
            
            k = 2 if int(k) < 2 else k
                
            kk = k
            
            while k > 0:
                k -= 1 

                r = random.randint(1, 10)
                
                ov = int(r) * int(m)

                a = random.randint(1, 4)
                
                if a == 1 or a == 3:
                    v = input(f"Paljon on {r} * {m}: ") 
                else:
                    v = input(f"Paljon on {m} * {r}: ")

                print("-------------------------------------------------")
                
                
                if int(v) == int(ov):
                    oikein += 1
                else:
                    väärin += 1

            if oikein >= 1:
                prosentteina = (float(oikein)/float(kk)) * 100
            else:
                prosentteina = 0.0
            print(f"Oikein meni {kk}/{oikein}, Prosentteina {prosentteina:.1f}. Väärin meni {kk}/{väärin}")
            print("-------------------------------------------------")
            
            jatkaa = input("Haluatko jatkaa kertataulujen opiskelua(kyllä/ei): ").lower()
            
            if jatkaa == "kyllä":
                continue
            else:
                t = False
                print("-------------------------------------------------")
                print("Heippa, toivotaan että nähdään uudestaan")
                break
    except:
        print("Jokin meni pieleen")
        input("Paina enter aloitaaksesi alusta: ")
        kertatauluPeli()

if __name__ == "__main__":
    kertatauluPeli()
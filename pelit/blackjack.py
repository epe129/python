import random

try:
    def blackjack():
        global KäyttäjänNumero
        global JakaNumero

        KäyttäjänNumero = random.randint(2, 9)
        JakaNumero = random.randint(2, 9)
        
        print("Tervetuloa blackjack tapaiseen peliin jos haluat voittaa sinun on saatava 21 tai enenmmän kuin jakaja. Mutta ei saa mennä yli 21.")
        print("-----------------------")
        
        str(input("Paina Enter jatkaaksesi: "))
        print("-----------------------")
        
        print(f"Jakan numero on {JakaNumero}")
        print("-----------------------")
        
        print(f"Sinun numero on {KäyttäjänNumero}: ")
        print("-----------------------")

    def korotus():
        global KäyttäjänNumero
        global JakaNumero
        KorotusMäärä2 = random.randint(2, 9)
        JakaNumero += KorotusMäärä2
        print(f"Jakaja korotta numeroaan {JakaNumero}")
        print("-----------------------")
        kortukset = True
        while kortukset:
            Korottaa = str(input("Haluatko korottaa numeroasi? (kyllä/ei): "))
            print("-----------------------")
            if JakaNumero < 10:
                KorotusMäärä3 = random.randint(2, 9)
                JakaNumero += KorotusMäärä3
                print(f"Jakaja korotta numeroaan {JakaNumero}")
                print("-----------------------")
            elif JakaNumero < 12:
                KorotusMäärä4 = random.randint(2, 9)
                JakaNumero += KorotusMäärä4
                print(f"Jakaja korotta numeroaan {JakaNumero}")
                print("-----------------------")
            elif JakaNumero < 15:
                KorotusMäärä5 = random.randint(2, 9)
                JakaNumero += KorotusMäärä5
                print(f"Jakaja korotta numeroaan {JakaNumero}")
                print("-----------------------")

            if Korottaa == "kyllä":
                KorotusMäärä = random.randint(2, 9)
                KäyttäjänNumero += KorotusMäärä
                print(f"Jakan numero on {JakaNumero}")
                print("-----------------------")
                
                print(f"Sinun numero on {KäyttäjänNumero}: ")
                print("-----------------------")
            else:
                Voittaja()
                kortukset = False


            if KäyttäjänNumero > 21:
                print(f"Hävisit sinulla meni yli, {KäyttäjänNumero}, jakalalla oli {JakaNumero}")
                break
            elif JakaNumero > 21:
                print(f"Voitit, {KäyttäjänNumero}. jakalalla meni yli, {JakaNumero}")
                break
            
    def Voittaja():
        if KäyttäjänNumero > JakaNumero:
            print(f"Voitit sinulla oli {KäyttäjänNumero}, jakalla oli {JakaNumero}")
        elif JakaNumero > KäyttäjänNumero:
            print(f"Hävisit sinulla oli {KäyttäjänNumero}, jakajalla oli {JakaNumero}")

    def kysy():
        print("-----------------------")
        k = str(input("Haluatko pelata uudelleen? (kyllä/ei): "))
        print("-----------------------")
        if k == "kyllä":
            main()
        else:
            print("heippa") 

    def main():
        if __name__ == "__main__":
            blackjack()
            korotus()
            kysy() 
    main()   
except:
    print("Jokin meni pieleen")
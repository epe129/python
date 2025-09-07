# All the task are form this page:
# https://adriann.github.io/programming_problems.html

def SuurinLukuList():
    # Kirjoita funktio, joka palauttaa luettelon suurimman elementin.
    list = [23,43,41,4123,12,3412,412,432,4,324,234,324,23,432,43]
    k = 0
    for i in list:
        if i > k:
            k = i
    print(k)

# SuurinLukuList()

def KääntääList():
    # Kirjoita toiminto, joka kääntää luettelon, mieluiten paikallaan
    list = [23,43,41,4123,12,3412,412,432,4,324,234,324,23,432,43]
    list.reverse()
    print(list)

# KääntääList()

def EsiinTyykö():
    # Kirjoita funktio, joka tarkistaa, esiintyykö jokin elementti luettelossa
    etsi = str(input("Anna sana jota etsit listasta: "))
    list = ["kissa","koira","paska","huora"]
    for i in list:
        if etsi == i:
            print(i)
            break
    if etsi != i:
        print("ei ole")
# EsiinTyykö()

def parittomat():
    # Kirjoita funktio, joka palauttaa luettelon parittomien paikkojen elementit
    list = [23,43,41,4123,12,3412,412,432,4,324,234,324,23,432,43]
    for i in range(len(list)):
        # print(i)
        if i % 2 != 0:
            # print(i)
            print(list[i])
# parittomat()

def kokonaisSumma():
    # Kirjoita funktio, joka laskee luettelon käynnissä olevan kokonaissumman
    a = 0
    list = [23,43,41,4123,12,3412,412,432,4,324,234,324,23,432,43]
    # list = [23,43]
    for i in list:
        a += i
    print(a)
# kokonaisSumma()

def palidrom():
    # Kirjoita funktio, joka testaa, onko merkkijono palindromi
    merkki = str(input("Anna merkkijono: "))
    kaannettu = merkki[::-1]
    if merkki == kaannettu or kaannettu == merkki:
        print(merkki)
        print(kaannettu)
        print(True)
    else:
        print(merkki)
        print(kaannettu)
        print(False)
# palidrom()

def YhdistäList():
    # Kirjoita funktio, joka yhdistää kaksi luetteloa. [a,b,c] [1,2,3] → [a,b,c,1,2,3]
    sana = input("Anna sana tai numero")
    list = [1,2,3,4,5,6]
    list.append(sana)
    list2 = ["m","l","o"]
    list3 = list + list2
    print(list3)

# YhdistäList()

def Vuorotellen():
    # Kirjoita funktio, joka yhdistää kaksi luetteloa ottamalla vuorotellen elementtejä, esim. [a,b,c] [1,2,3] → [a,1,b,2,c,3]
    list = [1,2,3,4,5,6]
    list2 = ["m","l","o"]
    list3 = []
    pituus = min(len(list) , len(list2))
    for i in range(pituus):
        list3.append(list[i])
        list3.append(list2[i])
    list3 += list[pituus:] + list2[pituus:]
    print(list3)

# Vuorotellen()

def lajittele():
    # Kirjoita funktio, joka yhdistää kaksi lajiteltua luetteloa uuteen lajiteltuun luetteloon. → . Voit tehdä tämän nopeammin kuin niiden yhdistäminen, jota seuraa eräänlainen.[1,4,6][2,3,5][1,2,3,4,5,6]
    list = [1,2,3,4,5,6]
    list2 = [12,55,11,10,9,8,7]
    list3 = list + list2
    list3.sort()
    print(list3)
# lajittele()


# Kirjoita funktio, joka kiertää luetteloa k elementit. 
# Esimerkiksi [1,2,3,4,5,6] pyöritetään kahdella tulee [3,4,5,6,1,2]. 
# Yritä ratkaista tämä luomatta kopiota luettelosta. 
# Kuinka monta swap tai siirtää toimintaa tarvitset?

k = [1,2,3,4,5,6]
def rotate(l, n):
    return l[n:] + l[:n]

# print(rotate(k, 2))

# Kirjoita funktio, joka laskee luettelon 100 ensimmäisestä Fibonacci-numerosta. Kaksi ensimmäistä Fibonaccin lukua ovat 1 ja 1. 
# The n+1-st Fibonacci numero voidaan laskea lisäämällä n- ja n-1- Fibonaccin numero. Ensimmäiset harvat ovat siis 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.
def Fibonacci():
    n = 10
    n1 = 0
    n2 = 1
    c = 0
    while c < n:
        print(n1)
        next = n1 + n2
        n1 = n2
        n2 = next
        c += 1

# Kirjoita funktio, joka ottaa numeron ja palauttaa luettelon sen numeroista. Joten 2342 sen pitäisi palata [2,3,4,2].
def LuetteloNumero():
    nelja = int(input("Anna numeroita: "))
    # nelja = 2342
    list = []
    for i in str(nelja):
        list.append(i)

    print(list)

# LuetteloNumero()

# Kirjoita funktio, joka ottaa luettelon merkkijonoista, tulostaa ne suorakulmaiseen kehykseen yksi riviä kohti. 
# Esimerkiksi luettelo ["Hello", "World", "in", "a", "frame"] tulostetaan seuraavasti:

# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********
def suorakulmainenKehys():
    list = ["Hello", "World", "in", "a", "frame", "perkele"] 
    for x in list:
        size = len(x)
    print("*" * (size + 4))
    for i in list:
        print('* {:<7} *'.format(i))
    print("*" * (size + 4))
# suorakulmainenKehys()



# KESKEN
# Kirjoita ohjelma, joka tuottaa kaikki mahdollisuudet laittaa + tai - tai ei mitään numeroiden 1,2,...,9 (tässä järjestyksessä) välillä siten, että tulos on 100.
#  Esimerkiksi 1 + 2 + 3 - 4 + 6 78 µg (100).
def PlusMiinus():
    lasku = 0
    l = int(input("Anna luku väliin: "))
    lasku = lasku +  l
    for i in range(1,9):
        lasku += i
    while lasku < 100:
        lasku += 1
        if lasku == 100:
            print(lasku)
    while lasku > 100:
        lasku -= 1
        if lasku == 100:
            print(lasku)
# PlusMiinus()

# Kirjoita toiminto, joka kääntää tekstin sika latinaksi ja takaisin.
# Englanti käännetään sikalatinaksi ottamalla jokaisen sanan ensimmäinen kirjain, 
# siirtämällä se sanan loppuun ja lisäämällä (ay). 
# “Nopeasta ruskeaketusta) tulee ” Hetay uickqay rownbay oxfay).
# Olen ottanut netistä koodin
def main():
    lause = str(input("Anna lause englanniksi jonka haluat kääntää sika-latinaksi: ")).split()
    for sana in lause:
        print(sana[1:] + sana[0] + "ay", end = " ")
    print ()

# main()

def yhtäSuuri():
    num1 = 2
    num2 = "2"
    if num1 == num2:
        return True
    else:
        return False


# print(yhtäSuuri())





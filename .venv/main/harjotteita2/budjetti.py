# Henkilökohtainen budjetti
# Tee sovellus, joka auttaa käyttäjää seuraamaan tuloja ja menoja. Käyttäjä voi lisätä tuloja ja kuluja, ja ohjelma näyttää kuukausittaisen budjetin ja mahdolliset säästöt.

def TulotJaMenot():
    kaikkiTulot = 0
    tulo = True
    menot = False
    while tulo:
        tulot = int(input("Anna kaikki tulot: "))
        kaikkiTulot += tulot
        onko = str(input("Onko vielä tuloja (kyllä/ei): "))
        if onko == "kyllä":
            continue
        else:
            tulo = False
            menot = True
    kaikkiMenot = 0
    while menot:
        m = int(input("Anna kaikki menot: "))
        kaikkiMenot += m
        onko2 = str(input("Onko vielä tuloja (kyllä/ei): "))
        if onko2 == "kyllä":
            continue
        else:
            menot = False
    käteen = kaikkiTulot - kaikkiMenot
    print(f"Tulosi {kaikkiTulot}, Menosi {kaikkiMenot}, Jääkäteen menojen jälkeen {käteen}")


TulotJaMenot()
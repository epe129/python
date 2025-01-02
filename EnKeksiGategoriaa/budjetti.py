# Henkilökohtainen budjetti
# Tee sovellus, joka auttaa käyttäjää seuraamaan tuloja ja menoja. Käyttäjä voi lisätä tuloja ja kuluja, ja ohjelma näyttää kuukausittaisen budjetin ja mahdolliset säästöt.

def TulotJaMenot():
    kaikkiTulot = 0
    while True:
        tulot = int(input("Anna kaikki tulot: "))
        kaikkiTulot += tulot
        onko = str(input("Onko vielä tuloja (kyllä/ei): "))
        if onko == "kyllä":
            continue
        else:
            break
    
    print(kaikkiTulot)


TulotJaMenot()
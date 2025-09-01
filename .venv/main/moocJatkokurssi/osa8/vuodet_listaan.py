# tee ratkaisu tänne
# Muista import-lause:
from datetime import date

def vuodet_listaan(paivamaarat: list):
    paiva_maarat = []
    for c in paivamaarat:
        paiva_maarat.append(c.year)
    paiva_maarat.sort()
    return paiva_maarat


if __name__ =="__main__":
    paiva1 = date(2019, 2, 3)
    paiva2 = date(2006, 10, 10)
    paiva3 = date(1993, 5, 9)

    vuodet = vuodet_listaan([paiva1, paiva2, paiva3])
    print(vuodet)
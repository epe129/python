def sarakkeen_alkioiden_summa(matriisi, sarake_nro: int):
    # summaan lisätään kaikkien rivien halutussa kohdassa oleva alkio
    summa = 0
    for rivi in matriisi:
        summa += rivi[sarake_nro]

    return summa

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

summa = sarakkeen_alkioiden_summa(m, 2)
print(summa) # tulostuu 39 (saadaan laskemalla 3 + 12 + 9 + 15)
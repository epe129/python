# tee ratkaisu tänne
def rivien_summat(matriisi: list):
    summa = 0
    matriisi_numero = 0
    for i in range(len(matriisi)):
        for c in matriisi[i]:
            summa += c

        matriisi[matriisi_numero].append(summa)
        summa = 0
        matriisi_numero += 1


if __name__ == "__main__":
    matriisi = [[1,1],[2,2]]
    rivien_summat(matriisi)
    print(matriisi)
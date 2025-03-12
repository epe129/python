def transponoi(matriisi: list):
    uusilista = []
    laskuri = 0
    a = []
    for i in range(len(matriisi)):
        for c in range(len(matriisi[i])):
            print(f"{matriisi[c][i]} ", end="")
            if i == 0:
                a.append(matriisi[c][i])
                uusilista.append(a)        
        print(" ")
    matriisi[:] = uusilista

if __name__=="__main__":
    matriisi = [[1,2,3],[4,5,6],[7,8,9]]
    transponoi(matriisi)
    print(matriisi)

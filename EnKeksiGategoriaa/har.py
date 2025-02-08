def tekijat(n):
    lista = []
    tekija = 2
    while tekija <= n:
        while n % tekija == 0:
            # print(n)
            n = n // tekija
            print(tekija)
            lista.append(tekija)
        tekija += 1     
    # return lista
    
print(tekijat(6))
print(tekijat(7))
print(tekijat(8))
print(tekijat(980))
print(tekijat(12345))
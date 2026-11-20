toka = 1
while toka < 12:
    toka += 1
    alkuluku = True
    for j in range(2, toka):
        if toka % j == 0:
            alkuluku = False
            break
    if alkuluku:
        print(toka)

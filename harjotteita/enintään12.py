# Kirjoita ohjelma, joka tulostaa kertotaulukon numeroille, jotka ovat enintään 12.
def Kertatailu():
    i = 0
    x = 0
    while i < 10 and x < 10:
        i += 1
        x += 1
        a = i * 2
        b = x * 3
        if a <= 12:
            if b <= 12:
                print(f"|{b:2} ", f" {a:2}|",)
    
Kertatailu()

def k():
    for i in range(11):
        print( f"{i * 1:2} | {i * 2:2} | {i * 3:2} | {i * 4:2} | {i * 5:2} | {i * 6:2} | {i * 7:2} | {i * 8:2} | {i * 9:2} | {i * 10:2}" )
k()

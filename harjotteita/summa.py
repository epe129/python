# Muokkaa edellistä ohjelmaa siten, että vain kolmen tai 
# viiden kerrannaiset otetaan huomioon summassa, esim. 3, 5, 6, 9, 10, 12, 15 n=17

def summa():
    luku1 = int(input("Anna luku: "))
    luku2 = int(input("Anna luku: "))

    if luku1 % 3 == 0 or luku1 % 5 == 0: 
        if luku2 % 3 == 0 or luku2 % 5 == 0 :
            print(luku2 + luku1) 
        else:
            print("En voi laskea yhteen ellei ole 3 tai 5 kerrottava luku.")
    else:
            print("En voi laskea yhteen ellei ole 3 tai 5 kerrottava luku.")

summa()
    
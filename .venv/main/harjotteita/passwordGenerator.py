import random

def generate_password():
    
    pituus = 10
    salasana = ""

    kirjaimet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numerot = ["0","1","2","3","4","5","6","7","8","9"]
    erikoismerkit = ["!","#","$","%","&"]

    for c in range(pituus):
        
        random_kirjain = random.choice(kirjaimet)
        
        random_numerot = random.choice(numerot)
        
        random_erikoismerkit = random.choice(erikoismerkit)
        
        salasana += random_kirjain
        
        if len(salasana) == pituus:
            break

        salasana += random_numerot
        
        if len(salasana) == pituus:
            break
        
        salasana += random_erikoismerkit

        if len(salasana) == pituus:
            break
        
    print(salasana)

generate_password()
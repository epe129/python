import random


def PasswordGenerator():
    Kirjaimet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    Numerot = ["1","2","3","4","5","6","7","8","9","10"]
    Erikoismerkit = ["!","?",",",".","-","#","@","&","$"]
    
    k = random.choices(Kirjaimet, k=5) 
    n = random.choices(Numerot, k=4) 
    e = random.choices(Erikoismerkit, k=2)
    
    password = k + n + e

    random.shuffle(password)
    
    lopullinen = ''.join(password)

    print(lopullinen)
   
        
PasswordGenerator()
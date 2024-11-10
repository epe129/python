
def SalasanaVahvuusTesti(password):
    
    Kirjaimet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","å","ä","ö"]
    IsotKirjaimet= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Å","Ä","Ö"]
    Numerot = ["0","1","2","3","4","5","6","7","8","9"]
    Erikoismerkit = ["!","?",",",".","-","#","@","&","$"]
    YleisimmätSalasanat = ["123456","12345","salasana","qwerty","perkele","123456789","salasana1","paska123","12345678","kakka123","lol123","asdasd","password","asd123","moi123","paska","kakka","qwerty123","1234567","123123"]

    VahvuusLaskuri = 0
    
    
    if len(password) > 7:
        VahvuusLaskuri += 1
    if any(x in Kirjaimet for x in password):
        VahvuusLaskuri += 1
    if any(i in Numerot for i in password):
        VahvuusLaskuri += 1
    if any(z in Erikoismerkit for z in password):
        VahvuusLaskuri += 1
    if any(q in IsotKirjaimet for q in password):
        VahvuusLaskuri += 1
        

    if not len(password) > 7:
        print("Salasanasi on liian lyhyt alle 8 merkkiä")
        print("-------------------------")

    if not any(x in Kirjaimet for x in password):
        print("Salasanassasi ei ole pieniä kirjaimia")
        print("-------------------------")

    if not any(i in Numerot for i in password):
        print("Salasanassasi ei ole numeroita")
        print("-------------------------")

    if not any(z in Erikoismerkit for z in password):
        print("Salasanassasi ei ole erikoismerkkejä")
        print("-------------------------")

    if not any(q in IsotKirjaimet for q in password):
        print("Salasanassasi ei ole isojakirjaimia")
        print("-------------------------")

    for a in YleisimmätSalasanat:
        pass          
    
    if a == password:
        print("Vaihda salasanasi heti ")
    else:
        print(f"5/{VahvuusLaskuri}")
        

            
    
    


print("""Salasanasi tulisi sisältää:
          Vähintääkin 8 merkkiä, mutta enintään 12 merkkiä,
          Erikoismerkkejä,
          Kirjaimia,
          Numeroita""")

print("-------------------------")
    
ass = input("Anna salasanasi jonka vahvuuden haluat tietää: ")    


print("-------------------------")

SalasanaVahvuusTesti(ass)

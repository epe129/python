lintulista = ["metso", "pyy", "teeri", "riekko", "kiiruna"]
mainitut_linnut = []

while True:
    lintu = input("Kerro jokin metsäkanalintu (lopeta lopettaaksesi): ")
    
    if lintu.lower() == "lopeta":
        break
    
    if lintu in lintulista and lintu not in mainitut_linnut:
        mainitut_linnut.append(lintu)
        print("Mainitsit metsäkanalinnun")
    else:
        print("Ei tunneta tai olet jo maininnut tämän linnun.")



        
   



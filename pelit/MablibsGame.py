

def EnsimmäinenLause():
    print("Tervetuloa peliin, sinun pitää laittaa satunnaisia sanoja tarinoiden väliin")
    print("--------------")
    puuttuvasana = ""
    tarina1 = f"""Pieni [--{puuttuvasana}---] löysi metsästä salaperäisen avaimen, joka sopi vanhaan, unohdettuun porttiin. 
               Avaimen kääntäessä portti aukeni, ja sen takaa paljastui maailma, jossa aika pysähtyi ja tähdet loistivat päivällä. 
               Tyttö tiesi löytäneensä paikan, jossa kaikki toiveet voisivat toteutua."""
    print(tarina1)
    puuttuvasana = input("Sukupuoli: ").casefold()
    print("--------------")
    if puuttuvasana == "":
            print("Sinun pitää laittaa jotakin")    
            print("--------------")
            puuttuvasana = input("Sukupuoli: ").casefold()
    
    while True:
        if puuttuvasana == "tyttö" or puuttuvasana == "poika":
            print("oikein")
        else:
            tarina1 = f"""Pieni tyttö löysi metsästä salaperäisen avaimen, joka sopi vanhaan, unohdettuun porttiin. 
                Avaimen kääntäessä portti aukeni, ja sen takaa paljastui maailma, jossa aika pysähtyi ja tähdet loistivat päivällä. 
                Tyttö tiesi löytäneensä paikan, jossa kaikki toiveet voisivat toteutua."""
            print(f"Väärin, oikein oli: {tarina1}")
        
        print("--------------")
        input("Paina enter jatkaaksesi seuraavaan lauseeseen ")
        ToinenLause()
        break


def ToinenLause():
    print("--------------")
    puuttuvasana2 = ""
    tarina2 = f"[{puuttuvasana2}-----] kissa kielen"
    print(tarina2)
    print("--------------")
    puuttuvasana2 = str(input("Suomalainen sanonta: ")).capitalize()
    print("--------------")
    if puuttuvasana2 == "":
            print("Sinun pitää laittaa jotakin")    
            print("--------------")
            puuttuvasana2 = str(input("Suomalainen sanonta: ")).capitalize()
    
    while True:
        if puuttuvasana2 == "Veikö":
            print("oikein")
            break
        else:
            tarina2 = f"Veikö kissa kielen"
            print(f"Väärin, oikein oli: {tarina2}")
            break

EnsimmäinenLause()

def SeuraavatKarkausVuodet():
    luku = 2024
    while luku < 2105:
        if luku % 100 == 0 and luku % 400 == 0:
            print("Vuosi on karkausvuosi.", luku)
        elif luku % 100 == 0:
            print("Vuosi ei ole karkausvuosi.", luku)  
        elif luku % 4 == 0:
            print("Vuosi on karkausvuosi.", luku)
        else:
            print("Vuosi ei ole karkausvuosi.", luku)
        
        
        luku += 1

SeuraavatKarkausVuodet()
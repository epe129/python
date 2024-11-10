#kysyy eri koodikysymyksiä esim mikä on tämän vastaus pow(1,10) ja kolme vaihtoehtoa 1 10 2

def testi():
    kieli = input("Tervetuloa koodaus testiin, valitsekieli josta haluat testin: python, javascript, css, c : ")

    if kieli == "python":
        python()
    elif kieli == "javascript":
        javascript()
    elif kieli == "css":
        css()
    elif kieli == "c":
        c()
    else:
        input("Ei ole kyseinen kieli listassa, paina enter mennäksesi takaisin alkuun: ")
        testi()

def python():
    oikein = 0
    ensimmäinen = input("Mikä Pythonin funktio palauttaa tietyn muuttujan tyypin? a) type() b) len() c) str(): ")
    if ensimmäinen == "a":
        print("Oikein")
        oikein += 1
    elif ensimmäinen == "b" or ensimmäinen == "c":
        print("Väärin oikein oli a) type()")
    print("------------")
    toinen = input('Miten Pythonissa aloitetaan monirivinen kommentti? a) Käyttämällä """ kolmoislainausmerkkejä b) Käyttämällä # joka rivillä c) Käyttämällä // kuten C++: ')
    print("------------")
    if toinen == "a":
        print("Oikein")
        oikein += 1
    elif toinen == "b" or toinen == "c":
        print('Väärin oikein oli a) Käyttämällä """ kolmoislainausmerkkejä')
    print("------------")
    kolmas = input('Mikä seuraavista on oikea tapa luoda lista Pythonissa? a) {1, 2, 3} b) [1, 2, 3] c) (1, 2, 3): ')
    print("------------")
    if kolmas == "b":
        print("Oikein")
        oikein += 1
    elif kolmas == "a" or kolmas == "c":
        print('Väärin oikein oli b) [1, 2, 3]')
    print("------------")
    neljäs = input('Mikä näistä on Pythonissa käytettävä moduuli, kun halutaan käsitellä satunnaislukuja? a) random b) math c) os: ')
    print("------------")
    if neljäs == "a":
        print("Oikein")
        oikein += 1
    elif neljäs == "b" or neljäs == "c":
        print('Väärin oikein oli  a) random')
    print("------------")
    viides = input('Mitä tapahtuu, jos Pythonissa yrittää käyttää muuttujaa, jota ei ole määritelty? a) Funktio palauttaa None b) Python nostaa NameError-virheen c) Python tulostaa "Undefined": ')
    print("------------")
    if viides == "b":
        print("Oikein")
        oikein += 1
    elif viides == "a" or viides == "c":
        print('Väärin oikein oli b) Python nostaa NameError-virheen')
    print("------------")
    kuudes = input('Mikä seuraavista on oikein kirjoitettu silmukka Pythonissa? a) while i <= 10 { print(i) } b) for i in range(10): print(i) c) for (int i = 0; i < 10; i++) { print(i) }: ')
    print("------------")
    if kuudes == "b":
        print("Oikein")
        oikein += 1
    elif kuudes == "a" or kuudes == "c":
        print('Väärin oikein oli b) for i in range(10): print(i) ')
    print("------------")
    seittemäs = input('Mikä funktio muuntaa kokonaisluvun merkkijonoksi Pythonissa? a) int() b) str() c) list(): ')
    print("------------")
    if seittemäs == "b":
        print("Oikein")
        oikein += 1
    elif seittemäs == "a" or seittemäs == "c":
        print('Väärin oikein oli b) str()')
    print("------------")
    kahdeksas = input('Mikä seuraavista Pythonin tietotyypeistä on muuttumaton? a) Lista (list) b) Sanakirja (dict) c) Tuple (tuple): ')
    print("------------")
    if kahdeksas == "c":
        print("Oikein")
        oikein += 1
    elif kahdeksas == "a" or kahdeksas == "c":
        print('Väärin oikein oli  c) Tuple (tuple)')
    print("------------")
    yhdeksäs = input('Mikä komento suorittaa Python-tiedoston komentoriviltä? a) run filename.py b) python filename.py c) start filename.py: ')
    print("------------")
    if yhdeksäs == "b":
        print("Oikein")
        oikein += 1
    elif yhdeksäs == "a" or yhdeksäs == "c":
        print('Väärin oikein oli b) python filename.py')
    print("------------")
    kymmenes = input('Mikä on Pythonissa oikea tapa luoda funktio? a) function my_function() b) def my_function(): c) create my_function(): ')
    print("------------")
    if kymmenes == "b":
        print("Oikein")
        oikein += 1
    elif kymmenes == "a" or kymmenes == "c":
        print('Väärin oikein oli b) def my_function(): ')
    print("-----------")
    print(f"Oikein meni {oikein}/10")
    

def javascript():
    oikein = 0
    ensimmäinen = input("  ")
    if ensimmäinen == "a":
        print("Oikein")
        oikein += 1
    elif ensimmäinen == "b" or ensimmäinen == "c":
        print("")
    print("------------")
    toinen = input(' ')
    print("------------")
    if toinen == "a":
        print("Oikein")
        oikein += 1
    elif toinen == "b" or toinen == "c":
        print('')
    print("------------")
    kolmas = input(' ')
    print("------------")
    if kolmas == "b":
        print("Oikein")
        oikein += 1
    elif kolmas == "a" or kolmas == "c":
        print('')
    print("------------")
    neljäs = input('  ')
    print("------------")
    if neljäs == "a":
        print("Oikein")
        oikein += 1
    elif neljäs == "b" or neljäs == "c":
        print('')
    print("------------")
    viides = input('')
    print("------------")
    if viides == "b":
        print("Oikein")
        oikein += 1
    elif viides == "a" or viides == "c":
        print('')
    print("------------")
    kuudes = input(' ')
    print("------------")
    if kuudes == "b":
        print("Oikein")
        oikein += 1
    elif kuudes == "a" or kuudes == "c":
        print('')
    print("------------")
    seittemäs = input(' ')
    print("------------")
    if seittemäs == "b":
        print("Oikein")
        oikein += 1
    elif seittemäs == "a" or seittemäs == "c":
        print('')
    print("------------")
    kahdeksas = input('   ')
    print("------------")
    if kahdeksas == "c":
        print("Oikein")
        oikein += 1
    elif kahdeksas == "a" or kahdeksas == "c":
        print('')
    print("------------")
    yhdeksäs = input(' ')
    print("------------")
    if yhdeksäs == "b":
        print("Oikein")
        oikein += 1
    elif yhdeksäs == "a" or yhdeksäs == "c":
        print('')
    print("------------")
    kymmenes = input(' )  ')
    print("------------")
    if kymmenes == "b":
        print("Oikein")
        oikein += 1
    elif kymmenes == "a" or kymmenes == "c":
        print(' ')
    print("-----------")
    print(f"Oikein meni {oikein}/10")

def css():
    oikein = 0
    ensimmäinen = input("  ")
    if ensimmäinen == "a":
        print("Oikein")
        oikein += 1
    elif ensimmäinen == "b" or ensimmäinen == "c":
        print("")
    print("------------")
    toinen = input(' ')
    print("------------")
    if toinen == "a":
        print("Oikein")
        oikein += 1
    elif toinen == "b" or toinen == "c":
        print('')
    print("------------")
    kolmas = input(' ')
    print("------------")
    if kolmas == "b":
        print("Oikein")
        oikein += 1
    elif kolmas == "a" or kolmas == "c":
        print('')
    print("------------")
    neljäs = input('  ')
    print("------------")
    if neljäs == "a":
        print("Oikein")
        oikein += 1
    elif neljäs == "b" or neljäs == "c":
        print('')
    print("------------")
    viides = input('')
    print("------------")
    if viides == "b":
        print("Oikein")
        oikein += 1
    elif viides == "a" or viides == "c":
        print('')
    print("------------")
    kuudes = input(' ')
    print("------------")
    if kuudes == "b":
        print("Oikein")
        oikein += 1
    elif kuudes == "a" or kuudes == "c":
        print('')
    print("------------")
    seittemäs = input(' ')
    print("------------")
    if seittemäs == "b":
        print("Oikein")
        oikein += 1
    elif seittemäs == "a" or seittemäs == "c":
        print('')
    print("------------")
    kahdeksas = input('   ')
    print("------------")
    if kahdeksas == "c":
        print("Oikein")
        oikein += 1
    elif kahdeksas == "a" or kahdeksas == "c":
        print('')
    print("------------")
    yhdeksäs = input(' ')
    print("------------")
    if yhdeksäs == "b":
        print("Oikein")
        oikein += 1
    elif yhdeksäs == "a" or yhdeksäs == "c":
        print('')
    print("------------")
    kymmenes = input(' )  ')
    print("------------")
    if kymmenes == "b":
        print("Oikein")
        oikein += 1
    elif kymmenes == "a" or kymmenes == "c":
        print(' ')
    print("-----------")
    print(f"Oikein meni {oikein}/10")

def c():
    oikein = 0
    ensimmäinen = input("  ")
    if ensimmäinen == "a":
        print("Oikein")
        oikein += 1
    elif ensimmäinen == "b" or ensimmäinen == "c":
        print("")
    print("------------")
    toinen = input(' ')
    print("------------")
    if toinen == "a":
        print("Oikein")
        oikein += 1
    elif toinen == "b" or toinen == "c":
        print('')
    print("------------")
    kolmas = input(' ')
    print("------------")
    if kolmas == "b":
        print("Oikein")
        oikein += 1
    elif kolmas == "a" or kolmas == "c":
        print('')
    print("------------")
    neljäs = input('  ')
    print("------------")
    if neljäs == "a":
        print("Oikein")
        oikein += 1
    elif neljäs == "b" or neljäs == "c":
        print('')
    print("------------")
    viides = input('')
    print("------------")
    if viides == "b":
        print("Oikein")
        oikein += 1
    elif viides == "a" or viides == "c":
        print('')
    print("------------")
    kuudes = input(' ')
    print("------------")
    if kuudes == "b":
        print("Oikein")
        oikein += 1
    elif kuudes == "a" or kuudes == "c":
        print('')
    print("------------")
    seittemäs = input(' ')
    print("------------")
    if seittemäs == "b":
        print("Oikein")
        oikein += 1
    elif seittemäs == "a" or seittemäs == "c":
        print('')
    print("------------")
    kahdeksas = input('   ')
    print("------------")
    if kahdeksas == "c":
        print("Oikein")
        oikein += 1
    elif kahdeksas == "a" or kahdeksas == "c":
        print('')
    print("------------")
    yhdeksäs = input(' ')
    print("------------")
    if yhdeksäs == "b":
        print("Oikein")
        oikein += 1
    elif yhdeksäs == "a" or yhdeksäs == "c":
        print('')
    print("------------")
    kymmenes = input(' ')
    print("------------")
    if kymmenes == "b":
        print("Oikein")
        oikein += 1
    elif kymmenes == "a" or kymmenes == "c":
        print(' ')
    print("-----------")
    print(f"Oikein meni {oikein}/10")

testi()

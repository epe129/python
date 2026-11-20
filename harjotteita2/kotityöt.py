def k():
    while True:
        vastaus = input("mitä halua tehdä? 1-4 ovat vaihtoehtoja:")
        if vastaus == "1":
            print("käytä koira")
            break
        elif vastaus == "2":
            print("siivoa")
            break
        elif vastaus == "3":
            print("käytä koira")
            break
        elif vastaus == "4":
            print("tyhjennä astianpesukone")
            break
        else:
            print("yksi vaihto ehdoista")
             
        
k()
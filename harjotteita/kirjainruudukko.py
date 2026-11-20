def kirjainruudukko():
    kerrokset = int(input("Kerrokset: "))
    kirjaimet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    merkkejä = kirjaimet[:kerrokset][::-1]
    # print(merkkejä)
    index = list(range(1, kerrokset + 1))
    # print(index)
    index += index[::-1][1:]
    # print(index)
    for i in index:
        rivi = merkkejä[:i]
        # print(rivi)
        rivi += rivi[-1] * (kerrokset - len(rivi))
        # print(rivi)
        rivi += rivi[::-1][1:]
        print(rivi)

kirjainruudukko()



        
 


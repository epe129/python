def kirjainruudukko():
    kerrokset = int(input("kierrokset: "))
    sisäkkäinen = kerrokset
    pituus = kerrokset*2-1
    for i in range(1,kerrokset):
        for c in range(1,kerrokset):
            if i == 1 and c == 1:
                print("B"*pituus)
    print("B" + "A" + "B")
    print("B"*pituus, end="")

kirjainruudukko()

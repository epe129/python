def kirjainruudukko():
    kerrokset = int(input("kierrokset: "))
    
    if kerrokset == 2:
        sisäkkäinen = kerrokset
        pituus = kerrokset*2-1
        for i in range(1,kerrokset):
            for c in range(1,kerrokset):
                if i == 1 and c == 1:
                    print("B"*pituus)
        print("B" + "A" + "B")
        print("B"*pituus, end="")

    if kerrokset == 3:
        sisäkkäinen = kerrokset
        pituus = kerrokset*2-1
        for i in range(1,kerrokset):
            for c in range(1,kerrokset):
                if i == 1 and c == 1:
                    print("C"*pituus)
        print("C" + ("B"*sisäkkäinen) + "C")
        if c == kerrokset-1:
            print("C" + "B" + "A" + "B" + "C")
        print("C" + ("B"*sisäkkäinen) + "C")
        print("C"*pituus, end="")

    if kerrokset == 4:
        sisäkkäinen = kerrokset-1
        sisäkkäinenC = kerrokset+1
        pituus = kerrokset*2-1
        for i in range(1,kerrokset):
            for c in range(1,kerrokset):
                if i == 1 and c == 1:
                    print("D"*pituus)
        print("D"+"C"*sisäkkäinenC+"D")
        print("D" + "C" + ("B"*sisäkkäinen) + "C" + "D")
        if c == kerrokset-1:
            print("D" + "C" + "B" + "A" + "B" + "C" + "D")
        print("D" + "C" + ("B"*sisäkkäinen) + "C" + "D")
        print("D"+"C"*sisäkkäinenC+"D")
        print("D"*pituus, end="")

    if kerrokset == 5:
        sisäkkäinen = kerrokset
        sisäkkäinenC = kerrokset*2-3
        pituus = kerrokset*2-1
        for i in range(1,kerrokset):
            for c in range(1,kerrokset):
                if i == 1 and c == 1:
                    print("E"*pituus)
        print("E"+"D"*sisäkkäinenC+ "E")
        print("E"+"D" +"C"*5+ "D" + "E")
        # print("E"+"D" + "C" + ("B"*3) + "C" + "D"+ "E")
        print("E"+"D" + "C" + ("B"*3) + "C" + "D" +"E")
        if c == kerrokset-1:
            print("E"+"D" + "C" + "B" + "A" + "B" + "C" + "D" + "E")
        print("E"+"D" + "C" + ("B"*3) + "C" + "D" + "E")
        # print("E" +"D" + "C" + ("B"*3) + "C" + "D" + "E")
        print("E"+ "D"+"C"*5 + "D" +"E")
        print("E"+"D"*sisäkkäinenC+ "E")
        print("E"*pituus, end="")


kirjainruudukko()

def Palindromi():
    AnnaSana = str(input("Onko sana palindromi: "))

    käännetään = AnnaSana[::-1]

    if AnnaSana == käännetään:
        print(True)
    else:
        print(False)

Palindromi()
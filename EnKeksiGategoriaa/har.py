def nelio(sana, luku):
    a = sana
    laskuri = 0
    c = True
    while c:
        for i in sana:
            a += i
            ekakirjain = i
            if luku >= 5 and luku <= 9:
                if len(a) >= luku:
                    print(a[:luku])
                    laskuri += 1
                    if ekakirjain == a[0]:
                        laskuri += 1
                        print(a[:luku])
                    a = a[2:luku]
                if laskuri == luku:
                    c = False
                    break
            elif luku <= 4:
                if len(a) >= luku:
                    print(a[:luku])
                    laskuri += 1
                    if ekakirjain == a[0]:
                        laskuri += 1
                        print(a[1:luku] + a[1])
                if laskuri == luku:
                    c = False
                    break
            elif luku >= 10:
                if len(a) >= luku:
                    print(a[:luku])
                    laskuri += 1
                    if ekakirjain == a[0]:
                        print(a[:luku])
                        laskuri += 1
                    a = a[3:luku]
                if laskuri == luku:
                    c = False
                    break

if __name__ == "__main__":
    # nelio("aba", 3)
    nelio("abc", 7)
    # nelio("python", 15)

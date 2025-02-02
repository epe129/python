def FindTheLongestWord():
    lause = "tervetuloa kaikki"
    words = lause.split()
    pisin = 0

    for word in words:
        if len(word) > pisin:
            pisin = len(word)
            
    print(pisin)

FindTheLongestWord()


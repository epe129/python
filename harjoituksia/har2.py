def sudoku_oikein(sudoku: list):
  f = 0
  t = 0
  
  rv = 0
  sk = 0
  
  paikat = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
  
  for z in paikat:
    laskuri = 0
    nelio = []
    nähty = []
    rv,sk = z
    # print(rv, sk)       
    if sk == 0:
        pituus = 3
    else:
        pituus = sk
    for rivi1 in range(len(sudoku)):
        if rivi1 == rv:
            for x in range(len(sudoku[rivi1])):
                nelio.append(sudoku[rivi1][x])
                while pituus <= sk*2 - 1:
                    pituus += 1
            # print(nelio[sk:pituus])
            for numerot in nelio[sk:pituus]:
                if numerot == 1 or numerot == 2 or numerot == 3 or numerot == 4 or numerot == 5 or numerot == 6 or numerot == 7 or numerot == 8 or numerot == 9:
                    if numerot in nähty:
                        # print("f")
                        f += 1
                        # return False
                    else: 
                        nähty.append(numerot)
            nelio.clear()
            nähty.clear()
            rv += 1
            laskuri += 1
            if laskuri == 3:
                break
  
  sarakenähty = []
  sarake = []
  sarake_nro = 0
  
  
  rivi_nro = 0
  rivinähty = []

  while rivi_nro <= 8:
    for rivi in range(len(sudoku)):
        if rivi == rivi_nro:
            # print(rivi)
            for ruutu in sudoku[rivi]:
                if 1 == ruutu or 2 == ruutu or 3 == ruutu or 4 == ruutu or 5 == ruutu or 6 == ruutu or 7 == ruutu or 8 == ruutu or 9 == ruutu:
                    if ruutu in rivinähty:
                        # print("f")
                        f += 1
                        # return False
                    else:
                        rivinähty.append(ruutu)
            if ruutu not in rivinähty:
                t += 1
                # print("t")
                # return True
            rivinähty.clear()
            rivi_nro += 1
    
  while sarake_nro <= 8:
    for c in range(len(sudoku)):
        for i in range(len(sudoku[c])):
            for sr in range(len(sudoku[i])):
                if sr == sarake_nro:
                    # print(sr)
                    sarake.append(sudoku[i][sr])
                    break
        if sudoku[c][sr] in sarake:
            # print(sarake)
            for numero in sarake:
                if 1 == numero or 2 == numero or 3 == numero or 4 == numero or 5 == numero or 6 == numero or 7 == numero or 8 == numero or 9 == numero:
                    if numero in sarakenähty:
                        f += 1
                        # return False
                    else:
                        sarakenähty.append(numero)   
            if numero not in sarakenähty:
                t += 1
                # return True
        sarakenähty.clear()
        sarake.clear()
        sarake_nro += 1
    if f >= 1:
        return False
    else:
        return True

  
if __name__=="__main__":
    sudoku = [
    [ 4, 8, 1, 2, 0, 9, 7, 0, 3 ],
    [ 7, 0, 3, 1, 0, 8, 6, 9, 2 ],
    [ 6, 9, 2, 3, 7, 5, 4, 8, 1 ],
    [ 5, 3, 4, 0, 8, 1, 9, 2, 7 ],
    [ 0, 0, 8, 7, 9, 2, 5, 3, 4 ],
    [ 9, 2, 7, 4, 5, 0, 8, 1, 0 ],
    [ 2, 7, 5, 8, 4, 4, 1, 6, 0 ],
    [ 1, 6, 9, 5, 2, 7, 3, 4, 8 ],
    [ 0, 4, 0, 9, 1, 6, 2, 7, 5 ],
  ]
    
    # print(sudoku_oikein(sudoku))
    
    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
  ]
    print(sudoku_oikein(sudoku2))                      

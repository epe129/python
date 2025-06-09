def rivi_oikein(sudoku: list):
  nähty = []
  rivi_nro = 0
  for rivi in range(len(sudoku)):
    if rivi == rivi_nro:
      for ruutu in sudoku[rivi]:
        # print(ruutu)
        if 1 == ruutu or 2 == ruutu or 3 == ruutu or 4 == ruutu or 5 == ruutu or 6 == ruutu or 7 == ruutu or 8 == ruutu or 9 == ruutu:
          if ruutu in nähty:
            return False
          else:
            nähty.append(ruutu)
  return True            


# tee ratkaisu tänne
def sarake_oikein(sudoku: list):
  nähty = []
  sarake = []
  sarake_nro = 4
  for c in range(len(sudoku)):
    for i in range(len(sudoku[c])):
        for x in range(len(sudoku[i])):
            if x == sarake_nro:
               sarake.append(sudoku[i][x])
    if len(sarake) >= 9:
        sarake = sarake[:8]
    if sudoku[c][x] in sarake:
        # print(sarake)
        for k in sarake:
            # print(k)
            if 1 == k or 2 == k or 3 == k or 4 == k or 5 == k or 6 == k or 7 == k or 8 == k or 9 == k:
                if k in nähty:
                    # print("f")
                    return False
                else:
                    nähty.append(k)   
        if k not in nähty:
            # print("t")
            return True     
            
# tee ratkaisu tänne
def nelio_oikein(sudoku: list):
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
                        return False
                    else: 
                        nähty.append(numerot)
            nelio.clear()
            nähty.clear()
            rv += 1
            laskuri += 1
            if laskuri == 3:
                break
  return True

if __name__=="__main__":
    sudoku = [
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
    print(rivi_oikein(sudoku))
    print(sarake_oikein(sudoku))
    print(nelio_oikein(sudoku))

    print(nelio_oikein(sudoku, 1, 2))

def sudoku_oikein(sudoku: list):
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
                            return False
                        else: 
                            nähty.append(numerot)
                nelio.clear()
                nähty.clear()
                rv += 1
                laskuri += 1
                if laskuri == 3:
                    break

    riviNähty = [] 
    for i in range(9):
        for rivi in sudoku[i]:
            # print(rivi)
            if rivi in riviNähty:
                return False
            else:
                riviNähty.append(rivi)
        riviNähty.clear()
        
    
    sarakeNähty = []
    for c in range(9):
        for x in range(9):
            sarake = sudoku[x][c]
            if sarake in sarakeNähty:
                return False
            else:
                sarakeNähty.append(sarake)
        sarakeNähty.clear()
        
 
    return True

if __name__=="__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(sudoku_oikein(sudoku))


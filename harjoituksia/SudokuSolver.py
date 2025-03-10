
def sarake_oikein(sudoku: list):
  nähty = []
  sarake = []
  sarake_nro = 0
  for c in range(1,9):
    for i in range(len(sudoku[c])):
        for x in range(len(sudoku[i])):
            if x == sarake_nro:
                sarake.append(sudoku[i][x])
        if len(sarake) == 9:
            for k in sarake:
                print(k)
                if 1 == k or 2 == k or 3 == k or 4 == k or 5 == k or 6 == k or 7 == k or 8 == k or 9 == k:
                    if k in nähty:
                        return False
                    else:
                        nähty.append(k)   
    

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
    print(sarake_oikein(sudoku))


# tee ratkaisu tänne
def tulosta(sudoku: list):
    for i in range(len(sudoku)):
        for x in range(9):
            if x % 3 == 0:
                print(" ", end="")
            if sudoku[i][x] == 0:
                print(f"_ ", end="")
        if i == 2 or i == 5:
            print()
        print()

def lisays(sudoku: list, rivi_nro: int, sarake_nro: int, luku:int):
    pass
    # print(sudoku)
    # uusilista = []
    # for i in range(len(sudoku)):
    #     for x in range(9):
    #         # if x % 3 == 0:
    #             # pass
    #             # print(" ", end="")
    #         if x == sarake_nro and i == rivi_nro:
    #             f"{luku}", end=""
    #         elif sudoku[i][x] == 0:
    #             pass
    #             print(f"_ ", end="")            
    #     if i == 2 or i == 5:
    #         print()
    #     print()


if __name__=="__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)


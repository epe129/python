# tehty opetus videon avulla
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# soolve-funktio yrittää ratkaista sudokun rekursiivisesti
def solve(bo):
    # etsitään seuraava tyhjä paikka (0 tarkoittaa tyhjää ruutua)
    find = löydäTyhjäPaikka(bo)

    if not find:
        return True # jos ei löytynyt tyhjää paikkaa, peli on ratkaistu
    else:
        row, col = find # tyhjä paikan sijainti (rivi, sarake)

   # kokeillaan lukuja 1-9 tyhjään paikkaan
    for i in range(1,10):
        if valid(bo, i, (row, col)): # tarkistetaan, onko luku kelvollinen tähän paikkaan
            bo[row][col] = i # asetetaan luku

            if solve(bo): # kutsutaan solve-funktiota rekursiivisesti (yritetään ratkaista peli eteenpäin)
                return True # jos ratkaisamme peli, palautetaan true

            bo[row][col] = 0 # Jos ratkaisua ei löydy, palautetaan tyhjään ruutuun 0 ja yritetään seuraavaa lukua

    return False # Jos mikään luku ei käy, palautetaan False, eli peli ei ole ratkaistavissa nykyisillä valinnoilla

# valid-funktio tarkistaa, onko annettu numero kelvollinen tietyssä ruudussa
def valid(bo, num, pos):
    # Tarkistetaan, ei oleko sama luku rivillä
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i: # Jos löytyy sama luku, joka ei ole nykyinen ruutu
            return False # Luku ei ole kelvollinen

    # Tarkistetaan, ei oleko sama luku sarakkeessa
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i: # Jos löytyy sama luku, joka ei ole nykyinen ruutu
            return False # Luku ei ole kelvollinen

    # Tarkistetaan, ei oleko sama luku 3x3-ruudussa
    box_x = pos[1] // 3  # Laske, mihin 3x3-ruutuun sarake kuuluu
    box_y = pos[0] // 3 # Laske, mihin 3x3-ruutuun rivi kuuluu

    # Tarkistetaan kaikki ruudun arvot alueella
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos: # Jos löytyy sama luku, joka ei ole nykyinen ruutu
                return False # Luku ei ole kelvollinen

    return True # Jos ei löytynyt ristiriitoja, luku on kelvollinen

# p-funktio tulostaa pelin tilan
def p(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("--------------------")  # Lisää erottelin riviin joka kolmannen rivin väliin
    
    
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0: # Lisää erottelin sarakkeeseen joka kolmannen sarakkeen väliin
                print(" | ", end="")


            if j == 8: # Viimeinen sarake
                print(bo[i][j]) # Tulostetaan rivi
            else:
                print(str(bo[i][j]) + " ", end="") # Tulostetaan sarake ja jätetään väli
# löydäTyhjäPaikka-funktio etsii pelistä seuraavan tyhjän ruudun (0)
def löydäTyhjäPaikka(bo):
    for i in range(len(bo)): # Käy läpi rivit
        for j in range(len(bo[0])): # Käy läpi sarakkeet
            if bo[i][j] == 0: # Jos ruudussa on 0 (tyhjä)
                return (i, j)  # Palautetaan sijainti (rivi, sarake)
    
    return None # Jos ei ole tyhjiä paikkoja, palautetaan None
            



# p(board)
print("-------------------")
solve(bo=board)
p(bo=board)

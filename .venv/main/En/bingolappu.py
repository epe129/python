# import random

# grid_size = 5 
# cell_width = 4  


# for i in range(grid_size):
#     print("_" * (grid_size * cell_width))
#     for j in range(grid_size):    
#         numbers = random.randint(1, 99)
#         print(f"|{numbers:2}|", end="") 
#     print("")

import random

def generoi_bingo_lappu():
    bingo = {
        "B": random.sample(range(1, 16), 5),
        "I": random.sample(range(16, 31), 5),
        "N": random.sample(range(31, 46), 5),
        "G": random.sample(range(46, 61), 5),
        "O": random.sample(range(61, 76), 5)
    }

    # Keskiruutu on ilmainen (Free)
    bingo["N"][2] = "FREE"

    # Tulostetaan bingo-lappu
    print(" B   I   N   G   O")
    for i in range(5):
        rivi = []
        for kirjain in "BINGO":
            rivi.append(f"{bingo[kirjain][i]:^4}")
        print("".join(rivi))

generoi_bingo_lappu()

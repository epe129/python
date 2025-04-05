import random

grid_size = 5 
cell_width = 4  


for i in range(grid_size):
    print("_" * (grid_size * cell_width))
    for j in range(grid_size):    
        numbers = random.randint(1, 99)
        print(f"|{numbers:2}|", end="") 
    print("")

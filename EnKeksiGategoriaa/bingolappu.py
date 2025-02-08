import random

print("-" * 16)
for i in range(4):
    for j in range(4):
        numbers = random.randint(1, 99)
        print(f"|{numbers:2}|", end="")
    print("")  
print("-" * 16, end='')  
 

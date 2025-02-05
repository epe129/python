import random

value = 10//2


for x in range(4):
    print(" ","_" * 21)
    for i in range(4):
        numbers = random.randint(1,99)
        print(" ",f"{numbers:2}|", end=" ")
print("___________________")

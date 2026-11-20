
aakkoset = "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z" 

sana = "perkele"

result = ""

for i in sana:
   for x in aakkoset:
        print(x)
        if i in x:
            result += i
            print(result)
            break      


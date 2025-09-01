import time

annaAika = int(input("Anna aikasekunneissa: "))

while annaAika:
    mins, secs = divmod(annaAika, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end='\r')
    time.sleep(1)
    annaAika -= 1

print("aika loppu")

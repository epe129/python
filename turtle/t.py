import turtle
import time
import random

try:
    num = int(input("Syötä piirrettävän muodon sivunumero: "))
    
    angle = 100 - 180*(num-2)/num

    turtle.up

    x = 0
    y = 0
    turtle.setpos(x, y)

    numshapes = 8

    for x in range(numshapes):
        turtle.color(random.random(), random.random(), random.random())
        x += 5
        y += 5
        turtle.forward(x)
        turtle.left(y)
        for i in range(num):
            turtle.begin_fill()
            turtle.down()
            turtle.forward(40)
            turtle.left(angle)
            turtle.forward(40)
            print(turtle.pos())
            turtle.up()
            turtle.end_fill()
            
except:
    print("Jokin meni pieleen!")



turtle.done()            

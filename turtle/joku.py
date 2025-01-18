import turtle

sc = turtle.Screen()
sc.setup(width=.75, height=0.5, startx=None, starty=None)
sc.bgcolor("black")
T = turtle.Turtle()
T.width(3)
T.color("red")
T.pencolor("brown")
for _ in range(3):
    T.forward(80)
    T.left(80)
    T.right(80)
    T.left(80)
    T.forward(80)
    for _ in range(3):
        T.forward(80)
        T.left(82)
        T.right(82)
        T.left(82)
        T.forward(80)

T.color("black")
T.pencolor("black")

T.home()   

turtle.done()

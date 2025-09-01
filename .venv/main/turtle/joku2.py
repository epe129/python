import turtle

t = turtle.Turtle()
tt = turtle.Screen()
tt.bgcolor("black")

colors = ["red", "purple", "blue", "green", "orange", "yellow"]
ttt = turtle.Pen()

for i in range(160):
    ttt.pencolor(colors[i%6])
    ttt.width(i//100 + 1)
    ttt.forward(i)
    ttt.left(59)


turtle.done()

    
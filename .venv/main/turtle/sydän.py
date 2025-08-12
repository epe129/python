import turtle

screen = turtle.Screen()
screen.setup(width=1620, height=900)
screen.bgcolor("black")
screen.title("SYDÄN")
t = turtle.Turtle()
t.speed(0)
t.width(10)
t.color("red")

t.begin_fill()
t.left(150)
t.forward(180)
t.circle(-100, 210)
t.setheading(70)
t.circle(-100, 210)
t.forward(180)
t.end_fill()

t.penup()
t.goto(-15, 100)  
t.color("white")
t.write("perhe", align="center", font=("Arial", 36, "normal"))


t.hideturtle()
screen.mainloop()

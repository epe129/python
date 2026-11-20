import turtle

screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for i in range(91):
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.right(4)
    



turtle.done()
    






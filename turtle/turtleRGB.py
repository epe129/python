import turtle
import random

t = turtle.Turtle()

turtle.speed(0)
turtle.bgcolor("black")

for i in range(100):
    # Generating random circle radius between 50 and 150
    radius = random.randint(100, 250)
    
    # Generating random position
    x = random.randint(-500, 900)
    y = random.randint(-500, 900)
    
    # Generating random color
    random_color = (random.random(), random.random(), random.random())  # Generates random RGB values
    
    # Moving turtle to random position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Setting random color
    t.color(random_color)
    
    # Drawing circle with random radius
    t.circle(radius)

turtle.done()

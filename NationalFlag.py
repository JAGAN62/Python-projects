import turtle
from turtle import *

t = turtle.Turtle()
screen = turtle.Screen()
speed(0)

#title
screen.title("National Flag")

#label
t.hideturtle()
t.penup() 
t.goto(0, 300)  
t.color('blue')
t.write("Happy Independence Day", align="center", font=("Times New Roman", 25, "normal"))

#pen setup
t.pencolor('black')
t.width(2)
t.pensize(1)

# Draw the orange rectangle
t.penup()
t.goto(-500, 270)
t.pendown()
t.color('black','orange')
t.begin_fill()
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# Draw the white rectangle
t.penup()
t.goto(-500, 70)
t.pendown()
t.color('black','white')
t.begin_fill()
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

# Draw the green rectangle
t.penup()
t.goto(-500, -130)
t.pendown()
t.color('black','green')
t.begin_fill()
for i in range(2):
    t.forward(1000)
    t.right(90)
    t.forward(200)
    t.right(90)
t.end_fill()

#Ashok Circle
t.penup()
t.width(2)
t.goto(10, -110)
t.pendown()
t.color("navy")
t.fillcolor()
t.circle(80)
t.end_fill()

# Spokes
t.penup()
t.goto(10, -30)
t.pendown()
t.pensize(2)
for i in range(24):
    t.forward(80)
    t.backward(80)
    t.left(15)

turtle.done()



import turtle
import random
import time

t = turtle.Turtle()
t.shape("turtle")
t.shapesize(3,3)
t.up()
t.speed(10)

def show(x,y):
    t.color("purple")
    time.sleep(1)

    x = random.randint(-300,300)
    y = random.randint(-300,300)
    angle = random.randint(-180,180)

    t.left(angle)
    t.goto(x,y)
    t.color("black")

t.onclick(show)

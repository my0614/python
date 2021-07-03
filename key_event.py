
import turtle
import random

t = turtle.Turtle()
sc = turtle.Screen()

def move():
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    t.up()
    t.goto(x,y)
    t.down()

def fill_circle():
    move()
    t.color(random.choice(['red', 'blue', 'black']))
    s = random.randint(10, 50)
    a = random.randint(1,3)
    t.begin_fill()
    
    if a == 1:
        t.circle(s)

    if a == 2:
        for i in range(3):
            t.fd(s)
            t.left(120)

    if a == 3:
        for i in range(4):
            t.fd(s)
            t.left(90)
            
    t.end_fill()

sc.onkeypress(fill_circle, 'c')
sc.listen()


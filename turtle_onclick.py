import turtle
import random

t = turtle.Turtle()
sc = turtle.Screen()

def circle(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(100)

sc.onclick(circle)
sc.mainloop()

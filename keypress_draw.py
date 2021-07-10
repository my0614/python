import turtle

t = turtle.Turtle()
sc = turtle.Screen()

t.shape("turtle")
t.pensize(3)

def draw(x,y):
    t.goto(x,y)

t.ondrag(draw)

sc.onkeypress(t.penup,"Up")
sc.onkeypress(t.pendown,"Down")
sc.onkeypress(t.clear,"Delete")

sc.onscreenclick(draw)
sc.listen()

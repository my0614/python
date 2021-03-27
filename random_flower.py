import turtle,random
t = turtle.Turtle()
t.pensize(2)
t.speed(40)
fcolor = ['red','purple','yellow']
t.color(random.choice(fcolor)) #랜덤색상고르기
radius = random.randint(100,150)
t.circle(radius)
for i in range(6):
    t.left(360/6)
    t.circle(radius)

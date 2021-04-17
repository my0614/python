import turtle
t = turtle.Turtle()
#t.speed(13)
cnt = 0
colors = ['yellow','green','blue','purple','red']
for count in range(50,100,10):
    t.color(colors[cnt])
    for i in range(6):
        t.circle(count)
        t.left(60)
    cnt+=1
        

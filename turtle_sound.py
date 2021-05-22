import turtle, time, winsound
t= turtle.Turtle()
s = turtle.Screen()
x = -300
for n in range(1,21):
    t.up()
    t.goto(x,0)
    if n%3 == 0:
        t.write("*",font ="굴림 15 bold")
        winsound.Beep(600,500)
    else:
        t.write(n,font ="굴림 15 bold")
    time.sleep(1)
    x = x+30
t.ht()
s.mainloop()

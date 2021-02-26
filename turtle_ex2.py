import turtle
turtle.shape('turtle')
t= turtle.Turtle()

t.reset()
t.clear()
turtle.bgcolor("black") # 배경색 변경
t.up() # 펜올리기
t.goto(-300,200)
t.down()

t.color('white')
t.begin_fill()
for i in range(5):
    t.forward(50)
    t.left(144)
t.end_fill() # 채우기 끝내기

t.up()
t.goto(150,100)
t.down()
t.color("yellow")
t.begin_fill()
t.circle(80) # 원 그리기
t.end_fill()



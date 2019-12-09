import sys
import os

insert =  " "
rear = 0  # rear
front = 0  # front
err = "hello everyone"
queue = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']   # 8개 배열 선언해주기


def Empty(queue): # 배열 비웠음
    return rear == front


def Full(queue): # 배열 가득참
    return (rear + 1) % 8 == front



def pop():
    global front, queue, err
    if Empty(queue) == 1:
        err = "Queue is Empty"
    else:
        err = "hello everyone"
        queue[front] = ' '  # 큐에서 제거
        if front == 7:
            front = 0
        else:
            front += 1


def push(insert):
    global rear, queue, err

    if Full(queue) == 1:
        err = "Queue is Full"
    else:
        err = "hello everyone"
        queue[rear] = insert  # 큐에 삽입
        if rear == 7:
            rear = 0
        else:
            rear += 1


while 1:
    print("삽입을 원하는 원소를 입력하세요.\n0이나 공백을 입력하면 원소를 pop 합니다.\n프로그램을 종료하려면 9를 누르세요\n\n   1303_김민영 \n\n      원형큐")
    print("rear =", rear, "/ front =", front)
    print("/=1=\ /=2=\ /=3=\ ")
    print("| " + queue[7] + " | | " + queue[0] + " | | " + queue[1] + " |")
    print("\= =/ \= =/ \= =/ \n")
    print("/=6=\       /=2=\ ")
    print("| " + queue[6] + " |     "         "  |" + queue[2] + "  |")
    print("\= =/       \= =/ \n")
    print("/=5=\ /=4=\ /=3=\ ")
    print("| " + queue[5] + " | | " + queue[4] + " | | " + queue[3] + " |")
    print("\= =/ \= =/ \= =/ \n")
    insert = input("원하는 문자를 적어주세요.")

    os.system('cls')
    if insert == "9":
        sys.exit()
    elif insert == "0" or insert == " " or insert == "":
        pop()
    else:
        push(insert)
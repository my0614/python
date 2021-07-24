from tkinter import *

window = Tk()
window.title("로그인")
window.geometry("300x150")

label1 = Label(window, text = "아이디")
label1.pack()

Id = Entry(window)
Id.pack()

label2 = Label(window, text= "비밀번호")
label2.pack()

pw = Entry(window)
pw.pack()

window.mainloop()

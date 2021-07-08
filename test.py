from tkinter import *
window = Tk()
window.title("Frame")
window.geometry('500x400')


frame1 = Frame(window, width=00, height=300, highlightbackground="blue", highlightthickness=2)
frame1.place(x=5, y=50)
l1 = Label(frame1, text="Please Enter Username")
l1.place(x=0, y=0)
e1 = Entry(frame1)
e1.place(x=200, y=0)
window.mainloop()

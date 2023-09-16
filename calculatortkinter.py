from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("calculator")


num = StringVar()
num1 = StringVar()
res = StringVar()
choice = StringVar
"""frame = Frame(win, width=200, height=50, bg="pink", bd=40,
              relief="raised").grid(padx=(10, 0), pady=(0, 40))"""

btn1 = Button(win, text=7, bd=2).grid(row=1, column=1, ipadx=4, ipady=3)
btn2 = Button(win, text=8, bd=2).grid(row=1, column=2, ipadx=4, ipady=3)
btn3 = Button(win, text=9, bd=2).grid(row=1, column=3, ipadx=4, ipady=3)
btn4 = Button(win, text="+", bd=2, textvariable=choice).grid(row=1,
                                                             column=4, ipadx=4, ipady=3)
btn1 = Button(win, text=4, bd=2).grid(row=2, column=1, ipadx=4, ipady=3)
btn2 = Button(win, text=5, bd=2).grid(row=2, column=2, ipadx=4, ipady=3)
btn3 = Button(win, text=6, bd=2).grid(row=2, column=3, ipadx=4, ipady=3)
btn4 = Button(win, text="-", bd=2, textvariable=choice).grid(row=2,
                                                             column=4, ipadx=4, ipady=3)
btn1 = Button(win, text=1, bd=2).grid(row=3, column=1, ipadx=4, ipady=3)
btn2 = Button(win, text=2, bd=2).grid(row=3, column=2, ipadx=4, ipady=3)
btn3 = Button(win, text=3, bd=2).grid(row=3, column=3, ipadx=4, ipady=3)
btn4 = Button(win, text="*", bd=2, textvariable=choice).grid(row=3,
                                                             column=4, ipadx=4, ipady=3)
btn1 = Button(win, text=0, bd=2).grid(row=4, column=1, ipadx=4, ipady=3)
btn2 = Button(win, text="C", bd=2, textvariable=choice).grid(
    row=4, column=2, ipadx=4, ipady=3)
btn3 = Button(win, text="=", bd=2, textvariable=choice).grid(
    row=4, column=3, ipadx=4, ipady=3)
btn4 = Button(win, text="/", bd=2, textvariable=choice).grid(row=4,
                                                             column=4, ipadx=4, ipady=3)
"""lb = Label(frame, text=str(choice), bg="red").grid(row=0, column=0)"""


win.mainloop()

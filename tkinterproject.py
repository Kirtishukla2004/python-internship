from tkinter import *

win = Tk()

def msg():
    try:
        a = int(num.get())
        b = int(num1.get())
        choice_value = int(choice.get())

        if choice_value == 1:
            s = a + b
        elif choice_value == 2:
            s = a - b
        elif choice_value == 3:
            s = a * b
        elif choice_value == 4:
            if b == 0:
                res.set("Division by zero is not allowed")
                return
            else:
                s = a / b
        else:
            res.set("Invalid choice")
            return

        res.set(s)
    except ValueError:
        res.set("Invalid input. Please enter valid numbers.")

lb = Label(win, text="enter first no.")
lb.grid(row=0, column=0)
num = StringVar()
tab = Entry(win, textvariable=num)
tab.grid(row=0, column=1)

lb = Label(win, text="enter second no.")
lb.grid(row=1, column=0)
num1 = StringVar()
tab = Entry(win, textvariable=num1)
tab.grid(row=1, column=1)

lb = Label(win, text="enter operation (1 for +, 2 for -, 3 for *, 4 for /)")
lb.grid(row=2, column=0)
choice = StringVar()
tb = Entry(win, textvariable=choice)
tb.grid(row=2, column=1)

lb = Label(win, text="result")
lb.grid(row=3, column=0)
res = StringVar()
tb = Entry(win, textvariable=res)
tb.grid(row=3, column=1)

btn = Button(win, text="submit", command=msg)
btn.grid(row=4, column=1)

win.mainloop()

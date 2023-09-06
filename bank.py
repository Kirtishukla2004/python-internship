from tkinter import *
win = Tk()


def display():
    name = (name_value.get())
    account = (account_value.get())
    amount = (amount_value.get())
    address = (add_value.get())
    contact = (contact_value.get())
    pin = (pin_value.get())
    show_label = Label(win, text="\n" + "name"+"   " + str(name) + "\n" + "account" + "   " + str(account) + "\n" + "amount" + "   " + str(amount) +
                       "\n" + "address" + "   " + str(address) + "\n" + "contact "+"   " + str(contact) + "\n" + "pin" + "   " + str(pin)).grid(row=9, column=1)


frame = Frame(win, width=300, height=100, bg="pink", bd=40,
              relief="raised").grid(row=0, column=2, pady=20, padx=10)
l = Label(frame, text="bank of bharat ", fg="black",
          bg="pink").grid(row=0, column=2)
name_value = StringVar()
account_value = StringVar()
add_value = StringVar()
contact_value = StringVar()
pin_value = StringVar()
amount_value = StringVar()
lb = Label(win, text="ENTER THE CUSTOME DETAILS BELOW").grid(row=1, column=2)
name_label = Label(win, text="enter your name").grid(row=2, column=1)
tb = Entry(win, textvariable=name_value).grid(row=2, column=2)
account_label = Label(win, text="enter your accountno").grid(row=3, column=1)
tb = Entry(win, textvariable=account_value).grid(row=3, column=2)
amount_label = Label(win, text="enter your amount").grid(row=4, column=1)
tb = Entry(win, textvariable=amount_value).grid(row=4, column=2)
add_label = Label(win, text="enter your address").grid(row=5, column=1)
tb = Entry(win, textvariable=add_value).grid(row=5, column=2)
contact_label = Label(win, text="enter your contact").grid(row=6, column=1)
tb = Entry(win, textvariable=contact_value).grid(row=6, column=2)
pin_label = Label(win, text="enter your pin").grid(row=7, column=1)
tb = Entry(win, textvariable=pin_value).grid(row=7, column=2)
btn = Button(win, text="showdetails", justify="center",command=display).grid(row=8, column=2)
win.mainloop()

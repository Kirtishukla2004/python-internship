from tkinter import *
win = Tk()
win.title("ATM MAIN HOME PAGE")
win.geometry("800x600")
mainframe=Frame(win,bg="white",relief="solid",bd=2,width=1000,height=100)
mainframe.grid(row=0,column=4)
lb=Label(mainframe,text="ROYAL BANK OF INDIA",font=('bold',20),fg="red",bg="black")
lb.grid(row=0,column=4)
deposit_btn = Button(win, text="Deposit cash", bg="grey",
                     font=("bold,30"), bd=2, relief="groove")
deposit_btn.grid(row=1, column=0, padx=10, pady=20, ipadx=10, ipady=10)
ministatement_btn = Button(win, text="Mini-Statement",
                           bg="grey", font=("bold,30"), bd=2, relief="groove")
ministatement_btn.grid(row=1, column=1, padx=10, pady=20, ipadx=10, ipady=10)
wisthdeaw_btn = Button(win, text="Withdraw Cash", bg="grey",
                       font=("bold,30"), bd=2, relief="groove")
wisthdeaw_btn.grid(row=2, column=0, padx=10, pady=20, ipadx=10, ipady=10)
fastcash_btn = Button(win, text="Fast cash", bg="grey",
                      font=("bold,30"), bd=2, relief="groove")
fastcash_btn.grid(row=2, column=1, padx=10, pady=20, ipadx=10, ipady=10)
balance_btn = Button(win, text="Balance Enquiry", bg="grey",
                     font=("bold,30"), bd=2, relief="groove")
balance_btn.grid(row=3, column=0, padx=10, pady=20, ipadx=10, ipady=10)
cheque_btn = Button(win, text="Change pin", bg="grey",
                    font=("bold,30"), bd=2, relief="groove")
cheque_btn.grid(row=3, column=1, padx=10, pady=20, ipadx=10, ipady=10)
transfer_btn = Button(win, text="Tranfer fund", bg="grey",
                      font=("bold,30"), bd=2, relief="groove")
transfer_btn.grid(row=4, column=0, padx=10, pady=20, ipadx=10, ipady=10)
update_btn = Button(win, text="Update cash", bg="grey",
                    font=("bold,30"), bd=2, relief="groove")
update_btn.grid(row=4, column=1, padx=10, pady=20, ipadx=10, ipady=10)

win.mainloop()

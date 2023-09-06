from  tkinter import*
Win=Tk()
Win.geometry("400x200")
def multiple():
    m=int(num.get())
    y=6
    for i in range(1,11):
        y=y+1
        lb=Label(Win,text=str(m) + "X" + str(i)+  "=" + str(i*m)).grid(row=y,column=4)



num=StringVar()
lb=Label(Win,text="enter number").grid(row=0,column=1)
tb=Entry(Win,textvariable=num).grid(row=0,column=2)
btn=Button(Win,text="table",command=multiple).grid(row=1,column=1)
Win.mainloop()

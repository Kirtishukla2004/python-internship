#tkinter
from tkinter import*
from tkinter import messagebox

win=Tk()#pre defined class first letter capital
win.title("win title")#title
win.geometry("400x400")#geometry function
win.config(bg="lime")#color
win.mainloop()
#win.resizable(False,False)      #no resize
#geometry function
'''grid()
pack()
place()'''


btn=Button(win,text="submit")
#btn.grid()
#btn.grid(row=0,column=0)

'''btn1=Button(win,text="omg")
btn1.grid()
btn2=Button(win,text="god")
btn2.grid()'''

'''btn1=Button(win,text="omg")
btn1.grid(row=0,colum=0)
btn2=Button(win,text="god")
btn2.grid(row=0,column=1)'''

#pack
'''btn1=Button(win,text="submit")
#btn1.pack()
btn1.pack(side="top")
btn2=Button(win,text="submit")
btn2.pack(side="right")
btn3=Button(win,text="submit")
btn3.pack(side="left")
btn4=Button(win,text="submit")
btn4.pack(side="bottom")'''





#place
'''def hello():
    #print("hello student")
    messagebox.showinfo("message","hello student")
btn1=Button(win,text="submit",command=hello)
btn1.place(x=150,y=150)'''


#how to generate events on button
'''Entry()
get()
Lable()'''

'''
def msg():
    username=us.get()
   # print("your name is",username)
    messagebox.showinfo("message",username)
    
lb=Label(win,text="enter name")
lb.grid(row=0,column=0)

us=StringVar()
tb=Entry(win,textvariable=us)
tb.grid(row=0,column=1)

btn=Button(win,text="submit",command=msg)
btn.grid(row=1,column=1)'''














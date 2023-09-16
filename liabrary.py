from tkinter import*
import pymysql 
import pymysql.cursors
win=Tk()
win.config(bg="grey")
frame=Frame(win,width=500, height=100, bg="pink", bd=4,relief="solid")
frame.pack()
head_lb=Label(frame,text="LIABRARY MANAGEMENT SYSTEM",bg="pink",font=("bold",15),width=31).grid(row=0, column=0, pady=10, padx=10)
mainframe=Frame(win,width=400,height=400,bg="orange",bd=3,relief="solid")
mainframe.pack(padx=500,pady=40)
lb=Label(mainframe,text="Search for student",bg="orange",font=("bold",15))
lb.grid()
win.mainloop();


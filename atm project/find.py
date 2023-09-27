from tkinter import *
import pyodbc


def find_user():
    iid = uid.get()
    user_name = name.get()
    conn = None
    try:
        server = 'localhost\SQLEXPRESS'
        database = 'tech'
        username = 'user_2004'
        password = 'kirti2004'

        conn = pyodbc.connect(
            f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        query = "SELECT * FROM emp WHERE id = ? AND name = ?"
        # Execute the query with parameters
        cursor.execute(query, (iid, user_name))
        result = cursor.fetchall()

        if result:
            for row in result:

                did.set(row[0])
                dname.set(row[1])
                address.set(row[2])
                salary.set(row[3])
                # btn=Button(win,text=row,bg='grey',fg='#0a0c0e',bd=0,font=('bold',15)).grid(row=5, column=0, columnspan=2, pady=20)
        else:
            btn = Button(win, text="NOT FOUND.....", bg='grey', fg='red', bd=0).grid(
                row=5, column=0, columnspan=2, pady=20)

        cursor.close()
    except Exception as e:
        print('Data not found:', e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


win = Tk()
win.geometry("800x500")
win.title("Find User")
win.config(bg="grey")

frame = Frame(win, bg="white", bd=4, relief='solid')
frame.grid(row=0, column=0, padx=20, pady=10)

title_label = Label(frame, text="FIND USER", bg='white',
                    font=('bold', 20), relief='solid', bd=4)
title_label.grid(row=0, column=0)

find_user_label = Label(win, text="FIND USER USING ID AND NAME....", font=(
    'bold', 15, 'underline'), fg='#063970', bg='grey')
find_user_label.grid(row=1, column=0, padx=20, pady=(20, 10), columnspan=2)

uid = StringVar()
id_label = Label(win, text='ID', font=('bold', 15), fg='#21130d', bg='grey')
id_label.grid(row=2, column=0, padx=(40, 10), pady=10, sticky='e')

id_entry = Entry(win, textvariable=uid)
id_entry.grid(row=2, column=1, padx=(10, 40), pady=10, sticky='w')

name = StringVar()
name_label = Label(win, text='NAME', font=(
    'bold', 15), fg='#21130d', bg='grey')
name_label.grid(row=3, column=0, padx=(40, 20), pady=10, sticky='e')

name_entry = Entry(win, textvariable=name)
name_entry.grid(row=3, column=1, padx=(10, 40), pady=10, sticky='w')

search_button = Button(win, text="Search", command=find_user,
                       font=('bold', 12), bg='#063970', fg='white')
search_button.grid(row=4, column=0, columnspan=2, pady=20)
Label(win, text="ID", width=5, bg='grey', font=(
    'bold', 10)).grid(row=5, column=0, padx=10, pady=10)
Label(win, text="NAME", width=5, bg='grey', font=(
    'bold', 10)).grid(row=6, column=0, padx=10, pady=10)
Label(win, text="ADDRESS", width=7, bg='grey', font=(
    'bold', 10)).grid(row=7, column=0, padx=10, pady=10)
Label(win, text="SALARY", width=7, bg='grey', font=(
    'bold', 10)).grid(row=8, column=0, padx=10, pady=10)
address = StringVar()
salary = StringVar()
did = StringVar()
dname=StringVar()
t1 = Entry(win, textvariable=did)
t1.grid(row=5, column=1)

t2 = Entry(win, textvariable=dname)
t2.grid(row=6, column=1)

t3 = Entry(win, textvariable=address)
t3.grid(row=7, column=1)

t4 = Entry(win, textvariable=salary)
t4.grid(row=8, column=1)

win.mainloop()

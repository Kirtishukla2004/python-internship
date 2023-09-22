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

        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        query_check = "SELECT COUNT(*) FROM emp WHERE id = ? AND name = ?"
        
        cursor.execute(query_check, (iid, user_name))
        count = cursor.fetchone()[0]
        if count > 0:
            query =  "DELETE FROM emp WHERE id = ? AND name = ?"
            cursor.execute(query, (iid, user_name))  
            conn.commit()
            lb=Label(win,text="DELETED SUCCESSFULLY.....",bg="white",fg='red',font=('bold',15,'underline')).grid(row=5, column=0, columnspan=2, pady=20)
        else:
            lb=Label(win,text=f"User with ID {iid} and name '{user_name}' not found.",bg="white",fg='red',font=('bold',15,'underline')).grid(row=5, column=0, columnspan=2, pady=20)
        cursor.close()
    except Exception as e:
        print('did not deleted:', e)
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()

win = Tk()
win.geometry("800x500")
win.title("Find User")
win.config(bg="white")

frame = Frame(win, bg="white", bd=4, relief='solid')
frame.grid(row=0, column=0, padx=20, pady=10)

title_label = Label(frame, text="DELETE USER", bg='white', font=('bold', 20), relief='solid', bd=4)
title_label.grid(row=0, column=0)

find_user_label = Label(win, text="DELETE USER USING ID AND NAME....", font=('bold', 15, 'underline'), fg='#063970', bg='white')
find_user_label.grid(row=1, column=0, padx=20, pady=(20, 10), columnspan=2)

uid = StringVar()
id_label = Label(win, text='ID', font=('bold', 15), fg='#21130d', bg='white')
id_label.grid(row=2, column=0, padx=(40, 10), pady=10, sticky='e')

id_entry = Entry(win, textvariable=uid,bd=4,relief='solid')
id_entry.grid(row=2, column=1, padx=(10, 40), pady=10, sticky='w')

name = StringVar()
name_label = Label(win, text='NAME', font=('bold', 15), fg='#21130d', bg='white')
name_label.grid(row=3, column=0, padx=(40, 20), pady=10, sticky='e')

name_entry = Entry(win, textvariable=name,bd=4,relief='solid')
name_entry.grid(row=3, column=1, padx=(10, 40), pady=10, sticky='w')

delete_button = Button(win, text="DELETE", command=find_user, font=('bold', 12), bg='white', fg='red',bd=2,relief='solid')
delete_button.grid(row=4, column=0, columnspan=2, pady=20,ipadx=10,ipady=10)

win.mainloop()

from tkinter import*
import pyodbc

def insert():
    uid = iid.get()
    nm = name.get()
    add = address.get()
    sal = salary.get()

    try:
        # Replace these with your SQL Server connection details
        server = 'localhost\SQLEXPRESS'
        database = 'tech'
        username = 'user_2004'
        password = 'kirti2004'

        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()

        query = f"INSERT INTO emp (id, name, salary, address) VALUES ({(uid)}, '{nm}', {(sal)}, '{add}')"
        cursor.execute(query)

        conn.commit()
        print("Data saved successfully.")
    except Exception as e:
        print('Data not saved:', e)
        conn.rollback()
    finally:
        conn.close()

win =  Tk()
win.geometry("400x250")
win.title("Window Application")
win.config(bg="grey")

# Labels
Label(win, text="id", width=5).grid(row=3, column=0, padx=10, pady=10)
Label(win, text="name", width=5).grid(row=4, column=0, padx=10, pady=10)
Label(win, text="address", width=5).grid(row=5, column=0, padx=10, pady=10)
Label(win, text="salary", width=5).grid(row=6, column=0, padx=10, pady=10)

iid =  StringVar()
name =  StringVar()
address =  StringVar()
salary =  StringVar()

t1 =  Entry(win, textvariable=iid)
t1.grid(row=3, column=1)

t2 =  Entry(win, textvariable=name)
t2.grid(row=4, column=1)

t3 =  Entry(win, textvariable=address)
t3.grid(row=5, column=1)

t4 =  Entry(win, textvariable=salary)
t4.grid(row=6, column=1)

# Submit Button
Button(win, text="Submit", command=insert).grid(row=7, column=0, columnspan=2, padx=10, pady=10)

win.mainloop()

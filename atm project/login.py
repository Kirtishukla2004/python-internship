import tkinter as tk
import pyodbc
from tkinter import messagebox
def check_login():
    username = username_entry.get()
    password = password_entry.get()
    try:
        server = 'localhost\SQLEXPRESS'
        database = 'tech'
        use = 'user_2004'
        passw = 'kirti2004'

        conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={use};PWD={passw}')
        cursor = conn.cursor()
    
        # Replace 'users' with your actual table name and 'username' and 'password' with the column names in your table
        cursor.execute("SELECT * FROM emp WHERE usename = ? AND passowrd = ?", (username, password))
        row = cursor.fetchone()
        
        if row:
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
        
        conn.close()
    except Exception as e:
        print("Error", "Database connection error: " + str(e))

# Create the main window
root = tk.Tk()
root.title("Login Page")

# Create labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Create a login button
login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack()

# Run the tkinter main loop
root.mainloop()

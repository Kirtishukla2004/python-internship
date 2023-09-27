import tkinter as tk
from tkinter import messagebox
import sqlite3

# Function to handle the login button click event
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Connect to the database (you should replace 'your_database.db' with your database file)
    conn = sqlite3.connect('tech.db')
    cursor = conn.cursor()

    # Check if the username and password match a record in the database
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login Successful", "Welcome, " + username)
        # Add your code to open the main application window here
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

    # Close the database connection
    conn.close()

# Create the main window
window = tk.Tk()
window.title("Login")
window.geometry("400x300")  # Set the window size

# Set background color
window.configure(bg="#444444")

# Create a label for the icon (replace 'icon.png' with your image file)
icon_image = tk.PhotoImage(file="login_icon.png")
icon_label = tk.Label(window, image=icon_image, bg="#444444")
icon_label.pack(pady=20)  # Add some padding

# Create a label and an entry for the username
label_username = tk.Label(window, text="Username", bg="#444444", fg="white", font=("Helvetica", 14))
label_username.pack()
entry_username = tk.Entry(window, font=("Helvetica", 14))
entry_username.pack()

# Create a label and an entry for the password
label_password = tk.Label(window, text="Password", bg="#444444", fg="white", font=("Helvetica", 14))
label_password.pack()
entry_password = tk.Entry(window, show="*", font=("Helvetica", 14))  # Mask the password with asterisks
entry_password.pack()

# Create a login button
login_button = tk.Button(window, text="Login", command=login, bg="#4CAF50", fg="white", font=("Helvetica", 14))
login_button.pack(pady=20)

# Start the Tkinter main loop
window.mainloop()

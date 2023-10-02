import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # To work with images

# Sample user database (you should use a real database)
user_database = {}

# Sample chatbot responses
chatbot_responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a chatbot, but thanks for asking!",
    "account balance": "Your account balance is $1000.",
    "recent transactions": "Your recent transactions include:\n1. Deposit: $500\n2. Withdrawal: $200",
    "bye": "Goodbye! Have a great day.",
}

def register():
    username = reg_username.get()
    password = reg_password.get()
    
    if username in user_database:
        messagebox.showerror("Registration Error", "Username already exists.")
    else:
        user_database[username] = password
        messagebox.showinfo("Registration Successful", "You are now registered.")

def login():
    username = login_username.get()
    password = login_password.get()
    
    if username in user_database and user_database[username] == password:
        open_account(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def open_account(username):
    account_window = tk.Toplevel(root)
    account_window.title(f"Bank Account - {username}")
    
    def send_message():
        user_input = chat_input.get()
        response = get_chatbot_response(user_input)
        chat_output.config(state=tk.NORMAL)  # Enable editing
        chat_output.insert(tk.END, f"You: {user_input}\nBot: {response}\n\n")
        chat_output.config(state=tk.DISABLED)  # Disable editing
        chat_input.delete(0, tk.END)
    
    chat_output = tk.Text(account_window, width=40, height=10)
    chat_output.pack(padx=10, pady=10)
    chat_output.config(state=tk.DISABLED)  # Disable editing
    
    chat_input = tk.Entry(account_window, width=40)
    chat_input.pack(pady=10)
    
    send_button = tk.Button(account_window, text="Send", command=send_message)
    send_button.pack()

def get_chatbot_response(user_input):
    # Convert user input to lowercase for case-insensitive matching
    user_input = user_input.lower()
    
    # Check if the user input matches any predefined responses
    for key, response in chatbot_responses.items():
        if key in user_input:
            return response
    
    # If no predefined response matches, provide a generic response
    return "I'm not sure how to respond to that."

root = tk.Tk()
root.title("Banking System")

# Registration
reg_label = tk.Label(root, text="Registration")
reg_label.pack()

reg_username_label = tk.Label(root, text="Username:")
reg_username_label.pack()

reg_username = tk.Entry(root)
reg_username.pack()

reg_password_label = tk.Label(root, text="Password:")
reg_password_label.pack()

reg_password = tk.Entry(root, show="*")
reg_password.pack()

register_button = tk.Button(root, text="Register", command=register)
register_button.pack()

# Login
login_label = tk.Label(root, text="Login")
login_label.pack()

login_username_label = tk.Label(root, text="Username:")
login_username_label.pack()

login_username = tk.Entry(root)
login_username.pack()

login_password_label = tk.Label(root, text="Password:")
login_password_label.pack()

login_password = tk.Entry(root, show="*")
login_password.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Load the chatbot icon image
chatbot_icon_image = Image.open("login_icon.png")  # Replace with your icon file path
chatbot_icon = ImageTk.PhotoImage(chatbot_icon_image)
chatbot_button = tk.Button(root, image=chatbot_icon, command=open_account)
chatbot_button.pack()

# Start the main loop
root.mainloop()

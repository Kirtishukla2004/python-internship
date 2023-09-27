import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

# Define reflections for the chatbot (you can customize these)
reflections = {
    "I am": "you are",
    "I was": "you were",
    "I": "you",
    "my": "your",
    "you": "me",
    "your": "my",
}

# Define chat pairs for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I'm a chatbot. You can call me ChatGPT.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm just a computer program, but I'm here to assist you.",]
    ],
    [
        r"(.*) (weather|temperature) in (.*)",
        ["I'm sorry, I don't have access to real-time weather information.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand. Can you please rephrase or ask another question?",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Define a function to handle user input
def chat():
    user_input = entry.get()
    response = chatbot.respond(user_input)
    conversation.config(state=tk.NORMAL)
    conversation.insert(tk.END, "You: " + user_input + "\n")
    conversation.insert(tk.END, "Chatbot: " + response + "\n")
    conversation.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# Create the GUI window
window = tk.Tk()
window.title("Desktop Chatbot")

# Create a scrolled text widget for the conversation
conversation = scrolledtext.ScrolledText(window, width=40, height=10)
conversation.pack()

# Create an entry widget for user input
entry = tk.Entry(window, width=30)
entry.pack()

# Create a button to send user input
send_button = tk.Button(window, text="Send", command=chat)
send_button.pack()

# Start the GUI event loop
window.mainloop()

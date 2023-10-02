import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Navigation Menu")

# Function to handle navigation link clicks
def navigate(link):
    # You can define what each link does here
    # For now, let's just print the selected link
    print(f"Clicked: {link}")

# Create a frame for the navigation menu with a gray background
nav_frame = tk.Frame(root, bg="gray")
nav_frame.pack(fill=tk.X)

# Create navigation links
nav_links = ["Services", "Expense Predictor", "Insurance", "Other"]

for link in nav_links:
    link_button = tk.Button(nav_frame, text=link, command=lambda l=link: navigate(l))
    link_button.pack(side=tk.LEFT, padx=10, pady=5)

# Run the Tkinter main loop
root.mainloop()

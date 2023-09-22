import tkinter as tk
from PIL import Image, ImageTk 
root = tk.Tk()
root.title("Tkinter Background Image")

image = Image.open("krishna.jpg")  
image = image.resize((800, 600), Image.ANTIALIAS)  # Set the desired width and height

# Convert the resized image to a Tkinter PhotoImage
photo = ImageTk.PhotoImage(image)

# Create a Canvas widget to display the image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# Display the image on the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# You can add other widgets or elements on top of the canvas here

# Run the Tkinter main loop
root.mainloop()

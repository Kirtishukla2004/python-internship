import tkinter as tk
from PIL import Image, ImageTk 
import cv2

def readimg(image_filename):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread(image_filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        detected_face = Image.fromarray(cv2.cvtColor(roi_color, cv2.COLOR_BGR2RGB))
        detected_face = ImageTk.PhotoImage(detected_face)
        canvas.create_image(100, 200, anchor=tk.CENTER, image=detected_face)
        canvas.detected_face = detected_face  
        if detected_face:
            print("shown")
        else:
            print("not shown")
    
    root.update_idletasks()

root = tk.Tk()
root.title("Tkinter Background Image")

image_filename = "myphoto3.png" 
image = Image.open(image_filename)  
image = image.resize((200, 300), Image.LANCZOS)  
photo = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=photo)

button = tk.Button(root, text="Detect Face", command=lambda: readimg(image_filename))
button.pack()

root.mainloop()

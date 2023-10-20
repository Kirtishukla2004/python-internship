import cv2
import os
from tkinter import *
from PIL import Image, ImageTk

def TakeImages():
    cam = cv2.VideoCapture(0)
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    sampleNum = 0

    while True:
        ret, img = cam.read()
        faces = face_classifier.detectMultiScale(img, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('frame', img)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):  # Press 'q' to quit
            break
        elif key == ord('c'):  # Press 'c' to capture an image
            sampleNum += 1
            img_name = f"camimages/{sampleNum}.jpg"
            cv2.imwrite(img_name, img)
            print(f"Image {sampleNum} captured and saved as {img_name}.")

            # Display the saved image in a Tkinter window
            display_saved_image(img_name)

    cam.release()
    cv2.destroyAllWindows()

def display_saved_image(image_path):
    root = Tk()
    root.title("Saved Image")

    # Load the image using PIL
    img = Image.open(image_path)
    img = img.resize((400, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)

    # Create a label to display the image
    label = Label(root, image=photo)
    label.pack()

    root.mainloop()

TakeImages()

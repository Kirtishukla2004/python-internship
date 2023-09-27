import numpy as np
import cv2
import os
import os


def takeimages():
    i = 0
    if (i == 0):
        cam = cv2.VideoCapture(0)
        face_classifier = cv2.CascadeClassifier(
            'haarcascade_frontalface_default.xml')
        samplenum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                samplenum = samplenum+1
                cv2.imwrite("camimages\ "+ str(samplenum)+"jpg", gray[y:y+h, x:x+w])
                cv2.imshow("frame", img)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                elif samplenum > 60:
                    break
        cam.realease()
        cv2.destryAllWindows()
    else:
        print("no")


takeimages()

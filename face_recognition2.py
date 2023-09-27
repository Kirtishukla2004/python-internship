
import cv2
import numpy as np
import os
 
def TakeImages():        

    i=0
    if(i==0):
        cam = cv2.VideoCapture(0)
        face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #harcascadePath = "haarcascade_frontalface_default.xml"
        #detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray,1.3,5)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("camimages\ "+str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>3:
                break
        cam.release()
        cv2.destroyAllWindows() 
        
    else:
        print("no")

TakeImages()

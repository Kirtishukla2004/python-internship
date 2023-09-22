import cv2
import matplotlib.pyplot as plt
def main():
    cap=cv2.VideoCapture(0)
    if(cap.isOpened()):
        ret,frame=cap.read()
    else:
        ret=False
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title("image")
    plt.xticks([])
    plt.yticks([])
    plt.show()
    cap.release()


def video():
    windowname="live video"
    cv2.namedWindow(windowname)
    cap=cv2.VideoCapture(0)
    if(cap.isOpened()):
        ret,frame=cap.read()
    else:
        ret=False
    while(ret):
        ret,frame=cap.read()
        cv2.imshow(windowname,frame)
        if cv2.waitKey(1)==27:
            break
    cv2.destroyAllWindows()
    cap.release()

video()
#esc is used shut the window 
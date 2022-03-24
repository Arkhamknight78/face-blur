import cv2
from cv2 import VideoCapture
from cv2 import waitKey
cap=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    success,img=cap.read()
    faces=face_cascade.detectMultiScale(img,1,2,4)
    for (x,y,w,h)in faces:
        ROI=img[y:y+h, x:x+w]
        blur=cv2.GaussianBlur(ROI,(91,91),0)
        img[y:y+h, x:x+h]=blur
    if faces==():
        cv2.putText(img,'No Face Found!',(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
    cv2.imshow('Face Blur',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()

import cv2 


face_clf = cv2.CascadeClassifier("Haarcascades/haarcascade_frontalface_default.xml")
eyes_clf =  cv2.CascadeClassifier("Haarcascades/haarcascade_eye.xml")


def detect(gray,frame):
    faces = face_clf.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(127,0,255),2)
        gray_points = gray[y:y+h,x:x+w]
        img_points = frame[y:y+h,x:x+w]
        eyes = eyes_clf.detectMultiScale(gray_points,1.3,5)
        for (ex,ey,ew,eh) in  eyes:
            cv2.rectangle(img_points,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
    return frame







videocapture = cv2.VideoCapture(0)

while True :
    _, frame = videocapture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow("canvas",canvas)
    if cv2.waitKey(1) == ord("q"):
        break 
videocapture.release()
cv2.destroyAllWindows()
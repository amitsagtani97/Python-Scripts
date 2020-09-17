import datetime
import cv2

now = datetime.datetime.now()

filename = str(now).split(".")
filename = filename[0].replace(':','-')
filename = filename.replace(' ','--')
filename = "".join((filename,'.jpg'))

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()
cv2.imwrite("/home/username/Images/"+filename,frame)

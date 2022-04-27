import cv2
import time

cap = cv2.VideoCapture(1)

while(cap.isOpened()):
 
    ret, frame = cap.read()
 
    frame = cv2.resize(frame, (500, 300))
 
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()

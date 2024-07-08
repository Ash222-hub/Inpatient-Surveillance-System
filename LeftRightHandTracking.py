import cv2 as cv
from cvzone import HandTrackingModule

cap = cv.VideoCapture(0)

detector=HandTrackingModule.HandDetector()

while True:
    ret,img =cap.read()
    hands,img =detector.findHands(img)
    
    cv.imshow("Hands Detected",img)
    
    if cv.waitKey(1) == ord('x'):
        break
    
cap.release()
cv.destroyAllWindows()
    
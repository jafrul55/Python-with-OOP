# computer version - cv
import cv2

#10-3 proof_of_concept_1:
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()

    cv2.imshow('Output',frame)
    if cv2.waitKey(10) == ord('q'):
        break

cap.release()  #after complete release to cap
cv2.destroyAllWindows() #and destroy cv2






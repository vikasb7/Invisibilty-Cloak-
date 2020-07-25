#Vikas Bhat
# invisible cloak 

import cv2
import numpy as np 
import time


# number of cameras
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('harry.avi' , fourcc, 20.0, (640,480))
time.sleep(2)
background = 0

# for background

for i in range(30):
    ret, background = cap.read()#capturing image
while(cap.isOpened()):
    ret, img = cap.read()
    
    # webcam closed
    if not ret:
        break

    # converting bgr to hsv
    # HSV => Hue Saturation Value
        
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    
     # HSV values
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv , lower_red , upper_red)
    
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv , lower_red , upper_red)
    
    mask1 = mask1 + mask2 

    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN ,np.ones((3,3) , np.uint8) , iterations=2)# remove noise
        
    mask2=cv2.morphologyEx(mask1, cv2.MORPH_DILATE ,np.ones((3,3) , np.uint8) , iterations=1) 
        
    mask2 = cv2.bitwise_not(mask1)
    
    res1 = cv2.bitwise_and(background, background, mask=mask1)  # segmentation of color
    res2 = cv2.bitwise_and(img, img, mask=mask2)# substittue cloak 
    
    final_output = cv2.addWeighted(res1 , 1, res2 , 1, 0)
    
    cv2.imshow('vikas' , final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
        
cap.release()
cv2.destroyAllWindows()
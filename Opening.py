import cv2
import numpy as np
image=cv2.imread('Images\Circle.png',0)
#kernel for erosion
kernel=np.ones((7,7),np.uint8)
opeaning=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
cv2.imshow('original image',image)
cv2.imshow('opened image',opeaning)
cv2.waitKey(0)
cv2.destroyAllWindows()
#opeaning is a combination of errosion followed by dialation .It is used to remove noise while keeping the structure of the object intact
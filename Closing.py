import cv2
import numpy as np
image=cv2.imread('Images\Circle.png',0)
#kernel for erosion
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
cv2.imshow('original image',image)
cv2.imshow('closed image',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
image=cv2.imread('Images\Circle.png',0)
#kernel for erosion
kernel=np.ones((5,5),np.uint8)
closing=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
cv2.imshow('original image',image)
cv2.imshow('gradient image',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
#diff btw the dialation and errosion of an image .it highlights the edges of objects
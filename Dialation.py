#dialation adds pixles to the boundaries of the object,expanding it . it is used to fill small holes ang gaps
import cv2
import numpy as np
image=cv2.imread('Images\Circle.png',0)
#kernel for erosion
kernel=np.ones((3,3),np.uint8)
dialation=cv2.dilate(image,kernel,iterations=4)
cv2.imshow('original image',image)
cv2.imshow('dialated image',dialation)
cv2.waitKey(0)
cv2.destroyAllWindows()
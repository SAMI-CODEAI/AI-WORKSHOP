import cv2
import numpy as np
image=cv2.imread('Images\Circle.png',0)
#kernel for erosion
kernel=np.ones((3,3),np.uint8)
erosion=cv2.erode(image,kernel,iterations=5)
cv2.imshow('original image',image)
cv2.imshow('Eroded image',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
#erosion removes pixeles from the boundaries of the foreground object,shriinking the object.It is usseful for removing smakk white noise
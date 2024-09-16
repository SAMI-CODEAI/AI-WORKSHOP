import cv2
image= cv2.imread(r"C:\SAMI\AI WORKSHOP\Images\cat.jpg")
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#binary thresholding
#all pixel values 127 will be converted to 225(white),and below to 0(black)
# 0,255,rgb(0,0,0)
#_, is a place holder ,the thresdhold function is in the form of tuple ,(val1,val2) to ignor val1 we give _,
_, threshold_image=cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
cv2.imshow('gray scale image',gray_image)
cv2.imshow('threshold image',threshold_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
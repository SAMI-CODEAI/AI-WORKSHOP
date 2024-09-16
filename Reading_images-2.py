import cv2

image= cv2.imread(r"C:\SAMI\AI WORKSHOP\Images\cat.jpg")
width, height = 400,100
resized_image=cv2.resize(image,(width,height))
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
flipped_image=cv2.flip(image,0)  # the '0' or '1' is for inverting on axis

#Flipped and gray image together
grayFlip=cv2.flip(image,0)
co_flip=cv2.cvtColor(grayFlip,cv2.COLOR_BGR2GRAY)
rezi=cv2.resize(co_flip,(200,500))

# Gaussian blur to reduce noise and improve edge detection
blurred_image=cv2.GaussianBlur(gray_image,(7,7),0)

#Performing canny edge detection
edges=cv2.Canny(blurred_image,100,200)

cv2.imshow('Original Image',image)
cv2.imshow('resized Image',resized_image)
cv2.imshow('Gray Image',gray_image)
cv2.imshow('Flipped Image', flipped_image)
cv2.imshow('Canny edge Image',edges)
cv2.imshow('Blurred Image',blurred_image)
cv2.imshow('The gray,flipped and resized, fliped and resize',rezi)
cv2.imshow('Fliped and gray Image',co_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()

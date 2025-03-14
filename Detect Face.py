import cv2

#pre trained model used by openCV for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#load an image
image=cv2.imread(r'C:\SAMI\AI WORKSHOP\Images\faces.jpg')

#Image to grayscale
gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Detect faces in grayscale image
faces=face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

#Draw rectanges arounf the detected faces
for(x, y, w, h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('Faces Detected', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
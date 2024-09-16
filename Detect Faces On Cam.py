import cv2

#pre trained model used by openCV for face detection
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

#open webcam
cap=cv2.VideoCapture(0)
while True:
    #read a frame from the video stream
    ret,frame=cap.read()
    #Image to grayscale
    gray_image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect faces in grayscale image
    faces=face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

    #Draw rectanges arounf the detected faces
    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        #detect the frame with detected faces
    cv2.imshow('face recognition',frame)

    #break the loop if'q' is pressed
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
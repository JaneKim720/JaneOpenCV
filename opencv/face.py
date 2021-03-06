import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('faces.jpg')

faces = face_cascade.detectMultiScale(img, 1.2, 5) 
for (x, y, w, h) in faces:

    #cv2.circle(img,(447,63), 63, (0,0,255), -1)
    cv2.circle(img,((2*x+w)/2,(2*y+h)/2),63,(153,0,255),3)
    #cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)  
  

# cv2.imwrite("heeh.jpg", img);

cv2.imwrite("stupid_face.jpg", img)

cv2.imshow('img',img)
cv2.waitKey(0)       # delay the program until getting typing input value
cv2.destroyAllWindows()
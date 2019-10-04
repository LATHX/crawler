# use face recognition iterator image face
import face_recognition
import cv2 as cv
image = face_recognition.load_image_file('img/1.jpg')
imageCV = cv.imread('img/1.jpg')
faceLocation = face_recognition.face_locations(image)
print(faceLocation)
for pos in faceLocation:
    cv.rectangle(imageCV,(pos[3],pos[0]),(pos[1],pos[2]),(0,255,0),4)
cv.imshow('img',imageCV)
cv.waitKey(0)
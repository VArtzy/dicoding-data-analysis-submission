# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
import cv2


cam = cv2.VideoCapture(0)
# atur ukuran webcam
cam.set(3, 640) # ubah lebar cam
cam.set(4, 480) # ubah tinggi cam

# panggil detector algoritmanya (mengambil file haarcascade)
facedetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    retV, frame = cam.read()
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = facedetector.detectMultiScale(Gray, 1.3, 5) #frame, scaleFactor, MinNeighbors
    for (x, y, w, h) in face:
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    cv2.imshow('webcam2', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27 or k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
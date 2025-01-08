# Import modulenya
import cv2

# Membaca cam / video kita
cam = cv2.VideoCapture(0)
# menangkap dan mengulangi frame
while True:
    # CAPTURE frame by frame  (Read)
    retV, frame = cam.read()
    # Buat warna abu abu
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # mengambil lalu mencetak keluar cam
    cv2.imshow('webcam2', Gray)
    # variable k
    k = cv2.waitKey(1) & 0xFF
    # membuat button supaya tidak loop terus
    if k == 27 or k == ord('q'):
        break
# agar memori terjaga, release cameranya, lalu destroy cam agar tidak tersimpan dan membebani laptop
cam.release()
cv2.destroyAllWindows()
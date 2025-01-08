# Import modulenya
import cv2

# Membaca cam / video kita
cam = cv2.VideoCapture(0)
# menangkap dan mengulangi frame
while True:
    # CAPTURE frame by frame  (Read)
    retV, frame = cam.read()
    # mengambil lalu mencetak keluar cam
    cv2.imshow('webcam', frame)
    # membuat button supaya tidak loop terus
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# agar memori terjaga, release cameranya, lalu destroy cam agar tidak tersimpan dan membebani laptop
cam.release()
cv2.destroyAllWindows()
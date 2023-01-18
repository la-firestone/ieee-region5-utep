import cv2
from djitellopy import Tello
import time

tello = Tello()
tello.connect()
detector = cv2.QRCodeDetector()
tello.streamon()

batt = tello.get_battery()
print(batt)

# create the video object
cap = tello.get_video_capture()

time.sleep(1)
#tello.takeoff()
for i in range(1000):
    # take a picture
    ret, frame = cap.read()

    # scan qr code
    data, bbox, _ = detector.detectAndDecode(frame)
    # data is the message , bbox is the bounding box

    if bbox is not None:
        if data:
            print("[+] QR Code detected, data:", data)

    cv2.imshow('frame', frame)
    # displaying frame will slow down the program only use this
    # for visual inspect that image is even showing the QR code

    # this is for displaying
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




tello.streamoff()
#tello.land()
# release
cap.release()
cv2.destroyAllWindows()
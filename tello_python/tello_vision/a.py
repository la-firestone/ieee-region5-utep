from djitellopy import tello
from time import sleep
import cv2

tello = Tello()
tello.connect()
tello.streamon()

# Open a capture object with open CV
cap = cv2.VideoCapture(tello.get_udp_video_address())

div = 4

while True:
    ret, frame = cap.read()
    if (ret):
        height, width, channel = frame.shape
        frame = cv2.resize(frame, (int(width / div), int(height / div)))
        cv2.imshow('Tello', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    

import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
from djitellopy import Tello

# Goal for this module is to give the drone the ability to read & scan QR codes

# iICO: initialize, Input, Compute, Output

# initialization process: initialize the drone, opencv, and pyzbar
tello = Tello()
tello.connect()
tello.streamon()

cap = cv2.VideoCapture(tello.get_udp_video_address())

div = 1 

# Inputs: The inputs in this system is the data from the stream
# Computations: The computations required for this system to work is the ability to detect & scan QR codes.
# Outputs: The outputs in this system is the text detected from the scanned QR code and the window to stream the video.
# The video stream is recursive. (The outputs are fed back to the system as new inputs.)

while True:

    (ret, frame) = cap.read()
    h1, w1 = frame.shape[0], frame.shape[1] # error here for some reason. It worked EXACTLY ONE TIME. I run it again with no changes and spewed out an error in this line.

    # scan qr code
    text = pyzbar.decode(frame)
    for texts in text:
        textdate = texts.data.decode('utf-8')
        print(textdate)
        (x, y, w, h) = texts.rect
        cx = int(x + w / 2)
        cy = int(y + h / 2)
        cv2.circle(frame, (cx, cy), 2, (0, 255, 0), 8)
        print(cx, cy)
        coordinate = (cx, cy)
    
    if (ret):
        height, width, channel = frame.shape
        frame = cv2.resize(frame, (int(width / div), int(height / div)))
        cv2.imshow('Tello', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

import cv2
from djitellopy import Tello
from pyzbar.pyzbar import decode

# Initialize Tello drone and its camera
tello = Tello()
tello.connect()
tello.streamon()

# Start capturing frames from Tello's camera
cap = cv2.VideoCapture('udp://@0.0.0.0:11111')

# Loop through frames and scan for QR codes
while True:
    # Read a frame from Tello's camera stream
    ret, frame = cap.read()

    # Decode any QR codes in the frame
    qr_codes = decode(frame)

    # Draw a bounding box and label around each detected QR code
    for qr in qr_codes:
        (x, y, w, h) = qr.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, qr.data.decode("utf-8"), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with bounding boxes and labels
    cv2.imshow('Tello Camera', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
tello.streamoff()
tello.end()
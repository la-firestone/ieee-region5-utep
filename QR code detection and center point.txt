import cv2
from pyzbar import pyzbar

#video capture
camera = cv2.VideoCapture(0)
div = 1
while True:
    (grabbed, frame) = camera.read()
    h1, w1 = frame.shape[0], frame.shape[1]

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

        # location
        cv2.putText(frame, 'QRcode_location' + str(coordinate), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


        # line between center of screen and center of qr code
        cv2.line(frame, (cx, cy), (int(w1 / 2), int(h1 / 2)), (255, 0, 0), 2)

        cv2.line(frame, texts.polygon[0], texts.polygon[1], (255, 0, 0), 2)
        cv2.line(frame, texts.polygon[1], texts.polygon[2], (255, 0, 0), 2)
        cv2.line(frame, texts.polygon[2], texts.polygon[3], (255, 0, 0), 2)
        cv2.line(frame, texts.polygon[3], texts.polygon[0], (255, 0, 0), 2)





    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("./frame.jpg", frame)
        break
# release
camera.release()
cv2.destroyAllWindows()
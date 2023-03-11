import cv2
from djitellopy import tello
# from utils_qr import *

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

me.takeoff()

while True:

    # VAR IMG GETS THE FRAME EVERY 1 MS AND DISPLAYS IT BACK TO USER

    # img = me.get_frame_read().frame
    # img = cv2.resize(img, (360, 240))
    # cv2.imshow(" MIS OJITOS ", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break

# THERE'S CURRENTLY NO EXIT CONDITION SO CODE WILL RUN INDEFINITELY UNTIL YOU MANUALLY STOP RUNNING IT


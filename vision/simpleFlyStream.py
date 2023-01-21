import cv2
from djitellopy import tello

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon()

me.takeoff()

while True:

    # VAR IMG GETS THE FRAME EVERY 1 MS AND DISPLAYS IT BACK TO USER

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow(" MIS OJITOS ", img)
    cv2.waitKey(1)

# THERE'S CURRENTLY NO EXIT CONDITION SO CODE WILL RUN INDEFINITELY UNTIL YOU MANUALLY STOP RUNNING IT


import cv2
from djitellopy import Tello
from myUtiTest import vidStream

# Setup and connect Tello

tello = Tello()
tello.connect()
tello.get_battery()

tello.takeoff()
vidStream()
cv2.waitKey(5)
tello.rotate_clockwise(360)
tello.land()

exit()




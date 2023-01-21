from djitellopy import Tello
import cv2
import time

#############################################################
width = 320 # WIDTH OF IMAGE
height = 240 # HEIGHT OF IMAGE
startCounter = 0 # 0 FOR FLIGHT, 1 FOR TESTING
#############################################################



# CONNECT TO TELLO

me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

print(me.get_battery())

me.streamoff()
me.streamon()

while True:

    # GET THE IMAGE FROM TELLO

    frame_read = me.get_frame_read()
    myFrame = frame_read.frame
    img = cv2.resize(myFrame, (width, height))

    # TO GO UP IN BEGINNING
    if startCounter == 0:
        me.takeoff()
        me.move_left(20)
        time.sleep(2)
        me.move_right(20)
        time.sleep(2)
        me.rotate_clockwise(360)
        startCounter = 1

    # SEND VELOCITY VALUES TO TELLO
    # if me.send_rc_control:
    #       me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)

    # DISPLAY IMAGE
    cv2.imshow("MyResult", img)

    # WAIT FOR THE 'Q' BUTTON TO STOP
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break



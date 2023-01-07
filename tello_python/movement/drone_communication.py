from djitellopy import tello
from time import sleep

me = tello.Tello() # create an instance of tello. Called 'me' in this case
me.connect()
print(me.get_battery())
try:
    me.takeoff()
    me.send_rc_control(left_right_velocity= 0, forward_backward_velocity=10, up_down_velocity=0, yaw_velocity=0)
    me.get_mission_pad_distance_x
    me.get_mission_pad_distance_y
    me.get_acceleration_z
    sleep(2)
    me.send_rc_control(0, 0, 0, 0)
    me.land()
finally:
    me.land()


from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()
"""
For this program make sure you are using the EDU 
and you have one the mission pads
have the drone takeoff from the mission pad
"""
tello.enable_mission_pads()

tello.move_forward(100)
x_dist = tello.get_mission_pad_distance_x()
y_dist = tello.get_mission_pad_distance_y()

"""
When tested we measure about 35 inches and it said 29
6.5 inches y axis 37.8 inches x
Estimated values x = 38  ,  y = 9

"""
print(x_dist, " , ", y_dist)
#tello.move_forward(100)

tello.land()

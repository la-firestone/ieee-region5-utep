from djitellopy import Tello
import cv2
import pandas as pd
import pyzbar.pyzbar as pyzbar

def initialize_Tello():

    miner5 = Tello()
    miner5.connect()
    miner5.for_back_velocity = 0
    miner5.left_right_velocity = 0
    miner5.up_down_velocity = 0
    miner5.yaw_velocity = 0
    miner5.speed = 0
    print(miner5.get_battery())
    miner5.streamoff()
    miner5.streamon()
    return miner5

def tello_Scan_QR(miner5):
    img = miner5.get_frame_read()
    font = cv2.FONT_HERSHEY_PLAIN
    img = img.frame
    decodedObjects = pyzbar.decode(img)
    for obj in decodedObjects:
        # print("Data", obj.data)
        cv2.putText(img, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
    return img
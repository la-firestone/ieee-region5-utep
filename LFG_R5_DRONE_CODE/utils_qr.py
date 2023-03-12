from djitellopy import Tello
import cv2
# import pandas as pd
import pyzbar.pyzbar as pyzbar
from pygame import time


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


def tilt(miner5):

    # Set the speed to a low value to ensure smooth movement
    miner5.set_speed(10)

    # Send the command to tilt the drone forward at a 45 degree angle
    miner5.rc_control(0, 20, 0, 0)

    # Wait for a short time to let the drone tilt
    time.sleep(5)

    # Send a command to bring the drone back to its normal position
    miner5.rc_control(0, -20, 0, 0)

    # Wait for a short time to let the drone reset to its normal position
    time.sleep(2)

    # Send a command to stop the drone's movement
    miner5.rc_control(0, 0, 0, 0)

    # return miner5

# implement show_battery() and battery_value() into the function
#


# ==========================================================
# ===================== [ TESTING ] ========================
# ==========================================================

# def display_test_view(miner5):
#     img = miner5.get_frame_read()
#     battery = show_battery()
#     font = cv2.FONT_COMIC_SANS
#     img = img.frame
#     decodedObjects = pyzbar.decode(img)
#     for obj in decodedObjects:
#         # print("Data", obj.data)
#         cv2.putText(img, str(obj.data), (50, 50), font, 2,
#                     (255, 0, 0), 3)
#     return img

# def display_test_view(miner5):
#     # Get image frame from drone
#     img = miner5.get_frame_read()
#
#     # Get battery percentage from drone
#     battery = show_battery(miner5)
#
#     # Add battery percentage to the image frame
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img.frame, 'Battery: {}%'.format(battery), (10, 30), font, 1, (0, 255, 0), 2)
#
#     # Decode QR codes in the modified image frame
#     decodedObjects = pyzbar.decode(img.frame)
#
#     # Draw bounding boxes around QR codes
#     for obj in decodedObjects:
#         cv2.rectangle(img.frame, obj.rect.left_top, obj.rect.right_bottom, (0, 255, 0), 2)
#
#     # Draw center point of image frame
#     height, width, _ = img.frame.shape
#     cv2.circle(img.frame, (int(width / 2), int(height / 2)), 5, (0, 0, 255), -1)
#
#     # Return the modified image frame
#     return img.frame

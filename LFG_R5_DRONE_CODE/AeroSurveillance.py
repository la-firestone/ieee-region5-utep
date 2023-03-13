from djitellopy import Tello
import cv2
from utils_qr import *
from test_diagnostics import *
# MAIN FUNCTION TO PERFORM: Fly and Scanning (synchronous), FlyBy, AeroSurveillance,
# MAIN FUNCTIONS in use
# run_ae()
# update_ae()
# aero_surveillance()
# tello_scan_ae()


# MAIN CODE
drone = Tello()

is_running = True


def run_ae(drone):
    while is_running:
        # print("Enter Input")
        update_ae(drone)


def update_ae(drone):
    # fly: 1. takeoff 2.
    # scan: 1. scan qr 2. put info into array 3. send info to Rover 4. go scan next qr
    aero_surveillance(drone)
    # drone.takeoff()
    # drone.tello_Scan_ae(drone)


def aero_surveillance(drone):
    drone.takeoff()
    tello_scan_ae(drone)


# def live_feed(drone):
#     while True:
#         img = tello_Scan_QR(drone)
#         tello_Scan_ae(drone)


def tello_scan_ae(miner5):
    img = miner5.get_frame_read()
    font = cv2.FONT_HERSHEY_PLAIN
    img = img.frame
    decoded_objects = pyzbar.decode(img)
    for obj in decoded_objects:
        # print("Data", obj.data)
        cv2.putText(img, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
        cv2.putText(img, str(miner5.get_battery()), (10, 30), font, 1, (0, 255, 0), 2)

    return img

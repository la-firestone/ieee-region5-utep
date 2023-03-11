from djitellopy import Tello
import cv2
from utils_qr import *

# Fly and Scanning (Syncronys), FlyBy, AeroSurvalience,

drone = Tello()

is_running = True

def run_ae(drone):
    while is_running:
        # print("Enter Input")
        update_ae(drone)


def update_ae(drone):
    # fly: 1. takeoff 2.
    # scan: 1. scan qr 2. put info into array 3. send info to Rover 4. go scan next qr
    drone.takeoff()

    while True:
        img = tello_Scan_QR(drone)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            drone.land()
            break


def tello_Scan_ae(miner5):
    img = miner5.get_frame_read()
    font = cv2.FONT_HERSHEY_PLAIN
    img = img.frame
    decodedObjects = pyzbar.decode(img)
    for obj in decodedObjects:
        # print("Data", obj.data)
        cv2.putText(img, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
        cv2.putText(img, str(miner5.get_battery()), (10, 30), font, 1, (0, 255, 0), 2)

    return img


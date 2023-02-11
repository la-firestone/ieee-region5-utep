from utils_qr import *
import cv2
import pyzbar.pyzbar as pyzbar
import pandas as pd


miner5 = initialize_Tello()

while True:
    img = tello_Scan_QR(miner5)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        miner5.land()
        break
from utils_qr import *
from test_diagnostics import run
# import cv2
# import pyzbar.pyzbar as pyzbar
# import pandas as pd
# from test_diagnostics import *  # ===[TESTING]===


######### start: test_diagnostics ############
miner5 = initialize_Tello()

run(miner5)
# has 'test' button
# 'test' is flying and scanning(QR)


######### end: test_diagnostics ############



######### start: AeroSurveillance ############



######### end: AeroSurveillance ############


# while True:
#     img = tello_Scan_QR(miner5)
#     cv2.imshow('Image', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         miner5.land()
#         break


# ORIGINAL CODE
# while True:
#     img = tello_Scan_QR(miner5)
#     cv2.imshow('Image', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         miner5.land()
#         break


# ==========================================================
# ===================== [ TESTING ] ========================
# ==========================================================


# ===[TEST: 2]===

# while True:
#     # Get image frame and battery percentage
#     img = tello_Scan_QR(miner5)
#     battery = show_battery(miner5)
#
#     # Add battery percentage to image frame
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img, 'Battery: {}%'.format(battery), (10, 30), font, 1, (0, 255, 0), 2)
#
#     # Concatenate image frame and battery percentage images horizontally
#     battery_img = cv2.putText(np.zeros_like(img), 'Battery: {}%'.format(battery), (10, 30), font, 1, (0, 255, 0), 2)
#     concatenated = cv2.hconcat([img, battery_img])
#
#     # Show concatenated image
#     cv2.imshow('Image with Battery', concatenated)
#
#     # Break loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         miner5.land()
#         break


# ===[TEST: 1]===

# while True:
#     # Get image frame from drone
#     img = tello_Scan_QR(miner5)
#
#     # Get battery percentage from drone
#     battery = show_battery(miner5)
#
#     # Add battery percentage to the image frame
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img, 'Battery: {}%'.format(battery), (10, 30), font, 1, (0, 255, 0), 2)
#
#     # Display the modified image frame
#     cv2.imshow('Tello Stream', img)
#
#     # Break the loop if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         miner5.land()
#         break
#
# # Release resources and close windows
# cv2.destroyAllWindows()


# ===[TEST: 0]===

# while True:
#     img = tello_Scan_QR(miner5)
#     battery = show_battery(miner5)
#     cv2.imshow('Image', img)
#     cv2.imshow('Battery', battery)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         miner5.land()
#         break
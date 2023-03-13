from djitellopy import Tello
# import cv2
# import pandas as pd
# import pyzbar.pyzbar as pyzbar
# from time import sleep

##### Version 2 #####

drone = Tello()

is_running = True
start_battery = drone.get_battery

def run(drone):
    while is_running:
        print("Enter Input")
        update(drone)

 # Run is a function that, when running, it constantly checks the updating function


def update(drone):
    users_movement(drone)


def users_movement(drone):
    # Wait for user input
    user_input = input("Press:  'w', 's', 't', 'b' or 'q': ")
    print("Or Type:  'up', 'land', 'hover', 'test', or 'quit': ")
    print("(Hit ENTER after to execute the action)")
    while True:
        # user_input = input("Press 'w', 's', 't', 'b' or 'q' to continue: ")
        if user_input in ['up', 'w', 'land', 's', 'hover', 'h', 'test', 't', 'b', 'quit', 'q']:
            break

    # Do something do on user input
    # if user_input == '?':
    if user_input == 'test' or user_input == 't':
        print("You Pressed '? test or t'")
        current_power(drone)
        # drone.takeoff()
        # time.wait(5)
        # drone.land()
    # elif user_input == 'menu' or user_input == 'm':
    #     print("You Pressed ' menu or m'")
    #     full_menu()
    elif user_input == 'up'or user_input == 'w':
        print("You Pressed 'up or w'")
        current_power(drone)
        drone.takeoff()
    elif user_input == 'land'or user_input == 's':
        print("You Pressed 'land or s'")
        current_power(drone)
        drone.land()
    elif user_input == 'hover' or user_input == 'h':
        print("You Pressed 'hover or h'")
        current_power(drone)
        # TILT FUNCTION
        # drone.land()
    elif user_input == 'b':
        print("You Pressed 'b'")
        print("Drone Battery Percentage: " + str(drone.get_battery()) + "%")
    elif user_input == 'quit' or user_input == 'q':
        # is_running = False
        print("You pressed 'quit or q'")
        drone.land()
        current_power(drone)
        power_drained(start_battery, drone)
        global is_running
        is_running = False
        # Handle 'q' key
        # print("You pressed 'q'!")


# BATTERY LEVELS

def power_drained(start_battery, drone):
    end_battery = drone.get_battery
    flight_power_usage = start_battery - end_battery
    print("Power Drained From Flight : " + str(flight_power_usage) + "%")

def current_power(drone):
    while is_running:
        print("Current Power Level: " + str(drone.get_battery()) + "%")

# LIST OF TASKS ##### scrapped ########
# put user input into array
# print array in user_input = input ("")
# use array for 'if user_input in [array]
    # this will need to change the inputs in the console
    # ... to be numbers instead of strings entered

# ##### MENUS #####
# short_menu = ['w', 's', 'h', 't', 'b', 'q', 'm']
# whole_word_menu = ['up', 'land', 'hover', 'test', 'quit', 'menu']
# full_menu = ['up', 'w',  'land', 's', 'hover', 'h', 'test', 't', 'b', 'quit', 'q']

# Menu: 1.Full Menu (tab spaced), 2.Quick Menu (Just characters, no tab space)

# Updated users_movement function. (Implemented arrays into list)

# original placed above users_movement function
# SCRAPPED FUNCTIONS #############
# def users_selections(drone):
#     user_input = input()
#     print()


# def printin_array(array, index):
#     print(array[index])


# def full_menu():
#
#     short_menu = ['w', 's', 'h', 't', 'b', 'q', 'm']
#     whole_word_menu = ['up', 'land', 'hover', 'test', 'quit', 'menu']
#     full_menu = ['up', 'w',  'land', 's', 'hover', 'h', 'test', 't', 'b', 'quit', 'q']
# SCRAPPED FUNCTIONS #############
# def up_n_down():

    ############################################################################

    # from djitellopy import Tello
    # import time
    # import cv2
    #
    #
    # # chatGPT answer
    #
    # # Define a function to check for battery percentage decrease by 1%
    #
    #
    # def show_battery(miner5):
    #
    #     # Connect to Tello drone
    #     miner5.connect()
    #     time.sleep(2)
    #
    #     # Continuously check battery percentage
    #     prev_battery = 0
    #     while True:
    #         battery = miner5.get_battery()
    #         if battery != prev_battery and battery % 1 == 0:
    #             if battery < prev_battery:
    #                 print(miner5.get_battery())
    #                 cv2.putText()
    #             prev_battery = battery
    #         time.sleep(1)
    #         return battery                                  # is the battery value is INT!!!!!!!
    #
    #
    # # put inside utils tello_Scan_QR
    #
    # def battery_value(img, battery):
    #     font = cv2.FONT_HERSHEY_PLAIN
    #     text = int(battery)                                 # is the battery value is INT!!!!!!!
    #     text_size = cv2.getTextSize(text, font, 2, 3)
    #     height, width = img.shape
    #     margin = 10
    #     x = width - text_size[0] - margin
    #     y = height - text_size[1] - margin
    #     cv2.putText(img, text, (x, y), font, 2, (0, 0, 255), 3)
    #     return img

#################################################

# import cv2
# from djitellopy import tello
# from utils_qr import *

# me = tello.Tello()
# me.connect()
# print(me.get_battery())
# me.streamon()

# me.takeoff()


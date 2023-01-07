from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()

while True:
    img = me.get_frame_read().frame # you can rezise image if you want to process it faster
    #img = cv2.resize(img, (360, 240)) 
    cv2.imshow("Image", img)
    cv2.waitKey(1) #frame shuts down before you see it if you don't delay it
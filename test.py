import keyboard
from djitellopy import tello

me = tello.Tello()

me.connect()
print(me.get_battery())
print(me.get_barometer())

while True:
    me.streamon()

    if keyboard.read_key() == 'q':
        me.streamoff()
        break

exit()

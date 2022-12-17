# Clicky key virtual LED bubble wrap
#
# 1. Have USB at top, that way LED show best
# 2. Power-on with rainbow pattern
# 3. Press a key and it will turn off/on
# 4. You can press multiple keys at a time
# 5. Hold top left key for 1 second to turn all red
# 6. Next keys will do all green, blue, white, cyan, yellow, magenta and rainbow
#
# Drop the `pmk` folder into your `lib` folder on your `CIRCUITPY` drive.

from pmk import PMK
from pmk.platform.keybow2040 import Keybow2040 as Hardware         # for Keybow 2040
# from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware # for Pico RGB Keypad Base
import time

keybow = PMK(Hardware())
keys = keybow.keys

red = (255, 0, 0)
gre = (0, 255, 0)
blu = (0, 0, 255)
cya = (0, 127, 127)
yel = (127, 127, 0)
mag = (127, 0, 127)
whi = (127, 127, 127)

# Because I prefer the keyboard with USB at top, the layout is:
#
#   03 07 11 15
#   02 06 10 14
#   01 05 09 13
#   00 04 08 12

def multi():
    keys[03].set_led(*red)
    keys[07].set_led(*gre)
    keys[11].set_led(*blu)
    keys[15].set_led(*whi)

    keys[02].set_led(*gre)
    keys[06].set_led(*red)
    keys[10].set_led(*whi)
    keys[14].set_led(*blu)

    keys[01].set_led(*blu)
    keys[05].set_led(*whi)
    keys[09].set_led(*red)
    keys[13].set_led(*gre)

    keys[00].set_led(*whi)
    keys[04].set_led(*blu)
    keys[08].set_led(*gre)
    keys[12].set_led(*red)

multi()
keybow.update()

for key in keys:
    key.hold_time=1
    
    @keybow.on_press(key)
    def press_handler(key):
#       print("Key {} pressed".format(key.number))
        key.toggle_led()

#   @keybow.on_release(key)
#   def release_handler(key):
#       print("Key {} released".format(key.number))

    @keybow.on_hold(key)
    def hold_handler(key):
#       print("Key {} held".format(key.number))
        if key.number==3: # Red
            keybow.set_all(*red)
        if key.number==7: # Green
            keybow.set_all(*gre)
        if key.number==11: # Blue
            keybow.set_all(*blu)
        if key.number==15: # White
            keybow.set_all(*whi)
        if key.number==2: # Cyan
            keybow.set_all(*cya)
        if key.number==6: # Yellow
            keybow.set_all(*yel)
        if key.number==10: # Magenta
            keybow.set_all(*mag)
        if key.number==14: # Multi
            multi()
            
while True:
    keybow.update()
    time.sleep(1.0 / 60)

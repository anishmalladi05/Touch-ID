import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Set up Pin 3 (D3) as custom ground
custom_ground = digitalio.DigitalInOut(board.D3)
custom_ground.direction = digitalio.Direction.OUTPUT
custom_ground.value = False

# Set up Pin 0 (D0) as input switch
switch = digitalio.DigitalInOut(board.D0)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

print("Ready!")

while True:
    if not switch.value:
        layout.write("tpqqpwt")
        keyboard.send(Keycode.ENTER)
        
        # Wait until released
        while not switch.value:
            time.sleep(0.01)
            
        time.sleep(0.2)
        
    time.sleep(0.01)

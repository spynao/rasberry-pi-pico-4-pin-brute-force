import random
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_tr import KeyboardLayout
from keycode_win_tr import Keycode

KEY_ENTER = 0x28

Liste = [0x27, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26]

kbd = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True
time.sleep(10)

while True:

    nar1 = random.randint(0, 9)
    nar2 = random.randint(0, 9)
    nar3 = random.randint(0, 9)
    nar4 = random.randint(0, 9)

    time.sleep(1)
    kbd.press(Liste[nar1])
    time.sleep(.09)
    kbd.release(Liste[nar1])
    time.sleep(1)
    kbd.press(Liste[nar2])
    time.sleep(.09)
    kbd.release(Liste[nar2])
    time.sleep(1)
    kbd.press(Liste[nar3])
    time.sleep(.09)
    kbd.release(Liste[nar3])
    time.sleep(1)
    kbd.press(Liste[nar4])
    time.sleep(.09)
    kbd.release(Liste[nar4])
    time.sleep(1)
    kbd.press(KEY_ENTER)
    time.sleep(.09)
    kbd.release(KEY_ENTER)
    time.sleep(1)


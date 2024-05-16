import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# Make sure to install pynput. Instructions in the README file.

# Change the toggle keys and the amount of time between clicks below
#--------------------------------------------------------
TOGGLE_KEY = KeyCode(char="-")
TimeBetweeenClicks = 70
#--------------------------------------------------------


clicking = False
mouse = Controller()

def clicks():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(TimeBetweeenClicks)

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking    

click_thread = threading.Thread(target=clicks)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()

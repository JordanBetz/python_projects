from pynput import keyboard
import time

f_hold = False

def on_press(key):
    global f_hold
    if key == keyboard.Key.shift_r:
        f_hold = not f_hold

listener = keyboard.Listener(on_press=on_press)
listener.start()

controller = keyboard.Controller()

while True:
    if f_hold:
        controller.press('f')
        time.sleep(0.01)
    else:
        controller.release('f')
    time.sleep(0.01)

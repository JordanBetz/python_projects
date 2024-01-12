import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Definiert eine Klasse ClickMouse, die von threading.Thread erbt, um Mausklicks in einem eigenen Thread zu verarbeiten.
class ClickMouse(threading.Thread):
    # Initialisiert die ClickMouse Instanz mit Verzögerung und Taste.
    def __init__(self):
        # Ruft den Konstruktor der Elternklasse Thread auf.
        self.mouse = Controller()
        self.start_stop_key = KeyCode(char='a')
        self.exit_key = KeyCode(char='b')
        self.running = False
        self.click_tread = None
        self.speed = float()
        
    def clicker(self, times=None, speed=None):
        counter = 0
        while self.running:
            if times is not None and counter >= times:
                break
            self.mouse.click(Button.left, 1)
            print(f"{counter + 1}")
            counter += 1
            time.sleep(self.intervall)

    def on_press(self, key):
        if key == self.start_stop_key:
            if self.running:
                self.running = False
                if self.click_tread is not None:
                    self.click_tread.join()
            else:
                self.running = True
                self.click_tread = threading.Thread(target=self.clicker, args=(self.times, self.speed))
                self.click_tread.start()
        elif key == self.exit_key:
            self.running = False
            if self.click_tread is not None:
                self.click_tread.join()
            return False
                        
    def run(self):
        try:
            mode = input("Which mode would you like to choose (limited/unlimited): ").strip().lower()
            if mode == "limited" or mode == "l":
                self.times = int(input("How many times would you like to click: "))
                clicks_per_second = float(input("How many times would you like to click per second: "))
                self.intervall = 1 / clicks_per_second
            elif mode == "unlimited" or mode == "u":
                clicks_per_second = float(input("How many times would you like to click per second: "))
                self.intervall = 1 / clicks_per_second
                self.times = None
            else:
                print("Invalid mode")
        except ValueError as e:
            print(f"An Error occurred {e}")
            
        print("Info: Press 'a' to start/pause the clicker. Press 'b' to end the clicker.")
        with Listener(on_press=self.on_press) as listener:
            listener.join()
            
if __name__ == "__main__":
    auto_clicker = ClickMouse()
    auto_clicker.run()
    

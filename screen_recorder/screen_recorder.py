import pyautogui
import cv2
import numpy as np
import os
from datetime import datetime

record_folder = "D:\Devlopment\Python\python_learn_projects\screen_recorder_recordings"
os.makedirs(record_folder, exist_ok=True)

resolution = (1920, 1080)

codec = cv2.VideoWriter_fourcc(*'XVID')
filename = 'recording.avi'
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 270)

recording = False

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    if recording:
        out.write(frame)
        
    cv2.imshow("Recording", frame)
    
    k = cv2.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    elif k & 0xFF == ord('r'):
        recording = not recording
        record_filename = os.path.join(record_folder , f"record_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        print(f"Record saved to {record_filename}")
    elif k & 0xFF == ord('s'):
        screenshot_filename = os.path.join(record_folder , f"screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
        pyautogui.screenshot(screenshot_filename)
        print(f"Screenshot saved to {screenshot_filename}")

out.release()
cv2.destroyAllWindows() 
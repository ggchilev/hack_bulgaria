import pyautogui
import os

pyautogui.position()

while True:
    x = pyautogui.position()[0]
    y = pyautogui.position()[1]
    if x > 1168 and y < 180:
        os.system("play -n synth 0.1 sine 800 vol 0.5")


1168, 174
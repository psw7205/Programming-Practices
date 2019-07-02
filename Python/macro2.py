import pyautogui
import time

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)

for i in range(50):
    pyautogui.moveTo(1811, 336)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1672, 519)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1811, 336)
    pyautogui.scroll(-121)
    time.sleep(1)

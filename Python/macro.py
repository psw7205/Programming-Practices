import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)

for i in range(50):
    pyautogui.moveTo(1812, 265)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1662, 377)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(911, 600)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1203, 485)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(1812, 265)
    pyautogui.scroll(-121)
    time.sleep(1)

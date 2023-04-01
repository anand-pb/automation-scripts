import pyautogui

# pyautogui.screenshot()

# pyautogui.screenshot('F:\\python_programs\\automation\\gui\\screenshot.png')

# print(pyautogui.locateOnScreen('F:\\python_programs\\automation\\gui\\fox.png'))

print(pyautogui.locateCenterOnScreen('F:\\python_programs\\automation\\gui\\fox.png'))

coord = pyautogui.locateCenterOnScreen('F:\\python_programs\\automation\\gui\\fox.png')

pyautogui.click(coord)
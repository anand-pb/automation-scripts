import pyautogui

pyautogui.size()

width, height = pyautogui.size()

print(width, height)

print(pyautogui.position())

pyautogui.moveTo(10, 10)

pyautogui.moveTo(100, 100, duration = 1.5)

pyautogui.moveRel(200, 200)

pyautogui.moveRel(300, 300, duration = 1.5)

pyautogui.click(400, 400)
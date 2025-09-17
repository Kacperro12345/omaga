import pyautogui

target = (75, 219, 106)

while True:
    rgb = pyautogui.pixel(535, 315)

    if rgb == target:
        pyautogui.leftClick()
    

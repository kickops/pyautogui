import time
import pyautogui

## Top level variables
meet_id = '939XXXXXX28'
password = '1XXXXXXXX'

pyautogui.hotkey('command', 'space')
pyautogui.typewrite('zoom')
pyautogui.hotkey('enter')

time.sleep(1)
pyautogui.hotkey('command', 'j')
time.sleep(1)
pyautogui.write(meet_id)
pyautogui.press('enter',interval=3)
pyautogui.write(password)
pyautogui.press('enter',interval=1)

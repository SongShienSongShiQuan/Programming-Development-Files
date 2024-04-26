import os
import keyboard
import time
import pyautogui

import win32api

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.01
def initiate():
    running = True
    print_text = True
    key_press = keyboard.get_hotkey_name()
    disabled = False
    pid_current = os.getpid()
    while disabled == False:

        # Left button down = 0 or 1. Button up = -127 or -128 
        state_middle_click_down = win32api.GetKeyState(0x04)
        state_left_click_down = win32api.GetKeyState(0x01)
        state_right_click_down = win32api.GetKeyState(0x02)
        ##print(f'state_middle_click_down: ', state_middle_click_down)
        if print_text == True:
            print('Press "Middle_Mouse_Button" to activate AutoClick.')
            print_text = False
        if state_middle_click_down < 0:
            print('Activated')
            pyautogui.FAILSAFE = False
            pyautogui.PAUSE = 0.01
            pyautogui.leftClick()
            print('Mouse clicked!')

if __name__ == '__main__':
    initiate()

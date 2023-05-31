import os
import keyboard
import time
import pyautogui

def initiate():
    running = True
    initialize = True
    print_text = True
    key_press = keyboard.get_hotkey_name()
    disabled = False
    pid_current = os.getpid()
    while disabled == False:
        if print_text == True:
            print('Press "]" to activate AutoClick.')
            print_text = False
        if keyboard.is_pressed(']'):
            initialize = True
            print('Activated')
            if initialize == True:
                while initialize == True:
                    pyautogui.leftClick()
                    time.sleep(0.00001)
                    print('Mouse clicked!')
                    if keyboard.is_pressed('['):
                        initialize = False
                        print('Deactivated')

if __name__ == '__main__':
    initiate()
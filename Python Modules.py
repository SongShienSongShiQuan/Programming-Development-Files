from ast import mod
import cmd
import os
from shlex import join
import subprocess
import sys
import time
import Modules_List

a = 'pip install PyAutoGUI #Used to install  modules through pip. Important modules: (hashlib, PyAutoGUI, uncompyle6, decompyle3, keyboard, customtkinter, psutil)'
b = 'uncompyle6 -o CTRL + SHIFT + Right click to open shell and enter file name'
c = 'uncompyle6 file name'
c1 = 'Convert to exe any pyton script by using the module and command in cmd, CMD ex: pyinstaller --onefile hello.py'
c2 = 'CMD ex: pyinstaller -F Mako_Software.py --collect-all customtkinter'
c3 = 'taskkill/f /im python.exe'
d = ' '
d1 = 'Installed Modules:'
#Create new line using print & add letters as varible name. For notes storage using python.
print(a)
print(b)
print(c)
print(c1)
print(c2)
print(c3)
print(d)
print(d1)
executecommand = "pip list"
command = executecommand
output = subprocess.run(command)
output2 = subprocess.run(command, capture_output=True).stdout
output2length = output2.decode("utf-8")
print('Modules Length Updated:', len(output2length))

modules_length_current = Modules_List.modules_length_actual
print('Modules Length Current Settings:', modules_length_current)

if len(output2length) == modules_length_current:
    print("Complete Core Modules")
elif len(output2length) > modules_length_current:
    print("Modules Incomplete")
    print("Allowed Input Parameters> 'update installed modules', 'cancel update installed modules', 'end'")

    new_input = (input("Input: "))
    
    if new_input.lower() == 'update installed modules':
        with open("installed_modules.txt", "w") as write_module:
            write_module.write(output2length)
    elif new_input.lower() == 'cancel update installed modules':
        modules_length_new = int(input("Enter a number: "))

        if type(modules_length_new) == int:
            print("Input Accepted")
            to_str = str(modules_length_new)
            with open("Modules_List.py", "w") as opened_file:
                opened_file.write('modules_length_actual = ' + to_str)
                print('Modules Updated To: ', to_str)
                pause = (input("..."))
            sys.exit()
    elif new_input == 'end':
        sys.exit()
elif len(output2length) < modules_length_current:
    print("Modules Has Excess")
    print("Allowed Input Parameters> 'update installed modules', 'cancel update installed modules', 'end'")
    
    new_input = (input("Input: "))
    
    if new_input.lower() == 'update installed modules':
        with open("installed_modules.txt", "w") as write_module:
            write_module.write(output2length)
    elif new_input.lower() == 'cancel update installed modules':
        modules_length_new = int(input("Enter a number: "))

        if type(modules_length_new) == int:
            print("Input Accepted")
            to_str = str(modules_length_new)
            with open("Modules_List.py", "w") as opened_file:
                opened_file.write('modules_length_actual = ' + to_str)
                print('Modules Updated To: ', to_str)
                pause = (input("..."))
            sys.exit()
    elif new_input == 'end':
        sys.exit()
pause = (input("..."))
sys.exit()

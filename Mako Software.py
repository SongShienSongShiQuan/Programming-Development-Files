from concurrent.futures import thread
from doctest import master
from pdb import run
from pydoc import doc
from re import sub
from runpy import run_module
from string import whitespace
import tkinter
from turtle import back
from types import NoneType
from webbrowser import get
import customtkinter as ctk
from pyscreeze import center
import tkinter
import pyautogui as pag
import random
import time
import keyboard
import sys
import cmd
import os
import subprocess
from PIL import Image, ImageTk, ImageFilter
import threading
import psutil

action = False
Set_Action_True = ']'
Set_Action_False = '['
win = ctk
root = ctk.CTk
anti_afk_running = True

#PATH Add path here to prevent scripts to start when added as variable
script_path_anti_afk = 'C:/Users/Chowfer/Desktop/CODE SPACE/PyAutoGUI sample, script.py'
script_path_modules = 'C:/Users/Chowfer/Desktop/CODE SPACE/Python Modules.py'
script_path_keyboard = 'C:/Users/Chowfer/Desktop/CODE SPACE/Keypress_Detection_Python.py'

#PID IDs, set variable to global in functions ex: "global pid_1"
#PID is acquired because 'script_path_example' is added as a variable and it starts the process before being called.
#Ex: 'subprocess.Popen(command).terminate()' Instead of terminating it lets the process run.
pid_1 = 0
pid_2 = 0
pid_3 = 0

class Aplikasi:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('700x700')
        self.master.resizable(False, False)
        self.master.wm_title('Mako Software')
        self.master.iconbitmap('C:/Users/Chowfer/Desktop/Mako/Square T650i Logo.ico')
        #self.master.attributes('-alpha', 0.7)
        self.master.wm_attributes('-alpha', 0.8, '-transparentcolor', 'grey')
        img_path = 'C:/Users/Chowfer/Desktop/Mako/2023-03-17 01_48_32-.png'
        openedimage = Image.open(img_path)
        blurred_image = openedimage.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blurred_image)
        background = ctk.CTkCanvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height())
        background.create_image(0, 0, anchor=ctk.NW, image=self.image)
        background.pack(fill=ctk.BOTH, expand=True)

        frame = ctk.CTkFrame(self.master, width=268, height=690, fg_color="black", corner_radius=0)
        frame.place(relx=0.195, rely=0.5, anchor='center')

        framebackgroundantiafk = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackgroundantiafk.place(relx=0.69, rely=0.1, anchor='center')

        framebackgroundclick = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackgroundclick.place(relx=0.69, rely=0.15, anchor='center')

        framebackgroundcheck_modules = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackgroundcheck_modules.place(relx=0.69, rely=0.2, anchor='center')
        
        framebackgroundcheck_keyboard_tester = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackgroundcheck_keyboard_tester.place(relx=0.69, rely=0.25, anchor='center')

        framebackgroundcheck_hbrd = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackgroundcheck_hbrd.place(relx=0.69, rely=0.3, anchor='center')

        framebackground_cpu_usage = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackground_cpu_usage.place(relx=0.69, rely=0.35, anchor='center')

        softwarename = ctk.CTkLabel(self.master, text='Xin Chào  -  Open Source GITHUB  -  Mako_Software.py', font=('Helvetica bold',26), bg_color="grey")
        softwarename.place(relx=0.5, rely=0.035, anchor='center')

        self.counter: str = '0'

        #entry = tk.Entry(root)
        #entry.pack()

        self.outputtext1 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext1.place(relx=0.45, rely=0.1, anchor='center')

        self.outputprint = ctk.CTkLabel(self.master, text='Shortcut Disabled', font=('Helvetica bold',26), bg_color="black")
        self.outputprint.place(relx=0.7, rely=0.1, anchor='center')

        self.enableantiafk = ctk.CTkButton(self.master, width=245, height=30, text='Enable Anti AFK Keyboard Shortcut', font=('Helvetica bold',10),command=self.enable_anti_afk_keyboard_shortcut, corner_radius=0, fg_color='indigo')
        self.enableantiafk.place(relx=0.185, rely=0.1, anchor='center')

        self.anti_afk_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.anti_afk_indicator.place(relx=0.375, rely=0.1, anchor='center')

        self.label = ctk.CTkLabel(self.master, text='Mouse Click Tests: 0', font=('Helvetica bold',26), bg_color="black")
        self.label.place(relx=0.7, rely=0.15, anchor='center')

        self.outputtext2 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext2.place(relx=0.45, rely=0.15, anchor='center')

        self.button = ctk.CTkButton(self.master, width=245, height=30, text='Click Counter', font=('Helvetica bold',10),command=self.increment, corner_radius=0, fg_color='indigo')
        self.button.place(relx=0.185, rely=0.15, anchor='center')

        self.outputtext3 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext3.place(relx=0.45, rely=0.2, anchor='center')

        self.check_modules_output = ctk.CTkLabel(self.master, text='.....Modules.....', font=('Helvetica bold',26), bg_color="black")
        self.check_modules_output.place(relx=0.7, rely=0.2, anchor='center')

        self.check_modules_enable = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE CHECK MODULES', font=('Helvetica bold',10),command=self.check_modules_enable_func, corner_radius=0, fg_color='indigo')
        self.check_modules_enable.place(relx=0.185, rely=0.2, anchor='center')

        self.check_modules_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.check_modules_indicator.place(relx=0.375, rely=0.2, anchor='center')
        
        self.outputtext4 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext4.place(relx=0.45, rely=0.25, anchor='center')

        self.keyboard_tester = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE TEST KEYBOARD', font=('Helvetica bold',10),command=self.enable_keyboard_tester_function, corner_radius=0, fg_color='indigo')
        self.keyboard_tester.place(relx=0.185, rely=0.25, anchor='center')

        self.outputtext4 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext4.place(relx=0.45, rely=0.3, anchor='center')

        self.hbrd_ = ctk.CTkButton(self.master, width=245, height=30, text='Hybrid Shutdown', font=('Helvetica bold',10),command=self.hbrd_function, corner_radius=0, fg_color='indigo')
        self.hbrd_.place(relx=0.185, rely=0.3, anchor='center')

        self.outputtext5 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext5.place(relx=0.45, rely=0.35, anchor='center')

        self.cpu_usage_output = ctk.CTkLabel(self.master, text='{CPU Usage: }', font=('Helvetica bold',26), bg_color="black")
        self.cpu_usage_output.place(relx=0.7, rely=0.35, anchor='center')
        
        self.cpu_usage = ctk.CTkButton(self.master, width=245, height=30, text='Get CPU Usage', font=('Helvetica bold',10),command=self.cpu_usage_function, corner_radius=0, fg_color='indigo')
        self.cpu_usage.place(relx=0.185, rely=0.35, anchor='center')

    def increment(self):
        try:
            self.counter = str(int(self.counter) + 1)
            self.label.configure(text=('Mouse Click Tests: ' + (self.counter)))
            if self.counter == '1':
                print('Mako')
            
            if int(self.counter) == 1:
                self.reset_button = ctk.CTkButton(self.master, text='Reset', font=('Helvetica bold',10), command=self.reset, corner_radius=0,fg_color='red', hover_color='darkred', width=60, height=20)
                self.reset_button.place(relx=0.92, rely=0.15, anchor='center')
        except Exception as e:
            print('Error:', e)
    def reset(self):
        try:
            self.counter = '0'
            self.label.configure(text=('Mouse Click Tests: ' + (self.counter)))
            self.reset_button.destroy()
        except Exception as m:
            print('Error:', m)
    def enable_anti_afk_keyboard_shortcut(self):
        try:
            self.outputprint.configure(text='Shortcut Enabled')
            self.enableantiafk.configure(self.master, width=245, height=30, text='Enable Anti AFK Keyboard Shortcut', font=('Helvetica bold',10), command=self.enable_anti_afk_keyboard_shortcut, corner_radius=0, fg_color='red')
            self.enableantiafk.destroy()
            self.disableantiafk = ctk.CTkButton(self.master, width=245, height=30, text='Disable Anti AFK Keyboard Shortcut', font=('Helvetica bold',10), command=self.disable_anti_afk_keyboard_shortcut, corner_radius=0, fg_color='red')
            self.disableantiafk.place(relx=0.185, rely=0.1, anchor='center')
            
            self.anti_afk_indicator.configure(self.master, width=10, height=30, fg_color="darkgreen", corner_radius=0)

            command = (script_path_anti_afk)
            print('Enabled Shortcut')


            process = subprocess.Popen(['python', command])
            process_cmd = subprocess.Popen(["cmd.exe"])

            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_3
            pid_3 = get_pid
            print(pid_3)


            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
            
            
        except Exception as c:
            print('Error:', c)

    def disable_anti_afk_keyboard_shortcut(self):
        try:
            self.outputprint.configure(text='Shortcut Disabled')
            print('Disabled Shortcut')
            self.disableantiafk.destroy()
            self.enableantiafk = ctk.CTkButton(self.master, width=245, height=30, text='Enable Anti AFK Keyboard Shortcut', font=('Helvetica bold',10), command=self.enable_anti_afk_keyboard_shortcut, corner_radius=0, fg_color='indigo')
            self.enableantiafk.place(relx=0.185, rely=0.1, anchor='center')

            self.anti_afk_indicator.configure(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)

            anti_afk_running = False
            threading.Event()


            print(pid_3)
            os.kill(pid_3, 9)

        except Exception as d:
            print('Error:', d)
    def check_modules_enable_func(self):
        try:
            self.check_modules_output.configure(self.master, text='Checking Modules', font=('Helvetica bold',26), bg_color="black")

            self.check_modules_enable.destroy()
            self.check_modules_disable = ctk.CTkButton(self.master, width=245, height=30, text='DISABLE CHECK MODULES', font=('Helvetica bold',10), command=self.check_modules_disable_func, corner_radius=0, fg_color='red')
            self.check_modules_disable.place(relx=0.185, rely=0.2, anchor='center')
            
            self.check_modules_indicator.configure(self.master, width=10, height=30, fg_color="darkgreen", corner_radius=0)

            command = (script_path_modules)
            print('Enable CHECK MODULES')

            process = subprocess.Popen(['python', command])
            process_cmd = subprocess.Popen(["cmd.exe"])

            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_2
            pid_2 = get_pid
            print(pid_2)

            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as e:
            print('Error:', e)
    def check_modules_disable_func(self):
        try:
            self.check_modules_output.configure(self.master, text='.....Modules.....', font=('Helvetica bold',26), bg_color="black")

            self.check_modules_disable.destroy()
            self.check_modules_enable = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE CHECK MODULES', font=('Helvetica bold',10),command=self.check_modules_enable_func, corner_radius=0, fg_color='indigo')
            self.check_modules_enable.place(relx=0.185, rely=0.2, anchor='center')
            
            self.check_modules_indicator.configure(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)

            script_path = 'C:/Users/Chowfer/Desktop/CODE SPACE/Python Modules.py'
            command = (script_path)

            process = subprocess.Popen(['python', command]).kill()

            print('Disable CHECK MODULES')

            print(pid_2)
            os.kill(pid_2, 9)

            if os.kill.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {os.kill.returncode}')
        except Exception as e:
            print('Error:', e)
    def enable_keyboard_tester_function(self):
        try:
            self.keyboard_tester.destroy()
            self.disable_keyboard_tester = ctk.CTkButton(self.master, width=245, height=30, text='DISABLE TEST KEYBOARD', font=('Helvetica bold',10),command=self.disable_keyboard_tester_function, corner_radius=0, fg_color='red')
            self.disable_keyboard_tester.place(relx=0.185, rely=0.25, anchor='center')

            print('Running command...')

            process = subprocess.Popen(['python', script_path_keyboard])
            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_1
            pid_1 = get_pid
            print(pid_1)

            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as f:
            print('Error:', f)
    def disable_keyboard_tester_function(self):
        try:
    
            self.disable_keyboard_tester.destroy()
            self.keyboard_tester = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE TEST KEYBOARD', font=('Helvetica bold',10),command=self.enable_keyboard_tester_function, corner_radius=0, fg_color='indigo')
            self.keyboard_tester.place(relx=0.185, rely=0.25, anchor='center')
            
            command = (script_path_keyboard)
            print('Running command...')

            process = subprocess.Popen(['python', script_path_keyboard]).kill()
            print(pid_1)
            os.kill(pid_1, 9)

            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as f2:
            print('Error:', f2)

            
            
    def hbrd_function(self):
        try:
            script_path = 'C:/Users/Chowfer/Desktop/CODE SPACE/Hibernate Sample.bat'
            command = (script_path)
            print('Running command...')

            process = subprocess.Popen([command])
            process()
            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as g:
            print('Error:', g)
    def cpu_usage_function(self):
        try:
            get_cpu_usage = psutil.cpu_percent(4)
            print(psutil.virtual_memory())
            self.cpu_usage_output.configure(self.master, text=('CPU Usage: ', get_cpu_usage), font=('Helvetica bold',26), bg_color="black")
            print('The CPU usage is: ', get_cpu_usage)
        except Exception as h:
            print('Error:', h)

class NewClass:
    def Software_Exit(self):
        print('Software Exited')
            
    
if __name__ == '__main__':
    app = ctk.CTk()
    gui = Aplikasi(master = app)
    app.mainloop()

    time.sleep(2)
    initialize_class = NewClass()
    initialize_class.Software_Exit()

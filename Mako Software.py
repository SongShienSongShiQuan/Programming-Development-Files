from cProfile import label
from concurrent.futures import thread
from doctest import master
from email.mime import image
from gc import get_stats
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

print('Initializing...')
print('Function Debug Location Format: sec_a0000, sec_b0001, sec_f5106')

action = False
Set_Action_True = ']'
Set_Action_False = '['
win = ctk
root = ctk.CTk
anti_afk_running = True

#PATH Add path here to prevent scripts to start when added as variable
script_path_anti_afk = 'PyAutoGUI sample, script.py'
script_path_modules = 'Python Modules.py'
script_path_keyboard = 'Keypress_Detection_Python.py'
Exception_Duplication_Initializer = 'Exception Duplication Initializer.py'
protect_process_terminate_blender = 'protect_process_terminate_blender.py'
Get_log_files = "Get_log_files.py"
Add_log_files = "Add_log_files.py"
Sub_log_files = "Sub_log_files.py"
protect_all_process_RAM = "protect_all_process_RAM.py"
add_program_to_list = "add_program_to_list.py"
sub_program_to_list = "sub_program_to_list.py"
Release_RAM_Usage_path = "Release_RAM_Usage.py"
explorer_command = "explorer.bat"
cmd_command = "cmd.bat"
msedge_command = "msedge.bat"
visual_studio_code_path = "vsc.bat"
visual_studio_path = "vs.bat"
blender_exe_path = "blender.bat"

#PID IDs, set variable to global in functions ex: "global pid_1"
#PID is acquired because 'script_path_example' is added as a variable and it starts the process before being called.
#Ex: 'subprocess.Popen(command).terminate()' Instead of terminating it lets the process run.
pid_1 = 0
pid_2 = 0
pid_3 = 0
pid_4 = 0
pid_5 = 0
pid_6 = 0

class Aplikasi:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('700x700')
        self.master.resizable(False, False)
        self.master.wm_title('Mako Software')
        self.master.iconbitmap('Square T650i Logo.ico')
        #self.master.attributes('-alpha', 0.7)
        self.master.wm_attributes('-alpha', 0.8, '-transparentcolor', '#808080')
        img_path = '2023-03-17 01_48_32-.png'
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

        framebackground_ram_usage = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackground_ram_usage.place(relx=0.69, rely=0.4, anchor='center')

        framebackground_protect_process_terminate_blender_RAM = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        framebackground_protect_process_terminate_blender_RAM.place(relx=0.69, rely=0.45, anchor='center')

        frame_Mako_Software_Debugger = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        frame_Mako_Software_Debugger.place(relx=0.69, rely=0.50, anchor='center')
        
        frame_Get_log_files = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        frame_Get_log_files.place(relx=0.69, rely=0.55, anchor='center')

        frame_protect_all_process_RAM = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        frame_protect_all_process_RAM.place(relx=0.69, rely=0.60, anchor='center')
        
        frame_Release_RAM_Usage = ctk.CTkFrame(self.master, width=420, height=30, fg_color="black", corner_radius=100)
        frame_Release_RAM_Usage.place(relx=0.69, rely=0.65, anchor='center')

        softwarename = ctk.CTkLabel(self.master, text='Xin Chào  -  Open Source GITHUB  -  Mako_Software.py', font=('Helvetica bold',26), bg_color="grey")
        softwarename.place(relx=0.5, rely=0.035, anchor='center')

        self.counter: str = '0'

        #entry = tk.Entry(root)
        #entry.pack()

        self.outputtext1 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext1.place(relx=0.45, rely=0.1, anchor='center')

        self.outputprint = ctk.CTkLabel(self.master, text='Shortcut Disabled', font=('Helvetica bold',26), bg_color="black")
        self.outputprint.place(relx=0.7, rely=0.1, anchor='center')

        self.enableantiafk = ctk.CTkButton(self.master, width=245, height=30, text='Enable Anti AFK Keyboard Shortcut', font=('Helvetica bold',10),command=self.enable_anti_afk_keyboard_shortcut, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.enableantiafk.place(relx=0.185, rely=0.1, anchor='center')

        self.anti_afk_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.anti_afk_indicator.place(relx=0.375, rely=0.1, anchor='center')

        self.label = ctk.CTkLabel(self.master, text='Mouse Click Tests: 0', font=('Helvetica bold',26), bg_color="black")
        self.label.place(relx=0.7, rely=0.15, anchor='center')

        self.outputtext2 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext2.place(relx=0.45, rely=0.15, anchor='center')

        self.button = ctk.CTkButton(self.master, width=245, height=30, text='Click Counter', font=('Helvetica bold',10),command=self.increment, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.button.place(relx=0.185, rely=0.15, anchor='center')

        self.outputtext3 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext3.place(relx=0.45, rely=0.2, anchor='center')

        self.check_modules_output = ctk.CTkLabel(self.master, text='.....Modules.....', font=('Helvetica bold',26), bg_color="black")
        self.check_modules_output.place(relx=0.7, rely=0.2, anchor='center')

        self.check_modules_enable = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE CHECK MODULES', font=('Helvetica bold',10),command=self.check_modules_enable_func, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.check_modules_enable.place(relx=0.185, rely=0.2, anchor='center')

        self.check_modules_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.check_modules_indicator.place(relx=0.375, rely=0.2, anchor='center')
        
        self.outputtext4 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext4.place(relx=0.45, rely=0.25, anchor='center')

        self.KEY_Get_Input_output = ctk.CTkLabel(self.master, text='KEY_Get_Input: DISABLED', font=('Helvetica bold',26), bg_color="black")
        self.KEY_Get_Input_output.place(relx=0.7, rely=0.25, anchor='center')

        self.KEY_Get_Input_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.KEY_Get_Input_indicator.place(relx=0.375, rely=0.25, anchor='center')

        self.KEY_Get_Input = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE KEY_Get_Input', font=('Helvetica bold',10),command=self.enable_keyboard_tester_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.KEY_Get_Input.place(relx=0.185, rely=0.25, anchor='center')

        self.outputtext4 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext4.place(relx=0.45, rely=0.3, anchor='center')

        self.hbrd_ = ctk.CTkButton(self.master, width=245, height=30, text='Hybrid Shutdown', font=('Helvetica bold',10),command=self.hbrd_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.hbrd_.place(relx=0.185, rely=0.3, anchor='center')

        self.outputtext5 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext5.place(relx=0.45, rely=0.35, anchor='center')

        self.cpu_usage_output = ctk.CTkLabel(self.master, text='{CPU Usage: }', font=('Helvetica bold',26), bg_color="black")
        self.cpu_usage_output.place(relx=0.7, rely=0.35, anchor='center')
        
        self.cpu_usage = ctk.CTkButton(self.master, width=245, height=30, text='Get CPU Usage', font=('Helvetica bold',10),command=self.cpu_usage_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.cpu_usage.place(relx=0.185, rely=0.35, anchor='center')

        self.outputtext6 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext6.place(relx=0.45, rely=0.4, anchor='center')

        self.ram_usage = ctk.CTkButton(self.master, width=245, height=30, text='Get RAM Usage', font=('Helvetica bold',10),command=self.ram_usage_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.ram_usage.place(relx=0.185, rely=0.4, anchor='center')

        self.ram_usage_output = ctk.CTkLabel(self.master, text='{RAM Usage: }', font=('Helvetica bold',26), bg_color="black")
        self.ram_usage_output.place(relx=0.7, rely=0.4, anchor='center')

        self.outputtext6 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext6.place(relx=0.45, rely=0.45, anchor='center')

        self.protect_process_terminate_blender = ctk.CTkButton(self.master, width=245, height=30, text='Protect Process RAM: Blender', font=('Helvetica bold',10),command=self.protect_process_terminate_blender_RAM_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.protect_process_terminate_blender.place(relx=0.185, rely=0.45, anchor='center')
        
        self.protect_process_terminate_blender_output = ctk.CTkLabel(self.master, text='Function is disabled.', font=('Helvetica bold',26), bg_color="black")
        self.protect_process_terminate_blender_output.place(relx=0.7, rely=0.45, anchor='center')

        self.protect_process_terminate_blender_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.protect_process_terminate_blender_indicator.place(relx=0.375, rely=0.45, anchor='center')

        self.outputtext7 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext7.place(relx=0.45, rely=0.50, anchor='center')

        self.Mako_Software_Debugger = ctk.CTkButton(self.master, width=245, height=30, text='Mako_Software_Debugger', font=('Helvetica bold',10),command=self.Mako_Software_Debugger_Unimplimented_Logic_Duplicate_Logic_Checker_Function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.Mako_Software_Debugger.place(relx=0.185, rely=0.50, anchor='center')

        self.Mako_Software_Debugger_output = ctk.CTkLabel(self.master, text='Debugger Checker', font=('Helvetica bold',26), bg_color="black")
        self.Mako_Software_Debugger_output.place(relx=0.7, rely=0.50, anchor='center')

        self.outputtext8 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext8.place(relx=0.45, rely=0.55, anchor='center')

        self.Get_log_files = ctk.CTkButton(self.master, width=245, height=30, text='Get Log Files', font=('Helvetica bold',10),command=self.get_log_txt_files, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.Get_log_files.place(relx=0.185, rely=0.55, anchor='center')

        self.add_log_files = ctk.CTkButton(self.master, text='Add Log Files', font=('Helvetica bold',10), command=self.add_log_files_function, corner_radius=0,fg_color='red', hover_color='darkred', width=75, height=20)
        self.add_log_files.place(relx=0.92, rely=0.55, anchor='center')

        self.sub_log_files = ctk.CTkButton(self.master, text='Sub Log Files', font=('Helvetica bold',10), command=self.sub_log_files_function, corner_radius=0,fg_color='blue', hover_color='darkblue', width=75, height=20)
        self.sub_log_files.place(relx=0.80, rely=0.55, anchor='center')

        self.Get_log_files_output = ctk.CTkLabel(self.master, text='Get Log Files', font=('Helvetica bold',26), bg_color="black")
        self.Get_log_files_output.place(relx=0.62, rely=0.55, anchor='center')

        self.outputtext9 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext9.place(relx=0.45, rely=0.60, anchor='center')

        self.protect_all_process_RAM = ctk.CTkButton(self.master, width=245, height=30, text='Protect All Process RAM', font=('Helvetica bold',10),command=self.protect_all_process_RAM_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
        self.protect_all_process_RAM.place(relx=0.185, rely=0.60, anchor='center')

        self.protect_all_process_RAM_indicator = ctk.CTkFrame(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
        self.protect_all_process_RAM_indicator.place(relx=0.375, rely=0.60, anchor='center')

        self.add_program_to_list = ctk.CTkButton(self.master, text='Add Program', font=('Helvetica bold',10), command=self.add_program_to_list_function, corner_radius=0,fg_color='red', hover_color='darkred', width=75, height=20)
        self.add_program_to_list.place(relx=0.92, rely=0.60, anchor='center')

        self.sub_program_to_list = ctk.CTkButton(self.master, text='Remove Program', font=('Helvetica bold',10), command=self.sub_program_to_list_function, corner_radius=0,fg_color='blue', hover_color='darkblue', width=75, height=20)
        self.sub_program_to_list.place(relx=0.80, rely=0.60, anchor='center')

        self.protect_all_process_RAM_output = ctk.CTkLabel(self.master, text='Protect Processes', font=('Helvetica bold',20), bg_color="black")
        self.protect_all_process_RAM_output.place(relx=0.62, rely=0.60, anchor='center')

        self.outputtext10 = ctk.CTkLabel(self.master, text='OUTPUT', font=('Helvetica bold',10), bg_color="black", height=0.5)
        self.outputtext10.place(relx=0.45, rely=0.65, anchor='center')

        self.Release_RAM_Usage = ctk.CTkButton(self.master, width=245, height=30, text='Release RAM Usage', font=('Helvetica bold',10),command=self.Activate_Release_RAM_Usage_, corner_radius=0, fg_color='red', hover_color='darkred')
        self.Release_RAM_Usage.place(relx=0.185, rely=0.65, anchor='center')

        self.add_program_to_list = ctk.CTkButton(self.master, text='Add Program', font=('Helvetica bold',10), command=self.add_program_to_list_function, corner_radius=0,fg_color='red', hover_color='darkred', width=75, height=20)
        self.add_program_to_list.place(relx=0.92, rely=0.65, anchor='center')

        self.sub_program_to_list = ctk.CTkButton(self.master, text='Remove Program', font=('Helvetica bold',10), command=self.sub_program_to_list_function, corner_radius=0,fg_color='blue', hover_color='darkblue', width=75, height=20)
        self.sub_program_to_list.place(relx=0.80, rely=0.65, anchor='center')

        self.Release_RAM_Usage_output = ctk.CTkLabel(self.master, text='Release RAM', font=('Helvetica bold',20), bg_color="black")
        self.Release_RAM_Usage_output.place(relx=0.62, rely=0.65, anchor='center')

        #Windows Default Application Below

        frame_windows_application = ctk.CTkFrame(self.master, width=425, height=70, fg_color="black", corner_radius=0)
        frame_windows_application.place(relx=0.69, rely=0.943, anchor='center')

        self.Windows_Default_Application_output = ctk.CTkLabel(self.master, text='Add to \'Environment Variables\' the apps below.', font=('Helvetica bold',10), bg_color="black")
        self.Windows_Default_Application_output.place(relx=0.2, rely=0.88, anchor='center')

        explorer_icon_open = "file_explorer_icon.png"
        openedimage_explorer_icon = Image.open(explorer_icon_open)
        resize_image_explorer_icon = openedimage_explorer_icon.resize((50, 50))
        image_explorer_icon = ImageTk.PhotoImage(resize_image_explorer_icon)
        self.launch_explorer = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_explorer_func, corner_radius=0, fg_color='black', hover_color='indigo', image=image_explorer_icon)
        self.launch_explorer.place(relx=0.05, rely=0.95, anchor='center')

        self.kill_explorer = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_explorer_func, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_explorer.place(relx=0.08, rely=0.92, anchor='center')

        cmd_icon_open = "cmd.png"
        openedimage_cmd_icon = Image.open(cmd_icon_open)
        resize_image_cmd_icon = openedimage_cmd_icon.resize((62, 52))
        image_cmd_icon = ImageTk.PhotoImage(resize_image_cmd_icon)
        self.launch_cmd = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_cmd_func, corner_radius=0, fg_color='black', hover_color='indigo', image=image_cmd_icon)
        self.launch_cmd.place(relx=0.15, rely=0.95, anchor='center')

        self.kill_cmd = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_cmd_func, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_cmd.place(relx=0.19, rely=0.92, anchor='center')

        msedge_icon_open = "msedge.png"
        openedimage_msedge_icon = Image.open(msedge_icon_open)
        resize_image_msedge_icon = openedimage_msedge_icon.resize((50, 50))
        image_msedge_icon = ImageTk.PhotoImage(resize_image_msedge_icon)
        self.launch_msedge = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_msedge_func, corner_radius=0, fg_color='black', hover_color='indigo', image=image_msedge_icon)
        self.launch_msedge.place(relx=0.25, rely=0.95, anchor='center')

        self.kill_msedge = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_msedge_func, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_msedge.place(relx=0.28, rely=0.92, anchor='center')

        vsc_icon_open = "vsc_icon.png"
        openedimage_vsc_icon = Image.open(vsc_icon_open)
        resize_image_vsc_icon = openedimage_vsc_icon.resize((50, 50))
        image_vsc_icon = ImageTk.PhotoImage(resize_image_vsc_icon)
        self.launch_visual_studio_code = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_visual_studio_code_function, corner_radius=0, fg_color='black', hover_color='indigo', image=image_vsc_icon)
        self.launch_visual_studio_code.place(relx=0.34, rely=0.95, anchor='center')

        self.kill_visual_studio_code = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_visual_studio_code_function, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_visual_studio_code.place(relx=0.37, rely=0.92, anchor='center')

        vs_icon_open = "vs_icon.png"
        openedimage_vs_icon = Image.open(vs_icon_open)
        resize_image_vs_icon = openedimage_vs_icon.resize((50, 50))
        image_vs_icon = ImageTk.PhotoImage(resize_image_vs_icon)
        self.launch_visual_studio = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_visual_studio_function, corner_radius=0, fg_color='black', hover_color='indigo', image=image_vs_icon)
        self.launch_visual_studio.place(relx=0.44, rely=0.95, anchor='center')

        self.kill_visual_studio = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_visual_studio_function, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_visual_studio.place(relx=0.47, rely=0.92, anchor='center')

        blender_icon_open = "blender_icon.png"
        openedimage_blender_icon = Image.open(blender_icon_open)
        resize_image_blender_icon = openedimage_blender_icon.resize((55, 50))
        image_blender_icon = ImageTk.PhotoImage(resize_image_blender_icon)
        self.launch_blender = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.launch_blender_function, corner_radius=0, fg_color='black', hover_color='indigo', image=image_blender_icon)
        self.launch_blender.place(relx=0.53, rely=0.95, anchor='center')

        self.kill_blender = ctk.CTkButton(self.master, width=15, height=15, text='X', font=('Helvetica bold',8),command=self.kill_blender_function, corner_radius=0, fg_color='gray', hover_color='darkred')
        self.kill_blender.place(relx=0.56, rely=0.92, anchor='center')

        shutdown_icon_open = "shutdown_icon.png"
        openedimage_shutdown_icon = Image.open(shutdown_icon_open)
        resize_image_shutdown_icon = openedimage_shutdown_icon.resize((50, 50))
        image_shutdown_icon = ImageTk.PhotoImage(resize_image_shutdown_icon)
        self.initiate_hibernate = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.hibernate_function, corner_radius=0, fg_color='black', hover_color='indigo', image=image_shutdown_icon)
        self.initiate_hibernate.place(relx=0.95, rely=0.95, anchor='center')

        environment_variable_icon_open = "environment_variable_icon.png"
        openedimage_environment_variable_icon = Image.open(environment_variable_icon_open)
        resize_image_environment_variable_icon = openedimage_environment_variable_icon.resize((50, 50))
        image_environment_variable_icon = ImageTk.PhotoImage(resize_image_environment_variable_icon)
        self.initiate_hibernate = ctk.CTkButton(self.master, width=50, height=50, text='', font=('Helvetica bold',10),command=self.environment_variable_function, corner_radius=0, fg_color='black', hover_color='indigo', image=image_environment_variable_icon)
        self.initiate_hibernate.place(relx=0.62, rely=0.95, anchor='center')

    def increment(self):
        try:
            self.counter = str(int(self.counter) + 1)
            self.label.configure(text=('Mouse Click Tests: ' + (self.counter)))
            if self.counter == '1':
                print('Mako')
            
            if int(self.counter) == 1:
                self.reset_button = ctk.CTkButton(self.master, text='Reset', font=('Helvetica bold',10), command=self.reset, corner_radius=0,fg_color='red', hover_color='darkred', width=60, height=20)
                self.reset_button.place(relx=0.92, rely=0.15, anchor='center')
        except Exception as error_output:
            print('Error Increment Loc>sec_a0001:', error_output)
    def reset(self):
        try:
            self.counter = '0'
            self.label.configure(text=('Mouse Click Tests: ' + (self.counter)))
            self.reset_button.destroy()
        except Exception as error_output:
            print('Error Reset Loc>sec_a0002:', error_output)
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


            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
            
            
        except Exception as error_output:
            print('Error enable_anti_afk_keyboard_shortcut Loc>sec_a0003:', error_output)

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

        except Exception as error_output:
            print('Error disable_anti_afk_keyboard_shortcut Loc>sec_a0004:', error_output)
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

            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error check_modules_enable_func Loc>sec_a0005:', error_output)
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

            if os.kill.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {os.kill.returncode}')
        except Exception as error_output:
            print('Error check_modules_disable_func Loc>sec_a0006:', error_output)
    def enable_keyboard_tester_function(self):
        try:
            self.KEY_Get_Input.destroy()
            self.disable_KEY_Get_Input = ctk.CTkButton(self.master, width=245, height=30, text='DISABLE KEY_Get_Input', font=('Helvetica bold',10),command=self.disable_keyboard_tester_function, corner_radius=0, fg_color='red')
            self.disable_KEY_Get_Input.place(relx=0.185, rely=0.25, anchor='center')
            self.KEY_Get_Input_output.configure(self.master, text='KEY_Get_Input: ENABLED', font=('Helvetica bold',26), bg_color="black")
            self.KEY_Get_Input_indicator.configure(self.master, width=10, height=30, fg_color="darkgreen", corner_radius=0)

            print('Running command...')

            process = subprocess.Popen(['python', script_path_keyboard])
            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_1
            pid_1 = get_pid
            print(pid_1)

            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error enable_keyboard_tester_function Loc>sec_a0007:', error_output)
    def disable_keyboard_tester_function(self):
        try:
    
            self.disable_KEY_Get_Input.destroy()
            self.KEY_Get_Input = ctk.CTkButton(self.master, width=245, height=30, text='ENABLE KEY_Get_Input', font=('Helvetica bold',10),command=self.enable_keyboard_tester_function, corner_radius=0, fg_color='indigo')
            self.KEY_Get_Input.place(relx=0.185, rely=0.25, anchor='center')
            self.KEY_Get_Input_output.configure(self.master, text='KEY_Get_Input: DISABLED', font=('Helvetica bold',26), bg_color="black")
            self.KEY_Get_Input_indicator.configure(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
            
            print('Running command...')

            process = subprocess.Popen(['python', script_path_keyboard]).kill()
            print(pid_1)
            os.kill(pid_1, 9)

            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error disable_keyboard_tester_function Loc>sec_a0008:', error_output)

            
            
    def hbrd_function(self):
        try:
            script_path = 'C:/Users/Chowfer/Desktop/CODE SPACE/Hibernate Sample.bat'
            command = (script_path)
            print('Running command...')

            process = subprocess.Popen([command])
            process()
            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error hbrd_function Loc>sec_a0009:', error_output)
    def cpu_usage_function(self):
        try:
            get_cpu_usage = psutil.cpu_percent(4)
            print(psutil.virtual_memory())
            self.cpu_usage_output.configure(self.master, text=('CPU Usage: ', get_cpu_usage), font=('Helvetica bold',26), bg_color="black")
            print('The CPU usage is: ', get_cpu_usage)
        except Exception as error_output:
            print('Error cpu_usage_function Loc>sec_a0010:', error_output)
    def ram_usage_function(self):
        try:
            get_ram_usage = psutil.virtual_memory()
            get_ram_usage_percent = get_ram_usage.percent
            self.ram_usage_output.configure(self.master, text=('RAM Usage: ', get_ram_usage_percent), font=('Helvetica bold',26), bg_color="black")
            print('The RAM usage is: ', get_ram_usage_percent)

        except Exception as error_output:
            print('Error ram_usage_function Loc>sec_a0011:', error_output)
    def protect_process_terminate_blender_RAM_function(self):
        try:
            print('Running command...')
            self.protect_process_terminate_blender_indicator.configure(self.master, width=10, height=30, fg_color="darkgreen", corner_radius=0)
            self.protect_process_terminate_blender_output.configure(self.master, text='Function is enabled.', font=('Helvetica bold',26), bg_color="black")
            self.protect_process_terminate_blender.destroy()
            self.disable_protect_process_terminate_blender = ctk.CTkButton(self.master, width=245, height=30, text='Protect Process RAM: Blender', font=('Helvetica bold',10),command=self.disable_protect_process_terminate_blender_RAM_function, corner_radius=0, fg_color='red', hover_color='darkred')
            self.disable_protect_process_terminate_blender.place(relx=0.185, rely=0.45, anchor='center')

            process = subprocess.Popen(['python', protect_process_terminate_blender])
            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_4
            pid_4 = get_pid
            print(pid_4)

            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error protect_process_terminate_blender_RAM_function Loc>sec_a0012:\a', error_output)
    def disable_protect_process_terminate_blender_RAM_function(self):
        try:
            print('Running command...')
            self.protect_process_terminate_blender_indicator.configure(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
            self.protect_process_terminate_blender_output.configure(self.master, text='Function is disabled.', font=('Helvetica bold',26), bg_color="black")
            self.disable_protect_process_terminate_blender.destroy()
            self.protect_process_terminate_blender = ctk.CTkButton(self.master, width=245, height=30, text='Protect Process RAM: Blender', font=('Helvetica bold',10),command=self.protect_process_terminate_blender_RAM_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
            self.protect_process_terminate_blender.place(relx=0.185, rely=0.45, anchor='center')

            process = subprocess.Popen(['python', protect_process_terminate_blender]).kill()
            print(pid_4)
            os.kill(pid_4, 9)
            
            if process.returncode == None:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
        except Exception as error_output:
            print('Error protect_process_terminate_blender_RAM_function Loc>sec_a0013:\a', error_output)
    def Mako_Software_Debugger_Unimplimented_Logic_Duplicate_Logic_Checker_Function(self):
        try:
            command = (Exception_Duplication_Initializer)
            print('Debugger Enabled...')

            process = subprocess.Popen(['python.exe', command])
            process()
        except Exception as error_output:
            print('Error Mako_Software_Debugger_Unimplimented_Logic_Duplicate_Logic_Checker_Function Loc>sec_a0014:', error_output)
    def get_log_txt_files(self):
        try:
            process = subprocess.Popen(['python', Get_log_files])
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0015:', error_output)
    def add_log_files_function(self):
        try:
            process = subprocess.Popen(['python', Add_log_files])
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0016:', error_output)
    def sub_log_files_function(self):
        try:
            process = subprocess.Popen(['python', Sub_log_files])
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0017:', error_output)
    def protect_all_process_RAM_function(self):
        try:
            self.protect_all_process_RAM_indicator.configure(self.master, width=10, height=30, fg_color="darkgreen", corner_radius=0)
            self.protect_all_process_RAM.destroy()
            self.disable_protect_all_process_RAM = ctk.CTkButton(self.master, width=245, height=30, text='Protect All Process RAM', font=('Helvetica bold',10),command=self.disable_protect_all_process_RAM_function, corner_radius=0, fg_color='red', hover_color='darkred')
            self.disable_protect_all_process_RAM.place(relx=0.185, rely=0.60, anchor='center')
            process = subprocess.Popen(['python', protect_all_process_RAM])
            time.sleep(2)
            get_pid = process.pid
            print(get_pid)

            global pid_5
            pid_5 = get_pid
            print(pid_5)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0018:', error_output)
    def disable_protect_all_process_RAM_function(self):
        try:
            self.protect_all_process_RAM_indicator.configure(self.master, width=10, height=30, fg_color="darkred", corner_radius=0)
            self.disable_protect_all_process_RAM.destroy()
            self.protect_all_process_RAM = ctk.CTkButton(self.master, width=245, height=30, text='Protect All Process RAM', font=('Helvetica bold',10),command=self.protect_all_process_RAM_function, corner_radius=0, fg_color='indigo', hover_color='darkred')
            self.protect_all_process_RAM.place(relx=0.185, rely=0.60, anchor='center')

            process = subprocess.Popen(['python', protect_process_terminate_blender]).kill()
            print(pid_5)
            os.kill(pid_5, 9)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0019:', error_output)
    def add_program_to_list_function(self):
        try:
            process = subprocess.Popen(['python', add_program_to_list])
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0020:', error_output)
    def sub_program_to_list_function(self):
        try:
            process = subprocess.Popen(['python', sub_program_to_list])
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0021:', error_output)
    def Activate_Release_RAM_Usage_(self):
        try:
            self.Release_RAM_Usage.destroy()
            self.Init_Release_RAM_Usage = ctk.CTkButton(self.master, width=245, height=30, text='Release RAM Usage', font=('Helvetica bold',10),command=self.Init_Release_RAM_Usage_, corner_radius=0, fg_color='indigo', hover_color='darkred')
            self.Init_Release_RAM_Usage.place(relx=0.185, rely=0.65, anchor='center')
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0022:', error_output)
    def Init_Release_RAM_Usage_(self):
        try:
            self.Init_Release_RAM_Usage.destroy()
            self.Release_RAM_Usage = ctk.CTkButton(self.master, width=245, height=30, text='Release RAM Usage', font=('Helvetica bold',10),command=self.Activate_Release_RAM_Usage_, corner_radius=0, fg_color='red', hover_color='darkred')
            self.Release_RAM_Usage.place(relx=0.185, rely=0.65, anchor='center')
            process = subprocess.Popen(['python', Release_RAM_Usage_path])
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0023:', error_output)
    def Custom_Crosshair_Overlay(self):
        try:
            raise NotImplementedError('Function returns nothing.')
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0024:', error_output)
    def initiate_developer_workspace_python_csharp_lua(self):
        try:
            raise NotImplementedError('Function returns nothing.')
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0025:', error_output)
    def launch_explorer_func(self):
        try:
            process = subprocess.run(explorer_command)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0026:', error_output)
    def kill_explorer_func(self):
        try:
            end_process = 'taskkill /im explorer.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0027:', error_output)
    def launch_cmd_func(self):
        try:
            process = subprocess.run(cmd_command)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0028:', error_output)
    def kill_cmd_func(self):
        try:
            end_process = 'taskkill /im cmd.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0029:', error_output)
    def launch_msedge_func(self):
        try:
            process = subprocess.run(msedge_command)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0030:', error_output)
    def kill_msedge_func(self):
        try:
            end_process = 'taskkill /im msedge.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error get_log_txt_files Loc>sec_a0031:', error_output)
    def launch_visual_studio_code_function(self):
        try:
            process = subprocess.run(visual_studio_code_path)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0032:', error_output)
    def kill_visual_studio_code_function(self):
        try:
            end_process = 'taskkill /im Code.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0033:', error_output)
    def launch_visual_studio_function(self):
        try:
            process = subprocess.run(visual_studio_path)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0034:', error_output)
    def kill_visual_studio_function(self):
        try:
            end_process = 'taskkill /im devenv.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0035:', error_output)
    def launch_blender_function(self):
        try:
            process = subprocess.run(blender_exe_path)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0036:', error_output)
    def kill_blender_function(self):
        try:
            end_process = 'taskkill /im blender.exe /F'
            process = subprocess.Popen(end_process)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0037:', error_output)
    def hibernate_function(self):
        try:
            process_hibernate = 'shutdown /h'
            process = subprocess.Popen(process_hibernate)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0038:', error_output)
    def environment_variable_function(self):
        try:
            environment_variable_path = "sysdm.cpl.bat"
            process = subprocess.run(environment_variable_path)
        except Exception as error_output:
            print('Error protect_process_CPU_function Loc>sec_a0039:', error_output)
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

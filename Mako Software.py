from doctest import master
from pdb import run
from runpy import run_module
from string import whitespace
import tkinter
from turtle import back
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

action = False
Set_Action_True = ']'
Set_Action_False = '['
win = ctk
root = ctk.CTk

class App:
    def __init__(self, master: ctk.CTk):
        self.master = master
        self.master.geometry('700x700')
        self.master.resizable(False, False)
        self.master.wm_title('Mako Software')
        self.master.iconbitmap('C:/Users/Chowfer/Desktop/T6/Main Files/Random Pics/Square T650i Logo.ico')
        #self.master.attributes('-alpha', 0.7)
        self.master.wm_attributes('-alpha', 0.8, '-transparentcolor', 'grey')
        img_path = 'C:/Users/Chowfer/Desktop/T6/Main Files/Random Pics/2023-03-17 01_48_32-.png'
        openedimage = Image.open(img_path)
        blurred_image = openedimage.filter(ImageFilter.BLUR)
        self.image = ImageTk.PhotoImage(blurred_image)
        background = ctk.CTkCanvas(self.master, width=self.master.winfo_width(), height=self.master.winfo_height())
        background.create_image(0, 0, anchor=ctk.NW, image=self.image)
        background.pack(fill=ctk.BOTH, expand=True)
        background.create_text = ctk.CTkLabel(self.master, text='Mako', font=('Helvetica bold',26), bg_color="grey")
        background.create_text.place(relx=0.5, rely=0.3, anchor='center')
        frame = ctk.CTkFrame(self.master, width=100, height=100, fg_color="green")
        frame.place(relx=0.5, rely=0.3, anchor='center')
        self.counter: str = '0'
        
        self.label = ctk.CTkLabel(self.master, text='Mouse Click Tests: 0', font=('Helvetica bold',26), bg_color="grey")
        self.label.place(relx=0.5, rely=0.5, anchor='center')
        
        self.outputprint = ctk.CTkLabel(self.master, text='Shortcut Disabled', font=('Helvetica bold',26), bg_color="grey")
        self.outputprint.place(relx=0.5, rely=0.1, anchor='center')

        self.button = ctk.CTkButton(self.master, text='Click Counter',command=self.increment, corner_radius=20, fg_color='indigo')
        self.button.place(relx=0.5, rely=0.6, anchor='center')

        self.enableantiafk = ctk.CTkButton(self.master, text='Enable Anti AFK Keyboard Shortcut',command=self.enable_anti_afk_keyboard_shortcut, corner_radius=20, fg_color='indigo')
        self.enableantiafk.place(relx=0.5, rely=0.2, anchor='center')
    
    def increment(self):
        try:
            self.counter = str(int(self.counter) + 1)
            self.label.configure(text=('Mouse Click Tests: ' + (self.counter)))
            
            if self.counter == '1':
                print('Mako')
            
            
            
            if int(self.counter) == 1:
                self.reset_button = ctk.CTkButton(self.master, text='Reset', command=self.reset, corner_radius=20,fg_color='red', hover_color='darkred')
                self.reset_button.place(relx=0.5, rely=0.68, anchor='center')
        except Exception as e:
            print('Error:', e)
    def reset(self):
        try:
            self.counter = '0'
            self.label.configure(text=self.counter)
            self.reset_button.destroy()
        except Exception as m:
            print('Error:', m)

    def enable_anti_afk_keyboard_shortcut(self):
        try:
            self.outputprint.configure(text='Shortcut Enabled')
            script_path = 'PyAutoGUI sample, script.py'
            self.enableantiafk.configure(self.master, text='Enable Anti AFK Keyboard Shortcut',command=self.enable_anti_afk_keyboard_shortcut, corner_radius=20, fg_color='red')
            self.enableantiafk.destroy()
            self.disableantiafk = ctk.CTkButton(self.master, text='Disable Anti AFK Keyboard Shortcut',command=self.disable_anti_afk_keyboard_shortcut, corner_radius=20, fg_color='red')
            self.disableantiafk.place(relx=0.5, rely=0.2, anchor='center')
            
            command = (script_path) #Variable set to script.
            print('Enabled Shortcut')



            process = subprocess.Popen(['python', command])

            process()

            if process.returncode == 0:
                print('Script executed successfully')
            else:
                print(f'Script execution failed with return code {process.returncode}')
            
            
        except Exception as c:
            print('Error:', c)

    def disable_anti_afk_keyboard_shortcut(self):
        try:
            self.outputprint.configure(text='Shortcut Disabled')
            script_path = 'PyAutoGUI sample, script.py'
            command = (script_path) #Variable set to script.
            print('Disabled Shortcut')
            self.disableantiafk.destroy()
            self.enableantiafk = ctk.CTkButton(self.master, text='Enable Anti AFK Keyboard Shortcut',command=self.enable_anti_afk_keyboard_shortcut, corner_radius=20, fg_color='indigo')
            self.enableantiafk.place(relx=0.5, rely=0.2, anchor='center')



            process = subprocess.Popen(['python', command])

            process.terminate()
        except Exception as d:
            print('Error:', d)
            
    
if __name__ == '__main__':
    app = ctk.CTk()
    gui = App(master = app)
    app.mainloop()
import tkinter as tk
import time
import sys
import cmd
import os
import subprocess
from PIL import Image, ImageTk, ImageFilter
import threading
import psutil

class Aplikasi:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.geometry('200x200')
        self.master.eval('tk::PlaceWindow . center')

if __name__ == '__main__':
    app = tk.Tk()
    gui = Aplikasi(master = app)
    app.mainloop()
import Mako_Software
import time
import customtkinter as ctk

def Mako_Software_Exit():
    Mako_Software_App_init1 = Mako_Software.NewClass()
    Mako_Software_App_init1.Software_Exit()

if __name__ == '__main__':
    app = ctk.CTk()
    gui = Mako_Software.Aplikasi(master = app)
    app.mainloop()
    Mako_Software_Exit()
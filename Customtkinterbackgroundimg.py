from cgitb import text
import customtkinter as ctk
from PIL import ImageTk, Image


root = ctk.CTk()
root.title("Background Image")


img_path = 'C:/Users/Chowfer/Desktop/T6/Main Files/Random Pics/Square T650i Logo.png'
mainimage = ImageTk.PhotoImage(Image.open(img_path))
root.geometry('576x576')
#root.attributes('-alpha', 0.7)
root.wm_attributes('-alpha', 0.8, '-transparentcolor', 'grey')

background = ctk.CTkCanvas(root, width=root.winfo_width(), height=root.winfo_height())


background.create_image(0, 0, anchor='nw', image=mainimage)
background.create_text = ctk.CTkLabel(root, text='Mako', font=('Helvetica bold',26), text_color='black', bg_color="white")
background.create_text.place(relx=0.5, rely=0.4, anchor='center')


background.pack(fill=ctk.BOTH, expand=True)


root.mainloop()
import tkinter as tk
 
root = tk.Tk()
width = 200 # Width 
height = 200 # Height
 
screen_width = root.winfo_screenwidth()  # Width of the screen
screen_height = root.winfo_screenheight() # Height of the screen
 
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
 
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.mainloop()
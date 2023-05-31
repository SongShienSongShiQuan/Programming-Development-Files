import tkinter as tk
 
root = tk.Tk()
 
label = tk.Label(root, text = "A Window")
label.place(x = 70, y = 80)
 
root.eval('tk::PlaceWindow . center')
root.mainloop()
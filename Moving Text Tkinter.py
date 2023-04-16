import tkinter as tk

class MovingText:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=200, height=100)
        self.canvas.pack()
        self.text = self.canvas.create_text(100, 50, text="Moving Text", fill="blue", font=("Helvetica", 16))
        self.move_text()

    def move_text(self):
        self.canvas.move(self.text, 5, 0)
        self.master.after(50, self.move_text)

root = tk.Tk()
app = MovingText(root)
root.mainloop()
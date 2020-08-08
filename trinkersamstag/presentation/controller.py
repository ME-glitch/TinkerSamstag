import tkinter as tk
from trinkersamstag.presentation import model
from trinkersamstag.presentation.view import View


class Controller:

    def __init__(self):
        self.root = tk.Tk()
        self.model = model.Model()
        self.view = View(self.root)
        self.run()

    def run(self):
        self.root.title("Chess board v0.0.1")
        self.root.deiconify()
        self.root.mainloop()
        pass

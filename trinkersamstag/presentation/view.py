import tkinter as tk
from tkinter import *


class View:

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.top_menu()

    def top_menu(self):
        self.top_menu_frame = tk.Frame(self.master)
        self.top_menu_frame.pack(side=TOP, fill=tk.BOTH, expand=1)
        self.testButton = tk.Button(self.top_menu_frame, text="Hello World")
        self.testButton.pack(side="top", fill=tk.BOTH)

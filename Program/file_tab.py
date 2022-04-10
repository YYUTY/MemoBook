import tkinter as tk
import tkinter.ttk as ttk

class File_tab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both',expand=1)

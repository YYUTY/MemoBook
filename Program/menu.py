import tkinter as tk
from Program import variable as va
from Program import file_tab as ft

class Menu():
    def __init__(self,master):
        self.menubar=master
        self.file()
        self.edit()
        va.root.config(menu=self.menubar)
    def file(self):
        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label='Add_file',command=va.nt.add_tab)
        self.filemenu.add_command(label='Open',command=va.nt.fileopen)
        self.filemenu.add_command(label='Save',command=va.nt.filesave)
        self.filemenu.add_command(label='Exit',command=va.nt.exit)
        self.menubar.add_cascade(label='File',menu=self.filemenu)
    def edit(self):
        self.editmenu=tk.Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Edit',menu=self.editmenu)

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
        self.filemenu.add_command(label=va.lang['Menu']['File']['New File'],command=va.nt.add_tab,accelerator='Ctrl+N')
        self.filemenu.add_command(label=va.lang['Menu']['File']['Open File'],command=va.nt.fileopen)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=va.lang['Menu']['File']['Setting'],command=va.nt.setting)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=va.lang['Menu']['File']['Save'],command=va.nt.filesave)
        self.filemenu.add_command(label=va.lang['Menu']['File']['Save As'],command=va.nt.filesaveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label=va.lang['Menu']['File']['Exit'],command=va.nt.exit)
        self.menubar.add_cascade(label=va.lang['Menu']['File']['File'],menu=self.filemenu)
    def edit(self):
        self.editmenu=tk.Menu(self.menubar,tearoff=0)
        self.editmenu.add_command(label=va.lang['Menu']['Edit']['Undo'])
        self.menubar.add_cascade(label=va.lang['Menu']['Edit']['Edit'],menu=self.editmenu)

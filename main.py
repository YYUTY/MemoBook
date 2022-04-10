import os
import json
import tkinter as tk
from Program import menu
import tkinter.ttk as ttk
from Program import variable as va
from Program import file_tab as ft

def json_read():
    with open('./Setting/Setting.json','r', encoding="utf-8") as f:
        va.setting=json.load(f)
    with open('./Setting/Language/'+str(va.setting["Language"])+'.json','r', encoding="utf-8") as f:
        va.lang=json.load(f)

def main():
    va.root=tk.Tk()
    va.root.title('MemoBook')
    va.root.geometry('640x480')
    style = ttk.Style(va.root)
    style.configure('CustomNotebook.tab', expand=(20,100,20,0))
    va.nt=ft.File_tab(va.root)
    m=menu.Menu(tk.Menu(va.root))
    va.root.mainloop()

if __name__ == '__main__':
    json_read()
    main()

import os
import json
import tkinter as tk
from Program import menu
import tkinter.ttk as ttk
from Program import variable as va
from Program import file_tab as ft

def init():
    with open('./Setting/Setting.json','r', encoding="utf-8") as f:
        va.setting=json.load(f)
    with open('./Setting/Language/'+str(va.setting["Language"])+'.json','r', encoding="utf-8") as f:
        va.lang=json.load(f)
    with open('./Setting/Texture/Skin/'+str(va.setting["Skin"])+'.json','r',encoding="utf-8") as f:
        va.skin=json.load(f)

def main():
    va.root=tk.Tk()
    va.path=os.getcwd()
    va.root.title('MemoBook')
    va.root.state('zoomed')
    va.root.geometry('1920x1080')
    va.nt=ft.File_tab(va.root)
    va.nt.start()
    m=menu.Menu(tk.Menu(va.root))
    va.root.mainloop()

if __name__ == '__main__':
    init()
    main()

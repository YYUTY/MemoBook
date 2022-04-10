import tkinter as tk
import tkinter.ttk as ttk
from Program import variable as va
from Program import file_tab as ft
from Program import menu

def main():
    va.root = tk.Tk()
    va.root.title('MemoBook')
    va.root.geometry('640x480')
    ft.File_tab(va.root)
    va.root.mainloop()

if __name__ == "__main__":
    main()

from tkinter import filedialog
def fileopen():
    fname = filedialog.askopenfilename()
    add_tab(fname)

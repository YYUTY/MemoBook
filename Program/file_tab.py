import os
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import threading as th

def thread(func):#デコレータ
    def wrapper(*args, **kwargs):
        x=th.Thread(target=func(*args, **kwargs))
        x.start()
    return wrapper

class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized=False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized=True

        kwargs["style"]="CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active=None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element=self.identify(event.x, event.y)

        if "close" in element:
            index=self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active=index
            return "break"

    def on_close_release(self, event):
        """Called when the button is released"""
        if not self.instate(['pressed']):
            return

        element= self.identify(event.x, event.y)
        if "close" not in element:
            # user moved the mouse off of the close button
            return

        index=self.index("@%d,%d" % (event.x, event.y))

        if self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active=None

    def __initialize_custom_style(self):
        style=ttk.Style()
        self.images=(
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe",
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])


class SbTextFrame(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        text=tk.Text(self,wrap='none',undo=True)
        x_sb=tk.Scrollbar(self,orient='horizontal')
        y_sb=tk.Scrollbar(self,orient='vertical')
        x_sb.config(command=text.xview)
        y_sb.config(command=text.yview)
        text.config(xscrollcommand=x_sb.set,yscrollcommand=y_sb.set)
        text.grid(column=0,row=0,sticky='nsew')
        x_sb.grid(column=0,row=1,sticky='ew')
        y_sb.grid(column=1,row=0,sticky='ns')
        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)
        self.text=text
        self.x_sb=x_sb
        self.y_sb=y_sb

class File_tab(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.notebook=CustomNotebook()
        self.notebook.pack(fill='both',expand=1)
        self.tframes=[]
        self.fnames=[]
    @thread
    def fileopen(self):
        fname=filedialog.askopenfilename()
        self.add_tab(fname)
    @thread
    def add_tab(self, fname='untitled'):
        tframe=SbTextFrame(self.notebook)
        self.tframes.append(tframe)
        if os.path.isfile(fname):
            f=open(fname,'r')
            lines=f.readlines()
            f.close()
            for line in lines:
                tframe.text.insert('end',line)
        self.fnames.append(fname)
        title=os.path.basename(fname)
        self.notebook.add(tframe,text=title)
        self.notebook.select(self.notebook.tabs()[self.notebook.index('end')-1])
    def filesave(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=self.fnames[idx]
        tframe=self.tframes[idx]
        if not os.path.isfile(fname):
            self.filesaveas()
        else:
            with open(fname,'w') as f:
                f.writelines(tframe.text.get('1.0','end-1c'))
    def filesaveas(self):
        idx=self.notebook.tabs().index(self.notebook.select())
        fname=filedialog.asksaveasfilename()
        tframe=self.tframes[idx]
        with open(fname,'w') as f:
            f.writelines(tframe.text.get('1.0','end-1c'))
    def exit(self):
        sys.exit()

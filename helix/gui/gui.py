#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  gui.py
#  
# Python 3.4.4
#
#
# GUI for SpyTools
# 
# IMPORTS
import tkinter as tk
from .mainmenu import MainMenu
from .whoismenu import WhoisMenu
from .encryptmenu import EncryptMenu
from .rsamenu import RsaMenu

# STATIC VARIABLES
LARGE_FONT = ("Verdana", 16)


# MODULE
class HelixApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainMenu, WhoisMenu, EncryptMenu, RsaMenu):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


    
if __name__ == '__main__':
    app = HelixApp()
    app.mainloop()




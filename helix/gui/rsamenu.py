#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rsamenu.py
#  
# Python 3.4.4
#
#
# Helix main menu page
# 

# IMPORTS
import sys
import tkinter as tk
from time import strftime
from PIL import Image, ImageTk
from ..infotools import InfoTools

# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("fixedsys", 14)
SMALL_FONT = ("Times", 10, 'bold')
PASSWORD_LENGTH = (range(8,21))


# MODULE

class RsaMenu(tk.Frame):
    """
    DNS Name Menu, contains functions to provide domain name and registrar information.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        data = InfoTools()
        """
        Date display

        """
        # date banner
        self.dateDisplay = tk.IntVar()
        self.dateDisplay.set(data.get_date())

        self.timeDisplay = tk.IntVar()
        self.timeDisplay.set(0)

        """
        Date/Time frame

        """
        self.titleFrame = tk.Frame(self, relief='solid', bg='navy')
        self.titleFrame.pack(side='top')

        self.dateLabel = tk.Label(self.titleFrame, font=SMALL_FONT, fg='white', bg='black',
                                  textvariable=self.dateDisplay)
        self.dateLabel.grid(row=0, column=1, sticky='ew', ipadx=1, ipady=1)

        self.timeLabel = tk.Label(self.titleFrame, font=SMALL_FONT, fg='white', bg='black',
                                  textvariable=self.timeDisplay)
        self.timeLabel.grid(row=0, column=0, sticky='ew', ipadx=1, ipady=1)

        """
        Title label

        """
        self.dnsTitleLabel = tk.Label(self, bd=5, font=MEDIUM_FONT, fg='white', bg='gray12', text='Generate RSA Key-Pair')
        self.dnsTitleLabel.pack(side='top', fill='x', ipady=2)

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='QUIT',
                                           command=lambda: sys.exit())
        self.programExitButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        self.backButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='BACK',
                                           command=lambda: controller.show_frame('MainMenu'))
        self.backButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        self.rsaImage = ImageTk.PhotoImage(Image.open('data/gui/rsabackground.png').resize((176,176)))
        rsaImage = tk.Label(self, image=self.rsaImage, bg='black').pack(side='top', pady=10)
        rsaImage = self.rsaImage



        self.digital_clock()


    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
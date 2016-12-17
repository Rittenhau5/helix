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
from tkinter import filedialog
from tkinter import messagebox
from time import strftime
from PIL import Image, ImageTk
from ..infotools import InfoTools
from ..rsakeytools import RsaKeyTools

# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("Times", 12, 'bold')
SMALL_FONT = ("Times", 10, 'bold')
PASSWORD_LENGTH = (range(8,21))


# MODULE

class RsaMenu(tk.Frame):
    """
    DNS Name Menu, contains functions to provide domain name and registrar information.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        """
        GUI Variables

        """
        self.rsakeyName = tk.StringVar()
        self.rsakeyName.set("")

        self.rsakeyExportDirectory = tk.StringVar()
        self.rsakeyExportDirectory.set("")

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
        self.RsaTitleLabelImg = ImageTk.PhotoImage(Image.open('data/gui/button4.png').resize((275, 65)))
        RsaTitleLabel = tk.Label(self, image=self.RsaTitleLabelImg, fg='white', bg='gray12',).pack(side='top', fill='x', ipady=2)
        RsaTitleLabel = self.RsaTitleLabelImg

        self.instructionLabel = tk.Label(self, bd=5, font=SMALL_FONT, fg='white', bg='black',
                                         text="Enter name for key and click generate.")
        self.instructionLabel.pack(side='top', fill='x', ipady=2)

        self.rsakeyNameEntry = tk.Entry(self, bd=5, font=MEDIUM_FONT, fg='green', bg='white',
                                        textvariable=self.rsakeyName)
        self.rsakeyNameEntry.pack(side='top', ipady=2)

        self.rsakeyGenerateButton = tk.Button(self, font=MEDIUM_FONT, bg='white', fg='black', text='GENERATE KEY',
                                              command=lambda: self.on_rsakey_generate_button())
        self.rsakeyGenerateButton.pack(side='top', ipady=2, pady=10)

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='QUIT',
                                           command=lambda: sys.exit())
        self.programExitButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        self.backButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='BACK',
                                           command=lambda: controller.show_frame('MainMenu'))
        self.backButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        self.rsaImage = ImageTk.PhotoImage(Image.open('data/gui/rsabackground.png').resize((146, 146)))
        rsaImage = tk.Label(self, image=self.rsaImage, bg='black').pack(side='top')
        rsaImage = self.rsaImage

        self.rsakeyNameEntry.focus_set()
        self.digital_clock()

    """
    Event Handlers

    """
    def on_rsakey_generate_button(self):
        """
        Initializes RSA Tools class and generates key to chosen directory.
        :return:

        """
        export_directory = filedialog.askdirectory(initialdir ="/", title="Select Export Directory")
        self.rsakeyExportDirectory.set(export_directory)

        rsa_key_name = self.rsakeyName.get()

        rsakey_tools = RsaKeyTools()
        if_successful = rsakey_tools.generate_key_pair(rsa_key_name, export_directory)
        if export_directory:
            if if_successful:
                self.successMessageBox = messagebox.showinfo("Helix", ("Success! Key %s exported." % rsa_key_name))
            else:
                self.failureMessageBox = messagebox.showerror("Helix", "Failure.")
        else:
            messagebox.showerror("Error", "Failure! Enter name for key pair.")

    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
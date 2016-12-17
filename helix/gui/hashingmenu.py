#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hashingmenu.py
#  
# Python 3.4.4
#
#
# Helix hash menu page
# 

# IMPORTS
import sys
import tkinter as tk
from tkinter import filedialog
from time import strftime
from PIL import Image, ImageTk
from ..infotools import InfoTools
from ..hash_generator import file_hash_generator, string_hash_generator

# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("Times", 12, 'bold')
SMALL_FONT = ("Times", 10, 'bold')
PASSWORD_LENGTH = (range(8,21))


# MODULE

class HashingMenu(tk.Frame):
    """
    DNS Name Menu, contains functions to provide domain name and registrar information.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        """
        GUI Variables.

        """
        self.stringToHash = tk.StringVar()
        self.stringToHash.set("")

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
        self.hashingTitleLabelImg = ImageTk.PhotoImage(Image.open('data/gui/button5.png').resize((275, 65)))
        HashTitleLabel = tk.Label(self, image=self.hashingTitleLabelImg, fg='white', bg='gray12',).pack(side='top', fill='x', ipady=2)
        HashTitleLabel = self.hashingTitleLabelImg

        self.instructionLabel = tk.Label(self, bd=5, font=SMALL_FONT, fg='white', bg='black',
                                         text="Enter phrase or choose file:")
        self.instructionLabel.pack(side='top', fill='x', ipady=2)

        """
        Center frame

        """
        self.hashingFrame = tk.Frame(self, relief='solid', bg='black')
        self.hashingFrame.pack(side='top', fill='x')

        self.hashStringEntry = tk.Entry(self.hashingFrame, bd=2, fg='green', bg='white',
                                                   textvariable=self.stringToHash)
        self.hashStringEntry.pack(side='top', ipady=2, pady=5)

        self.hashStringButton = tk.Button(self.hashingFrame, font=MEDIUM_FONT, bg='RoyalBlue4', fg='white',
                                          text='HASH STRING', command=lambda: self.on_hash_string_button_click())
        self.hashStringButton.pack(side='top', ipady=2, ipadx=10)

        self.hashFileButton = tk.Button(self.hashingFrame, font=MEDIUM_FONT, bg='RoyalBlue4', fg='white',
                                        text='HASH FILE', command=lambda: self.on_hash_file_button_click())
        self.hashFileButton.pack(side='top', ipady=2, ipadx=23)

        self.hashText = tk.Text(self.hashingFrame, height=1, bd=2, font=MEDIUM_FONT, fg='green', bg='black', width=30)
        self.hashText.pack(side='top', ipadx=10, pady=5)
        self.hashText.insert('1.0', "Your hash will appear here.")

        self.hashImage = ImageTk.PhotoImage(Image.open('data/gui/hashingbackground.png').resize((146, 146)))
        hashImage = tk.Label(self, image=self.hashImage, bg='black').pack(side='top')
        hashImage = self.hashImage

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='QUIT',
                                           command=lambda: sys.exit())
        self.programExitButton.pack(side='bottom', ipadx=5, ipady=5, pady=3, fill='x')

        self.backButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='BACK',
                                           command=lambda: controller.show_frame('MainMenu'))
        self.backButton.pack(side='bottom', ipadx=5, ipady=5, pady=3, fill='x')

        self.hashStringEntry.focus_set()
        self.digital_clock()

    """
    Event Handlers

    """
    def on_hash_string_button_click(self):
        """
        Event handler to hash a string.
        :return:

        """
        string_to_hash = self.stringToHash.get()
        hashed_string = string_hash_generator(string_to_hash)
        self.hashText.delete('1.0', 'end')
        self.hashText.insert('1.0', hashed_string)

    def on_hash_file_button_click(self):
        """
        Event handler to hash a file.
        :return:

        """
        file_to_hash = filedialog.askopenfilename(initialdir="/", title="Select File",
                                                  filetypes=(("Exe files", "*.exe"),("All files", "*.*")))
        if file_to_hash:
            hashed_file_contents = file_hash_generator(file_to_hash)
            self.hashText.delete('1.0', 'end')
            self.hashText.insert('1.0', hashed_file_contents)
        else:
            pass


    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
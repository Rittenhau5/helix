#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  encryptmenu.py
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
from ..cryptotools import CryptoTools
from ..password_generator import password_generator

# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("Times", 12, 'bold')
SMALL_FONT = ("Times", 10, 'bold')
PASSWORD_LENGTH = (range(8,21))


# MODULE

class EncryptMenu(tk.Frame):
    """
    DNS Name Menu, contains functions to provide domain name and registrar information.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        self.encryptImage = ImageTk.PhotoImage(Image.open('data/gui/encryptbackground.png').resize((176, 176)))
        encryptImage = tk.Label(self, image=self.encryptImage, bg='black').place(x=0, y=40, relwidth=1, relheight=1)
        encryptImage = self.encryptImage

        """
        GUI Variables

        """
        self.encryptWidgetStatus = tk.BooleanVar()
        self.encryptWidgetStatus.set(False)

        self.decryptWidgetStatus = tk.BooleanVar()
        self.decryptWidgetStatus.set(False)

        self.fileToEncrypt = tk.StringVar()
        self.fileToEncrypt.set("")

        self.encryptionPassword = tk.StringVar()
        self.encryptionPassword.set("")

        self.fileToDecrypt = tk.StringVar()
        self.fileToDecrypt.set("")

        self.newFileName = tk.StringVar()
        self.newFileName.set("")

        self.decryptionPassword = tk.StringVar()
        self.decryptionPassword.set("")

        self.destinationDirectory = tk.StringVar()
        self.destinationDirectory.set("")

        self.decryptionKeyFile = tk.StringVar()
        self.decryptionKeyFile.set("")

        """
        Date display

        """
        data = InfoTools()

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
        self.cryptoTitleLabelImg = ImageTk.PhotoImage(Image.open('data/gui/button3.png').resize((275,65)))
        cryptoTitleLabel = tk.Label(self, image=self.cryptoTitleLabelImg, fg='white', bg='gray12',).pack(side='top', fill='x', ipady=2)
        cryptoTitleLabel = self.cryptoTitleLabelImg

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='QUIT',
                                           command=lambda: sys.exit())
        self.programExitButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        self.backButton = tk.Button(self, font=SMALL_FONT, bg='white', fg='black', text='BACK',
                                           command=lambda: controller.show_frame('MainMenu'))
        self.backButton.pack(side='bottom', ipadx=5, ipady=5, pady=5, fill='x')

        """
        Primary Button Frames

        """
        self.encryptFrame = tk.Frame(self, relief='solid', bg='black')
        self.encryptFrame.pack(side='top', fill='x')

        self.encryptButton = tk.Button(self.encryptFrame, font=MEDIUM_FONT, bg='white', fg='black', text='ENCRYPT FILE',
                                       command=lambda: self.on_encrypt_button_click())
        self.encryptButton.pack(side='top', ipadx=5, ipady=5, pady=5, fill='x')

        self.encryptWidgetFrame = tk.Frame(self.encryptFrame, relief='solid', bg='black')
        self.encryptWidgetFrame.pack(side='top', fill='x')

        self.decryptFrame = tk.Frame(self, relief='solid', bg='black')
        self.decryptFrame.pack(side='top', fill='x')

        self.decryptButton = tk.Button(self.encryptFrame, font=MEDIUM_FONT, bg='white', fg='black', text='DECRYPT FILE',
                                       command=lambda: self.on_decrypt_button_click())
        self.decryptButton.pack(side='top', ipadx=5, ipady=5, pady=5, fill='x')

        self.decryptWidgetFrame = tk.Frame(self.decryptFrame, relief='solid', bg='black')
        self.decryptWidgetFrame.pack(side='top', fill='x')



        self.digital_clock()

    """
    Event Handlers.

    """
    def on_encrypt_button_click(self):
        """
        Opens the encryption widget menu.
        :return:

        """
        status = self.encryptWidgetStatus.get()
        self.encryptWidgetFileButton = tk.Button(self.encryptWidgetFrame, font=MEDIUM_FONT, bg='white', fg='black',
                                                 text='SELECT FILE', command=lambda: self.on_select_file_button_click())

        self.encryptWidgetPasswordButton = tk.Button(self.encryptWidgetFrame, bd=2, font=MEDIUM_FONT, fg='black',
                                                     bg='white', text="PASSWORD",
                                                     command=lambda: self.on_encrypt_password_button_click())

        self.encryptWidgetFilenameEntry = tk.Entry(self.encryptWidgetFrame, bd=2, fg='green', bg='black',
                                                   textvariable=self.fileToEncrypt)
        self.encryptWidgetPasswordEntry = tk.Entry(self.encryptWidgetFrame, bd=2, fg='green', bg='black',
                                                   textvariable=self.encryptionPassword)

        self.encryptWidgetEncryptFileButton = tk.Button(self.encryptWidgetFrame, bd=2, font=MEDIUM_FONT,
                                                        fg='black', bg='white', text="ENCRYPT",
                                                        command=lambda: self.on_encrypt_file_button_click())

        if status == False:
            self.encryptWidgetFileButton.grid(row=0, column=0, sticky='w', ipadx=10)
            self.encryptWidgetPasswordButton.grid(row=1, column=0, sticky='nsew', ipadx=10)
            self.encryptWidgetFilenameEntry.grid(row=0, column=1, sticky='w', ipadx=10)
            self.encryptWidgetPasswordEntry.grid(row=1, column=1, sticky='w', ipadx=10)
            self.encryptWidgetEncryptFileButton.grid(row=2, column=0, columnspan=2, sticky='ns',pady=2)
            self.encryptWidgetStatus.set(True)
        else:
            pass

    def on_select_file_button_click(self):
        """
        Opens a dialog to choose a file and sets that file to variable.
        :return:

        """
        filename = filedialog.askopenfilename(initialdir ="/", title="Select File", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        self.fileToEncrypt.set(filename)

    def on_encrypt_password_button_click(self):
        """
        Generates random password and populates password entry field.
        :return:

        """
        encryption_password = password_generator(12, 'NO')
        self.encryptionPassword.set(encryption_password)

        # add password to clipboard
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(encryption_password)
        clip.destroy()

    def on_encrypt_file_button_click(self):
        """
        Sends filename and password to file encryption module.
        :return:

        """
        export_directory = filedialog.askdirectory(initialdir ="/", title="Select Export Directory")
        self.destinationDirectory.set(export_directory)

        filename = self.fileToEncrypt.get()
        password = self.encryptionPassword.get()

        encryptor = CryptoTools()
        encryptor.encrypt(password, filename, export_directory)
        self.successMessageBox = messagebox.showinfo("Helix", "Success! File encrypted.")



    def on_decrypt_button_click(self):
        """
        Opens the decryption widget menu>
        :return:

        """
        status = self.decryptWidgetStatus.get()
        self.decryptWidgetFilenameButton = tk.Button(self.decryptWidgetFrame, font=MEDIUM_FONT, bg='white', fg='black', text='SELECT FILE', command=lambda: self.on_select_decrypt_file_button_click())

        self.decryptWidgetNewFilenameButton = tk.Button(self.decryptWidgetFrame, bd=2, font=MEDIUM_FONT, fg='black', bg='white', text="NEW FILENAME", command=lambda: self.on_select_new_filename_button_click())

        self.decryptWidgetFilenameEntry = tk.Entry(self.decryptWidgetFrame, bd=2, fg='green', bg='black', textvariable=self.fileToDecrypt)
        self.decryptWidgetNewFilenameEntry = tk.Entry(self.decryptWidgetFrame, bd=2, fg='green', bg='black', textvariable=self.newFileName)
        self.decryptKeyFileButton = tk.Button(self.decryptWidgetFrame, font=MEDIUM_FONT, fg='black', bg='white', text="KEY FILE", command=lambda: self.on_decrypt_key_file_button_click())

        self.decryptWidgetDecryptPasswordEntry = tk.Entry(self.decryptWidgetFrame, bd=2, fg='green', bg='black', textvariable=self.decryptionKeyFile)

        self.decryptWidgetDecryptButton = tk.Button(self.decryptWidgetFrame, bd=2, font=MEDIUM_FONT, fg='black', bg='white', text="DECRYPT", command=lambda: self.on_decrypt_file_button_click())

        if status == False:
            self.decryptWidgetFilenameButton.grid(row=0, column=0, sticky='ew', ipadx=10)
            self.decryptWidgetNewFilenameButton.grid(row=1, column=0, sticky='ew', ipadx=10)
            self.decryptWidgetFilenameEntry.grid(row=0, column=1, ipadx=10, sticky='ew')
            self.decryptWidgetNewFilenameEntry.grid(row=1, column=1, ipadx=10, sticky='ew')
            self.decryptKeyFileButton.grid(row=2, column=0, sticky='ew', ipadx=8, ipady=1)
            self.decryptWidgetDecryptPasswordEntry.grid(row=2, column=1, sticky='ew', ipadx=10, ipady=1)
            self.decryptWidgetDecryptButton.grid(row=3, column=0, columnspan=2, sticky='ns', pady=2)
            self.decryptWidgetStatus.set(True)
        else:
            pass

    def on_select_decrypt_file_button_click(self):
        """
        Opens a dialog to choose a file to decrypt.
        :return:

        """
        filename = filedialog.askopenfilename(initialdir ="/", title="Select File", filetypes=(("Encrypted files", "*.encrypted"), ("all files", "*.*")))
        self.fileToDecrypt.set(filename)
        new_file_name = filename[:-10]
        self.newFileName.set(new_file_name)

    def on_select_new_filename_button_click(self):
        """
        Opens a dialog to choose a new filename for decrypted file.
        :return:

        """
        new_filename = filedialog.asksaveasfilename(initialdir ="/", title="Save as...", filetypes=(("Text files", "*.text"), ("all files", "*.*")))
        self.newFileName.set(new_filename)

    def on_decrypt_key_file_button_click(self):
        """
        Opens a dialog to choose key file name.
        :return:

        """
        key_file_name = filedialog.askopenfilename(initialdir="/", title="Select Key File", filetypes=(("Key files", "*.key"), ("all files", "*.*")))
        self.decryptionKeyFile.set(key_file_name)
        while True:
            try:
                with open(key_file_name) as f:
                    password = f.read()
                    self.decryptionPassword.set(password)
                    break
            except FileNotFoundError:
                print("Error file not found!")
                break

    def on_decrypt_file_button_click(self):
        """
        Decrypts selected file with input password.
        :return:

        """
        filename = self.fileToDecrypt.get()
        new_filename = self.newFileName.get()
        password = self.decryptionPassword.get()

        decryptor = CryptoTools()
        decryptor.decrypt(password, filename, new_filename)
        self.successMessageBox = messagebox.showinfo("Helix", "Success! File decrypted.")


    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
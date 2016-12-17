#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mainmenu.py
#  
# Python 3.4.4
#
#
# SpyTools main menu page
# 

# IMPORTS
import sys
import tkinter as tk
from time import strftime
from PIL import Image, ImageTk
from ..infotools import InfoTools
from ..password_generator import password_generator
from .._version import __version__



# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("fixedsys", 14)
SMALL_FONT = ("Times", 10, 'bold')
TITLE_FONT = ('Verana', 11, 'bold')
PASSWORD_LENGTH = (range(8,21))
PASSWORD_OPTION = ('YES', 'NO')


# MODULE

class MainMenu(tk.Frame):
    """
    Main menu, contains statistical information and buttons to other functions/menus.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        """
        GUI Variables

        """
        data = InfoTools()

        # version information
        self.versionInfo = tk.StringVar()
        self.versionInfo.set("Helix version" + __version__ + "\nrrittenhau5 2016")

        # time banner
        self.timeDisplay = tk.IntVar()
        self.timeDisplay.set(0)

        # date banner
        self.dateDisplay = tk.IntVar()
        self.dateDisplay.set(data.get_date())

        # hostname
        self.systemName = tk.StringVar()
        self.systemName.set("Hostname: " + data.get_hostname())

        # processor
        self.processorType = tk.StringVar()
        self.processorType.set("Processor: " + data.get_processor_type())

        # os
        self.operatingSystem = tk.StringVar()
        self.operatingSystem.set("OS: " + data.get_operating_system())

        # os version
        self.operatingSystemVersion = tk.StringVar()
        self.operatingSystemVersion.set("Version: " + data.get_os_version())

        # private ip
        self.lanIPAddress = tk.IntVar()
        self.lanIPAddress.set("LAN IP: " + data.get_private_ip())

        # public ip
        self.wanIPAddress = tk.IntVar()
        self.wanIPAddress.set("WAN IP: " + data.get_public_ip())

        # python version
        self.pythonVersion = tk.StringVar()
        self.pythonVersion.set("Python %s" % data.get_python_version())

        # location
        self.cityLocation = tk.StringVar()
        self.cityLocation.set("Location: %s, %s" % (data.get_city_location(), data.get_state_location()))

        # password length
        self.passwordLength = tk.IntVar()
        self.passwordLength.set(8)

        # user password
        self.password = tk.StringVar()
        self.password.set("Your password will be shown here...")

        self.passwordOption = tk.StringVar()
        self.passwordOption.set(PASSWORD_OPTION[0])

        """
        Header/Title frame

        """
        self.headerFrame = tk.Frame(self, relief='solid', bg='navy')
        self.headerFrame.pack(side='top')

        self.dateLabel = tk.Label(self.headerFrame, font=SMALL_FONT, fg='white', bg='black',
                                  textvariable=self.dateDisplay)
        self.dateLabel.grid(row=0, column=1, sticky='ew', ipadx=1, ipady=1)

        self.timeLabel = tk.Label(self.headerFrame, font=SMALL_FONT, fg='white', bg='black',
                                  textvariable=self.timeDisplay)
        self.timeLabel.grid(row=0, column=0, sticky='ew', ipadx=1, ipady=1)

        self.mainTitleImg = ImageTk.PhotoImage(Image.open('data/gui/helixlogo.png').resize((275, 100)))
        mainTitleImg = tk.Label(self, image=self.mainTitleImg, bg='black').pack(side='top')
        mainTitleImg = self.mainTitleImg

        """
        Button Frame and corresponding buttons.

        """
        self.buttonFrame = tk.Frame(self, relief='sunken', width=500, height=176, bg='black')
        self.buttonFrame.pack(side='top', fill='x')

        self.buttonBackgroundImg = ImageTk.PhotoImage(Image.open('data/gui/background.png').resize((256,256)))
        buttonBackgroundLabel = tk.Label(self.buttonFrame, image=self.buttonBackgroundImg, bg='black').place(x=0, y=0,
                                                                                                             relwidth=1,
                                                                                                             relheight=1)
        buttonBackgroundLabel = self.buttonBackgroundImg

        self.button1Img = ImageTk.PhotoImage(Image.open('data/gui/button1.png').resize((275,65)))
        self.pwdGeneratorButton = tk.Button(self.buttonFrame, image=self.button1Img, font=MEDIUM_FONT, bg='black',
                                            fg='black', relief='groove', command=lambda: self.on_password_button_click())

        self.pwdGeneratorButton.pack(side='top', fill='both')

        self.button2Img = ImageTk.PhotoImage(Image.open('data/gui/button2.png').resize((275, 65)))
        self.ipaddresslookupButton = tk.Button(self.buttonFrame, image=self.button2Img, font=MEDIUM_FONT, bg='black',
                                               fg='black', relief='groove', command=lambda: controller.show_frame('WhoisMenu'))

        self.ipaddresslookupButton.pack(side='top', fill='x')

        self.button3Img = ImageTk.PhotoImage(Image.open('data/gui/button3.png').resize((275, 65)))
        self.fileencryptButton = tk.Button(self.buttonFrame, image=self.button3Img, font=MEDIUM_FONT, bg='black',
                                           fg='black', relief='groove', command=lambda: controller.show_frame("EncryptMenu"))

        self.fileencryptButton.pack(side='top', fill='x')

        self.button4Img = ImageTk.PhotoImage(Image.open('data/gui/button4.png').resize((275, 65)))
        self.rsakeyButton = tk.Button(self.buttonFrame, image=self.button4Img, font=MEDIUM_FONT, bg='black',
                                      fg='black', relief='groove',command=lambda: controller.show_frame("RsaMenu"))

        self.rsakeyButton.pack(side='top', fill='x')

        self.button5Img = ImageTk.PhotoImage(Image.open('data/gui/button5.png').resize((275, 65)))
        self.md5HashButton = tk.Button(self.buttonFrame, image=self.button5Img, font=MEDIUM_FONT, bg='black',
                                       fg='black', relief='groove', command=lambda: controller.show_frame("HashingMenu"))

        self.md5HashButton.pack(side='top', fill='x')

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='QUIT',
                                           command=lambda: sys.exit())

        self.programExitButton.pack(side='bottom', ipadx=5, ipady=6, pady=4, fill='x')

        self.systeminfoButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white',
                                          relief='groove', text='SYSTEM INFORMATION',
                                          command=lambda: self.on_systeminfo_button_click())
        self.systeminfoButton.pack(side='bottom', fill='x', ipady=6)

        self.digital_clock()

    """
    Event Handlers

    """
    def on_password_button_click(self):
        """
        Opens pop up window to generate password.
        :param self:
        :return:

        """
        # password generator label
        self.passwordMenu = tk.Toplevel(bg='black')
        self.passwordMenu.title("Password Generator")

        self.passwordTitleImage = ImageTk.PhotoImage(Image.open('data/gui/button1.png').resize((275,65)))
        passwordImage = tk.Label(self.passwordMenu, image=self.passwordTitleImage, bg='black').pack(side='top')
        passwordImage = self.passwordTitleImage

        # primary frame
        self.passwordFrame = tk.Frame(self.passwordMenu, relief='solid', bg='RoyalBlue4')
        self.passwordFrame.pack(side='top', fill='x')

        # choose password length label
        self.passwordLengthLabel = tk.Label(self.passwordFrame, bd=2, font=MEDIUM_FONT, fg='white', bg='RoyalBlue4',
                                            text=' - Password length')
        self.passwordLengthLabel.grid(row=0, column=1, sticky='nsew')

        self.passwordLengthMenu = tk.OptionMenu(self.passwordFrame, self.passwordLength, *PASSWORD_LENGTH)
        self.passwordLengthMenu.grid(row=0, column=0, sticky='nsew')

        self.passwordOptionLabel = tk.Label(self.passwordFrame, bd=2, font=MEDIUM_FONT, fg='white', bg='RoyalBlue4',
                                            text=' - Special characters')
        self.passwordOptionLabel.grid(row=1, column=1, sticky='nsew')

        self.passwordOptionMenu = tk.OptionMenu(self.passwordFrame, self.passwordOption, *PASSWORD_OPTION)
        self.passwordOptionMenu.grid(row=1, column=0, sticky='nsew')

        self.generateButton = tk.Button(self.passwordMenu, font=MEDIUM_FONT, bg='RoyalBlue4', fg='white',
                                        text='Generate Password', command=lambda: self.on_generate_button_click())
        self.generateButton.pack(side='top', ipadx=10, ipady=5, pady=20)

        self.userPasswordText = tk.Text(self.passwordMenu, height=1, bd=2, font=MEDIUM_FONT, fg='green', bg='black',
                                        width=30)
        self.userPasswordText.pack(side='top', ipadx=10, ipady=10)
        self.userPasswordText.insert('1.0', "Your password will appear here\nand copy to clipboard.")

        self.passwordExitButton = tk.Button(self.passwordMenu, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='OK',
                                            command=lambda: self.passwordMenu.destroy())
        self.passwordExitButton.pack(side='bottom', ipadx=10, fill='x')

    def on_generate_button_click(self):
        """
        Event handler to return random password generated by system.
        :return:

        """
        passwordLength = self.passwordLength.get()
        newPassword = password_generator(passwordLength, self.passwordOption.get())
        self.userPasswordText.delete('1.0', 'end')
        self.userPasswordText.insert('1.0', newPassword)

        # add password to clipboard
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(newPassword)
        clip.destroy()

    def on_systeminfo_button_click(self):
        """
        Event handler to show system information on pop-up.
        :return:

        """
        self.systemInformationTop = tk.Toplevel(bg='black')
        self.systemInformationTop.title("Sysinfo")

        """
        System information frame

        """
        # system information frame
        self.sysinfoFrame = tk.Frame(self.systemInformationTop, relief='solid', bg='black')
        self.sysinfoFrame.pack(side='top', fill='x')

        # hostname
        self.hostnameLabel = tk.Label(self.sysinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                      textvariable=self.systemName)
        self.hostnameLabel.grid(row=0, column=0, sticky='e', padx=10)

        # processor
        self.processorLabel = tk.Label(self.sysinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                       textvariable=self.processorType)
        self.processorLabel.grid(row=0, column=1, sticky='e', padx=10)

        # os
        self.osLabel = tk.Label(self.sysinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                textvariable=self.operatingSystem)
        self.osLabel.grid(row=1, column=0, sticky='e', padx=10)

        # os version
        self.osVersionLabel = tk.Label(self.sysinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                       textvariable=self.operatingSystemVersion)
        self.osVersionLabel.grid(row=1, column=1, sticky='e', padx=10)

        # ok destroy window button
        self.sysinfoDestroyButton = tk.Button(self.systemInformationTop, font=SMALL_FONT, bg='RoyalBlue4', fg='white',
                                           relief='groove', text='OK', command=lambda: self.systemInformationTop.destroy())
        self.sysinfoDestroyButton.pack(side='bottom', fill='x', ipady=3)

        """
        Network information frame.

        """
        # network information frame
        self.networkinfoFrame = tk.Frame(self.systemInformationTop, relief='solid', bg='black')
        self.networkinfoFrame.pack(side='top')

        # lan ip address
        self.privateIPAddress = tk.Label(self.networkinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                         textvariable=self.lanIPAddress)
        self.privateIPAddress.grid(row=0, column=0, sticky='nsew', ipadx=10)

        # wan ip address
        self.publicIPAddress = tk.Label(self.networkinfoFrame, bd=2, font=SMALL_FONT, fg='white', bg='black',
                                        textvariable=self.wanIPAddress)
        self.publicIPAddress.grid(row=0, column=1, sticky='nsew', ipadx=10)

        # location label
        self.locationLabel = tk.Label(self.networkinfoFrame, bd=2, font=MEDIUM_FONT, fg='white', bg='black',
                                      textvariable=self.cityLocation)
        self.locationLabel.grid(row=1, column=0, columnspan=2, sticky='ew', ipadx=1, ipady=1)

    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
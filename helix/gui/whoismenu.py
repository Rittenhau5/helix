#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  whoismenu.py
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
from ..whoistools import WhoisTools

# STATIC VARIABLES
LARGE_FONT = ("fixedsys", 32, 'bold')
MEDIUM_FONT = ("Times", 12, 'bold')
SMALL_FONT = ("Times", 10, 'bold')
PASSWORD_LENGTH = (range(8,21))


# MODULE

class WhoisMenu(tk.Frame):
    """
    DNS Name Menu, contains functions to provide domain name and registrar information.

    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='black')

        """
        GUI Variables

        """
        data = InfoTools()

        self.statusText = tk.StringVar()
        self.statusText.set("Enter IP or domain name below")

        self.entryText = tk.StringVar()
        self.entryText.set("")

        self.domainName = tk.StringVar()
        self.domainName.set("www.domain.com")

        self.whoisServer = tk.StringVar()
        self.whoisServer.set("")

        self.nameServer = tk.StringVar()
        self.nameServer.set("")

        self.registrar = tk.StringVar()
        self.registrar.set("")

        self.organization = tk.StringVar()
        self.organization.set("")

        self.registeredName = tk.StringVar()
        self.registeredName.set("")

        self.address = tk.StringVar()
        self.address.set("")

        self.city = tk.StringVar()
        self.city.set("")

        self.zip = tk.StringVar()
        self.zip.set("")

        self.state = tk.StringVar()
        self.state.set("")

        self.country = tk.StringVar()
        self.country.set("")

        """
        Date display

        """
        # date banner
        self.dateDisplay = tk.IntVar()
        self.dateDisplay.set(data.get_date())

        self.timeDisplay = tk.IntVar()
        self.timeDisplay.set(0)

        """
        Title frame

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
        self.dnsTitleLabelImg = ImageTk.PhotoImage(Image.open('data/gui/button2.png').resize((275,65)))
        dnsTitleLabel = tk.Label(self, image=self.dnsTitleLabelImg, fg='white', bg='gray12',).pack(side='top', fill='x', ipady=2)
        dnsTitleLabel = self.dnsTitleLabelImg

        self.instructionLabel = tk.Label(self, bd=5, font=SMALL_FONT, fg='white', bg='black',
                                         textvariable=self.statusText)

        self.instructionLabel.pack(side='top', fill='x', ipady=2)

        """
        Entry for ip addresses and dns names.

        """
        self.dnsMenuEntry = tk.Entry(self, bd=5, font=MEDIUM_FONT, fg='green', bg='white', textvariable=self.entryText)
        self.dnsMenuEntry.pack(side='top', ipady=2)

        self.ipNameLookupButton = tk.Button(self, font=MEDIUM_FONT, bg='RoyalBlue4', fg='white', text='LOOKUP',
                                            command=lambda: self.on_lookup_button_click())

        self.ipNameLookupButton.pack(side='top', ipady=1, pady=15)

        """
        DNS Lookup information frame.

        """
        self.dnsInfoFrame = tk.Frame(self, relief='solid', bg='black')
        #self.dnsInfoFrame.pack(side='top')

        self.domainNameLabel = tk.Label(self.dnsInfoFrame, font=MEDIUM_FONT, fg='white', bg='gray12',
                                        textvariable=self.domainName)

        self.domainNameLabel.pack(side='top', ipady=5, pady=5, fill='x')

        self.whoisServerDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray30', textvariable=self.whoisServer)
        self.whoisServerDisplay.pack(side='top', fill='x')

        self.nameServerDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray25', textvariable=self.nameServer)
        self.nameServerDisplay.pack(side='top', fill='x')

        self.registrarDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray30', textvariable=self.registrar)
        self.registrarDisplay.pack(side='top', fill='x')

        self.organizationDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray25', textvariable=self.organization)
        self.organizationDisplay.pack(side='top', fill='x')

        self.nameDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray30', textvariable=self.registeredName)
        self.nameDisplay.pack(side='top', fill='x')

        self.addressDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray25', textvariable=self.address)
        self.addressDisplay.pack(side='top', fill='x')

        self.cityDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray30', textvariable=self.city)
        self.cityDisplay.pack(side='top', fill='x')

        self.zipDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray25', textvariable=self.zip)
        self.zipDisplay.pack(side='top', fill='x')

        self.stateDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray30', textvariable=self.state)
        self.stateDisplay.pack(side='top', fill='x')

        self.countryDisplay = tk.Label(self.dnsInfoFrame, bd=5, font=SMALL_FONT, fg='white', bg='gray25', textvariable=self.country)
        self.countryDisplay.pack(side='top', fill='x')

        self.programExitButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='QUIT',
                                           command=lambda: sys.exit())
        self.programExitButton.pack(side='bottom', ipadx=5, ipady=5, pady=3, fill='x')

        self.backButton = tk.Button(self, font=SMALL_FONT, bg='RoyalBlue4', fg='white', text='BACK',
                                           command=lambda: controller.show_frame('MainMenu'))
        self.backButton.pack(side='bottom', ipadx=5, ipady=5, pady=3, fill='x')

        self.dnsMenuEntry.focus_set()
        self.digital_clock()

    """
    Event Handlers.

    """
    def on_lookup_button_click(self):
        """
        Handles input validation and events related to domain lookups.
        :return:

        """
        self.dns = WhoisTools()
        userEntry = self.entryText.get()
        hasNumber = self.dns.check_if_ip(userEntry)

        if userEntry != None:
            if hasNumber:
                userEntry = self.dns.ip_name_lookup(userEntry)
                self.statusText.set(userEntry)
                while True:
                    try:
                        self.dnsData = self.dns.get_dns_information(userEntry)
                        self.update_gui_dns(self.dnsData)
                        break
                    except TypeError:
                        self.statusText.set("Error: Enter valid host")
                        break

            else:
                self.statusText.set(userEntry)
                while True:
                    try:
                        self.dnsData = self.dns.get_dns_information(userEntry)
                        self.update_gui_dns(self.dnsData)
                        break
                    except TypeError:
                        self.statusText.set("Error: Enter IP or Domain")
                        break
        else:
            self.statusText.set("Error!!")

    def update_gui_dns(self, dnsData):
        """
        Module that updates DNS information for GUI.
        :return:

        """
        self.dnsInfoFrame.pack(side='top')
        self.statusText.set(dnsData["domain_name"])
        self.domainName.set(dnsData["domain_name"])
        self.whoisServer.set("Whois: " + dnsData["whois_server"])
        self.nameServer.set("NameServer: " + dnsData["name_servers"][0])
        self.registrar.set("Registrar: " + dnsData["registrar"])
        self.organization.set("Org: " + dnsData["org"])
        self.registeredName.set("Name: " + dnsData["name"])
        self.address.set("Address: " + dnsData["address"])
        self.city.set("City: " + dnsData["city"])
        self.zip.set("Zip: " + dnsData["zipcode"])
        self.state.set("State: " + dnsData["state"])
        self.country.set("Country: " + dnsData["country"])

    """
    Misc. Functionality

    """
    def digital_clock(self):
        current_time = strftime("%H:%M:%S")
        self.timeDisplay.set(current_time)
        self.after(200, self.digital_clock)

if __name__ == '__main__':
    pass
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cryptotools.py
#  
# Python 3.4.4
#
#
# Collection of command line network and information gathering tools.
# 
# IMPORTS
from simplecrypt import encrypt, decrypt

# STATIC VARIABLES

# MODULE
class CryptoTools(object):
    """
    Collection of cryptography tools.

    """
    def __init__(self):
        pass

    def encrypt(self, password, filename, export_directory):
        """
        Encrypts data from provided filename using provided password.
        :param password:
        :param filename:
        :return:

        """
        filename_list = filename.split("/")
        new_filename = filename_list[-1]
        output_filename = export_directory + "/" + new_filename + ".encrypted"
        key_filename = export_directory + "/" + new_filename + ".key"
        print(output_filename, key_filename)

        with open(filename, 'r') as file_contents:
            file_text = file_contents.read()
            encrypted_text = encrypt(password, file_text.encode('utf8'))
        with open(output_filename, 'wb') as output:
            output.write(encrypted_text)
        with open(key_filename, 'w') as key_output:
            key_output.write(password)

        print("Encrypt success")

    def decrypt(self, password, input_filename, output_filename):
        """
        Decrypts data from provided file name with provided password, then writes to provided filename.
        :param password:
        :param input_filename:
        :param output_filename:
        :return:

        """
        with open(input_filename, 'rb') as file_contents:
            encrypted_text = file_contents.read()
            decrypted_text = decrypt(password, encrypted_text)
            decrypted_text = "%s" % decrypted_text.decode('utf8')
        with open(output_filename, 'w') as output:
            output.write(decrypted_text)
        print("Decrypt success")




if __name__ == '__main__':
    from tkinter import Tk
    from tkinter import filedialog

    filename = filedialog.askopenfilename()
    password = 'ron'

    encryptor = CryptoTools()
    encrypted_data = encryptor.encrypt(password, filename)
    print(encrypted_data)

    #file = filedialog.askopenfile()
    #savelocation = filedialog.asksaveasfilename()
    #directory = filedialog.askdirectory()
    #print(directory)


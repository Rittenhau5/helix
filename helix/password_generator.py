#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  password_generator.py
#  
# Python 3.4.4
#
#
# Password Generator. Returns password of uppercase, lowercase, numbers and symbols, to desired length.
# 
# IMPORTS
import string
import random

# STATIC VARIABLES
LOWERLETTERS = list(string.ascii_lowercase)
UPPERLETTERS = list(string.ascii_uppercase)
SYMBOLS = list(string.punctuation)
NUMBER = list(range(0, 10))

# MODULE

def password_generator(pwd_length, pwd_option):
    """
    Password Generator script.
    :param pwdLength:
    :return:

    """
    numbers = []
    for n in NUMBER:
        numbers.append(str(n))

    if pwd_option == 'YES':
        characters = LOWERLETTERS + UPPERLETTERS + SYMBOLS + numbers
    else:
        characters = LOWERLETTERS + UPPERLETTERS + numbers

    userPassword = ''.join((random.choice(characters)) for n in range(pwd_length))
    return userPassword


if __name__ == '__main__':
    password = password_generator(12)
    print(password)



#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  generate_test.py
#  
# Python 3.4.4
#
#
# simple string generator
# 
# IMPORTS

import string
import random

# STATIC VARIABLES
LOWERLETTERS = list(string.ascii_lowercase)
UPPERLETTERS = list(string.ascii_uppercase)
SYMBOLS = list(string.punctuation)
NUMBER = list(range(0,10))


# MODULE
pwdLength = 20
numbers = []
for n in NUMBER:
    numbers.append(str(n))

characters = LOWERLETTERS + UPPERLETTERS + SYMBOLS + numbers



def text_generator_test():
    print(numbers)
    print(LOWERLETTERS)
    print(UPPERLETTERS)
    print(SYMBOLS)
    print(characters)

    return ''.join((random.choice(characters)) for n in range(pwdLength))







    
if __name__ == '__main__':
    password = text_generator_test()
    print(password)




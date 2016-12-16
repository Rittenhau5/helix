#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hash_generator.py
#  
# Python 3.4.4
#
#
# Password Generator. Returns password of uppercase, lowercase, numbers and symbols, to desired length.
# 
# IMPORTS
import hashlib

# STATIC VARIABLES

# MODULE

def string_hash_generator(input_string):
    """
    Generates and returns md5 hash from provided string.
    :param input_string
    :return:

    """
    input_string = input_string.encode("utf-8")
    hash_string = hashlib.md5(input_string).hexdigest()

    return hash_string

def file_hash_generator(input_filename):
    """
    Generates and returns md5 hash from provided filename.
    :param input_filename:
    :return:

    """
    with open(input_filename, 'r') as file:
        input_string = file.read(input_filename).encode("utf-8")
        hash_string = string_hash_generator(input_string)
        return hash_string



if __name__ == '__main__':
    string = "Hello my nae is Ron"
    hashed_string = string_hash_generator(string)
    print(hashed_string)



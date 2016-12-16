#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rsakeytools.py
#  
# Python 3.4.4
#
#
# Collection of command line network and information gathering tools.
# 
# IMPORTS
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

# STATIC VARIABLES

# MODULE
class RsaKeyTools(object):
    """
    Tools to generate RSA Key pair.

    """
    def __init__(self):
        pass

    def generate_key_pair(self, name, export_directory):
        """
        Generates RSA key pair and exports to chosen directory.
        :return:

        """
        private_key_filename = export_directory + "/" + name + ".txt"
        public_key_filename = export_directory + "/" + name + "_pub.txt"

        # generate public/private key pair
        key = rsa.generate_private_key(backend=default_backend(), public_exponent=65537, key_size=2048)

        # convert public key to openssh format
        public_key = key.public_key().public_bytes(serialization.Encoding.OpenSSH, serialization.PublicFormat.OpenSSH)

        # convert private key to PEM container format
        pem = key.private_bytes(encoding=serialization.Encoding.PEM,
                                format=serialization.PrivateFormat.TraditionalOpenSSL,
                                encryption_algorithm=serialization.NoEncryption())

        private_key_string = pem.decode('utf-8')
        public_key_string = public_key.decode('utf-8')

        with open(private_key_filename, 'w') as private_key_file:
            private_key_file.write(private_key_string)

        with open(public_key_filename, 'w') as public_key_file:
            public_key_file.write(public_key_string)

        return True

if __name__ == '__main__':
    key_tools = RsaKeyTools()
    private_key, public_key = key_tools.generate_key_pair()
    print("Public Key string\n")
    print(public_key)
    print("Private key string\n")
    print(private_key)


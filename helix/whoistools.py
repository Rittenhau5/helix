#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  whoistools.py
#  
# Python 3.4.4
#
#
# Collection of command line network and information gathering tools.
# 
# IMPORTS
import whois
import socket

# STATIC VARIABLES

# MODULE
class WhoisTools(object):
    """
    Collection of network information gathering tools.

    """
    def __init__(self):
        pass

    def get_dns_information(self, lookup_address):
        """
        Gets DNS name information for URL inputted, returns dictionary with all data.
        :param lookup_address:
        :return:

        """
        lookup = whois.whois(lookup_address)
        return lookup

    def ip_name_lookup(self, ip_address):
        """
        Converts IP address to domain name.
        :param ip_address:
        :return:

        """
        while True:
            try:
                domain_name = socket.gethostbyaddr(ip_address)
                return domain_name
            except socket.error:
                return "Error: Host not found"

    def check_if_ip(self, input_string):
        """
        Checks if inputted string contains numbers for IP address.
        :param inputString:
        :return:

        """
        return any(c.isdigit() for c in input_string)


if __name__ == '__main__':
    lookup = NameTools()
    dnsInfo = lookup.get_dns_information('www.facebook.com')
    print(dnsInfo)

    nameInfo = lookup.ip_name_lookup('31.13.74.52')
    nameInfo = nameInfo[0]

    print(nameInfo)
    dnsInfo = lookup.get_dns_information(nameInfo)
    print(dnsInfo)




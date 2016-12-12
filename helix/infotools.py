#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  infotools.py
#  
# Python 3.4.4
#
#
# Info tools module contains all information gathering scripts, such as system and network information.
# 
# IMPORTS
from requests import get
import datetime
import platform
import socket
import geocoder




# STATIC VARIABLES



# MODULE
class InfoTools(object):
    """
    Collection of information gathering functions.

    """
    def __init__(self):
        pass

    def get_date(self):
        """
        Collects time data and parses.
        :return:

        """
        now = datetime.datetime.now()
        banner = "%d/%d/%d" % (now.month, now.day, now.year)
        return banner

    def get_private_ip(self):
        """
        Returns private IP address
        :return:

        """
        private_ip_address = socket.gethostbyname(socket.gethostname())
        return private_ip_address


    def get_public_ip(self):
        """
        Returns public IP address of host computer.
        :return:

        """
        public_ip_address = get("https://api.ipify.org").text
        return public_ip_address

    def get_hostname(self):
        """
        Returns system hostname.
        :return:

        """
        network_name = platform.node()
        return network_name

    def get_processor_type(self):
        """
        Returns processor type.
        :return:

        """
        machine_type = platform.machine()
        return machine_type

    def get_operating_system(self):
        """
        Returns operating system details.
        :return:

        """
        local_platform = platform.system()
        return local_platform

    def get_os_version(self):
        """
        Returns operating system version
        :return:

        """
        local_version = platform.version()
        return local_version

    def get_python_version(self):
        """
        Returns python system version.
        :return:

        """
        python_version = platform.python_version()
        return  python_version

    def get_city_location(self):
        """
        Returns city location data.
        :return:

        """
        public_ip_address = self.get_public_ip()
        geo = geocoder.freegeoip(public_ip_address)
        return geo.city

    def get_state_location(self):
        """
        Returns state location data.
        :return:

        """
        public_ip_address = self.get_public_ip()
        geo = geocoder.freegeoip(public_ip_address)
        return geo.state


if __name__ == '__main__':
    info = InfoTools()
    public_ip = info.get_public_ip()
    current_time = info.get_time()
    private_ip = info.get_private_ip()
    pythonVersion = info.get_python_version()

    print(public_ip)
    print(current_time)
    print(private_ip)
    print(pythonVersion)




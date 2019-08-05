#!/usr/bin/env python

'''
| Description:
    Change MAC address of interface by user input
    arguments through bash command.
| Notes:
    MAC address 1st octet must be even number
| Version: 
    4
| Variables:
    interface
    new_mac
'''

import subprocess
import argparse

def get_arguments():
    '''
    Get mac_changer.py arguments passed from user input.
    Returns parser object's stored objects passed from user input.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()    

def change_mac(interface, new_mac):
    '''
    Change mac address of specified interface to new mac address.
    '''    
    print("[+] Changing MAC address for", interface, "to", new_mac) 
    # Safe practice using lists to store bash commands
    # Can hijack program through code injection " wlan0;ls; "
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])    

    # UNsafe practice using string concatenation to store bash commands
    # Can hijack program through code injection " wlan0;ls; "
    """
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether ", + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)
    """
#--------------[ MAIN ]--------------

args = get_arguments()
change_mac(args.interface, args.new_mac)


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
    args = parser.parse_args()    
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    if not args.new_mac:
        parser.error("[-] Please specify a new mac address, use --help for more info.")
    return args


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


#--------------[ MAIN ]--------------

args = get_arguments()
change_mac(args.interface, args.new_mac)


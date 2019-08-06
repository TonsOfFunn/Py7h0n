#!/usr/bin/env python3

'''
| Description:
    Change MAC address of interface by user input
    arguments through bash command.
| Notes:
    MAC address 1st octet must be even number
| Version: 
    6
| Variables:
    interface
    new_mac
'''

import subprocess
import argparse
import re

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


def get_current_mac(interface):
    '''
    Get current MAC address from output of command ifconfig <interface>
    '''
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    
    # use regex to search for MAC address in output of ifconfig command
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))   
    
    # check if mac was found in search result
    if mac_search_result:
        return mac_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")    

#--------------[ MAIN ]--------------

args = get_arguments()

current_mac = get_current_mac(args.interface)
print("[*] Current MAC address", current_mac)

change_mac(args.interface, args.new_mac)

current_mac = get_current_mac(args.interface)
if current_mac == args.new_mac:
    print("[+] MAC address was successfully changed to", current_mac)
else:
    print("[-] MAC address did not get changed.")


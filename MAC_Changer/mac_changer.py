#!/usr/bin/env python

'''
| Change MAC address of interface by user input.
| Version: 1
| Variables:
    interface
    new_mac
'''

import subprocess

print("[+] Changing MAC address for " + interface + " to " + new_mac)

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


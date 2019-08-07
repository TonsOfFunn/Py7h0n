#!/usr/bin/env python2

'''
| Description:
    Network devices scanner and enumerator
| Notes:
    Cannot import scapy using python3
| Version: 
    1
| Variables:
    
'''

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

# returns MAC address of scanned IP range    
scan("10.0.2.0/24")
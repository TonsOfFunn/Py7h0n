#!/usr/bin/env python2

'''
| Description:
    Network devices scanner and enumerator
| Notes:
    
| Version: 
    1
| Variables:
    
'''

import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

# returns MAC address of scanned IP    
scan("10.0.2.2")
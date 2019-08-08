#!/usr/bin/env python2

'''
| Description:
    Network devices scanner and enumerator to discover clients
    on a network.
| Notes:
    Cannot import scapy using python3
| Steps:
    1. Create arp request directed to broadcast MAC asking for IP.
    2. Send packet and receive respones.
    3. Parse the response.
    4. Print result.
| Version: 
    3
| Variables:
    ip
'''

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    print(arp_request.summary())

# returns mac address of scanned ip range    
scan("10.0.2.0/24")



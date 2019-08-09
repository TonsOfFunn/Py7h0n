#!/usr/bin/env python2

'''
| Description:
    Network devices scanner and enumerator to discover clients
    on a network.
| Version:
    4
| Notes:
    Cannot import scapy using python3
| Algorithm:
    1. Create ARP request directed to broadcast MAC asking for IP.
        1.a Use ARP to ask who has target IP.
        1.b Set destination MAC to broadcast MAC.
    2. Send packet and receive respones.
    3. Parse the response.
    4. Print result.
| Variables:
    ip
'''

import scapy.all as scapy

def scan(ip):
    # create ARP packet
    arp_request = scapy.ARP(pdst=ip)

    # create broadcast frame
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')

    # encapsulate ARP packet in broadcast frame
    arp_request_broadcast = broadcast/arp_request

    # srp send/receive/packets with custom mac address
    answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    print(answered.summary())

#--------------[ MAIN ]--------------

# returns mac address of scanned ip range    
scan("10.0.2.0/24")



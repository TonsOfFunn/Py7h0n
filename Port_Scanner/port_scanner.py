#!/usr/bin/env python

'''
| Description:
    Scan for open ports on designated IP address
| Usage:
    python3 port_scanner.py 127.0.0.1
| Notes:

| Version: 
    3
| Variables:
    nm_scan
    nm_scanner
    host_up
    port_open
    method_scan
    guessed_os
'''

import nmap
import sys
from pprint import pprint

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments='-O')

pprint(nm_scanner)

host_up = "The host is: " + nm_scanner['scan'][sys.argv[1]]['status']['state'] + ".\n"
port_open = "The port 80 is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state'] + ".\n"
scan_method = "The method of scanning is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + ".\n"
guessed_os = "There is a %s percent chance that the host is running %s" %(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'], nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name']) + ".\n"




print(host_up)
print(port_open)
print(scan_method)
print(guessed_os)



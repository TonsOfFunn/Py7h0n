#!/usr/bin/env python

'''
| Description:
    Scan for open ports on designated IP address
| Notes:

| Version: 
    1
| Variables:
    nm_scan
    nm_scanner
'''

import nmap
import sys

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments='-O')

print(nm_scanner)



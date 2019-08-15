#!/usr/bin/env python

'''
| Description:
    Scan for open ports on designated IP address
| Usage:
    python3 port_scanner.py 127.0.0.1
| Notes:

| Version: 
    2
| Variables:
    nm_scan
    nm_scanner
'''

import nmap
import sys
from pprint import pprint

nm_scan = nmap.PortScanner()
nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments='-O')

pprint(nm_scanner)



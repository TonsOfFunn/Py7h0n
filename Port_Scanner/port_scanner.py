#!/usr/bin/env python

'''
| Description:
    Scan for open ports on designated IP address
| Usage:
    python3 port_scanner.py 127.0.0.1
| Notes:

| Version: 
    4
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
import time

nm_scan = nmap.PortScanner()

print("\nRunning...")

nm_scanner = nm_scan.scan(sys.argv[1], '80', arguments='-O')

# parse scan results to variables
host_up = "The host is: " + nm_scanner['scan'][sys.argv[1]]['status']['state'] + ".\n"

port_open = "The port 80 is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state'] + ".\n"

scan_method = "The method of scanning is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + ".\n"

guessed_os = "There is a %s percent chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"

# write scan results to file
with open("%s.txt" % sys.argv[1], 'w') as f:
    f.write(host_up + port_open + scan_method + guessed_os)
    f.write("\nReport generated " + time.strftime("%Y-%m-%d_%H:%M:%S GMT\n", time.gmtime()))
    f.close()

print("\nFinished...")


#!/usr/bin/env python3
import os

staticip = input("What is the new static IP address for this host, ending with /24 prefix?")
gatewayip = input("What is the new gateway IP address for this host?")
nameserverip = input("What is the new DNS server IP address for this host?")

os.popen("mv 01-netcfg.yaml 01-netcfg.yaml.bak")

ifc = os.popen("ifconfig | awk 'NR==1{print $1}'")
nic = ifc.readline(5)

with open("01-netcfg.yaml", 'a') as f:
    f.write('network:\n')
    f.write('  version: 2\n')
    f.write('  renderer: networkd\n')
    f.write('  ethernets:\n')
    f.write('    '+ nic + "\n")
    f.write('      dhcp4: no\n')
    f.write('      addresses: ['+ staticip +"]\n")
    f.write('      gateway4: '+ gatewayip + "\n")
    f.write('      nameservers:\n')
    f.write('        addresses: ['+ nameserverip +"]\n")

os.popen("sudo netplan apply")
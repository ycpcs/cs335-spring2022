#!/usr/bin/python3
from scapy.all import *

print("SENDING SPOOFED UDP PACKET.........")
ip = IP(src="1.2.3.4", dst="10.20.30.40") 	# IP Layer
udp = UDP(sport=8888, dport=9090)       	# UDP Layer
data = "Spoofing UDP!\n"                   	# Payload
pkt = ip/udp/data      						# Construct the complete packet
pkt.show()
send(pkt,verbose=0)

---
layout: default
course_number: CS335
title: Code Snippets
---

Creating UDP packets

```
#!/usr/bin/python3
from scapy.all import *

IPpkt  = IP(dst='10.0.2.5', chksum=0)
UDPpkt = UDP(dport=9090, chksum=0)
data = "Woo hoo, UDP server!\n"
pkt = IPpkt/UDPpkt/data

# Save the packet data to a file
with open('ip.bin', 'wb') as f:
  f.write(bytes(pkt))
```

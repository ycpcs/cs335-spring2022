---
layout: default
course_number: CS335
title: Code Snippets
---

This page contains code snippets regularly used in class.

<!--
#### Password
- Built _John The Ripper_ from source:
  - ```git clone https://github.com/magnumripper/JohnTheRipper.git```
  - ```cd ./JohnTheRipper/src```
  - ```sudo apt-get update```
  - ```sudo apt-get install libssl-dev```
  - ```./configure```
  - ``` make -s clean && make -sj4```

- We can also download the binaries as zip:
  - ```wget https://github.com/magnumripper/JohnTheRipper/archive/bleeding-jumbo.zip```
  - ```unzip bleeding-jumbo.zip```
  - ```cd JohnTheRipper-bleeding-jumbo/src```
  - ```./configure && make```
  - ``` make -s clean && make -sj4```

- We can also download the binaries as tar:
  - ```sudo apt-get install libssl-dev```
  - ```wget https://www.openwall.com/john/k/john-1.9.0-jumbo-1.tar.xz```
  - ```tar -xvf ./john-1.9.0-jumbo-1.tar.xz```
  - ```cd john-1.9.0-jumbo-1/src```
  - ```./configure```
  - ``` make -s clean && make -sj4```

- Install it using the app store (not recommended):
  - ```sudo apt install john```

- Install using [snapd](https://snapcraft.io/) (not recommended):
  - ```sudo snap install john-the-ripper```

- Install THC-Hydra
  - ```wget https://github.com/vanhauser-thc/thc-hydra/archive/v9.1.tar.gz```
  - ```tar -xvf v9.1.tar.gz```
  - ```cd thc-hydra-9.1```
  - ```./configure```
  - ```make```
  - ```sudo make install```

- Crack me
  - [joke.docx](pass\joke.docx)
  - [joke.pdf](pass\joke.pdf)

#### SQL
- [Insert Employees](sql\insert_script.html)

#### XSS
- [Add a friend](xss\add_friend.html)
- [Update Profile](xss\edit_profile.html)
- Content Security Policy Experiment
  - [http_server.py](csp\http_server.html)
  - [index.html](csp\index.html)

#### CSRF
- [Template](csrf\post.html) for POST attacks

#### ARP
- Add firewall rule on the client
  - sudo iptables -t nat -A OUTPUT -p tcp --dport 8000 -j DNAT --to-destination _attacker_ip_address_
- Rules on the attacker
  - sudo sysctl -w net.ipv4.ip_forward=1
  - sudo iptables -t nat -A PREROUTING -p tcp --dport 8000 -j DNAT --to-destination _server_ip_address_
  - sudo iptables -t nat -A POSTROUTING -j MASQUERADE

#### DNS
- Add to `/etc/bind/`
  - [etc/bind/191.168.0.db](dns\191.168.0.db)
  - [etc/bind/cs335.com.db](dns\cs335.com.db)
- Append to `/etc/bind/named.conf`
  - [cs335zone](dns\cs335_zone.html)
- [dns_spoof.py](dns\dns_spoof.py)
-->
<!--
#### TCP
- Client: [tcp_client.c](tcp\tcp_client.c)
- Server: [tcp_server.c](tcp\tcp_server.c) & [tcp_server_multi.c](tcp\tcp_server_multi.c)
- Sent RST packet: [rst_packet.py](tcp\rst_packet.py)
-->

#### Packet Sniffing and Spoofing
- Sniffing
  - UDP server: [udp_server.c](sniff\udp_server.c)
  - Packet Sniffing using raw sockets: [sniff_raw.c](sniff\sniff_raw.c)
  - Packet Sniffing using pcap API: [sniff_pcap.c](sniff\sniff_pcap.c)
  - Packet Sniffing using pcap API (improved): [sniff_ether.c](sniff\sniff_ether.c)
  - Sniff using Scapy: [sniff.py](sniff\sniff.py)
- Spoofing
  - UDP client: [udp_client.c](sniff\udp_client.c)
  - Spoof ICMP using raw sockets: [spoof_icmp.c](sniff\spoof_icmp.c)
  - Spoof UDP using raw sockets: [spoof_udp.c](sniff\spoof_udp.c)
  - Spoof TCP using raw sockets: [spoof_tcp.c](sniff\spoof_tcp.c)
  - Spoof UDP using Scapy: [spoof_udp.py](sniff\spoof_udp.py)
  - Spoof ICMP using Scapy: [spoof_icmp.py](sniff\spoof_icmp.py)
- Sniffing along with Spoofing
  - Create packet using Scapy: [create_udp_packet.py](sniff\create_udp_packet.py)
  - Send created packet using raw sockets: [send_udp_packet.c](sniff\send_udp_packet.c)
  - Sniffing and the Spoofing ICMP using Scapy: [sniff_snoop_icmp.py](sniff\sniff_snoop_icmp.py)
- Helpers
  - TCP/IP Header Structures: [ip.h](sniff\ip.h)
  - Calculating Checksum: [checksum.h](sniff\checksum.c)
  - Send Raw Packets (method only): [spoof.c](sniff\spoof.c)

#### Buffer Overflow
- Memory Layout: [mem_layout.cpp](buffer_overflow\mem_layout.cpp)
- Launching shell: [launch_shell.c](buffer_overflow\launch_shell.c)
- ASCII vs binary: [print_zero.c](buffer_overflow\print_zero.c)
- Print *esp*: [sp.c](buffer_overflow\sp.c)
- ASLR: [aslr.c](buffer_overflow\aslr.c)

<!--
##
## Shell Shock
- Attack on Set-UID: [vul.c](shell_shock\vul.c)
- Vulnerable Bash program: [variables.c](shell_shock\variables.c)
- Attack on CGI program: [test.cgi](shell_shock\test.cgi)
-->

#### Reverse Shell
- File Descriptors: [fd.c](reverse_shell\fd.c)
- Redirection (demo): [red.c](reverse_shell\red.c)
- Redirection (dup): [dup.c](reverse_shell\dup.c)
- Redirection (dup2): [dup2.c](reverse_shell\dup2.c)
- Redirection (tcp out): [tcp_out.c](reverse_shell\tcp_out.c)
- Redirection (tcp in): [tcp_in.c](reverse_shell\tcp_in.c)

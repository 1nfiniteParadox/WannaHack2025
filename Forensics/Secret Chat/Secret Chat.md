## Description
Two Agents were communicating through a TCP connection which they thought was secure, but somehow there connection was being tapped.... Check out the chat and find something useful.

## Given Files
![[chall.pcap]]

## Solution
The description hinted on TCP Protocols.
I opened this file in Wireshark and followed the TCP Stream to get the conversation.

![[Pasted image 20250114015916.png]]

Found this **V2FubmFIYWNre1RDUF9FTkMwREVEX0NINFR9** string in the conversation.
Found the flag after Base 64 decoding.

## Flag
WannaHack{TCP_ENC0DED_CH4T}
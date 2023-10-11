# Net_Practice

## Some Notes

DEFINITIONS

LAN - Local Area Network

WAN - Wide Are Network

SWITCH - Connects LAN devices

ROUTER - Forwards data between different networks

SUBNET - Defines LAN Range

ROUTER (GATEWAY) Functionality:

NAT - Network Address Translation

FIREWALL - set of passive rules to protect the network from unauthorized access.

DMZ - (demilitarize zone ?!)

ARP - Address Resolution Protocol

HTTP - Hyper Text Transfer Protocol

SSL - Secure Socket Layer

TLS - Transport Layer Security

HTTPS - HTTP secured with SSL/TSL

FTP - File Transfer Protocol

SMTP - Simple Mail Transfer Protocol

DNS - Domain Name System

IP Address = Host’s Identity on the Internet

SM - Subnet Mask

DG - Default Gateway (router’s IP address)

DHCP - Dynamic Host Config. Protocol

TCP/IP  - Transmission Control Protocol/Internet Protocol

UDP - User Datagram Protocol

CIDR - Classless Inter-domain Routing

=============================================================

Network Address Translation - remapping IP address for the trafic routing through the network.

PORT FORWARDING - redirects a communication request address and port number combination to another while the packets traversing a network gateway (router or firewall).

SUBNET MASK eg: (/24) == (255.255.255.0)

IP, SM and DG are necessary components to be able to speak to any FTP server in the internet given its IP address. And to speak to any other server (SMTP - mail, WEB - http )  in the internet DNS’s IP is needed as well in order to translate server’s (public)address into its IP address.

So, IP, SM, DM and DNS must be configured on any host for it to be able to communicate with the internet.

DHCP is a protocol which configures IP, SM, DM, DSM for each host device automatically once it is connected to the (new/old) network.



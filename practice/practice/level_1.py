# Level 1:

# Network layout / topology:
client_B = {
    "name": "my little brother's computer",
    "interface": "B1",
    "IP": "104.94.23.12",
    "Mask": "255.255.255.0"
}

client_A = {
    "name": "my PC",
    "interface": "A1",
    "IP": "104.93.23.285",
    "Mask": "255.255.255.0"
}

client_D = {
    "name": "my little sister's computer",
    "interface": "D1",
    "IP": "211.190.319.42",
    "Mask": "255.255.0.0"
}

client_C = {
    "name": "my Mac",
    "interface": "C1",
    "IP": "211.191.145.75",
    "Mask": "255.255.0.0"
}

# Topology description:
"""
Client_A and client_B are on the same network. Modifiable: IP of client_A.
Client_C and client_D are on the same network. Modifiable: IP of client_D.
"""

# Task description:
"""
Goal 1: "my PC" needs to communicate with "my little brother's computer"
Goal 2: "my Mac" needs to communicate with "my little sister's computer"
"""

# Solution description and approach:
"""
To achieve Goal 1:
	client_A and client_B need to be on the same subnet
	Based of the 'Mask' their IP addresses need to have 
	the same network prefix: (104.94.23.---)
	This will put client_A and client_B on the same /24 subnet 104.94.23.0/24

To achieve Goal 2:
	client_C and client_D need to be on the same subnet
	Based of the 'Mask' their IP addresses need to have 
	the same network prefix: (211.190.---.---)
	This will put client_C and client_D on the same /16 subnet 211.191.0.0/16

'/24' means the subnet mask is "255.255.255.0". 
This masks the first 24 bits of the IP address, leaving the last 8 bits for host addresses. 
So a '/24' subnet has 256 (2^8) host addresses.

'/16' means the subnet mask is "255.255.0.0". 
This masks the first 16 bits of the IP address, leaving the last 16 bits for host addresses. 
So a '/16' subnet has 65536 (2^16) host addresses.

In general, '/x' refers to a subnet with a x-bit prefix and 32-x host bits. 
The subnet mask has x 1's followed by 32-x 0's in binary.

So in our example:
	'/24' (subnet mask 255.255.255.0) allows 256 hosts per subnet. 
	This puts client_A and client_B in the same 104.94.23.0/24 subnet.

	'/16' (subnet mask 255.255.0.0) allows 65536 hosts per subnet. 
	This puts client_C and client_D in the same 211.191.0.0/16 subnet.
"""

# Paramters to be added:
client_A["IP"] = "104.94.23.100"
client_D["IP"] = "211.191.145.200"

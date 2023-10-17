# Level 2:

# Network layout / topology:
client_A = {
    "name": "Computer A",
    "interface": "A1",
    "IP": "",
    "Mask": "255.255.255.224"
}

client_B = {
    "name": "Computer B",
    "interface": "B1",
    "IP": "192.168.28.222",
    "Mask": ""
}

client_C = {
    "name": "Computer C",
    "interface": "C1",
    "IP": "",
    "Mask": "255.255.255.252"
}

client_D = {
    "name": "Computer D",
    "interface": "D1",
    "IP": "",
    "Mask": "/30"
}

# Topology description:
"""
client_A directly connected to client_B.
client_C directly connected to client_D.
"""

# Task description:
"""
Goal 1: "Computer B" needs to communicate with "Computer A"
Goal 2: "Computer D" needs to communicate with "Computer C"
"""

# Solution description and approach:
"""
Subnetting is the process of dividing a network into smaller subnetworks 
or subnets to efficiently utilize IP addresses and manage network traffic.
Each subnet has its own range of IP addresses and a subnet mask that 
determines the network and host portions of an IP address.

In the given scenario, the client_C and client_D are connected directly, 
and we need to modify their IP addresses to enable communication between them.
The subnet mask for both clients is "255.255.255.252", 
which means there are only 2 usable host IP addresses in the subnet.

To calculate the valid range within this subnet, 
we need to consider the network and broadcast addresses. 
The network address is the first IP address in the subnet, 
and the broadcast address is the last IP address.

In a /30 subnet, the formula to calculate the valid range is: 
Valid Range = Network Address + 1, Network Address + 2, ..., Broadcast Address - 1

To calculate the network address, we can perform a bitwise logical AND operation 
between the IP address and the subnet mask. 
For example: 
	client_C network address = client_C IP & client_C subnet mask 
	client_D network address = client_D IP & client_D subnet mask

To calculate the broadcast address, we perform the bitwise logical OR operation 
between the network address and the inverse of the subnet mask. 
For example: 
	client_C broadcast address = client_C network address | (client_C subnet mask) 
	client_D broadcast address = client_D network address | (client_D subnet mask)

Once we have the network address and broadcast address, 
we can determine the valid range of IP addresses for each client.

---
How to calculate the valid range without knowing the specific IP addresses: 
	we can leverage the nature of a /30 subnet. In a /30 subnet, 
	there are only 4 possible IP addresses: the network address, 
	the broadcast address, and two usable host addresses. 
	These host addresses will be the valid IP range within the subnet.

subnet_mask = "255.255.255.252"

Step 1: Converting the subnet mask to its binary representation.
	The subnet mask "\30" in binary will be: 
	"11111111 11111111 11111111 11111100"

Step 2: Identifying the number of posible host.
	There are 2 bits, which can be used for hosts.
	So, 'possible hosts' in this case will be 4

Step 3: Calculate the valid IP range
	Choose the arbitrary network address:
	network_address = "192.168.4.0"
	Converting the network address to its binary representation:
	"11000000 10101000 00000100 00000000"

Step 4: Determine the first and last IP addresses in the valid range
	First IP address = network address + 1 
	"192.168.4.1"
	Last IP address = network address + possible hosts - 2
						(192.168.4.0)  		(4)
	"192.168.4.2"
"""

# Paramters to be added:
client_A["IP"] = "192.168.28.193" # the IP range can be from 193 to 221 given the Mask
client_B["Mask"] = "255.255.255.224" # should bethe same as client_A mask, which is NOT modifiable

client_C["IP"] = "192.168.0.1"
client_D["IP"] = "192.168.0.2"

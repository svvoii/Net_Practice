# Level 4:

# Network layout / topology:
client_A = {
    "name": "A nice host",
    "interface": "A1",
    "IP": "108.84.118.132",
    "Mask": ""
}

client_B = {
    "name": "Another host",
    "interface": "B1",
    "IP": "",
    "Mask": ""
}

switch_S = {
    "name": "Switch-1",
}

router_R = {
    "name": "My_Gate",
	"interfaces": [
		{
			"interface": "R1",
			"IP": "",
			"Mask": ""
		},
		{
			"interface": "R2",
			"IP": "108.84.118.1",
			"Mask": "255.255.255.128"
		},
		{
			"interface": "R3",
			"IP": "108.84.118.224",
			"Mask": "255.255.255.192"
		}	
	]
}

# Topology description:
"""
client_A and client_B are connected to switch_S and 
switch_S is connected to router_R through its interface R1
"""

# Task description:
"""
Goal 1: client_A need to communicate with client_B.
Goal 2: client_A need to communicate with router_R.
Goal 3: client_B need to communicate with router_R.
"""

# Solution description and approach:
"""
Some calculations to determine the range of IP addresses for a 
subnet mask of 255.255.255.128:

The subnet mask 255.255.255.128 in binary is:
11111111.11111111.11111111.10000000

This mask has 25 prefix bits set to 1. 
This leaves 7 bits for host addresses.
The number of possible host IPs is calculated as 2^7 which is 128

The valid host IP range for this subnet is: 108.84.118.129 - 108.84.118.254
with network address: 108.84.118.128 
and broadcast address: 108.84.118.255
 
For client B to be able to communicate with client A and router R, 
it needs to have an IP address within the 108.84.118.128/25 subnet range.

"""

# Paramters to be added:
router_R["interfaces"][0]["IP"] = "108.84.118.129"
router_R["interfaces"][0]["Mask"] = "255.255.255.128"
client_A["Mask"] = "255.255.255.128"
client_B["IP"] = "108.84.118.131"
client_B["Mask"] = "255.255.255.128"

# Level 3:

# Network layout / topology:
client_A = {
    "name": "Host A",
    "interface": "A1",
    "IP": "104.198.12.125",
    "Mask": ""
}

client_B = {
    "name": "Host B",
    "interface": "B1",
    "IP": "",
    "Mask": ""
}

client_C = {
    "name": "Host C",
    "interface": "C1",
    "IP": "",
    "Mask": "255.255.255.128"
}

switch_S = {
    "name": "Switch-1",
}

# Topology description:
"""
Host A, Host B, Host C are connected through Switch-1
"""

# Task description:
"""
Goal 1: "Host A need to communicate with Host B"
Goal 2: "Host A need to communicate with Host C"
Goal 3: "Host B need to communicate with Host C"
"""

# Solution description and approach:
"""
How to identify the valid IP addresses within the subnet range for this example:

Host C has a subnet mask of "255.255.255.128" or "/25".

"/25" subnet has a 25-bit prefix, leaving 7 bits for host addresses.
2^7 = 128 possible host addresses.

The network address is identified by the prefix 104.198.12.0/25.

So the valid host IP range is:
104.198.12.1 - 104.198.12.126

For example:
	Given the 
	Host A IP as: 104.198.12.125
	we can set
	Host (B or C) IP to: 104.198.12.126
	Host (C or B) IP to: 104.198.12.124

This puts all three hosts in the same 104.198.12.0/25 subnet, allowing communication.

The network address: 104.198.12.0
and broadcast address: 104.198.12.127
cannot be assigned as host IPs.

Identify the subnet mask
Calculate the prefix length (/25)
Calculate the number of host bits (7)
Calculate the number of possible hosts (2^7 = 128)
Identify the network address (104.198.12.0/25)
Derive the valid host IP range from this (104.198.12.1-104.198.12.126)
Assign IPs to other hosts from within this range
"""

# Paramters to be added:
client_A["Mask"] = "255.255.255.128"
client_B["IP"] = "104.198.12.124"
client_B["Mask"] = "255.255.255.128"
client_C["IP"] = "104.198.12.126"

# Level 3:

# Task description:
# 
# Host A, Host B, Host C are connected to Switch-1
#
# Goal 1: "Host A need to communicate with Host B"
# Goal 2: "Host A need to communicate with Host C"
# Goal 3: "Host B need to communicate with Host C"

# Given network settings parameters:
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

# Modify the following parameters to achieve the Goal :
client_A["Mask"] = "255.255.255.128"
client_B["IP"] = "104.198.12.124"
client_B["Mask"] = "255.255.255.128"
client_C["IP"] = "104.198.12.126"
# client_B and client_C IPs can be swiched but must be next or previous from client_A IP

## SOLUTION ##

# Since Host A, B and C are connected to the same switch, 
# they need to be in the same subnet to communicate directly.

# Host C's mask is 255.255.255.128, which means its 
# subnet is 104.198.12.0/25.

# Setting Host A and B masks to match Host C's mask puts 
# them in the same subnet.

# Choosing IP addresses within the subnet range allows
# communication between the hosts.

"""
How to identify the valid IP addresses within the subnet range for this example:

Host C has a subnet mask of 255.255.255.128, 
this means the subnet is a /25.

A /25 subnet has a 25-bit prefix, leaving 7 bits for host addresses.
2^7 = 128 possible host addresses.

The network address is identified by the prefix 104.198.12.0/25.

So the valid host IP range is:
104.198.12.1 - 104.198.12.126

For example:

Given the 
Host A IP as: 104.198.12.125
we can set
Host B IP to: 104.198.12.126
Host C IP to: 104.198.12.124
(or vice versa)

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
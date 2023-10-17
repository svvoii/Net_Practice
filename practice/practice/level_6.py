# Level 6:

# Network layout / topology:
client_A = {
    "name": "webserv.non-real.com",
    "interface": "A1",
    "IP": "62.117.76.227",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

switch_S = {
    "name": "sw-1.non-real.com",
}

router_R = {
    "name": "gate.non-real.com",
	"interfaces": [
		{
			"interface": "R1",
			"IP": "",
			"Mask": "255.255.255.128"
		},
		{
			"interface": "R2",
			"IP": "163.172.250.12",
			"Mask": "255.255.255.240"
		}
	],
	"Destination": "",
	"Next hop": "163.172.250.1"
}

internet_I = {
	"name": "Internet",
	"interface": "Somewhere on the Net",
	"IP": "8.8.8.8",
	"Mask": "/16",
	"Destination": "",
	"Next hop": "163.172.250.12"
}


# Topology description:
"""
client_A is connected to switch_S and
switch_S is connected to router_R through interface R1 and
router_R connected to the internet_I through interface R2
"""

# Task description:
"""
Goal 1: "interface 'A1' need to communicate with the Internet interface 'Somewhere on the Net'"
"""

# Solution description and approach:
"""
Adding to the previous task, the concept of routing table is introduced.
Here we have a routing table from at the Internet interface.
The first field in the routing table is "Destination".
It should contain the destination IP range, "Network address" with the mask as a suffix,
indicating the range of IP addresses that can be reached through this interface.
"""

# Paramters to be added:
client_A["Mask"] = "255.255.255.128"
client_A["Destination"] = "default" # or 0.0.0.0/0
client_A["Next hop"] = "62.117.76.129"
router_R["interfaces"][0]["IP"] = "62.117.76.129" # technically can be any IP in the range according to mask
router_R["Destination"] = "default"
internet_I["Destination"] = "62.117.76.128/25" # this one should be the destination IP range with netmask for client_A

# Level 7:

# Network layout / topology:
client_A = {
    "name": "dev.non-real.net",
    "interface": "A1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

router_R1 = {
    "name": "tech.non-real.net",
	"interfaces": [
		{
			"interface": "R11",
			"IP": "101.198.14.1",
			"Mask": ""
		},
		{
			"interface": "R12",
			"IP": "101.198.14.254",
			"Mask": ""
		}
	],
	"Destination": "",
	"Next hop": ""
}

router_R2 = {
    "name": "adm.non-real.net",
	"interfaces": [
		{
			"interface": "R21",
			"IP": "",
			"Mask": ""
		},
		{
			"interface": "R22",
			"IP": "",
			"Mask": ""
		}
	],
	"Destination": "",
	"Next hop": ""
}

client_C = {
    "name": "accounting.non-real.net",
    "interface": "C1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

# Topology description:
"""
client_A is connected to router_R1's interface R11, 
router_R1's interface R12 is connected to router_R2's interface R21, 
client_C is connected to router_R2's interface R22.
"""

# Task description:
"""
Goal: client_A need to communicate with client_C
"""

# Solution description and approach:
"""
Given network layout in this task there should have at least 3 subnetworks to manage.
1st subnet: router_R1's interface R11 and client_A's interface
2nd subnet: router_R2's interface R22 and client_C's interface
3rd subnet: router_R1's interface R12 and router_R2's interface R21

Since the task doe not precise any subnet mask it is required to chose the proper one.
So, we can check the subnetting table to identify which subnet mask can handle at least 3 subnets
in this case the '/26' or '255.255.255.192` submask can handle up to 4 subnets with the folowing 
IP addresses range:
-.-.-.1 - 62
-.-.-.65 - 126
-.-.-.129 - 190
-.-.-.193 - 254

It is also possible to use other subnet masks for subnets with clients.
In this case those subnet masks should be higher in value than subnet where the both routers are located.
If routers are in '/26's subnet the clients could be in '/27', '/28', '/29' subnet with appropriate 
IP addresses range.

Filling in the IPs we need to keep in mind that connected interfaces should be within respective IP range
chosen for that subnet

The routing table in this task is more straight forward since it is not necessary to use 
specific destination, 'defailt' / '0.0.0.0/0' value would be sufficient.
"""

# Paramters to be added:
client_A["IP"] = "101.198.14.2"
client_A["Mask"] = "255.255.255.192" # or "/26"
client_A["Destination"] = "0.0.0.0/0" # or "default"
client_A["Next hop"] = "101.198.14.1" # interface of the nearest connected router

router_R1["interfaces"][0]["Mask"] = "255.255.255.192" # or "/26"
router_R1["interfaces"][1]["Mask"] = "255.255.255.128" # also can be "/25" or higher but not lower since there should be roo m for at least 3 sub-networks
router_R1["Destination"] = "0.0.0.0/0" # or "default"
router_R1["Next hop"] = "101.198.14.253"

router_R2["interfaces"][0]["IP"] = "101.198.14.253"
router_R2["interfaces"][0]["Mask"] = "255.255.255.128" # should be the same as R1 mask
router_R2["interfaces"][1]["IP"] = "101.198.14.65" # can bi in the range from -.-.-.65 to 126, according to subnet mask /26
router_R2["interfaces"][1]["Mask"] = "255.255.255.192" # or "/26" also can be /27, /28, /29, /30 but not smaler that /26
router_R2["Destination"] = "101.198.14.254"
router_R2["Next hop"] = "0.0.0.0/0"

client_C["IP"] = "101.198.14.66" # can bi in the range from -.-.-.65 to 126, according to subnet mask /26
client_C["Mask"] = "255.255.255.192" # or "/26"
client_C["Destination"] = "0.0.0.0/0" # or "default"
client_C["Next hop"] = "101.198.14.65" # interface of the nearest connected router

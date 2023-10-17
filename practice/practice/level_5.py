# Level 5:

# Network layout / topology:
client_A = {
    "name": "Machine A",
    "interface": "A1",
    "IP": "",
    "Mask": "",
	"routes from": "",
	"routes to": ""
}

client_B = {
    "name": "Machine B",
    "interface": "B1",
    "IP": "",
    "Mask": "",
	"routes from": "defaul",
	"routes to": ""
}

router_R = {
    "name": "My_Gate",
	"interfaces": [
		{
			"interface": "R1",
			"IP": "63.157.228.126",
			"Mask": "255.255.255.128"
		},
		{
			"interface": "R2",
			"IP": "167.49.253.254",
			"Mask": "255.255.192.0"
		}
	]
}

# Topology description:
"""
client_A is connected to router_R through interface R1
client_B is connected to router_R through interface R2
"""

# Task description:
"""
Goal 1: "'Machine A' need to communicate with 'The Mighty Router'"
Goal 2: "'Machine B' need to communicate with 'The Mighty Router'"
Goal 3: "'Machine A' need to communicate with 'Machine B'"
"""

# Solution description and approach:
"""
Starting from this exercise, the concept of routing table is introduced.
The first field in the routing table is "Destination". 
This field specifies the general destination of the traffic.
In this tasks set all cases from the HOST side this is set to "default", 
this means that the traffic is sent to the gateway specified in "Next hop".

The second field is "Next hop". This field specifies the next hop of the traffic.
This is the nearest router "gateway" that can forward the traffic to the destination.

Everything else is the same as in the previous tasks set.
"""

# Paramters to be added:
client_A["IP"] = "63.157.228.125"
client_A["Mask"] = "255.255.255.128"
client_A["routes from"] = "defaul"
client_A["routes to"] = "63.157.228.126"
client_B["IP"] = "167.49.253.253"
client_B["Mask"] = "255.255.192.0"
client_B["routes from"] = "default"
client_B["routes to"] = "167.49.253.254"

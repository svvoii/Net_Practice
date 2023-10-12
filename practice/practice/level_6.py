# Level 6:

# Task description:

# client_A is connected to switch_S and
# switch_S is connected to router_R through interface R1 and
# router_R connected to the internet_I through interface R2

# Goal 1: "interface 'A1' need to communicate with the Internet interface 'Somewhere on the Net'"

# Given network settings parameters:
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

# The following parameters need to be modified to achieve the Goal :
client_A["Mask"] = "255.255.255.128"
client_A["Destination"] = "default" # or 0.0.0.0/0
client_A["Next hop"] = "62.117.76.129"
router_R["interfaces"][0]["IP"] = "62.117.76.129" # technically can be any IP in the range according to mask
router_R["Destination"] = "default"
internet_I["Destination"] = "62.117.76.128/25" # this one should be the destination IP range with netmask for client_A

"""
The main take away from this task is to understand the Routing table
which consists of DESTINATION and NEXT HOP (next router address)
Destination is indicated as IP range according to /25 mask
"""

# Level 5:

# Task description:

# client_A is connected to router_R through interface R1
# client_B is connected to router_R through interface R2

# Goal 1: "'Machine A' need to communicate with 'The Mighty Router'"
# Goal 2: "'Machine B' need to communicate with 'The Mighty Router'"
# Goal 3: "'Machine A' need to communicate with 'Machine B'"

# Given network settings parameters:
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

# Modify the following parameters to achieve the Goal :
client_A["IP"] = "63.157.228.125"
client_A["Mask"] = "255.255.255.128"
client_A["routes from"] = "defaul"
client_A["routes to"] = "63.157.228.126"
client_B["IP"] = "167.49.253.253"
client_B["Mask"] = "255.255.192.0"
client_B["routes from"] = "default"
client_B["routes to"] = "167.49.253.254"

# Routing direftion:
# "routes from": This is set to "default", this means that client_A will send all traffic 
# by default to the gateway specified in "routes to". In this case this is the 
# IP address of router_R's interface R1 (63.157.228.126)
#
# For client_B this set to the IP address of router_R's interface R2 (167.49.253.254)

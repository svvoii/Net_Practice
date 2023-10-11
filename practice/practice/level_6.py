# Level 6:

# Task description:

# client_A is connected to switch_S 
# switch_S is connected to router_R through interface R1 and
# router_R connected to the internet_I through interface R2

# Goal 1: "interface 'A1' need to communicate with interface 'Somewhere on the Net'"

# Given network settings parameters:
client_A = {
    "name": "webserv.non-real.com",
    "interface": "A1",
    "IP": "62.117.76.227",
    "Mask": "",
	"Routes from": "",
	"Routes to": ""
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
	"Routes from": "",
	"Routes to": "163.172.250.1"
}

internet_I = {
	"name": "Internet",
	"interface": "Somewhere on the Net",
	"IP": "8.8.8.8",
	"Mask": "/16",
	"Routes from": "",
	"Routes to": "163.172.250.12"
}

# Modify the following parameters to achieve the Goal :
client_A["Mask"] = ""
client_A["Routes from"] = ""
client_A["Routes to"] = ""
router_R["interfaces"][0]["IP"] = ""
router_R["Routes from"] = ""
internet_I["Routes from"] = ""

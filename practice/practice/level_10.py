# Level 10:

# Network layout / topology:
internet_I = {
	"name": "Internet",
	"routing table": [
		{
			"Destination": "",
			"Next hop": "163.172.250.12"
		},
		{
			"Destination": "",
			"Next hop": ""
		},
		{
			"Destination": "",
			"Next hop": ""
		}
	]
}

router_R1 = {
    "name": "proton",
	"interfaces": [
		{
			"interface": "R11",
			"IP": "",
			"Mask": ""
		},
		{
			"interface": "R12",
			"IP": "",
			"Mask": ""
		},
		{
			"interface": "R13",
			"IP": "",
			"Mask": ""
		}
	],
	"routing table": [
		{
			"Destination": "",
			"Next hop": ""
		},
		{
			"Destination": "",
			"Next hop": ""
		},
		{
			"Destination": "",
			"Next hop": ""
		}
	]
}

router_R2 = {
    "name": "boson",
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
		},
		{
			"interface": "R23",
			"IP": "",
			"Mask": ""
		}
	],
	"Destination": "",
	"Next hop": ""
}

switch_S = {
	"name": "neutron"
}

client_A = {
    "name": "meson",
    "interface": "A1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

client_B = {
    "name": "ion",
    "interface": "B1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

client_C = {
    "name": "cation",
    "interface": "C1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

client_D = {
    "name": "gluon",
    "interface": "D1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

# Topology description:
"""
"""

# Task description:
"""
Goal 1:
Goal 2:
Goal 3:
Goal 4:
Goal 5:
Goal 6:
Goal 7:
"""

# Solution description and approach:
"""
"""

# Paramters to be added:
internet_I["routing table"][0]["Destination"] = ""
internet_I["routing table"][1]["Destination"] = ""
internet_I["routing table"][2]["Destination"] = ""

router_R1["interfaces"][0]["IP"] = ""
router_R1["interfaces"][2]["IP"] = ""
router_R1["interfaces"][2]["Mask"] = ""
router_R1["routing table"][0]["Destination"] = ""
router_R1["routing table"][0]["Next hop"] = ""
router_R1["routing table"][1]["Destination"] = ""

client_A["IP"] = ""
client_A["Mask"] = ""
client_A["Destination"] = ""
client_A["Next hop"] = ""

client_B["IP"] = ""
client_B["Mask"] = ""
client_B["Destination"] = ""
client_B["Next hop"] = ""

router_R2["interfaces"][0]["IP"] = ""
router_R2["interfaces"][1]["IP"] = ""
router_R2["interfaces"][1]["Mask"] = ""
router_R2["interfaces"][2]["IP"] = ""
router_R2["Next hop"] = ""

client_C["IP"] = ""
client_C["Mask"] = ""
client_C["Next hop"] = ""

client_D["IP"] = "17.224.136.215"
client_D["Mask"] = "/18" # given in router_R2 interface R23
client_D["Destination"] = "0.0.0.0/0" # or "default"

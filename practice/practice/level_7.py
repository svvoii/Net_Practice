# Level 7:

# Task description:

# client_A is connected to router_R1's interface R11, router_R1's interface R12 is connected to router_R2's interface R21, client_C is connected to router_R2's interface R22.

# The Goal is to establish communication between client_A and client_C

# Network parametersa as given:
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
			"interface": "R12",
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

"""
The following parameters need to be added to achieve the Goal :
"""
client_A["IP"] = ""
client_A["Mask"] = ""
client_A["Destination"] = ""
client_A["Next hop"] = ""

router_R1["interfaces"][0]["Mask"] = ""
router_R1["interfaces"][1]["Mask"] = ""
router_R1["Destination"] = ""
router_R1["Next hop"] = ""

router_R2["interfaces"][0]["IP"] = ""
router_R2["interfaces"][0]["Mask"] = ""
router_R2["interfaces"][1]["IP"] = ""
router_R2["interfaces"][1]["Mask"] = ""
router_R2["Destination"] = ""
router_R2["Next hop"] = ""

client_C["IP"] = ""
client_C["Mask"] = ""
client_C["Destination"] = ""
client_C["Next hop"] = ""

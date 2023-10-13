# Level 8:

# Network layout / topology:
internet_I = {
	"name": "Internet",
	"Destination": "132.251.9.0/26",
	"Next hop": ""
}

router_R1 = {
    "name": "gate.non-real.com",
	"interfaces": [
		{
			"interface": "R12",
			"IP": "163.114.250.12",
			"Mask": "255.255.255.240"
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
			"Destination": "0.0.0.0/0",
			"Next hop": "163.114.250.1"
		}
	]
}

router_R2 = {
    "name": "transit.my-isp.org",
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
	"Next hop": "132.251.9.62"
}

client_C = {
    "name": "office.non-real.com",
    "interface": "C1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": ""
}

client_D = {
    "name": "home.non-real.com",
    "interface": "D1",
    "IP": "",
    "Mask": "255.255.255.240",
	"Destination": "",
	"Next hop": ""
}
# topology description:


# Task description:

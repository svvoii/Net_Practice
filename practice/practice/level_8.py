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

# Topology description:
"""
router_R1's interface R12 is connected to the internet_I.
router_R1's interface R13 is connected to router_R2's interface R21.

router_R2's interface R22 is connected to client_C's interface C1.
router_R2's interface R23 is connected to client_D's interface D1.
"""

# Task description:
"""
Goal 1: client_C need to communicate with client_D.
Goal 2: client_C need to communicate with the internet_I.
Goal 3: client_D need to communicate with the internet_I.
"""

# Solution description:
"""
Analyzing the task and the given network layout, 
we can focus on routing table and the "destination" parameter 
of the internet_I.
It gives us the idea of the IP address and the mask 
which should cover the subnets of the given network layout.

We can use that IP address (first 3 octets) in all subnets 
and set the proper mask for each subnet.

The mask for each subnet must be higher (/27, /28 ..) 
than the mask given in the internet_I "destination" (/26).

Since the client_D already have the mask (/28 or 255.255.255.240) set 
we can use it in the client_C's subnet as well.
Since routing table of the router_R2 alraday have the "next hop" parameter (132.251.9.62),
which is the IP address of the router_R1's interface R13, we can use it
for router_R1's interface R21 IP but decremented by 1.
The mask for the subnet with interfaces R21 and R13 can be set to (/30 or 255.255.255.252),
which will allow to use only 2 IP addresses in this subnet.

Another important point is to chose proper IP addresses range for each subnet.
Given the subnet mask (\26) we can use up to 4 subnets:
-.-.-.0 - .63	# this has been taken by the subnet with interfaces R21 and R13.
-.-.-.64 - .127
-.-.-.128 - .191
-.-.-.192 - .255
However we can break down the folowing subnets into smaller ones.
client_D's subnet has the mask (/28 or 255.255.255.240) which allows to use 
up to 16 subnets with 14 available IP addresses each. However, we need only 2 IP addresses
and only two subnets. So, we can use the folowing IP addresses range:
-.-.-.1 - .14
-.-.-.17 - .30
and so on.
We can use these for either client_D or client_C. 
Keeping in mind that if we decide to use higher range it should not overlap wit the 
IP addresses used for interfaces R21 and R13 (-.-.-.62 and -.-.-.61).
so the range (-.-.-49 - .62) is not suitable for client_D's nor client_C's subnets.

Another point to remember that if any subnet need to communicate with the internet_I,
some, specific Network addresses can not be used.
For example these are reserved for Private Networks, and should be avoided:
10.0.0.0
172.16.0.0
192.168.0.0

'Pay attention since, these are used in this task by default'.
"""

# Paramters to be added:
internet_I["Next hop"] = "163.114.250.254"

router_R1["interfaces"][1]["IP"] = "132.251.9.62" # given in router_R2's routing table
router_R1["interfaces"][1]["Mask"] = "255.255.255.252" # or "/30"
router_R1["routing table"][0]["Destination"] = "0.0.0.0/0" # or "default"
router_R1["routing table"][0]["Next hop"] = "132.251.9.61"

router_R2["interfaces"][0]["IP"] = "132.251.9.61"
router_R2["interfaces"][0]["Mask"] =  "255.255.255.252" # or "/30"
router_R2["interfaces"][1]["IP"] = "132.251.9.17" # client_C's subnet
router_R2["interfaces"][1]["Mask"] = "255.255.255.240" # or "/28
router_R2["interfaces"][2]["IP"] = "132.251.9.1" # client_D's subnet
router_R2["interfaces"][2]["Mask"] = "255.255.255.240" # or "/28" - given in client_D
router_R2["Destination"] = "0.0.0.0/0" # or "default"

client_C["IP"] = "132.251.9.18"
client_C["Mask"] = "255.255.255.240" # or "/28"
client_C["Destination"] = "0.0.0.0/0" # or "default"
client_C["Next hop"] =  "132.251.9.17"

client_D["IP"] = "132.251.9.2"
client_D["Destination"] = "255.255.255.240" # or "/28"
client_D["Next hop"] = "132.251.9.1"

# Level 9:

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
			"Next hop": "163.172.250.12"
		},
		{
			"Destination": "",
			"Next hop": "163.172.250.12"
		}
	]
}

router_R1 = {
    "name": "proton",
	"interfaces": [
		{
			"interface": "R11",
			"IP": "",
			"Mask": "255.255.255.128"
		},
		{
			"interface": "R12",
			"IP": "163.172.250.12",
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
			"Destination": "",
			"Next hop": ""
		},
		{
			"Destination": "0.0.0.0/0",
			"Next hop": "163.172.250.1"
		}
	]
}

router_R2 = {
    "name": "boson",
	"interfaces": [
		{
			"interface": "R21",
			"IP": "",
			"Mask": "255.255.255.252"
		},
		{
			"interface": "R22",
			"IP": "",
			"Mask": ""
		},
		{
			"interface": "R23",
			"IP": "",
			"Mask": "/18"
		}
	],
	"Destination": "0.0.0.0/0",
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
	"Destination": "0.0.0.0/0",
	"Next hop": ""
}

client_D = {
    "name": "gluon",
    "interface": "D1",
    "IP": "",
    "Mask": "",
	"Destination": "",
	"Next hop": "17.224.136.214"
}

# Topology description:
"""
client_A's interface A1 connected to client_B's interface B1 through switch_S;

router_R1's interface R11 is connected to client_A's interface A1
sa well as client_B's interface B1 through switch_S;
router_R1's interface R12 is connected to the internet_I;
router_R1's interface R13 is connected to router_R2's interface R21;

router_R2's interface R22 is connected to client_C's interface C1;
router_R2's interface R23 is connected to client_D's interface D1;
"""

# Task description:
"""
Goal 1: client_A "messon" need to communicate with client_B "ion";
Goal 2: client_C "cation" need to communicate with client_D "gluon";
Goal 3: client_A "messon" need to communicate with the internet_I;
Goal 4: client_A "messon" need to communicate with client_D "gluon";
Goal 5: client_B "ion" need to communicate with client_C "cation";
Goal 6: client_C "cation" need to communicate with the internet_I;
"""

# Solution description and approach:
"""
This task is a bit more complicated than the previous ones.
The network layout / topology has more devices and one more subnet to handle.
There are more fields to be filled in.
Both routing tables for the router_R1 and internet_I have more fields to handle.
To understand how to fill in the internet_I's routing table, one approach would be 
to identify the number of subnets to handle.

In this task there are 4 subnets (exccept connection to Internet, R12) 
with the folowing interfaces in each subnet:
subnet 1: A1, B1, R11
subnet 2: R13, R21
subnet 3: R22, C1
subnet 4: R23, D1

Breaking down the approach to handle each subnet:
subnet 1: A1, B1, R11 - there is no fixed IP address given in this subnet.
So, we can choose arbitrary IP's, avoiding the IP's from the reserved range.
There is mask given in R11 interface, so we can distribute it accordingly.

subnet 2: R13, R21 - there is no fixed IP address given in this subnet either.
The mask is given in R21 interface, so we can copy it to R13.
Current mask allows to use only 2 IP addresses in this subnet.
So, we might use the end of the available range, which also corresponds 
to the Network address's last (4th) octet (-.-.-.253, 254).

subnet 3: R22, C1 - there is no fixed IP address not mask in this subnet either.
We might play around with the IP addresses and masks in this subnet.
Keeping in mind that chosen subnet mask should handle at least 4 subnets.

subnet 4: R23, D1 - here we can find the fixed IP address and mask.
So, just arranging the IPs and mask accordingly.

Once this is done, we can fill in the internet_I's routing table, where
we need to use the Network address of each subnet as the "destination", and
subnet mask shall be set accordingly. Usually it is 1 level higher than the mask
used in the subnet. For example, if the subnet mask is /25, 
the mask in the routing table shall be /24.

The routing table of the router_R1 is more straight forward. 
We already have the "next hop" parameter for to route the traffic 
from client_C and client_D to the internet_I. So we just need to fill in
the "Next hop" to drive the trafic to the respective clients.
The destination can be set to "default".
There is no need to fill in the entire table here. 
2 entries which drive the trafic both ways would be sufficient. 

For debugging we still can use the log table in the right bottom corner.
Even if it might be confusing some times, it still provides some useful information.

Another approach would be to follow each Goal from top to bottom 
and fill in the parameters accordingly.
"""

# Paramters to be added:
internet_I["routing table"][0]["Destination"] = "92.168.203.0/24"
internet_I["routing table"][1]["Destination"] = "9.0.0.128/25"
internet_I["routing table"][2]["Destination"] = "0.0.0.0/0" # or "default"

router_R1["interfaces"][0]["IP"] = "92.168.203.1" # given
router_R1["interfaces"][2]["IP"] = "89.254.16.254"
router_R1["interfaces"][2]["Mask"] = "255.255.255.252" # given in router_R2 interface R21
router_R1["routing table"][0]["Destination"] = "default"
router_R1["routing table"][0]["Next hop"] = "89.254.16.253" # drives trafic towards clients C and D
router_R1["routing table"][1]["Destination"] = "" # not necessary to fill in

client_A["IP"] = "92.168.203.2"
client_A["Mask"] = "255.255.255.128" # given in router_R1 interface R11
client_A["Destination"] = "0.0.0.0/0" # or "default"
client_A["Next hop"] = "92.168.203.1"

client_B["IP"] = "92.168.203.3"
client_B["Mask"] = "255.255.255.128" # given in router_R1 interface R11
client_B["Destination"] = "0.0.0.0/0" # or "default"
client_B["Next hop"] = "92.168.203.1"

router_R2["interfaces"][0]["IP"] = "89.254.16.253"
router_R2["interfaces"][1]["IP"] = "9.0.0.253"
router_R2["interfaces"][1]["Mask"] = "255.255.255.252" # given
router_R2["interfaces"][2]["IP"] = "17.224.136.214" # given in client_D as next hop
router_R2["Next hop"] = "89.254.16.254"

client_C["IP"] = "9.0.0.254"
client_C["Mask"] = "255.255.255.192"
client_C["Next hop"] = "9.0.0.253"

client_D["IP"] = "17.224.136.215"
client_D["Mask"] = "/18" # given in router_R2 interface R23
client_D["Destination"] = "0.0.0.0/0" # or "default"

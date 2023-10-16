# Level 10:

# Network layout / topology:
internet_I = {
	"name": "Internet",
	"routing table": [
		{
			"Destination": "",
			"Next hop": "163.172.250.12"
		},
	]
}

router_R1 = {
    "name": "Router one",
	"interfaces": [
		{
			"interface": "R11",
			"IP": "142.239.111.1",
			"Mask": "255.255.255.128"
		},
		{
			"interface": "R12",
			"IP": "163.172.250.12",
			"Mask": "255.255.255.240"
		},
		{
			"interface": "R13",
			"IP": "142.239.111.254",
			"Mask": ""
		}
	],
	"routing table": [
		{
			"Destination": "",
			"Next hop": "142.239.111.253"
		},
		{
			"Destination": "142.239.111.128/26",
			"Next hop": "142.239.111.253"
		},
		{
			"Destination": "0.0.0.0/0",
			"Next hop": "163.172.250.1"
		}
	]
}

router_R2 = {
    "name": "Router two",
	"interfaces": [
		{
			"interface": "R21",
			"IP": "142.239.111.253",
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
			"Mask": ""
		}
	],
	"Destination": "0.0.0.0/0",
	"Next hop": "142.239.111.254"
}

switch_S1 = {
	"name": "Switch one",
}

client_H1 = {
    "name": "Host one",
    "interface": "H11",
    "IP": "142.239.111.2",
    "Mask": "",
	"Destination": "0.0.0.0/0",
	"Next hop": "142.239.111.1"
}

client_H2 = {
    "name": "Host two",
    "interface": "H21",
    "IP": "",
    "Mask": "",
	"Destination": "0.0.0.0/0",
	"Next hop": "142.239.111.1"
}

client_H3 = {
    "name": "Host three",
    "interface": "H31",
    "IP": "",
    "Mask": "",
	"Destination": "0.0.0.0/0",
	"Next hop": ""
}

client_H4 = {
    "name": "Host four",
    "interface": "H41",
    "IP": "142.239.111.131",
    "Mask": "255.255.255.192",
	"Destination": "default",
	"Next hop": "142.239.111.129"
}

# Topology description:
"""
Host one is connected to Host two through Switch one.
Host one and Host two are connected to router_R1's interface R11 through Switch one.
router_R1's interface R12 is connected to the Internet.
router_R1's interface R13 is connected to router_R2's interface R21.
Host three is connected to router_R2's interface R22.
Host four is connected to router_R2's interface R23.
"""

# Task description:
"""
Goal 1: Host one need to communicate with Host two.
Goal 2: Host three need to communicate with Host four.
Goal 3: Host one need to communicate with the Internet.
Goal 4: Host one need to communicate with Host four.
Goal 5: Host two need to communicate with Host three.
Goal 6: Host three need to communicate with the Internet.
Goal 7: Host four need to communicate with the Internet.
"""

# Solution description and approach:
"""
The approach for this level is similar to level 9.
We firt analyze the network topology and fill in the missing parameters in each subnet.

There are 4 subnets to handle (exccept the Internet - R12). We dont need to handle that exccept the "Destination" parameter in the routing table.
Destination in this case must be network address and the mask which covers all 4 subnets.

Subnet 1: R11, H11, H21
Subnet 2: R13, R21
Subnet 3: R23, H42
Subnet 4: R22, H31

Subnet 1 (R11, H11, H21):
	The IP and mask are already provided for H11 as well as H11. So, we can assign the next increment of IP to H21.
	The mask is specified on R11, so we just copy paste.

Subnet 2 (R13, R21):
	The IP and mask are already specified on R21 and IP on R13. We just copy the same mask from R21 to R13.

Subnet 3:
	IP and mask already specified on H41. So, we assign decremented IP to R23 and copy the mask.

Subnet 4 (R22, H31)):
	No IPs or masks specified. This is where the error can be made. We need to pick IP range which will not overlap with other subnetworks.
	Since we have only 2 interfaces in this subnet, for simplicity, we can use same mask same as in R21 - R13 (subnet 2): "/30" or "255.255.255.252".
	In this case we need to pick IP range which will n't overlap with other subnetworks. So, we can chose the previous available range from subnet 2.
	"142.239.111.249" and "142.239.111.250".

As for the routing table of router_R1, we need to add one destination (network address and assosiated mask) to point traffic to Subnet 4 (R22 - H31).

Another important pioint regarding Subnet 4 (R22 - H31) is that there is limited number of IP addresses available for hosts.
Given the destination parameter in router_R1's routing table (142.239.111.128/26) we cannot use the same mask in Subnet 4
as used in Subnet 3 (255.255.255.192).
"142.239.111.128/26" limits the available host IPs (-.-.-.129 - .254)
(-.-.-.129 - .190) range is used in Subnet 3 with mask "/26" (255.255.255.192)
we wont be able to use (-.-.-.193 - .254) range in Subnet 4 with the same mask "/26" (255.255.255.192)
since the Subnet 2 (R13 - R21) is using fixed IPs "-.-.-.253 - 254" (mask "/30") which overlap.
So, it is necessary to use different mask in Subnet 4 (R22 - H31) to avoid the overlap. 
(/27, /28, /29, /30) any of these masks with the respective range will do.
For simplisity we can use the same mask as in Subnet 2 (R13 - R21) "/30" with IPs just the previous range of available 2 IPs.
("142.239.111.249" and "142.239.111.250")

To sum up, the key things in this task are:

Pick appropriate subnet masks and IP range for Subnet 4 (R22 - H31).
Set routes to direct traffic between the subnets and Internet. The destination in the Internet's routing table should cover all 4 subnets.
The destination in router_R1's routing table should target specificaly the Subnet 4 (R22 - H31).
"""

# Paramters to be added:
internet_I["routing table"][0]["Destination"] = "142.239.111.0/24" # this should cover all the IP's in all given subnetworks

router_R1["interfaces"][2]["Mask"] = "255.255.255.252" # or "30", given in router_R2's R21 interface
router_R1["routing table"][0]["Destination"] = "142.239.111.248/30" # this one might be tricky, it has to match the network IP of R22 and H31

client_H11["Mask"] = "255.255.255.128" # or "/25", given in router_R1's R11 interface

client_H21["IP"] = "142.239.111.3" # based on the IP's given in its subnet
client_H21["Mask"] = "255.255.255.128" # or "/25", given in router_R1's R11 interface

router_R2["interfaces"][1]["IP"] = "142.239.111.249" # not much of the choice here, the network part should be the same as in all other sunetworks
router_R2["interfaces"][1]["Mask"] = "255.255.255.252" # picked for simplicity, same as in R21 - R13 subnet
router_R2["interfaces"][2]["IP"] = "142.239.111.129" # this should align with the IP given to H41
router_R2["interfaces"][2]["Mask"] = "255.255.255.192" # or "/26", given in H41's interface 

client_H31["IP"] = "142.239.111.250" # (see comment in R22 "142.239.111.249") the host part is previous available range compared to R21 - R13 subnet
client_H31["Mask"] = "255.255.255.252" # picked for simplicity, same as in R21 - R13 subnet
client_H31["Next hop"] = "142.239.111.249" # R22

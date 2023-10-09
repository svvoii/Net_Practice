# Level 2:

# Task description:
#
# client_A directly connected to client_B.
#
# Goal 1: "Computer B" needs to communicate with "Computer A"
# client_A "Mask" CANNOT be modified
# client_A "IP" can be modified
# client_B "Mask" can be modified
# client_B "IP" CANNOT be modified

# Given network settings parameters:
client_A = {
    "name": "Computer A",
    "interface": "A1",
    "IP": "", # can modify
    "Mask": "255.255.255.224" # NOT modifiable
}

client_B = {
    "name": "Computer B",
    "interface": "B1",
    "IP": "192.168.28.222", # NOT modifiable
    "Mask": "" # can modify
}

# Modify the following parameters to achieve the Gial 1:
client_A["IP"] = "192.168.28.193" # the IP range can be from 193 to 221 given the Mask
client_B["Mask"] = "255.255.255.224" # should bethe same as client_A mask, which is NOT modifiable

################################################################

# Task description:
#
# client_C directly connected to client_D.
#
# Goal 2: "Computer D" needs to communicate with "Computer C"
# client_C "Mask" CANNOT be modified
# client_C "IP" can be modified
# client_D "Mask" CANNOT be modified
# client_D "IP" can be modified

# Given network settings parameters:
client_C = {
    "name": "Computer C",
    "interface": "C1",
    "IP": "", # can modify
    "Mask": "255.255.255.252" # NOT modifiable
}

client_D = {
    "name": "Computer D",
    "interface": "D1",
    "IP": "", # can modify
    "Mask": "/30" # NOT modifiable
}

# Modify the following parameters to achieve the Gial 2:
client_C["IP"] = "192.168.0.1"
client_D["IP"] = "192.168.0.2"

# Calculate the network and broadcast address for client_C
client_C_network = client_C["IP"] & client_C["Mask"]
client_C_broadcast = client_C_network | (~client_C["Mask"])

# Calculating valid IP range for client_C
client_C_valid_range = [client_C_network + 1, client_C_broadcast - 1]

# Calculate the network and broadcast addresses for client_D
client_D_network = client_D["IP"] & client_D["Mask"]
client_D_broadcast = client_D_network | (~client_D["Mask"])

# Calculate the valid range for client_D
client_D_valid_range = [client_D_network + 1, client_D_broadcast - 1]

print("Valid Range for Computer C:", client_C_valid_range)
print("Valid Range for Computer D:", client_D_valid_range)

"""
Subnetting is the process of dividing a network into smaller subnetworks 
or subnets to efficiently utilize IP addresses and manage network traffic.
Each subnet has its own range of IP addresses and a subnet mask that 
determines the network and host portions of an IP address.

In the given scenario, the client_C and client_D are connected directly, 
and we need to modify their IP addresses to enable communication between them.
The subnet mask for both clients is "255.255.255.252", 
which means there are only 2 usable host IP addresses in the subnet.

To calculate the valid range within this subnet, 
we need to consider the network and broadcast addresses. 
The network address is the first IP address in the subnet, 
and the broadcast address is the last IP address.

In a /30 subnet, the formula to calculate the valid range is: 
Valid Range = Network Address + 1, Network Address + 2, ..., Broadcast Address - 1

To calculate the network address, we perform a bitwise logical AND operation 
between the IP address and the subnet mask. 
For example: client_C network address = client_C IP & client_C subnet mask 
client_D network address = client_D IP & client_D subnet mask

To calculate the broadcast address, we perform the bitwise logical OR operation 
between the network address and the inverse of the subnet mask. 
For example: client_C broadcast address = client_C network address | (client_C subnet mask) 
client_D broadcast address = client_D network address | (client_D subnet mask)

Once we have the network address and broadcast address, 
we can determine the valid range of IP addresses for each client.

---
### To calculate the valid range without knowing the specific IP addresses, 
# we can leverage the nature of a /30 subnet. In a /30 subnet, 
# there are only 4 possible IP addresses: the network address, 
# the broadcast address, and two usable host addresses. 
# These host addresses will be the valid IP range within the subnet.

subnet_mask = "255.255.255.252"

# Step 1: Convert the subnet mask to binary representation
subnet_mask_binary = ''.join([bin(int(x))[2:].zfill(8) for x in subnet_mask.split('.')])
# subnet_mask_binary will be "11111111111111111111111111111100"

# Step 2: Count the number of host bits
host_bits_count = subnet_mask_binary.count('0')
# host_bits_count will be 2

# Step 3: Calculate the number of possible hosts
possible_hosts = 2 ** host_bits_count
# possible_hosts will be 4

# Step 4: Calculate the valid IP range
# Choose the network address arbitrarily
network_address = "192.168.4.0"
network_address_binary = ''.join([bin(int(x))[2:].zfill(8) for x in network_address.split('.')])
# network_address_binary will be "11000000101010000000010000000000"

# Determine the first and last IP addresses in the valid range
first_ip_address = int(network_address_binary, 2) + 1
last_ip_address = first_ip_address + possible_hosts - 2

# Convert the first and last IP addresses back to dotted-decimal notation
first_ip_address_decimal = '.'.join([str((first_ip_address >> (3 - i) * 8) & 255) for i in range(4)])
last_ip_address_decimal = '.'.join([str((last_ip_address >> (3 - i) * 8) & 255) for i in range(4)])

# Print the valid IP range
print("Valid Range:", first_ip_address_decimal, "-", last_ip_address_decimal)

"""

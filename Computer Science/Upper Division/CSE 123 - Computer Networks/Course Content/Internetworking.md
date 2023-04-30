Problem: Not all networks are directly connected. 
- the concept of interconnecting different types of networks to build a large, global one is *internetworking*

# Switching Basics
A switch is a mechanism that allows us to interconnect links to form a larger network.
- multi-input, multi-output
- "star topology" allows for scaling:
	- large numbers of switches can interconnect with each other, exponentially increasing the multi-input/output capacity
	- adding a new host to the network by connecting to a switch doesn't necessarily reduce performance of the network for other connected hosts
- runs appropriate data link protocol to allow communication
- in order to decide which output to send a packet on, switches usually look at the header of the packet which provides that information
- in order to identify ports within a switch we can either:
	- number each port
	- identify the port by the name of the node to which it leads

## Datagrams
Main idea: include just enough information in every packet to enable any switch to decide how to get to its destination.
- a switch will consult a forwarding/routing table to decide where to send a packet.
- hosts can send packets anywhere at any time, since packets at switches can be immediately forwarded.
	- called *connectionless* for this reason, since connections don't need to be established before sending.
- when a host sends a packet, it has no way of knowing whether the network can deliver it or if the destination host is even up and running.
- each packet is forwarded independently of previous packets.
	- i.e. two successibe packets from host A to B may follow completely different paths.
- a switch or link failure may not have any serious effect on communication if it is possible to find an alternate route around the failure and update the forwarding table

## Virtual Circuit Switching
Alternate idea: Use a *connection-oriented* model, which sets up a virtual connection from the source to destination before any data is sent.


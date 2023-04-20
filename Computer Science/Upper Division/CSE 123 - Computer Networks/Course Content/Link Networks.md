Hubs / Repeaters
- any host can talk to any other host
- physical layer device
- one "port" per LAN
- "repeat" received bits on one port out to *all* other ports
- "daisy chain"

Hub advantages
- hubs can be arranged into hierarchies
- most of lan continues to operate if "leaf" hub dies
- simple, cheap
- "backbone hub" to connect to other hubs

Hub problem: still one big shared bus
- single collision domain: no imporvement in max throughput as you add more links
- still limited in distance and number of hosts
	- collision detection requirements
	- synchronization requirements
- requires link technology homogeneity
	- can't connect both 1 Gbps and 100 Mbps devices to the network

## Bridges
- "store and forward" device
	- data-link layer device
	- buffers entire packet and *then* rebroadcasts it on other ports
	- regenerates transmission so network can be longer distance
- creates *separate* collision domains!
	- senses line for access to each LAN (acts like a host)
	- can accommodate different speed interfaces
	- improves throughput
- not all frames go *everywhere*.

"Selective Forwarding"

Switched Ethernet
- hosts **directly connected to a bridge**
	- learning + spanning tree protocol
- switch supports parallel forawrding
	- A to B and A' to B' simultaneously
- non-blocking!
- no sharing of links!
- but expensive. but we did it

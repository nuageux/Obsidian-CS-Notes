Problem
- Communication is hella complicated
- It's a bunch of problems
- abstraction & modularity is the solution
- layering is the modularity
- abstraction is the protocol / standardization

Layering, a Modular Approach
- subproblem to solve to benefit from layers below that are solving other problems yet provide benefits to layers above (since we solved a piece of the puzzle)
- interface among peers in a layer is called a protocol
	- agreement about how we're gonna exchange information, "speak the same language". ex: big and little endian
- changing a layer won't affect a lower layer. sometimes it may affect an upper layer (minimally)

key design decision
- what functionality to put in each layer? how to divide functionality
- end-to-end argument
	- functionality should be implemented in a lower layer if it can be implemented completely and correctly there
	- dont rely on a lower layer unless it can do it perfectly for me
	- functionality can also be implemented in a lower layer incompletely if it boosts performance. It may be incorrect!
- app won't be reliable if even one layer does something dumb
- reliability is never complete and correct in ANY layer. we can never fully trust all layers. so we have to reimplement reliability also at higher levels
- ex: if a webpage doesnt load (transport layer), we must try to solve the reliability problem at the upper application layer by refreshing the page

protocol standardization
- standardize what is said
- not very technical, we just made a task force for it. super political
- written in a text file with ascii art!
- request for comments (RFCs), eventually promoted to Internet Standards
- internet engineering task force

tcp / ip protocol stack
- the most common system stack used
- each protocol solves one problem
- some layers are implemented in hosts (computers) and some are implemented in routers. some are implemented redundantly.
	- IP must be implemented like everywhere
- application layer for http to download webpages
- transport layer (TCP) provides reliable and in order delivery of bytes from one computer to another. other layers dont do that
- network layer gets a message from one network to another
- link layer (physical layer), the thing that delivers bits from one computer to another.

layering enabled growth
- hourglass model, "thin waist"
	- IP is the thin waist in question
- lets us change things at another layer and let that layer evolve and grow to match needs of humans
- but IP stays the same, in fact since like the 60's. we can change every other layer!

layer context encapsulated in packets via headers
- original message to send! passes thru the code at each layer, each layer adds some bytes to the header.
- there is some overhead, a cost.

link layer
- signal encoding to physical signals
- also decodes back to binary data
- media access
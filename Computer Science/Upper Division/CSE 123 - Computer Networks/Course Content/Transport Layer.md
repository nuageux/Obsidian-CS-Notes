summary
- link layer is lossy
	- has possibility of corruption, which are deliberately thrown away at the link layer
	- link speed is a bottleneck, which might drop frames
	- links can lose, corrupt, reorder, etc, but all of these events are called losses
- provides abstractions of reliable, in order delivery

reliable transmission
- packet (instead of frame) based version of reliability
- can only do reliability on the end hosts themselves
- two options
	- detect loss/corruption and retransmit
		- this is better bc its more efficient, since errors are rare.
	- send data redundantly to tolerate loss/corruption

## ARQ
- "Automatic Repeat reQuest"
- receiver sends acknowledgments (ACK)
	- sender "times out" and retransmits if they don't get this ACK.
- **timeouts are fundamental to networking**
	- *only* way to figure out if something did or didn't do something
- how to avoid duplicates?
	- with sequence numbers
- the simplest ARQ protocol is "stop and wait", to only allow one outstanding frame at a time.
- lousy performance if time to send 1 packet is << propagation delay
	- want to utilize bandwidth completely.
	- called bandwidth-delay product (BDP)
		- really hard to estimate. timeouts are also hard to calculate
	- limited by accuracy of timeout

## Pipelined Transmission
- keep multiple packets "in flight"
	- sender makes efficient use of link
- sender buffers outstanding un-ACK'd packets in case it has to retransmit these packets.
	- ACKs are cumulative and covers the current frame and all previous packets
		- the last sent ACK tells us the largest packet send reliably.
	- this assumes packets must be received in order

#### Go-Back-*N*
- Retransmit all packets from point of loss
- Packets sent after the lost packet/ACK are ignored.
- Simple to implement, receiver no longer has to buffer anything
- Leads to sending potentially a lot of duplicates

# Sliding Window
- Mechanism that supports
	- multiple outstanding packets
	- reliable delivery
	- in order dlivery
	- flow control
- sender and receiver maintain their own "windows" to track outstanding packets
	- at the core of all modern ARQ protocols
- Go-Back-*N* has a receive window size of 1.

### Send Window
- Its size limits outstanding packets we can send.
	- size is limited in order to limit amount of memory waste
		- don't need to remember all packets ever sent
- Window "moves forward" upon receipt of *new* ACK
- Window "goes back" to beginning upon a timeout
- Use repeated ACKs to notice that frames must be retransmitted BEFORE the timeout (which kills efficiency, inherent to waiting)
- ACKs give a hint about RTT
- can be proactive if we get these hints:
	- negative ACKs
	- Fast retransmit (retransmit right away)
		- incidentally, modern TCP does this if 3 repeated ACKs

## Host-based Congestion Control
- one of biggest unsolved problems in CS
- how fast should a host send data? don't cause congestion
	- shouldn't be faster than the sender's share of bandwidth
	- shouldn't be faster than the network can process
- related to bandwidth allocation

Congestion occurs at routers
- have some memory in the router to absorb bursts  of packets into a buffer
- but if sending rate is persistently is > drain rate, the queue builds up
	- i.e. buffers only help *temporary* input rate > output rates.
	- buffers inherently increase latency! the lesson is that buffers aren't for free.
		- "drop-tail queuing problem": increasing network load increases throughput until a bottleneck, then exponentially increases latency, then there is loss due to congestion leading to a congestion collapse(!!)
- dropped packets represent wasted work; goodput < throughput

so congestion control is when an increase in network load produces a decrease in useful work. happens cos'
- sneder sends faster than bottleneck link speed
- packets queue up until they are dropped
- in response to dropped packets, sender retransmits
- all hosts repeat this in steady state

solutions?
- increase network resources
	- more buffers for queuing (but led to "bufferbloat")
	- increase link speed
- **reduce network load**
	- send data more slowly... but how much more slowly? when to slow down?

## Control Schemes
- how?
	- open loop
		- explicity reserve bandwidth in the network in advance
		- isn't logistically doable, since reservation systems aren't scalable
	- closed loop
		- respond to feedback and adjust bandwidth allocation
- Where?
	- network-based
		- network imlpements and enforces bandwidth allocation
		- bad approach; its telling routers to get overwhelmed and just deal with it. 
	- host-based
		- hosts are resonsible for controlling their sending rate
		- better, just tell hosts to shut up for a bit. reduce complexity, don't introduce more

We want to do congestion avoidance:
- try to stay to the left of the "knee", where we stop getting large benefits in throughput. this is proactive
- congestion control is trying to stay to the left of the "cliff", riiiight before the loss begins and heads to literal congestion collapse

challenges:
- how to even detect congestion? it must be inferred!
	- explicit congestion signalling
		- source quench: ICMP message from router to sender
		- DECBit / Explicit Congestion Notification (ECN)
			- router marks packet based on queue occupancy, which should indicate that the packet encountered congestion along the way
			- receiver tells sender if queues are getting too full
			- problem, easily exploitable and annoying to implement
	- implicit 
		- packet loss
			- assume congestion is primary source of packet loss
			- lost packets indicate congestion
		- packet delay
			- rtt increases as packets queue
			- realize packet inter-arrival time is a function of bottleneck link
- how to limit sending data rate?
- how fast to send?

throttling options
- sender window-based (TCP)
	- constrain number of outstanding packets allowed in network. send more or send less.
	- increase window size to send more/faster, decrease to send less/slower
	- pro: cheap to implement since we already have windowing, good failure properties
	- creates traffic bursts (requires bigger buffers)
- rate-based (streaming media protocols, usually)
	- two params, period and packets
	- allow sending of x packets in period y
	- pro: smooth traffic
	- con: fine-grained per-connection times, what if receiver fails?

choosing a send rate
- ideally keep equilibirum at the "knee"
	- find it somehow...
	- keep number of packets "in flight" the same
	- don't send a new packet into the network until you know one has left
	- ...what if you guess wrong, or if bandwidth availabiltiy changes?
- compromise: adaptive approciximation
	- if congestion is signalled, reduce sending rate by x
	- if data delivered successfully, increase sending rate by y
	- how to relate x and y? most choices dont converge...

tcp's probing approach
- each source independently probes the network to determine how much bandwidth is available
	- changes over time, since everyone does this
- assume that packet loss implies congestion
	- since errors are rare; also, requires no support from routers!
- window-based congestion control
	- unified congestion conrtol and flow control mechanism
	- rwin: advertised flow control window from receiver
	- cwnd: congestion control window
		- estimate of how much outstanding data network can deliver in a rtt
	- sender can only send min(rwin, cwnd) at any time
- idea: decrease cwnd when congestion is encountered, increase cwnd otherwise. ...how much to adjust?
	- adapt to changes in available bandwidth
	- additive increase, multiplicative decrease (AIMD)
		- increase sending rate by a constant (e.g. TCP MSS)
		- decrease sending rate by a linear factor (e.g. divide by 2)
	- why this works?
		- if $L_i$ is the queue length at time $i$
		- in steady state: $L_i = N$, where $N$ is a constant
		- during congestion, $L_i = N + yL_{i-1}$, where $y > 0$
		- consequence is queue size increases multiplicatively
			- so we must reduce sending rate multiplicatively as well
- what should the initial TCP flow be? has to cover 6+ orders of magnitude... e.g. 10k to 10Gbps
	- starting too fast is catastrophic!

### Slow Start
Goal: quickly find the equilibrium sending rate
- quickly increase sending rate until congestion detected
	- remember last rate that worked and don't overshoot it
- TCP Reno Algorithm
	- on new connection, or after timeout, set cwnd = 1 MSS
	- for each segment ack'd incremend cwnd by 1 MSS (double it...(?))
	- if timeout then divide cwnd by 2, and set ssthresh = cwnd
	- if cwnd >= ssthresh then exit slow start
- why called slow if its exponential?

fast retransmit
- already covered, use 3 duplicate acks to indicate a loss and just resend immediately
fast recovery
- avoid stalling after loss
- if there are still acks coming in, don't slow start!
- if a packet has made it through, we can send another one
- divide cwnd by 2 after a fast retransmit
- incremend cwnd by 1 MSS for each additional duplicate ACK

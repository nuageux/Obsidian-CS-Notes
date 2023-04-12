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
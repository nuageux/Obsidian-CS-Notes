- How do systems behave in the presence of an adversary?
	- i.e. an intelligence that actively tries to cause a system to misbehave.
- Security and Safety are different. 
	- Safety is design without the presence of an adversary.
		- Inherent to engineering.
	- Nature is *not* an adversary, because it doesn't have intent.
- A common approach to security is a cycle of attack and defense.
	- An attack is a set of steps that leverage the vulnerability to cause an assault on a system.
	- We study attacks in order to:
		- create incentives for vendors to be careful
		- identify vulnerabilities
		- learn about new classes of threats
		- determine what to defend against
		- help developers create stronger systems
		- help users more accurately evaluate risk
- Everything can be compromised. There is no such thing as complete security, only degrees of security.

### "CIA" Properties
- Confidentiality
	- It is the protection of info from being accessed by unauthorized parties.
	- Once confidentiality is breached, it cannot be undone.
- Integrity
	- The protection of information from being altered by unauthorized parties.
- Availability
	- The maintenance of accessability of information to authorized users.
	- Prevent users from being locked out!

## The Security Mindset
- Always be on the lookout for weakest links.
- Identify the assumptions that security depends on. Are they false?
- See the world for what it is, not what others tell you it is.
- "Rational Paranoia"!

### Thinking as a Defender
- Security Policy
- Threat Model and Risk Assessment
	- The Threat Model is a set of assumptions about the attacks that a security system is trying to protect against.
	- Important to consider before starting work on a defense.
	- Must be straightforward and reasonable.
- Countermeasures
	- Cost vs. Benefit involved in these countermeasures

### Where to Focus Defenses
- Trusted Components
- Attack Surface
	- The parts of the system exposed to the attacker
- Reduction of Complexity and Obscurity
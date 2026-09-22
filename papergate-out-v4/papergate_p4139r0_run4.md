Verdict: Weak (2/14)

The paper offers only scattered assertions in favor of its own standardization, and even those are largely framed as observations rather than evidence. The thinnest areas are the complete absence of any identified affected users, implementation experience, or argument for why a library solution would not suffice, leaving the standardization case largely unbuilt.

- The strongest support is the observation that the proposed operation would differ meaningfully from existing `get()` functions by potentially failing and looping, which at least gestures toward a library-design problem.
- The paper mentions that an alternative name was considered and rejected, but it does not establish what was learned from that prior discussion or how it informs the current proposal.
- The paper explicitly declines to advocate for a concrete design choice, which weakens any claim that the standard library specifically needs this facility.
- The most glaring omission is that the paper never identifies who is affected by the current state of affairs or demonstrates that existing library mechanisms cannot address the need.

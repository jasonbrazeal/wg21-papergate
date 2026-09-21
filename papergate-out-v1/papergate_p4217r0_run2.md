Verdict: Adequate (4/14, close to Weak)

The paper offers only a narrow, repeated rationale for standardizing zero-argument `when_all`, and it does not build a broader case by addressing affected users, alternatives, implementation experience, or why a library solution would be insufficient. The support is thinnest where the paper asserts equivalence to `just()` and the generic-algorithm benefit without evidence or examples.

- The strongest support is the specific claim that banning `when_all()` creates a special case in generic algorithms, though even this is asserted rather than demonstrated.
- The paper asserts that zero senders trivially complete and that `when_all()` is equivalent to `just()`, but it provides no supporting argument or precedent.
- The paper does not address who is affected by the current restriction or what practical code would benefit from the change.
- The most glaring omission is the absence of any implementation experience, coordination discussion, or explanation of why a library-level workaround would not suffice.

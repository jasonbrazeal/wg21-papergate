Verdict: Adequate (7/14, close to Strong)

The paper offers only a narrow, repeated justification for changing the status quo, and it does not build a broader case for standardization through affected users, implementation experience, or coordination with the wider ecosystem. The strongest support is the specific logical argument that an empty `when_all()` is naturally equivalent to `just()`, but nearly every other category rests on the same single assertion about generic algorithms.

- The paper gives a concrete, reasoned equivalence between `when_all()` with zero senders and `just()`, which directly supports the core technical change.
- The claim that banning empty `when_all()` creates an unnecessary special case in generic algorithms is plausible but is asserted rather than demonstrated with examples or affected code.
- The paper does not address implementation experience, leaving the practical viability and consequences of the change unexamined.
- The most glaring omission is any discussion of who is affected, so the proposal never establishes the scope of the problem or the audience for the change.

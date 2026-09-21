Verdict: Adequate (7/14, close to Strong)

The paper gives a partial account of why changing the return type of `address` to `void*` would resolve the NB comment, but it does not build a complete case for standardization. The strongest material concerns alternatives and library limitations, while the discussion of affected users, implementation experience, and coordination is entirely absent.

- The paper explains why `uintptr_t` is not a viable alternative, citing both its optional status and its incompatibility with constant evaluation.
- It grounds the proposal in a specific NB comment and connects the proposed `void*` return type to the stated safety concern.
- The paper offers no implementation experience or evidence of how the change would behave in practice.
- It does not identify who is affected by the current API or how the change would interact with existing code and other standardization efforts.

Verdict: Weak (2/14)

The paper gestures toward a motivating rationale and an analogy for treating the empty `when_all()` case as a completion, but it does not build the surrounding case that would justify a standards change. Its support is concentrated almost entirely in assertions about why the current rule is unnecessary, while the sections that would connect the change to real users, existing practice, or implementation experience are effectively absent. What remains thinnest is any evidence that the proposed behavior is expected, implementable, or needed by the standard rather than simply plausible.

- The strongest support is the paper’s claim that zero senders already trivially satisfy “all” and therefore `when_all()` could reasonably mean `just()` rather than being ill-formed.
- The paper also asserts a special-case burden for generic algorithms, though it does not demonstrate who actually encounters that burden.
- It offers no evidence of affected users, implementation experience, or prior art that would corroborate the proposed interpretation.
- Most glaringly, the paper never establishes why the standard library, as opposed to user-level wrappers or conventions, should change.

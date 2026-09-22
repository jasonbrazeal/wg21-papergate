Verdict: Weak (2/14)

The paper offers only a narrow sliver of the case needed for standardization: it identifies a plausible lifetime hazard in one code pattern, but leaves nearly every other question about necessity, audience, alternatives, and feasibility unaddressed. The support is thinnest where it matters most for a standards-track document—there is no evidence about affected users, no comparison to existing practice or library-based mitigations, and no indication that anyone has tried to implement the idea.

- The strongest support is the single concrete example showing how an exception can allow asynchronous tasks to outlive the objects they reference.
- The paper does not establish who is affected by the problem, whether it is widespread, or whether it is already handled by common patterns or tools.
- The paper gives no account of prior art, alternative designs, or why the solution belongs in the standard rather than in a library or guideline.
- The most glaring omission is the absence of any implementation experience, which leaves the proposal without evidence that the mechanism is practical or well understood.

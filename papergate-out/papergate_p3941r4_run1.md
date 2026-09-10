Verdict: Strong (8/14, close to Adequate)

The paper offers some concrete grounding for its standardization case, particularly in explaining how the proposed facility interacts with the existing scheduler model and why a library-only approach may be insufficient. However, the support is uneven: several sections that would normally establish the need for a standard, the affected audience, and real-world viability are left unaddressed, which weakens the overall argument.

- The strongest support comes from the technical rationale, including the discussion of scheduler affinity, receiver environment queries, and the permissive error specification that allows throwing synchronization primitives.
- The paper also provides a specific account of prior art, noting how the original `task` proposal used `continues_on` to restore execution on the original scheduler.
- The most glaring omission is the absence of any discussion of who is affected by the proposal, leaving the motivating user base and practical impact unclear.
- Implementation experience is likewise unaddressed, so the paper offers no evidence that the design has been tried in practice or validated outside the specification itself.

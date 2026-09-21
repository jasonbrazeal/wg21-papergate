Verdict: Strong (8/14, close to Adequate)

The paper provides a narrow but concrete rationale for its proposal, mainly by explaining why existing facilities such as `uintptr_t` are insufficient and why direct access to the stored address is unsafe. The support is thinnest around the affected audience, implementation experience, and interoperability, leaving the reader without a clear picture of who would use the feature or how it behaves in practice.

- The strongest support explains why a library-only solution fails, citing the lack of a mandated `uintptr_t` and its incompatibility with constant evaluation.
- The paper also gives specific context from the NB comment and EWG’s reluctance, which grounds the proposal in real committee discussion.
- It does not address who is affected by the change, making it hard to judge the proposal’s reach or urgency.
- The most glaring omission is the absence of any implementation experience or coordination discussion, leaving practical feasibility and ecosystem impact unexamined.

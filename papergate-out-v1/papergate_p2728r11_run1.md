Verdict: Strong (10/14)

The paper offers meaningful but uneven support for its own standardization, grounding its motivation in concrete failure modes and implementation experience while leaving key strategic questions about standards placement and library viability largely unanswered. The strongest evidence is practical and specific, but the case thins considerably around coordination with existing Unicode facilities and why this work cannot succeed outside the standard.

- The paper gives concrete, specific motivation by tying exception-based Unicode error handling to denial-of-service vulnerabilities on untrusted input.
- It demonstrates real implementation experience through a reference implementation and a lineage of prior revisions and reimplementations.
- It does not address coordination or interoperability with existing standard or ecosystem Unicode facilities.
- It does not explain why a library would be insufficient, leaving the central standardization rationale incomplete.

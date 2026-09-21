Verdict: Strong (10/14)

The paper provides a reasonably grounded case for standardization, with concrete references to prior discussions, design rationale, and standard-library gaps, but it leaves important practical evidence unaddressed. The strongest support appears in the discussion of prior art and coordination with existing proposals, while the thinnest areas concern implementation experience and the affected user population.

- The paper substantiates its design rationale by explaining the scheduler-resumption behavior and linking it to earlier `task` proposals and `continues_on`.
- It justifies the need for a standard facility by noting the lack of easy scheduler adaptation in the standard library and the specification’s allowance for throwing synchronization primitives.
- The paper engages with prior standardization concerns by citing multiple issues raised against `affine_on` and discussed in P3796R1.
- It does not identify who would be affected by the proposal or provide any implementation experience to demonstrate feasibility in practice.

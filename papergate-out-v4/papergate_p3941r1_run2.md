Verdict: Adequate (4/14)

The paper offers a narrow but genuine basis for standardization: it connects the proposed guarantee to a specific, already-discussed problem with `affine_on` and situates the idea against prior designs. Beyond that initial motivation and the outline of an alternative, however, the case is largely undeveloped, especially on the question of why this belongs in the standard or how it would fit with existing facilities.

- The strongest support is the identification of a concrete specification issue with `affine_on`, including the need for symmetric transfer between `task`s to complete on the correct scheduler.
- The paper gives a recognizable account of prior work, including the earlier use of `continues_on` and the simplification enabled by the proposed guarantee.
- The thinnest areas are the absence of any established case for standardization, interoperability, or why a library solution would not suffice.
- The claim about how users would be affected is left as a bare assertion, and the implementation experience offered does not demonstrate meaningful practice with the proposed design.

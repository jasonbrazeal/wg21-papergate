Verdict: Strong (8/14)

The paper provides credible support in the areas of implementation experience, prior art, and the inadequacy of a library-only approach, but it leaves the case for standardization thinner on who is actually affected and on coordination with existing or in-flight standards work. The strongest material is practical: a reference implementation, reported usage since 2023, multi-compiler support, and concrete demonstration that a pure library solution fails without relying on optimizer behavior. The most serious gaps are the absence of interoperability or coordination evidence and the lack of specificity about the affected user base.

- The paper is strongest in showing that the facility has been implemented and used across all three major compilers, with tests demonstrating the intended compile-time failure behavior.
- It also firmly establishes that prior and existing C++ mechanisms do not provide this capability portably, and that a library-only or optimizer-dependent approach is unsuitable.
- The claim about who is affected is asserted through usage and use cases but not backed with enough concrete detail to show the breadth or significance of that audience.
- The paper offers no coordination or interoperability discussion, leaving entirely unexamined how the proposal relates to contracts, profiles, or other standardization efforts in the same space.

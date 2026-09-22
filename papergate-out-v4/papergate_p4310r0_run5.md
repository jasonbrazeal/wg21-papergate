Verdict: Excellent (12/14)

The paper offers substantial support for standardizing its proposed semantics, with most of the necessary case already established through prior committee decisions, deployed implementations, and documented practice. The support is thinnest where the paper argues that a library solution will not suffice, since that claim rests more on inference from related facilities than on direct evidence for the specific feature being proposed.

- The paper’s strongest ground is that the committee has already adopted the parallel restriction for standard-library hardened preconditions in C++26, so the core design question is settled rather than novel.
- The paper also convincingly shows that both affected deployments and prior art consistently treat termination as the production default and continuation modes as temporary adoption aids.
- The most visible gap is the argument that a library cannot provide what is needed, which is asserted but not established with direct evidence for this particular facility.

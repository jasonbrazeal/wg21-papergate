Verdict: Strong (9/14)

The paper offers substantial support on several fronts—showing the issue matters, establishing the prior-art landscape, exposing coordination problems, and documenting implementation experience—but its case is thinnest where it relies on unsupported claims of who is affected and why a standard is needed, and it offers nothing at all on why a library solution would not suffice.

- The strongest support rests on the implementation record showing a decade of shipped named-guarantee practice, including clang-tidy and MSVC, set against no shipped deployment of the distinctive machinery the paper challenges.
- The paper also establishes the coordination problem concretely by tracing how P3100R8 withdrew the `detection_mode` enumerators that P3081R2’s wording still depends on, leaving a live inter-paper dependency without a mechanism.
- The argument that the standard must act in this area is asserted through the poll-history reconstruction and deployment evidence, but the paper does not establish why standardization, rather than other venues, is required.
- Most glaringly, the paper provides no support for the claim that this work cannot be done as a library, leaving that essential part of the standardization case entirely unaddressed.

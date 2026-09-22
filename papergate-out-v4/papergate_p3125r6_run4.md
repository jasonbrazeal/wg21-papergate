Verdict: Strong (8/14)

The paper’s strongest, most concrete support comes from its implementation experience and from acknowledging comparable designs in other languages and LLVM, but much of the argument for who needs this and why it belongs in the standard is asserted rather than demonstrated. The thinnest areas are the absence of evidence that existing alternatives are insufficient for real users and the lack of a clear explanation of how standardization would coordinate with current practice.

- The paper is on firmest ground in showing that an earlier form of the design has been implemented in libc++ and clang and is publicly accessible.
- It also does reasonably well at situating the idea against prior art in Rust, D, Zig, LLVM, and other systems, while noting that the proposed interface differs from those designs.
- The case for who is affected and why the feature matters relies heavily on the general popularity of pointer tagging, without showing that those users are blocked by the current C++ approaches.
- Most notably, the paper does not establish why a compiler-supported standard facility is necessary rather than a library-only solution, especially since the claimed constant-evaluation limitation is mentioned but not developed.

Verdict: Strong (9/14)

The paper offers meaningful support for its standardization in the areas of existing practice and interoperability, particularly through its implementation survey and the acknowledged divergence of MSVC, but the case thins considerably where it needs to show who is affected and why a library solution cannot suffice. The strongest parts of the argument rest on evidence that libc++ and libstdc++ already implement the proposed behavior, while the weakest parts rely on general claims about standardizing common practice without direct demonstration of user impact or the inadequacy of non-standard alternatives.

- The paper most convincingly establishes prior art and implementation experience by comparing major standard libraries and showing that two of them already conform to the proposed specification for zero-length arrays.
- The paper also clearly establishes coordination and interoperability concerns by identifying MSVC’s non-conformance and the ABI break that a fix would entail.
- The paper only claims, but does not establish, why the affected user base is significant enough to justify standardization, since no concrete evidence of widespread reliance or breakage is provided.
- The most glaring omission is the absence of a demonstrated reason that a library-level or vendor-documented solution would not address the stated use cases, leaving the necessity of a standard change asserted rather than shown.

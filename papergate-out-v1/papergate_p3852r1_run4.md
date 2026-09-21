Verdict: Strong (10/14)

The paper gives a reasonably concrete account of why a standard facility is needed and why existing language rules make a library-only solution insufficient, but it leaves several parts of the standardization case largely unargued. The strongest material concerns implementation experience and the need for compiler support, while the thinnest areas are the absence of any discussion of affected users, coordination with related work, or interoperability concerns.

- The paper most convincingly supports its case by pointing to a working Clang prototype and explaining that the check requires compiler magic rather than ordinary library code.
- It also offers a specific rationale tied to constant evaluation, where unrelated pointer comparisons can fail in ways that cannot be recovered without a builtin.
- The discussion of prior art is limited to a passing mention of CHERI, without explaining how this proposal relates to or learns from such systems.
- The paper does not address who is affected by the problem or how the proposed facility would coordinate with existing or future standard features.

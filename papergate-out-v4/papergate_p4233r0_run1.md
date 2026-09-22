Verdict: Adequate (4/14)

The paper offers meaningful support for the motivation behind the proposed hardening checks, but its case for standardization remains incomplete in several important respects. The strongest material concerns the identified gap in existing hardening coverage and the direct evidence that the proposed checks correspond to real out-of-bounds accesses. The thinnest parts are the absence of any argument for why these additions belong in the standard itself, and why implementers or users could not address them through non-standard means.

- The paper establishes that the checks address a real coverage gap in the existing hardening paradigm and that violations produce observable memory-safety failures in major implementations.
- The paper stakes a plausible, if underdeveloped, claim to continuity with prior hardening work and to affecting users of the relevant library facilities.
- The paper does not establish why these checks require standardization rather than remaining implementer extensions or library-level mitigations.
- The paper offers no implementation experience beyond sanitizer confirmation of the underlying memory-safety violations, and does not show that the proposed standardized checks have been prototyped or deployed as specified.

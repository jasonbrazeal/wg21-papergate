Verdict: Strong (10/14)

The paper gives a reasonably concrete account of the implementation divergence it wants to fix and points to existing practice in two major standard libraries, but it leaves the standardization rationale largely implicit and does not explain why a library-level solution would be insufficient. The strongest support is practical rather than procedural: it shows released implementation experience and identifies specific defects in prior wording and proposals. The thinnest parts are the absence of any discussion of why the standard is the right venue and the lack of engagement with non-standard alternatives.

- The paper is strongest in documenting concrete implementation divergence and released experience in MSVC STL and libc++.
- It also usefully ties the problem to specific unresolved issues in LWG3081 and P2827R1.
- The most glaring omission is that it never addresses why the standard, rather than a library or implementation-level fix, is necessary.
- It likewise offers no discussion of why a library solution would not suffice for the proposed behavior.

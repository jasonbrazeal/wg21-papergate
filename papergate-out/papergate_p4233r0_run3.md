Verdict: Adequate (6/14)

The paper provides concrete implementation experience and cites prior work, but it leaves several foundational questions about standardization unaddressed. The thinnest support concerns why a library solution is insufficient and who would be affected by the proposed changes.

- The strongest support is the claim that the listed checks were verified to cause out-of-bounds reads or writes in major implementations, which grounds the motivation in observed failure.
- The paper also connects its scope to the earlier hardening paper P3471, giving some continuity with prior standardization discussion.
- The most glaring omission is the absence of any argument for why the standard, rather than a library, is the right vehicle for these checks.

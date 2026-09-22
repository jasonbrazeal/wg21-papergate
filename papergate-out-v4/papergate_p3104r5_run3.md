Verdict: Strong (9/14)

The paper gives a plausible motivation for adding these operations and demonstrates that they can be implemented, but much of the argument for why they belong in the standard rests on assertions that are not backed up with evidence. The thinnest support appears where the paper most needs to connect practical need, compiler advantage, and the insufficiency of library-only solutions.

- The strongest support is the existence of a reference implementation that works across major compilers and already exploits relevant hardware support on ARM and x86_64.
- The paper clearly establishes that the operations are non-trivial in software and have widespread hardware acceleration.
- The claim of affected users is not established beyond a single GitHub search presented without enough context to show how representative or significant it is.
- The most glaring omission is the failure to demonstrate convincingly that a library implementation cannot suffice, despite that being central to the case for standardization.

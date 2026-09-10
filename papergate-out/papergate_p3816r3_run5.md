Verdict: Strong (9/14)

The paper grounds its standardization case in concrete references to P2996 and compiler feedback, but it leaves several parts of its argument asserted rather than demonstrated, particularly around why a library solution would be insufficient and who would actually be affected by the absence of hashing.

- The strongest support comes from the explicit connection to P2996’s intentional omission of hashing and the compiler feedback favoring stable hashing through mangling.
- The claim that robust hashing requires compiler support is repeated as a reason for standardization, but no evidence or example is offered to show why a library-only approach would fail.
- The paper does not identify any affected users, use cases, or workloads that would motivate adoption.
- There is no implementation experience reported, leaving the practical viability and design constraints of the proposed facility unexamined.

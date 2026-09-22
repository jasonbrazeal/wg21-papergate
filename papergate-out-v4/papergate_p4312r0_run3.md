Verdict: Strong (11/14, close to Excellent)

The paper’s strongest material comes from the existence and long use of Clang’s nonblocking and nonallocating effects, which gives the proposal a concrete implementation history and a clear reason to prefer standardization over a vendor attribute. The case is considerably thinner when it moves from “this exists and is useful” to showing that the affected population, the limits of a library solution, and the breadth of implementation experience are actually established rather than asserted.

- The most convincing support is the demonstrated prior art: Clang already implements these effect checks in real code, and the paper explains why attributes cannot carry the guarantee the way a type-based, compiler-checked construct can.
- The proposal also justifies standardization itself well, since separate compilation and type identity make a purely informal or attribute-based convention unreliable across interfaces.
- The thinnest established support concerns who is actually affected and how much implementation experience exists beyond the single Clang precedent, where the paper largely repeats the same real-time-audio and libc++ references without broadening the evidence.

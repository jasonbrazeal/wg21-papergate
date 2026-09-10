Verdict: Strong (8/14, close to Adequate)

The paper grounds its case most concretely in implementation experience and in the specific oddity it wants to remove, but it leaves several parts of the standardization argument asserted rather than demonstrated. The thinnest support is around who is actually affected and why the proposed restriction belongs in the standard rather than being handled elsewhere.

- The strongest support is the reported implementation in a Clang fork, including successful compilation of LLVM/Clang/libc++ and another large codebase.
- The discussion of prior art and alternatives is specific about how related papers would otherwise have to accommodate the same implausible signatures.
- The claim that nobody writes such declarations is asserted without evidence about real-world usage or affected code.
- The paper does not address coordination and interoperability, nor why a library-level or non-standard solution would be insufficient.

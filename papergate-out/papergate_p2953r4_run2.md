Verdict: Adequate (7/14, close to Strong)

The paper gives a concrete account of the problem and demonstrates implementability, but it does not build a persuasive case that the change belongs in the standard, largely because the affected audience, rationale for standardization, and non-library alternatives are left unexplored.

- The strongest support is the implementation experience, with the proposed wording compiled against LLVM/Clang/libc++ and another large C++17 codebase.
- The paper identifies specific drawbacks of the current rule and points to related work that would need to remain consistent with any change.
- The justification for acting through the standard is asserted rather than argued, with no explanation of why the current permission is harmful enough to warrant normative change.
- The paper does not address who is affected, how the change interacts with existing code or teaching, or why a library-level or guidance-level response would be insufficient.

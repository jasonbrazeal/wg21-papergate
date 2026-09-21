Verdict: Adequate (6/14)

The paper gives a reasonably concrete account of why the current rule is odd and shows that a compiler implementation exists, but it leaves large parts of the standardization case unstated, especially around affected users, committee coordination, and why a library solution would not suffice.

- The strongest support is the implementation experience, with both wording options reportedly compiled against LLVM/Clang/libc++ and another large C++17 codebase.
- The paper also grounds its motivation in a specific permitted declaration and notes the consistency burden this places on related proposals such as P3834.
- It does not identify who is affected by the status quo or what practical code would benefit from the change.
- The most glaring omission is the absence of any discussion of coordination, interoperability, or why the problem cannot be addressed outside the standard.

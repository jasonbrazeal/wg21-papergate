Verdict: Strong (9/14)

The paper’s strongest support lies in its concrete account of existing practice and its clear explanation of how the current restrictions produce undefined behavior in an area users genuinely rely on. Its case is much thinner when it comes to showing who is affected beyond a code-search result, and it does not engage at all with the possibility of a library-level solution. The most conspicuous gap is the absence of any argument for why a library cannot address the need.

- The paper establishes why the issue matters by pointing to undefined behavior for 8-bit character types and the practical importance of generating random bytes.
- It provides solid implementation experience, citing extensions in libc++ and libstdc++ as well as the behavior of the MSVC STL.
- The evidence for affected users rests almost entirely on a GitHub code search and is treated as self-evident rather than examined.
- The paper never addresses why a library-based approach would be inadequate, leaving a core standardization question unanswered.

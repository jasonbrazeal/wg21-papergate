Verdict: Strong (8/14)

The paper gives a genuinely concrete account of the stack-growth problem it wants to solve and points to real implementation experience, but most of its broader case rests on assertions about pervasiveness, uniqueness, and the impracticality of alternatives that are named rather than demonstrated. The thinnest support sits exactly where the standardization argument should be strongest: the claim that the fix must enter the standard now, that the affected surface is unavoidable, and that no non-standard mitigation can suffice.

- Its strongest support is the implementation experience, credited as established through the author’s maintenance of Capy and Corosio.
- The core motivating problem—unbounded stack growth from synchronous sender completion under the current protocol—is clearly established.
- The section on who is affected remains thin because the claimed convergence of five out of six libraries on `coroutine_handle<>` return is asserted without supporting evidence.
- The most glaring omission is the unsupported claim that the standard must change now because the protocol-level fix is pervasive and the gap is otherwise permanent, when no sufficient case is made for why a library-level or design-level mitigation would not do.

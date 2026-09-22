Verdict: Strong (10/14)

The paper gives substantial support for standardization on the dimensions that matter most to a working group: it grounds the problem in deployed practice, documents public decision history, and adds implementation or prototype evidence for several response shapes. The support is thinnest where the paper must show that only a standard can solve the problem, and that the proposed direction holds together across translation units and toolchains.

- The strongest support is the concrete evidence of deployed and prototyped response shapes, including the GCC and Clang forks on Compiler Explorer, which anchors the design space in real implementation experience.
- The paper clearly establishes who is affected by citing libc++ hardening across hundreds of millions of lines and by documenting SG21’s seven January 2025 polls on the `noexcept` interaction.
- The least established part is the claim that the ODR argument specifically reaches Option 0 and not Option A, since the paper marks that argument as asserted rather than demonstrated.
- The most glaring omission is the coordinating and interoperability case: the paper asserts a single program-wide handler and consistent mangling consequences, but does not establish that the proposed semantics behave coherently across the ABI, linking, and mixed-declaration scenarios it raises.

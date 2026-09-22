Verdict: Weak (2/14)

The paper offers only a very thin case for standardization, largely resting on a desire attributed to CWG for consistency and a single sentence about current compiler divergence. Most of the necessary support—who is affected, why the standard is the right venue, why a library solution will not do, and how the change fits with the wider ecosystem—is simply absent.

- The strongest support is the reported implementation divergence, with GCC accepting the behavior while Clang and MSVC reject it.
- The paper at least gestures toward alternatives by noting that rejection would leave noexcept-specifiers self-consistent but inconsistent with function contract specifiers.
- The most glaring omission is the lack of any discussion of who is affected by the current state of affairs or what practical problems it causes.

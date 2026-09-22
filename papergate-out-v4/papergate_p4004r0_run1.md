Verdict: Adequate (6/14)

The paper does establish why the issue matters and shows that there are plausible alternatives, but it leans heavily on a single anecdote about one implementation’s bug reports to carry most of its case. The thinnest areas are the absence of concrete evidence about affected users, real-world code, implementation plans, and why a library-level workaround cannot suffice.

- The strongest support is the contrast between the CWG 1395 resolution and the observed behavior of GCC, Clang, and MSVC, which grounds the problem in existing practice.
- The paper demonstrates that there is a tractable direction by pointing to CWG 3154 and a minimal change focused on reverting part of the earlier resolution.
- The case for who is affected remains anecdotal, resting on reported bug feedback to one vendor without examples or scale.
- The most glaring omission is implementation experience: the paper acknowledges that most implementers are unlikely to adopt the specified rules, but offers no evidence of a path toward convergence.

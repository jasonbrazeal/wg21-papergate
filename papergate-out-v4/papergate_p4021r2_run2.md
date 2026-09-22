Verdict: Strong (8/14)

The paper offers meaningful support for its core motivation, prior art, and implementation experience, but its case thins considerably when it comes to showing who is affected, why standardization is necessary, and why a library or existing compiler attributes cannot suffice. The strongest material is concrete and demonstrable, while the weakest portions rely on assertions about portability, usage, and design clarity that are not backed with evidence.

- The paper clearly establishes a real gap between `static_assert()` and runtime `assert()`, and shows that existing compiler behavior can already approximate the proposed feature.
- Implementation experience is the best-supported area, with a published macro, use since 2023, and a concrete LTO example across all three major compilers.
- The claim that a standardized keyword is needed rather than a library macro or existing attributes rests on unestablished assumptions about portability and implementation clarity.
- The paper never establishes who is actually affected or why existing codebases cannot continue using the demonstrated macro approach.

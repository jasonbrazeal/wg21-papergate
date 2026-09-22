Verdict: Adequate (7/14, close to Strong)

The paper gives a reasonably clear account of the problem it addresses and shows that the feature has been prototyped, but the argument for standardization is uneven: several important points are asserted rather than demonstrated, especially around prevalence, workarounds, and the limits of library-only solutions.

- The strongest support comes from concrete implementation experience in GCC and Clang, with compiler flags and a Compiler Explorer link showing the feature exists in practice.
- The paper also identifies a plausibly awkward situation in generic code and explains why the change would improve ergonomics there.
- However, the claim that the situation arises often is not backed by evidence beyond a reference to another paper, leaving the frequency and severity of the problem largely unestablished.
- The most glaring omission is that the paper does not actually demonstrate why existing declaration-level constraints or a library-based approach are inadequate, despite saying that duplication or forwarding would be required.

Verdict: Adequate (6/14)

The paper offers a solid conceptual motivation for changing `when_all`, and it points to relevant prior discussion and a possible implementation, but it does not convincingly establish that the proposed change belongs in the standard rather than remaining an implementation detail or library-level adaptation.

- The strongest support is the clear explanation of why `when_all` can generate an unnecessary stop source and why current sender properties make that behavior hard to avoid.
- The paper also grounds the idea in existing discussion and prior art, including a reference implementation and a known workaround for the unary case.
- The case for affected users is thin, relying on a single implementation’s workaround and an implementation of the paper without broader evidence of need across the ecosystem.
- The most glaring omission is the absence of any argument for why the standard should specify this behavior, given that library-level implementations appear capable of addressing it in practice.

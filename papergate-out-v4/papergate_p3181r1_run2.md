Verdict: Adequate (6/14)

The paper offers solid grounding for why the problem matters and for its reading of prior art and alternatives, but it leaves several central burdens—especially implementation experience, library workarounds, and the need for a standardese change—largely asserted rather than demonstrated. The thinnest support appears around practical evidence and around the claim that existing primitives or library-level solutions cannot already provide the needed guarantee.

- The strongest support is the paper’s explanation of why the current happens-before and lifetime rules fail to give the guarantee the authors want.
- The discussion of prior art and alternatives is credible, particularly the rejection of strengthening happens-before itself and the historical note about Itanium.
- The paper does not convincingly establish that common implementations actually avoid the problematic outcome, since that remains a claim about plausibility rather than demonstrated practice.
- The most glaring omission is implementation experience, where the only cited architecture is Itanium, which is historical and does not show that the proposed change reflects real-world behavior or need.

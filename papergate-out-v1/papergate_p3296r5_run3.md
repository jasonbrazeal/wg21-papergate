Verdict: Adequate (4/14, close to Weak)

The paper provides only a narrow, example-driven justification for its proposal, leaving most of the case for standardization unstated. Its strongest support rests on a single lifetime-safety scenario, while broader questions about affected users, prior work, and implementation experience are entirely absent.

- The paper gives a concrete, specific example of how the proposed feature would prevent use-after-lifetime bugs when exceptions bypass scope joining.
- The same example is reused to argue that a library-only solution is insufficient, giving that point at least some grounding.
- The paper does not address who would be affected by the change or what existing practice and alternatives look like.
- The most glaring omission is the complete lack of implementation experience, leaving no evidence that the design is practical or has been validated in real code.

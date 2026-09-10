Verdict: Adequate (4/14, close to Weak)

The paper offers only a narrow, name-focused argument for its position, with some concrete references to existing `std::execution` facilities but little else to justify standardization. The support is thinnest around the practical consequences, affected users, and why a library-level or naming-only change would not suffice.

- The strongest support comes from specific examples showing how the current name `affine_on` conflicts with the established use of “on” in related `std::execution` entities.
- The paper grounds its discussion in prior art by citing `std::execution::task` and listing the three pre-existing “on”-named facilities.
- It does not address who is affected by the proposed change or what the standardization impact would be.
- The most glaring omission is the absence of any discussion of implementation experience, coordination, or why a library solution cannot address the concern.

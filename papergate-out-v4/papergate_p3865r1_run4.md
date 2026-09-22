Verdict: Strong (9/14)

The paper gives solid, concrete support for the existence of a real defect, with specific issue references and clear examples that implementation divergence has already made visible. The case for why a library-only solution is impossible is asserted rather than demonstrated, and the claims about affected users and implementation experience rest almost entirely on repeated, high-level statements rather than evidence in the paper.

- The strongest support is the established prior art and alternatives section, which correctly grounds the proposal in recent template matching history and ties it to active core issues.
- The paper clearly establishes why the problem matters by naming CWG 3003 and LWG 4381 and showing a crash-inducing example.
- The thinnest support is the repeated, unsupported claim that no library wording fix exists, which is asserted as fact without showing why the core-language change is the only route.
- Glaringly absent is any concrete demonstration of implementation experience, since statements that “current implementations accept” the behavior are not backed by tested compiler or library results in the paper.

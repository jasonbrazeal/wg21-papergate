Verdict: Adequate (6/14)

The paper’s support is uneven: it offers solid grounding in implementation experience and a clear account of the problem’s relevance, but it struggles to show that this behavior requires standardization rather than being expressible through existing or library-level mechanisms. The thinnest part is the absence of any developed argument for why the standard itself must change, which leaves the proposal’s core justification asserted rather than demonstrated.

- The strongest support comes from implementation experience, with prototype implementations in both GCC and Clang described as straightforward and already available for testing.
- The paper also establishes why the behavior matters by connecting it directly to concerns about exceptions escaping from contract violations and the overhead or safety implications involved.
- Prior art and alternatives are acknowledged, though the paper does not fully establish how its approach improves on or coordinates with the cited competing or complementary proposals.
- The most glaring omission is the lack of any established case for why the standard—as opposed to a library facility or compiler extension—is necessary to deliver the proposed semantics.

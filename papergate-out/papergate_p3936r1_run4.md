Verdict: Adequate (7/14, close to Strong)

The paper gives a partial account of why the proposed change is needed, but it leaves several important parts of the standardization case unstated, especially around affected users and implementation experience. The strongest material concerns alternatives and why a library-only solution would fall short, while the rationale for changing the standard itself is largely asserted rather than argued.

- The paper offers concrete reasons why `uintptr_t` and library-only approaches are inadequate, including lack of a mandate and failure during constant evaluation.
- It identifies the safety concern with direct access at `address` as the motivating problem, though the connection to the proposed `void*` return is not fully developed.
- The discussion of affected users and coordination with existing practice is absent, leaving the scope and impact of the change unclear.
- No implementation experience is presented beyond a single compiler explorer link, so the paper does not show that the change is practical across implementations.

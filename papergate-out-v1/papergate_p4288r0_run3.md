Verdict: Strong (10/14)

The paper offers a solid, well-supported case in several key areas, particularly around the need for reference returns in asynchronous functions and the limitations of decay-copying, but it leaves important practical questions unanswered. The thinnest support concerns implementation experience and coordination with existing algorithms, where assertions are made without evidence or detail.

- The strongest support is the concrete, standards-based argument that synchronous reference returns are uncontroversial and should extend to asynchronous functions.
- The discussion of why a library-only solution fails is well grounded in the specific requirement that decay-copying materially changes the completion.
- The paper’s claims about implementation against nVidia’s reference implementation are unverifiable because the implementation is not publicly available.
- The most glaring omission is the lack of any discussion of who is affected by the proposal, leaving the audience and impact unclear.

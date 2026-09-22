Verdict: Strong (9/14)

The paper offers solid support for the core rationale—why virtual functions need contract support and why this requires language-level changes rather than library workarounds—but its case thins considerably when it comes to demonstrating who is actually asking for this feature, how it coordinates with existing practice, and whether the proposed wording has been meaningfully exercised in real code.

- The strongest part of the paper is its treatment of prior art and alternatives, which clearly explains why earlier inheritance models and other languages' approaches fail to express the full range of use cases.
- The argument for why the standard must address this is well grounded in the breadth of existing C++ code and the need to handle multiple inheritance correctly.
- The paper's claims about who is affected rest mainly on a single EWG poll and broad assertions about existing code, without concrete evidence of user demand or real-world adoption needs.
- The most glaring omission is implementation experience: the paper repeatedly references a complete GCC implementation but offers no evidence of testing, use, or lessons learned from that implementation.

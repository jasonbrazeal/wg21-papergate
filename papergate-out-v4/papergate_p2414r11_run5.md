Verdict: Strong (9/14)

The paper offers solid grounding in prior work and real-world usage, but its case thins considerably when it comes to showing that existing practice actually breaks under current rules, that a library solution is insufficient, and that the affected codebases need the proposed special behaviors rather than some other remedy.

- The strongest support comes from the paper’s engagement with prior art and implementation experience, including long-standing production usage and the historical Treiber stack precedent.
- The paper also convincingly explains why the topic matters by tying `volatile` and pointer-lifetime issues to device I/O and existing concurrent algorithms.
- What remains thinnest is the claim that a library cannot address the problem: the cited passages assert current language limitations but do not demonstrate why a standards-level language change is the only viable path.
- The most glaring omission is the lack of concrete evidence identifying who is affected and how widely, beyond general assertions about production use over decades.

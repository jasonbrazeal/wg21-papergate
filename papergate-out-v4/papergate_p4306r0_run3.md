Verdict: Strong (10/14)

The paper’s strongest support rests on implementation evidence and the demonstrated existence of deployed, production-scale practice, while its thinnest support lies in showing why standardization—rather than a library or continued vendor convention—is required. Much of the argument for affected users, the need for a standard, coordination, and the insufficiency of non-standard approaches is asserted rather than established with concrete evidence.

- The clearest support is that the named-guarantee checking form has shipped for a decade across multiple vendors at production scale, with at least one large codebase rebased onto an experimental contract_assert implementation.
- The prior-art comparison is credibly framed as a decision the committee must make between two live proposals that answer the same configuration question, with existing committee criteria available to weigh them.
- The paper asserts, but does not demonstrate, that the affected population extends meaningfully beyond the vendors and projects already using the named-guarantee form, and that the proposed mechanism would serve needs those existing users cannot already meet.
- The most glaring omission is the lack of established evidence that standardization, as opposed to a library facility or continued vendor practice, is necessary in the first place.

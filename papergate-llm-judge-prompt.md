You are reviewing a WG21 proposal paper to assess one aspect (and only this aspect), namely whether the paper justifies the need for the proposal to be standardized, as opposed to, for instance, living as a separate library or, in the case of language proposals, rely on library-based alternatives, etc.
You are not supposed to assess the instrinsic quality of the proposal, only if the paper does the homework in terms of justifying is standardization merits.

There are seven criteria you're asked to assess:
Motivation (why it matters):
Describes the reason, motivation or justification for the proposal: what problem exists today and why it is worth solving. This is about the problem, not the solution: text that only explains how the proposed feature works does not count.
Audience (who is affected):
Quantifies the usage or the size of the affected audience: counts, percentages, survey results, named codebases, download or telemetry figures, poll outcomes. Qualitative claims that something is 'common', 'widespread' or 'frequently requested', with no figure attached, do not count.
Prior art (prior art and alternatives):
Identifies specific design alternatives, competing proposals, existing library facilities or prior art by name, and says how the proposal relates to them. Naming an existing implementation, a framework that solved the same problem, or another committee proposal that this design follows or diverges from all count here. This is about enumerating and comparing the alternatives; arguing that they are inadequate belongs to a different criterion.
Vehicle (why the standard):
Explains why the C++ standard specifically is the right vehicle: why this must be in the language or the standard library rather than left to a third-party library, a compiler extension or a quality-of-implementation matter. Arguing that the feature is useful is not the same as arguing that it must be standardized.
Coordination (coordination and interoperability):
Identifies a concrete coordination problem that standardization would solve, or an interoperability opportunity it would enable: named parties who must agree, an ABI or vocabulary-type boundary across which independently written code must interoperate, or incompatible ecosystem conventions that a single blessed spelling would unify. Merely relating this design to another proposal, or noting that it follows another facility's conventions, does NOT count here - that is prior art. There must be a party who must agree or a boundary that must match.
Insufficiency (why a library will not do):
Shows why solutions outside the standard are insufficient, with specific technical reasons: something a user-space library provably cannot express, cannot do portably, or can only do at unacceptable cost. Mere preference, ergonomics or verbosity complaints, unsupported by a technical obstacle, do not count.
Implementation (implementation experience):
Describes implementation, field or deployment experience of this proposal or a close precursor: an existing implementation, a compiler branch, a shipped library, use in production code, measured results from that use. A promise or plan to implement does not count.

For each criterion, please rate like this:
0: the criterion is not addressed at all in this text.
1: the criterion is addressed only by assertion: the claim is made but nothing supports it.
2: the criterion is addressed with specifics: figures, names, comparisons, technical reasons or reported experience that a reader could check.



Paper ID
p3045r9
p2728r14
p0260r20
p1040r11
p3091r6
p2806r5
p3100r8
p2826r4
p2287r6
p2719r7


Paper ID    Link
p3045r9     https://wg21.link/p3045r9
p2728r14    https://wg21.link/p2728r14
p0260r20    https://wg21.link/p0260r20
p1040r11    https://wg21.link/p1040r11
p3091r6     https://wg21.link/p3091r6
p2806r5     https://wg21.link/p2806r5
p3100r8     https://wg21.link/p3100r8
p2826r4     https://wg21.link/p2826r4
p2287r6     https://wg21.link/p2287r6
p2719r7     https://wg21.link/p2719r7

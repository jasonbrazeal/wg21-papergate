Verdict: Adequate (7/14, close to Strong)

The paper gives a narrow but concrete rationale for changing `address` to return `void*`, grounded in the NB comment and the constraints around `uintptr_t`, but it leaves several parts of the standardization case largely unstated. The strongest support concerns why a library-only or `uintptr_t`-based fix is insufficient, while the thinnest areas are the absence of affected users, implementation experience beyond a single compiler link, and any discussion of coordination or interoperability.

- The paper most concretely supports its case by explaining that `uintptr_t` is not mandated and would not work during constant evaluation, which directly motivates a language-level return type change.
- It also grounds the proposal in a specific NB comment and notes prior EWG reluctance to mandate `uintptr_t`, giving some context for the chosen direction.
- The paper asserts that `void*` satisfactorily addresses the NB comment, but offers little supporting reasoning for why that type is the right standard solution.
- It does not identify who is affected by the current design or provide meaningful implementation experience, leaving the practical impact and feasibility of the change largely unexamined.

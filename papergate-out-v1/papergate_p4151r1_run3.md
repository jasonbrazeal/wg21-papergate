Verdict: Adequate (4/14, close to Weak)

The paper provides only a narrow, name-focused rationale for its proposal, with some concrete references to prior naming conventions and a brief mention of committee discussion, but it leaves the broader standardization case largely unstated. The thinnest areas are the absence of any discussion of affected users, why a library solution would be insufficient, implementation experience, or interoperability concerns.

- The strongest support comes from the specific observation that making `affine_on` unary undermines the meaning of the “on” suffix, tied to existing names like `on`, `continues_on`, and `starts_on`.
- The paper also cites a LEWG remark that changing the interface shape should prompt a name change, though it does not develop this into a fuller rationale.
- It does not address who would be affected by the change or what the practical consequences for users would be.
- Most glaringly, the paper offers no implementation experience, no argument for why a library cannot address the issue, and no discussion of coordination or interoperability.

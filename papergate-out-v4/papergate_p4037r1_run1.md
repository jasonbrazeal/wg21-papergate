Verdict: Strong (8/14)

The paper makes a credible start by establishing that the current restriction is a real defect and that implementations have already moved in the direction the proposal wants to standardize. Its case is much thinner, however, on the broader questions of who is affected, why wording changes are the right vehicle, and how the change coordinates with the wider library ecosystem. The thinnest areas are precisely where the paper relies on assertion rather than evidence.

- The strongest support is the combination of a clear motivation and documented implementation experience in both libstdc++ and libc++.
- The paper establishes prior art and alternatives adequately by pointing to existing library issue resolutions and implementation extensions.
- The discussion of affected users rests mainly on a code-search figure and a claim about breakage, without substantiating how representative or significant that breakage would be.
- The most glaring omission is the lack of a demonstrated case for why this belongs in the standard rather than remaining a common extension, since the paper’s own evidence suggests libraries already provide the behavior.

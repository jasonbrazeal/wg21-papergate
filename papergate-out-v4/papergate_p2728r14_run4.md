Verdict: Strong (8/14)

The paper offers a solid foundation for standardization, with credible implementation experience and a clear explanation of why safe Unicode replacement matters. Its case is much thinner when it comes to showing who specifically needs this in the standard, how it fits with existing facilities, and why a library solution would not suffice.

- The strongest support comes from the available reference implementation and its connection to prior libstdc++ work, which demonstrates real implementation experience.
- The paper clearly establishes the safety motivation, explaining the need for replacement behavior when invalid UTF is encountered.
- The least convincing part of the paper is its treatment of coordination and interoperability, where it offers almost nothing to show how the proposal would work with the rest of the standard.
- The claim that affected users are widespread is asserted rather than shown, leaving the practical urgency of standardization largely unestablished.

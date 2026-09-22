Verdict: Strong (9/14)

The paper gives credible, concrete support for the existence of the problem, the affected audience, the relevant prior art, and the availability of implementation experience, but it does not persuasively connect those facts to a need for standardization as opposed to a library-level fix. The case is thinnest around why the standard must change, how the change coordinates with existing guarantees and implementations, and why a library solution would be insufficient.

- The strongest support comes from the demonstrated implementation experience in {fmt}, including its wide deployment and past experience changing output format.
- The paper also clearly establishes why the current behavior matters to users and which communities are affected.
- The most obvious gap is the failure to show why this change belongs in the standard rather than in a library or implementation-specific setting.

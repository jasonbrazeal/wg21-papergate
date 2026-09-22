Verdict: Strong (8/14)

The paper offers solid justification for why pointer invalidation on `volatile` access matters and situates its approach well within prior C and C++ discussions, but much of the case for affected users, implementation practice, and the necessity of a standard-language change rests on assertion rather than demonstrated evidence.

- The strongest support is the connection to existing WG14 and WG21 work on pointer provenance and lifetime-end zap, which gives the proposal a clear technical lineage.
- The paper convincingly explains why `volatile` accesses need to tolerate invalid pointer values for hardware I/O address passing.
- The thinnest support is the repeated claim of widespread production use and de facto status quo, which is stated but not backed by concrete code, systems, or measured prevalence.
- The paper also does not establish why existing practice or library-level mechanisms cannot adequately address the problem, making the standardization need more asserted than shown.

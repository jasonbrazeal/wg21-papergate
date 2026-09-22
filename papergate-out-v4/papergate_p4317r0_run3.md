Verdict: Strong (11/14, close to Excellent)

The paper offers substantial support for standardizing a hardening profile in the form already deployed across multiple production systems, with particularly strong evidence in implementation experience, runtime cost, and real-world defect reduction. The case is thinnest where it leans on claims rather than established argument, especially in explaining why the standard—rather than existing implementations, libraries, or other standardization routes—is the necessary vehicle.

- The strongest support is the measured, shipped experience: the named-guarantee, terminate-on-violation form is running across eight systems, with hardening across hundreds of millions of lines of C++ costing about 0.30% on average and surfacing more than 1,000 bugs during rollout.
- The paper also establishes clearly who is affected and why the feature matters, since it targets the enumerable core-language undefined-behavior operations and preserves unchanged meaning for programs without violations.
- Prior art and alternatives are handled credibly, including the comparison with Contracts routing and the claim of zero foundational changes to the standard’s definitional machinery.
- The most glaring omissions are the under-supported arguments that a library cannot meet the need and that the standard itself is improved by adopting this profile, since the paper asserts these positions without establishing them beyond the fact that production deployments already exist.

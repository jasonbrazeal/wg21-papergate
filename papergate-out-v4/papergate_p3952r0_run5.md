Verdict: Adequate (7/14, close to Strong)

The paper offers credible evidence of existing implementation practice and some relevant prior art, but it leaves the core rationale for standardization largely asserted rather than demonstrated. The thinnest support appears wherever the paper depends on claims about portability, prevalence, and the inadequacy of non-standard solutions without connecting those claims to concrete consequences for users or the standard.

- The strongest support is the documented implementation experience, including libc++’s existing internal function and Hana Dusíková’s implementation with a compiler intrinsic.
- The prior art and alternatives are reasonably established through named implementations in Boost, Qt, and libc++, and through acknowledgment of the merged predecessor proposal.
- The paper only claims, rather than establishes, who is affected and why the feature matters, resting on a short list of projects and unsupported statements that the function is regularly requested or widely needed.
- The most glaring omission is the failure to establish why a library cannot suffice, since the paper itself acknowledges that current library implementations work in practice despite relying on unspecified behavior.

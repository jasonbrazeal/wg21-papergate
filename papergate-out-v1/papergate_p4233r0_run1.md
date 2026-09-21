Verdict: Adequate (6/14)

The paper provides concrete evidence that the proposed checks catch real out-of-bounds access in major implementations, but it leaves several parts of the standardization case largely unargued, particularly around affected users, the need for a standard rather than a library solution, and interoperability.

- The strongest support comes from implementation experience, with Address Sanitizer verification showing the checks detect actual OOB reads or writes in at least one major implementation.
- The paper also grounds itself in prior art by explicitly building on P3471R4 and P3697R1, which helps situate the proposal within ongoing hardening work.
- The thinnest support concerns why the standard is the right venue, since the paper does not address why a library-only approach would be insufficient.
- The most glaring omission is the lack of any discussion of who is affected, especially given the paper’s own note that some hardened functions are not widely used.

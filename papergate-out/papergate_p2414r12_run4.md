Verdict: Strong (9/14)

The paper’s support for its own standardization is uneven: it offers concrete historical and cross-committee context in places, but many of its central claims about necessity, affected users, and interoperability are stated without evidence or explanation. The thinnest support appears wherever the paper asserts that existing code and production practice demand a standard solution, since those assertions are not backed by examples, data, or references.

- The strongest support is the specific citation of WG14’s N2676 and the 1986 Treiber report, which grounds the discussion in identifiable prior work.
- The claim that concurrent algorithms using these pointer operations have been in production for decades is asserted without supporting examples or references.
- The argument that a standard solution is needed to preserve optimizations, debugging tools, and existing source code is presented as a conclusion rather than a demonstrated case.
- The most glaring omission is the unsupported assertion that `volatile` accesses must forgive invalidity for I/O device addresses, which is offered as a key interoperability point but never explained or justified.

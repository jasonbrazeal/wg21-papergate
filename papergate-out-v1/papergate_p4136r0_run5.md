Verdict: Strong (10/14)

The paper gives a reasonably concrete, implementation-grounded case for relaxing the constraints, but it leaves several parts of the standardization argument underdeveloped, particularly around affected users and the precise role of the standard in codifying existing practice.

- The strongest support comes from concrete testing across Clang, EDG, GCC, and MSVC, showing that implementations already accept values the standard currently forbids.
- The paper also explains why a library solution is insufficient, since the behavior was already used as an implementation extension point that the current wording accidentally removed.
- It offers some prior-art and interoperability evidence by identifying EDG as the outlier that diagnoses the first directive while all implementations accept the second.
- The most glaring omission is any discussion of who is affected by the current restriction or by the proposed change, leaving the practical stakes for users unclear.

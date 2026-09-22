Verdict: Adequate (7/14, close to Strong)

The paper offers meaningful support for the existence of a real core-language problem and for the general shape of a fix, but it leaves several parts of its standardization case asserted rather than demonstrated. The thinnest support concerns who is affected, why a library-only change will not suffice, and whether implementations truly align with the proposed semantics.

- The strongest support is the paper’s identification of a concrete wording defect tied to CWG 3003 and LWG 4381, with evidence that current deduction behavior can produce types that cannot otherwise be written.
- The paper also does well in grounding the issue in prior standardization work, including the design intent of P0091R3 and the later change from P0552R0.
- The case that the core language, rather than the library, must change is repeated but not established beyond pointing at LWG 4381.
- The most glaring omission is the absence of any account of who is affected, which leaves the urgency and scope of the proposed change unclear.

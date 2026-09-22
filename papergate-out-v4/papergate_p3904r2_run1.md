Verdict: Adequate (7/14, close to Strong)

The paper’s strongest case is that the problem is real and the proposed direction has credible precedent, particularly through the adoption of P2845 and the use of WTF-8 in other systems. The support becomes much thinner, however, around why this work belongs specifically in the C++ standard rather than in a library, and around evidence that anyone actually needs or has gained from standardizing it.

- The document clearly establishes the motivating gap—unpaired surrogates on Windows break lossless formatting—and grounds the proposed fix in an existing encoding and prior standardization work.
- It identifies Rust, Node.js libuv, and Python as prior art, which lends the general approach some external validation, though the paper does not develop how those systems’ choices bear on C++’s needs.
- The weakest part of the case is implementation experience: the only cited C++ implementation is in {fmt}, with no demonstration that users, standard library vendors, or other implementers have adopted or even tested the proposed behavior.

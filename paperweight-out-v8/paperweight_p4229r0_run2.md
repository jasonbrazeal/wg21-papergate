Verdict: Strong (10/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates why the problem is real, who is affected, what prior art exists, and that implementable solutions are already working on multiple hardware targets. The support is thinnest where the proposal needs to show that a library solution cannot suffice and that the proposed facility will actually interoperate across implementations, since the latter is asserted rather than demonstrated.

- The strongest support is the implementation experience, with measured results on CPU and GPU targets showing bit-level consistency and a concrete contrast with existing non-agreeing baselines.
- The paper also clearly establishes why the issue matters and who is affected, with specific performance and correctness data tied to floating-point scan and reduce.
- Prior art and the need for a standard-level contract are well grounded in existing practice and earlier proposals.
- The most glaring omission is the absence of any established argument for why a library cannot provide the proposed facility, leaving the standardization necessity incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 6 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 18. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 10.00   accumulate 10.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.50  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.00 / 10.00 / 10.00   (all 3 samples: 10.00)
headings: h2 13
on threshold: vehicle
splits: motivation[5] 0/1/1  motivation[8] 1/1/2  motivation[9] 2/2/1  audience[7] 0/0/2
        prior_art[7] 1/2/2  prior_art[11] 1/2/1  vehicle[7] 0/1/1  vehicle[8] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2. Scopes of determinism                     2/2/2  -> 2.00
  [4] 3. Expression is not execution               2/2/2  -> 2.00
  [5] 4. The accumulate and partialsum example     0/1/1  -> 0.67
  [6] 5. Reduce observes the root; scan observe... 2/2/2  -> 2.00
  [7] 5. Reduce observes the root; scan observe... 2/2/2  -> 2.00
  [8] 16. Conclusion                               1/1/2  -> 1.33
  [9] Appendix A: Direct Iterated Pairwise Scan... 2/2/1  -> 1.67
  [10] Appendix B: Implementation Experience        2/2/2  -> 2.00
  [11] Appendix C: Executable CUDA artifact         0/0/0  -> 0.00
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 0/0/0  -> 0.00
  [14] Appendix F: Cross-platform expression-rep... 0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): For floating-point and other order-sensitive operations, it can change the result.
candidate 2 (found by 3 of 45 passes): A proposal for deterministic `scan` or `reduce` is ambiguous unless it states the scope of determinism being promised.
candidate 3 (found by 3 of 45 passes): The Standard must not over-constrain how implementations schedule and map work to hardware.
candidate 4 (found by 3 of 45 passes): CUB’s existing `inclusive_scan` and `reduce` are each individually deterministic on this hardware, yet they do not agree with each other on the same input.

## audience - grade 2.00 (fired in 3 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 2. Scopes of determinism                     0/0/0  -> 0.00
  [4] 3. Expression is not execution               0/0/0  -> 0.00
  [5] 4. The accumulate and partialsum example     0/0/0  -> 0.00
  [6] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [7] 5. Reduce observes the root; scan observe... 0/0/2  -> 0.67
  [8] 16. Conclusion                               0/0/0  -> 0.00
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        2/2/2  -> 2.00
  [11] Appendix C: Executable CUDA artifact         0/0/0  -> 0.00
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 2/2/2  -> 2.00
  [14] Appendix F: Cross-platform expression-rep... 0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Measurements were taken on an NVIDIA Tesla T4 with `N` `=` `1,048,576` `double` inputs, block size `B` `=` `256`, and `--fmad=false` to prevent fused multiply-add contraction.
candidate 2 (found by 3 of 45 passes): At `N` `=` `10,000` `double` inputs (in-cache regime), the reduce measurements are: peak `canonical_block_dyadic_reduce<32>` throughput is approximately 41.5 GB/s on x86- 64 against an `std::reduce` baseline of approximately 23.3 GB/s
candidate 3 (found by 1 of 45 passes): Appendix B.8 reports a measured Tesla T4 result showing scan/reduce consistency at the bit level across 1M elements, alongside an existing GPU baseline whose scan and reduce do not agree with each other on the same input.

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2. Scopes of determinism                     1/1/1  -> 1.00
  [4] 3. Expression is not execution               1/1/1  -> 1.00
  [5] 4. The accumulate and partialsum example     1/1/1  -> 1.00
  [6] 5. Reduce observes the root; scan observe... 2/2/2  -> 2.00
  [7] 5. Reduce observes the root; scan observe... 1/2/2  -> 1.67
  [8] 16. Conclusion                               1/1/1  -> 1.00
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        2/2/2  -> 2.00
  [11] Appendix C: Executable CUDA artifact         1/2/1  -> 1.33
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 0/0/0  -> 0.00
  [14] Appendix F: Cross-platform expression-rep... 1/1/1  -> 1.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): P4016R0 addressed this for reduce by proposing a fixed expression structure. scan exposes the next distinction: reduce observes one value, while scan returns a sequence of prefix values.
candidate 2 (found by 3 of 45 passes): The complementary problem of controlling the floating-point environment so that a fixed expression evaluates identically across implementations is the subject of [P3375R3].
candidate 3 (found by 3 of 45 passes): The Standard Library already uses this separation.
candidate 4 (found by 3 of 45 passes): The simplest way to introduce expression and observation is the relationship between `accumulate` and `partial_sum`.

## vehicle - grade 1.50 (fired in 5 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 2. Scopes of determinism                     0/0/0  -> 0.00
  [4] 3. Expression is not execution               1/1/1  -> 1.00
  [5] 4. The accumulate and partialsum example     0/0/0  -> 0.00
  [6] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [7] 5. Reduce observes the root; scan observe... 0/1/1  -> 0.67
  [8] 16. Conclusion                               0/1/1  -> 0.67
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        2/2/2  -> 2.00
  [11] Appendix C: Executable CUDA artifact         0/0/0  -> 0.00
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 0/0/0  -> 0.00
  [14] Appendix F: Cross-platform expression-rep... 0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): This matters for standardization. A reproducible scan facility should not mandate a CPU-centric expression or a particular multi-pass schedule. It should specify observable values and leave implementations free to use hardware-appropriate execution strategies.
candidate 2 (found by 2 of 45 passes): Reproducibility is a contract specified by an abstract expression.
candidate 3 (found by 2 of 45 passes): This separation is essential for standardization.
candidate 4 (found by 2 of 45 passes): The Standard Library already contains a useful precedent: random-number generation.

## coordination - grade 0.50 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 2. Scopes of determinism                     0/0/0  -> 0.00
  [4] 3. Expression is not execution               0/0/0  -> 0.00
  [5] 4. The accumulate and partialsum example     0/0/0  -> 0.00
  [6] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [7] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [8] 16. Conclusion                               0/0/0  -> 0.00
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        0/0/0  -> 0.00
  [11] Appendix C: Executable CUDA artifact         0/0/0  -> 0.00
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 0/0/0  -> 0.00
  [14] Appendix F: Cross-platform expression-rep... 0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Reproducibility is a contract specified by an abstract expression. Agreement follows from choosing a named expression that defines the result.

## insufficiency - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 2. Scopes of determinism                     0/0/0  -> 0.00
  [4] 3. Expression is not execution               0/0/0  -> 0.00
  [5] 4. The accumulate and partialsum example     0/0/0  -> 0.00
  [6] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [7] 5. Reduce observes the root; scan observe... 0/0/0  -> 0.00
  [8] 16. Conclusion                               0/0/0  -> 0.00
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        0/0/0  -> 0.00
  [11] Appendix C: Executable CUDA artifact         0/0/0  -> 0.00
  [12] Appendix D: Executable CUDA witness — c... 0/0/0  -> 0.00
  [13] Appendix E: Executable CPU witnesses — ... 0/0/0  -> 0.00
  [14] Appendix F: Cross-platform expression-rep... 0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 9 of 15 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 2. Scopes of determinism                     0/0/0  -> 0.00
  [4] 3. Expression is not execution               0/0/0  -> 0.00
  [5] 4. The accumulate and partialsum example     0/0/0  -> 0.00
  [6] 5. Reduce observes the root; scan observe... 1/1/1  -> 1.00
  [7] 5. Reduce observes the root; scan observe... 1/1/1  -> 1.00
  [8] 16. Conclusion                               1/1/1  -> 1.00
  [9] Appendix A: Direct Iterated Pairwise Scan... 0/0/0  -> 0.00
  [10] Appendix B: Implementation Experience        2/2/2  -> 2.00
  [11] Appendix C: Executable CUDA artifact         2/2/2  -> 2.00
  [12] Appendix D: Executable CUDA witness — c... 2/2/2  -> 2.00
  [13] Appendix E: Executable CPU witnesses — ... 2/2/2  -> 2.00
  [14] Appendix F: Cross-platform expression-rep... 2/2/2  -> 2.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The implementation artifacts in the appendices are proof by existence.
candidate 2 (found by 3 of 45 passes): The framework is supported by implementation work on CPU SIMD targets (AVX2, NEON) and CUDA.
candidate 3 (found by 3 of 45 passes): Appendix B.8 reports a measured Tesla T4 result showing scan/reduce consistency at the bit level across 1M elements, alongside an existing GPU baseline whose scan and reduce do not agree with each other on the same input.
candidate 4 (found by 3 of 45 passes): Implementation experience suggests that it affects performance, scalability, buffering, streamability, numerical behavior, and hardware suitability.

-->

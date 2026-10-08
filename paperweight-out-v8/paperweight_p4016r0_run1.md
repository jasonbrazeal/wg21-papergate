Verdict: Strong to Excellent (11/14)

The paper offers solid support for its core technical claims, particularly around implementation feasibility, prior art, and coordination with existing practice, but it is thinner when it comes to showing who specifically needs this facility and why it cannot be adequately supplied outside the standard.

- The strongest support is the implementation experience, with working SIMD and CUDA implementations producing expression-identical results and throughput comparable to unconstrained reduction.
- The paper also establishes prior art and alternatives clearly, showing how the proposed canonical tree generalizes existing standard-library determinism and how it relates to complementary proposals.
- The weakest area is the affected-user case, which rests on performance measurements but does not establish that the stability problem is widespread or that existing workarounds are insufficient for a meaningful population.
- The most glaring omission is the failure to establish why a library solution will not do, since the paper asserts that views and external wrappers cannot constrain combination semantics but does not demonstrate that a non-standard library facility would be inadequate in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.00   accumulate 12.33   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.33  coordination 1.67  insufficiency 1.17  implementation 2.00
sample agreement: 65 of 77 section-criterion pairs unanimous (84%)
single-sample totals would have been: 11.50 / 12.50 / 11.00   (all 3 samples: 11.17)
headings: h2 3
on threshold: audience, vehicle, coordination, insufficiency
splits: motivation[4] 2/0/2  vehicle[4] 0/2/0  vehicle[8] 0/1/0  vehicle[11] 0/2/0
        coordination[4] 2/2/0  coordination[8] 2/2/0  coordination[9] 0/0/1
        insufficiency[8] 1/0/0  insufficiency[10] 0/1/0  insufficiency[11] 0/0/1
        implementation[5] 0/1/0  implementation[11] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 11 sections, strong in 8)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/0/2  -> 1.33
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      2/2/2  -> 2.00
  [7] Polls for LEWG Direction  (part 4 of 8)      2/2/2  -> 2.00
  [8] Polls for LEWG Direction  (part 5 of 8)      2/2/2  -> 2.00
  [9] Polls for LEWG Direction  (part 6 of 8)      2/2/2  -> 2.00
  [10] Polls for LEWG Direction  (part 7 of 8)      2/2/2  -> 2.00
  [11] Polls for LEWG Direction  (part 8 of 8)      2/2/2  -> 2.00
candidate 1 (found by 3 of 33 passes): C++ today offers two endpoints for reduction: `std::accumulate`: a specified left-fold expression, inherently sequential. `std::reduce`: scalable, but permits reassociation; for non-associative operations (e.g., floating-point addition), the returned value may differ across conforming evaluations.
candidate 2 (found by 3 of 33 passes): For non-associative `binary_op` (notably floating-point addition), different reduction topologies produce different results — this is precisely why `std::reduce` leaves its expression unspecified.
candidate 3 (found by 3 of 33 passes): This proposal is motivated by workloads where run-to-run stability matters, but existing parallel reductions are intentionally free to choose an evaluation order (and thus may vary with scheduling).
candidate 4 (found by 3 of 33 passes): In practice, many frameworks prioritize throughput by permitting schedule-dependent reduction structures; when operations are non-associative (e.g., floating-point addition), different reduction trees can yield different results.

## audience - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      0/0/0  -> 0.00
  [5] Polls for LEWG Direction  (part 2 of 8)      0/0/0  -> 0.00
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      0/0/0  -> 0.00
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      2/2/2  -> 2.00
candidate 1 (found by 2 of 33 passes): Their SIMD-optimized implementation achieves 89% of the throughput of unconstrained naïve summation when data is not resident in L1 cache (86% from L2, 90% streaming from memory)
candidate 2 (found by 1 of 33 passes): Their SIMD-optimized implementation achieves 89% of the throughput of unconstrained naïve summation when data is not resident in L1 cache (86% from L2, 90% streaming from memory), while providing the O(log N · ε) error bound of pairwise summation.

## prior_art - grade 2.00 (fired in 9 of 11 sections, strong in 8)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/2  -> 2.00
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      2/2/2  -> 2.00
  [7] Polls for LEWG Direction  (part 4 of 8)      2/2/2  -> 2.00
  [8] Polls for LEWG Direction  (part 5 of 8)      2/2/2  -> 2.00
  [9] Polls for LEWG Direction  (part 6 of 8)      2/2/2  -> 2.00
  [10] Polls for LEWG Direction  (part 7 of 8)      2/2/2  -> 2.00
  [11] Polls for LEWG Direction  (part 8 of 8)      2/2/2  -> 2.00
candidate 1 (found by 3 of 33 passes): The approach generalizes a technique already present in the Standard Library: `std::accumulate` obtains determinism by fixing its abstract expression structure, not by constraining execution strategy or floating-point arithmetic (see Appendix D).
candidate 2 (found by 3 of 33 passes): Recursive bisection (“balanced”) was considered as an alternative tree construction. It is documented in Appendix O (informative) for comparison and historical record.
candidate 3 (found by 3 of 33 passes): This canonical tree is near-balanced: it is exactly balanced when the number of participating operands is a power of two; otherwise it corresponds to iterative pairwise reduction with carry/absent operands as specified in §4.
candidate 4 (found by 3 of 33 passes): This proposal and P3375 are complementary: this paper fixes the *expression structure* (parenthesization and operand order) of a parallel reduction, while P3375 addresses the *evaluation model* (rounding, contraction, intermediate precision) for individual operations.

## vehicle - grade 1.33 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      0/2/0  -> 0.67
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      0/1/0  -> 0.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      0/2/0  -> 0.67
candidate 1 (found by 2 of 33 passes): Each vendor — Intel (CNR), NVIDIA (CUDA reduction libraries), and framework authors (PyTorch, Kokkos) — has independently built a proprietary determinism facility because the C++ Standard provides no canonical expression to target.
candidate 2 (found by 1 of 33 passes): This facility cannot be obtained merely as an external wrapper around existing standard components.
candidate 3 (found by 1 of 33 passes): As P2300 senders/receivers enable heterogeneous dispatch across CPUs, GPUs, and accelerators, this fragmentation worsens: a developer seeking deterministic reduction must use vendor-specific APIs on each target.
candidate 4 (found by 1 of 33 passes): This proposal standardizes the abstract expression structure (parenthesization and operand order).

## coordination - grade 1.67 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/0  -> 1.33
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      2/2/0  -> 1.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/1  -> 0.33
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Each vendor — Intel (CNR), NVIDIA (CUDA reduction libraries), and framework authors (PyTorch, Kokkos) — has independently built a proprietary determinism facility because the C++ Standard provides no canonical expression to target.
candidate 2 (found by 2 of 33 passes): This enables “golden result” workflows where a reference evaluation can act as a baseline for accelerator correctness verification.
candidate 3 (found by 1 of 33 passes): Heterogeneous execution. Modern C++ programs increasingly execute on heterogeneous platforms — CPU threads, GPU kernels, and accelerators within a single application.
candidate 4 (found by 1 of 33 passes): Modern C++ programs increasingly execute on heterogeneous platforms — CPU threads, GPU kernels, and accelerators within a single application.

## insufficiency - grade 1.17 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      0/0/0  -> 0.00
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      1/0/0  -> 0.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      0/1/0  -> 0.33
  [11] Polls for LEWG Direction  (part 8 of 8)      0/0/1  -> 0.33
candidate 1 (found by 3 of 33 passes): A range adaptor (View) can change which values are presented to an algorithm and in what iteration order they are produced. However, a view does not and cannot constrain the combination semantics of the consuming algorithm.
candidate 2 (found by 1 of 33 passes): In practice, users who require stronger reproducibility across configurations often adopt workarounds such as fixedtopology reductions, compensated/exact summation techniques, or application-level deterministic accumulation strategies — at non-trivial implementation cost.
candidate 3 (found by 1 of 33 passes): The reference implementation achieves throughput exceeding `std::reduce` while maintaining the canonical expression contract.
candidate 4 (found by 1 of 33 passes): The throughput and regret analyses above establish that neither candidate has a decisive performance advantage.

## implementation - grade 2.00  [binary: max] (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/2  -> 2.00
  [5] Polls for LEWG Direction  (part 2 of 8)      0/1/0  -> 0.33
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      1/1/1  -> 1.00
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      2/2/2  -> 2.00
  [11] Polls for LEWG Direction  (part 8 of 8)      1/2/1  -> 1.33
candidate 1 (found by 3 of 33 passes): The approach has been validated with working implementations across x86 AVX2, ARM NEON, and CUDA (Appendix K), producing expression-identical results for fixed topology coordinates
candidate 2 (found by 3 of 33 passes): Representative measurements appear in Appendix N (Performance feasibility). With proper SIMD optimization (8- block unrolling), the reference implementation indicates that the canonical expression structure can be evaluated at throughput comparable to unconstrained reduction
candidate 3 (found by 3 of 33 passes): A reference implementation is available at **[GB-x86-MT]**.
candidate 4 (found by 1 of 33 passes): This includes NVIDIA CUB’s deterministic reduction modes.

-->

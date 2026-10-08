Verdict: Strong to Excellent (11/14)

The paper offers solid support for the core technical motivation, prior art, implementation experience, and interoperability concerns, but its case is thinner on who specifically is affected, why the standard is the right venue, and why a library solution cannot suffice. The strongest material is concrete and comparative, while the weakest material relies on assertions that are not backed by evidence in the paper itself.

- The paper convincingly establishes that deterministic parallel reduction matters because existing standard facilities either serialize or permit schedule-dependent results for non-associative operations.
- It also demonstrates meaningful implementation experience, including cross-platform validation and performance data showing competitive throughput with pairwise error bounds.
- The discussion of prior art and alternatives is well grounded, showing how the proposed tree generalizes existing standard-library determinism and complements related proposals.
- The most glaring omission is the lack of established evidence for who is affected and why a library cannot address the need, leaving the standardization rationale asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 10.00   accumulate 11.33   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.00  coordination 1.67  insufficiency 1.33  implementation 2.00
sample agreement: 65 of 77 section-criterion pairs unanimous (84%)
single-sample totals would have been: 12.50 / 11.00 / 10.50   (all 3 samples: 11.00)
headings: h2 3
on threshold: audience, coordination, implementation
splits: motivation[3] 2/1/2  prior_art[5] 0/2/2  vehicle[5] 2/0/0  vehicle[8] 1/1/2
        coordination[4] 2/2/0  coordination[8] 2/0/2  coordination[9] 2/2/0
        insufficiency[5] 2/1/1  insufficiency[8] 2/2/0  implementation[5] 0/1/0
        implementation[8] 1/0/0  implementation[10] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 11 sections, strong in 9)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     2/1/2  -> 1.67
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/2  -> 2.00
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
candidate 1 (found by 3 of 33 passes): Their SIMD-optimized implementation achieves 89% of the throughput of unconstrained naïve summation when data is not resident in L1 cache (86% from L2, 90% streaming from memory)

## prior_art - grade 2.00 (fired in 9 of 11 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/2  -> 2.00
  [5] Polls for LEWG Direction  (part 2 of 8)      0/2/2  -> 1.33
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

## vehicle - grade 1.00 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      0/0/0  -> 0.00
  [5] Polls for LEWG Direction  (part 2 of 8)      2/0/0  -> 0.67
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      1/1/2  -> 1.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): This proposal standardizes the abstract expression structure (parenthesization and operand order).
candidate 2 (found by 1 of 33 passes): As P2300 senders/receivers enable heterogeneous dispatch across CPUs, GPUs, and accelerators, this fragmentation worsens: a developer seeking deterministic reduction must use vendor-specific APIs on each target.
candidate 3 (found by 1 of 33 passes): This proposal standardizes the abstract expression structure (parenthesization and operand order). Bitwise-identical results across different platforms, compilers, or architectures generally require that fixed expression structure and an equivalent floating-point evaluation environment.

## coordination - grade 1.67 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/0  -> 1.33
  [5] Polls for LEWG Direction  (part 2 of 8)      2/2/2  -> 2.00
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      2/0/2  -> 1.33
  [9] Polls for LEWG Direction  (part 6 of 8)      2/2/0  -> 1.33
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Each vendor — Intel (CNR), NVIDIA (CUDA reduction libraries), and framework authors (PyTorch, Kokkos) — has independently built a proprietary determinism facility because the C++ Standard provides no canonical expression to target.
candidate 2 (found by 2 of 33 passes): Modern C++ programs increasingly execute on heterogeneous platforms — CPU threads, GPU kernels, and accelerators within a single application.
candidate 3 (found by 2 of 33 passes): Because these presets are standard-fixed lane counts, a user can select the same preset when executing on different hardware or in different deployment environments.
candidate 4 (found by 1 of 33 passes): Matching those values across platforms validates both (a) correct expression structure (this proposal) and (b) sufficiently aligned floating-point environments (user responsibility).

## insufficiency - grade 1.33 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      0/0/0  -> 0.00
  [5] Polls for LEWG Direction  (part 2 of 8)      2/1/1  -> 1.33
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      2/2/0  -> 1.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      0/0/0  -> 0.00
  [11] Polls for LEWG Direction  (part 8 of 8)      0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A range adaptor (View) can change which values are presented to an algorithm and in what iteration order they are produced. However, a view does not and cannot constrain the combination semantics of the consuming algorithm.
candidate 2 (found by 2 of 33 passes): Kokkos does not generally specify a fixed reduction expression for `parallel_reduce` or `parallel_scan`: the documentation notes that neither concurrency nor order of execution are guaranteed.

## implementation - grade 2.00  [binary: max] (fired in 5 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Structure for Run-To-Run Consistency         0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Polls for LEWG Direction  (part 1 of 8)      2/2/2  -> 2.00
  [5] Polls for LEWG Direction  (part 2 of 8)      0/1/0  -> 0.33
  [6] Polls for LEWG Direction  (part 3 of 8)      0/0/0  -> 0.00
  [7] Polls for LEWG Direction  (part 4 of 8)      0/0/0  -> 0.00
  [8] Polls for LEWG Direction  (part 5 of 8)      1/0/0  -> 0.33
  [9] Polls for LEWG Direction  (part 6 of 8)      0/0/0  -> 0.00
  [10] Polls for LEWG Direction  (part 7 of 8)      2/0/2  -> 1.33
  [11] Polls for LEWG Direction  (part 8 of 8)      1/1/1  -> 1.00
candidate 1 (found by 3 of 33 passes): The approach has been validated with working implementations across x86 AVX2, ARM NEON, and CUDA (Appendix K), producing expression-identical results for fixed topology coordinates
candidate 2 (found by 3 of 33 passes): Their SIMD-optimized implementation achieves 89% of the throughput of unconstrained naïve summation when data is not resident in L1 cache (86% from L2, 90% streaming from memory), while providing the O(log N · ε) error bound of pairwise summation
candidate 3 (found by 1 of 33 passes): This includes NVIDIA CUB’s deterministic reduction modes.
candidate 4 (found by 1 of 33 passes): The demonstrators in Appendix K use a fixed seed and publish expected hex outputs for representative topology coordinates.

-->

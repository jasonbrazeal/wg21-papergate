Verdict: Adequate (5/14)

The paper offers a narrow but genuine foundation for its standardization case, centered on a clearly articulated motivation and a demonstrated implementation path. Its support is thinnest where it matters most for committee action: the paper does not establish who is affected, why the standard is the right venue, how the feature coordinates with existing machinery, or why a library solution cannot suffice.

- The strongest support comes from the implementation experience, with a working Clang fork and a compiler explorer link showing the feature in practice.
- The paper also establishes prior art and alternatives by tracing its lineage through P2484R0, P3380R1, P0424R2, and P0732R2.
- The most glaring omission is the absence of any established case for why the standard is needed, leaving the core standardization rationale unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.00   accumulate 5.00   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 27 of 28 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 3
on threshold: motivation, prior_art, implementation
splits: implementation[2] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): The goal here is to allow types to opt-in to being usable as constant template parameters in a way that’s forward-looking to containers as well.
candidate 2 (found by 3 of 12 passes): Ultimately, the whole problem of how to opt an arbitrary type with non-public subobjects into being usable as a constant template parameter is about this question of how to produce the template parameter object.

## audience - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This is a follow-up to [[P2484R0] (Extending class types as non-type template parameters)](https://wg21.link/p2484r0) and [[P3380R1] (Extending support for class types as non-type template parameters)](https://wg21.link/p3380r1)
candidate 2 (found by 2 of 12 passes): Now, [[P0424R2] (String literals as non-type template parameters)] already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)] in the C++20 timeframe.
candidate 3 (found by 1 of 12 passes): Now, [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/1  -> 0.33
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This has been implemented in [my fork](https://github.com/brevzin/llvm-project/commit/750c1763c183d9fb1bc0e6bb1c6a4adde11c9094) of Clang, and you can see it on [compiler explorer](https://compiler-explorer.com/z/WbYjs5EaK).
candidate 2 (found by 1 of 12 passes): Dan Katz’s experimentation that eventually led to the `std::define_static_meow` functions in [[P3491R3] (`define_static_{string,object,array}`)](https://wg21.link/p349143)

-->

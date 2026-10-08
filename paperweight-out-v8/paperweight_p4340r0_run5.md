Verdict: Adequate (6/14)

The paper gives a clear account of the problem it is trying to solve and shows real implementation experience, but it leaves several parts of the standardization case underdeveloped, particularly around who is affected and why a library solution cannot suffice. The strongest support comes from its engagement with prior proposals and its working implementation, while the thinnest areas are the absence of an affected-user discussion and any argument ruling out non-standard approaches.

- The paper establishes why the problem matters by tying it to the forward-looking goal of allowing types with non-public subobjects to work as constant template parameters.
- It credibly grounds itself in prior art, including P2484R0, P3380R1, P0424R2, and P0732R2, and it points to a concrete Clang implementation available on Compiler Explorer.
- The claim that standardization is the only way to ensure the desired property is asserted rather than demonstrated, leaving the necessity of a standard change weakly supported.
- The paper does not establish who is affected by the problem or why a library-only solution would be inadequate, which are notable gaps in the case for standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 6.33   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 27 of 28 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.50 / 6.50   (all 3 samples: 6.33)
headings: h2 3
on threshold: motivation, implementation
splits: vehicle[3] 0/1/1
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

## prior_art - grade 2.00 (fired in 2 of 4 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This is a follow-up to [[P2484R0] (Extending class types as non-type template parameters)](https://wg21.link/p2484r0) and [[P3380R1] (Extending support for class types as non-type template parameters)](https://wg21.link/p3380r1) ... and is a new solution to that problem building upon three insights
candidate 2 (found by 2 of 12 passes): [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.
candidate 3 (found by 1 of 12 passes): Previous papers in this space brought up two examples: - a `Fraction` type that is only in lowest terms - a `SmallString` container that doesn’t care about trailing data.

## vehicle - grade 0.33 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/1/1  -> 0.67
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): This is really the only way to ensure this property, and is the requirement for this to be allowed to work, so we should do it.

## coordination - grade 0.50 (fired in 1 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     1/1/1  -> 1.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This is really the only way to ensure this property, and is the requirement for this to be allowed to work, so we should do it.

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This has been implemented in [my fork](https://github.com/brevzin/llvm-project/commit/750c1763c183d9fb1bc0e6bb1c6a4adde11c9094) of Clang, and you can see it on [compiler explorer](https://compiler-explorer.com/z/WbYjs5EaK).

-->

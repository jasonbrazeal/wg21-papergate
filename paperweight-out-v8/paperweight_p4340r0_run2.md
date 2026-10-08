Verdict: Adequate (6/14)

The paper offers some concrete grounding for its standardization case, but much of the surrounding argument is asserted rather than demonstrated. The strongest support is the existence of a working implementation, while the thinnest areas concern who is actually affected and why the problem cannot be solved outside the standard.

- The paper establishes implementation experience through a Clang fork and a compiler explorer link, which gives the proposal a tangible basis.
- The motivation is established in general terms as enabling types to opt into use as constant template parameters.
- The discussion of prior art and coordination is claimed but not established, since the paper references earlier proposals without fully showing how this one resolves their limitations or fits with existing practice.
- The most glaring omissions are any account of who is affected, why the standard is the right venue, and why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.00   accumulate 5.83   max 8.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 27 of 28 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 6.50 / 5.50   (all 3 samples: 5.83)
headings: h2 3
on threshold: motivation, prior_art, coordination, implementation
splits: prior_art[2] 0/2/0
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

## prior_art - grade 1.33 (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/2/0  -> 0.67
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): Now, [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.
candidate 2 (found by 1 of 12 passes): This is a follow-up to [[P2484R0] (Extending class types as non-type template parameters)](https://wg21.link/p2484r0) and [[P3380R1] (Extending support for class types as non-type template parameters)](https://wg21.link/p3380r1) ... and is a new solution to that problem building upon three insights
candidate 3 (found by 1 of 12 passes): [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): This is really the only way to ensure this property, and is the requirement for this to be allowed to work, so we should do it.
candidate 2 (found by 1 of 12 passes): The reason for this is that we do not ensure that `"hello"` is the same exact pointer across all translation units (and we will not start doing this now), and the result is that given a class template like:

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

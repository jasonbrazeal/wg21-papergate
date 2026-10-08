Verdict: Adequate (6/14)

The paper gives a reasonably grounded account of why the problem matters and how it relates to earlier proposals, and it offers concrete implementation evidence, but it leaves several parts of the standardization case largely asserted rather than demonstrated. The thinnest support concerns who is affected, why a library solution is insufficient, and how the proposed behavior coordinates with existing rules.

- The strongest support is the implementation experience, with a working Clang fork and a compiler explorer link showing the idea in practice.
- The paper also situates itself credibly in prior art, tracing the idea back through earlier proposals and explaining how the C++20 direction diverged from an older approach.
- The discussion of why the standard is needed rests mainly on an assertion that this is the only way to ensure the desired property, without establishing that claim.
- The most glaring omission is the absence of any account of who is affected by the problem or why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 5.67   accumulate 6.00   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.67  vehicle 0.50  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 25 of 28 section-criterion pairs unanimous (89%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 3
on threshold: motivation, prior_art, implementation
splits: prior_art[2] 2/2/0  coordination[3] 0/0/2  implementation[2] 1/0/1
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

## prior_art - grade 1.67 (fired in 2 of 4 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/0  -> 1.33
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): This is a follow-up to [[P2484R0] (Extending class types as non-type template parameters)](https://wg21.link/p2484r0) and [[P3380R1] (Extending support for class types as non-type template parameters)](https://wg21.link/p3380r1) ... and is a new solution to that problem building upon three insights
candidate 2 (found by 2 of 12 passes): [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.
candidate 3 (found by 1 of 12 passes): Now, [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) already proposed the solution to this problem. Except that paper was dropped in favor of the more general [[P0732R2] (Class Types in Non-Type Template Parameters)](https://wg21.link/p0732r2) in the C++20 timeframe.

## vehicle - grade 0.50 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     1/1/1  -> 1.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This is really the only way to ensure this property, and is the requirement for this to be allowed to work, so we should do it.

## coordination - grade 0.33 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design                                     0/0/2  -> 0.67
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): That is, for all class types that are today usable as constant template parameters, this comparison holds (let’s agree to ignore that I’m not using `std::addressof`):

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
  [2] 1 Introduction                               1/0/1  -> 0.67
  [3] 2 Design                                     2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): This has been implemented in [my fork](https://github.com/brevzin/llvm-project/commit/750c1763c183d9fb1bc0e6bb1c6a4adde11c9094) of Clang, and you can see it on [compiler explorer](https://compiler-explorer.com/z/WbYjs5EaK).
candidate 2 (found by 2 of 12 passes): Dan Katz’s experimentation that eventually led to the `std::define_static_meow` functions in [[P3491R3] (`define_static_{string,object,array}`)](https://wg21.link/p349143)

-->

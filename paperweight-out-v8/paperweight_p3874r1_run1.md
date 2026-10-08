Verdict: Adequate to Strong (7/14)

The paper makes a credible case that memory safety is a pressing problem for C++ and that a syntactically explicit, UB-free subset is a plausible direction, but it leaves several essential standardization questions largely unaddressed. The strongest support is conceptual, while the thinnest areas concern how such a subset would fit into the existing standard, interoperate with surrounding code, and be delivered without a full library replacement.

- The paper clearly establishes why memory safety matters and that a subset-of-superset approach has meaningful precedent in Rust and Swift.
- The discussion of a weird machine and the need to replace UB-prone features gives the proposal a coherent technical motivation.
- The paper claims broad industry relevance and implementation experience, but does not substantiate who is affected or demonstrate that the Circle implementation validates the standardization path.
- The paper does not establish coordination with existing C++ code, interoperability requirements, or why the necessary changes cannot be achieved through a library rather than core language standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 24. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 112 of 119 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 8.00 / 7.00   (all 3 samples: 6.83)
headings: h2 16
on threshold: none
splits: motivation[9] 2/1/1  motivation[11] 2/0/2  prior_art[5] 2/1/0  vehicle[8] 2/2/0
        vehicle[9] 0/1/1  implementation[9] 0/2/2  implementation[14] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 17 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 2/1/1  -> 1.33
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             2/0/2  -> 1.33
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 1/1/1  -> 1.00
  [15] 34 Note that self in this case is a usize... 1/1/1  -> 1.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Consistently, the observation is made that memory-safety bugs lead to critical security vulnerabilities and that the use of memory-safe programming languages can eliminate them.
candidate 2 (found by 3 of 51 passes): Given the recommendations to prefer memory-safe languages, how should WG21 respond?
candidate 3 (found by 3 of 51 passes): Any program which can exhibit UB under some inputs provides no guarantees whatsoever.
candidate 4 (found by 3 of 51 passes): Perhaps the greatest concern with regards to a memory-safe C++ is that it will require an entire new standard library before it is useful.

## audience - grade 0.50 (fired in 1 of 17 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 1/1/1  -> 1.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++25.

## prior_art - grade 2.00 (fired in 8 of 17 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   2/1/0  -> 1.00
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 1/1/1  -> 1.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Rust is consistently described as a memory-safe language while C++ is not
candidate 2 (found by 3 of 51 passes): In contrast to the abstract machine which describes the semantics of a programming language, a weird machine represents a computational environment which is unconstrained by language semantics and therefore vulnerable to exploitation.
candidate 3 (found by 3 of 51 passes): The subset-of-superset approach is pursued to the same end as Rust and Swift, resulting in a useful subset with no UB.
candidate 4 (found by 3 of 51 passes): Swift takes a different approach based on automatic reference counting, but this entails additional runtime overhead.

## vehicle - grade 1.00 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/0  -> 1.33
  [9] 22 The Circle Language also uses the same... 0/1/1  -> 0.67
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): This proposal is explicitly about the definition of a memory-safe language and the decision to pursue this goal for C++.
candidate 2 (found by 1 of 51 passes): This paper proposes a subset-of-superset strategy19 for C++ to achieve memory safety such that: 1. The subset is syntactically explicit and well-defined; no undefined behavior can be exhibited within it and only code within the subset may be accessed.
candidate 3 (found by 1 of 51 passes): This is why it is necessary to add new features that *replace* those which must be restricted for the sake of avoiding UB.

## coordination - grade 0.00 (fired in 0 of 17 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 17 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 17 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 0/2/2  -> 1.33
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/2/2  -> 1.33
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): as of writing, [this is indeed how the Rust implementation works](https://github.com/rust-lang/rust/blob/873b4beb0cc726493b94c8ef21f68795c04fbbc1/library/core/src/slice/index.rs#L218-L225)
candidate 2 (found by 1 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/)
candidate 3 (found by 1 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/) which is demonstrative of the fundamental effort to apply this design to C++26.

-->

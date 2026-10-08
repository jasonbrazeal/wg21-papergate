Verdict: Strong (8/14)

The paper offers substantial support for the relevance, affected audience, prior art, and implementation experience behind its proposal, but it leaves the case for why this work belongs in the C++ standard itself largely asserted rather than demonstrated. The thinnest parts concern coordination with existing or adjacent standardization efforts and why a library-based approach would be insufficient.

- The strongest support comes from the paper’s grounding in real-world memory-safety concerns, user demand, and demonstrated implementation experience in both Rust and Circle.
- The discussion of prior art and alternatives is well developed, showing awareness of Rust, Swift, and the broader safety landscape.
- The argument for standardization specifically is only claimed, not established, since the paper asserts the necessity of new language features without fully showing why existing mechanisms cannot serve.
- The most glaring omission is the absence of any discussion of coordination and interoperability with other standardization efforts or existing C++ features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 5 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 20. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 7.67   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 111 of 119 section-criterion pairs unanimous (93%)
single-sample totals would have been: 8.50 / 7.50 / 8.50   (all 3 samples: 8.17)
headings: h2 16
on threshold: audience
splits: motivation[9] 1/2/2  motivation[11] 1/0/1  motivation[15] 1/0/1  audience[9] 1/1/2
        prior_art[5] 0/0/2  prior_art[9] 0/2/2  vehicle[8] 1/0/1  vehicle[9] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 17 sections, strong in 3)
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
  [9] 22 The Circle Language also uses the same... 1/2/2  -> 1.67
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             1/0/1  -> 0.67
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 1/1/1  -> 1.00
  [15] 34 Note that self in this case is a usize... 1/0/1  -> 0.67
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Consistently, the observation is made that memory-safety bugs lead to critical security vulnerabilities and that the use of memory-safe programming languages can eliminate them.
candidate 2 (found by 3 of 51 passes): Given the recommendations to prefer memory-safe languages, how should WG21 respond?
candidate 3 (found by 3 of 51 passes): Meanwhile, memory-safe languages have demonstrated real-world benefits significant enough for organizations with some of the world’s largest
candidate 4 (found by 3 of 51 passes): Clearly, in order to deliver memory-safety guarantees at the program level, memory-safe APIs must be sound.

## audience - grade 1.67 (fired in 2 of 17 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 1/1/2  -> 1.33
  [10] Conclusion                                   2/2/2  -> 2.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++25.
candidate 2 (found by 2 of 51 passes): Especially in light of [the clear signal from users that such features are](https://isocpp.org/files/papers/CppDevSurvey-2025-summary.pdf) [highly desired](https://isocpp.org/files/papers/CppDevSurvey-2025-summary.pdf)
candidate 3 (found by 1 of 51 passes): the clear signal from users that such features are highly desired

## prior_art - grade 2.00 (fired in 9 of 17 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/2  -> 0.67
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 0/2/2  -> 1.33
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 1/1/1  -> 1.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): In contrast to the abstract machine which describes the semantics of a programming language, a weird machine represents a computational environment which is unconstrained by language semantics and therefore vulnerable to exploitation.
candidate 2 (found by 3 of 51 passes): The subset-of-superset approach is pursued to the same end as Rust and Swift, resulting in a useful subset with no UB.
candidate 3 (found by 3 of 51 passes): Swift takes a different approach based on automatic reference counting, but this entails additional runtime overhead.
candidate 4 (found by 3 of 51 passes): See [P3578 R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3578r1.pdf) “What is “Safety”?”, and the [Safety-Critical Rust Consortium](https://rustfoundation.org/safety-critical-rust-consortium/) for more.

## vehicle - grade 0.50 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 1/0/1  -> 0.67
  [9] 22 The Circle Language also uses the same... 1/0/0  -> 0.33
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 1 of 51 passes): This is why it is necessary to add new features that *replace* those which must be restricted for the sake of avoiding UB.
candidate 2 (found by 1 of 51 passes): This is why it is necessary to add new features that replace those which must be restricted for the sake of avoiding UB.
candidate 3 (found by 1 of 51 passes): The reality of decades of legacy C++ existing is unavoidable, but it does not preclude the value of adding memory-safety for new code.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 17 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 2/2/2  -> 2.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): as of writing, [this is indeed how the Rust implementation works](https://github.com/rust-lang/rust/blob/873b4beb0cc726493b94c8ef21f68795c04fbbc1/library/core/src/slice/index.rs#L218-L225)
candidate 2 (found by 2 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/) which is demonstrative of the fundamental effort to apply this design to C++26.
candidate 3 (found by 1 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/)

-->

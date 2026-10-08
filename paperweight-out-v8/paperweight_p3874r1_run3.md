Verdict: Adequate to Strong (6/14)

The paper offers a reasonably grounded motivation for pursuing a memory-safe subset of C++, and it shows awareness of relevant prior work, but it leaves several essential parts of the standardization case largely unargued. The thinnest support concerns coordination with the existing standard, why a library-based approach would be insufficient, and evidence that the proposed design can be implemented and adopted in practice.

- The strongest part of the paper is its explanation of why memory safety matters, supported by references to industry, academic, and government recommendations and the consequences of undefined behavior.
- The discussion of prior art is also solid, situating the subset-of-superset approach alongside Rust and Swift and pointing to related safety work.
- The paper claims broad user demand and relevant implementation experience, but it does not substantiate either with concrete evidence beyond a binary implementation and a passing reference to Rust internals.
- Most glaringly, the paper does not establish why standardization is the right vehicle, how the feature would coordinate with the existing standard, or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 22. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 106 of 119 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.00 / 8.00 / 6.50   (all 3 samples: 6.50)
headings: h2 16
on threshold: none
splits: motivation[2] 2/2/0  motivation[5] 2/2/0  motivation[9] 2/2/1  motivation[10] 1/2/1
        motivation[11] 0/0/2  motivation[14] 0/1/2  motivation[15] 1/0/0  audience[10] 0/2/0
        prior_art[5] 2/0/0  prior_art[6] 0/2/2  vehicle[8] 1/1/0  implementation[9] 2/0/2
        implementation[14] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 17 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/0  -> 1.33
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   2/2/0  -> 1.33
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 2/2/1  -> 1.67
  [10] Conclusion                                   1/2/1  -> 1.33
  [11] Appendix: Encapsulating Unsafety             0/0/2  -> 0.67
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/1/2  -> 1.00
  [15] 34 Note that self in this case is a usize... 1/0/0  -> 0.33
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Consistently, the observation is made that memory-safety bugs lead to critical security vulnerabilities and that the use of memory-safe programming languages can eliminate them.
candidate 2 (found by 3 of 51 passes): Any program which can exhibit UB under some inputs provides no guarantees whatsoever.
candidate 3 (found by 3 of 51 passes): Perhaps the greatest concern with regards to a memory-safe C++ is that it will require an entire new standard library before it is useful.
candidate 4 (found by 2 of 51 passes): In recent years there have been numerous recommendations from industry, academia and government to prefer “memory-safe languages”.

## audience - grade 0.83 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [10] Conclusion                                   0/2/0  -> 0.67
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++25.
candidate 2 (found by 1 of 51 passes): the clear signal from users that such features are highly desired

## prior_art - grade 2.00 (fired in 8 of 17 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   2/0/0  -> 0.67
  [6] What is a memory-safe language?              0/2/2  -> 1.33
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
candidate 1 (found by 3 of 51 passes): In recent years there have been numerous recommendations from industry, academia and government to prefer “memory-safe languages”1.
candidate 2 (found by 3 of 51 passes): The subset-of-superset approach is pursued to the same end as Rust and Swift, resulting in a useful subset with no UB.
candidate 3 (found by 3 of 51 passes): Swift takes a different approach based on automatic reference counting, but this entails additional runtime overhead.
candidate 4 (found by 3 of 51 passes): See [P3578 R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3578r1.pdf) “What is “Safety”?”, and the [Safety-Critical Rust Consortium](https://rustfoundation.org/safety-critical-rust-consortium/) for more.

## vehicle - grade 0.33 (fired in 1 of 17 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 1/1/0  -> 0.67
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): This is why it is necessary to add new features that replace those which must be restricted for the sake of avoiding UB.

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
  [9] 22 The Circle Language also uses the same... 2/0/2  -> 1.33
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/2/0  -> 0.67
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/) which is demonstrative of the fundamental effort to apply this design to C++26.
candidate 2 (found by 1 of 51 passes): as of writing, [this is indeed how the Rust implementation works](https://github.com/rust-lang/rust/blob/873b4beb0cc726493b94c8ef21f68795c04fbbc1/library/core/src/slice/index.rs#L218-L225)

-->

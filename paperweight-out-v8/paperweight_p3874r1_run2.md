Verdict: Adequate (7/14)

The paper gives a credible account of why memory safety matters and shows familiarity with existing approaches, but it does not yet make a complete case that this particular design belongs in the C++ standard. The thinnest parts concern how the proposed features would work with existing C++ code and tooling, and whether the demonstrated implementation is enough to justify standardization.

- The strongest support is the clear motivation connecting undefined behavior to security vulnerabilities and the need for sound memory-safe APIs.
- The paper also adequately situates its subset-of-superset strategy among prior efforts such as Rust and Swift.
- It asserts user demand and implementation experience, but offers little concrete evidence of affected users or deployment beyond a single demonstrative implementation.
- The most glaring omission is any discussion of coordination and interoperability with existing C++ code, libraries, or toolchains.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 26. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 110 of 119 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.67)
headings: h2 16
on threshold: none
splits: motivation[7] 2/2/1  motivation[9] 1/2/1  motivation[10] 2/1/2  audience[9] 2/1/1
        audience[10] 2/0/0  prior_art[5] 0/0/2  prior_art[15] 2/1/1  vehicle[8] 1/1/0
        implementation[9] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 17 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    2/2/1  -> 1.67
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 1/2/1  -> 1.33
  [10] Conclusion                                   2/1/2  -> 1.67
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 1/1/1  -> 1.00
  [15] 34 Note that self in this case is a usize... 1/1/1  -> 1.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Consistently, the observation is made that memory-safety bugs lead to critical security vulnerabilities and that the use of memory-safe programming languages can eliminate them.
candidate 2 (found by 3 of 51 passes): Given the recommendations to prefer memory-safe languages, how should WG21 respond?
candidate 3 (found by 3 of 51 passes): Any program which can exhibit UB under some inputs provides no guarantees whatsoever.
candidate 4 (found by 3 of 51 passes): Clearly, in order to deliver memory-safety guarantees at the program level, memory-safe APIs must be sound.

## audience - grade 1.00 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 0/0/0  -> 0.00
  [9] 22 The Circle Language also uses the same... 2/1/1  -> 1.33
  [10] Conclusion                                   2/0/0  -> 0.67
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++25.
candidate 2 (found by 1 of 51 passes): the clear signal from users that such features are highly desired

## prior_art - grade 2.00 (fired in 8 of 17 sections, strong in 3)
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
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 2/1/1  -> 1.33
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): In recent years there have been numerous recommendations from industry, academia and government to prefer “memory-safe languages”1.
candidate 2 (found by 3 of 51 passes): In contrast to the abstract machine which describes the semantics of a programming language, a weird machine represents a computational environment which is unconstrained by language semantics and therefore vulnerable to exploitation.
candidate 3 (found by 3 of 51 passes): The subset-of-superset approach is pursued to the same end as Rust and Swift, resulting in a useful subset with no UB.
candidate 4 (found by 3 of 51 passes): Swift takes a different approach based on automatic reference counting, but this entails additional runtime overhead.

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
candidate 1 (found by 1 of 51 passes): This paper proposes a subset-of-superset strategy19 for C++ to achieve memory safety such that:
candidate 2 (found by 1 of 51 passes): This is why it is necessary to add new features that *replace* those which must be restricted for the sake of avoiding UB.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 17 sections, strong in 0)
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
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): Circle has a functional implementation available in [binary form](https://www.circle-lang.org/site/download/) and on [Compiler](https://circle.godbolt.org/) [Explorer](https://circle.godbolt.org/) which is demonstrative of the fundamental effort to apply this design to C++26.

-->

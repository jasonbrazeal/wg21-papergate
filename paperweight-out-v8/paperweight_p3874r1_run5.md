Verdict: Adequate to Strong (8/14)

The paper offers solid grounding in the problem of memory safety and in prior approaches such as Rust and Swift, but its case for standardization rests heavily on assertions about user demand and the necessity of language-level change rather than demonstrated evidence. The thinnest areas are interoperability, coordination with existing ecosystems, and why a library-level solution cannot suffice.

- The strongest support comes from the paper’s treatment of prior art and alternatives, where it clearly situates its subset-of-superset approach against Rust and Swift and acknowledges the costs of unsafe code.
- The paper also establishes why the issue matters, connecting memory-safety bugs to security vulnerabilities and the limits of undefined behavior.
- Its claims about who is affected rely on broad statements about Rust’s adoption and user desire without supporting data or concrete testimony.
- The most glaring omission is the absence of any discussion of coordination and interoperability with existing C++ code, tooling, or standards processes, leaving a central practical question unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 25. Replies missing: 0. Sections: 17. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 7.50   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 113 of 119 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.50 / 7.50 / 6.50   (all 3 samples: 7.50)
headings: h2 16
on threshold: implementation
splits: motivation[5] 2/0/2  motivation[9] 2/1/2  audience[10] 2/0/0  prior_art[9] 2/0/2
        vehicle[8] 1/1/0  vehicle[9] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 17 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   2/0/2  -> 1.33
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 2/1/2  -> 1.67
  [10] Conclusion                                   1/1/1  -> 1.00
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
candidate 4 (found by 3 of 51 passes): Perhaps the greatest concern with regards to a memory-safe C++ is that it will require an entire new standard library before it is useful.

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
  [10] Conclusion                                   2/0/0  -> 0.67
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++25.
candidate 2 (found by 1 of 51 passes): Rust has 10 years of experience in deployment at scale and significant adoption across nearly all the core industries as C++.
candidate 3 (found by 1 of 51 passes): the clear signal from users that such features are highly desired

## prior_art - grade 2.00 (fired in 8 of 17 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              2/2/2  -> 2.00
  [7] Should C++ become a memory-safe language?    1/1/1  -> 1.00
  [8] 16 See “Secure by Design: Google’s Pe... 2/2/2  -> 2.00
  [9] 22 The Circle Language also uses the same... 2/0/2  -> 1.33
  [10] Conclusion                                   1/1/1  -> 1.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 1/1/1  -> 1.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): The subset-of-superset approach is pursued to the same end as Rust and Swift, resulting in a useful subset with no UB.
candidate 2 (found by 3 of 51 passes): Swift takes a different approach based on automatic reference counting, but this entails additional runtime overhead.
candidate 3 (found by 3 of 51 passes): For a full treatment of the challenges associated with writing correct memory-unsafe code in Rust, see *[The Rustonomicon](https://doc.rust-lang.org/stable/nomicon/)* and *[Rust's Unsafe Code Guidelines](https://rust-lang.github.io/unsafe-code-guidelines)* Reference.
candidate 4 (found by 2 of 51 passes): Rust is consistently described as a memory-safe language while C++ is not

## vehicle - grade 0.67 (fired in 2 of 17 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CISA: “The Urgent Need for Memory Saf... 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] What is a memory-safe language?              0/0/0  -> 0.00
  [7] Should C++ become a memory-safe language?    0/0/0  -> 0.00
  [8] 16 See “Secure by Design: Google’s Pe... 1/1/0  -> 0.67
  [9] 22 The Circle Language also uses the same... 1/1/0  -> 0.67
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 0/0/0  -> 0.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 2 of 51 passes): This proposal is explicitly about the definition of a memory-safe language and the decision to pursue this goal for C++.
candidate 2 (found by 1 of 51 passes): This is why it is necessary to add new features that *replace* those which must be restricted for the sake of avoiding UB.
candidate 3 (found by 1 of 51 passes): This is why it is necessary to add new features that replace those which must be restricted for the sake of avoiding UB.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 17 sections, strong in 1)  (ON THRESHOLD)
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
  [9] 22 The Circle Language also uses the same... 0/0/0  -> 0.00
  [10] Conclusion                                   0/0/0  -> 0.00
  [11] Appendix: Encapsulating Unsafety             0/0/0  -> 0.00
  [12] 28 “Rust in Android: move fast and fix ... 0/0/0  -> 0.00
  [13] 29 See “Request for Information: Open-S... 0/0/0  -> 0.00
  [14] 32 Compilers have bugs too, of course. Th... 2/2/2  -> 2.00
  [15] 34 Note that self in this case is a usize... 0/0/0  -> 0.00
  [16] Acknowledgements                             0/0/0  -> 0.00
  [17] Revision History                             0/0/0  -> 0.00
candidate 1 (found by 3 of 51 passes): as of writing, [this is indeed how the Rust implementation works](https://github.com/rust-lang/rust/blob/873b4beb0cc726493b94c8ef21f68795c04fbbc1/library/core/src/slice/index.rs#L218-L225)

-->

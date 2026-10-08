Verdict: Adequate (6/14)

The paper offers some useful groundwork for its standardization request, particularly in explaining why the issue matters and in surveying prior approaches, but it leaves several essential parts of the case largely unaddressed. The thinnest areas concern who is actually affected, how the change would interoperate with existing practice, and why a library solution is insufficient.

- The strongest support is the paper’s explanation of why out-of-thin-air behavior matters and its acknowledgment that the current standard leaves key terms undefined.
- The discussion of prior art and alternatives is also well established, showing familiarity with earlier models and existing compiler switches.
- The request for a non-normative change is asserted but not backed by a clear argument that a standard change is the right vehicle.
- The most glaring omission is the absence of any established evidence about who is affected, coordination with implementations, or why a library approach cannot address the concern.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 4 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 6.00   accumulate 5.50   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 101 of 105 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 14
on threshold: none
splits: motivation[5] 1/1/2  motivation[12] 0/0/1  prior_art[9] 1/0/0  prior_art[11] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                2/2/2  -> 2.00
  [4] History                                      2/2/2  -> 2.00
  [5] 2 OOTA, Semantic Dependencies, and           1/1/2  -> 1.33
  [6] 3 What is an Execution?                      1/1/1  -> 1.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 1/1/1  -> 1.00
  [9] 4.2 Global Optimization Can Destroy Depen... 2/2/2  -> 2.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 2/2/2  -> 2.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/1  -> 0.33
  [13] 7 Issues and Refinements                     1/1/1  -> 1.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 45 passes): Attempts to create memory models that forbid out-of-thin-air (OOTA) behaviors of C++ memory_order_relaxed accesses have been either non-executable, complex, or unloved by implementers.
candidate 2 (found by 3 of 45 passes): Unfortunately, the standard does not explain what the phrase “depend on” in the quotation above really means.
candidate 3 (found by 3 of 45 passes): In areas that are not well settled or where users might reasonably want to resist the dictates of the standard, compilers often provide switches to override their default behaviors.
candidate 4 (found by 3 of 45 passes): Such a transformation complies with the loose C++ standard, even though the resulting executable file would produce an unintuitive OOTA outcome every time it runs, even if relaxed loads are ordered before relaxed stores!

## audience - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/0  -> 0.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 11 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                2/2/2  -> 2.00
  [4] History                                      2/2/2  -> 2.00
  [5] 2 OOTA, Semantic Dependencies, and           2/2/2  -> 2.00
  [6] 3 What is an Execution?                      1/1/1  -> 1.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 1/1/1  -> 1.00
  [9] 4.2 Global Optimization Can Destroy Depen... 1/0/0  -> 0.33
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 1/1/1  -> 1.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/1/1  -> 0.67
  [12] 5 Hardware Dependencies, Instruction         1/1/1  -> 1.00
  [13] 7 Issues and Refinements                     2/2/2  -> 2.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 45 passes): We show that these models’ constraints prevent OOTA cycles from occurring in undefined-behaviorfree C++ programs running on such implementations, provided the cycles involve only volatile atomics.
candidate 2 (found by 3 of 45 passes): P0442R0 (“Out-of-Thin-Air Execution is Vacuous”) [26] provided a decision procedure for distinguishing between reordering and OOTA, using a perturbation method based on the insight that OOTA cycles are fixed-point computations
candidate 3 (found by 3 of 45 passes): Expanding on earlier discussions [6], as long as y is zero, changes in the value of x will not cause a change in the value stored to z.
candidate 4 (found by 3 of 45 passes): An example is GCC’s -funsigned-char command-line argument, which causes it to treat variables of type char as unsigned (see Section 2.2.9).

## vehicle - grade 0.50 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                1/1/1  -> 1.00
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/0  -> 0.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): As a consequence, we are asking for only for a small non-normative change to the standard.

## coordination - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/0  -> 0.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                0/0/0  -> 0.00
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/0  -> 0.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 15 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                1/1/1  -> 1.00
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         1/1/1  -> 1.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): We know of no instances of OOTA behavior in real C++ implementations.
candidate 2 (found by 2 of 45 passes): Note well that these compilers’ current analysis suffices.
candidate 3 (found by 1 of 45 passes): These exercises use the following steps: 1. Identify the potential semantic dependencies of inter- est. 2. Compile the code to assembly language, either using a real compiler or conceptually.

-->

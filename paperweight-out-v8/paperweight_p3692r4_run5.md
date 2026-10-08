Verdict: Adequate (6/14)

The paper offers solid grounding for why the out-of-thin-air problem matters and for the prior work it builds on, but its case for standardization rests on several assertions that are not backed up with evidence, particularly around real-world impact and implementability. The thinnest support is where the paper asks the committee to accept claims about compiler behavior and the absence of observed problems without demonstration.

- The strongest support is the explanation of why the problem matters, including the difficulty of forbidding out-of-thin-air behavior and the role of compiler transformations in destroying dependencies.
- The paper also establishes meaningful prior art and alternatives, showing that the approach follows from earlier discussions and formal insights about volatile environments and fixed-point cycles.
- The claim that no out-of-thin-air behavior occurs in real implementations is repeated but never substantiated, leaving the affected-user case unproven.
- The most glaring omission is the absence of any coordination or interoperability discussion, which leaves open how the proposed non-normative change would fit with existing practice and other standards work.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 6.33   accumulate 5.50   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.17  implementation 0.67
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 6.00 / 4.50   (all 3 samples: 5.50)
headings: h2 14
on threshold: none
splits: motivation[5] 2/1/1  motivation[9] 2/2/0  audience[3] 0/1/0  prior_art[3] 1/1/2
        prior_art[9] 1/1/0  insufficiency[10] 1/0/0  implementation[3] 1/1/0
        implementation[12] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 15 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                2/2/2  -> 2.00
  [4] History                                      2/2/2  -> 2.00
  [5] 2 OOTA, Semantic Dependencies, and           2/1/1  -> 1.33
  [6] 3 What is an Execution?                      1/1/1  -> 1.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 1/1/1  -> 1.00
  [9] 4.2 Global Optimization Can Destroy Depen... 2/2/0  -> 1.33
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 2/2/2  -> 2.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         1/1/1  -> 1.00
  [13] 7 Issues and Refinements                     1/1/1  -> 1.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 45 passes): Attempts to create memory models that forbid out-of-thin-air (OOTA) behaviors of C++ memory_order_relaxed accesses have been either non-executable, complex, or unloved by implementers.
candidate 2 (found by 3 of 45 passes): The primary difficulty lies in the fact that the code transformations performed by optimizing compilers can destroy syntactic dependencies, possibly even semantic ones (depending on one’s definition).
candidate 3 (found by 3 of 45 passes): In areas that are not well settled or where users might reasonably want to resist the dictates of the standard, compilers often provide switches to override their default behaviors.
candidate 4 (found by 3 of 45 passes): Inventing atomic loads can also destroy dependencies.

## audience - grade 0.17 (fired in 1 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                0/1/0  -> 0.33
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
candidate 1 (found by 1 of 45 passes): we know of no instances of OOTA behavior in real C++ implementations.

## prior_art - grade 2.00 (fired in 10 of 15 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                1/1/2  -> 1.33
  [4] History                                      2/2/2  -> 2.00
  [5] 2 OOTA, Semantic Dependencies, and           2/2/2  -> 2.00
  [6] 3 What is an Execution?                      1/1/1  -> 1.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 1/1/1  -> 1.00
  [9] 4.2 Global Optimization Can Destroy Depen... 1/1/0  -> 0.67
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 1/1/1  -> 1.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         1/1/1  -> 1.00
  [13] 7 Issues and Refinements                     2/2/2  -> 2.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 45 passes): We begin with a brief overview of the OOTA problem followed by an equally brief summary of prior OOTA work and of our approach.
candidate 2 (found by 3 of 45 passes): P0442R0 (“Out-of-Thin-Air Execution is Vacuous”) [26] provided a decision procedure for distinguishing between reordering and OOTA, using a perturbation method based on the insight that OOTA cycles are fixed-point computations
candidate 3 (found by 3 of 45 passes): Expanding on earlier discussions [6], as long as y is zero, changes in the value of x will not cause a change in the value stored to z.
candidate 4 (found by 3 of 45 passes): Taking our cue from the folklore, we propose to recognize formally that programs with volatile objects can execute in two different kinds of environment

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

## insufficiency - grade 0.17 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 1/0/0  -> 0.33
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/0/0  -> 0.00
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): Because invented loads can cause errors and break dependencies, as we have just seen, we should insist that the compiler not invent (or duplicate) atomic loads.

## implementation - grade 0.67  [binary: max] (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction and Background                1/1/0  -> 0.67
  [4] History                                      0/0/0  -> 0.00
  [5] 2 OOTA, Semantic Dependencies, and           0/0/0  -> 0.00
  [6] 3 What is an Execution?                      0/0/0  -> 0.00
  [7] 4 C++ Compilers                              0/0/0  -> 0.00
  [8] 4.1 Users Influence the Behavior of Compi... 0/0/0  -> 0.00
  [9] 4.2 Global Optimization Can Destroy Depen... 0/0/0  -> 0.00
  [10] 4.3 Inventing Atomic Loads Can Cause Erro... 0/0/0  -> 0.00
  [11] 4.4 Volatile and Quasi Volatile Accesses     0/0/0  -> 0.00
  [12] 5 Hardware Dependencies, Instruction         0/1/0  -> 0.33
  [13] 7 Issues and Refinements                     0/0/0  -> 0.00
  [14] 8 Summary and Conclusion                     0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): We know of no instances of OOTA behavior in real C++ implementations.
candidate 2 (found by 1 of 45 passes): These exercises use the following steps: 1. Identify the potential semantic dependencies of inter- est. 2. Compile the code to assembly language, either using a real compiler or conceptually.

-->

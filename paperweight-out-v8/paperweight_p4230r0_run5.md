Verdict: Strong (9/14)

The paper offers a mixed case for its own standardization, with its strongest grounding in prior art and implementation experience, but it leans heavily on assertion when explaining who is affected and why a library-level solution is insufficient. The thinnest support appears around the necessity of a standard mechanism rather than an implementation-defined or library-based one.

- The paper clearly establishes relevant prior art through P0943, the known divergence between C and C++ atomic implementations, and Clang’s existing compatibility mechanism.
- The paper establishes implementation experience by pointing to an Android implementation that has been in use for nearly a decade.
- The paper claims but does not establish who is affected, offering only a suspicion about Clang clients rather than evidence of broader impact.
- The paper claims but does not establish why a library will not do, leaving the core argument for standardization dependent on asserted ABI problems rather than demonstrated ones.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.67   accumulate 9.17   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.33  coordination 0.83  insufficiency 0.67  implementation 2.00
sample agreement: 36 of 42 section-criterion pairs unanimous (86%)
single-sample totals would have been: 9.50 / 9.00 / 9.00   (all 3 samples: 9.17)
headings: h2 5
on threshold: vehicle, implementation
splits: motivation[2] 0/1/1  motivation[5] 1/2/1  audience[4] 0/1/1  vehicle[3] 1/0/1
        coordination[5] 1/1/0  insufficiency[3] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 6 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/2/1  -> 1.33
  [6] Concerns about ODR violations                1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 3 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.
candidate 3 (found by 3 of 18 passes): There has been a lot of discussion arguing that the C++23 spec essentially forces ODR violations.
candidate 4 (found by 2 of 18 passes): This is an attempt to outline the issues, as mostly exposed in the LEWG discussion, a later reflector discussion (“stdatomic.h in C++”, starting March 27, 2026), and some discussion on a github implementation CL.

## audience - grade 0.33 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     0/1/1  -> 0.67
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade.
candidate 2 (found by 1 of 18 passes): We suspect that most clients of clangs _Atomic could be converted easily to P0943 by including P0943’s `stdatomic.h`.

## prior_art - grade 2.00 (fired in 5 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/1  -> 1.00
  [6] Concerns about ODR violations                2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): [P0943](http://wg21.link/p0943) was accepted into C++23.
candidate 2 (found by 3 of 18 passes): P0943 did so (or at least we can agree that it attempted to do so), with an unorthodox approach, by defining stdatomic.h in C++ as a header that defined the C primitives in terms of the C++ ones
candidate 3 (found by 3 of 18 passes): C and C++ atomic types often do not share the same implementation.
candidate 4 (found by 2 of 18 passes): Clang has also long provided an alternate C compatibility mechanism by exposing C’s `_Atomic` in C++ as a C-compatible alternative to `std::atomic`.

## vehicle - grade 1.33 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/0/1  -> 0.67
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 2 (found by 2 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.

## coordination - grade 0.83 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Current state of affairs                     0/0/0  -> 0.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/0  -> 0.67
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 2 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.

## insufficiency - grade 0.67 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/0/0  -> 0.33
  [4] Current state of affairs                     1/1/1  -> 1.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 2 (found by 1 of 18 passes): P0943 made it clear that the utility of this solution depended on ensuring the C representation and the C++ representation of these atomic types was in fact the same.

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade.

-->

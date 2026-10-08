Verdict: Strong (10/14)

The paper offers a solid foundation for why the problem matters and why standardization is the right venue, particularly through its discussion of C/C++ compatibility failures and the precedent of P0943. The support is thinnest around demonstrating who is concretely affected, how coordination would work in practice, and why a library-level solution cannot suffice.

- The strongest support is the established need for a shared C/C++ header that can mention atomics without forcing ODR violations or ABI mismatches.
- The paper also credibly establishes prior art and standardization relevance through P0943 and the documented incompatibilities when atomics cross language boundaries.
- The most glaring omission is the lack of established evidence for who is affected beyond a single implementation claim, leaving the user impact largely asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 7 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 10.00   accumulate 10.00   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.50  coordination 0.83  insufficiency 0.67  implementation 2.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 9.50 / 9.50 / 9.50   (all 3 samples: 9.50)
headings: h2 5
on threshold: vehicle, implementation
splits: motivation[5] 2/2/1  vehicle[5] 0/1/0  coordination[5] 0/1/1  insufficiency[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 6 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 2/2/1  -> 1.67
  [6] Concerns about ODR violations                1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 3 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.
candidate 3 (found by 3 of 18 passes): There has been a lot of discussion arguing that the C++23 spec essentially forces ODR violations.
candidate 4 (found by 2 of 18 passes): This is an attempt to outline the issues, as mostly exposed in the LEWG discussion, a later reflector discussion (“stdatomic.h in C++”, starting March 27, 2026), and some discussion on a github implementation CL.

## audience - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     1/1/1  -> 1.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade.

## prior_art - grade 2.00 (fired in 5 of 6 sections, strong in 3)  (SHARED PASSAGE)
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
candidate 3 (found by 3 of 18 passes): Clang has also long provided an alternate C compatibility mechanism by exposing C’s `_Atomic` in C++ as a C-compatible alternative to `std::atomic`.
candidate 4 (found by 2 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.

## vehicle - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/1/0  -> 0.33
  [6] Concerns about ODR violations                1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 3 of 18 passes): We treat C and C++ as different languages trying to access the same data structures in memory.
candidate 3 (found by 1 of 18 passes): It is unclear to us whether the clang approach here is really workable.
candidate 4 (found by 1 of 18 passes): We found this problematic when the initial P0943-like implementation was developed for Android.

## coordination - grade 0.83 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Current state of affairs                     0/0/0  -> 0.00
  [5] Concerns about fundamental C vs C++ incom... 0/1/1  -> 0.67
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 2 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.

## insufficiency - grade 0.67 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     1/1/1  -> 1.00
  [5] Concerns about fundamental C vs C++ incom... 1/0/0  -> 0.33
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 2 (found by 1 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.

## implementation - grade 2.00  [binary: max] (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade.
candidate 2 (found by 2 of 18 passes): This summarizes points we think should be kept in mind.
candidate 3 (found by 1 of 18 passes): This is an attempt to outline the issues, as mostly exposed in the LEWG discussion, a later reflector discussion (“stdatomic.h in C++”, starting March 27, 2026), and some discussion on a github implementation CL.

-->

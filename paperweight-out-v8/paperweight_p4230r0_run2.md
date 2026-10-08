Verdict: Strong (9/14)

The paper offers some useful grounding for its standardization case, particularly around prior art and implementation experience, but much of the argument remains asserted rather than demonstrated. The thinnest support concerns why a library solution is insufficient and whether the affected constituencies and interoperability problems are real enough to justify standardization.

- The strongest support comes from the accepted C++23 precedent in P0943 and the documented Android implementation experience behind it.
- The paper also establishes that prior approaches exist and that C and C++ treat atomics differently in ways that create genuine compatibility friction.
- The case for who is affected rests mainly on a single implementation’s longevity rather than broader evidence of user or vendor need.
- The most glaring omission is the failure to establish why a library-only solution cannot address the stated ABI and alignment concerns.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 10.00   accumulate 9.17   max 11.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 0.50  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.00 / 9.00 / 9.50   (all 3 samples: 9.17)
headings: h2 5
on threshold: vehicle, implementation
splits: prior_art[6] 2/2/1  vehicle[6] 0/0/1  implementation[2] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 6 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/1  -> 1.00
  [6] Concerns about ODR violations                1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): This is an attempt to outline the issues, as mostly exposed in the LEWG discussion, a later reflector discussion (“stdatomic.h in C++”, starting March 27, 2026), and some discussion on a github implementation CL.
candidate 2 (found by 3 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 3 (found by 3 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 4 (found by 3 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.

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

## prior_art - grade 2.00 (fired in 5 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/1  -> 1.00
  [6] Concerns about ODR violations                2/2/1  -> 1.67
candidate 1 (found by 3 of 18 passes): [P0943](http://wg21.link/p0943) was accepted into C++23.
candidate 2 (found by 3 of 18 passes): P0943 did so (or at least we can agree that it attempted to do so), with an unorthodox approach, by defining stdatomic.h in C++ as a header that defined the C primitives in terms of the C++ ones
candidate 3 (found by 3 of 18 passes): Clang has also long provided an alternate C compatibility mechanism by exposing C’s `_Atomic` in C++ as a C-compatible alternative to `std::atomic`.
candidate 4 (found by 2 of 18 passes): C++ atomics have class type, and C atomics like _Atomic(int) (or _Atomic int) are normally viewed as scalars.

## vehicle - grade 1.17 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/1  -> 0.33
candidate 1 (found by 2 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 2 (found by 1 of 18 passes): In addition, some implementation strategies perform very poorly.
candidate 3 (found by 1 of 18 passes): We treat C and C++ as different languages trying to access the same data structures in memory.

## coordination - grade 1.00 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Current state of affairs                     0/0/0  -> 0.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/1  -> 1.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.
candidate 2 (found by 2 of 18 passes): it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 3 (found by 1 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.

## insufficiency - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     1/1/1  -> 1.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.

## implementation - grade 2.00  [binary: max] (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 0/0/0  -> 0.00
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade.
candidate 2 (found by 2 of 18 passes): This is an attempt to outline the issues, as mostly exposed in the LEWG discussion, a later reflector discussion (“stdatomic.h in C++”, starting March 27, 2026), and some discussion on a github implementation CL.

-->

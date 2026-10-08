Verdict: Strong (9/14)

The paper offers some grounding for its standardization case, chiefly through its discussion of prior art and the long-standing implementation experience behind P0943, but much of the argument for why this belongs in the standard remains asserted rather than demonstrated. The thinnest support is around the necessity of standardization itself, the limits of library-only solutions, and the practical coordination burden across C and C++.

- The strongest support is the established prior art, including P0943’s acceptance into C++23 and the decade of Android implementation experience.
- The paper clearly identifies why the topic matters by pointing to concrete ABI and parameter-passing incompatibilities between C and C++ atomics.
- The case for who is affected leans almost entirely on the Android example without showing the broader population or scale of users facing the problem.
- The most glaring omission is the lack of an established argument for why a library cannot address the issue, since the paper’s own text concedes that passing atomics by value is generally not meaningful.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.67   accumulate 9.33   max 10.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.17  coordination 0.83  insufficiency 0.50  implementation 2.00
sample agreement: 32 of 42 section-criterion pairs unanimous (76%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.00)
headings: h2 5
on threshold: vehicle, implementation
splits: motivation[5] 1/2/1  prior_art[3] 0/2/2  vehicle[3] 1/0/1  vehicle[4] 1/2/2
        vehicle[5] 0/0/1  coordination[3] 2/1/0  coordination[5] 1/1/0  insufficiency[3] 0/1/0
        insufficiency[4] 0/1/1  insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 6 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/2/1  -> 1.33
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

## prior_art - grade 2.00 (fired in 5 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 0/2/2  -> 1.33
  [4] Current state of affairs                     2/2/2  -> 2.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/1  -> 1.00
  [6] Concerns about ODR violations                2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): [P0943](http://wg21.link/p0943) was accepted into C++23.
candidate 2 (found by 3 of 18 passes): It is fundamentally not what wg21.link/P0943 does. We treat C and C++ as different languages trying to access the same data structures in memory.
candidate 3 (found by 2 of 18 passes): P0943 did so (or at least we can agree that it attempted to do so), with an unorthodox approach, by defining stdatomic.h in C++ as a header that defined the C primitives in terms of the C++ ones
candidate 4 (found by 2 of 18 passes): P0943 is based on an Android implementation that has been in use for nearly a decade. Clang has also long provided an alternate C compatibility mechanism by exposing C’s `_Atomic` in C++ as a C-compatible alternative to `std::atomic`.

## vehicle - grade 1.17 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/0/1  -> 0.67
  [4] Current state of affairs                     1/2/2  -> 1.67
  [5] Concerns about fundamental C vs C++ incom... 0/0/1  -> 0.33
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 2 (found by 1 of 18 passes): It is unclear to us whether the clang approach here is really workable.
candidate 3 (found by 1 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 4 (found by 1 of 18 passes): In addition, some implementation strategies perform very poorly. I currently often recommend avoiding these other cases altogether given the ABI issues.

## coordination - grade 0.83 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 2/1/0  -> 1.00
  [4] Current state of affairs                     0/0/0  -> 0.00
  [5] Concerns about fundamental C vs C++ incom... 1/1/0  -> 0.67
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The reflector discussions exposed inherent compatibility issues when atomics are passed as parameters or returned as results, since structs are sometimes passed or returned differently than scalars, even if the bit layout is the same.
candidate 2 (found by 1 of 18 passes): it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.
candidate 3 (found by 1 of 18 passes): Nonetheless we believe that it is essential to provide an easy way to implement a header file that is both shared between C and C++ and mentions atomics.

## insufficiency - grade 0.50 (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/1/0  -> 0.33
  [4] Current state of affairs                     0/1/1  -> 0.67
  [5] Concerns about fundamental C vs C++ incom... 0/0/1  -> 0.33
  [6] Concerns about ODR violations                0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): In cases with weaker alignment, current implementations are often problematic in that they do not enforce a consistent ABI across compilers, even within the same language.
candidate 2 (found by 1 of 18 passes): P0943 made it clear that the utility of this solution depended on ensuring the C representation and the C++ representation of these atomic types was in fact the same.
candidate 3 (found by 1 of 18 passes): However, it is generally not meaningful to pass an atomic (as opposed to a pointer to one) as a parameter.

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

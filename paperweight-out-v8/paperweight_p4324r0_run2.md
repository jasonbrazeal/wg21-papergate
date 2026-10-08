Verdict: Adequate (5/14)

The paper offers concrete support for its standardization case mainly through an available GCC fork implementation and a clear statement of the flexibility problems it wants to solve, but much of the surrounding argument is asserted rather than demonstrated. The thinnest areas are the absence of any identified affected audience, any discussion of coordination or interoperability, and any explanation of why the work cannot be done in a library.

- The strongest support is the implementation experience, since the approach has been realized in a GCC fork and can be examined directly.
- The paper also establishes why the problem matters by pointing to already-communicated needs such as turning off constification and controlling exception translation.
- Prior art and alternatives are only claimed, with references to related papers and a syntactic similarity to P3400, but without a substantive comparison showing how this approach improves on them.
- The most glaring omission is the lack of any case for why a library will not do, which is especially damaging for a proposal explicitly describing itself as library-oriented.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 4 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.67   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 5
on threshold: motivation, implementation
splits: prior_art[2] 1/1/2  vehicle[3] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] The goal, elaborated                         2/2/2  -> 2.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The goal of the exploration is to look at an alternative model that is less compiler-dependent, more library-oriented, and by being especially the latter, more flexible and more user-extensible.
candidate 2 (found by 2 of 18 passes): There are various such needs that have already been communicated, such as being able to: - turn off constification - write contracts that do not translate predicate exceptions into contract violations, but pass such exceptions through
candidate 3 (found by 1 of 18 passes): There are various such needs that have already been communicated, such as being able to: turn off constification; write contracts that do not translate predicate exceptions into contract violations, but pass such exceptions through

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The goal, elaborated                         0/0/0  -> 0.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 4 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/2  -> 1.33
  [3] The goal, elaborated                         1/1/1  -> 1.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          1/1/1  -> 1.00
  [6] Implementation experience                    1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): This exploration is heavily based on ideas formulated in Bengt Gustafsson's paper [P3968](https://wg21.link/p3968), but also builds on various other papers such as [P4005](https://wg21.link/p4005) and [P4009](https://wg21.link/p4009), attempting to further refine those papers and address the review feedback given for them.
candidate 2 (found by 3 of 18 passes): Some of these things are things that have been on the committee's agenda during the development of C++26 contracts.
candidate 3 (found by 3 of 18 passes): This approach has been implemented in a fork of GCC, at [https://github.com/villevoutilainen/gcc/tree/p4324](https://github.com/villevoutilainen/gcc/tree/p4324).
candidate 4 (found by 2 of 18 passes): To go straight to the point, the syntactic keying used here is similar to P3400: `void f(int x) pre&lt;cco>(x >= 0);` and similarly for `post` and `contract_assert`.

## vehicle - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The goal, elaborated                         1/1/0  -> 0.67
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This framework allows Just Doing them, in (3rd party) library code, which could later become standard library code.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The goal, elaborated                         0/0/0  -> 0.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The goal, elaborated                         0/0/0  -> 0.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] The goal, elaborated                         0/0/0  -> 0.00
  [4] The approach                                 0/0/0  -> 0.00
  [5] The building blocks                          0/0/0  -> 0.00
  [6] Implementation experience                    2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): This approach has been implemented in a fork of GCC, at [https://github.com/villevoutilainen/gcc/tree/p4324](https://github.com/villevoutilainen/gcc/tree/p4324).

-->

Verdict: Adequate (6/14)

The paper offers a narrow but genuine case for its central technical claim, supported mainly by reasoning about existing inconsistencies and by some implementation experience. Its support is thinnest on the institutional questions: it does not establish who is affected, why this belongs in the standard rather than a library, or how it would coordinate with existing practice.

- The strongest support is the reported implementation work, including a libstdc++ fork and an initial GCC patch, which gives the proposal some practical grounding.
- The paper also establishes that the problem is real and that alternatives have been considered, particularly by diagnosing the ambiguity in the P3792R0 example and arguing for `std::constant_wrapper` over `std::constant_arg`.
- The most glaring omission is the absence of any established audience or impact, leaving unclear who would benefit from standardization.
- Equally missing is a case for why the standard is the right venue, since the paper does not show that a library solution would be insufficient or that coordination with other proposals and implementations has been addressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 3 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 10
on threshold: implementation
splits: motivation[8] 1/2/1  prior_art[9] 0/1/0  prior_art[11] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     1/1/1  -> 1.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  1/1/1  -> 1.00
  [7] 4 RESOLVING THE INCONSISTENCY                2/2/2  -> 2.00
  [8] 5 SUMMARY                                    1/2/1  -> 1.33
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       1/1/1  -> 1.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This is especially important for constructors where we cannot give explicit template arguments.
candidate 2 (found by 3 of 33 passes): The presence of a second type `std::constant_arg` that has the same design intent but with extra semantics and a narrow focus on `std::function_ref` is just inconsistent and hard to teach.
candidate 3 (found by 3 of 33 passes): This is pointless. The point of passing a callable with function parameters is to call it with *unknown values* for those parameters.
candidate 4 (found by 3 of 33 passes): The actual problem in the [P3792R0] example is an ambiguity/dual semantics: Did the user mean to call `cw<foo>(baz)` or `foo(baz)`.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  0/0/0  -> 0.00
  [7] 4 RESOLVING THE INCONSISTENCY                0/0/0  -> 0.00
  [8] 5 SUMMARY                                    0/0/0  -> 0.00
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       0/0/0  -> 0.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 8 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     1/1/1  -> 1.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  1/1/1  -> 1.00
  [7] 4 RESOLVING THE INCONSISTENCY                2/2/2  -> 2.00
  [8] 5 SUMMARY                                    1/1/1  -> 1.00
  [9] 6 PROPOSAL                                   0/1/0  -> 0.33
  [10] 7 FURTHER/RELATED WORK                       1/1/1  -> 1.00
  [11] 8 WORDING                                    0/0/1  -> 0.33
candidate 1 (found by 3 of 33 passes): The actual problem in the [P3792R0] example is an ambiguity/dual semantics: Did the user mean to call `cw<foo>(baz)` or `foo(baz)`.
candidate 2 (found by 3 of 33 passes): The current inconsistencies for “transparent” wrappers due to the language rules are not helpful.
candidate 3 (found by 2 of 33 passes): This paper shows that there is no real problem, and provides a simple solution to resolve the contrived problems that can be constructed.
candidate 4 (found by 2 of 33 passes): After reviewing the reasons why LEWG decided to not use `std::constant_wrapper` I got only more convinced that we should use `std::constant_wrapper` for `std::function_ref`.

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  0/0/0  -> 0.00
  [7] 4 RESOLVING THE INCONSISTENCY                0/0/0  -> 0.00
  [8] 5 SUMMARY                                    0/0/0  -> 0.00
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       0/0/0  -> 0.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  0/0/0  -> 0.00
  [7] 4 RESOLVING THE INCONSISTENCY                0/0/0  -> 0.00
  [8] 5 SUMMARY                                    0/0/0  -> 0.00
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       0/0/0  -> 0.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  0/0/0  -> 0.00
  [7] 4 RESOLVING THE INCONSISTENCY                0/0/0  -> 0.00
  [8] 5 SUMMARY                                    0/0/0  -> 0.00
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       0/0/0  -> 0.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 0/0/0  -> 0.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  0/0/0  -> 0.00
  [7] 4 RESOLVING THE INCONSISTENCY                2/2/2  -> 2.00
  [8] 5 SUMMARY                                    0/0/0  -> 0.00
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       1/1/1  -> 1.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): I implemented `function_ref` unwrapping `constant_wrapper` with such a detection in a libstdc++ fork.5
candidate 2 (found by 3 of 33 passes): An initial patch to GCC to call `operator()` for wrappers like `constant_wrapper` already feels more consistent (to me).

-->

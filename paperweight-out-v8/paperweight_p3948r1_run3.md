Verdict: Adequate (6/14)

The paper offers some concrete support for its position, particularly in its engagement with prior discussion and its report of implementation experience, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the absence of any identified affected users, any argument for why this belongs in the standard rather than a library, and any discussion of coordination or interoperability.

- The paper’s strongest support comes from its prior-art analysis, which engages seriously with the earlier `std::constant_wrapper` decision and explains why the author remains convinced it should be used with `std::function_ref`.
- The implementation experience is also credited, since the author reports both a libstdc++ fork implementing the unwrapping and detection, and an initial GCC patch toward more consistent wrapper call semantics.
- The most glaring omission is the lack of any established audience: the paper does not show who is affected by the problem or who would benefit from standardization.
- Equally unestablished are the arguments that this requires a standard change rather than a library solution, and that it coordinates or interoperates with existing or planned features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 3 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 10
on threshold: implementation
splits: motivation[8] 1/0/1  prior_art[10] 0/1/1  prior_art[11] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] ABSTRACT                                     1/1/1  -> 1.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 STRAW POLLS                                0/0/0  -> 0.00
  [5] 3 MOTIVATION                                 2/2/2  -> 2.00
  [6] 4 https://compiler-explorer.com/z/59EMracKT  1/1/1  -> 1.00
  [7] 4 RESOLVING THE INCONSISTENCY                2/2/2  -> 2.00
  [8] 5 SUMMARY                                    1/0/1  -> 0.67
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       1/1/1  -> 1.00
  [11] 8 WORDING                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): We added `std::constant_wrapper<value>` to C++26 to enable “passing constant expressions as function arguments”.
candidate 2 (found by 3 of 33 passes): This is pointless. The point of passing a callable with function parameters is to call it with *unknown values* for those parameters.
candidate 3 (found by 3 of 33 passes): The actual problem in the [P3792R0] example is an ambiguity/dual semantics: Did the user mean to call `cw<foo>(baz)` or `foo(baz)`.
candidate 4 (found by 3 of 33 passes): The current inconsistencies for “transparent” wrappers due to the language rules are not helpful.

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

## prior_art - grade 2.00 (fired in 7 of 11 sections, strong in 2)
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
  [9] 6 PROPOSAL                                   0/0/0  -> 0.00
  [10] 7 FURTHER/RELATED WORK                       0/1/1  -> 0.67
  [11] 8 WORDING                                    1/1/0  -> 0.67
candidate 1 (found by 3 of 33 passes): After reviewing the reasons why LEWG decided to not use `std::constant_wrapper` I got only more convinced that we should use `std::constant_wrapper` for `std::function_ref`.
candidate 2 (found by 3 of 33 passes): `constant_arg<fun>` works with `function_ref` but not with any other function wrapper.
candidate 3 (found by 2 of 33 passes): The existence of `constant_wrapper::operator()` lead to fear, uncertainty, and doubt1, whether wrapping a callable with `constant_wrapper` leads to inconsistent semantics.
candidate 4 (found by 2 of 33 passes): It is fairly simply to detect this potential mismatch in `function_-` `ref` and reject the program. Rejecting is consistent with overload resolution where ambiguities are rejected.

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

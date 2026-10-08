Verdict: Strong (8/14)

The paper offers substantial support for standardization in the areas of implementation experience, prior art, and interoperability, but it leaves the core question of why a standard change is needed largely unaddressed. The thinnest parts of the case concern the absence of a direct argument that the current standard text is defective or that standardization would resolve a real problem beyond what implementations already do.

- The strongest support comes from demonstrated implementation experience across Clang, GCC, MSVC, and NVC++, including a prototype matching the proposed approach.
- The paper also establishes meaningful prior art and design-space analysis, with clear WG21 consensus direction and a documented alternative approach.
- The case for who is affected rests mainly on an anecdotal claim about Stack Overflow frequency, without evidence that this is a widespread or significant user problem.
- The most glaring omission is the lack of any established argument for why the standard itself must change, rather than leaving the behavior as a de facto common extension.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 5 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 7.67   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.00 / 8.00 / 8.50   (all 3 samples: 8.17)
headings: h3 6   <- NOT h2, check the unit list
on threshold: coordination
splits: audience[3] 0/1/0  audience[4] 0/1/1  prior_art[7] 0/1/0  coordination[3] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/2  -> 2.00
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 3 of 21 passes): The status quo is that this is ambiguous because the candidates `X::X(int)` and `X::X(X&&)` each require a different user-defined conversion function (`Y::operator int` and `Y::operator X`), respectively.

## audience - grade 0.50 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    0/1/0  -> 0.33
  [4] Known divergences                            0/1/1  -> 0.67
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This is the most common type of implementation divergence noticed by Stack Overflow users.
candidate 2 (found by 1 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/2  -> 2.00
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/1/0  -> 0.33
candidate 1 (found by 3 of 21 passes): the EDG approach with an additional restriction that only copy and move constructors could be elided. (Other approaches considered are described in R2 of this paper.)
candidate 2 (found by 2 of 21 passes): Comparison of the approaches reveals a surprisingly large design space for copy elision for direct-initialization using a conversion function.
candidate 3 (found by 2 of 21 passes): In the February 2023 WG21 meeting in Issaquah, the consensus in CWG was that code like the above ought to be well-formed, and that an approach similar to the Clang approach should be pursued in order to make it so.
candidate 4 (found by 1 of 21 passes): Clang's approach, as explained to me by Richard Smith, involves considering both constructors and conversion functions as candidates for the direct-initialization.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    0/0/0  -> 0.00
  [4] Known divergences                            0/0/0  -> 0.00
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.67 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/0/2  -> 1.33
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 1 of 21 passes): The consensus was that the behavior of Example 4 should not be changed, which rules out the current Clang and GCC approaches.
candidate 3 (found by 1 of 21 passes): The status quo is that this is ambiguous because the candidates `X::X(int)` and `X::X(X&&)` each require a different user-defined conversion function (`Y::operator int` and `Y::operator X`), respectively.
candidate 4 (found by 1 of 21 passes): The most common type of implementation divergence noticed by Stack Overflow users.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    0/0/0  -> 0.00
  [4] Known divergences                            0/0/0  -> 0.00
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/2  -> 2.00
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    1/1/1  -> 1.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 3 of 21 passes): GCC chooses the conversion function over the constructor since version 7.1 as long as the language mode is set to C++17 or higher.
candidate 3 (found by 3 of 21 passes): We have produced an implementation of the proposed approach and verified that it accepts examples 1, 2, 3, 7, and 8 and leaves the behavior of examples 4, 5, and 6 unchanged.

-->

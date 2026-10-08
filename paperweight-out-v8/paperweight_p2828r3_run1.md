Verdict: Strong (8/14)

The paper offers solid evidence that the problem is real and that major implementations have already converged on accepting the relevant code, but it leaves the standardization rationale incomplete in a few important places. The thinnest support concerns why a standard change is necessary at all, and why the behavior cannot be addressed through a library or left to existing implementation practice.

- The strongest support is the implementation experience, with multiple major compilers already accepting the code and a prototype confirming the proposed approach works on the intended examples.
- The paper also clearly establishes why the issue matters by identifying the ambiguity and the strong community desire to make certain examples well-formed.
- The weakest area is the absence of any established argument for why the standard itself must change, rather than relying on existing compiler behavior.
- The paper likewise does not establish why a library solution would be insufficient, leaving that part of the standardization case unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 8.00 / 7.50   (all 3 samples: 8.00)
headings: h3 6   <- NOT h2, check the unit list
on threshold: audience
splits: audience[3] 1/2/2  audience[4] 0/0/1  coordination[3] 2/2/0  coordination[4] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/2  -> 2.00
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           1/1/1  -> 1.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 3 of 21 passes): The status quo is that this is ambiguous because the candidates `X::X(int)` and `X::X(X&&)` each require a different user-defined conversion function (`Y::operator int` and `Y::operator X`), respectively.
candidate 3 (found by 3 of 21 passes): a strong desire emerged to make Examples 2, 3, and 8 compile; Examples 4 and 5 should be unaffected, and ideally so should Example 6.

## audience - grade 1.00 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    1/2/2  -> 1.67
  [4] Known divergences                            0/0/1  -> 0.33
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 1 of 21 passes): This is the most common type of implementation divergence noticed by Stack Overflow users.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/2  -> 2.00
  [4] Known divergences                            2/2/2  -> 2.00
  [5] Description of proposed resolution           2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      1/1/1  -> 1.00
candidate 1 (found by 3 of 21 passes): Also, it's not clear to me that it ever makes a difference whether we consider the user-defined conversion in the user-defined conversion sequence to be `C` or the conversion function, so I've added this note just to be safe.
candidate 2 (found by 2 of 21 passes): Comparison of the approaches reveals a surprisingly large design space for copy elision for direct-initialization using a conversion function.
candidate 3 (found by 2 of 21 passes): The Clang approach makes direct-initialization conceptually more similar to copy-initialization in that constructors and conversion functions are both considered when enumerating candidates.
candidate 4 (found by 2 of 21 passes): Other approaches considered are described in R2 of this paper.

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

## coordination - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] Copy elision in the Big 4                    2/2/0  -> 1.33
  [4] Known divergences                            2/0/0  -> 0.67
  [5] Description of proposed resolution           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Recent versions of Clang, GCC, MSVC, and NVC++ (which uses an EDG front end) all implement copy elision, and accept the code even if `Cat`'s move constructor is explicitly deleted.
candidate 2 (found by 1 of 21 passes): In the February 2023 WG21 meeting in Issaquah, the consensus in CWG was that code like the above ought to be well-formed, and that an approach similar to the Clang approach should be pursued in order to make it so.

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

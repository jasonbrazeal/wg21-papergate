Verdict: Weak (3/14)

The paper offers only a narrow basis for its own standardization: the implementation experience is concrete, but most of the surrounding case is asserted rather than demonstrated. The thinnest support lies in the absence of any established audience, need for standard wording, or reason a library solution would be insufficient.

- The strongest support is the observation that both libstdc++ and libc++ already abandon the state in practice, despite what the standard says.
- The paper gestures at a real failure mode, but it does not establish who is affected or why that failure matters broadly enough to justify standardization.
- The discussion of prior art and alternatives is only claimed, leaving the relationship to earlier work such as P1831R1 undeveloped.
- The most glaring omission is the lack of any established case for why the standard must change, as opposed to a library-level or implementation-level remedy.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 3. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 3.00   accumulate 2.50   max 3.00

## SUMMARY
grades: motivation 0.33  audience 0.00  prior_art 0.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 19 of 21 section-criterion pairs unanimous (90%)
single-sample totals would have been: 2.50 / 2.50 / 2.50   (all 3 samples: 2.50)
headings: none found   <- NOT h2, check the unit list
on threshold: implementation
splits: motivation[1] 0/1/1  prior_art[1] 1/0/0
## END SUMMARY

## motivation - grade 0.33 (fired in 1 of 3 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 1 of 9 passes): Any future that shares ownership of the shared state will never receive a result, because the provider is gone. This means that any thread that waits on the future will block forever.
candidate 2 (found by 1 of 9 passes): The above leads to a hardened precondition failure in libstdc++, the reason is that we are iterating over the nested range as:

## audience - grade 0.00 (fired in 0 of 3 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.17 (fired in 1 of 3 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 1 of 9 passes): Paper [P1831R1](https://wg21.link/p1831r1) aimed to deprecate all the atomic overloads for `volatile` qualified member function of `std::atomic` unless `is_always_lock_free` is `true`.

## vehicle - grade 0.00 (fired in 0 of 3 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 3 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 3 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 3 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 9 passes): Both libstdc++ and libc++ abandon the state, despite what the standard says.

-->

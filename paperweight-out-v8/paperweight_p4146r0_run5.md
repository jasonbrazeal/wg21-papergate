Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly in showing that the problem is real, that alternatives have been considered, and that implementations exist, but it leaves the core standardization rationale largely unstated. The thinnest parts are the absence of any discussion of who is affected, why a library solution is insufficient, and why the standard itself must change.

- The strongest support is the concrete implementation experience, with changes already applied in libstdc++ and implementations included in stdexec.
- The paper also establishes prior art and alternatives, including two mutually exclusive options and links to related library issues and NB comments.
- The most glaring omission is the lack of any established case for why the standard, rather than a library, is the right place to address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 3 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 55 of 63 section-criterion pairs unanimous (87%)
single-sample totals would have been: 5.50 / 6.00 / 5.50   (all 3 samples: 5.50)
headings: none found   <- NOT h2, check the unit list
on threshold: prior_art
splits: motivation[5] 0/0/2  motivation[6] 0/1/0  prior_art[4] 1/0/1  prior_art[5] 1/1/0
        prior_art[6] 0/2/1  prior_art[7] 0/1/0  prior_art[8] 0/1/0  implementation[5] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/0/2  -> 0.67
  [6] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [7] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): However, for parallel range algorithms the output size can be insufficient to have every single element from input that fits.
candidate 2 (found by 2 of 27 passes): This will allocate temporary string, then copy one byte from it
candidate 3 (found by 1 of 27 passes): This will allocate temporary string, then copy one byte from it:
candidate 4 (found by 1 of 27 passes): This prevents perfectly reasonable code from working, like `ranges::find(v, nullopt)` where `v` is a `vector<optional<T>>`, for no good reason.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [6] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 7 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 1/0/1  -> 0.67
  [5] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [6] (front matter: title, abstract and anythi... 0/2/1  -> 1.00
  [7] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [8] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Two mutually exclusive options are prepared, depicted below by **Option A** and **Option B**, respectively.
candidate 2 (found by 2 of 27 passes): Such changes are being made in libc++ ([llvm/llvm-project#74768](https://github.com/llvm/llvm-project/pull/74768)).
candidate 3 (found by 1 of 27 passes): This is almost the same problem as LWG 4071 except that it happens to `std::inplace_vector`.
candidate 4 (found by 1 of 27 passes): Addresses [US 257-382](https://github.com/cplusplus/nbballot/issues/957)

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [6] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [6] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [6] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 0/2/2  -> 1.33
  [6] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This inconsistency was noticed while fixing [PR121061](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=121061) and these changes have been applied to all layout mappings implemented in libstdc++.
candidate 2 (found by 2 of 27 passes): I've implemented the requested additional throws and they are easily achievable.
candidate 3 (found by 2 of 27 passes): An implementation that addresses this issue is included in stdexec PR 1713, specifically in commit 5209ffdcaf9a3badf0079746b5578c12a1d0da4f
candidate 4 (found by 1 of 27 passes): An implementation that addresses this issue is included in stdexec PR 1713, specifically in commit 5209ffdcaf9a3badf0079746b5578c12a1d0da4f.

-->

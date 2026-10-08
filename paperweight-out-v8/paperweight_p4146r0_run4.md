Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly by connecting its changes to existing practice and prior standardization discussions, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest support concerns who would be affected, why the standard is the right venue, and how the proposal fits with adjacent specifications.

- The strongest support comes from concrete implementation experience, including fixes already applied in libstdc++ and work in stdexec and NVIDIA’s CCCL.
- The paper also establishes why the problem matters by pointing to specific code that fails or behaves unreasonably under the current specification.
- Prior art and alternatives are addressed through explicit options and references to related LWG issues and papers.
- The most glaring omission is the absence of any discussion of who is affected, leaving the scope and practical impact of the change unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 3 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: none found   <- NOT h2, check the unit list
on threshold: prior_art
splits: motivation[3] 0/2/0  motivation[4] 0/0/1  motivation[5] 1/0/2  motivation[6] 2/2/0
        prior_art[7] 1/1/0  prior_art[8] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 0/2/0  -> 0.67
  [4] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [5] (front matter: title, abstract and anythi... 1/0/2  -> 1.00
  [6] (front matter: title, abstract and anythi... 2/2/0  -> 1.33
  [7] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This will allocate temporary string, then copy one byte from it:
candidate 2 (found by 2 of 27 passes): This prevents perfectly reasonable code from working, like `ranges::find(v, nullopt)` where `v` is a `vector<optional<T>>`, for no good reason.
candidate 3 (found by 2 of 27 passes): The current specification of `not_fn<f>` says that the perfect forwarding call wrapper it returns does not have state entities.
candidate 4 (found by 2 of 27 passes): However, for parallel range algorithms the output size can be insufficient to have every single element from input that fits.

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

## prior_art - grade 1.50 (fired in 7 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [3] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [6] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [7] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [8] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Two mutually exclusive options are prepared, depicted below by **Option A** and **Option B**, respectively.
candidate 2 (found by 3 of 27 passes): This is almost the same problem as LWG 4071 except that it happens to `std::inplace_vector`.
candidate 3 (found by 3 of 27 passes): This inconsistency was noticed while fixing [PR121061](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=121061) and these changes have been applied to all layout mappings implemented in libstdc++.
candidate 4 (found by 2 of 27 passes): Paper [P2405](https://wg21.link/P2405), for which the `nullopt` part received LEWG support, is relevant here.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [3] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [4] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [5] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [6] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [7] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [8] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [9] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This inconsistency was noticed while fixing [PR121061](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=121061) and these changes have been applied to all layout mappings implemented in libstdc++.
candidate 2 (found by 2 of 27 passes): Since then, [a lock-free implementation of `run_loop` has been found](https://github.com/NVIDIA/cccl/blob/main/cudax/include/cuda/experimental/__execution/run_loop.cuh).
candidate 3 (found by 2 of 27 passes): An implementation that addresses this issue is included in stdexec PR 1713, specifically in commit 5209ffdcaf9a3badf0079746b5578c12a1d0da4f
candidate 4 (found by 1 of 27 passes): I've implemented the requested additional throws and they are easily achievable.

-->

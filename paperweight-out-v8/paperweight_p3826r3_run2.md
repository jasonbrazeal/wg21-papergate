Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly in showing that the problem is real and that the proposed fix has been implemented and used in practice. However, it leaves the standardization case largely unbuilt: it does not establish who is affected, why a library solution is insufficient, or how the proposal would coordinate with existing and future standard facilities.

- The strongest support comes from implementation experience, with two largely independent implementations and no reported bug fallout.
- The paper also establishes prior art and alternatives by situating the fix against recent proposals and existing library work.
- The most glaring omission is the absence of any established case for why this must be in the standard rather than remain a library solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 3 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 5.67)
headings: h2 9
on threshold: prior_art
splits: prior_art[5] 2/0/2  prior_art[6] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     2/2/2  -> 2.00
  [5] 4 Solutions considered                       2/2/2  -> 2.00
  [6] 5 Fixing algorithm customization             2/2/2  -> 2.00
  [7] 6 Addressing feedback from LEWG design re... 1/1/1  -> 1.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Unfortunately, there are gaps in its proposed resolution.
candidate 2 (found by 3 of 36 passes): Many senders do not know where they will complete until they know where they will be started.
candidate 3 (found by 3 of 36 passes): This would leave users with no easy standard way to start work on a given execution context, or transition to another execution context, or to execute work in parallel, or to wait for work to finish.
candidate 4 (found by 3 of 36 passes): As described in Fix algorithm customization now, so-called “early” customization, which determines the return type of `then(sndr, fn)` for example, is irreparably broken.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       0/0/0  -> 0.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       2/0/2  -> 1.33
  [6] 5 Fixing algorithm customization             0/2/0  -> 0.67
  [7] 6 Addressing feedback from LEWG design re... 2/2/2  -> 2.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [[P3718R0]](https://wg21.link/p3718r0) is the latest effort to shore up the mechanism.
candidate 2 (found by 3 of 36 passes): [[P3826R2]](https://wg21.link/p3826r2) was reviewed by LEWG at the Fall 2025 meeting in Kona, HI.
candidate 3 (found by 2 of 36 passes): This fix has been implemented in NVIDIA’s [CCCL](https://github.com/NVIDIA/cccl) library since mid-September 2025 (see [NVIDIA/cccl#5793](https://github.com/NVIDIA/cccl/pull/5793)) and in [stdexec](https://github.com/NVIDIA/stdexec) since late November (see [NVIDIA/stdexec#1683](https://github.com/NVIDIA/stdexec/pull/1683)).
candidate 4 (found by 1 of 36 passes): In the [CCCL](https://github.com/NVIDIA/cccl) project, I have implemented this design and ported my CUDA stream scheduler to use it.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       0/0/0  -> 0.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       0/0/0  -> 0.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       0/0/0  -> 0.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/0/0  -> 0.00
  [5] 4 Solutions considered                       2/2/2  -> 2.00
  [6] 5 Fixing algorithm customization             2/2/2  -> 2.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The fix has been implemented twice, largely independently and causing no bug reports.
candidate 2 (found by 3 of 36 passes): This fix has been implemented in NVIDIA’s [CCCL](https://github.com/NVIDIA/cccl) library since mid-September 2025 (see [NVIDIA/cccl#5793](https://github.com/NVIDIA/cccl/pull/5793)) and in [stdexec](https://github.com/NVIDIA/stdexec) since late November (see [NVIDIA/stdexec#1683](https://github.com/NVIDIA/stdexec/pull/1683)).
candidate 3 (found by 3 of 36 passes): In the [CCCL](https://github.com/NVIDIA/cccl) project, I have implemented this design and ported my CUDA stream scheduler to use it.

-->

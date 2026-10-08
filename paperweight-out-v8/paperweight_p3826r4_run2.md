Verdict: Adequate (7/14)

The paper offers meaningful support in the areas of motivation, prior art, and implementation experience, but it leaves several essential parts of the standardization case unaddressed, particularly why the standard is the right venue and why a library solution would not suffice. The thinnest support concerns the affected audience and interoperability, where the paper asserts consequences without demonstrating them.

- The strongest support is the implementation experience, with two largely independent implementations and no reported bugs.
- The paper also establishes that the problem is real and that prior efforts have not fully resolved it.
- The most glaring omission is the absence of any argument for why this must be standardized rather than left to libraries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.67)
headings: h2 9
on threshold: none
splits: motivation[7] 2/1/2  audience[2] 1/0/1  prior_art[4] 0/2/2  coordination[4] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     2/2/2  -> 2.00
  [5] 4 Solutions considered                       2/2/2  -> 2.00
  [6] 5 Fixing algorithm customization             2/2/2  -> 2.00
  [7] 6 Addressing feedback from LEWG design re... 2/1/2  -> 1.67
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Unfortunately, there are gaps in its proposed resolution.
candidate 2 (found by 3 of 36 passes): This would leave users with no easy standard way to start work on a given execution context, or transition to another execution context, or to execute work in parallel, or to wait for work to finish.
candidate 3 (found by 3 of 36 passes): As described in Fix algorithm customization now, so-called “early” customization, which determines the return type of `then(sndr, fn)` for example, is irreparably broken.
candidate 4 (found by 2 of 36 passes): Many senders do not know where they will complete until they know where they will be started.

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/0/1  -> 0.67
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
candidate 1 (found by 2 of 36 passes): The fix has been implemented twice, largely independently and causing no bug reports.

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/2/2  -> 1.33
  [5] 4 Solutions considered                       2/2/2  -> 2.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 2/2/2  -> 2.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [[P3718R0]](https://wg21.link/p3718r0) is the latest effort to shore up the mechanism.
candidate 2 (found by 3 of 36 passes): This fix has been implemented in NVIDIA’s [CCCL](https://github.com/NVIDIA/cccl) library since mid-September 2025 (see [NVIDIA/cccl#5793](https://github.com/NVIDIA/cccl/pull/5793)) and in [stdexec](https://github.com/NVIDIA/stdexec) since late November (see [NVIDIA/stdexec#1683](https://github.com/NVIDIA/stdexec/pull/1683)).
candidate 3 (found by 2 of 36 passes): [[P3718R0]](https://wg21.link/p3718r0) identifies real problems with the status quo of sender algorithm customization.
candidate 4 (found by 2 of 36 passes): After considering the issue, I decided that I agreed with Robert that the proposed design was deficient in this respect.

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

## coordination - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Background                                 0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 The problem with P3718                     0/2/0  -> 0.67
  [5] 4 Solutions considered                       0/0/0  -> 0.00
  [6] 5 Fixing algorithm customization             0/0/0  -> 0.00
  [7] 6 Addressing feedback from LEWG design re... 0/0/0  -> 0.00
  [8] 7 Proposed wording  (part 1 of 3)            0/0/0  -> 0.00
  [9] 7 Proposed wording  (part 2 of 3)            0/0/0  -> 0.00
  [10] 7 Proposed wording  (part 3 of 3)            0/0/0  -> 0.00
  [11] 8 Appendix A: Listing for updated transfo... 0/0/0  -> 0.00
  [12] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Many senders do not know where they will complete until they know where they will be started.

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

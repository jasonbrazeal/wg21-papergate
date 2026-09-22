Verdict: Adequate (4/14)

The paper offers a narrow but genuine rationale for revisiting `affine_on`, grounded in prior discussion and recorded concerns, but it does not build a complete case for standardization. The thinnest areas are the absence of any demonstrated need for a standard facility, the lack of affected users, and the missing argument for why a library solution would be insufficient.

- The strongest support comes from the paper’s connection to prior concerns raised against `affine_on` and the original design’s use of `continues_on`, which establishes that the design question is a live one within the committee’s ongoing work.
- The paper also establishes some engagement with existing specification by citing `change_coroutine_scheduler` and the related LWG issue, though this remains only a claim about coordination rather than a demonstrated interoperability story.
- The paper does not establish who is affected by the proposed change, leaving the actual user community and its stakes unclear.
- Most glaringly, the paper never establishes why the feature belongs in the C++ standard rather than being provided as a library capability, nor does it show that existing libraries cannot already serve the need.

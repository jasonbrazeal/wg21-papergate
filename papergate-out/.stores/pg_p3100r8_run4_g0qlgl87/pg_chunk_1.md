---
title: "A framework for systematically addressing undefined behaviour in the C++ Standard"
document: P3100R8
date: 2026-08-14
audience: EWG, LEWG
reply-to:
  - "Timur Doumler <papers@timur.audio>"
  - "Joshua Berne <jberne4@bloomberg.net>"
---


## Abstract

In this paper, we enumerate all cases of core language undefined behaviour explicitly specified in the C++ Standard, group them into ten categories, and classify them along a number of relevant criteria.

We then present a holistic strategy for systematically detecting, mitigating, and ultimately eliminating such undefined behaviour from the C++ Standard. This strategy is built on top of seven basic tools: feature removal, refined behaviour, erroneous behaviour, insertion of runtime checks, language subsetting, the introduction of annotations, and the introduction of entirely new language features. We discuss which tools are applicable to which cases of core language undefined behaviour.

We find that two of these tools — erroneous behaviour and runtime checks — are applicable to a wide range of existing cases and do not require any source changes. We describe how runtime checks can be systematically introduced via *implicit* *contract* *assertions*, giving users complete control over what impact that undefined behaviour has on their programs. In addition to runtime checking, we replace undefined behaviour with erroneous, but well-defined behaviour that allows the program to continue execution past a violated implicit contract assertion wherever possible.

Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the *entire* C++ language specification, fundamentally changing the landscape of how undefined behaviour is approached in C++.


## Revision history

— **R8**, 2026-08-14: Wording formatting improvements, rebased wording on latest draft and [P4284R0], updated discussion of interaction with `noexcept` (removed ubdef {basic.stc.alloc. dealloc.throw}, added {basic.compound.pointer.before.storage.duration} and {expr.reinterpret. cast.invalid.pointer.value}).

— **R7,** 2026-06-01: Wording formatting improvements; response to early wording review; clarified that implicit contract assertions have conditions and do not necessarily have predicates

— **R6**, 2026-05-12: Completed wording; rebased on [P3596R2]; simplified diagnosability criteria; added history and polls section

— **R5**, 2025-11-07: Added one more case of UB that was initially overlooked because it did not use the word “undefined” in the wording

— **R4**, 2025-08-13: Updated the paper to align with [P3754R0]; incorporated feedback from the WG21 meeting in Sofia; removed items from UB list that should not be specified as UB and have Core issues to make it so; added discussion of interaction with `noexcept`; improved paper structure; changed title to reflect the wider scope.

- **R3**, 2025-06-28: Removed preprocessor UB due to adoption of [P2843R3] into C++26.

- **R2**, 2025-05-19: Complete rewrite after the WG21 meeting in Hagenberg.

- **R1**, 2024-10-16: Complete rewrite after the WG21 meeting in St. Louis.

- **R0**, 2023-03-08: Initial version.


## 1 Introduction

Eliminating or at least meaningfully reducing the amount of *undefined* *behaviour* (UB) is an important objective for the future evolution of C++. WG21 has been continuously working in that direction. For a recent status update, see [Sutter2025] and references therein; for background, see [Sutter2024] and references therein.

While reducing the amount of UB on a case-by-case basis is useful to make the C++ programming language more safe and secure, what has been missing is a *holistic* strategy for systematically detecting, mitigating, and ultimately removing UB across the *entire* C++ programming language specification. In this paper, we present such a holistic strategy.

The remainder of this paper is structured as follows.

In Section 2, we summarise the history of this proposal and the polls taken by the various WG21 subgroups that reviewed it.

In Section 3, we identify and enumerate all core language UB explicitly specified in the current C++ working paper [N5054]. We group all core language UB into ten categories. We then classify cases of UB along several relevant criteria, such as whether they are checkable at compile time or at runtime, whether a check can be performed locally, how expensive a check would be, and in which cases the UB can be replaced with meaningful, well-defined behaviour.

In Section 4, we present our holistic strategy for addressing UB across the entire C++ language. The proposed strategy is composed of seven basic tools: feature removal, refined behaviour, erroneous behaviour, insertion of runtime checks, language subsetting, the introduction of annotations, and the introduction of entirely new language features. We use the results of the analysis in Section 3 to identify which tools are applicable to which cases of UB. We find that the conditions under which UB will occur can, in many cases, be identified by a runtime check. In addition, there are a significant number of cases where UB can be replaced by well-defined erroneous behaviour following a failed check. These two techniques are applicable to a wide range of existing cases of UB and, importantly, do not require any source changes.

In Section 5, we present a generic framework for applying these two techniques across the entire C++ language. The proposed design has been reviewed and approved by SG21, SG23, and EWG. We describe how runtime checks can be systematically introduced via *implicit* *contract* *assertions*, building on the basic framework of Contracts adopted for C++26 via [P2900R14] and giving users complete control over what impact that undefined behaviour has on their programs. In addition to runtime checking, we replace UB by erroneous, but well-defined behaviour that allows the program to continue execution past a violated implicit contract assertion wherever possible. We also propose an escape hatch to mitigate the runtime cost of such well-defined replacement behaviour and avoid performance regressions in existing C++ programs.

In Section 6, we propose wording that implements the framework presented in Section 5.

Finally, in Section 7, we discuss how future extensions, such as Labels [P3400R4], will enable programmatically identifying the category of UB that has occurred and provide us with granular, in-source control of the evaluation semantics for implicit contract assertions.


## 2 History and polls

The initial version R0 of this proposal, containing the basic ideas in this paper, was written up in early 2023, as a product of our work on designing a contract-assertion facility for C++ and understanding the many use cases of such a facility ([P1995R1]). During the WG21 meeting in June 2024 in St. Louis, these ideas were significantly refined, essentially taking on the shape they have today, and published in revision R1. This revision was reviewed by SG21 at the WG21 meeting in November 2024 in Wrocław. SG21 unanimously supported the proposed direction:

SG21 Poll 6, Wrocław, 2024-11-22

We support the direction of P3100R1 and encourage the authors to come back with a fully specified proposal.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 19 | 6 | 0 | 0 | 0 |
|  |  |  |  |  |

Result: Consensus

At the WG21 February 2025 meeting in Hagenberg, EWG agreed on pursuing a systematic treatment of core language UB in C++. The ship vehicle for this effort was originally supposed to be a *core* *language* *UB* *white* *paper*, to be released in the C++26 timeframe, and covering erroneous behaviour (EB), Profiles, and Contracts:

EWG Poll, Hagenberg, 2025-02

Pursue a language safety white paper in the C++26 timeframe containing systematic treatment of core language Undefined Behavior in C++, covering Erroneous Behavior, Profiles, and Contracts. Appoint Herb and Gašper as editors.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 32 | 31 | 6 | 4 | 4 |
|  |  |  |  |  |

Result: Consensus

The proposed process was to start with an empty white paper working draft and then iteratively get EWG approval for papers to be adopted into that working draft. This white paper working draft document, describing the proposed process, was published as [P3656R1].

We immediately realised that the present paper directly addresses the major work items proposed by [P3656R1], and prepared revision R2, now explicitly targeting the UB white paper, for EWG review.

At the WG21 meeting in June 2025 in Sofia, EWG reviewed this R2 of this paper and approved its adoption into the core language UB white paper working draft:

EWG Poll, Sofia, 2025-06-20

EWG encourages more work on P3100R2 and wants a step-by-step systematic review of P3100R2 to do per-clause approval for inclusion in the core language UB whitepaper (in telecons)

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 15 | 27 | 2 | 0 | 0 |
|  |  |  |  |  |

Result: Consensus

Furthermore, in the same session we gave a presentation to EWG, published in [P3754R0], outlining the wider, holistic strategy to systematically address core language UB in the C++ language that underpins this proposal. EWG reached consensus to use the diagram on slide 53 from that presentation (a.k.a. the “magic slide”), visualising our strategy, as a basis for the core language UB white paper:

EWG Poll, Sofia, 2025-06-20

EWG agrees that Timur’s (magic) slide 53 in P3754R0 is a good basis for the core language UB whitepaper, and asks that the Whitepaper editors make it so.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 14 | 28 | 2 | 1 | 0 |
|  |  |  |  |  |

Result: Consensus

An updated version of the diagram and the strategy description is available in Section 4 of this paper.

However, the telecons for per-clause approval of this paper into the white paper were never scheduled, and the pursuit of the white paper as a ship vehicle has stalled. To make progress, we decided to instead target C++29 with the present proposal. While EWG was busy finishing C++26, SG23 (Safety & Security) reviewed revision R4, now targeting C++29, and approved it with strong consensus:

SG23 Poll, Kona, 2025-11-07

SG23 supports the direction of P3100R4 and recommends its inclusion in C++29

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 15 | 12 | 1 | 1 | 2 |
|  |  |  |  |  |

Result: Consensus

Finally, at the WG21 meeting in March 2026 in Croydon, EWG reviewed revision R5 of this paper and encouraged this direction. We were told to come back to EWG with full wording:

EWG Poll, Croydon, 2026-03-26

Update P3100R5 by applying the presented rules to all cases of runtime-checkable UB in the standard, as listed in appendix A, and bring it back to EWG for case-by-case wording review

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 39 | 19 | 5 | 2 | 1 |
|  |  |  |  |  |

Result: Strong consensus

The full wording requested by EWG is available in the present revision.

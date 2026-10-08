Verdict: Strong (10/14)

The paper gives a reasonably solid account of why the feature cannot be achieved through ordinary library code and why compiler involvement is necessary, and it points to concrete implementation experience. The support is thinnest around the breadth of the affected audience and around how the proposed facility would coordinate with existing tagged-pointer code, where the paper asserts more than it demonstrates.

- The strongest part of the paper is its explanation that conforming library implementations cannot express this functionality, particularly because `reinterpret_cast` is unavailable during constant evaluation.
- The paper also establishes meaningful implementation experience through a prior libc++ and Clang implementation that is publicly accessible.
- The discussion of prior art and alternatives is adequately grounded, including the explicit narrowing of scope to low bits known to be zero from alignment.
- The most glaring omission is the lack of established evidence for who is affected and how the proposal would interoperate with existing tagged-pointer code, since both are asserted rather than shown in detail.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.00/14)

Provisionally addressed: 7 of 7. Provisional points: 10.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.00   corroborated 9.33   accumulate 11.00   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.50  coordination 0.17  insufficiency 1.50  implementation 2.00
sample agreement: 79 of 84 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.00 / 10.00 / 10.00   (all 3 samples: 10.00)
headings: h3 11   <- NOT h2, check the unit list
on threshold: vehicle, insufficiency, implementation
splits: motivation[6] 0/0/1  audience[4] 1/2/1  audience[5] 0/0/1  coordination[8] 1/0/0
        implementation[4] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/1  -> 0.33
  [7] Things it's not doing and why                1/1/1  -> 1.00
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 2 (found by 3 of 36 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 36 passes): this is not a owning pointer, it's a tool to build one
candidate 4 (found by 3 of 36 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.

## audience - grade 0.83 (fired in 2 of 12 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/2/1  -> 1.33
  [5] Implementation experience                    0/0/1  -> 0.33
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Pointer tagging is widely known and used technique
candidate 2 (found by 1 of 36 passes): Pointer tagging is widely known and used technique ([Glasgow Haskell Compiler](https://takenobu-hs.github.io/downloads/haskell_ghc_illustrated.pdf), LLVM's `[PointerIntPair](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerIntPair.h#L80)`, `[PointerUnion](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerUnion.h#L112)`, [CPython's garbage collector](https://blog.codingconfessions.com/p/cpython-garbage-collection-internals), [Objective C](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) / Swift, Chrome's [V8 JavaScript engine](https://v8.dev/blog/pointer-compression), [GAP](https://www.gap-system.org), [OCaml](https://ocaml.org/docs/memory-representation#distinguishing-integers-and-pointers-at-runtime), [PBRT](https://pbr-book.org/4ed/Utilities/Containers_and_Memory_Management#TaggedPointers)).
candidate 3 (found by 1 of 36 passes): Old version of this proposal has been implemented within libc++ & clang and it is accessible on github and compiler explorer.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Things it's not doing and why                1/1/1  -> 1.00
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Alternative way to implement `constexpr` support (for compiler which don't have heavy pointer representation in their interprets) is inserting a hidden intermediate object holding the metadata and pointer to original object.
candidate 2 (found by 3 of 36 passes): LLVM has design with a pointer, but this design is not symmetric with rest of standard library.
candidate 3 (found by 3 of 36 passes): *modeling pointer* — this is not a pointer type, access to the pointer should be explicitly visible
candidate 4 (found by 2 of 36 passes): This proposal doesn't propose accessing any other bits other than low-bits which are known to be zero due alignment. [SG1 doesn't want](https://github.com/cplusplus/papers/issues/1903#issuecomment-2488661934) to standardize access to high-bits as it's considered dangerous and non-portable.

## vehicle - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/1/1  -> 1.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 2 (found by 3 of 36 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 36 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Implementation experience                    0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      1/0/0  -> 0.33
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Integral part of the proposed design is ability to interact with such existing code and migrate away from it.

## insufficiency - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/1/1  -> 1.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 2 (found by 3 of 36 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 36 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/0/0  -> 0.33
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Old version of this proposal has been implemented within libc++ & clang and it is accessible on [github](https://github.com/llvm/llvm-project/pull/111861) and [compiler explorer](https://compiler-explorer.com/z/Y884arzjd).
candidate 2 (found by 1 of 36 passes): This functionality widely supported can't be expressed in a standard conforming way.

-->

Verdict: Excellent (12/14)

The paper gives solid support for the core technical need and for the impossibility of a pure-library solution, but its case is thinner when it comes to showing who would actually use the facility and how it would fit with existing standards and interfaces. The strongest material concerns implementation experience and the need for compiler involvement, while the weakest concerns the breadth and concreteness of the affected audience.

- The paper clearly establishes that the facility cannot be implemented as a conforming library and requires compiler support, particularly because `reinterpret_cast` is unavailable during constant evaluation.
- It also establishes meaningful implementation experience through a prior version implemented in libc++ and Clang, with accessible code and a compiler explorer link.
- The discussion of prior art and alternatives is credited as established, especially the recognition that existing LLVM intrinsics and library designs are not symmetric with the standard library.
- The most glaring omission is the lack of established evidence about who is affected, since the paper lists many known users of pointer tagging but does not demonstrate that they would adopt or benefit from this specific standardized facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.17/14)

Provisionally addressed: 7 of 7. Provisional points: 12.17 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.17   corroborated 12.00   accumulate 12.33   max 14.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 2.00  coordination 1.17  insufficiency 2.00  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 12.50 / 12.00 / 12.00   (all 3 samples: 12.17)
headings: h3 12   <- NOT h2, check the unit list
on threshold: audience, coordination, implementation
splits: motivation[7] 1/0/0  prior_art[8] 0/2/2  coordination[4] 1/0/0  coordination[9] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Invalid pointers                             2/2/2  -> 2.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Design                                       1/0/0  -> 0.33
  [8] Things it's not doing and why                1/1/1  -> 1.00
  [9] Impact on existing code                      1/1/1  -> 1.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This paper proposes a new library non-owning pointer and value pair which has ability to store small amount of information in a *tag* in alignment low-bits.
candidate 2 (found by 3 of 39 passes): This is giving us another motivational example why we need the proposed facility, because normal (or existing) pointer tagging approaches thru `uintptr_t` loos the pointer authentication.
candidate 3 (found by 3 of 39 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 4 (found by 3 of 39 passes): these are not portable and are subject of being enabled/disabled as an OS setting, this would create at best ABI problems

## audience - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Invalid pointers                             0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Design                                       0/0/0  -> 0.00
  [8] Things it's not doing and why                0/0/0  -> 0.00
  [9] Impact on existing code                      0/0/0  -> 0.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Pointer tagging is widely known and used technique ([Glasgow Haskell Compiler](https://takenobu-hs.github.io/downloads/haskell_ghc_illustrated.pdf), LLVM's `[PointerIntPair](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerIntPair.h#L80)`, `[PointerUnion](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerUnion.h#L112)`, [CPython's garbage collector](https://blog.codingconfessions.com/p/cpython-garbage-collection-internals), [Objective C](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) / Swift, Chrome's [V8 JavaScript engine](https://v8.dev/blog/pointer-compression), [GAP](https://www.gap-system.org), [OCaml](https://ocaml.org/docs/memory-representation#distinguishing-integers-and-pointers-at-runtime), [PBRT](https://pbr-book.org/4ed/Utilities/Containers_and_Memory_Management#TaggedPointers)).

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Invalid pointers                             2/2/2  -> 2.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Design                                       2/2/2  -> 2.00
  [8] Things it's not doing and why                0/2/2  -> 1.33
  [9] Impact on existing code                      1/1/1  -> 1.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): For unmasking there is already `ptr.mask` LLVM's builtin, but there is no similar intrinsic to do the tagging.
candidate 2 (found by 3 of 39 passes): LLVM has design with a pointer, but this design is not symmetric with rest of standard library.
candidate 3 (found by 3 of 39 passes): Integral part of the proposed design is ability to interact with such existing code and migrate away from it.
candidate 4 (found by 2 of 39 passes): This proposal only proposes interface to accessing low bits for storing / reading a tag value, not observing bits of a pointer.

## vehicle - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/1/1  -> 1.00
  [5] Invalid pointers                             2/2/2  -> 2.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Design                                       0/0/0  -> 0.00
  [8] Things it's not doing and why                0/0/0  -> 0.00
  [9] Impact on existing code                      1/1/1  -> 1.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 2 (found by 3 of 39 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 39 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.
candidate 4 (found by 2 of 39 passes): Providing proposed `pointer_tag_pair` gives ability to user to express what it's happening, and implementations can provide facility which will keep valid signature even thru `.tagged_pointer()`.

## coordination - grade 1.17 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/0/0  -> 0.33
  [5] Invalid pointers                             2/2/2  -> 2.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Design                                       0/0/0  -> 0.00
  [8] Things it's not doing and why                0/0/0  -> 0.00
  [9] Impact on existing code                      1/0/0  -> 0.33
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): It's there only to be able to be passed thru C and legacy interfaces (without depending on `reinterpret_cast`).
candidate 2 (found by 1 of 39 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 3 (found by 1 of 39 passes): Integral part of the proposed design is ability to interact with such existing code and migrate away from it.

## insufficiency - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  1/1/1  -> 1.00
  [5] Invalid pointers                             2/2/2  -> 2.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Design                                       0/0/0  -> 0.00
  [8] Things it's not doing and why                0/0/0  -> 0.00
  [9] Impact on existing code                      1/1/1  -> 1.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This functionality widely supported can't be expressed in a standard conforming way.
candidate 2 (found by 3 of 39 passes): This is giving us another motivational example why we need the proposed facility, because normal (or existing) pointer tagging approaches thru `uintptr_t` loos the pointer authentication.
candidate 3 (found by 3 of 39 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 4 (found by 3 of 39 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.

## implementation - grade 2.00  [binary: max] (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Invalid pointers                             0/0/0  -> 0.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Design                                       0/0/0  -> 0.00
  [8] Things it's not doing and why                0/0/0  -> 0.00
  [9] Impact on existing code                      0/0/0  -> 0.00
  [10] Proposed changes to wording                  0/0/0  -> 0.00
  [11] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [12] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [13] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Old version of this proposal has been implemented within libc++ & clang and it is accessible on [github](https://github.com/llvm/llvm-project/pull/111861) and [compiler explorer](https://compiler-explorer.com/z/TWPEKxo15).

-->

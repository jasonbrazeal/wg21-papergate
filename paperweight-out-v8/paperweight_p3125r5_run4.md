Verdict: Strong (9/14)

The paper offers solid support in the areas that are easiest to demonstrate—prior art, the need for compiler involvement, and implementation experience—but its case thins considerably when it comes to showing who would actually use the feature and why the problem is urgent enough to standardize. The most glaring gap is the complete absence of any discussion of coordination with existing implementations, ABIs, or adjacent standardization efforts.

- The strongest support is the concrete implementation experience, including a working libc++ and clang prototype and a long list of real-world systems that already use pointer tagging.
- The paper also clearly establishes that the feature cannot be done as a pure library and requires compiler support, which justifies bringing it to the standard.
- The discussion of prior art and alternatives is well grounded, with named interfaces in Rust, D, and Zig and an acknowledgment of existing LLVM intrinsics.
- The thinnest part is the absence of any coordination or interoperability analysis, leaving unaddressed how this would fit with existing ABIs, vendor extensions, or other standardization work.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.00   accumulate 11.00   max 11.33

## SUMMARY
grades: motivation 1.17  audience 1.00  prior_art 2.00  vehicle 1.50  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 9.50 / 9.00 / 9.00   (all 3 samples: 9.17)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience, vehicle, insufficiency, implementation
splits: motivation[5] 2/1/1  prior_art[7] 1/0/1  implementation[4] 0/1/0
## END SUMMARY

## motivation - grade 1.17 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Implementation experience                    2/1/1  -> 1.33
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                1/1/1  -> 1.00
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This functionality is also usable in `constexpr` environment. It's meant to be a building tool to build more advanced data-structures and also last requirement for `atomic<std::shared_ptr<T>>` to be constexpr.
candidate 2 (found by 3 of 36 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 36 passes): these are not portable and are subject of being enabled/disabled as an OS setting, this would create at best ABI problems
candidate 4 (found by 3 of 36 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.

## audience - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Implementation experience                    0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Pointer tagging is widely known and used technique ([Glasgow Haskell Compiler](https://takenobu-hs.github.io/downloads/haskell_ghc_illustrated.pdf), LLVM's `[PointerIntPair](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerIntPair.h#L80)`, `[PointerUnion](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerUnion.h#L112)`, [CPython's garbage collector](https://blog.codingconfessions.com/p/cpython-garbage-collection-internals), [Objective C](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) / Swift, Chrome's [V8 JavaScript engine](https://v8.dev/blog/pointer-compression), [GAP](https://www.gap-system.org), [OCaml](https://ocaml.org/docs/memory-representation#distinguishing-integers-and-pointers-at-runtime), [PBRT](https://pbr-book.org/4ed/Utilities/Containers_and_Memory_Management#TaggedPointers)).

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Things it's not doing and why                1/0/1  -> 0.67
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [Rust](https://doc.rust-lang.org/std/primitive.pointer.html#examples-9), [Dlang](https://dlang.org/library/std/bitmanip/tagged_pointer.html), or [Zig](https://zig.news/orgold/type-safe-tagged-pointers-with-comptime-ghi) has an interface for pointer tagging.
candidate 2 (found by 3 of 36 passes): For unmasking there is already `ptr.mask` LLVM's builtin, but there is no similar intrinsic to do the tagging.
candidate 3 (found by 3 of 36 passes): LLVM has design with a pointer, but this design is not symmetric with rest of standard library.
candidate 4 (found by 2 of 36 passes): Integral part of the proposed design is ability to interact with such existing code and migrate away from it.

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

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Implementation experience                    0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidates: (none validated)

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
  [4] Introduction and motivation                  0/1/0  -> 0.33
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Old version of this proposal has been implemented within libc++ & clang and it is accessible on [github](https://github.com/llvm/llvm-project/pull/111861) and [compiler explorer](https://compiler-explorer.com/z/Y884arzjd).
candidate 2 (found by 1 of 36 passes): Pointer tagging is widely known and used technique ([Glasgow Haskell Compiler](https://takenobu-hs.github.io/downloads/haskell_ghc_illustrated.pdf), LLVM's `[PointerIntPair](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerIntPair.h#L80)`, `[PointerUnion](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerUnion.h#L112)`, [CPython's garbage collector](https://blog.codingconfessions.com/p/cpython-garbage-collection-internals), [Objective C](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) / Swift, Chrome's [V8 JavaScript engine](https://v8.dev/blog/pointer-compression), [GAP](https://www.gap-system.org), [OCaml](https://ocaml.org/docs/memory-representation#distinguishing-integers-and-pointers-at-runtime), [PBRT](https://pbr-book.org/4ed/Utilities/Containers_and_Memory_Management#TaggedPointers)).

-->

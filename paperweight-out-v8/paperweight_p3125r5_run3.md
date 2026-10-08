Verdict: Strong (9/14)

The paper offers a mixed case for standardization, with its strongest support concentrated in the technical necessity for compiler involvement and in the existence of prior implementation experience. The argument is thinnest around the affected audience and the practical motivation, where the paper asserts widespread use and hardware support but does not substantiate those claims with concrete evidence or usage data.

- The paper clearly establishes that the functionality cannot be implemented as a conforming library and requires compiler support, especially for constexpr contexts.
- The paper provides credible implementation experience through a prior clang and libc++ implementation available on GitHub and Compiler Explorer.
- The paper’s discussion of prior art and alternatives is grounded in specific references to LLVM, Rust, D, and Zig interfaces.
- The paper does not address coordination and interoperability with existing standards, ABIs, or other language features, leaving a significant gap in the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 8.00   accumulate 10.83   max 11.00

## SUMMARY
grades: motivation 1.17  audience 0.83  prior_art 2.00  vehicle 1.50  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.00 / 9.50 / 8.50   (all 3 samples: 9.00)
headings: h3 11   <- NOT h2, check the unit list
on threshold: audience, vehicle, insufficiency, implementation
splits: motivation[5] 1/2/1  motivation[7] 1/1/0  audience[4] 2/2/1  prior_art[7] 1/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 4 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Implementation experience                    1/2/1  -> 1.33
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                1/1/0  -> 0.67
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This functionality is also usable in `constexpr` environment. It's meant to be a building tool to build more advanced data-structures and also last requirement for `atomic<std::shared_ptr<T>>` to be constexpr.
candidate 2 (found by 3 of 36 passes): This functionality can't be implemented as a pure library (`reinterpret_cast` is not allowed during constant evaluation) and needs compiler support in some form.
candidate 3 (found by 3 of 36 passes): It allows to express semantic clearly for a compiler instead of using an unsafe `reinterpret_cast` based techniques.
candidate 4 (found by 2 of 36 passes): this is not a pointer type, access to the pointer should be explicitly visible

## audience - grade 0.83 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/1  -> 1.67
  [5] Implementation experience                    0/0/0  -> 0.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): All major CPU vendors provides mechanism for pointer tagging (Intel's LAM linear address masking, AMD's Upper Address Ignore, ARM's TBI top byte ignore and MTE memory tagging extension).
candidate 2 (found by 1 of 36 passes): Pointer tagging is widely known and used technique ([Glasgow Haskell Compiler](https://takenobu-hs.github.io/downloads/haskell_ghc_illustrated.pdf), LLVM's `[PointerIntPair](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerIntPair.h#L80)`, `[PointerUnion](https://github.com/llvm/llvm-project/blob/8e5aa538caccef167e8096b2173fdaf2be9cc129/llvm/include/llvm/ADT/PointerUnion.h#L112)`, [CPython's garbage collector](https://blog.codingconfessions.com/p/cpython-garbage-collection-internals), [Objective C](https://alwaysprocessing.blog/2023/03/19/objc-tagged-ptr) / Swift, Chrome's [V8 JavaScript engine](https://v8.dev/blog/pointer-compression), [GAP](https://www.gap-system.org), [OCaml](https://ocaml.org/docs/memory-representation#distinguishing-integers-and-pointers-at-runtime), [PBRT](https://pbr-book.org/4ed/Utilities/Containers_and_Memory_Management#TaggedPointers)).
candidate 3 (found by 1 of 36 passes): Pointer tagging is widely known and used technique

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  2/2/2  -> 2.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Things it's not doing and why                1/1/2  -> 1.33
  [8] Impact on existing code                      1/1/1  -> 1.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): For unmasking there is already `ptr.mask` LLVM's builtin, but there is no similar intrinsic to do the tagging.
candidate 2 (found by 3 of 36 passes): LLVM has design with a pointer, but this design is not symmetric with rest of standard library.
candidate 3 (found by 3 of 36 passes): Integral part of the proposed design is ability to interact with such existing code and migrate away from it.
candidate 4 (found by 2 of 36 passes): [Rust](https://doc.rust-lang.org/std/primitive.pointer.html#examples-9), [Dlang](https://dlang.org/library/std/bitmanip/tagged_pointer.html), or [Zig](https://zig.news/orgold/type-safe-tagged-pointers-with-comptime-ghi) has an interface for pointer tagging.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgement                              0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] Introduction and motivation                  0/0/0  -> 0.00
  [5] Implementation experience                    2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Things it's not doing and why                0/0/0  -> 0.00
  [8] Impact on existing code                      0/0/0  -> 0.00
  [9] Proposed changes to wording                  0/0/0  -> 0.00
  [10] 20.1 General [mem.general]                   0/0/0  -> 0.00
  [11] 20.2 Memory [memory]                         0/0/0  -> 0.00
  [12] [17.3.2 Header <version> synopsis [versio... 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Old version of this proposal has been implemented within libc++ & clang and it is accessible on [github](https://github.com/llvm/llvm-project/pull/111861) and [compiler explorer](https://compiler-explorer.com/z/Y884arzjd).

-->

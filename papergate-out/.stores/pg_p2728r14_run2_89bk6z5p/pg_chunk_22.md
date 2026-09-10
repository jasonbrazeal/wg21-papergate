## 11 Changelog

### 11.1 Changes since R13

- Fix typo in Table 3-9 of error handling diagram pointed out during SG16 review (`ED A0` had been misspelled as `E0 A0`).
- Add design discussion about `.base_code_units()`.
- Loosen the wording to admit chunked (e.g. SIMD) implementations when the underlying range models `forward_range`: make `buf_`’s capacity an unspecified constant, allow `*read*` and `*read-reverse*` to transcode several input subsequences per invocation, and respecify `base()` and iterator equality positionally instead of in terms of the exposition-only members. Make `operator--` skip an ill-formed input subsequence’s replacement-character code units as a unit in `_or_error` views, mirroring `operator++`, since with chunking they can now appear in the middle of `buf_`. Specify explicitly that `*read-reverse*` leaves `current_` at the beginning of the first input subsequence it transcoded. Add corresponding design discussion.

### 11.2 Changes since R12

- Add example: transcoding into a fixed-size buffer without truncating code points.
- Add example: using `to_utf32` and `base()` for code point-aware substring replacement on cuneiform text, adapted from an ICU unit test.
- Give `utf_transcoding_error` and `to_utf_view_error_kind` unspecified underlying types, following the precedent of `memory_order`, `launch`, and `assertion_kind`. Fixing the underlying type (to `int` or `bool`) is an unnecessary constraint; an unspecified underlying type gives implementations freedom to choose a type suited to their layout and ABI needs.
- Remove `base()` from the transcoding iterator when the base range is an input range and not a forward range.
- Add `views::as_char` and `views::as_wchar_t`; it’s also useful to get UTF-encoded strings from `charN_t` types back into `char`/`wchar_t` as well as having the reverse direction.
- Fix subclause numbers in wording sections to use 25.7 consistently, matching the current working paper’s numbering for [range.adaptors].
- Add wording for changes to the `<ranges>` header synopsis in [ranges.syn].
- Expand “CTP” abbreviation to “constant template parameter” in [range.transcoding.overview].
- Add missing “Otherwise” before expression-equivalent clauses in [range.transcoding.overview] and [range.codeunitadaptor].

### 11.3 Changes since R11

- Refactor use of `std::nontype` to use `std::constant_wrapper` instead per [[P3948R1]](https://wg21.link/p3948r1).
- Remove back-pointer to parent view in iterator, restoring R7’s three-iterator design and borrowedness, based on precedent from `views::adjacent<N>`; and based on the fact that, since R10 implements the double-transcode optimization in the CPO, we no longer need the `*innermost-iter*` machinery that overcomplicated the R7 design.

### 11.4 Changes since R10

- Fix the wording around rejecting arrays for the code unit adaptors
- Add example for handling byte offsets and endianness

### 11.5 Changes since R9

- Replace bool OrError CTP with `to_utf_view_error_kind` enum class like ranges::subrange_kind
- Replace `to_utfX_view` classes with a single `to_utf_view` class with annoying constructor tags to make CTAD work, per SG9 feedback from Kona 2025, and remove related obsolete design discussion
- Fix a bug where the value type of `empty_view` was not set properly in the CPO when using an `_or_error` CPO
- Remove section stating that the concept of a CPO template is a “novelty” after it was pointed out in Kona 2025 that it has precedent in `views::adjacent_transform<N>` and elsewhere
- Don’t cache `begin()`
- Reject arrays of `charN_t` in the CPOs
- Implement double-transcode optimization in the CPOs

### 11.6 Changes since R8

- Fix const correctness bug in wording relating to noncopyable input iterators
- Use a std::inplace_vector instead of a std::array for buf_, allowing us to eliminate buf_last_ exposition-only member
- Simplify the implementation of `*to-utf-view-impl*`’s operators
- Rename `*utf-iterator*` to `*to-utf-view-impl*::*iterator*`
- Add a `*to-utf-view-impl*::*sentinel*` type
- Cache `begin()`
- Clean up wording
- Add `reserve_hint()` member functions
- Fix bug in `operator==` for input iterators
- Add additional design discussion
- Add `size()` member function when transcoding from and to UTF-32

### 11.7 Changes since R7

- Add playing card example.
- Remove `iterator_interface` from `*utf-iterator*`.
- Replace code unit views with range adaptor closure objects that are expression-equivalent to P3117 `transform_view`.
- Move `null_sentinel` and `null_term` into P3705.
- Remove `std::uc` namespace and replace it with `std::ranges` and `std::ranges::views`.
- Remove library EB.
- Change iterator to use a back-pointer to its parent view, removing borrowedness and quadratic stack size growth.
- Remove support for `char` and `wchar_t`.
- Rewrite most of the verbiage and add new diagrams.

### 11.8 Changes since R6

- Fix a bug in `null_sentinel_t` causing it not to satisfy `sentinel_for` by changing its `operator==` to return `bool`.
- Fix a bug in `null_sentinel_t` where it did not support non-copyable input iterators by having operator== take input iterators by reference.
- Rename `as_utfN` to `to_utfN` to emphasize that a conversion is taking place and to contrast with the code unit views, which remain named `as_charN_t`.
- Refactor `utf_view` into an exposition-only `*utf-view-impl*` class used as an implementation detail of separate `to_utf8_view`, `to_utf16_view`, and `to_utf32_view` classes, addressing broken deduction guides in the previous revision.
- Remove `project_view` and copy most of its implementation into separate `char8_view`, `char16_view`, and `char32_view` classes, addressing broken deduction guides in the previous revision.
- Change `utf_iterator` to an exposition-only member class of `*utf-view-impl*`.
- Eliminate iterator unpacking mechanism and replace it with an alternative solution to the problem of transcoding ranges wrapping other transcoding ranges. This simplifies the API at the expense of removing the transcoding iterator’s `begin()` and `end()` member functions and losing the ability to implement unpacking for user-defined UTF iterators.
- Remove `std::uc::format`.
- Make all concepts exposition-only.
- Remove `utf_transcoding_error_handler` mechanism.
- Introduce new error handling mechanism based on a new `utf_transcoding_error` enumeration which is returned by an `success()` member function of the transcoding view’s iterator.
- Remove ability to pass pointers to range adaptor closure objects, which violated the restriction that only ranges may be passed to range adaptor closure objects.
- Remove `std::format` and `std::ostream` functionality. It doesn’t make sense for this mechanism to be the only way we have to format/output `char8_t`; we can revisit this functionality when we have already figured out how to support e.g. `std::u8string`.
- Replace code examples with new ones reflecting API changes.
- Provide a reference implementation.

### 11.9 Changes since R5

- Simplify the complicated constraint on the comparison operator for `null_sentinel_t`.
- Introduce `ranges::project_view`, and implement `charN_view`s in terms of that.
- Convert the `utfN_view`s to aliases, rather than individual classes.

### 11.10 Changes since R4

- Replace `unpacking_owning_view` with `unpacking_view`, and use it to do unpacking, rather than sometimes doing the unpacking in the adaptor.
- Ensure `const` and non-`const` overloads for `begin` and `end` in all views.
- Move `null_sentinel_t` to `std`, remove its `base` member function, and make it useful for more than just pointers, based on SG-9 guidance.

### 11.11 Changes since R3

- Changed the definition of the `code_unit` concept, and added `as_charN_t` adaptors.
- Removed the utility functions and Unicode-related constants, except `replacement_character`.
- Changed the constraint on `utf_iterator` slightly.
- Change `null_sentinel_t` back to being Unicode-specific.

### 11.12 Changes since R2

- Add `noexcept` where appropriate.
- Remove non-essential constants and utility functions, and elaborate on the usage of the ones that remain.
- Note differences from similar elements proposed in [[P1629R1]](https://wg21.link/p1629r1).
- Extend the examples slightly.
- Correct an error in the description of the view adaptors’ semantics, and provide several examples of their use.

### 11.13 Changes since R1

- Reintroduce the transcoding-from-a-buffer example.
- Generalize `null_sentinel_t` to a non-Unicode-specific facility.
- In utility functions that search for ill-formed encoding, take a range argument instead of a pair of iterator arguments.
- Replace `utf{8,16,32}_view` with a single `utf_view`.

### 11.14 Changes since R0

- When naming code points in interfaces, use `char32_t`.
- When naming code units in interfaces, use `charN_t`.
- Remove each eager algorithm, leaving in its corresponding view.
- Remove all the output iterators.
- Change template parameters to `utfN_view` to the types of the from-range, instead of the types of the transcoding iterators used to implement the view.
- Remove all make-functions.
- Replace the misbegotten `as_utfN()` functions with the `as_utfN` view adaptors that should have been there all along.
- Add missing `utf_transcoding_error_handler` concept.
- Turn `unpack_iterator_and_sentinel` into a CPO.
- Lower the UTF iterator concepts from bidirectional to input.


## 12 Relevant Polls/Minutes

### 12.1 SG16 review of P2728R13 on 2026-05-27 (Telecon)

- [Minutes](https://wiki.isocpp.org/2026_Telecons:SG16Teleconference2026-05-27)

No polls were taken during this review.

### 12.2 SG16 review of P2728R12 on 2026-05-13 (Telecon)

- [Minutes](https://wiki.isocpp.org/2026_Telecons:SG16Teleconference2026-05-13)

No polls were taken during this review.

### 12.3 SG9 review of P2728R9 on 2025-11-06 during Kona 2025

- [Minutes](https://wiki.isocpp.org/2025-11_Kona:NotesSG9P2728R8)

**POLL:** We want to remove the null terminator of char arrays (if present) so that `u8"abc" | to_utf32` (and `to_utf8`, `to_utf16`) do not include the null terminator in the resulting output.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 0 | 2 | 2 | 3 | 1 |

**Attendance**: 10 (2 abstentions)

**Author Position:** A, F

**Outcome:** Consensus against

**POLL:** We want to ban char arrays as input to `to_utfX` to prevent accidental inclusion of the null terminator of a string literal.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 4 | 3 | 1 | 0 | 0 |

**Attendance**: 10 (2 abstentions)

**Author Position:** F, SF

**Outcome:** Strong consensus in favor

**ACTION ITEM:** Figure out whether we need to cache `begin()`.

**POLL:** Simplify the `to_utfX_view` classes by just having a single templated view class similar to `scan_view` (with potentially annoying constructor tags to make CTAD work) and focus on usability with the CPOs only.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 0 | 7 | 1 | 1 | 0 |

**Attendance**: 9 (0 abstentions)

**Author Position:** N

**Outcome:** Consensus in favor

**POLL:** We want to optimize nested `to_utf_view`s.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 1 | 4 | 4 | 0 | 0 |

**Attendance**: 9 (0 abstentions)

**Author Position:** N

**Outcome:** Consensus in favor

**ACTION ITEM:** Come up with more examples where nested `to_utf_view`s occur in practice to explore whether a designated CPO approach is feasible.

### 12.4 Unofficial SG9 review of P2728R7 during Wrocław 2024

SG9 members provided unofficial guidance that the `.success()` member function on the `*utf-iterator*` wasn’t workable and encouraged providing views with `std::expected` as a value type.

### 12.5 SG16 review of P2728R6 on 2023-09-13 (Telecon)

- [Minutes](https://github.com/sg16-unicode/sg16-meetings/blob/master/README-2023.md#september-13th-2023)

No polls were taken during this review.

### 12.6 SG16 review of P2728R6 on 2023-08-23 (Telecon)

- [Minutes](https://github.com/sg16-unicode/sg16-meetings/blob/master/README-2023.md#august-23rd-2023)

No polls were taken during this review.

### 12.7 SG9 review of [D2728R4](https://isocpp.org/files/papers/D2728R4.html) on 2023-06-12 during Varna 2023

- [Minutes](https://wiki.isocpp.org/2023-06_Varna:P2728)

**POLL:** utf_iterator should be a separate type and not nested within utf_view

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 1 | 2 | 1 | 0 | 1 |

**Attendance:** 8 (3 abstentions)

**# of Authors:** 1

**Author Position:** F

**Outcome:** Weak consensus in favor

SA: Having a separate type complexifies the API

### 12.8 SG16 review of P2728R0 on 2023-04-12 (Telecon)

- [Minutes](https://github.com/sg16-unicode/sg16-meetings/blob/master/README-2023.md#april-12th-2023)

**POLL:** SG16 would like to see a version of P2728 without eager algorithms.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 4 | 2 | 0 | 1 | 0 |

**Attendance:** 10 (3 abstentions)

**Outcome:** Consensus in favor

**POLL:** UTF transcoding interfaces provided by the C++ standard library should operate on charN_t types, with support for other types provided by adapters, possibly with a special case for char and wchar_t when their associated literal encodings are UTF.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 5 | 1 | 0 | 0 | 1 |

**Attendance:** 9 (2 abstentions)

**Outcome:** Strong consensus in favor

Author’s note: More commentary on this poll is provided in the section “Discussion of whether transcoding views should accept ranges of `char` and `wchar_t`”. But note here that the authors doubt the viability of “a special case for char and wchar_t when their associated literal encodings are UTF”, since making the evaluation of a concept change based on the literal encoding seems like a flaky move; the literal encoding can change TU to TU.

### 12.9 SG16 review of P2728R0 on 2023-03-22 (Telecon)

- [Minutes](https://github.com/sg16-unicode/sg16-meetings/blob/master/README-2023.md#march-22nd-2023)

No polls were taken during this review.

**POLL:** `char32_t` should be used as the Unicode code point type within the C++ standard library implementations of Unicode algorithms.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 6 | 0 | 1 | 0 | 0 |

**Attendance:** 9 (2 abstentions)

**Outcome:** Strong consensus in favor


## 13 Special Thanks

Zach Laine, for writing revisions one through six of the paper and implementing Boost.Text.

Jonathan Wakely, for implementing P2728R6, and design guidance.

Robert Leahy and Gašper Ažman, for design guidance.

The Beman Project, for helping support the reference implementation.


## 14 References

[CVE-2007-3917] NVD - CVE-2007-3917.

https://nvd.nist.gov/vuln/detail/CVE-2007-3917

[Definitions] The Unicode Standard, Version 17.0, §3.4 Characters and
Encoding.

https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G2212

[N2902] JeanHeyd Meneide. Restartable and Non-Restartable Functions for
Efficient Character Conversions, revision 6.

https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2902.htm

[Null-terminated multibyte strings] Null-terminated multibyte strings.

https://en.cppreference.com/w/c/string/multibyte.html

[P0244R2] Tom Honermann. 2017-06-13. Text_view: A C++ concepts and range
based character encoding and code point enumeration library.

https://wg21.link/p0244r2

[P1629R1] JeanHeyd Meneide. 2020-03-02. Transcoding the world - Standard
Text Encoding.

https://wg21.link/p1629r1

[P2871R3] Alisdair Meredith. 2023-12-18. Remove Deprecated Unicode
Conversion Facets From C++26.

https://wg21.link/p2871r3

[P2873R2] Alisdair Meredith, Tom Honermann. 2024-07-06. Remove
Deprecated locale category facets for Unicode from C++26.

https://wg21.link/p2873r2

[P3117R1] Zach Laine, Barry Revzin, Jonathan Müller. 2024-12-15.
Extending Conditionally Borrowed.

https://wg21.link/p3117r1

[P3725R3] Nicolai Josuttis. 2026-03-24. Filter View Extensions for Safer
Use, Rev 3.

https://wg21.link/p3725r3

[P3948R1] Matthias Kretz. 2026-03-24. constant_wrapper is the only tool
needed for passing constant expressions.

https://wg21.link/p3948r1

[Substitution] The Unicode Standard, Version 17.0, §3.9.6 Substitution
of Maximal Subparts.

https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G66453

[SubstitutionExamples] The Unicode Standard, Version 17.0, §3.9.6
Substitution of Maximal Subparts.

https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G67519

[wesnoth] The Battle for Wesnoth,

“fixed a crash if the client
recieves invalid utf-8.”

https://github.com/wesnoth/wesnoth/commit/c5bc4e2a915ddf53b63f292f587526aaa39a96aa

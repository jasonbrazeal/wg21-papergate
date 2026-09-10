---
title: "Quantities and units library"
document: P3045R9
date: 2026-06-12
audience: LEWG Library Evolution Working Group,SG6 Numerics,SG16 Unicode,SG20 Education
reply-to:
  - "Mateusz Pusz (Train IT) <mateusz.pusz@gmail.com>"
  - "Dominik Berner <dominik.berner@gmail.com>"
  - "Johel Ernesto Guerrero Peña <johelegp@gmail.com>"
  - "Chip Hogg (Aurora Innovation) <charles.r.hogg@gmail.com>"
  - "Nicolas Holthaus <nholthaus@gmail.com>"
  - "Roth Michaels (Native Instruments) <isocxx@rothmichaels.us>"
  - "Vincent Reverdy <vince.rev@gmail.com>"
---


## 1 Revision history

### 1.1 Changes since [[P3045R8]](https://wg21.link/p3045r8)

- Quantity formatting chapter extended with a Two levels of format specification.
- [Text output open questions] chapter removed.
- Remaining references to the `final` keyword in definitions removed
- New Concept Hierarchy chapter added, documenting the building-block concepts, the character-specific concepts, the internal representation concepts, and the public `RepresentationOf` concept.
- Vector/tensor magnitude redesign: `mp_units::norm()` replaced by `mp_units::magnitude()` as the primary CPO (with `norm`-named member/free functions accepted as fallbacks for linear-algebra library interoperability).
- New `disable_vector<T>` opt-out customization point added, with `std::complex<T>` opted out by default.
- Text output is now provided for `quantity_point` when its point origin equals `default_point_origin(R)`.
- `quantity_from_unit_zero()` renamed back to `quantity_from_zero()` with its constraint simplified to `PO == default_point_origin(R)`, matching `zero()`.
- `quantity_point::in(unit)` semantics updated for units that carry a built-in `_point_origin_`: when the current point is at the default origin for its current unit (`PO == default_point_origin(R)`), `.in(target_unit)` now also switches the point origin to `target_unit._point_origin_` — matching the design proposed for logarithmic level units. Points at custom origins continue to perform a pure unit-scale conversion.

### 1.2 Changes since [[P3045R7]](https://wg21.link/p3045r7)

- New Navigating this proposal section added to orient readers of different backgrounds.
- WG21 wants it chapter updated with Croydon 2026 LEWG polls showing strong consensus support
- Dependencies on other proposals table updated.
- Broken table in Quantity specification chapter fixed.
- `RepresentationOf` concept updated.
- `quantity_from_zero()` renamed to `quantity_from_unit_zero()`, and `zeroth_point_origin<QS>` renamed to `natural_point_origin<QS>`.
- `final` keyword removed from all symbolic-expression type definitions throughout code examples.
- Representation Types chapter added.
- New Hello units chapter added between Representation Types and Usage examples, tracing the Smoot example top-down through all framework layers.
- “Hello units” section in Usage examples renamed to “mp-units showcase” to avoid a name conflict with the new chapter.
- Library namespace chapter significantly extended.
- Quantity kind diagrams improved: `is_kind` connections in `quantities_of_dimensionless.svg` now use dotted lines.
- “Magnitude” terminology normalized.
- Audience tables added to Teachability chapter following [[P1700R0]](https://wg21.link/p1700r0) recommendations.
- Teaching impact beyond C++ section added to Teachability chapter to highlight the library’s broader pedagogical value for interdisciplinary education.

### 1.3 Changes since [[P3045R6]](https://wg21.link/p3045r6)

- Document metadata updated (added LEWG and SG20 to audience).
- Several chapters significantly condensed and unneeded content duplication removed.
- Compiler Explorer examples updated to match the latest version of [[mp-units]](https://mpusz.github.io/mp-units).
- Creating distinct quantity kinds with `is_kind` chapter added.
- Safety chapter redesigned to be scoped around six distinct safety levels.
- `AssociatedUnit` concept removed.
- Missing `PrefixableUnit` concept added.
- Direct comparison against literal `0` replaced the discussion of non-ideal alternatives
- `named_constant` support added.
- `pi` `mag_constant` renamed to `pi_c` to allow `π` be an identifier for a `named_constant`.
- `default_denominator` renamed to `default_solidus` in `unit_symbol_solidus` enum.
- `quantity_values` trait renamed to `representation_values`.
- `quantity::one()` static member function removed after LEWGI and SG6 feedback.
- Teachability chapter significantly expanded for SG20.

### 1.4 Changes since [[P3045R5]](https://wg21.link/p3045r5)

- Dependencies on other proposals chapter updated.
- Constraining a variable on the stack chapter extended.
- Usage examples links updated.
- Scaling overflow prevention chapter added.
- Concepts chapter updated.
- Storage tank example updated.
- Safe operations of vector and tensor quantities chapter updated.
- Superpowers of the unit `one` chapter updated.
- Symbols of scaled units chapter updated.
- “EQUIV{…}” replaced with “[…]” in the text output of common units.
- Inconsistencies with `std::chrono::duration` chapter added
- [Complex operations] chapter added.
- Integer division chapter extended.
- Bikeshedding concepts chapter added.
- Supported operations and their results chapter updated.
- Equality and equivalence chapter extended.
- [Obtaining common entities] chapter renamed to Arithmetics and changed.
- Negative constants chapter added.
- Many small cleanup changes in other chapters.

### 1.5 Changes since [[P3045R4]](https://wg21.link/p3045r4)

- Hardware voltage measurement readout example description fixed.
- WG21 wants it chapter added.
- `text_encoding` renamed to `character_set`.
- `mp_units` namespace usage replaced with `std`.
- `absolute` creation helper renamed to `point`.
- Expression templates renamed to symbolic expressions.
- Usage examples updated.
- “Minimal Viable Product (MVP) scope” refactored to Core Library Framework scope.
- An alternative of printing space ” ” for `half_high_dot` added.
- `QuantitySpecOf` and `UnitOf` concepts simplified.
- `QuantityOf` and `QuantityPointOf` concepts constrained with `ReferenceOf`.
- Conversions beyond quantity subkinds added to the Nested quantity kinds chapter.
- [[P2830R10]](https://wg21.link/p2830r10) referred in the Simplifying the resulting symbolic expressions chapter.
- Scaled units are now surrounded with `(...)` instead of `[...]` in the text output.
- Invalid [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) quote removed from the Unit formatting chapter.
- Explicit unit conversion example added to the Symbols of common units chapter.
- UTF-8 printing rules specified for `symbol_text`.
- `unit-symbol-solidus` alternative grammars added.
- Extensions to `std-format-spec` chapter added.
- [Text output open questions] chapter updated.
- Integer overflow chapter added.

### 1.6 Changes since [[P3045R3]](https://wg21.link/p3045r3)

- Quantity arithmetics chapter updated with improved quantity compound assignment.
- `𝜋` changed to `π` after SG16 feedback.
- `quantity_like_traits`, `quantity_point_like_traits`, `QuantityLike`, and `QuantityPointLike` refactored to use `explicit_import` and `explicit_export` flags instead of wrapping tag types.
- Unicode characters and their portable replacements chapter added.
- Framework-only class templates chapter added.
- Special values of a quantity chapter added.
- `RepresentationOf` concept refactored.
- *position vector* moved under *displacement* in the hierarchy of kind *length*.

### 1.7 Changes since [[P3045R2]](https://wg21.link/p3045r2)

- `ascii` renamed to `portable` and `unicode` renamed to `utf8`.
- `space_before_unit_symbol` alternatives chapter added.
- Prefixing units with prefixes chapter added.
- Bikeshedding `force_in(U)` chapter added.
- Bikeshedding `quantity::rep` chapter added.
- [Minimal Viable Product (MVP) scope] chapter extended.
- Binary operators chapter added.
- Interoperability with the `std::chrono` abstractions chapter extended.
- [`default_point_origin<Reference>`, `quantity_from_zero()`, and `zeroth_point_origin<QuantitySpec>`] chapter added.
- Multiply syntax commutativity chapter added.
- Quantity specifications and Bikeshedding `quantity_spec` chapters added.
- Bikeshedding `reference` chapter added.
- `𝜋` added as an alias for `pi`
- Library namespace chapter added.

### 1.8 Changes since [[P3045R1]](https://wg21.link/p3045r1)

- Scope of this proposal chapter added.
- Dimensions, quantity specification, units, and point origins marked `final`.
- `delta` and `absolute` creation helpers added to improve readability of the affine space entities creation.
- `std::remove_const` was not needed in prefixes definitions.
- Compiler Explorer links updated to reflect the latest API changes.
- Text output and Safety chapters reordered.
- `inline` dropped from `inline constexpr` variable templates (based on [CWG2387](https://cplusplus.github.io/CWG/issues/2387.html))
- After consulting with the LEWGI in St. Lois, `q.in<Representation>(unit)` support added despite possible `template` disambiguator drawbacks.
- `quantity_point_like_traits` member functions refactored to not depend on `quantity`-like abstractions.
- `unit_can_be_prefixed` removed from the design.
- Radians and degrees support chapter added.
- [`delta` and `absolute` creation helpers] chapter added.
- Unit symbols chapter added.
- Superpowers of the unit `one` chapter added.
- Hardware voltage measurement readout chapter with a code example added.
- Why do we need typed quantities? chapter improved.
- Code examples in the Converting between quantities of the same kind chapter fixed and improved.
- Symbols of scaled units and Symbols of common units chapters added.
- New style of definitions chapter extended.
- `mag_pi` replaced with `mag<pi>`
- Value conversions chapter added.
- Common units chapter added.
- [Text output open questions] chapter added.
- [Minimal Viable Product (MVP) scope] chapter added.
- Operations on units, dimensions, quantity types, and references chapter updated.
- Units chapter added.
- Common unit magnitude chapter added.
- Addition and subtraction chapter extended with the paragraph about irrational magnitudes.
- “Lack of convertibility from fundamental types” chapter refactored to [Convertibility from fundamental types].

### 1.9 Changes since [[P3045R0]](https://wg21.link/p3045r0)

- One more dependency added to the table in the Dependencies on other proposals chapter.
- [Safe unit conversions] chapter extended with more `value_cast` overloads.
- The affine space chapter rewritten nearly from scratch.
- [Magnitudes] chapter added.
- `qp.quantity_from_zero()` does not work for user’s named origins anymore.
- `qp.quantity_from()` now works with other quantity points as well.
- `basic_symbol_text` renamed to `symbol_text`.
- `[[nodiscard]]` removed from `symbol_text`.
- `symbol_text` constructors taking string literals made `consteval`.
- `symbol_text` now always stores `char8_t` and `char` versions of symbols.
- In case UTF-8 symbol is used, now it has to be provided as an UTF-8 (`u8`) literal.
- Symbols of derived dimensions added and the entire symbols generation text refactored into the Symbols for derived entities chapter.
- Quantity formatting refactored to the new syntax agreed with Victor Zverovich.
- Minor editorial changes and additional clarifications added to the Text output chapter.
- `mag<ratio{N, D}>` replaced with `mag_ratio<N, D>` so the `ratio` type becomes the implementation detail rather than the public interface of the library
- Compiler Explorer links updated to reflect the latest design changes in the library


## 2 Introduction

Several groups in the ISO C++ Committee reviewed the “P1935: A C++ Approach to Physical Units” [[P1935R2]](https://wg21.link/p1935r2) proposal in Belfast 2019 and Prague 2020. All those groups expressed interest in the potential standardization of such a library and encouraged further work. The authors also got valuable initial feedback that highly influenced the design of the V2 version of the [[mp-units]](https://mpusz.github.io/mp-units) library.

In the following years, the library’s authors focused on getting more feedback from the production about the design and developed version 2 of the [[mp-units]](https://mpusz.github.io/mp-units) library that resolves the issues raised by the users and Committee members. The features and interfaces of this version are close to being the best we can get with the current version of the C++ language standard.

This paper is authored by the [[mp-units]](https://mpusz.github.io/mp-units) library developers, the authors of other actively maintained similar libraries on the market, and other active members of the C++ physical quantities and units community who have worked on this subject for many years. We join our forces to say with one voice that we deeply care about standardizing such features as a part of the C++ Standard Library. Based on our long and broad experience in the subject, we agree that the interfaces we will provide in the upcoming proposals are the best we can get today in the C++ language.

During the Kona 2023 ISO C++ Committee meeting, we got repeating feedback that there should be one big, unified paper with all the contents inside. Addressing this requirement, this paper adds a detailed design description and also includes the most important parts of [[P2980R1]](https://wg21.link/p2980r1), [[P2981R1]](https://wg21.link/p2981r1), and [[P2982R1]](https://wg21.link/p2982r1). With this, we assume that [[P2981R1]](https://wg21.link/p2981r1) and [[P2982R1]](https://wg21.link/p2982r1) are superseded by this paper. The plan and scope described in [[P2980R1]](https://wg21.link/p2980r1) might still be updated based on the current progress and feedback from the upcoming discussions.

*Note: This paper is incomplete and many chapters are still missing. It is published to gather early feedback and possibly get acceptance for the major design decisions of the library. More details will arrive in the next revisions of this paper.*

### 2.1 Navigating this proposal

This proposal is designed to serve multiple audiences, from beginners learning type-safe programming to framework developers extending the library’s core. The Teachability chapter includes audience tables (following [[P1700R0]](https://wg21.link/p1700r0)) that map library features to four distinct user populations: Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).

Most readers—whether evaluating the proposal for standardization or planning to use the library—need only understand the core usage patterns described in API overview and Usage examples. The vast majority of users will interact solely with predefined units from standard systems (SI, CGS, etc.) using intuitive multiply syntax and automatic unit conversions. More advanced topics like custom quantity hierarchies, affine space abstractions, and framework extension points are clearly marked and can be deferred or skipped entirely by casual users.


## 3 Scope of this proposal

This paper describes and defines a generic framework for quantities and units library. Such framework should allow modeling various systems of quantities and units customized according to specific user’s needs. Such systems can be embraced with the affine space abstractions to provide dimension-, unit-, representation-, quantity kind-, quantity-, and affine space-safe abstractions for many industries.

Beyond physical units, this library may also provide long-awaited functionality for the C++ community. It enables creating strongly-typed wrappers for fundamental types to prevent bugs that arise from accidentally mixing semantically different values.

Even if mentioned, this paper does not propose standardizing any systems of quantities or units. Such definitions will arrive in subsequent proposals.

In the extreme case, we can even discuss just providing a library framework in the first C++ standard and standardize systems and additional utilities (e.g., math) in the next iterations.


## 4 Terms and definitions

This document consistently uses the official metrology vocabulary defined in the [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) and [[JCGM 200:2012]](https://jcgm.bipm.org/vim/en).


## 5 Impact on the C++ standard

This change is purely additive. It does not change, fix, or break any of the existing tools in the C++ standard library.

### 5.1 Interaction with `std::chrono` types and `std::ratio`

The only interaction of this proposal with the C++ standard facilities is the compatibility mode with `std::chrono` types (`duration` and `time_point`) described in Interoperability with the `std::chrono` abstractions.

We should also mention the potential confusion of users with having two different ways to deal with time abstractions in the C++ standard library. If this proposal gets accepted:

- `std::chrono` abstractions together with `std::ratio` should be used primarily to deal with clocks, calendars, and threading facilities,
- abstractions introduced in this proposal should be used in all other use cases (e.g., physical quantities equations).

### 5.2 Dependencies on other proposals

The features in this chapter are heavily used in the library but are not domain-specific. Having them standardized (instead of left as exposition-only) could not only improve this library’s specification, but also serve as an essential building block for tools in other domains that we can get in the future from other authors.

| Feature | Priority | Papers | Description |
| --- | --- | --- | --- |
| `std::basic_fixed_string` | 1 | [[P3094R6]](https://wg21.link/p3094r6) | String-like structural type with inline storage (can be used as an NTTP). |
| Extending NTTPs | 2 | [[P3380R1]](https://wg21.link/p3380r1) | Avoiding public members in classes. |
| User control of associated entities | 2 | [[P2822R2]](https://wg21.link/p2822r2) | ADL for NTTP parameters. |
| `template = delete` | 2 | [[P2041R1]](https://wg21.link/p2041r1) | Deleting primary variable templates for customization points. |
| Preventing value truncation | 2 | [[P0870R5]](https://wg21.link/p0870r5), [[P2509R1]](https://wg21.link/p2509r1) | Type traits stating if the conversion from one type to another is narrowing/value preserving or not. |
| Format context rebind | 2 | ??? | Possibility to override the format string in the parse and format contexts. |
| Grouping numbers in `std-format-spec` | 2 | ??? | Extensions to `std-format-spec`. |
| Number concepts | 2 | [[P3003R0]](https://wg21.link/p3003r0) | Concepts for vector- and point-space numbers. |
| SFINAEable constexpr exceptions | 3 | [[P3679R0]](https://wg21.link/p3679r0) | Much improved error messages. |
| A Simple Approach to Universal Template Parameters | 3 | [[P2989R2]](https://wg21.link/p2989r2) | Uniform handling of types and NTTPs in the generic interfaces. |
| Compile-time prime numbers | 3 | [[P3133R0]](https://wg21.link/p3133r0) | Compile-time facilities to break any integral value to a product of prime numbers and their powers. |
| Constrained Numbers | 3 | [[P2993R0]](https://wg21.link/p2993r0) | Numerical type wrappers with values bounded to a provided interval (optionally with wraparound semantics). |

Priorities used above:

1. Mandatory to implement the library or exposed in its public interfaces.
2. Functional extension/improvement to the framework design but worse alternatives are currently available.
3. Not exposed in the official library’s interfaces but improves its use cases and internal implementation.


## 6 About authors

### 6.1 Dominik Berner

Dominik has 15+ years of C++ experience, primarily in regulated Med-Tech projects where type safety is critical. He is the author of [[SI library]](https://si.dominikberner.ch/doc), a physical quantities library focused on type-safe conversions and zero-overhead computation. His extensive experience debugging issues caused by incorrect primitive type usage in safety-critical contexts motivated his work on standardizing quantities and units. He joined this proposal to contribute his practical experience with production safety requirements and strongly-typed interfaces.

### 6.2 Johel Ernesto Guerrero Peña

Johel is a computing systems engineer and C++ programmer since 2014. He was a core contributor to [[nholthaus/units]](https://github.com/nholthaus/units) v3 (2018-2020), where he remodeled interfaces after `std::chrono::duration` and improved error messages. Since 2020, he has been a key contributor to [[mp-units]](https://mpusz.github.io/mp-units), designing and implementing `quantity_point` (affine space) and `quantity_kind` (distinct quantities of same dimension). He ensures the library’s alignment with [[JCGM 200:2012]](https://jcgm.bipm.org/vim/en) and [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) metrology standards, bringing rigorous domain expertise to the proposal.

### 6.3 Charles Hogg

Chip Hogg is a Staff Software Engineer at Aurora Innovation working on autonomous vehicle Motion Planning. He holds a PhD in Physics from Carnegie Mellon and worked as a staff scientist at NIST. He is the creator and lead developer of [[Au]](https://aurora-opensource.github.io/au), a widely-adopted zero-dependency units library with novel features including vector space magnitudes and adaptive overflow protection. His pioneering work on unit-safe interfaces at Uber ATG (2018) and Aurora (2021) established best practices for safe API design with quantities. He contributes his extensive production experience and focus on developer ergonomics to this proposal.

### 6.4 Nicolas Holthaus

Nicolas holds a B.S. in Computer Engineering (Summa Cum Laude) from Northwestern University. He designed real-time C++ software for aircraft survivability simulation at the U.S. Naval Air Warfare Center and has continued in safety-critical domains at MIT Lincoln Laboratory and STR. He is the author of [[nholthaus/units]](https://github.com/nholthaus/units), one of the most widely adopted C++ units libraries, with extensive deployment in modeling & simulation, agriculture, and geodesy. His practical experience with production units libraries across multiple domains informs the safety and usability requirements of this proposal.

### 6.5 Roth Michaels

Roth Michaels is a Principal Software Engineer at Native Instruments, working on audio and music software. With a degree in music composition and over a decade of experience in digital signal processing, analog audio, and acoustics, he brings unique domain expertise to the proposal. He has researched and prototyped domain-specific quantities and units for audio (samples, beats, frequency, power ratios) using [[mp-units]](https://mpusz.github.io/mp-units), contributing perspective on logarithmic quantities, non-linear relationships, and the needs of domains beyond traditional physics and engineering.

### 6.6 Mateusz Pusz

Mateusz is the creator and lead developer of [[mp-units]](https://mpusz.github.io/mp-units), the most popular and actively maintained C++ physical quantities and units library. With over 10 years of experience in the domain dating back to the [[LK8000]](http://lk8000.it) flight computer project, he designed [[mp-units]](https://mpusz.github.io/mp-units) to leverage modern C++ (Concepts, NTTP) for safety and user experience. He has unified the C++ quantities community by bringing together authors of other major libraries to collaborate on this proposal. Through numerous conference talks and workshops, he has become a recognized expert in physical quantities and units for C++.

### 6.7 Vincent Reverdy

Vincent is an astrophysicist and computer scientist at the French National Centre for Scientific Research (CNRS) and a member of the French delegation to the ISO C++ Committee. He authored [[P1930R0]](https://wg21.link/p1930r0) providing foundational context for quantities and units in C++. His current research focuses on the mathematical formalization of systems of quantities and units as an interdisciplinary problem spanning physics, mathematics, and computer science. He brings rigorous theoretical foundations and scientific computing perspective to this proposal.

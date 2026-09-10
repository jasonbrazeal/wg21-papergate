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

## 7 Motivation

This chapter describes why we believe that physical quantities and units should be part of a C++ Standard Library.

### 7.1 Safety concerns

It is no longer only the space industry or experienced pilots that benefit from the autonomous operations of some machines. We live in a world where more and more ordinary people trust machines with their lives daily. In the near future, we will be allowed to sleep while our car autonomously drives us home from a late party. As a result, many more C++ engineers are expected to write life-critical software today than it was a few years ago. However, writing safety-critical code requires extensive training and experience, both of which are in short demand. While there exists some standards and guidelines such as MISRA C++ [[MISRA C++]](https://misra.org.uk/misra-c-plus-plus/) with the aim of enforcing the creation of safe code in C++, they are cumbersome to use and tend to shift the burden on the discipline of the programmers to enforce these. At the time of writing, the C++ language does not change fast enough to enforce safe-by-construction code.

One of the ways C++ can significantly improve the safety of applications being written by thousands of developers is by introducing a type-safe, well-tested, standardized way to handle physical quantities and their units. The rationale is that people tend to have problems communicating or using proper units in code and daily life. Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.

The most famous and probably the most expensive example in the software engineering domain is the Mars Climate Orbiter that in 1999 failed to enter Mars’ orbit and crashed while entering its atmosphere [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter). This is one of many examples here. People tend to confuse units quite often. We see similar errors occurring in various domains over the years:

- On October 12, 1492, Christopher Columbus unintentionally discovered the sea route from Europe to America because, during his travel preparations, he mixed the Arabic mile with a Roman mile, which led to the wrong estimation of the equator and his expected travel distance [[Columbus]](https://en.wikipedia.org/wiki/Christopher_Columbus).
- In 1628, a new warship, Vasa, accidentally had an asymmetrical hull (being thicker on the port side than the starboard side), which was one of the reasons for her sinking less than a mile into her maiden voyage, resulting in the death of 30 people on board. This asymmetry could have been caused by the use of different systems of measurement, as archaeologists have found four rulers used by the workers who built the ship. Two were calibrated in Swedish feet, which had 12 inches, while the other two measured Amsterdam feet, which had 11 inches [[Vasa]](https://theworld.org/stories/2012-02-23/new-clues-emerge-centuries-old-swedish-shipwreck).
- Air Canada Flight 143 ran out of fuel on July 23, 1983, at an altitude of 41 000 feet (12 000 metres), midway through the flight because the fuel had been calculated in pounds instead of kilograms by the ground crew [[Gimli Glider]](https://en.wikipedia.org/wiki/Gimli_Glider).
- The British rock band Black Sabbath, during its Born Again tour in 1983, ordered a replica of Stonehenge as props for the scene. Unfortunately, they had to leave them in the storage area because, while submitting the order, their manager wrote dimensions down in meters when he meant feet, and so the stones didn’t fit the scene. “It cost a fortune to make, but there was not a building on Earth that you could fit it into” [[Stonehenge]](https://www.telegraph.co.uk/films/2020/05/01/tiny-stones-giant-laughs-story-behind-spinal-taps-stonehenge).
- On April 15, 1999, Korean Air Cargo Flight 6316 crashed due to a miscommunication between pilots about the desired flight altitude [[Flight 6316]](https://web.archive.org/web/20210917190721/https://www.ntsb.gov/news/press-releases/Pages/Korean_Air_Flight_6316_MD-11_Shanghai_China_-_April_15_1999.aspx).
- In February 2001, the crew of the Moorpark College Zoo built an enclosure for Clarence the Tortoise with a weight of 250 pounds instead of 250 kilograms [[Clarence]](https://www.latimes.com/archives/la-xpm-2001-feb-09-me-23253-story.html).
- In December 2003, one of the roller coaster’s cars at Tokyo Disneyland’s Space Mountain attraction suddenly derailed due to a broken axle caused by confusion after upgrading the specification from imperial to metric units [[Disney]](https://web.archive.org/web/20040209033827/http://www.olc.co.jp/news/20040121_01en.html).
- During the construction of the Hochrheinbrücke bridge to connect the small German town of Laufenburg with Swiss Laufenburg, the construction team made a sign error that resulted in a discrepancy of 54 cm between the two outer ends of the bridge [[Hochrheinbrücke]](https://www.normaalamsterdamspeil.nl/wp-content/uploads/2015/03/website_bridge.pdf).
- An American company sold a shipment of wild rice to a Japanese customer, quoting a price of 39 cents per pound, but the customer thought the quote was for 39 cents per kilogram [[Wild Rice]](https://www.bizjournals.com/eastbay/stories/2001/07/09/focus3.html).
- On October 17, 2023, The Guardian published an article titled “Record Heat: Malawi swelters with temperatures nearly 68F above average” with many issues related to the affine space types and temperature units. Due to incorrect logic, probably during the translation of the article to the U.S. market, `20 °C` above the average temperature was converted to `68 °F`. The actual temperature increase was `32 °F`, not `68 °F` [[The Guardian]](https://randomascii.wordpress.com/2023/10/17/localization-failure-temperature-is-hard).
- A whole set of [[Medication dose errors]](https://onlinelibrary.wiley.com/doi/10.1111/jan.15072)…

The safety subject is so vast and essential by itself that we dedicated an entire [Safety features] chapter of this paper that discusses all the nuances in detail.

### 7.2 Vocabulary types

We standardized many library features mostly used in the implementation details (fmt, ranges, random-number generators, etc.). However, we believe that the most important role of the C++ Standard is to provide a standardized way of communication between different vendors.

Let’s imagine a world without `std::string` or `std::vector`. Every vendor has their version of it, and of course, they are highly incompatible with each other. As a result, when someone needs to integrate software from different vendors, it turns out to be an unnecessarily arduous task.

Introducing `std::chrono::duration` and `std::chrono::time_point` improved the interfaces a lot, but time is only one of many quantities that we deal with in our software on a daily basis. We desperately need to be able to express more quantities and units in a standardized way so different libraries get means to communicate with each other.

If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds, and the [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) would not have crashed during the Mars orbital insertion maneuver.

### 7.3 Certification

Mission and life-critical projects, or those for embedded devices, often have to obey the safety norms that care about software for safety-critical systems (e.g., ISO 61508 is a basic functional safety standard applicable to all industries, and ISO 26262 for automotive). As a result, their company policy often forbid third-party tooling that lacks official certification. Such certification requires a specification to be certified against, and those tools often do not have one. The risk and cost of self-certifying an Open Source project is too high for many as well.

Companies often have a policy that the software they use must obey all the rules MISRA provides. This is a common misconception, as many of those rules are intended to be deviated from. However, those deviations require rationale and documentation, which is also considered to be risky and expensive by many.

All of those reasons often prevent the usage of an Open Source product in a company, which is a huge issue, as those companies typically are natural users of physical quantities and units libraries.

Having the physical quantities and units library standardized would solve those issues for many customers, and would allow them to produce safer code for projects on which human life depends every single day.

### 7.4 Complex and complicated

Suppose vendors can’t use an Open Source library in a production project for the above reasons. They are forced to write their own abstractions by themselves. Besides being costly and time-consuming, it also happens that writing a physical quantities and units library by yourself is far from easy. Doing this is complex and complicated, especially for engineers who are not experts in the domain. There are many exceptional corner cases to cover that most developers do not even realize before falling into a trap in production. On the other hand, domain experts might find it difficult to put their knowledge into code and create a correct implementation in C++. As a result, companies either use really simple and unsafe numeric wrappers, or abandon the effort entirely and just use built-in types, such as `float` or `int`, to express quantity values, thus losing all semantic categorization. This often leads to safety issues caused by accidentally using values representing the wrong quantity or having an incorrect unit.

### 7.5 Extensibility

Many applications of a quantity and units library may need to operate on a combination of standard (e.g., SI) and domain-specific quantities and units. The complexity of developing domain-specific solutions highlights the value in being able to define new quantities and units that have all the expressivity and safety as those provided by the library.

Experience with writing ad hoc typed quantities without library support that can be combined with or converted to `std::chrono::duration` has shown the downside of bespoke solutions: If not all operations or conversions are handled, users will need to leave the safety of typed quantities to operate on primitive types.

The interfaces of the this library were designed with ease of extensibility in mind. Each definition of a dimension, quantity type, or unit typically takes only a single line of code. This is possible thanks to the extensive usage of C++20 class types as Non-Type Template Parameters (NTTP). For example, the following code presents how second (a unit of time in the [[SI]](https://www.bipm.org/en/publications/si-brochure)) and hertz (a unit of frequency in the [[SI]](https://www.bipm.org/en/publications/si-brochure)) can be defined:

```cpp
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
inline constexpr struct hertz : named_unit<"Hz", 1 / second, kind_of<isq::frequency>> {} hertz;
```

### 7.6 Broad industry value

When people think about industries that could use physical quantities and unit libraries, they think of a few companies related to aerospace, autonomous cars, or embedded industries. That is all true, but there are many other potential users for such a library.

Here is a list of some less obvious candidates:

- Manufacturing and production systems,
- energy sector (power generation, electrical grids, renewable energy),
- maritime industry,
- freight transport and logistics,
- chemical and process engineering,
- oil and gas (drilling, pipelines, refineries),
- HVAC and environmental control,
- telecommunications and signal processing,
- military,
- astronomy,
- civil engineering and construction,
- 3D design and CAD,
- robotics,
- audio and music production,
- medical devices and pharmaceutical dosing,
- gaming and physics simulation,
- national laboratories,
- scientific institutions and universities,
- all kinds of navigation and charting,
- GUI frameworks and computer graphics,
- finance (including HFT).

As we can see, the range of domains for such a library is vast and not limited to applications involving specifically physical units. Any software that involves measurements, or operations on counts of some standard or domain-specific quantities, could benefit from a zero-cost abstraction for operating on quantity values and their units. The library also provides affine space abstractions, which may prove useful in many applications.

### 7.7 Standardizing existing practice

Plenty of physical units libraries have been available to the public for many years. In 1998 Walter Brown provided an “Introduction to the SI Library of Unit-Based Computation” paper for the International Conference on Computing in High Energy Physics [[CHEP’98]](https://digital.library.unt.edu/ark:/67531/metadc668099). It emphasizes the importance of strong types and static type-checking. After that, it describes a library modeling the [[SI]](https://www.bipm.org/en/publications/si-brochure) to provide “strict compile-time type-checking without run-time overhead”.

It also states that at this time, “in numeric programming, programmers make heavy, near-exclusive, use of a language’s native numeric types (e.g., `double`)”. Today, twenty-five years later, plenty of “Modern C++” production code bases still use `double` to represent various quantities and units. It is high time to change this.

Throughout the years, we have learned the best practices for handling specific cases in the domain. Various products may have different scopes and support different C++ versions. Still, taking that aside, they use really similar concepts, types, and operations under the hood. We know how to do those things already.

The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B). The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.

The authors joined forces and are working together to propose the best quantities and units library we can get with the latest version of the C++ language. They spend their private time and efforts hoping that the ISO C++ Committee will be willing to include such a feature in the C++ standard library.

### 7.8 WG21 wants it

In Belfast 2019 the following polls were taken for [[P1935R0]](https://wg21.link/p1935r0) in LEWG:

**POLL:** *We should promise more committee time to pursuing adding common units (such as SI, customary, etc) to the standard library, knowing that our time is scarce and this will leave less time for other work.*

| SF | WF | N | WA | SA |
| --- | --- | --- | --- | --- |
| 11 | 7 | 4 | 2 | 0 |

**POLL:** *We should promise more committee time to pursuing a standard library framework for user defined units and unit systems, knowing that our time is scarce and this will leave less time for other work.*

| SF | WF | N | WA | SA |
| --- | --- | --- | --- | --- |
| 10 | 8 | 4 | 1 | 1 |

As a result of the above polls, Mateusz approached authors of all other popular actively maintained libraries. We formed a working group of experts and worked on a common unified proposal for a few years. This paper and the current implementation of the [[mp-units]](https://mpusz.github.io/mp-units) library is the result of those actions.

In Croydon 2026, this paper was reviewed by both SG18 (LEWG Incubator) and LEWG. LEWG took the following polls:

**POLL:** *We acknowledge the complexity inherent to the domain of quantities and units and think this is a problem worth solving thoroughly in the standard library, following the direction presented in P3045R7.*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 22 | 13 | 1 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We support the direction presented as a technical solution (instantiating quantities with units, creating the hierarchy of kinds).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 16 | 22 | 0 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value in covering use cases in fine granularity (different quantities of the same kind, such as width and height, or difference between kinetic and potential energy).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 22 | 12 | 3 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value of standardizing these parts of the framework: Core library (quantity, symbolic expressions, dimensions, units, references and concepts), Quantity kinds (support quantities of the same dimension), Quantities of the same kind (width, height, etc.).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 27 | 9 | 0 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value of standardizing Affine space (quantity_point, point origin, and concepts for them).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 24 | 8 | 1 | 0 | 0 |

**Outcome: Strong consensus in favor**

**POLL:** *We see the value of standardizing Text output (for quantity, units, and dimensions).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 15 | 14 | 5 | 0 | 0 |

**Outcome: Strong consensus in favour**

These results demonstrate strong committee support for the comprehensive approach to quantities and units presented in this paper, including the more advanced features like affine space abstractions and fine-grained quantity specifications.

## 8 Common smells when there is no library for quantities and units

In this chapter, we are going to review typical safety issues related to physical quantities and units in the C++ code when a proper library is not used. Even though all the examples come from the Open Source projects, expensive revenue-generating production source code often is similar.

### 8.1 The proliferation of `double`

It turns out that in the C++ software, most of our calculations in the physical quantities and units domain are handled with fundamental types like `double`. Code like below is a typical example here:

```cpp
double GlidePolar::MacCreadyAltitude(double MCREADY,
                                     double Distance,
                                     const double Bearing,
                                     const double WindSpeed,
                                     const double WindBearing,
                                     double *BestCruiseTrack,
                                     double *VMacCready,
                                     const bool isFinalGlide,
                                     double *TimeToGo,
                                     const double AltitudeAboveTarget=1.0e6,
                                     const double cruise_efficiency=1.0,
                                     const double TaskAltDiff=-1.0e6);
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Header/McReady.h#L7-L21).

There are several problems with such an approach: The abundance of `double` parameters makes it easy to accidentally switch values and there is no way of noticing such a mistake at compile-time. The code is not self-documenting in what units the parameters are expected. Is `Distance` in meters or kilometers? Is `WindSpeed` in meters per second or knots? Different code bases choose different ways to encode this information, which may be internally inconsistent. A strong type system would help answer these questions at the time the interface is written, and the compiler would verify it at compile-time.

### 8.2 The proliferation of magic numbers

There are a lot of constants and conversion factors involved in the quantity equations. Source code responsible for such computations is often trashed with magic numbers:

```cpp
double AirDensity(double hr, double temp, double abs_press)
{
  return (1/(287.06*(temp+273.15)))*(abs_press - 230.617 * hr * exp((17.5043*temp)/(241.2+temp)));
}
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Source/Library/PressureFunctions.cpp#L134-L136).

Apart from the obvious readability issues, such code is hard to maintain, and it needs a lot of domain knowledge on the developer’s side. While it would be easy to replace these numbers with named constants, the question of which unit the constant is in remains. Is `287.06` in pounds per square inch (psi) or millibars (mbar)?

### 8.3 The proliferation of conversion macros

The lack of automated unit conversions often results in handwritten conversion functions or macros that are spread everywhere among the code base:

```cpp
#ifndef PI
static const double PI = (4*atan(1));
#endif
#define EARTH_DIAMETER    12733426.0    // Diameter of earth in meters
#define SQUARED_EARTH_DIAMETER  162140137697476.0 // Diameter of earth in meters (EARTH_DIAMETER*EARTH_DIAMETER)
#ifndef DEG_TO_RAD
#define DEG_TO_RAD  (PI / 180)
#define RAD_TO_DEG  (180 / PI)
#endif

#define NAUTICALMILESTOMETRES (double)1851.96
#define KNOTSTOMETRESSECONDS (double)0.5144

#define TOKNOTS (double)1.944
#define TOFEETPERMINUTE (double)196.9
#define TOMPH   (double)2.237
#define TOKPH   (double)3.6

// meters to.. conversion
#define TONAUTICALMILES (1.0 / 1852.0)
#define TOMILES         (1.0 / 1609.344)
#define TOKILOMETER     (0.001)
#define TOFEET          (1.0 / 0.3048)
#define TOMETER         (1.0)
```

[Original code here](https://github.com/LK8000/LK8000/blob/052bbc20a106fda4db41874e788e39020fb86512/Common/Header/Defines.h#L901-L924).

Again, the question of which unit the constant is in remains. Without looking at the code, it is impossible to tell from which unit `TOMETER` converts. Also, macros have the problem that they are not scoped to a namespace and thus can easily clash with other macros or functions, especially if they have such common names like `PI` or `RAD_TO_DEG`. A quick search through open source C++ code bases reveals that, for example, the `RAD_TO_DEG` macro is defined in a multitude of different ways – sometimes even within the same repository:

```cpp
#define RAD_TO_DEG (180 / PI)
#define RAD_TO_DEG 57.2957795131
#define RAD_TO_DEG ( radians ) ((radians ) * 180.0 / M_PI)
#define RAD_TO_DEG 57.2957805f
...
```

[Example search across multiple repositories](https://github.com/search?q=lang%3AC%2B%2B++%22%23define+RAD_TO_DEG%22&type=code)

[Multiple redefinitions in the same repository](https://github.com/search?q=repo%3ALK8000%2FLK8000%20rad_to_deg&type=code)

Another safety issue occurring here is the fact that macro values can be deliberately tainted by compiler settings at built time and can acquire values that are not present in the source code. Human reviews won’t catch such issues.

Also, most of the macros do not follow best practices. Often, necessary parentheses are missing, processing in a preprocessor ends up with redundant casts, or some compile-time constants use too many digits for a value to be exact for a specific type (e.g., `float`).

### 8.4 Lack of consistency

If we not only lack strong types to isolate the abstractions from each other, but also lack discipline to keep our code consistent, we end up in an awful place:

```cpp
void DistanceBearing(double lat1, double lon1,
                     double lat2, double lon2,
                     double *Distance, double *Bearing);

double DoubleDistance(double lat1, double lon1,
                      double lat2, double lon2,
                      double lat3, double lon3);

void FindLatitudeLongitude(double Lat, double Lon,
                           double Bearing, double Distance,
                           double *lat_out, double *lon_out);

double CrossTrackError(double lon1, double lat1,
                       double lon2, double lat2,
                       double lon3, double lat3,
                       double *lon4, double *lat4);

double ProjectedDistance(double lon1, double lat1,
                         double lon2, double lat2,
                         double lon3, double lat3,
                         double *xtd, double *crs);
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Header/NavFunctions.h#L7C1-L27).

Users can easily make errors if the interface designers are not consistent in ordering parameters. It is really hard to remember which function takes latitude or `Bearing` first and when a latitude or `Distance` is in the front.

### 8.5 Lack of a conceptual framework

The previous points mean that the fundamental types can’t be leveraged to model the different concepts of quantities and units frameworks. There is no shared vocabulary between different libraries. User-facing APIs use ad-hoc conventions. Even internal interfaces are inconsistent between themselves.

Arithmetic types such as `int` and `double` are used to model different concepts. They are used to represent any abstraction (be it a magnitude, difference, point, or kind) of any quantity type of any unit. These are weak types that make up weakly-typed interfaces. The resulting interfaces and implementations built with these types easily allow mixing up parameters and using operations that are not part of the represented quantity.

## 9 Design goals

The library facilities that we plan to propose in the upcoming papers is designed with the following goals in mind.

### 9.1 Compile-time safety

The most important property of any such a library is the safety it brings to C++ projects. The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.

In some cases, we are even eager to prioritize safe interfaces over the general usability experience (e.g., getters of the underlying raw numerical value will always require a unit in which the value should be returned in, which results in more typing and is sometimes redundant).

More information on this subject can be found in [Safety features].

### 9.2 Performance

The library should be as fast or even faster than working with fundamental types. There should be no runtime overhead, and no space size overhead should be needed to implement higher-level abstractions. In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.

### 9.3 Great user experience

The primary purpose of the library is to generate compile-time errors. If users did not introduce any bugs in the manual handling of quantities and units, the library would be of little use. This is why the library is optimized for readable compilation errors and great debugging experience.

The library is easy to use and flexible. The interfaces are straight-forward and safe by default. Users should be able to easily express any quantity and unit, which requires them to compose.

The above constraints imply the usage of special implementation techniques. The library will not only provide types, but also compile-time known values that will enable users to write easy to understand and efficient equations on quantities and units.

### 9.4 Scope

There are plenty of expectations from different parties regarding such a library. It should support at least:

- Any unit’s magnitude (huge, small, floating-point).
- Systems of Quantities.
- Systems of Units.
- The affine space.
- Highly adjustable text-output formatting.

Additionally, it would be good to also support the following features:

- Scalar, vector, and tensor quantities.
- Natural units systems.

### 9.5 Easy to extend

The library’s core framework does not assume the usage of any systems of quantities or units. It is fully generic and allow defining any system abstraction on top of it.

Most entities in the library can be defined with a single line of code without preprocessor macros. Users can easily extend provided systems with custom dimensions, quantities, and units.

### 9.6 Low standardization cost

The set of entities required for standardization should be limited to the bare minimum.

Most of the entities in systems definitions should be possible to implement with a single line of code.

Derived units do not need separate library types. Instead, they can be obtained through the composition of predefined named units. Units should not be associated with User-Defined Literals (UDLs), as it is the case with `std::chrono::duration`. UDLs do not compose, have very limited scope and functionality, and are expensive to standardize.

The user interface should have no preprocessor macros.

It should be possible for most proposed features (besides the text output) to be freestanding.

## 10 Quick domain introduction

This chapter provides a brief introduction to the quantities and units domain. Please refer to [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) for more details.

![](data:image/svg+xml;base64,PHN2ZyBpZD0iZXhwb3J0LXN2ZyIgd2lkdGg9IjEwMCUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgY2xhc3M9ImZsb3djaGFydCIgc3R5bGU9Im1heC13aWR0aDogMjk0LjU5OHB4OyBiYWNrZ3JvdW5kOiByZ2IoMjU1LCAyNTUsIDI1NSk7IiB2aWV3Qm94PSIwIDAgMjk0LjU5NzY1NjI1IDM2NyIgcm9sZT0iZ3JhcGhpY3MtZG9jdW1lbnQgZG9jdW1lbnQiIGFyaWEtcm9sZWRlc2NyaXB0aW9uPSJmbG93Y2hhcnQtdjIiPjxzdHlsZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+cCB7bWFyZ2luOiAwO308L3N0eWxlPjxzdHlsZT4jZXhwb3J0LXN2Z3tmb250LWZhbWlseTphcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNHB4O2ZpbGw6IzMzMzt9QGtleWZyYW1lcyBlZGdlLWFuaW1hdGlvbi1mcmFtZXtmcm9te3N0cm9rZS1kYXNob2Zmc2V0OjA7fX1Aa2V5ZnJhbWVzIGRhc2h7dG97c3Ryb2tlLWRhc2hvZmZzZXQ6MDt9fSNleHBvcnQtc3ZnIC5lZGdlLWFuaW1hdGlvbi1zbG93e3N0cm9rZS1kYXNoYXJyYXk6OSw1IWltcG9ydGFudDtzdHJva2UtZGFzaG9mZnNldDo5MDA7YW5pbWF0aW9uOmRhc2ggNTBzIGxpbmVhciBpbmZpbml0ZTtzdHJva2UtbGluZWNhcDpyb3VuZDt9I2V4cG9ydC1zdmcgLmVkZ2UtYW5pbWF0aW9uLWZhc3R7c3Ryb2tlLWRhc2hhcnJheTo5LDUhaW1wb3J0YW50O3N0cm9rZS1kYXNob2Zmc2V0OjkwMDthbmltYXRpb246ZGFzaCAyMHMgbGluZWFyIGluZmluaXRlO3N0cm9rZS1saW5lY2FwOnJvdW5kO30jZXhwb3J0LXN2ZyAuZXJyb3ItaWNvbntmaWxsOmhzbCgyMjAuNTg4MjM1Mjk0MSwgMTAwJSwgOTguMzMzMzMzMzMzMyUpO30jZXhwb3J0LXN2ZyAuZXJyb3ItdGV4dHtmaWxsOnJnYig4LjUwMDAwMDAwMDIsIDUuNzUwMDAwMDAwMSwgMCk7c3Ryb2tlOnJnYig4LjUwMDAwMDAwMDIsIDUuNzUwMDAwMDAwMSwgMCk7fSNleHBvcnQtc3ZnIC5lZGdlLXRoaWNrbmVzcy1ub3JtYWx7c3Ryb2tlLXdpZHRoOjFweDt9I2V4cG9ydC1zdmcgLmVkZ2UtdGhpY2tuZXNzLXRoaWNre3N0cm9rZS13aWR0aDozLjVweDt9I2V4cG9ydC1zdmcgLmVkZ2UtcGF0dGVybi1zb2xpZHtzdHJva2UtZGFzaGFycmF5OjA7fSNleHBvcnQtc3ZnIC5lZGdlLXRoaWNrbmVzcy1pbnZpc2libGV7c3Ryb2tlLXdpZHRoOjA7ZmlsbDpub25lO30jZXhwb3J0LXN2ZyAuZWRnZS1wYXR0ZXJuLWRhc2hlZHtzdHJva2UtZGFzaGFycmF5OjM7fSNleHBvcnQtc3ZnIC5lZGdlLXBhdHRlcm4tZG90dGVke3N0cm9rZS1kYXNoYXJyYXk6Mjt9I2V4cG9ydC1zdmcgLm1hcmtlcntmaWxsOiMwYjBiMGI7c3Ryb2tlOiMwYjBiMGI7fSNleHBvcnQtc3ZnIC5tYXJrZXIuY3Jvc3N7c3Ryb2tlOiMwYjBiMGI7fSNleHBvcnQtc3ZnIHN2Z3tmb250LWZhbWlseTphcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNHB4O30jZXhwb3J0LXN2ZyBwe21hcmdpbjowO30jZXhwb3J0LXN2ZyAubGFiZWx7Zm9udC1mYW1pbHk6YXJpYWwsc2Fucy1zZXJpZjtjb2xvcjojMzMzO30jZXhwb3J0LXN2ZyAuY2x1c3Rlci1sYWJlbCB0ZXh0e2ZpbGw6cmdiKDguNTAwMDAwMDAwMiwgNS43NTAwMDAwMDAxLCAwKTt9I2V4cG9ydC1zdmcgLmNsdXN0ZXItbGFiZWwgc3Bhbntjb2xvcjpyZ2IoOC41MDAwMDAwMDAyLCA1Ljc1MDAwMDAwMDEsIDApO30jZXhwb3J0LXN2ZyAuY2x1c3Rlci1sYWJlbCBzcGFuIHB7YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDt9I2V4cG9ydC1zdmcgLmxhYmVsIHRleHQsI2V4cG9ydC1zdmcgc3BhbntmaWxsOiMzMzM7Y29sb3I6IzMzMzt9I2V4cG9ydC1zdmcgLm5vZGUgcmVjdCwjZXhwb3J0LXN2ZyAubm9kZSBjaXJjbGUsI2V4cG9ydC1zdmcgLm5vZGUgZWxsaXBzZSwjZXhwb3J0LXN2ZyAubm9kZSBwb2x5Z29uLCNleHBvcnQtc3ZnIC5ub2RlIHBhdGh7ZmlsbDojZmZmNGRkO3N0cm9rZTpoc2woNDAuNTg4MjM1Mjk0MSwgNjAlLCA4My4zMzMzMzMzMzMzJSk7c3Ryb2tlLXdpZHRoOjFweDt9I2V4cG9ydC1zdmcgLnJvdWdoLW5vZGUgLmxhYmVsIHRleHQsI2V4cG9ydC1zdmcgLm5vZGUgLmxhYmVsIHRleHQsI2V4cG9ydC1zdmcgLmltYWdlLXNoYXBlIC5sYWJlbCwjZXhwb3J0LXN2ZyAuaWNvbi1zaGFwZSAubGFiZWx7dGV4dC1hbmNob3I6bWlkZGxlO30jZXhwb3J0LXN2ZyAubm9kZSAua2F0ZXggcGF0aHtmaWxsOiMwMDA7c3Ryb2tlOiMwMDA7c3Ryb2tlLXdpZHRoOjFweDt9I2V4cG9ydC1zdmcgLnJvdWdoLW5vZGUgLmxhYmVsLCNleHBvcnQtc3ZnIC5ub2RlIC5sYWJlbCwjZXhwb3J0LXN2ZyAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNleHBvcnQtc3ZnIC5pY29uLXNoYXBlIC5sYWJlbHt0ZXh0LWFsaWduOmNlbnRlcjt9I2V4cG9ydC1zdmcgLm5vZGUuY2xpY2thYmxle2N1cnNvcjpwb2ludGVyO30jZXhwb3J0LXN2ZyAucm9vdCAuYW5jaG9yIHBhdGh7ZmlsbDojMGIwYjBiIWltcG9ydGFudDtzdHJva2Utd2lkdGg6MDtzdHJva2U6IzBiMGIwYjt9I2V4cG9ydC1zdmcgLmFycm93aGVhZFBhdGh7ZmlsbDojMGIwYjBiO30jZXhwb3J0LXN2ZyAuZWRnZVBhdGggLnBhdGh7c3Ryb2tlOiMwYjBiMGI7c3Ryb2tlLXdpZHRoOjFweDt9I2V4cG9ydC1zdmcgLmZsb3djaGFydC1saW5re3N0cm9rZTojMGIwYjBiO2ZpbGw6bm9uZTt9I2V4cG9ydC1zdmcgLmVkZ2VMYWJlbHtiYWNrZ3JvdW5kLWNvbG9yOmhzbCgtNzkuNDExNzY0NzA1OSwgMTAwJSwgOTMuMzMzMzMzMzMzMyUpO3RleHQtYWxpZ246Y2VudGVyO30jZXhwb3J0LXN2ZyAuZWRnZUxhYmVsIHB7YmFja2dyb3VuZC1jb2xvcjpoc2woLTc5LjQxMTc2NDcwNTksIDEwMCUsIDkzLjMzMzMzMzMzMzMlKTt9I2V4cG9ydC1zdmcgLmVkZ2VMYWJlbCByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6aHNsKC03OS40MTE3NjQ3MDU5LCAxMDAlLCA5My4zMzMzMzMzMzMzJSk7ZmlsbDpoc2woLTc5LjQxMTc2NDcwNTksIDEwMCUsIDkzLjMzMzMzMzMzMzMlKTt9I2V4cG9ydC1zdmcgLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyNDMuOTk5OTk5OTk5OSwgMjIwLjk5OTk5OTk5OTgsIDI1NSwgMC41KTt9I2V4cG9ydC1zdmcgLmNsdXN0ZXIgcmVjdHtmaWxsOiNGRkZGRjg7c3Ryb2tlOmhzbCgyMjAuNTg4MjM1Mjk0MSwgNjAlLCA4OC4zMzMzMzMzMzMzJSk7c3Ryb2tlLXdpZHRoOjFweDt9I2V4cG9ydC1zdmcgLmNsdXN0ZXIgdGV4dHtmaWxsOnJnYig4LjUwMDAwMDAwMDIsIDUuNzUwMDAwMDAwMSwgMCk7fSNleHBvcnQtc3ZnIC5jbHVzdGVyIHNwYW57Y29sb3I6cmdiKDguNTAwMDAwMDAwMiwgNS43NTAwMDAwMDAxLCAwKTt9I2V4cG9ydC1zdmcgZGl2Lm1lcm1haWRUb29sdGlwe3Bvc2l0aW9uOmFic29sdXRlO3RleHQtYWxpZ246Y2VudGVyO21heC13aWR0aDoyMDBweDtwYWRkaW5nOjJweDtmb250LWZhbWlseTphcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxMnB4O2JhY2tncm91bmQ6aHNsKDIyMC41ODgyMzUyOTQxLCAxMDAlLCA5OC4zMzMzMzMzMzMzJSk7Ym9yZGVyOjFweCBzb2xpZCBoc2woMjIwLjU4ODIzNTI5NDEsIDYwJSwgODguMzMzMzMzMzMzMyUpO2JvcmRlci1yYWRpdXM6MnB4O3BvaW50ZXItZXZlbnRzOm5vbmU7ei1pbmRleDoxMDA7fSNleHBvcnQtc3ZnIC5mbG93Y2hhcnRUaXRsZVRleHR7dGV4dC1hbmNob3I6bWlkZGxlO2ZvbnQtc2l6ZToxOHB4O2ZpbGw6IzMzMzt9I2V4cG9ydC1zdmcgcmVjdC50ZXh0e2ZpbGw6bm9uZTtzdHJva2Utd2lkdGg6MDt9I2V4cG9ydC1zdmcgLmljb24tc2hhcGUsI2V4cG9ydC1zdmcgLmltYWdlLXNoYXBle2JhY2tncm91bmQtY29sb3I6aHNsKC03OS40MTE3NjQ3MDU5LCAxMDAlLCA5My4zMzMzMzMzMzMzJSk7dGV4dC1hbGlnbjpjZW50ZXI7fSNleHBvcnQtc3ZnIC5pY29uLXNoYXBlIHAsI2V4cG9ydC1zdmcgLmltYWdlLXNoYXBlIHB7YmFja2dyb3VuZC1jb2xvcjpoc2woLTc5LjQxMTc2NDcwNTksIDEwMCUsIDkzLjMzMzMzMzMzMzMlKTtwYWRkaW5nOjJweDt9I2V4cG9ydC1zdmcgLmljb24tc2hhcGUgcmVjdCwjZXhwb3J0LXN2ZyAuaW1hZ2Utc2hhcGUgcmVjdHtvcGFjaXR5OjAuNTtiYWNrZ3JvdW5kLWNvbG9yOmhzbCgtNzkuNDExNzY0NzA1OSwgMTAwJSwgOTMuMzMzMzMzMzMzMyUpO2ZpbGw6aHNsKC03OS40MTE3NjQ3MDU5LCAxMDAlLCA5My4zMzMzMzMzMzMzJSk7fSNleHBvcnQtc3ZnIC5sYWJlbC1pY29ue2Rpc3BsYXk6aW5saW5lLWJsb2NrO2hlaWdodDoxZW07b3ZlcmZsb3c6dmlzaWJsZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTt9I2V4cG9ydC1zdmcgLm5vZGUgLmxhYmVsLWljb24gcGF0aHtmaWxsOmN1cnJlbnRDb2xvcjtzdHJva2U6cmV2ZXJ0O3N0cm9rZS13aWR0aDpyZXZlcnQ7fSNleHBvcnQtc3ZnIC5ub2RlIC5uZW8tbm9kZXtzdHJva2U6aHNsKDQwLjU4ODIzNTI5NDEsIDYwJSwgODMuMzMzMzMzMzMzMyUpO30jZXhwb3J0LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIHJlY3QsI2V4cG9ydC1zdmcgW2RhdGEtbG9vaz0ibmVvIl0uY2x1c3RlciByZWN0LCNleHBvcnQtc3ZnIFtkYXRhLWxvb2s9Im5lbyJdLm5vZGUgcG9seWdvbntzdHJva2U6dXJsKCNleHBvcnQtc3ZnLWdyYWRpZW50KTtmaWx0ZXI6ZHJvcC1zaGFkb3coIDFweCAycHggMnB4IHJnYmEoMTg1LDE4NSwxODUsMSkpO30jZXhwb3J0LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIHBhdGh7c3Ryb2tlOnVybCgjZXhwb3J0LXN2Zy1ncmFkaWVudCk7c3Ryb2tlLXdpZHRoOjE7fSNleHBvcnQtc3ZnIFtkYXRhLWxvb2s9Im5lbyJdLm5vZGUgLm91dGVyLXBhdGh7ZmlsdGVyOmRyb3Atc2hhZG93KCAxcHggMnB4IDJweCByZ2JhKDE4NSwxODUsMTg1LDEpKTt9I2V4cG9ydC1zdmcgW2RhdGEtbG9vaz0ibmVvIl0ubm9kZSAubmVvLWxpbmUgcGF0aHtzdHJva2U6aHNsKDQwLjU4ODIzNTI5NDEsIDYwJSwgODMuMzMzMzMzMzMzMyUpO2ZpbHRlcjpub25lO30jZXhwb3J0LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIGNpcmNsZXtzdHJva2U6dXJsKCNleHBvcnQtc3ZnLWdyYWRpZW50KTtmaWx0ZXI6ZHJvcC1zaGFkb3coIDFweCAycHggMnB4IHJnYmEoMTg1LDE4NSwxODUsMSkpO30jZXhwb3J0LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIGNpcmNsZSAuc3RhdGUtc3RhcnR7ZmlsbDojMDAwMDAwO30jZXhwb3J0LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5zdGF0ZWRpYWdyYW0tY2x1c3RlciByZWN0e2ZpbGw6I2ZmZjRkZDtzdHJva2U6dXJsKCNleHBvcnQtc3ZnLWdyYWRpZW50KTtzdHJva2Utd2lkdGg6MTt9I2V4cG9ydC1zdmcgW2RhdGEtbG9vaz0ibmVvIl0uaWNvbi1zaGFwZSAuaWNvbntmaWxsOnVybCgjZXhwb3J0LXN2Zy1ncmFkaWVudCk7ZmlsdGVyOmRyb3Atc2hhZG93KCAxcHggMnB4IDJweCByZ2JhKDE4NSwxODUsMTg1LDEpKTt9I2V4cG9ydC1zdmcgW2RhdGEtbG9vaz0ibmVvIl0uaWNvbi1zaGFwZSAuaWNvbi1uZW8gcGF0aHtzdHJva2U6dXJsKCNleHBvcnQtc3ZnLWdyYWRpZW50KTtmaWx0ZXI6ZHJvcC1zaGFkb3coIDFweCAycHggMnB4IHJnYmEoMTg1LDE4NSwxODUsMSkpO30jZXhwb3J0LXN2ZyA6cm9vdHstLW1lcm1haWQtZm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO308L3N0eWxlPjxnPjxtYXJrZXIgaWQ9ImV4cG9ydC1zdmdfZmxvd2NoYXJ0LXYyLXBvaW50RW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDExLjUgMTQiIHJlZlg9IjcuNzUiIHJlZlk9IjciIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjEwLjUiIG1hcmtlckhlaWdodD0iMTQiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAwIDAgTCAxMS41IDcgTCAwIDE0IHoiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDA7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0iZXhwb3J0LXN2Z19mbG93Y2hhcnQtdjItcG9pbnRTdGFydCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMS41IDE0IiByZWZYPSI0IiByZWZZPSI3IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMS41IiBtYXJrZXJIZWlnaHQ9IjE0IiBvcmllbnQ9ImF1dG8iPjxwb2x5Z29uIHBvaW50cz0iMCw3IDExLjUsMTQgMTEuNSwwIiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAwOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9ImV4cG9ydC1zdmdfZmxvd2NoYXJ0LXYyLXBvaW50RW5kLW1hcmdpbiIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMS41IDE0IiByZWZYPSIxMS41IiByZWZZPSI3IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMC41IiBtYXJrZXJIZWlnaHQ9IjE0IiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMCAwIEwgMTEuNSA3IEwgMCAxNCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAwOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9ImV4cG9ydC1zdmdfZmxvd2NoYXJ0LXYyLXBvaW50U3RhcnQtbWFyZ2luIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDExLjUgMTQiIHJlZlg9IjEiIHJlZlk9IjciIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExLjUiIG1hcmtlckhlaWdodD0iMTQiIG9yaWVudD0iYXV0byI+PHBvbHlnb24gcG9pbnRzPSIwLDcgMTEuNSwxNCAxMS41LDAiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDA7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0iZXhwb3J0LXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlRW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZZPSI1IiByZWZYPSIxMC43NSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTQiIG1hcmtlckhlaWdodD0iMTQiIG9yaWVudD0iYXV0byI+PGNpcmNsZSBjeD0iNSIgY3k9IjUiIHI9IjUiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDA7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0iZXhwb3J0LXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlU3RhcnQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjAiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjE0IiBtYXJrZXJIZWlnaHQ9IjE0IiBvcmllbnQ9ImF1dG8iPjxjaXJjbGUgY3g9IjUiIGN5PSI1IiByPSI1IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAwOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9ImV4cG9ydC1zdmdfZmxvd2NoYXJ0LXYyLWNpcmNsZUVuZC1tYXJnaW4iIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlk9IjUiIHJlZlg9IjEyLjI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxNCIgbWFya2VySGVpZ2h0PSIxNCIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMDsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48bWFya2VyIGlkPSJleHBvcnQtc3ZnX2Zsb3djaGFydC12Mi1jaXJjbGVTdGFydC1tYXJnaW4iIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9Ii0yIiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxNCIgbWFya2VySGVpZ2h0PSIxNCIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMDsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48bWFya2VyIGlkPSJleHBvcnQtc3ZnX2Zsb3djaGFydC12Mi1jcm9zc0VuZCIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxNSAxNSIgcmVmWD0iMTcuNyIgcmVmWT0iNy41IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMiIgbWFya2VySGVpZ2h0PSIxMiIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBMIDE0LDE0IE0gMSwxNCBMIDE0LDEiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDIuNTsiLz48L21hcmtlcj48bWFya2VyIGlkPSJleHBvcnQtc3ZnX2Zsb3djaGFydC12Mi1jcm9zc1N0YXJ0IiBjbGFzcz0ibWFya2VyIGNyb3NzIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDE1IDE1IiByZWZYPSItMy41IiByZWZZPSI3LjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjEyIiBtYXJrZXJIZWlnaHQ9IjEyIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIEwgMTQsMTQgTSAxLDE0IEwgMTQsMSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMi41OyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9ImV4cG9ydC1zdmdfZmxvd2NoYXJ0LXYyLWNyb3NzRW5kLW1hcmdpbiIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxNSAxNSIgcmVmWD0iMTcuNyIgcmVmWT0iNy41IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMiIgbWFya2VySGVpZ2h0PSIxMiIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBMIDE0LDE0IE0gMSwxNCBMIDE0LDEiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDIuNTsiLz48L21hcmtlcj48bWFya2VyIGlkPSJleHBvcnQtc3ZnX2Zsb3djaGFydC12Mi1jcm9zc1N0YXJ0LW1hcmdpbiIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxNSAxNSIgcmVmWD0iLTMuNSIgcmVmWT0iNy41IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMiIgbWFya2VySGVpZ2h0PSIxMiIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBMIDE0LDE0IE0gMSwxNCBMIDE0LDEiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDIuNTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48ZyBjbGFzcz0icm9vdCI+PGcgY2xhc3M9ImNsdXN0ZXJzIi8+PGcgY2xhc3M9ImVkZ2VQYXRocyI+PHBhdGggZD0iTTg1LjA5Mzc1LDUzTDg1LjA5Mzc1LDc4TDg1LjA5Mzc1LDEwMyIgaWQ9IkxfZGltZW5zaW9uX3F1YW50aXR5X3R5cGVfMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6IDAgMCA1MCAwOyBzdHJva2UtZGFzaG9mZnNldDogMDs7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfZGltZW5zaW9uX3F1YW50aXR5X3R5cGVfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2T0RVdU1Ea3pOelVzSW5raU9qVXpmU3g3SW5naU9qZzFMakE1TXpjMUxDSjVJam8zT0gwc2V5SjRJam80TlM0d09UTTNOU3dpZVNJNk1UQXpmVjA9Ii8+PHBhdGggZD0iTTg1LjA5Mzc1LDE0OEw4NS4wOTM3NSwxNzNMODUuMDkzNzUsMTk4IiBpZD0iTF9xdWFudGl0eV90eXBlX3JlZmVyZW5jZV8wIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0ic3Ryb2tlLWRhc2hhcnJheTogMCAwIDUwIDA7IHN0cm9rZS1kYXNob2Zmc2V0OiAwOzsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9xdWFudGl0eV90eXBlX3JlZmVyZW5jZV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZPRFV1TURrek56VXNJbmtpT2pFME9IMHNleUo0SWpvNE5TNHdPVE0zTlN3aWVTSTZNVGN6ZlN4N0luZ2lPamcxTGpBNU16YzFMQ0o1SWpveE9UaDlYUT09Ii8+PHBhdGggZD0iTTg1LjA5Mzc1LDI2NEw4NS4wOTM3NSwyNzguOTM1NDU5MzE4MDQ3MTVRODUuMDkzNzUsMjg5IDkzLjc3MjQzNjg3OTYwNTU1LDI5NC4wOTY2MDQwODM1NDg4TDEyNy42NjQ2NzkyNzYzMTU3OCwzMTQiIGlkPSJMX3JlZmVyZW5jZV9xdWFudGl0eV8wIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0ic3Ryb2tlLWRhc2hhcnJheTogMCAwIDcyLjYyMTEzMTg5Njk3MjY2IDA7IHN0cm9rZS1kYXNob2Zmc2V0OiAwOzsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9yZWZlcmVuY2VfcXVhbnRpdHlfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2T0RVdU1Ea3pOelVzSW5raU9qSTJOSDBzZXlKNElqbzROUzR3T1RNM05Td2llU0k2TWpnNWZTeDdJbmdpT2pFeU55NDJOalEyTnpreU56WXpNVFUzT0N3aWVTSTZNekUwZlYwPSIvPjxwYXRoIGQ9Ik0yNDYuODYzMjgxMjUsMjUzLjVMMjQ2Ljg2MzI4MTI1LDI3OC45MzU0NTkzMTgwNDcxNVEyNDYuODYzMjgxMjUsMjg5IDIzOC4xODQ1OTQzNzAzOTQ0NSwyOTQuMDk2NjA0MDgzNTQ4OEwyMDQuMjkyMzUxOTczNjg0MjIsMzE0IiBpZD0iTF9udW1iZXJfcXVhbnRpdHlfMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9InN0cm9rZS1kYXNoYXJyYXk6IDAgMCA4My4xMjExMjQyNjc1NzgxMiAwOyBzdHJva2UtZGFzaG9mZnNldDogMDs7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfbnVtYmVyX3F1YW50aXR5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1qUTJMamcyTXpJNE1USTFMQ0o1SWpveU5UTXVOWDBzZXlKNElqb3lORFl1T0RZek1qZ3hNalVzSW5raU9qSTRPWDBzZXlKNElqb3lNRFF1TWpreU16VXhPVGN6TmpnME1qSXNJbmtpT2pNeE5IMWQiLz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbHMiPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9kaW1lbnNpb25fcXVhbnRpdHlfdHlwZV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9xdWFudGl0eV90eXBlX3JlZmVyZW5jZV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9yZWZlcmVuY2VfcXVhbnRpdHlfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfbnVtYmVyX3F1YW50aXR5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PC9nPjxnIGNsYXNzPSJub2RlcyI+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9ImZsb3djaGFydC1kaW1lbnNpb24tMCIgZGF0YS1pZD0iZGltZW5zaW9uIiBkYXRhLW5vZGU9InRydWUiIGRhdGEtZXQ9Im5vZGUiIGRhdGEtbG9vaz0ibmVvIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg4NS4wOTM3NSwgMzAuNSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIGRhdGEtaWQ9ImRpbWVuc2lvbiIgeD0iLTQ3LjkxMDE1NjI1IiB5PSItMjIuNSIgd2lkdGg9Ijk1LjgyMDMxMjUiIGhlaWdodD0iNDUiIHN0cm9rZT0idXJsKCNncmFkaWVudCkiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0zMS45MTAxNTYyNSwgLTEwLjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjYzLjgyMDMxMjUiIGhlaWdodD0iMjEiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD5kaW1lbnNpb248L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQiIGlkPSJmbG93Y2hhcnQtcXVhbnRpdHlfdHlwZS0xIiBkYXRhLWlkPSJxdWFudGl0eV90eXBlIiBkYXRhLW5vZGU9InRydWUiIGRhdGEtZXQ9Im5vZGUiIGRhdGEtbG9vaz0ibmVvIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSg4NS4wOTM3NSwgMTI1LjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiBkYXRhLWlkPSJxdWFudGl0eV90eXBlIiB4PSItNzcuMDkzNzUiIHk9Ii0yMi41IiB3aWR0aD0iMTU0LjE4NzUiIGhlaWdodD0iNDUiIHN0cm9rZT0idXJsKCNncmFkaWVudCkiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02MS4wOTM3NSwgLTEwLjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjEyMi4xODc1IiBoZWlnaHQ9IjIxIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+cXVhbnRpdHkga2luZCAmYW1wOyB0eXBlPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0iZmxvd2NoYXJ0LXJlZmVyZW5jZS0zIiBkYXRhLWlkPSJyZWZlcmVuY2UiIGRhdGEtbm9kZT0idHJ1ZSIgZGF0YS1ldD0ibm9kZSIgZGF0YS1sb29rPSJuZW8iIHRyYW5zZm9ybT0idHJhbnNsYXRlKDg1LjA5Mzc1LCAyMzEpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiBkYXRhLWlkPSJyZWZlcmVuY2UiIHg9Ii03Mi4wMzUxNTYyNSIgeT0iLTMzIiB3aWR0aD0iMTQ0LjA3MDMxMjUiIGhlaWdodD0iNjYiIHN0cm9rZT0idXJsKCNncmFkaWVudCkiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC01Ni4wMzUxNTYyNSwgLTIxKSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMTIuMDcwMzEyNSIgaGVpZ2h0PSI0MiI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3JtYWw7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPnF1YW50aXR5IHJlZmVyZW5jZTxiciAvPihpLmUuLCB1bml0KTwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9ImZsb3djaGFydC1xdWFudGl0eS01IiBkYXRhLWlkPSJxdWFudGl0eSIgZGF0YS1ub2RlPSJ0cnVlIiBkYXRhLWV0PSJub2RlIiBkYXRhLWxvb2s9Im5lbyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTY1Ljk3ODUxNTYyNSwgMzM2LjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiBkYXRhLWlkPSJxdWFudGl0eSIgeD0iLTQwLjUxOTUzMTI1IiB5PSItMjIuNSIgd2lkdGg9IjgxLjAzOTA2MjUiIGhlaWdodD0iNDUiIHN0cm9rZT0idXJsKCNncmFkaWVudCkiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yNC41MTk1MzEyNSwgLTEwLjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjQ5LjAzOTA2MjUiIGhlaWdodD0iMjEiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm9ybWFsOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD5xdWFudGl0eTwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9ImZsb3djaGFydC1udW1iZXItNiIgZGF0YS1pZD0ibnVtYmVyIiBkYXRhLW5vZGU9InRydWUiIGRhdGEtZXQ9Im5vZGUiIGRhdGEtbG9vaz0ibmVvIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyNDYuODYzMjgxMjUsIDIzMSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIGRhdGEtaWQ9Im51bWJlciIgeD0iLTM5LjczNDM3NSIgeT0iLTIyLjUiIHdpZHRoPSI3OS40Njg3NSIgaGVpZ2h0PSI0NSIgc3Ryb2tlPSJ1cmwoI2dyYWRpZW50KSIvPjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTIzLjczNDM3NSwgLTEwLjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjQ3LjQ2ODc1IiBoZWlnaHQ9IjIxIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vcm1hbDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+bnVtYmVyPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PC9nPjwvZz48ZGVmcz48ZmlsdGVyIGlkPSJkcm9wLXNoYWRvdyIgaGVpZ2h0PSIxMzAlIiB3aWR0aD0iMTMwJSI+PGZlRHJvcFNoYWRvdyBkeD0iNCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iMCIgZmxvb2Qtb3BhY2l0eT0iMC4wNiIgZmxvb2QtY29sb3I9IiMwMDAwMDAiLz48L2ZpbHRlcj48L2RlZnM+PGRlZnM+PGZpbHRlciBpZD0iZHJvcC1zaGFkb3ctc21hbGwiIGhlaWdodD0iMTUwJSIgd2lkdGg9IjE1MCUiPjxmZURyb3BTaGFkb3cgZHg9IjIiIGR5PSIyIiBzdGREZXZpYXRpb249IjAiIGZsb29kLW9wYWNpdHk9IjAuMDYiIGZsb29kLWNvbG9yPSIjMDAwMDAwIi8+PC9maWx0ZXI+PC9kZWZzPjxsaW5lYXJHcmFkaWVudCBpZD0iZXhwb3J0LXN2Zy1ncmFkaWVudCIgZ3JhZGllbnRVbml0cz0ib2JqZWN0Qm91bmRpbmdCb3giIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjAlIj48c3RvcCBvZmZzZXQ9IjAlIiBzdG9wLWNvbG9yPSJoc2woNDAuNTg4MjM1Mjk0MSwgNjAlLCA4My4zMzMzMzMzMzMzJSkiIHN0b3Atb3BhY2l0eT0iMSIvPjxzdG9wIG9mZnNldD0iMTAwJSIgc3RvcC1jb2xvcj0iaHNsKC03OS40MTE3NjQ3MDU5LCA2MCUsIDgzLjMzMzMzMzMzMzMlKSIgc3RvcC1vcGFjaXR5PSIxIi8+PC9saW5lYXJHcmFkaWVudD48L3N2Zz4=)

*Note: A more detailed graph of the framework’s entities can be found in the Framework entities chapter.*

### 10.1 Dimension

[Dimension](https://jcgm.bipm.org/vim/en/1.7.html) specifies the dependence of a quantity on the base quantities of a particular system of quantities. It is represented as a product of powers of factors corresponding to the base quantities, omitting any numerical factor.

Even though ISO does not officially define these, we find the below terms useful when discussing the domain and its C++ implementation:

- **base dimension** is the dimension of a [base quantity](https://jcgm.bipm.org/vim/en/1.4.html),
- **derived dimension** is the dimension of a [derived quantity](https://jcgm.bipm.org/vim/en/1.5.html).

As stated above, ISO does not mention a “base dimension” term. Nevertheless, it treats dimensions of base quantities in a special way by:

- assigning unique identifiers/symbols to all of them,
- stating that derived quantities have a dimension being a product of dimensions of base quantities.

For example:

- *length* (\(L\)), *mass* (\(M\)), *time* (\(T\)), *electric current* (\(I\)), *thermodynamic temperature* (\(Θ\)), *amount of substance* (\(N\)), and *luminous intensity* (\(J\)) are the base dimensions of the ISQ.
- A derived dimension of *force* in the ISQ is denoted by \(dim\;F = LMT^{–2}\).
- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) provides *traffic intensity* quantity that is measured in erlangs but not in the unit one, which also implies that it should be introduced as a base quantity with its own dimension.

### 10.2 Quantity kind & type

Dimension alone is insufficient to describe a quantity. [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides hundreds of named quantity types—much more than the named units in [[SI]](https://www.bipm.org/en/publications/si-brochure).

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) defines **kind of quantity** as an aspect common to mutually comparable quantities. Two or more quantities cannot be added or subtracted unless they belong to the same category of mutually comparable quantities.

Quantities might be:

- of different dimensions (e.g., *length*, *time*, *speed*, *power*),
- of the same dimension but different kind (e.g., *work* vs. *torque*, *frequency* vs. *activity*, *area* vs. *fuel consumption*),
- of the same dimension and kind but still distinct (e.g., *radius* vs. *width* vs. *height* or *potential energy* vs. *kinetic energy* vs. *thermodynamic energy*).

ISO specifies **quantities of dimension one** (dimensionless quantities) where all exponents of base quantities are zero. These typically represent ratios of quantities of the same dimension or counts.

### 10.3 Quantity reference

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) defines quantity value as number and reference together expressing magnitude of a quantity, where the reference can be a measurement unit, measurement procedure, reference material, or combination thereof.

Measurement units are designated by assigned names and symbols. Units of quantities with the same dimension may share names and symbols even when quantities differ in kind (e.g., joule per kelvin for both *heat capacity* and *entropy*). However, some units are restricted to specific kinds (e.g., hertz for *frequency*, becquerel for *radioactive activity*, both equivalent to 1/s).

Dimensionless quantities have units that are numbers, sometimes with special names (radian, steradian, decibel) or expressed as ratios (millimole per mole: \(10^{−3}\), microgram per kilogram: \(10^{−9}\)).

### 10.4 Quantity

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) defines a quantity as “property of a phenomenon, body, or substance, where the property has a magnitude that can be expressed as a number and a reference.”

This means a quantity abstraction should store a numerical value and a reference (typically a unit). Common practice embeds the reference into the C++ type to avoid runtime storage overhead.

It is also worth mentioning here that the distinction between a quantity and a quantity type is not clearly defined in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html). [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) even explicitly states:

> It is customary to use the same term, “quantity”, to refer to both general quantities, such as length, mass, etc., and their instances, such as given lengths, given masses, etc. Accordingly, we are used to saying both that length is a quantity and that a given length is a quantity, by maintaining the specification – “general quantity, \(Q\)” or “individual quantity, \(Q_a\)” – implicit and exploiting the linguistic context to remove the ambiguity.

To prevent such ambiguities in this document, we will consistently use the term:

- “quantity type” when we mean a general quantity,
- “quantity” when we mean the instance of a quantity that also stores its numerical value.

It is also worth mentioning here that [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) does not distinguish between point and vector/interval quantities of The affine space.

## 11 API overview

This chapter presents the library’s core abstractions and design choices. The `quantity` class template represents displacement vectors in an affine space, while `quantity_point` represents points. Generic interfaces enable efficient, type-safe code without unit-specific functions.

*Note for readers: Most application developers need only understand Quantity construction and basic operations (arithmetic, conversions, formatting). Generic interfaces are primarily for library developers designing reusable libraries. More advanced topics like affine space and quantity specifications are covered later for domain specialists and framework developers.*

More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.

### 11.1 Quantity construction

The `quantity` class template takes a reference and representation type:

```cpp
template<Reference auto R,
         RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity;
```

`quantity` is best understood as a **numerical strong type wrapper**: it takes any number-like representation type and enriches it with compile-time metadata — a quantity specification and a measurement unit — collectively called the **quantity reference** — that the type system uses to enforce correctness. The runtime cost is zero; all safety guarantees are resolved at compile time.

This design is not limited to physical computation. Any countable or measurable domain is a valid target: file sizes, pixel counts, angular positions, currency amounts, database row counts, audio sample offsets, and more. If a value can be added to another value of the same kind, multiplied by a dimensionless factor, or meaningfully converted to a different scale, `quantity` can model it. The library is a general-purpose compile-time safety layer for numeric domain modelling, of which SI units are simply the most prominent example.

If we want to set a value for a quantity, we always have to provide a number and a unit:

```cpp
quantity<si::metre, int> q{42, si::metre};
```

In case a quantity class template should use exactly the same unit and a representation type as provided in the initializer, it is recommended to use CTAD:

```cpp
quantity q{42, si::metre};
```

The [[SI]](https://www.bipm.org/en/publications/si-brochure) says:

> The value of the quantity is the product of the number and the unit. The space between the number and the unit is regarded as a multiplication sign (just as a space between units implies multiplication).

Following the above, the value of a quantity can also be created by multiplying a number with a predefined unit:

```cpp
quantity q = 42 * si::metre;
```

The above creates an instance of `quantity<si::metre(), int>`. It is worth noting here that the syntax with the reversed order of arguments is invalid and will not compile (e.g., we can’t write `si::metre * 42`).

The same can be obtained using an optional unit symbol:

```cpp
using namespace si::unit_symbols;

quantity q = 42 * m;
```

Unit symbols introduce a lot of short identifiers into the current scope, which is why they are opt-in. A user has to explicitly “import” them from a dedicated `unit_symbols` namespace.

[[SI]](https://www.bipm.org/en/publications/si-brochure) specifies 7 base and 22 coherent derived units with special names. Additionally, it specifies 24 prefixes. There are also non-SI units accepted for use with SI. Some of them are really popular, for example, minute, hour, day, degree, litre, hectare, tonne. All of those entities compose to allow the creation of a vast number of various derived units.

For example, we can create a quantity of speed with either:

```cpp
quantity speed1 = 60 * si::kilo<si::metre> / non_si::hour;
quantity speed2 = 60 * km / h;
```

The library is optimized to generate short and easy-to-understand types that highly improve the analysis of compile-time errors and debugging experience. All of the above definitions will create an instance of the type `quantity<derived_unit<si::kilo_<si::metre>, per<non_si::hour>>{}, int>>`. As we can see, the type generation is optimized to be easily understood even by non-experts in the domain. The library tries to keep the type’s readability as close to English as possible.

To find more discussion on a quantity creation syntax please refer to the following chapters:

- `explicit` is not explicit enough,
- Why don’t we use UDLs to create quantities?,
- Potential surprises during units composition.

### 11.2 Generic interfaces

#### 11.2.1 The issues with unit-specific interfaces

Unit-specific function interfaces introduce several problems:

```cpp
quantity<km / h> avg_speed(quantity<km> distance, quantity<h> duration)
{
  return distance / duration;
}
```

Using this function:

```cpp
quantity<km / h> s1 = avg_speed(220 * km, 2 * h);
quantity<mi / h> s2 = avg_speed(140 * mi, 2 * h);
quantity<m / s> s3 = avg_speed(20 * m, 2 * s);
```

Problems:

1. Expensive unit conversions at each call and return.
2. Additional conversions to use results in caller’s preferred units.
3. Potential data truncation during conversions.
4. Forces floating-point types; integral types fail to compile without explicit `value_cast` or `force_in`, which can produce incorrect results (e.g., division by zero).

#### 11.2.2 Constraining function parameters with concepts

Generic code using quantity concepts eliminates these issues:

```cpp
auto avg_speed(QuantityOf<isq::length> auto distance,
               QuantityOf<isq::time> auto duration)
{
  return isq::speed(distance / duration);
}
```

This ensures arguments are implicitly convertible to the required quantity types while allowing the compiler to generate optimal code without conversions. Integral types can be safely used, improving performance.

#### 11.2.3 Constraining the function return type

Constraining return types provides documentation and verification:

```cpp
QuantityOf<isq::speed> auto avg_speed(QuantityOf<isq::length> auto distance,
                                      QuantityOf<isq::time> auto duration)
{
  return isq::speed(distance / duration);
}
```

Benefits:

1. Documents expected results for users.
2. Acts as a compile-time test verifying the quantity equation is correct.

#### 11.2.4 Constraining a variable on the stack

When using generic interfaces, constrain variables with concepts to document intent and verify correctness:

```cpp
QuantityOf<isq::speed> auto s1 = avg_speed(220 * km, 2 * h);
QuantityOf<isq::speed> auto s2 = avg_speed(140 * mi, 2 * h);
QuantityOf<isq::speed> auto s3 = avg_speed(20 * m, 2 * s);
```

This serves as documentation and a unit test for the returned type.

### 11.3 The affine space

The affine space distinguishes between:

- ***point*** - a position (*location*, *timestamp*, *altitude*, *temperature reading*, etc.)
- ***displacement vector*** - the difference between two points (*distance*, *duration*, *offset*, etc.)

The *displacement vector* described here is specific to the affine space theory and is not the same thing as the quantity of a vector character that we discuss later (although, in some cases, those terms may overlap).

In the following subchapters, we will often refer to *displacement vectors* simply as *vectors* for brevity.

#### 11.3.1 Operations in the affine space

Valid operations:

- *vector* ± *vector* → *vector*
- -*vector* → *vector*
- *vector* × scalar → *vector*
- scalar × *vector* → *vector*
- *vector* / scalar → *vector*
- *point* - *point* → *vector*
- *point* ± *vector* → *point*
- *vector* + *point* → *point*

It is not possible to:

- add two *points*,
- subtract a *point* from a *vector*,
- multiply nor divide *points* with anything else.

#### 11.3.2 *Displacement vector* is modeled by `quantity`

The `quantity` type models displacement vectors. Construction options include:

- Multiply syntax: `42 * m`, `100 * km / h`
- `delta<Reference>` constructor: `delta<deg_C>(3)`, `delta<isq::height[m]>(42)`
- Two-parameter constructor: `quantity{42, si::metre}`

The multiply syntax is disabled for units with inherent point origins (temperature units). Rationale is in `delta` and `point` creation helpers.

#### 11.3.3 *Point* is modeled by `quantity_point` and `PointOrigin`

The `quantity_point` class template represents points:

```cpp
template<Reference auto R,
         PointOriginFor<get_quantity_spec(R)> auto PO = default_point_origin(R),
         RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity_point;
```

The `PO` parameter specifies the measurement origin. By default, `default_point_origin(R)` provides:

- The unit’s defined origin (e.g., for °C, °F), or
- `natural_point_origin<QuantitySpec>` for other quantities.

Construction requires explicit conversion or the `point` helper:

```cpp
quantity_point qp1(42 * m);              // explicit conversion
quantity_point qp2 = point<m>(42);       // construction helper
quantity_point qp3 = point<deg_C>(21);   // temperature point
```

Multiply syntax is disabled to prevent confusion between vectors and points.

##### 11.3.3.1 `natural_point_origin<QuantitySpec>`

`natural_point_origin<QuantitySpec>` provides a default origin for domains with a well-established, unique zeroth point, eliminating boilerplate:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuNTE5NDQ3bW0iCiAgIGhlaWdodD0iMTguOTc3NTA3bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni41MTk0NDcgMTguOTc3NTA3IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdy03IgogICAgICAgcmVmWD0iMCIKICAgICAgIHJlZlk9IjAiCiAgICAgICBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSIKICAgICAgIG1hcmtlcldpZHRoPSIxIgogICAgICAgbWFya2VySGVpZ2h0PSIxIgogICAgICAgdmlld0JveD0iMCAwIDEgMSIKICAgICAgIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImZpbGw6Y29udGV4dC1zdHJva2U7ZmlsbC1ydWxlOmV2ZW5vZGQ7c3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gMCwwIDUsLTUgLTEyLjUsMCA1LDUgWiIKICAgICAgICAgdHJhbnNmb3JtPSJzY2FsZSgtMC41KSIKICAgICAgICAgaWQ9InBhdGg2LTQiIC8+CiAgICA8L21hcmtlcj4KICA8L2RlZnM+CiAgPGcKICAgICBpZD0ibGF5ZXIxIgogICAgIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yNS42ODgwMzEsLTUuMTM3ODg0NSkiPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuNTtzdHJva2UtZGFzaGFycmF5Om5vbmU7bWFya2VyLWVuZDp1cmwoI0RhcnRBcnJvdy03KSIKICAgICAgIGQ9Ik0gMjUuNjg4MDMxLDIwLjE5MDgwNCBIIDExOC42ODU0OCIKICAgICAgIGlkPSJwYXRoNC0xIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gMzguOTcyNTgyLDE5LjE1MDc0NiB2IDIuMDgwMTE2IgogICAgICAgaWQ9InBhdGg3LTYiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTc4MjM7c3Ryb2tlLWRhc2hhcnJheToxLjE5MTI5LCAwLjI5NzgyMztzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJNIDM4Ljk3MjU4Miw2LjQ3NzA0OTIgViAxOC45NDA1OTQiCiAgICAgICBpZD0icGF0aDItMi0yIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gMTA2LjcwMDI0LDYuNDc3MDQ5IFYgMTguOTQwNTk0IgogICAgICAgaWQ9InBhdGgyLTItMS0wIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gOTQuNDkzMDI2LDYuNDc3MDQ4OSBWIDE4Ljk0MDU5NCIKICAgICAgIGlkPSJwYXRoMi0yLTEtMC0wIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gOTQuNDkzMDI2LDE5LjE1MDc0NiB2IDIuMDgwMTE2IgogICAgICAgaWQ9InBhdGgyLTUtMiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDEwNi43MDAyNCwxOS4xNTA3NDYgdiAyLjA4MDExNiIKICAgICAgIGlkPSJwYXRoMi01LTctOCIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iMzguMjk0OTMzIgogICAgICAgeT0iMjMuNjA1NTE1IgogICAgICAgaWQ9InRleHQyLTEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTQiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iMzguMjk0OTMzIgogICAgICAgICB5PSIyMy42MDU1MTUiPjA8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iOTIuNDQzODAyIgogICAgICAgeT0iMjMuNjI4MjU0IgogICAgICAgaWQ9InRleHQyLTItOSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS05IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI5Mi40NDM4MDIiCiAgICAgICAgIHk9IjIzLjYyODI1NCI+cXAxPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjY1LjcyNDEyOSIKICAgICAgIHk9IjE1LjkwMzc4IgogICAgICAgaWQ9InRleHQyLTItNy00OSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTk2IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI2NS43MjQxMjkiCiAgICAgICAgIHk9IjE1LjkwMzc4Ij5xMTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSIxMDQuNTEyMzMiCiAgICAgICB5PSIyMy42MjgyNTQiCiAgICAgICBpZD0idGV4dDItMi0yLTMxIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iMTA0LjUxMjMzIgogICAgICAgICB5PSIyMy42MjgyNTQiPnFwMjwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0wIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC44NTkwMjUsMTYuOTU4NjI1IEggOTMuODgzMjEzIgogICAgICAgICBpZD0icGF0aDE5IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljg1OTM3NSwxNi44MzM5ODQgdiAwLjI1IGggNTUuMDIzNDM3IHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgyMCIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImcxOCI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gOTIuNTg3ODkxLDE2LjA1MDc4MSAtMC4xNTgyMDQsMC4zMTY0MDYgMS4xODM1OTQsMC41OTE3OTcgLTEuMTgzNTk0LDAuNTkxNzk3IDAuMTU4MjA0LDAuMzE2NDA2IDEuODE2NDA2LC0wLjkwODIwMyB6IgogICAgICAgICAgIGlkPSJwYXRoMTgiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzttaXgtYmxlbmQtbW9kZTpub3JtYWw7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9Ijk2LjAzMDU0OCIKICAgICAgIHk9IjYuNjgzMDEyIgogICAgICAgaWQ9InRleHQyLTItNy00OS01Ij48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iOTYuMDMwNTQ4IgogICAgICAgICB5PSI2LjY4MzAxMiI+cXAyIC0gcXAxPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg4LTAtOSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDk0LjY2ODYwNSw4LjEzNDcyNTkgSCAxMDYuMTUyNyIKICAgICAgICAgaWQ9InBhdGgxMyIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gOTQuNjY3OTY5LDguMDA5NzY1NiB2IDAuMjUgaCAxMS40ODQzNzEgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDE0IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzEyIj4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSAxMDQuODU3NDIsNy4yMjY1NjI1IC0wLjE1ODIsMC4zMTY0MDYyIDEuMTgzNTksMC41OTE3OTY5IC0xLjE4MzU5LDAuNTkxNzk2OSAwLjE1ODIsMC4zMTY0MDYzIDEuODE2NDEsLTAuOTA4MjAzMiB6IgogICAgICAgICAgIGlkPSJwYXRoMTIiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDMtMi02Ij4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC45NDczNDcsMTIuNjM5MjMzIEggMTA2LjA4NTYyIgogICAgICAgICBpZD0icGF0aDE2IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljk0NzI2NiwxMi41MTM2NzIgdiAwLjI1IGggNjcuMTM4Njc0IHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgxNyIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImcxNSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gMTA0Ljc4OTA2LDExLjczMDQ2OSAtMC4xNTgyLDAuMzE2NDA2IDEuMTgzNTksMC41OTE3OTcgLTEuMTgzNTksMC41OTE3OTcgMC4xNTgyLDAuMzE2NDA2IDEuODE2NDEsLTAuOTA4MjAzIHoiCiAgICAgICAgICAgaWQ9InBhdGgxNSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI3MS42ODQ0OTQiCiAgICAgICB5PSIxMS42NTU3NyIKICAgICAgIGlkPSJ0ZXh0Mi0yLTItNS0xIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtMi04NSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNzEuNjg0NDk0IgogICAgICAgICB5PSIxMS42NTU3NyI+cTI8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuODIyMjJweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAiCiAgICAgICB4PSIxMjAuMDQ5NDgiCiAgICAgICB5PSIyMy45MTA0MDgiCiAgICAgICBpZD0idGV4dDEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuODIyMjJweDtzdHJva2Utd2lkdGg6MCIKICAgICAgICAgeD0iMTIwLjA0OTQ4IgogICAgICAgICB5PSIyMy45MTA0MDgiPlE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzttaXgtYmxlbmQtbW9kZTpub3JtYWw7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjU0LjAzNTQ5MiIKICAgICAgIHk9IjYuNjc4ODc3OCIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNDktNS0zLTItNi0yIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNC0xLTgtOC0xIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI1NC4wMzU0OTIiCiAgICAgICAgIHk9IjYuNjc4ODc3OCI+cXAxLnF1YW50aXR5X2Zyb21fdW5pdF96ZXJvKCk8L3RzcGFuPjwvdGV4dD4KICAgIDxnCiAgICAgICBpZD0icGF0aDgtMC05LTgtMC0wLTAiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC4yMTM2NzIzMSwtOTAuOTM3NSkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOS4xMDc3MTksOTkuMDcxODI2IEggOTQuMTE1NzcyIgogICAgICAgICBpZD0icGF0aDU2LTAiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM5LjEwNzQyMiw5OC45NDcyNjYgdiAwLjI1IGggNTUuMDA3ODEyIHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGg1Ny04IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzU1LTQiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDkyLjgyMDMxMiw5OC4xNjQwNjIgLTAuMTU4MjAzLDAuMzE2NDA3IDEuMTgzNTk0LDAuNTkxNzk3IC0xLjE4MzU5NCwwLjU5MTc5NiAwLjE1ODIwMywwLjMxNjQwNyAxLjgxNjQwNywtMC45MDgyMDMgeiIKICAgICAgICAgICBpZD0icGF0aDU1LTkiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICA8L2c+Cjwvc3ZnPgo=)

```cpp
quantity_point<isq::distance[si::metre]> qp1(100 * m);
quantity_point<isq::distance[si::metre]> qp2 = point<m>(120);

assert(qp2 - qp1 == 20 * m);
assert(qp1.quantity_from_zero() == 100 * m);
// auto res = qp1 + qp2;   // Compile-time error
```

Key design considerations:

- Points can be explicitly constructed from quantities when using `zeroth_point_origin`.
- A point has no inherent value—it’s a position expressible with different displacement vectors from different origins.
- **Safety trade-off**: `natural_point_origin` makes quantity points compatible when their quantity types are compatible (e.g., `isq::distance` and `isq::height` points can be subtracted), which may be surprising but enables ergonomic usage for common cases.

##### 11.3.3.2 Absolute *point* origin

Absolute point origins establish isolated, independent spaces where points are incompatible even with the same quantity type:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuNDAzMjM2bW0iCiAgIGhlaWdodD0iMTguOTA0OTM0bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni40MDMyMzYgMTguOTA0OTM0IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdyIKICAgICAgIHJlZlg9IjAiCiAgICAgICByZWZZPSIwIgogICAgICAgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiCiAgICAgICBtYXJrZXJXaWR0aD0iMSIKICAgICAgIG1hcmtlckhlaWdodD0iMSIKICAgICAgIHZpZXdCb3g9IjAgMCAxIDEiCiAgICAgICBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOmNvbnRleHQtc3Ryb2tlO2ZpbGwtcnVsZTpldmVub2RkO3N0cm9rZTpub25lIgogICAgICAgICBkPSJNIDAsMCA1LC01IC0xMi41LDAgNSw1IFoiCiAgICAgICAgIHRyYW5zZm9ybT0ic2NhbGUoLTAuNSkiCiAgICAgICAgIGlkPSJwYXRoNiIgLz4KICAgIDwvbWFya2VyPgogIDwvZGVmcz4KICA8ZwogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTI1LjgwNDIzNiwtMzAuMTkwNTc4KSI+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC41O3N0cm9rZS1kYXNoYXJyYXk6bm9uZTttYXJrZXItZW5kOnVybCgjRGFydEFycm93KSIKICAgICAgIGQ9Ik0gMjUuODA0MjM2LDQ1LjE2MTEwNSBIIDExOC44MDE2OCIKICAgICAgIGlkPSJwYXRoMSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDM5LjA4ODc4Nyw0NC4xMjEwNDcgdiAyLjA4MDExNiIKICAgICAgIGlkPSJwYXRoMiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5NzgyMztzdHJva2UtZGFzaGFycmF5OjEuMTkxMjksIDAuMjk3ODIzO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gMzkuMDg4Nzg3LDMyLjM4Mjc5NyBWIDQzLjkxMDg5NSIKICAgICAgIGlkPSJwYXRoMi0yIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gOTQuNjA5MjMxLDQ0LjEyMTA0NyB2IDIuMDgwMTE2IgogICAgICAgaWQ9InBhdGgyLTUiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAxMDYuODE2NDQsNDQuMTIxMDQ3IHYgMi4wODAxMTYiCiAgICAgICBpZD0icGF0aDItNS03IiAvPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSIzNS42OTMzMDYiCiAgICAgICB5PSI0OC41NzU4MTciCiAgICAgICBpZD0idGV4dDIiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgIHg9IjM1LjY5MzMwNiIKICAgICAgICAgeT0iNDguNTc1ODE3Ij5vcmlnaW48L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iOTIuNTYwMDA1IgogICAgICAgeT0iNDguNTk4NTU3IgogICAgICAgaWQ9InRleHQyLTIiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTkiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgIHg9IjkyLjU2MDAwNSIKICAgICAgICAgeT0iNDguNTk4NTU3Ij5xcDE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNjUuODQwMzMyIgogICAgICAgeT0iNDAuODc0MDkyIgogICAgICAgaWQ9InRleHQyLTItNyI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI2NS44NDAzMzIiCiAgICAgICAgIHk9IjQwLjg3NDA5MiI+cTE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iMTA0LjYyODU1IgogICAgICAgeT0iNDguNTk4NTU3IgogICAgICAgaWQ9InRleHQyLTItMiI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS02IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwMDAwZGQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSIxMDQuNjI4NTUiCiAgICAgICAgIHk9IjQ4LjU5ODU1NyI+cXAyPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGgzIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOS4xMDc1MjIsNDEuOTI4OTI2IEggOTMuOTk5NDE4IgogICAgICAgICBpZD0icGF0aDI4IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM5LjEwNzQyMiw0MS44MDQ2ODcgdiAwLjI1IEggOTQgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDI5IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzI3Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA5Mi43MDMxMjUsNDEuMDIxNDg0IC0wLjE1ODIwMywwLjMxNjQwNyAxLjE4MzU5NCwwLjU5MTc5NiAtMS4xODM1OTQsMC41OTE3OTcgMC4xNTgyMDMsMC4zMTY0MDcgMS44MTY0MDYsLTAuOTA4MjA0IHoiCiAgICAgICAgICAgaWQ9InBhdGgyNyIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJwYXRoMy0yIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC45OTc0MDYsMzcuNjA5NTM2IEggMTA2LjIwMTgyIgogICAgICAgICBpZD0icGF0aDIyIiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljk5ODA0NywzNy40ODQzNzUgdiAwLjI1IGggNjcuMjAzMTIzIHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgyMyIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImcyMSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gMTA0LjkwNjI1LDM2LjcwMTE3MiAtMC4xNTgyLDAuMzE2NDA2IDEuMTgzNTksMC41OTE3OTcgLTEuMTgzNTksMC41OTE3OTcgMC4xNTgyLDAuMzE2NDA2IDEuODE2NDEsLTAuOTA4MjAzIHoiCiAgICAgICAgICAgaWQ9InBhdGgyMSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI3MS44MDA2OTciCiAgICAgICB5PSIzNi42MjYwNzYiCiAgICAgICBpZD0idGV4dDItMi0yLTUiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktNi0yIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiMwMDAwZGQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI3MS44MDA2OTciCiAgICAgICAgIHk9IjM2LjYyNjA3NiI+cTI8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJNIDEwNi43NzQ3OSwzMS41Mjk3NDEgViA0My45OTMyODUiCiAgICAgICBpZD0icGF0aDItMi0xLTAtMyIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJNIDk0LjU2NzU4MiwzMS41Mjk3NDEgViA0My45OTMyODUiCiAgICAgICBpZD0icGF0aDItMi0xLTAtMC0zIiAvPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO21peC1ibGVuZC1tb2RlOm5vcm1hbDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iOTYuMTA1MTAzIgogICAgICAgeT0iMzEuNzM1NzA0IgogICAgICAgaWQ9InRleHQyLTItNy00OS01LTMiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05Ni00LTEiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgIHg9Ijk2LjEwNTEwMyIKICAgICAgICAgeT0iMzEuNzM1NzA0Ij5xcDIgLSBxcDE8L3RzcGFuPjwvdGV4dD4KICAgIDxnCiAgICAgICBpZD0icGF0aDgtMC05LTgiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSA5NC42NzcwMTEsMzMuMTg3NDE4IEggMTA2LjIyNzI1IgogICAgICAgICBpZD0icGF0aDI1IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSA5NC42Nzc3MzQsMzMuMDYyNSB2IDAuMjUgaCAxMS41NDg4MjYgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDI2IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzI0Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSAxMDQuOTMxNjQsMzIuMjc5Mjk3IC0wLjE1ODIsMC4zMTY0MDYgMS4xODM1OSwwLjU5MTc5NyAtMS4xODM1OSwwLjU5MTc5NyAwLjE1ODIsMC4zMTY0MDYgMS44MTY0MSwtMC45MDgyMDMgeiIKICAgICAgICAgICBpZD0icGF0aDI0IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjgyMjIycHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowIgogICAgICAgeD0iMTIwLjA0OTQ4IgogICAgICAgeT0iNDguODgwNzExIgogICAgICAgaWQ9InRleHQxLTEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xLTAiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi44MjIyMnB4O3N0cm9rZS13aWR0aDowIgogICAgICAgICB4PSIxMjAuMDQ5NDgiCiAgICAgICAgIHk9IjQ4Ljg4MDcxMSI+UTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO21peC1ibGVuZC1tb2RlOm5vcm1hbDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNTMuODkyNzA4IgogICAgICAgeT0iMzEuNzMxNTcxIgogICAgICAgaWQ9InRleHQyLTItNy00OS01LTMtMi02LTItOCI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTk2LTQtMS04LTgtMS01IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI1My44OTI3MDgiCiAgICAgICAgIHk9IjMxLjczMTU3MSI+cXAxLnF1YW50aXR5X2Zyb20ob3JpZ2luKTwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0wLTktOC0wLTAtMC01IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuMTExMzk0MzUsLTY1Ljg4NDc2NSkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOS4xMDc3MTksOTkuMDcxODI2IEggOTQuMTE1NzcyIgogICAgICAgICBpZD0icGF0aDU2LTAtNSIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMzkuMTA3NDIyLDk4Ljk0NzI2NiB2IDAuMjUgaCA1NS4wMDc4MTIgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDU3LTgtMiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc1NS00LTYiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDkyLjgyMDMxMiw5OC4xNjQwNjIgLTAuMTU4MjAzLDAuMzE2NDA3IDEuMTgzNTk0LDAuNTkxNzk3IC0xLjE4MzU5NCwwLjU5MTc5NiAwLjE1ODIwMywwLjMxNjQwNyAxLjgxNjQwNywtMC45MDgyMDMgeiIKICAgICAgICAgICBpZD0icGF0aDU1LTktNCIgLz4KICAgICAgPC9nPgogICAgPC9nPgogIDwvZz4KPC9zdmc+Cg==)

```cpp
inline constexpr struct origin : absolute_point_origin<isq::distance> {} origin;

// quantity_point<si::metre, origin> qp1{100 * m};        // Compile-time error
quantity_point<si::metre, origin> qp1 = origin + 100 * m;
quantity_point qp2{120 * m, origin};  // alternative syntax

assert(qp1.quantity_from(origin) == 100 * m);
assert(qp1 - origin == 100 * m);
assert(qp2 - qp1 == 20 * m);
assert(origin - qp1 == -100 * m);
// assert(origin - origin == 0 * m);   // Compile-time error
```

**Design rationale**: Safety requires explicit construction with both origin and displacement vector. Direct construction from quantities is prevented. Subtracting two `absolute_point_origin` instances is forbidden because they lack unit information needed to determine the resulting quantity type.

###### 11.3.3.2.1 Modeling independent spaces in one domain

Absolute point origins enable multiple independent coordinate systems within the same quantity type:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuOTk5Mzc0bW0iCiAgIGhlaWdodD0iMjEuOTU4ODI2bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni45OTkzNzQgMjEuOTU4ODI2IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICBpbmtzY2FwZTp2ZXJzaW9uPSIxLjMuMiAoMDkxZTIwZSwgMjAyMy0xMS0yNSwgY3VzdG9tKSIKICAgc29kaXBvZGk6ZG9jbmFtZT0iYWZmaW5lIHNwYWNlLnN2ZyIKICAgeG1sbnM6aW5rc2NhcGU9Imh0dHA6Ly93d3cuaW5rc2NhcGUub3JnL25hbWVzcGFjZXMvaW5rc2NhcGUiCiAgIHhtbG5zOnNvZGlwb2RpPSJodHRwOi8vc29kaXBvZGkuc291cmNlZm9yZ2UubmV0L0RURC9zb2RpcG9kaS0wLmR0ZCIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8c29kaXBvZGk6bmFtZWR2aWV3CiAgICAgaWQ9Im5hbWVkdmlldzEiCiAgICAgcGFnZWNvbG9yPSIjZmZmZmZmIgogICAgIGJvcmRlcmNvbG9yPSIjMDAwMDAwIgogICAgIGJvcmRlcm9wYWNpdHk9IjAuMjUiCiAgICAgaW5rc2NhcGU6c2hvd3BhZ2VzaGFkb3c9IjIiCiAgICAgaW5rc2NhcGU6cGFnZW9wYWNpdHk9IjAuMCIKICAgICBpbmtzY2FwZTpwYWdlY2hlY2tlcmJvYXJkPSIwIgogICAgIGlua3NjYXBlOmRlc2tjb2xvcj0iI2QxZDFkMSIKICAgICBpbmtzY2FwZTpkb2N1bWVudC11bml0cz0ibW0iCiAgICAgaW5rc2NhcGU6em9vbT0iMi44Mjg0MjcxIgogICAgIGlua3NjYXBlOmN4PSIzMTQuMTMyMTkiCiAgICAgaW5rc2NhcGU6Y3k9IjQwNS44NzkyOSIKICAgICBpbmtzY2FwZTp3aW5kb3ctd2lkdGg9IjE5MjAiCiAgICAgaW5rc2NhcGU6d2luZG93LWhlaWdodD0iMTAxOCIKICAgICBpbmtzY2FwZTp3aW5kb3cteD0iLTYiCiAgICAgaW5rc2NhcGU6d2luZG93LXk9Ii02IgogICAgIGlua3NjYXBlOndpbmRvdy1tYXhpbWl6ZWQ9IjEiCiAgICAgaW5rc2NhcGU6Y3VycmVudC1sYXllcj0ibGF5ZXIxIiAvPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdy00IgogICAgICAgcmVmWD0iMCIKICAgICAgIHJlZlk9IjAiCiAgICAgICBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSIKICAgICAgIGlua3NjYXBlOnN0b2NraWQ9IkRhcnQgYXJyb3ciCiAgICAgICBtYXJrZXJXaWR0aD0iMSIKICAgICAgIG1hcmtlckhlaWdodD0iMSIKICAgICAgIHZpZXdCb3g9IjAgMCAxIDEiCiAgICAgICBpbmtzY2FwZTppc3N0b2NrPSJ0cnVlIgogICAgICAgaW5rc2NhcGU6Y29sbGVjdD0iYWx3YXlzIgogICAgICAgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iZmlsbDpjb250ZXh0LXN0cm9rZTtmaWxsLXJ1bGU6ZXZlbm9kZDtzdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAwLDAgNSwtNSAtMTIuNSwwIDUsNSBaIgogICAgICAgICB0cmFuc2Zvcm09InNjYWxlKC0wLjUpIgogICAgICAgICBpZD0icGF0aDYtMCIgLz4KICAgIDwvbWFya2VyPgogICAgPG1hcmtlcgogICAgICAgc3R5bGU9Im92ZXJmbG93OnZpc2libGUiCiAgICAgICBpZD0iRGFydEFycm93LTQtNjMiCiAgICAgICByZWZYPSIwIgogICAgICAgcmVmWT0iMCIKICAgICAgIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIgogICAgICAgaW5rc2NhcGU6c3RvY2tpZD0iRGFydCBhcnJvdyIKICAgICAgIG1hcmtlcldpZHRoPSIxIgogICAgICAgbWFya2VySGVpZ2h0PSIxIgogICAgICAgdmlld0JveD0iMCAwIDEgMSIKICAgICAgIGlua3NjYXBlOmlzc3RvY2s9InRydWUiCiAgICAgICBpbmtzY2FwZTpjb2xsZWN0PSJhbHdheXMiCiAgICAgICBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOmNvbnRleHQtc3Ryb2tlO2ZpbGwtcnVsZTpldmVub2RkO3N0cm9rZTpub25lIgogICAgICAgICBkPSJNIDAsMCA1LC01IC0xMi41LDAgNSw1IFoiCiAgICAgICAgIHRyYW5zZm9ybT0ic2NhbGUoLTAuNSkiCiAgICAgICAgIGlkPSJwYXRoNi0wLTEiIC8+CiAgICA8L21hcmtlcj4KICA8L2RlZnM+CiAgPGcKICAgICBpbmtzY2FwZTpsYWJlbD0iTGF5ZXIgMSIKICAgICBpbmtzY2FwZTpncm91cG1vZGU9ImxheWVyIgogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTI1LjIwODA5OCwtNjIuNzk5ODI2KSI+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC41O3N0cm9rZS1kYXNoYXJyYXk6bm9uZTttYXJrZXItZW5kOnVybCgjRGFydEFycm93LTQpIgogICAgICAgZD0iTSAyNS44MzYwOTUsNjkuMTUyMDIyIEggMTE4LjgzMzUzIgogICAgICAgaWQ9InBhdGg0IgogICAgICAgaW5rc2NhcGU6ZXhwb3J0LWZpbGVuYW1lPSJcXHdzbC5sb2NhbGhvc3RcVWJ1bnR1XGhvbWVcbXB1c3pccmVwb3Ncd2cyMS1wYXBlcnNcc3JjXGltZ1xhZmZpbmVfc3BhY2VfMy5zdmciCiAgICAgICBpbmtzY2FwZTpleHBvcnQteGRwaT0iOTYiCiAgICAgICBpbmtzY2FwZTpleHBvcnQteWRwaT0iOTYiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC41O3N0cm9rZS1kYXNoYXJyYXk6bm9uZTttYXJrZXItZW5kOnVybCgjRGFydEFycm93LTQtNjMpIgogICAgICAgZD0ibSAyNS44MzYxLDc1LjAzMTYxNCBoIDkyLjk5NzQzIgogICAgICAgaWQ9InBhdGg0LTE5IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Ik0gMzkuMTIwNjQ2LDY4LjExMTk2NCBWIDcwLjE5MjA4IgogICAgICAgaWQ9InBhdGg3IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk3ODIzO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTEyOSwgMC4yOTc4MjM7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSAzOS4xMjA2NDYsNjMuNDgzMDg4IHYgNC40MTg3MjQiCiAgICAgICBpZD0icGF0aDItMi03IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk3ODIzO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTEyOSwgMC4yOTc4MjM7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSAxMDYuODQ4Myw2My40ODMwODggdiA0LjQxODcyNCIKICAgICAgIGlkPSJwYXRoMi0yLTEtNSIgLz4KICAgIDxnCiAgICAgICBpZD0iZzIiCiAgICAgICB0cmFuc2Zvcm09Im1hdHJpeCgxLDAsMCwtMSwwLDE0NC4xNTExKSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgICAgZD0ibSA5NC42NDEwOSw2NC4xMDEyNTkgdiAzLjgwMDU0NyIKICAgICAgICAgaWQ9InBhdGgyLTItNC00LTAiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgZD0ibSA5NC42NDEwOSw2OC4xMTE5NTggdiAyLjA4MDExNiIKICAgICAgICAgaWQ9InBhdGgyLTUtNC0xIiAvPgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJnMi0wIgogICAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMSwwLDAsLTEsLTQwLjg1MTUwNiwxNDQuMTUxMSkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgIGQ9Im0gOTQuNjQxMDksNjQuMTAxMjU5IHYgMy44MDA1NDciCiAgICAgICAgIGlkPSJwYXRoMi0yLTQtNC0wLTkiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgZD0ibSA5NC42NDEwOSw2OC4xMTE5NTggdiAyLjA4MDExNiIKICAgICAgICAgaWQ9InBhdGgyLTUtNC0xLTEiIC8+CiAgICA8L2c+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0iTSAxMDYuODQ4Myw2OC4xMTE5NjQgViA3MC4xOTIwOCIKICAgICAgIGlkPSJwYXRoMi01LTctNSIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAiCiAgICAgICB4PSIzNS4wMTczNzIiCiAgICAgICB5PSI3Mi41NjY3MzQiCiAgICAgICBpZD0idGV4dDItOCI+PHRzcGFuCiAgICAgICAgIHNvZGlwb2RpOnJvbGU9ImxpbmUiCiAgICAgICAgIGlkPSJ0c3BhbjItNiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowIgogICAgICAgICB4PSIzNS4wMTczNzIiCiAgICAgICAgIHk9IjcyLjU2NjczNCI+b3JpZ2luMjwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI0OS44MjQ5NzQiCiAgICAgICB5PSI3Mi40NjkxMDkiCiAgICAgICBpZD0idGV4dDItOC03Ij48dHNwYW4KICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSIKICAgICAgICAgaWQ9InRzcGFuMi02LTQiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgIHg9IjQ5LjgyNDk3NCIKICAgICAgICAgeT0iNzIuNDY5MTA5Ij5vcmlnaW4xPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjQ2OTQ0cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjkyLjU5MTg2NiIKICAgICAgIHk9IjcyLjU4OTQ3IgogICAgICAgaWQ9InRleHQyLTItOCI+PHRzcGFuCiAgICAgICAgIHNvZGlwb2RpOnJvbGU9ImxpbmUiCiAgICAgICAgIGlkPSJ0c3BhbjItOS0zIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI5Mi41OTE4NjYiCiAgICAgICAgIHk9IjcyLjU4OTQ3Ij5xcDE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNzMuMjE1NDI0IgogICAgICAgeT0iNzcuNjIwMTI1IgogICAgICAgaWQ9InRleHQyLTItNy00Ij48dHNwYW4KICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSIKICAgICAgICAgaWQ9InRzcGFuMi05LTAtOSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNzMuMjE1NDI0IgogICAgICAgICB5PSI3Ny42MjAxMjUiPnExPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjQ2OTQ0cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjEwNC42NjA0MSIKICAgICAgIHk9IjcyLjU4OTQ3IgogICAgICAgaWQ9InRleHQyLTItMi0zIj48dHNwYW4KICAgICAgICAgc29kaXBvZGk6cm9sZT0ibGluZSIKICAgICAgICAgaWQ9InRzcGFuMi05LTYtMjgiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgIHg9IjEwNC42NjA0MSIKICAgICAgICAgeT0iNzIuNTg5NDciPnFwMjwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDBkZDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gNTMuNzQyMTYzLDc4LjY3NDk0NSBIIDk0LjI0NzI0OCIKICAgICAgICAgaWQ9InBhdGgzNCIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSA1My43NDIxODcsNzguNTUwNzgxIHYgMC4yNSBoIDQwLjUwNTg2IHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgzNSIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImczMyI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gOTIuOTUxMTcyLDc3Ljc2NzU3OCAtMC4xNTgyMDMsMC4zMTY0MDYgMS4xODM1OTMsMC41OTE3OTcgLTEuMTgzNTkzLDAuNTkxNzk3IDAuMTU4MjAzLDAuMzE2NDA2IDEuODE2NDA2LC0wLjkwODIwMyB6IgogICAgICAgICAgIGlkPSJwYXRoMzMiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDMtMi05IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwzLjcwNDE2NjgpIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC44OTc2MzMsNjEuNjAwNDU1IEggMTA2LjMyNjU2IgogICAgICAgICBpZD0icGF0aDMxIiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljg5ODQzNyw2MS40NzQ2MDkgdiAwLjI1IGggNjcuNDI3NzMzIHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgzMiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImczMCI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gMTA1LjAzMTI1LDYwLjY5MTQwNiAtMC4xNTgyLDAuMzE2NDA2IDEuMTgzNTksMC41OTE3OTcgLTEuMTgzNTksMC41OTE3OTcgMC4xNTgyLDAuMzE2NDA2IDEuODE2NDEsLTAuOTA4MjAzIHoiCiAgICAgICAgICAgaWQ9InBhdGgzMCIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI3MS44NzkzMjYiCiAgICAgICB5PSI2NC4zMjExODIiCiAgICAgICBpZD0idGV4dDItMi0yLTUtNiI+PHRzcGFuCiAgICAgICAgIHNvZGlwb2RpOnJvbGU9ImxpbmUiCiAgICAgICAgIGlkPSJ0c3BhbjItOS02LTItOCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNzEuODc5MzI2IgogICAgICAgICB5PSI2NC4zMjExODIiPnEyPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC1hbmNob3I6bWlkZGxlO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4yOTg7c3Ryb2tlLW1pdGVybGltaXQ6NDtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjAiCiAgICAgICB4PSIzNi41OTM2MzkiCiAgICAgICB5PSI4MS41MTgzNjQiCiAgICAgICBpZD0idGV4dDUiPjx0c3BhbgogICAgICAgICBzb2RpcG9kaTpyb2xlPSJsaW5lIgogICAgICAgICBpZD0idHNwYW41IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDt0ZXh0LWFsaWduOmNlbnRlcjt0ZXh0LWFuY2hvcjptaWRkbGU7ZmlsbDojMDAwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowLjI5OCIKICAgICAgICAgeD0iMzYuNTkzNjM5IgogICAgICAgICB5PSI4MS41MTgzNjQiPnVucmVsYXRlZDwvdHNwYW4+PHRzcGFuCiAgICAgICAgIHNvZGlwb2RpOnJvbGU9ImxpbmUiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSIzNi41OTM2MzkiCiAgICAgICAgIHk9Ijg0LjE2NDIiCiAgICAgICAgIGlkPSJ0c3BhbjYiPihubyBrbm93biB0cmFuc2xhdGlvbik8L3RzcGFuPjwvdGV4dD4KICAgIDxnCiAgICAgICBpZD0icGF0aDkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDI5LjE4MTY0MSw2OS43ODEyNSAtMC4xNzc3MzUsMC4wODc4OSA0Ljk1NzAzMSw5LjgyMjI2NSAwLjE3NzczNSwtMC4wODc4OSB6IgogICAgICAgICBpZD0icGF0aDM5IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzM4Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSAyOC45MDYyNSw2OS40NTcwMzEgMC4wMDU5LDEuNjA5Mzc1IDAuMjgxMjUsLTAuMDAyIC0wLjAwMzksLTEuMDQ4ODI4IDAuODM5ODQ0LDAuNjI2OTUzIDAuMTY3OTY5LC0wLjIyNDYwOSB6IgogICAgICAgICAgIGlkPSJwYXRoMzgiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDktMCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNDMuODM3ODkxLDc1LjgzNzg5MSAtMy40NjI4OTEsMy42NDg0MzcgMC4xNDQ1MzEsMC4xMzQ3NjYgMy40NjA5MzgsLTMuNjQ2NDg1IHoiCiAgICAgICAgIGlkPSJwYXRoMzciIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnMzYiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDQ0LjE5MzM1OSw3NS42MDc0MjIgLTEuNTExNzE4LDAuNTQ4ODI4IDAuMDkzNzUsMC4yNjE3MTkgMC45ODYzMjgsLTAuMzU3NDIyIC0wLjMwNDY4OCwxLjAwMzkwNiAwLjI2NzU3OCwwLjA4MDA4IHoiCiAgICAgICAgICAgaWQ9InBhdGgzNiIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi44MjIyMnB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MCIKICAgICAgIHg9IjEyMC4wNDk0OCIKICAgICAgIHk9IjcyLjg3MTYyIgogICAgICAgaWQ9InRleHQxLTAiPjx0c3BhbgogICAgICAgICBzb2RpcG9kaTpyb2xlPSJsaW5lIgogICAgICAgICBpZD0idHNwYW4xLTEiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi44MjIyMnB4O3N0cm9rZS13aWR0aDowIgogICAgICAgICB4PSIxMjAuMDQ5NDgiCiAgICAgICAgIHk9IjcyLjg3MTYyIj5RPC90c3Bhbj48L3RleHQ+CiAgPC9nPgo8L3N2Zz4K)

```cpp
inline constexpr struct origin1 : absolute_point_origin<isq::distance> {} origin1;
inline constexpr struct origin2 : absolute_point_origin<isq::distance> {} origin2;

quantity_point qp1 = origin1 + 100 * m;
quantity_point qp2 = origin2 + 120 * m;

assert(qp1 - origin1 == 100 * m);
// assert(qp2 - qp1 == 20 * m);         // Compile-time error: incompatible origins
// assert(qp1 - origin2 == 100 * m);    // Compile-time error: wrong origin
```

##### 11.3.3.3 Relative *point* origin

Relative point origins support common scales with multiple reference points that remain compatible (*temperatures*, *timestamps*, *altitudes*):

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuMzI2OTM1bW0iCiAgIGhlaWdodD0iMjkuNzM0MDU1bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni4zMjY5MzUgMjkuNzM0MDU1IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdy00LTYiCiAgICAgICByZWZYPSIwIgogICAgICAgcmVmWT0iMCIKICAgICAgIG9yaWVudD0iYXV0by1zdGFydC1yZXZlcnNlIgogICAgICAgbWFya2VyV2lkdGg9IjEiCiAgICAgICBtYXJrZXJIZWlnaHQ9IjEiCiAgICAgICB2aWV3Qm94PSIwIDAgMSAxIgogICAgICAgcHJlc2VydmVBc3BlY3RSYXRpbz0ieE1pZFlNaWQiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iZmlsbDpjb250ZXh0LXN0cm9rZTtmaWxsLXJ1bGU6ZXZlbm9kZDtzdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAwLDAgNSwtNSAtMTIuNSwwIDUsNSBaIgogICAgICAgICB0cmFuc2Zvcm09InNjYWxlKC0wLjUpIgogICAgICAgICBpZD0icGF0aDYtMC0yIiAvPgogICAgPC9tYXJrZXI+CiAgPC9kZWZzPgogIDxnCiAgICAgaWQ9ImxheWVyMSIKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjUuODgwNTQ1LC05Ni42MDQyODMpIj4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzt0ZXh0LWFsaWduOmNlbnRlcjt0ZXh0LWFuY2hvcjptaWRkbGU7ZmlsbDojMDAwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtbWl0ZXJsaW1pdDo0O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MCIKICAgICAgIHg9IjM4Ljk2ODM0OSIKICAgICAgIHk9IjEyMy4wOTgwNSIKICAgICAgIGlkPSJ0ZXh0NS03Ij48dHNwYW4KICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC1hbmNob3I6bWlkZGxlO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MC4yOTgiCiAgICAgICAgIHg9IjM4Ljk2ODM0OSIKICAgICAgICAgeT0iMTIzLjA5ODA1IgogICAgICAgICBpZD0idHNwYW40Ij5hYnNvbHV0ZTwvdHNwYW4+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSIzOC45NjgzNDkiCiAgICAgICAgIHk9IjEyNS43NDM4OSIKICAgICAgICAgaWQ9InRzcGFuNyI+cG9pbnQgb3JpZ2luPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg5LTAtNiI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMzguOTc0NjA5LDExNi42ODk0NSAtMC4wODc4OSw0LjQ0MTQxIDAuMTk5MjE4LDAuMDA0IDAuMDg1OTQsLTQuNDQxNDEgeiIKICAgICAgICAgaWQ9InBhdGg2MiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gMzkuMDgyMDMxLDExNi4yNzkzIC0wLjc0ODA0NywxLjQyMzgzIDAuMjQ4MDQ3LDAuMTMwODUgMC40ODgyODEsLTAuOTI3NzMgMC40NDkyMTksMC45NDUzMSAwLjI1MzkwNiwtMC4xMTkxNCB6IgogICAgICAgICAgIGlkPSJwYXRoNjEiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzttaXgtYmxlbmQtbW9kZTpub3JtYWw7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9Ijk2LjIwMjE5NCIKICAgICAgIHk9Ijk4LjE0OTQxNCIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNDktNS0zLTIiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05Ni00LTEtOCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iOTYuMjAyMTk0IgogICAgICAgICB5PSI5OC4xNDk0MTQiPnFwMiAtIHFwMTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO21peC1ibGVuZC1tb2RlOm5vcm1hbDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNzAuNzQ1MjAxIgogICAgICAgeT0iOTguMTQ1Mjc5IgogICAgICAgaWQ9InRleHQyLTItNy00OS01LTMtMi02Ij48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNC0xLTgtOCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNzAuNzQ1MjAxIgogICAgICAgICB5PSI5OC4xNDUyNzkiPnFwMS5xdWFudGl0eV9mcm9tKEQpPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg4LTAtOS04LTAiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLDAuNTI5MTY2NjMpIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gOTQuNzA3OTU0LDk5LjA3MTgyNiBIIDEwNi4zMjQzNCIKICAgICAgICAgaWQ9InBhdGg1OSIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gOTQuNzA3MDMxLDk4Ljk0NzI2NiB2IDAuMjUgaCAxMS42MTcxODkgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDYwIiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzU4Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSAxMDUuMDI5Myw5OC4xNjQwNjIgLTAuMTU4MjEsMC4zMTY0MDcgMS4xODM2LDAuNTkxNzk3IC0xLjE4MzYsMC41OTE3OTYgMC4xNTgyMSwwLjMxNjQwNyAxLjgxNDQ1LC0wLjkwODIwMyB6IgogICAgICAgICAgIGlkPSJwYXRoNTgiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDgtMC05LTgtMC0wIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDtzdHJva2Utd2lkdGg6MTstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNjguNzYwOTc3LDk5LjQ3NjQzMyB2IDAuMjUgaCAyNS4zNTQyNTggdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDU3IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzU1IgogICAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLDAuNTI5MTY2NjMpIj4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA5Mi44MjAzMTIsOTguMTY0MDYyIC0wLjE1ODIwMywwLjMxNjQwNyAxLjE4MzU5NCwwLjU5MTc5NyAtMS4xODM1OTQsMC41OTE3OTYgMC4xNTgyMDMsMC4zMTY0MDcgMS44MTY0MDcsLTAuOTA4MjAzIHoiCiAgICAgICAgICAgaWQ9InBhdGg1NSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuNTtzdHJva2UtZGFzaGFycmF5Om5vbmU7bWFya2VyLWVuZDp1cmwoI0RhcnRBcnJvdy00LTYpIgogICAgICAgZD0iTSAyNS44ODA1NDUsMTExLjgzNzA4IEggMTE4Ljg3Nzk4IgogICAgICAgaWQ9InBhdGg0LTUiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAzOS4xNjUwOTYsMTEwLjc5NzAxIHYgMi4wODAxMyIKICAgICAgIGlkPSJwYXRoNy02OCIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5NzgyMztzdHJva2UtZGFzaGFycmF5OjEuMTkxMjksIDAuMjk3ODIzO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Im0gMzkuMTY1MDk2LDEwMi45ODc1OCB2IDcuNTk5MjgiCiAgICAgICBpZD0icGF0aDItMi03LTQiIC8+CiAgICA8ZwogICAgICAgaWQ9ImczIgogICAgICAgdHJhbnNmb3JtPSJtYXRyaXgoMSwwLDAsMC45Mjg0NTIwNywwLDguMDc2MTIwNCkiCiAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjEuMDM3ODIiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjMwOTA4NTtzdHJva2UtZGFzaGFycmF5OjEuMjM2MzQsIDAuMzA5MDg1O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgICAgZD0iTSAxMDYuODkyNzUsOTcuNDIxNjkzIFYgMTEwLjU4Njg2IgogICAgICAgICBpZD0icGF0aDItMi0xLTUtNiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc1LTgiCiAgICAgICAgIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE0LjE2OTY0NSw3Mi44NDc1MDIpIgogICAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjEuMDM3ODIiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4zMDkyNjk7c3Ryb2tlLWRhc2hhcnJheToxLjIzNzA4LCAwLjMwOTI2OTtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgICAgZD0ibSA4MC41MTU4OTUsMjQuNTg0MzEzIHYgMTMuMTU0OTgiCiAgICAgICAgICAgaWQ9InBhdGgyLTItNC00LTUiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM5NTcxNztzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICAgICAgZD0ibSA4MC41MTU4OTUsMzcuOTQ5NDQ1IHYgMi4wODAxMTYiCiAgICAgICAgICAgaWQ9InBhdGgyLTUtNC04IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTg7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTg7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSA1MS4wMjc3MDQsMTA2Ljc4NjI4IHYgMy44MDA1NyIKICAgICAgIGlkPSJwYXRoMi0yLTQtNC05LTgiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSA1MS4wMjc3MDQsMTEwLjc5NyB2IDIuMDgwMTIiCiAgICAgICBpZD0icGF0aDItNS00LTctNSIgLz4KICAgIDxnCiAgICAgICBpZD0iZzUtNy01LTAiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTguOTg3MzA3LDcyLjg0NzUwMikiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgIGQ9Im0gODAuNTE1ODk1LDMzLjkzODc0NiB2IDMuODAwNTQ3IgogICAgICAgICBpZD0icGF0aDItMi00LTQtOS04LTMiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgZD0ibSA4MC41MTU4OTUsMzcuOTQ5NDQ1IHYgMi4wODAxMTYiCiAgICAgICAgIGlkPSJwYXRoMi01LTQtNy01LTgiIC8+CiAgICA8L2c+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAxMDYuODkyNzUsMTEwLjc5NzAxIHYgMi4wODAxMyIKICAgICAgIGlkPSJwYXRoMi01LTctNS0yIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk3ODIzO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTEyOSwgMC4yOTc4MjM7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0iTSA2OC45NDQ0MTYsOTguNjg0NTQyIFYgMTEwLjc1MDcyIgogICAgICAgaWQ9InBhdGgyLTItMS01LTYtNiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDY4Ljk0NDQxNywxMTAuNzk2OTkgdiAyLjA4MDEzIgogICAgICAgaWQ9InBhdGgyLTUtNy01LTItMSIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNTAuMTIyNDYzIgogICAgICAgeT0iMTE1LjUxNDM3IgogICAgICAgaWQ9InRleHQyLTgtNSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItNi03IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgICB4PSI1MC4xMjI0NjMiCiAgICAgICAgIHk9IjExNS41MTQzNyI+QjwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzI3OWIxNDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC44MTgxODIiCiAgICAgICB4PSIzOC4yOTE5NTQiCiAgICAgICB5PSIxMTUuNTE0MzciCiAgICAgICBpZD0idGV4dDItOC03LTQiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNC00IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMyNzliMTQ7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuODE4MTgyIgogICAgICAgICB4PSIzOC4yOTE5NTQiCiAgICAgICAgIHk9IjExNS41MTQzNyI+QTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDBlMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC42MDc4NDMiCiAgICAgICB4PSI5Mi42MzYzMjIiCiAgICAgICB5PSIxMTUuMjc0MzgiCiAgICAgICBpZD0idGV4dDItMi04LTkiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMy04IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgICB4PSI5Mi42MzYzMjIiCiAgICAgICAgIHk9IjExNS4yNzQzOCI+cXAxPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgIHg9Ijc3LjA3NTgxMyIKICAgICAgIHk9IjEwNy41NDk5OSIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNC02Ij48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOS00IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgICB4PSI3Ny4wNzU4MTMiCiAgICAgICAgIHk9IjEwNy41NDk5OSI+cTE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNDIuNzUwMzgxIgogICAgICAgeT0iMTA3LjU0Njg5IgogICAgICAgaWQ9InRleHQyLTItNy00LTYtNDUiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05LTQtNSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgICAgeD0iNDIuNzUwMzgxIgogICAgICAgICB5PSIxMDcuNTQ2ODkiPnFBQjwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZjtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDBlMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC42MDc4NDMiCiAgICAgICB4PSI1NC4wNDIwNjUiCiAgICAgICB5PSIxMDcuNTU5ODEiCiAgICAgICBpZD0idGV4dDItMi03LTQtNi00NS0zIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOS00LTUtMyIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgICAgeD0iNTQuMDQyMDY1IgogICAgICAgICB5PSIxMDcuNTU5ODEiPnFCQzwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIHg9IjEwNC43MDQ4NiIKICAgICAgIHk9IjExNS4yNzQzOCIKICAgICAgIGlkPSJ0ZXh0Mi0yLTItMy0wIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtMjgtMiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSIxMDQuNzA0ODYiCiAgICAgICAgIHk9IjExNS4yNzQzOCI+cXAyPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg4LTIiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGY7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDYxLjQ4NjY1MywxMDguNjA0ODggSCA5NC4yODk2ODYiCiAgICAgICAgIGlkPSJwYXRoNTAiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDBlMDtmaWxsLW9wYWNpdHk6MC42MDc4NDM7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDYxLjQ4NjMyOCwxMDguNDkyMTkgdiAwLjIyNDYxIGggMzIuODAyNzM0IHYgLTAuMjI0NjEgeiIKICAgICAgICAgaWQ9InBhdGg1MSIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc0OSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZTA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gOTMuMTI2OTUzLDEwNy43OTEwMiAtMC4xNDI1NzgsMC4yODMyIDEuMDYyNSwwLjUzMTI1IC0xLjA2MjUsMC41MzEyNSAwLjE0MjU3OCwwLjI4MzIgMS42Mjg5MDYsLTAuODE0NDUgeiIKICAgICAgICAgICBpZD0icGF0aDQ5IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iODYuNzI4OTM1IgogICAgICAgeT0iMTAyLjk4MjQ0IgogICAgICAgaWQ9InRleHQyLTItNy00LTYtNCI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTktNC00IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgIHg9Ijg2LjcyODkzNSIKICAgICAgICAgeT0iMTAyLjk4MjQ0Ij5xMjwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0yLTUiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDY4LjkwODE3MywxMDQuMDM3MjcgSCAxMDYuMzQ1OTgiCiAgICAgICAgIGlkPSJwYXRoNTMiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNjguOTA4MjAzLDEwMy45MjE4OCB2IDAuMjMwNDYgSCAxMDYuMzQ1NyB2IC0wLjIzMDQ2IHoiCiAgICAgICAgIGlkPSJwYXRoNTQiIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnNTIiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDEwNS4xNDg0NCwxMDMuMTk5MjIgLTAuMTQ2NDksMC4yOTEwMSAxLjA5Mzc1LDAuNTQ2ODggLTEuMDkzNzUsMC41NDY4NyAwLjE0NjQ5LDAuMjkyOTcgMS42Nzc3MywtMC44Mzk4NCB6IgogICAgICAgICAgIGlkPSJwYXRoNTIiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNjAuODAxNjk3IgogICAgICAgeT0iMTE1LjUxNDM3IgogICAgICAgaWQ9InRleHQyLTgtNS04Ij48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi02LTctNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgICAgeD0iNjAuODAxNjk3IgogICAgICAgICB5PSIxMTUuNTE0MzciPkM8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICB4PSI2OC4wMjUwMDkiCiAgICAgICB5PSIxMTUuNDg0MjMiCiAgICAgICBpZD0idGV4dDItOC01LTgtMyI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItNi03LTQtMCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI2OC4wMjUwMDkiCiAgICAgICAgIHk9IjExNS40ODQyMyI+RDwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0yLTMiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGY7c3Ryb2tlLWRhc2hhcnJheTowLjQ0ODY0MiwgMC4yMjQzMjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDM5LjMxNzA3MywxMDguNjA0ODggSCA1MC41MjM0ODYiCiAgICAgICAgIGlkPSJwYXRoNDQiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDBlMDtmaWxsLW9wYWNpdHk6MC42MDc4NDM7c3Ryb2tlLWRhc2hhcnJheTowLjQ0ODY0MiwgMC4yMjQzMjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM5LjMxNjQwNiwxMDguNDkyMTkgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjksMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE4IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjUgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOCB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBIIDQ5LjE4NzUgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDM5NDUzIHYgLTAuMjI0NjEgeiIKICAgICAgICAgaWQ9InBhdGg0NSIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc0MyI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZTA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gNDkuMzYxMzI4LDEwNy43OTEwMiAtMC4xNDI1NzgsMC4yODMyIDEuMDYyNSwwLjUzMTI1IC0xLjA2MjUsMC41MzEyNSAwLjE0MjU3OCwwLjI4MzIgMS42Mjg5MDYsLTAuODE0NDUgeiIKICAgICAgICAgICBpZD0icGF0aDQzIiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iNTEuODYxNSIKICAgICAgIHk9IjEwMi45NzkzNCIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNC02LTQ1LTgiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05LTQtNS0zMiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI1MS44NjE1IgogICAgICAgICB5PSIxMDIuOTc5MzQiPnFBRDwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0yLTMtMSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDtzdHJva2UtZGFzaGFycmF5OjAuNDQ4NjQyLCAwLjIyNDMyMTstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gMzkuMjE3MDc3LDEwNC4wMzcyNyBIIDY4LjM4MTY1OCIKICAgICAgICAgaWQ9InBhdGg0MSIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwO3N0cm9rZS1kYXNoYXJyYXk6MC40NDg2NDIsIDAuMjI0MzIxOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSAzOS4yMTY3OTcsMTAzLjkyNTc4IHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjYgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI5LDAgdiAwLjIyNDYxIGggMC40NDcyNjUgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOCB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE4IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTggdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjYgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgSCA1My4xMjUgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjksMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE4IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjUgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOCB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ3MjY1IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjYgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ3MjY2IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjksMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOCB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE4IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTggdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuMjI2NTYyIHYgLTAuMjI0NjEgeiIKICAgICAgICAgaWQ9InBhdGg0MiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc0MCI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gNjcuMjE4NzUsMTAzLjIyMjY2IC0wLjE0MjU3OCwwLjI4MzIgMS4wNjI1LDAuNTMxMjUgLTEuMDYyNSwwLjUzMTI1IDAuMTQyNTc4LDAuMjgzMiAxLjYyODkwNiwtMC44MTQ0NSB6IgogICAgICAgICAgIGlkPSJwYXRoNDAiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDgtMi0zLTgiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGY7c3Ryb2tlLWRhc2hhcnJheTowLjQ0ODY0MiwgMC4yMjQzMjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDUxLjMwMTc3MywxMDguNjA0ODggaCA5LjgxNjIzOSIKICAgICAgICAgaWQ9InBhdGg0NyIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGUwO2ZpbGwtb3BhY2l0eTowLjYwNzg0MztzdHJva2UtZGFzaGFycmF5OjAuNDQ4NjQyLCAwLjIyNDMyMTstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNTEuMzAyNzM0LDEwOC40OTIxOSB2IDAuMjI0NjEgSCA1MS43NSB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjYgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOSwwIHYgMC4yMjQ2MSBoIDAuNDQ3MjY1IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC40NDkyMTggdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOCB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE4IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDkyMTkgdiAtMC4yMjQ2MSB6IG0gMC42NzM4MjgsMCB2IDAuMjI0NjEgaCAwLjQ0NzI2NiB2IC0wLjIyNDYxIHogbSAwLjY3MTg3NSwwIHYgMC4yMjQ2MSBoIDAuNDQ5MjE5IHYgLTAuMjI0NjEgeiBtIDAuNjczODI4LDAgdiAwLjIyNDYxIGggMC40NDcyNjYgdiAtMC4yMjQ2MSB6IG0gMC42NzE4NzUsMCB2IDAuMjI0NjEgaCAwLjQ0OTIxOSB2IC0wLjIyNDYxIHogbSAwLjY3MzgyOCwwIHYgMC4yMjQ2MSBoIDAuNDQ3MjY2IHYgLTAuMjI0NjEgeiBtIDAuNjcxODc1LDAgdiAwLjIyNDYxIGggMC4zOTQ1MzEgdiAtMC4yMjQ2MSB6IgogICAgICAgICBpZD0icGF0aDQ4IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzQ2Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDBlMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA1OS45NTUwNzgsMTA3Ljc5MTAyIC0wLjE0MjU3OCwwLjI4MzIgMS4wNjQ0NTMsMC41MzEyNSAtMS4wNjQ0NTMsMC41MzEyNSAwLjE0MjU3OCwwLjI4MzIgMS42Mjg5MDYsLTAuODE0NDUgeiIKICAgICAgICAgICBpZD0icGF0aDQ2IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjgyMjIycHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowIgogICAgICAgeD0iMTIwLjA0OTQ4IgogICAgICAgeT0iMTE1LjU1NjUzIgogICAgICAgaWQ9InRleHQxLTkiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xLTIiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi44MjIyMnB4O3N0cm9rZS13aWR0aDowIgogICAgICAgICB4PSIxMjAuMDQ5NDgiCiAgICAgICAgIHk9IjExNS41NTY1MyI+UTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1taXRlcmxpbWl0OjQ7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTg7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eTowIgogICAgICAgeD0iNjAuNzI1Njc0IgogICAgICAgeT0iMTIzLjA5ODA1IgogICAgICAgaWQ9InRleHQ1LTctMyI+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSI2MC43MjU2NzQiCiAgICAgICAgIHk9IjEyMy4wOTgwNSIKICAgICAgICAgaWQ9InRzcGFuNy0yIj5yZWxhdGl2ZTwvdHNwYW4+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSI2MC43MjU2NzQiCiAgICAgICAgIHk9IjEyNS43NDM4OSIKICAgICAgICAgaWQ9InRzcGFuOCI+cG9pbnQgb3JpZ2luczwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOS0wLTYtMCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNTIuNDc0NjA5LDExNi4yODMyIC0wLjEyMTA5MywwLjE1NjI1IDUuNDY4NzUsNC4yNDQxNCAwLjEyMTA5MywtMC4xNTgyIHoiCiAgICAgICAgIGlkPSJwYXRoNjQiIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnNjMiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDUyLjA4OTg0NCwxMTYuMTA3NDIgMC42OTUzMTIsMS40NTExNyAwLjI1MTk1MywtMC4xMjEwOSAtMC40NTMxMjUsLTAuOTQ1MzEgMS4wMjczNDQsMC4yMDUwOCAwLjA1NDY5LC0wLjI3NTM5IHoiCiAgICAgICAgICAgaWQ9InBhdGg2MyIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJwYXRoOS0wLTYtMiI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNjEuMzgwODU5LDExNi40MDIzNCAtMS4wODAwNzgsNC4yNDQxNCAwLjE5MTQwNiwwLjA0ODggMS4wODAwNzksLTQuMjQ0MTQgeiIKICAgICAgICAgaWQ9InBhdGg2NiIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc2NSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gNjEuNTc4MTI1LDExNi4wMjczNCAtMS4wNTA3ODEsMS4yMTY4IDAuMjEwOTM3LDAuMTgzNTkgMC42ODU1NDcsLTAuNzk0OTIgMC4yMjI2NTYsMS4wMjUzOSAwLjI3MzQzOCwtMC4wNTg2IHoiCiAgICAgICAgICAgaWQ9InBhdGg2NSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJwYXRoOS0wLTYtOCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNjcuNDI5Njg3LDExNi40ODYzMyAtNC40NTUwNzgsNC4xMTEzMyAwLjEzNDc2NiwwLjE0NjQ4IDQuNDUzMTI1LC00LjExMTMzIHoiCiAgICAgICAgIGlkPSJwYXRoNjgiIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnNjciPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDY3Ljc5ODgyOCwxMTYuMjc5MyAtMS41NDQ5MjIsMC40NDcyNiAwLjA3ODEzLDAuMjY5NTMgMS4wMDc4MTMsLTAuMjkxMDEgLTAuMzcxMDk0LDAuOTgwNDcgMC4yNjE3MTksMC4wOTc2IHoiCiAgICAgICAgICAgaWQ9InBhdGg2NyIgLz4KICAgICAgPC9nPgogICAgPC9nPgogIDwvZz4KPC9zdmc+Cg==)

```cpp
inline constexpr struct A : absolute_point_origin<isq::distance> {} A;
inline constexpr struct B : relative_point_origin<A + 10 * m> {} B;
inline constexpr struct C : relative_point_origin<B + 10 * m> {} C;
inline constexpr struct D : relative_point_origin<A + 30 * m> {} D;

quantity_point qp1 = C + 100 * m;
quantity_point qp2 = D + 120 * m;

assert(qp2 - qp1 == 30 * m);           // Compatible: both relative to A
assert(qp1.quantity_from(C) == 100 * m);
assert(qp1.quantity_from(A) == 120 * m);
assert(B - A == 10 * m);               // Can subtract relative from absolute
assert(C - B == 10 * m);               // Can subtract relative origins
// assert(A - A == 0 * m);             // Compile-time error
```

**Design feature**: Unlike absolute origins, relative origins can be subtracted from each other or from their absolute base.

##### 11.3.3.4 Converting between different representations of the same *point*

The same point can be represented with displacement vectors from various origins:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuMzI2OTQybW0iCiAgIGhlaWdodD0iMjEuNDY2MTQ4bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni4zMjY5NDIgMjEuNDY2MTQ4IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdy00LTYtNSIKICAgICAgIHJlZlg9IjAiCiAgICAgICByZWZZPSIwIgogICAgICAgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiCiAgICAgICBtYXJrZXJXaWR0aD0iMSIKICAgICAgIG1hcmtlckhlaWdodD0iMSIKICAgICAgIHZpZXdCb3g9IjAgMCAxIDEiCiAgICAgICBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOmNvbnRleHQtc3Ryb2tlO2ZpbGwtcnVsZTpldmVub2RkO3N0cm9rZTpub25lIgogICAgICAgICBkPSJNIDAsMCA1LC01IC0xMi41LDAgNSw1IFoiCiAgICAgICAgIHRyYW5zZm9ybT0ic2NhbGUoLTAuNSkiCiAgICAgICAgIGlkPSJwYXRoNi0wLTItNiIgLz4KICAgIDwvbWFya2VyPgogIDwvZGVmcz4KICA8ZwogICAgIGlkPSJsYXllcjEiCiAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTI1LjUzMjI5MiwtMTMxLjU3MDI2KSI+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC41O3N0cm9rZS1kYXNoYXJyYXk6bm9uZTttYXJrZXItZW5kOnVybCgjRGFydEFycm93LTQtNi01KSIKICAgICAgIGQ9Ik0gMjUuNTMyMjkyLDE0OS4xMTE5NiBIIDExOC41Mjk3MyIKICAgICAgIGlkPSJwYXRoNC01LTAiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAzOC44MTY4NDMsMTQ4LjA3MTg5IHYgMi4wODAxMyIKICAgICAgIGlkPSJwYXRoNy02OC0yIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk3ODIzO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTEyOSwgMC4yOTc4MjM7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSAzOC44MTY4NDMsMTMyLjc5NzcyIHYgMTUuMDY0MDIiCiAgICAgICBpZD0icGF0aDItMi03LTQtMSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5NzgyMztzdHJva2UtZGFzaGFycmF5OjEuMTkxMjksIDAuMjk3ODIzO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Im0gMTA2LjU0NDUsMTMyLjg1MTA0IHYgMTUuMDEwNyIKICAgICAgIGlkPSJwYXRoMi0yLTEtNS02LTQiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTgwMDE7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTgwMDE7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSA1MC42Nzk0NTIsMTM3LjA0NTM0IHYgMTAuODE2MzkiCiAgICAgICBpZD0icGF0aDItMi00LTQtOS04LTYiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0iTSA1MC42Nzk0NTEsMTQ4LjA3MTg4IFYgMTUwLjE1MiIKICAgICAgIGlkPSJwYXRoMi01LTQtNy01LTMiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTgwMDE7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTgwMDE7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSA2MS4xODAzMzIsMTQxLjA2NzcgdiA2Ljg4NDQ2IgogICAgICAgaWQ9InBhdGgyLTItNC00LTktOC0zLTQiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAxMDYuNTQ0NSwxNDguMDcxODkgdiAyLjA4MDEzIgogICAgICAgaWQ9InBhdGgyLTUtNy01LTItNSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5NzgyMztzdHJva2UtZGFzaGFycmF5OjEuMTkxMjksIDAuMjk3ODIzO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Im0gNjguNTk2MTY0LDE0NS4wMzMyMiB2IDIuODI4NTIiCiAgICAgICBpZD0icGF0aDItMi0xLTUtNi02LTMiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0iTSA2OC41OTYxNjQsMTQ4LjA3MTg3IFYgMTUwLjE1MiIKICAgICAgIGlkPSJwYXRoMi01LTctNS0yLTEtNyIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNDkuNzc0MjEyIgogICAgICAgeT0iMTUyLjc4OTI2IgogICAgICAgaWQ9InRleHQyLTgtNS0xIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi02LTctMiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgICAgeD0iNDkuNzc0MjEyIgogICAgICAgICB5PSIxNTIuNzg5MjYiPkI8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMyNzliMTQ7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuODE4MTgyIgogICAgICAgeD0iMzcuOTQzNzAzIgogICAgICAgeT0iMTUyLjc4OTI2IgogICAgICAgaWQ9InRleHQyLTgtNy00LTciPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNC00LTYiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzI3OWIxNDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC44MTgxODIiCiAgICAgICAgIHg9IjM3Ljk0MzcwMyIKICAgICAgICAgeT0iMTUyLjc4OTI2Ij5BPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjQ2OTQ0cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iMTA0LjM1NjYxIgogICAgICAgeT0iMTUyLjU0OTI3IgogICAgICAgaWQ9InRleHQyLTItMi0zLTAtMSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS02LTI4LTItNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSIxMDQuMzU2NjEiCiAgICAgICAgIHk9IjE1Mi41NDkyNyI+cXAyPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iODUuODczNjE5IgogICAgICAgeT0iMTQ0LjgzMjY2IgogICAgICAgaWQ9InRleHQyLTItNy00LTYtNC0wIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOS00LTQtMCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI4NS44NzM2MTkiCiAgICAgICAgIHk9IjE0NC44MzI2NiI+cUQ8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSA2OC41NTk5MiwxNDUuODg3NTcgaCAzNy40Mzc4MSIKICAgICAgIGlkPSJwYXRoNTMtNiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSA2OC41NTk5NSwxNDUuNzcyMTggdiAwLjIzMDQ2IGggMzcuNDM3NSB2IC0wLjIzMDQ2IHoiCiAgICAgICBpZD0icGF0aDU0LTAiIC8+CiAgICA8ZwogICAgICAgaWQ9Imc1Mi00IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuMzQ4MjUyNjksNDEuODUwMjk2KSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMTA1LjE0ODQ0LDEwMy4xOTkyMiAtMC4xNDY0OSwwLjI5MTAxIDEuMDkzNzUsMC41NDY4OCAtMS4wOTM3NSwwLjU0Njg3IDAuMTQ2NDksMC4yOTI5NyAxLjY3NzczLC0wLjgzOTg0IHoiCiAgICAgICAgIGlkPSJwYXRoNTItOSIgLz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNjAuNDUzNDQ1IgogICAgICAgeT0iMTUyLjc4OTI2IgogICAgICAgaWQ9InRleHQyLTgtNS04LTYiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNy00LTAyIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgICB4PSI2MC40NTM0NDUiCiAgICAgICAgIHk9IjE1Mi43ODkyNiI+QzwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIHg9IjY3LjY3Njc1OCIKICAgICAgIHk9IjE1Mi43NTkxMSIKICAgICAgIGlkPSJ0ZXh0Mi04LTUtOC0zLTIiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNy00LTAtOSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI2Ny42NzY3NTgiCiAgICAgICAgIHk9IjE1Mi43NTkxMSI+RDwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi44MjIyMnB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MCIKICAgICAgIHg9IjExOS43MDEyMyIKICAgICAgIHk9IjE1Mi44MzE0MiIKICAgICAgIGlkPSJ0ZXh0MS05LTIiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xLTItOSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjgyMjIycHg7c3Ryb2tlLXdpZHRoOjAiCiAgICAgICAgIHg9IjExOS43MDEyMyIKICAgICAgICAgeT0iMTUyLjgzMTQyIj5RPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iODIuMTM4MTYxIgogICAgICAgeT0iMTQwLjgyNDQ5IgogICAgICAgaWQ9InRleHQyLTItNy00LTYtNC0wLTciPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05LTQtNC0wLTQiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgICAgeD0iODIuMTM4MTYxIgogICAgICAgICB5PSIxNDAuODI0NDkiPnFDPC90c3Bhbj48L3RleHQ+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgIGQ9Ik0gNjguNTI3MDgyLDE0MS44NzkzOSBIIDEwNS45NjQ4OSIKICAgICAgIGlkPSJwYXRoNTMtNi04IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MTstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICBkPSJtIDYxLjExODc4LDE0MS43NjQgdiAwLjIzMDQ2IGggNDQuODQ1ODMgViAxNDEuNzY0IFoiCiAgICAgICBpZD0icGF0aDU0LTAtNCIgLz4KICAgIDxnCiAgICAgICBpZD0iZzUyLTQtMSIKICAgICAgIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0wLjM4MTA5MDU2LDM3Ljg0MjEyKSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMTA1LjE0ODQ0LDEwMy4xOTkyMiAtMC4xNDY0OSwwLjI5MTAxIDEuMDkzNzUsMC41NDY4OCAtMS4wOTM3NSwwLjU0Njg3IDAuMTQ2NDksMC4yOTI5NyAxLjY3NzczLC0wLjgzOTg0IHoiCiAgICAgICAgIGlkPSJwYXRoNTItOS00IiAvPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIHg9Ijc2LjkxMDU3NiIKICAgICAgIHk9IjEzNi45ODgwMiIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNC02LTQtMC03LTEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05LTQtNC0wLTQtNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI3Ni45MTA1NzYiCiAgICAgICAgIHk9IjEzNi45ODgwMiI+cUI8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0iTSA2OC41OTMyMjgsMTM4LjA0MjkyIEggMTA2LjAzMTA0IgogICAgICAgaWQ9InBhdGg1My02LTgtOSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSA1MC42MDE1OSwxMzcuOTI3NTMgdiAwLjIzMDQ2IGggNTUuNDI5MTcgdiAtMC4yMzA0NiB6IgogICAgICAgaWQ9InBhdGg1NC0wLTQtMiIgLz4KICAgIDxnCiAgICAgICBpZD0iZzUyLTQtMS02IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuMzE0OTQ0NzMsMzQuMDA1NjQ3KSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2Q0MDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMTA1LjE0ODQ0LDEwMy4xOTkyMiAtMC4xNDY0OSwwLjI5MTAxIDEuMDkzNzUsMC41NDY4OCAtMS4wOTM3NSwwLjU0Njg3IDAuMTQ2NDksMC4yOTI5NyAxLjY3NzczLC0wLjgzOTg0IHoiCiAgICAgICAgIGlkPSJwYXRoNTItOS00LTciIC8+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgeD0iNzAuOTA5MzkzIgogICAgICAgeT0iMTMzLjA4NTQyIgogICAgICAgaWQ9InRleHQyLTItNy00LTYtNC0wLTctMTYiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTktMC05LTQtNC0wLTQtNiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojZDQwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eToxIgogICAgICAgICB4PSI3MC45MDkzOTMiCiAgICAgICAgIHk9IjEzMy4wODU0MiI+cUE8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0iTSA2OC42NTkzNzQsMTM0LjAwODAyIEggMTA2LjA5NzE4IgogICAgICAgaWQ9InBhdGg1My02LTgtMSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSAzOC42MjkxOTksMTM0LjAyNDkzIHYgMC4yMzA0NiBoIDY3LjQ2NzcxMSB2IC0wLjIzMDQ2IHoiCiAgICAgICBpZD0icGF0aDU0LTAtNC0wIiAvPgogICAgPGcKICAgICAgIGlkPSJnNTItNC0xLTkiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC4yNDg3OTg2OCwyOS45NzA3NTEpIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSAxMDUuMTQ4NDQsMTAzLjE5OTIyIC0wLjE0NjQ5LDAuMjkxMDEgMS4wOTM3NSwwLjU0Njg4IC0xLjA5Mzc1LDAuNTQ2ODcgMC4xNDY0OSwwLjI5Mjk3IDEuNjc3NzMsLTAuODM5ODQgeiIKICAgICAgICAgaWQ9InBhdGg1Mi05LTQtNCIgLz4KICAgIDwvZz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJNIDYxLjE4MDMzNSwxNDguMDcxODcgViAxNTAuMTUyIgogICAgICAgaWQ9InBhdGgyLTUtNy01LTItMS03LTMiIC8+CiAgPC9nPgo8L3N2Zz4K)

```cpp
quantity_point<si::metre, C> qp2C = qp2;          // converting constructor
quantity_point qp2B = qp2.point_for(B);           // conversion interface

assert(qp2 == qp2C);  // Same point, different representation
assert(qp2 == qp2B);
```

**Design constraint**: Conversions are only allowed between origins sharing the same `absolute_point_origin` base. There is no way to express relationships between distinct absolute origins—custom conversion functions are required for such cases.

##### 11.3.3.5 Temperature support

*Temperature* is a canonical example of relative point origins with stacked hierarchies:

```cpp
namespace si {

inline constexpr struct absolute_zero : absolute_point_origin<isq::thermodynamic_temperature> {} absolute_zero;
inline constexpr struct ice_point : relative_point_origin<point<milli<kelvin>>(273'150)> {} ice_point;

}

namespace usc {

inline constexpr struct zeroth_degree_Fahrenheit :
  relative_point_origin<point<mag_ratio<5, 9> * si::degree_Celsius>(-32)> {} zeroth_degree_Fahrenheit;

}
```

**Design feature**: Origins stack hierarchically (°F → °C → K), and units embed their natural origins:

```cpp
namespace si {

inline constexpr struct kelvin : named_unit<"K", kind_of<isq::thermodynamic_temperature>, zeroth_kelvin> {} kelvin;
inline constexpr struct degree_Celsius : named_unit<{u8"℃", "`C"}, kelvin, zeroth_degree_Celsius> {} degree_Celsius;

}
```

Construction syntax flexibility (all produce the same type):

```cpp
quantity_point<si::degree_Celsius, si::zeroth_degree_Celsius> q1 = si::zeroth_degree_Celsius + delta<deg_C>(20.5);
quantity_point q2{delta<deg_C>(20.5)};
quantity_point q3 = point<deg_C>(20.5);
```

Custom temperature references enable domain-specific applications:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuMTIyNDM3bW0iCiAgIGhlaWdodD0iMzUuNDQ2NDhtbSIKICAgdmlld0JveD0iMCAwIDk2LjEyMjQzNyAzNS40NDY0OCIKICAgdmVyc2lvbj0iMS4xIgogICBpZD0ic3ZnMSIKICAgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIgogICB4bWxuczpzdmc9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZGVmcwogICAgIGlkPSJkZWZzMSI+CiAgICA8bWFya2VyCiAgICAgICBzdHlsZT0ib3ZlcmZsb3c6dmlzaWJsZSIKICAgICAgIGlkPSJEYXJ0QXJyb3ctNC02LTUtNSIKICAgICAgIHJlZlg9IjAiCiAgICAgICByZWZZPSIwIgogICAgICAgb3JpZW50PSJhdXRvLXN0YXJ0LXJldmVyc2UiCiAgICAgICBtYXJrZXJXaWR0aD0iMSIKICAgICAgIG1hcmtlckhlaWdodD0iMSIKICAgICAgIHZpZXdCb3g9IjAgMCAxIDEiCiAgICAgICBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJmaWxsOmNvbnRleHQtc3Ryb2tlO2ZpbGwtcnVsZTpldmVub2RkO3N0cm9rZTpub25lIgogICAgICAgICBkPSJNIDAsMCA1LC01IC0xMi41LDAgNSw1IFoiCiAgICAgICAgIHRyYW5zZm9ybT0ic2NhbGUoLTAuNSkiCiAgICAgICAgIGlkPSJwYXRoNi0wLTItNi0wIiAvPgogICAgPC9tYXJrZXI+CiAgPC9kZWZzPgogIDxnCiAgICAgaWQ9ImxheWVyMSIKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjUuMTQ2MDQxLC0xNzEuOTU0NikiPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuNTtzdHJva2UtZGFzaGFycmF5Om5vbmU7bWFya2VyLWVuZDp1cmwoI0RhcnRBcnJvdy00LTYtNS01KSIKICAgICAgIGQ9Im0gMjUuMTQ2MDQsMTkyLjM2NzU3IGggOTIuOTk3NDQiCiAgICAgICBpZD0icGF0aDQtNS0wLTYiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAzOC40MzA1OTEsMTkxLjMyNzUgdiAyLjA4MDEzIgogICAgICAgaWQ9InBhdGg3LTY4LTItMSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDUzLjQ2ODIwMSwxOTEuMzI3NDkgdiAyLjA4MDEyIgogICAgICAgaWQ9InBhdGgyLTUtNC03LTUtMy02IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gOTguOTAxNTk4LDE5MS4zMjc0OCB2IDIuMDgwMTMiCiAgICAgICBpZD0icGF0aDItNS03LTUtMi0xLTctNiIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNlZWIwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgeD0iNTEuOTk3MTQ3IgogICAgICAgeT0iMTk2LjEzODE1IgogICAgICAgaWQ9InRleHQyLTgtNS0xLTkiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNy0yLTkiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6I2VlYjAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDBlMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC42MDc4NDMiCiAgICAgICAgIHg9IjUxLjk5NzE0NyIKICAgICAgICAgeT0iMTk2LjEzODE1Ij5GMDwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2VlYjAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzI3OWIxNDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC44MTgxODIiCiAgICAgICB4PSIzNi44MjA4NzMiCiAgICAgICB5PSIxOTYuMTM4MTUiCiAgICAgICBpZD0idGV4dDItOC03LTQtNy0yIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi02LTQtNC02LTciCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6I2VlYjAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzI3OWIxNDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC44MTgxODIiCiAgICAgICAgIHg9IjM2LjgyMDg3MyIKICAgICAgICAgeT0iMTk2LjEzODE1Ij5LMDwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2Q0MDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6I2Q0MDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIHg9IjEwNi4wMzA5OCIKICAgICAgIHk9IjE5NS44ODk3NiIKICAgICAgIGlkPSJ0ZXh0Mi0yLTItMy0wLTEtMiI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS02LTI4LTItNC0yIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgIHg9IjEwNi4wMzA5OCIKICAgICAgICAgeT0iMTk1Ljg4OTc2Ij5oaWdoPC90c3Bhbj48L3RleHQ+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4zODEyOTg7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgZD0ibSAxMDguNjQxNDksMTkxLjMyNzUgdiAyLjA4MDEzIgogICAgICAgaWQ9InBhdGgyLTUtNy01LTItNS01IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gODkuMTYxNzA0LDE5MS4yOTM4NSB2IDIuMDgwMTMiCiAgICAgICBpZD0icGF0aDItNS03LTUtMi01LTUtMSIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwZGY7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuMDY2NjY2NyIKICAgICAgIHg9Ijg3LjAxNjAxNCIKICAgICAgIHk9IjE5Ni4xMzUxMyIKICAgICAgIGlkPSJ0ZXh0Mi0yLTItMy0wLTEtMi0zIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtMjgtMi00LTItMCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjA2NjY2NjciCiAgICAgICAgIHg9Ijg3LjAxNjAxNCIKICAgICAgICAgeT0iMTk2LjEzNTEzIj5sb3c8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjAuOTk5OTk4Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgIGQ9Im0gOTguOTc5MTMxLDE4NS43OTEyMyB2IDAuMjMwNDYgaCA5LjI4MDY1OSB2IC0wLjIzMDQ2IHoiCiAgICAgICBpZD0icGF0aDU0LTAtOCIgLz4KICAgIDxnCiAgICAgICBpZD0iZzUyLTQtMiIKICAgICAgIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuOTE0MDgyMiw4MS44Njg0MTUpIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZDQwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSAxMDUuMTQ4NDQsMTAzLjE5OTIyIC0wLjE0NjQ5LDAuMjkxMDEgMS4wOTM3NSwwLjU0Njg4IC0xLjA5Mzc1LDAuNTQ2ODcgMC4xNDY0OSwwLjI5Mjk3IDEuNjc3NzMsLTAuODM5ODQgeiIKICAgICAgICAgaWQ9InBhdGg1Mi05LTIiIC8+CiAgICA8L2c+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRmO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowLjk5OTk5ODstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICBkPSJtIDk4Ljc4MzExMywxODUuNzkxMjMgdiAwLjIzMDQ2IGggLTkuMjgwNjQ4IHYgLTAuMjMwNDYgeiIKICAgICAgIGlkPSJwYXRoNTQtMC04LTYiIC8+CiAgICA8ZwogICAgICAgaWQ9Imc1Mi00LTItNCIKICAgICAgIHRyYW5zZm9ybT0ibWF0cml4KC0xLDAsMCwxLDE5NS44NDgxNSw4MS44NjgzNzUpIgogICAgICAgc3R5bGU9ImZpbGw6IzAwMDBkZjtmaWxsLW9wYWNpdHk6MSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDBkZjtmaWxsLW9wYWNpdHk6MTstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMTA1LjE0ODQ0LDEwMy4xOTkyMiAtMC4xNDY0OSwwLjI5MTAxIDEuMDkzNzUsMC41NDY4OCAtMS4wOTM3NSwwLjU0Njg3IDAuMTQ2NDksMC4yOTI5NyAxLjY3NzczLC0wLjgzOTg0IHoiCiAgICAgICAgIGlkPSJwYXRoNTItOS0yLTAiIC8+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjQ2OTQ0cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZWViMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMGUwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2Utb3BhY2l0eTowLjYwNzg0MyIKICAgICAgIHg9IjU5LjIxODEyOCIKICAgICAgIHk9IjE5Ni4xNDk2MSIKICAgICAgIGlkPSJ0ZXh0Mi04LTUtOC02LTgiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNy00LTAyLTUiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O2ZpbGw6I2VlYjAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDBlMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC42MDc4NDMiCiAgICAgICAgIHg9IjU5LjIxODEyOCIKICAgICAgICAgeT0iMTk2LjE0OTYxIj5DMDwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6I2VlYjAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDBlMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmU7c3Ryb2tlLW9wYWNpdHk6MC42MDc4NDMiCiAgICAgICB4PSI5Ni4zOTkwMDIiCiAgICAgICB5PSIxOTYuMTQ5NiIKICAgICAgIGlkPSJ0ZXh0Mi04LTUtOC02LTgtNyI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItNi03LTQtMDItNS02IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiNlZWIwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwZTA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjAuNjA3ODQzIgogICAgICAgICB4PSI5Ni4zOTkwMDIiCiAgICAgICAgIHk9IjE5Ni4xNDk2Ij5SRUY8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwOWFkMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICB4PSI5Ny4yMDU2NzMiCiAgICAgICB5PSIxOTkuNjI0NjMiCiAgICAgICBpZD0idGV4dDItOC01LTgtMy0yLTAiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTYtNy00LTAtOS05IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiMwOWFkMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiNkNDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICAgIHg9Ijk3LjIwNTY3MyIKICAgICAgICAgeT0iMTk5LjYyNDYzIj5yZWY8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuODIyMjJweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAiCiAgICAgICB4PSIxMTkuMzE0OTkiCiAgICAgICB5PSIxOTYuMDg2NzYiCiAgICAgICBpZD0idGV4dDEtOS0yLTkiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xLTItOS02IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuODIyMjJweDtzdHJva2Utd2lkdGg6MCIKICAgICAgICAgeD0iMTE5LjMxNDk5IgogICAgICAgICB5PSIxOTYuMDg2NzYiPlQ8L3RzcGFuPjwvdGV4dD4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDYwLjc5NDA4MywxOTEuMzI3NDggdiAyLjA4MDEzIgogICAgICAgaWQ9InBhdGgyLTUtNy01LTItMS03LTMtMCIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODAwMTtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODAwMTtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJtIDYwLjc5NDA4MywxODEuMzM4NzIgdiA5LjY5MDc5IgogICAgICAgaWQ9InBhdGgyLTItNC00LTktOC0zLTQtMSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODAwMTtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODAwMTtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJtIDEwOC42NDE0OSwxODQuNzk5ODUgdiA2LjIyOTY1IgogICAgICAgaWQ9InBhdGgyLTItNC00LTktOC0zLTQtMS04IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4MDAyO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4MDAyO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gOTguOTAxNTk5LDE3My42MDA0NiBWIDE5MS4wMjk1IgogICAgICAgaWQ9InBhdGgyLTItNC00LTktOC0zLTQtMS04OSIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojYTRhNGE0O3N0cm9rZS13aWR0aDowLjI5ODAwMTtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODAwMTtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJtIDg5LjE2MTcwNCwxODQuNzA2MzEgdiA2LjMyMzE5IgogICAgICAgaWQ9InBhdGgyLTItNC00LTktOC0zLTQtMS04OS0wIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4MDAxO3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4MDAxO3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Im0gMzguNDMwNTkxLDE3My4yOTM5IHYgMTcuNzM1NjEiCiAgICAgICBpZD0icGF0aDItMi00LTQtOS04LTMtNC0xLTIiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTgwMDE7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTgwMDE7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eToxIgogICAgICAgZD0ibSA1My40NjgyMDEsMTc3LjQwOTg2IHYgMTMuNjE5NjUiCiAgICAgICBpZD0icGF0aDItMi00LTQtOS04LTMtNC0xLTIzIiAvPgogICAgPGcKICAgICAgIGlkPSJwYXRoMTAiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNmZmJmMDA7ZmlsbC1vcGFjaXR5OjAuMDE1Njg2MztzdHJva2UtZGFzaGFycmF5OjAuNDYsIDAuMjM7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDM4LjU0MDI2NCwxODkuMTQzMDIgSCA2MC4zNTQwNDMiCiAgICAgICAgIGlkPSJwYXRoODAiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2VlYjAwMDtzdHJva2UtZGFzaGFycmF5OjAuNDYsIDAuMjM7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4LjU0MTAxNiwxODkuMDI3MzQgdiAwLjIzMDQ3IEggMzkgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NSB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42OTE0MDcsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg1IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NTg5ODUgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTQsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA2LDAgdiAwLjIzMDQ3IGggMC40NTg5ODUgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTQsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42OTE0MDcsMCB2IDAuMjMwNDcgSCA1Ni4yNSB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg1IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQyMzgyOSB2IC0wLjIzMDQ3IHoiCiAgICAgICAgIGlkPSJwYXRoODEiIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnNzkiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZWViMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDU5LjE2MjEwOSwxODguMzA2NjQgLTAuMTQ2NDg0LDAuMjkxMDIgMS4wODk4NDQsMC41NDQ5MiAtMS4wODk4NDQsMC41NDQ5MiAwLjE0NjQ4NCwwLjI5MTAyIDEuNjY5OTIyLC0wLjgzNTk0IHoiCiAgICAgICAgICAgaWQ9InBhdGg3OSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcKICAgICAgIGlkPSJwYXRoMTAtMyI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2ZmYmYwMDtmaWxsLW9wYWNpdHk6MC4wMTU2ODYzO3N0cm9rZS1kYXNoYXJyYXk6MC40NiwgMC4yMzAwMDE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDYwLjkzMjEzMywxODkuMTQzMDMgaCAzNy43NzUyMiIKICAgICAgICAgaWQ9InBhdGg4MyIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZWViMDAwO3N0cm9rZS1kYXNoYXJyYXk6MC40NiwgMC4yMzAwMDE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDYwLjkzMTY0MSwxODkuMDI3MzQgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg1IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDU0LDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA2LDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA3LDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NSB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IEggNzMuODEyNSB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA2LDAgdiAwLjIzMDQ3IGggMC40NTg5ODUgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1NCwwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA2LDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NSB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1NCwwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDYsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM3IHYgLTAuMjMwNDcgeiBtIDAuNjkxNDA2LDAgdiAwLjIzMDQ3IGggMC40NTg5ODUgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBIIDkxLjA2MjUgdiAtMC4yMzA0NyB6IG0gMC42OTE0MDcsMCB2IDAuMjMwNDcgaCAwLjQ1ODk4NCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzcgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg1IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NjA5MzggdiAtMC4yMzA0NyB6IG0gMC42ODk0NTQsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzNyB2IC0wLjIzMDQ3IHogbSAwLjY5MTQwNiwwIHYgMC4yMzA0NyBoIDAuNDU4OTg0IHYgLTAuMjMwNDcgeiBtIDAuNjg5NDUzLDAgdiAwLjIzMDQ3IGggMC40NTg5ODQgdiAtMC4yMzA0NyB6IG0gMC42ODk0NTMsMCB2IDAuMjMwNDcgaCAwLjQ2MDkzOCB2IC0wLjIzMDQ3IHogbSAwLjY4OTQ1MywwIHYgMC4yMzA0NyBoIDAuNDYwOTM4IHYgLTAuMjMwNDcgeiIKICAgICAgICAgaWQ9InBhdGg4NCIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9Imc4MiI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNlZWIwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gOTcuNTE1NjI1LDE4OC4zMDY2NCAtMC4xNDY0ODQsMC4yOTEwMiAxLjA4OTg0MywwLjU0NDkyIC0xLjA4OTg0MywwLjU0NDkyIDAuMTQ2NDg0LDAuMjkxMDIgMS42Njk5MjIsLTAuODM1OTQgeiIKICAgICAgICAgICBpZD0icGF0aDgyIiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZwogICAgICAgaWQ9InBhdGgxMC03IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwwLjM3MDMzKSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2ZmYmYwMDtmaWxsLW9wYWNpdHk6MC4wMTU2ODYzO3N0cm9rZS1kYXNoYXJyYXk6MC40NiwgMC4yMzstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gNjAuNzE1Njk3LDE4NS41MzYzMSBIIDUzLjg3NTEwNCIKICAgICAgICAgaWQ9InBhdGg3NyIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZWViMDAwO3N0cm9rZS1kYXNoYXJyYXk6MC40NiwgMC4yMzstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNTQuMDQ0OTIyLDE4NS40MjE4NyB2IDAuMjI4NTIgaCAwLjQ2MDkzNyB2IC0wLjIyODUyIHogbSAwLjY5MTQwNiwwIHYgMC4yMjg1MiBoIDAuNDU4OTg0IHYgLTAuMjI4NTIgeiBtIDAuNjg5NDUzLDAgdiAwLjIyODUyIGggMC40NTg5ODUgdiAtMC4yMjg1MiB6IG0gMC42ODk0NTMsMCB2IDAuMjI4NTIgaCAwLjQ2MDkzOCB2IC0wLjIyODUyIHogbSAwLjY5MTQwNywwIHYgMC4yMjg1MiBoIDAuNDU4OTg0IHYgLTAuMjI4NTIgeiBtIDAuNjg5NDUzLDAgdiAwLjIyODUyIGggMC40NTg5ODQgdiAtMC4yMjg1MiB6IG0gMC42ODk0NTMsMCB2IDAuMjI4NTIgaCAwLjQ2MDkzNyB2IC0wLjIyODUyIHogbSAwLjY4OTQ1MywwIHYgMC4yMjg1MiBoIDAuNDYwOTM3IHYgLTAuMjI4NTIgeiBtIDAuNjkxNDA2LDAgdiAwLjIyODUyIGggMC40NTg5ODUgdiAtMC4yMjg1MiB6IG0gMC42ODk0NTMsMCB2IDAuMjI4NTIgaCAwLjQ1ODk4NSB2IC0wLjIyODUyIHoiCiAgICAgICAgIGlkPSJwYXRoNzgiIC8+CiAgICAgIDxnCiAgICAgICAgIGlkPSJnNzYiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojZWViMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDU1LjA2NjQwNiwxODQuNzAxMTcgLTEuNjY5OTIyLDAuODM1OTQgMS42Njk5MjIsMC44MzM5OCAwLjE0NjQ4NSwtMC4yOTEwMSAtMS4wODk4NDQsLTAuNTQ0OTIgMS4wODk4NDQsLTAuNTQyOTcgeiIKICAgICAgICAgICBpZD0icGF0aDc2IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7bWl4LWJsZW5kLW1vZGU6bm9ybWFsO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI2Ny40MDU5NzUiCiAgICAgICB5PSIxODEuMzkzMjgiCiAgICAgICBpZD0idGV4dDItMi03LTQ5LTUtMy0yLTYtOCI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTk2LTQtMS04LTgtNSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNjcuNDA1OTc1IgogICAgICAgICB5PSIxODEuMzkzMjgiPnJlZi5xdWFudGl0eV9mcm9tX3plcm8oKTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO21peC1ibGVuZC1tb2RlOm5vcm1hbDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNTguNjk4NTM2IgogICAgICAgeT0iMTc3LjI2Mzk2IgogICAgICAgaWQ9InRleHQyLTItNy00OS01LTMtMi02LTgtMCI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTk2LTQtMS04LTgtNS0xIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI1OC42OTg1MzYiCiAgICAgICAgIHk9IjE3Ny4yNjM5NiI+cmVmLmluKGRlZ19GKS5xdWFudGl0eV9mcm9tX3plcm8oKTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO21peC1ibGVuZC1tb2RlOm5vcm1hbDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iNTMuNTUzNTMyIgogICAgICAgeT0iMTczLjQ5NTU5IgogICAgICAgaWQ9InRleHQyLTItNy00OS01LTMtMi02LTgtMC0yIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNC0xLTgtOC01LTEtNiIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNTMuNTUzNTMyIgogICAgICAgICB5PSIxNzMuNDk1NTkiPnJlZi5pbihLKS5xdWFudGl0eV9mcm9tX3plcm8oKTwvdHNwYW4+PC90ZXh0PgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0iTSA5Ni43OTU3NzksMTgyLjQ1NDY4IEggMTA4LjQxMjE3IgogICAgICAgaWQ9InBhdGg1OS00IiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7c3Ryb2tlLXdpZHRoOjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSA2MC44NzU2NzUsMTgyLjIzNjU4IHYgMC4yNSBoIDM3LjQzNTM3NCB2IC0wLjI1IHoiCiAgICAgICBpZD0icGF0aDYwLTIiIC8+CiAgICA8ZwogICAgICAgaWQ9Imc1OC00IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTguMDEzMTE0LDgzLjI4OTIxMikiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDEwNS4wMjkzLDk4LjE2NDA2MiAtMC4xNTgyMSwwLjMxNjQwNyAxLjE4MzYsMC41OTE3OTcgLTEuMTgzNiwwLjU5MTc5NiAwLjE1ODIxLDAuMzE2NDA3IDEuODE0NDUsLTAuOTA4MjAzIHoiCiAgICAgICAgIGlkPSJwYXRoNTgtMyIgLz4KICAgIDwvZz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0O3N0cm9rZS13aWR0aDowLjk5OTk5ODstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICBkPSJtIDUzLjUyOTI1OSwxNzguMjMyOTkgdiAwLjI1IGggNDQuODI1MzkgdiAtMC4yNSB6IgogICAgICAgaWQ9InBhdGg2MC0yLTQiIC8+CiAgICA8ZwogICAgICAgaWQ9Imc1OC00LTEiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNy45Njk1MjYxLDc5LjI4NTYxNSkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDEwNS4wMjkzLDk4LjE2NDA2MiAtMC4xNTgyMSwwLjMxNjQwNyAxLjE4MzYsMC41OTE3OTcgLTEuMTgzNiwwLjU5MTc5NiAwLjE1ODIxLDAuMzE2NDA3IDEuODE0NDUsLTAuOTA4MjAzIHoiCiAgICAgICAgIGlkPSJwYXRoNTgtMy0yIiAvPgogICAgPC9nPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7c3Ryb2tlLXdpZHRoOjE7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgZD0ibSAzOC40NTQ4NTUsMTc0LjI0MDQxIHYgMC4yNSBoIDU5Ljk3OTU2MiB2IC0wLjI1IHoiCiAgICAgICBpZD0icGF0aDYwLTItNC00IiAvPgogICAgPGcKICAgICAgIGlkPSJnNTgtNC0xLTAiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNy44ODk3NDc3LDc1LjI5MzAyMikiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDEwNS4wMjkzLDk4LjE2NDA2MiAtMC4xNTgyMSwwLjMxNjQwNyAxLjE4MzYsMC41OTE3OTcgLTEuMTgzNiwwLjU5MTc5NiAwLjE1ODIxLDAuMzE2NDA3IDEuODE0NDUsLTAuOTA4MjAzIHoiCiAgICAgICAgIGlkPSJwYXRoNTgtMy0yLTEiIC8+CiAgICA8L2c+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC1hbmNob3I6bWlkZGxlO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MC4yOTg7c3Ryb2tlLW1pdGVybGltaXQ6NDtzdHJva2UtZGFzaGFycmF5OjEuMTkyLCAwLjI5ODtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjAiCiAgICAgICB4PSIxMDcuNjk2MTQiCiAgICAgICB5PSIxNzkuNTAyNjIiCiAgICAgICBpZD0idGV4dDUtNCI+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSIxMDcuNjk2MTQiCiAgICAgICAgIHk9IjE3OS41MDI2MiIKICAgICAgICAgaWQ9InRzcGFuNi01Ij5vcmlnaW4gZG9lc24ndDwvdHNwYW4+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSIxMDcuNjk2MTQiCiAgICAgICAgIHk9IjE4Mi4xNDg0NyIKICAgICAgICAgaWQ9InRzcGFuNzQiPmNoYW5nZTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1taXRlcmxpbWl0OjQ7c3Ryb2tlLWRhc2hhcnJheToxLjE5MiwgMC4yOTg7c3Ryb2tlLWRhc2hvZmZzZXQ6MDtzdHJva2Utb3BhY2l0eTowIgogICAgICAgeD0iMzguNDMwMDczIgogICAgICAgeT0iMjA0LjE2MDgiCiAgICAgICBpZD0idGV4dDUtNy00Ij48dHNwYW4KICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC1hbmNob3I6bWlkZGxlO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MC4yOTgiCiAgICAgICAgIHg9IjM4LjQzMDA3MyIKICAgICAgICAgeT0iMjA0LjE2MDgiCiAgICAgICAgIGlkPSJ0c3BhbjQtMCI+YWJzb2x1dGU8L3RzcGFuPjx0c3BhbgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDt0ZXh0LWFsaWduOmNlbnRlcjt0ZXh0LWFuY2hvcjptaWRkbGU7ZmlsbDojMDAwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowLjI5OCIKICAgICAgICAgeD0iMzguNDMwMDczIgogICAgICAgICB5PSIyMDYuODA2NjQiCiAgICAgICAgIGlkPSJ0c3BhbjctNSI+cG9pbnQgb3JpZ2luPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg5LTAtNi01IgogICAgICAgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTAuNjIzMTE5MjgsODEuMDYyOTQyKSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gMzguOTc0NjA5LDExNi42ODk0NSAtMC4wODc4OSw0LjQ0MTQxIDAuMTk5MjE4LDAuMDA0IDAuMDg1OTQsLTQuNDQxNDEgeiIKICAgICAgICAgaWQ9InBhdGg2Mi04IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzYxLTQiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDM5LjA4MjAzMSwxMTYuMjc5MyAtMC43NDgwNDcsMS40MjM4MyAwLjI0ODA0NywwLjEzMDg1IDAuNDg4MjgxLC0wLjkyNzczIDAuNDQ5MjE5LDAuOTQ1MzEgMC4yNTM5MDYsLTAuMTE5MTQgeiIKICAgICAgICAgICBpZD0icGF0aDYxLTkiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzt0ZXh0LWFsaWduOmNlbnRlcjt0ZXh0LWFuY2hvcjptaWRkbGU7ZmlsbDojMDAwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjI5ODtzdHJva2UtbWl0ZXJsaW1pdDo0O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MCIKICAgICAgIHg9Ijc5LjU0NzYyMyIKICAgICAgIHk9IjIwNC4xNjA4IgogICAgICAgaWQ9InRleHQ1LTctMy00Ij48dHNwYW4KICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7dGV4dC1hbGlnbjpjZW50ZXI7dGV4dC1hbmNob3I6bWlkZGxlO2ZpbGw6IzAwMDAwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2Utd2lkdGg6MC4yOTgiCiAgICAgICAgIHg9Ijc5LjU0NzYyMyIKICAgICAgICAgeT0iMjA0LjE2MDgiCiAgICAgICAgIGlkPSJ0c3BhbjctMi0zIj5yZWxhdGl2ZTwvdHNwYW4+PHRzcGFuCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi4xMTY2N3B4O3RleHQtYWxpZ246Y2VudGVyO3RleHQtYW5jaG9yOm1pZGRsZTtmaWxsOiMwMDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjAuMjk4IgogICAgICAgICB4PSI3OS41NDc2MjMiCiAgICAgICAgIHk9IjIwNi44MDY2NCIKICAgICAgICAgaWQ9InRzcGFuOC0wIj5wb2ludCBvcmlnaW5zPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg5LTAtNjItMyIKICAgICAgIHRyYW5zZm9ybT0ibWF0cml4KC0wLjg4MDQzMjI1LC0wLjM0MjY4MTEyLDAuMzQxNDk2ODEsLTAuODgzNDg1NTksNzQuMzkzMiwyOTIuOTQ5MTcpIgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDoxLjA1NzExIj4KICAgICAgPGcKICAgICAgICAgaWQ9InBhdGg3NC02Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0iTSA1NS41NDM0OTcsODcuNzgzMjY0IDM0Ljg2MzUyNCw4OC4xNzQ0MzUiCiAgICAgICAgICAgaWQ9InBhdGg4NiIgLz4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA1NS41NDEwMTYsODcuNjc3NzM0IC0yMC42Nzk2ODgsMC4zOTA2MjUgMC4wMDM5LDAuMjEwOTM4IDIwLjY3OTY4OCwtMC4zOTA2MjUgeiIKICAgICAgICAgICBpZD0icGF0aDg3IiAvPgogICAgICAgIDxnCiAgICAgICAgICAgaWQ9Imc4NSI+CiAgICAgICAgICA8cGF0aAogICAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICAgIGQ9Im0gNTQuNDMzNTk0LDg3LjAzNzEwOSAtMC4xMjg5MDcsMC4yNjk1MzIgMS4wMDk3NjYsMC40ODA0NjggLTAuOTkwMjM0LDAuNTE5NTMyIDAuMTM4NjcyLDAuMjY1NjI1IDEuNTIxNDg0LC0wLjc5Njg3NSB6IgogICAgICAgICAgICAgaWQ9InBhdGg4NSIgLz4KICAgICAgICA8L2c+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDc0LTYtNSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gNjMuMDg4MDA0LDE5Ni4wOTE4MiAxMi40NDc2MDksNi4wODYyNCIKICAgICAgICAgaWQ9InBhdGg4OSIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMDAwOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0ibSA2My4xMzI4MTIsMTk2LjAwMTk1IC0wLjA4Nzg5LDAuMTc5NjkgMTIuNDQ3MjY1LDYuMDg1OTQgMC4wODc4OSwtMC4xNzk2OSB6IgogICAgICAgICBpZD0icGF0aDkwIiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzg4Ij4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA2NC4zMzc4OTEsMTk1Ljg5NDUzIC0xLjYyMzA0NywwLjAxMzcgMC45ODYzMjgsMS4yOTEwMiAwLjIyNDYwOSwtMC4xNzE4OCAtMC42NDI1NzgsLTAuODM5ODQgMS4wNTg1OTQsLTAuMDEgeiIKICAgICAgICAgICBpZD0icGF0aDg4IiAvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZwogICAgICAgaWQ9InBhdGg3NC02LTkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDk1LjczNzI2MiwxOTYuMTgzMDkgLTExLjU5MzI4NSw3LjExNTIzIgogICAgICAgICBpZD0icGF0aDkyIiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDk1LjY4NTU0NywxOTYuMDk3NjYgLTExLjU5Mzc1LDcuMTE1MjMgMC4xMDM1MTUsMC4xNjk5MiAxMS41OTM3NSwtNy4xMTUyMyB6IgogICAgICAgICBpZD0icGF0aDkzIiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzkxIj4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSA5Ni4wOTE3OTcsMTk1Ljk2NDg0IC0xLjYxNzE4OCwwLjE0MDYzIDAuMDIzNDQsMC4yODMyIDEuMDU2NjQsLTAuMDkxOCAtMC41NjA1NDYsMC44OTg0NCAwLjI0MDIzNCwwLjE0ODQ0IHoiCiAgICAgICAgICAgaWQ9InBhdGg5MSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGNpcmNsZQogICAgICAgc3R5bGU9ImZpbGw6IzA5YWQwMDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6bm9uZTtzdHJva2Utd2lkdGg6MC4yO3N0cm9rZS1kYXNoYXJyYXk6bm9uZTtzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBpZD0icGF0aDc1IgogICAgICAgY3g9Ijk4LjkwOTI1NiIKICAgICAgIGN5PSIxODUuOTM5OCIKICAgICAgIHI9IjAuNDkzNDU4MTgiIC8+CiAgICA8ZwogICAgICAgaWQ9InBhdGg5LTAtNjIiCiAgICAgICB0cmFuc2Zvcm09Im1hdHJpeCgtMC44ODA0MzIyNiwtMC4zNDI2ODExMSwwLjM0MTQ5NjgxLC0wLjg4MzQ4NTU4LDExMi40MTkyNiwyNzAuNzAyMTkpIgogICAgICAgc3R5bGU9InN0cm9rZS13aWR0aDoxLjA1NzExIj4KICAgICAgPGcKICAgICAgICAgaWQ9InBhdGg3NCI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gNDUuMTE4MjE4LDc5LjEyMTIzOSAtMi4wNDQ4NzEsNC4zMzM1NDQiCiAgICAgICAgICAgaWQ9InBhdGg5NSIgLz4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6IzAwMDAwMDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0iTSA0NS4wMjM0MzcsNzkuMDc2MTcyIDQyLjk3ODUxNiw4My40MTAxNTYgNDMuMTY5OTIyLDgzLjUgNDUuMjEyODkxLDc5LjE2NjAxNiBaIgogICAgICAgICAgIGlkPSJwYXRoOTYiIC8+CiAgICAgICAgPGcKICAgICAgICAgICBpZD0iZzk0Ij4KICAgICAgICAgIDxwYXRoCiAgICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgICAgZD0ibSA0NS4zMDY2NDEsNzguNzIyNjU2IC0xLjM1MTU2MywxLjA2MjUgMC4xODU1NDcsMC4yMzQzNzUgMC44ODA4NTksLTAuNjkxNDA2IDAuMDI1MzksMS4xMTkxNDEgMC4yOTg4MjgsLTAuMDA3OCB6IgogICAgICAgICAgICAgaWQ9InBhdGg5NCIgLz4KICAgICAgICA8L2c+CiAgICAgIDwvZz4KICAgIDwvZz4KICA8L2c+Cjwvc3ZnPgo=)

```cpp
constexpr struct room_reference_temp : relative_point_origin<point<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

constexpr auto step_delta = delta<isq::Celsius_temperature[deg_C]>(0.5);
constexpr int number_of_steps = 6;

room_temp room_ref{};
room_temp room_low = room_ref - number_of_steps * step_delta;
room_temp room_high = room_ref + number_of_steps * step_delta;

auto std_ref = room_ref.point_for(si::ice_point);
std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             std_ref, std_ref.in(deg_F), std_ref.in(K));

std::println("| {:<18} | {:^18} | {:^18} | {:^18} |",
             "Temperature delta", "Room reference", "Ice point", "Absolute zero");
std::println("|{0:=^20}|{0:=^20}|{0:=^20}|{0:=^20}|", "");

auto print_temp = [&](std::string_view label, auto v) {
  std::println("| {:<18} | {:^18} | {:^18} | {:^18:N[.2f]} |", label,
               v - room_reference_temp, (v - si::ice_point).in(deg_C), (v - si::absolute_zero).in(deg_C));
};

print_temp("Lowest", room_low);
print_temp("Default", room_ref);
print_temp("Highest", room_high);
```

The above prints:

```
Room reference temperature: 21 ℃ (69.8 ℉, 294.15 K)

| Temperature delta  |   Room reference   |     Ice point      |   Absolute zero    |
|====================|====================|====================|====================|
| Lowest             |       -3 ℃        |       18 ℃        |     291.15 ℃      |
| Default            |        0 ℃        |       21 ℃        |     294.15 ℃      |
| Highest            |        3 ℃        |       24 ℃        |     297.15 ℃      |
```

More about temperatures can be found in the [Potential surprises while working with temperatures] chapter.

### 11.4 User-defined representation types

The library should work with any representation type for:

- Improved safety (overflow prevention, range restrictions).
- Additional information (measurement uncertainty).
- Linear algebra support.

By default, floating-point and integral types (except `bool`) are treated as real scalars.

## 12 Representation Types

Every `quantity` has a **representation type** that stores the numerical value. The library works seamlessly with fundamental arithmetic types (except `bool`) and `std::complex`, but custom representation types can also be used to model domain-specific requirements—such as range-validated values, vectors, or specialized numeric types.

The representation type determines what mathematical operations are available and how the quantity behaves in calculations. The library verifies at compile time that the representation type has the capabilities required for the quantity’s character.

### 12.1 Representation Requirements

To be used as a representation type, a type must satisfy the `RepresentationOf` concept. The library supports different types of representations corresponding to different quantity characters.

**Why verify representation capabilities?** The same unit can represent fundamentally different physical concepts requiring different mathematical operations. For example:

- *speed* (scalar, magnitude only) vs. *velocity* (vector, magnitude and direction) both use m/s,
- *mass* (scalar) uses kg while *weight force* (vector, pointing downward) uses N.

The library tracks **character in the quantity specification** (what the quantity represents) and verifies that the **representation type provides the required capabilities**. This dual approach provides **compile-time type safety** for the mathematical nature of physical quantities—preventing, for example, using a scalar type where vector operations like cross product are needed.

The following table summarizes the requirements for different representation characters:

| Requirement | Real Scalar | Complex Scalar | Vector | Tensor |
| --- | --- | --- | --- | --- |
| Copyable | ✅ | ✅ | ✅ | ✅ |
| Addition/subtraction (`+`, `-`, unary `-`) | ✅ | ✅ | ✅ | ✅ |
| `MagnitudeScalable` (unit-conversion) | ✅ | ✅ | ✅ | ✅ |
| Self-scalable (`T * T`, `T / T`) | ✅ | ✅ | - | - |
| Equality comparable (`==`) | ✅ | ✅ | ✅ | ✅ |
| Totally ordered (`<`, `>`, `<=`, `>=`) | ✅ | - | - | - |
| Not a quantity type itself | ✅ | ✅ | ✅ | ✅ |
| **Construction** | - | `T{real, imag}` | - | - |
| **Required CPOs** | - | `mp_units::real()`, `mp_units::imag()`, `mp_units::modulus()` | `mp_units::magnitude()` | `mp_units::magnitude()` |
| **Opt-out mechanism** | `disable_real<T>` | - | `disable_vector<T>` | - |
| **Examples** | `int`, `double`, `long double` | `std::complex<double>` | `Eigen::Vector3d`, `cartesian_vector<double>`, `int`, `double` | `Eigen::Matrix3d`, `int`, `double` (for scalar measures) |

All representation types must be **weakly regular**, which means they satisfy the `std::regular` concept except for the default-constructibility requirement. Specifically, they must be:

- **Copyable** (`std::copyable`)
- **Equality comparable** (`std::equality_comparable`)

This ensures that representation types have value semantics suitable for use in quantities. Default construction is not required, allowing types like range-validated representations that may not have a meaningful default value.

**Construction**

Complex scalars **must** be constructible from real and imaginary parts: `T{real_value, imag_value}`. This is essential for operations that combine real-valued quantities into complex results. For example, combining *active power* and *reactive power* into *complex power*:

```cpp
quantity active = isq::active_power(100.0 * W);
quantity reactive = isq::reactive_power(50.0 * W);
// Library needs to construct: std::complex<double>{active.numerical_value(),
//                                                  reactive.numerical_value()}
```

**Total Ordering**

Well-designed complex-like types do not provide total ordering (`operator<`, etc.) since there is no natural ordering for complex numbers. If a complex-like type does provide ordering operators (e.g., for use in containers), use the `disable_real` opt-out mechanism:

```cpp
template<>
constexpr bool mp_units::disable_real<my_complex_type> = true;
```

Alternatively, the library could explicitly check for the absence of `mp_units::real()` and `mp_units::imag()` to distinguish real from complex scalars — a design choice that may be refined based on standardization discussions.

The different names reflect domain conventions: `modulus()` is traditional complex analysis terminology, while `magnitude()` follows physics and engineering conventions for vectors. Naming the vector CPO `norm` was considered but rejected: `std::norm` already exists in `<complex>` with a different meaning — it returns |z|² (the squared modulus), not |z|. Introducing a standard CPO named `norm` that returns |v| would create a semantic collision within the same namespace. The library therefore uses `magnitude` as the primary name and additionally accepts `norm`-named member functions and free functions as fallbacks, so that types from linear algebra libraries integrate without adaptation.

Arithmetic types like `int` and `double` intentionally satisfy requirements for multiple characters — real scalar (primary use), 1-dimensional vector, and scalar tensor measures like von Mises stress. Type safety comes from `quantity_character` matching in the quantity specification, not from mutually exclusive representation concepts:

```cpp
// All valid uses of double:
quantity m = isq::mass(5.0 * kg);           // Scalar
quantity v = isq::velocity(10.0 * m/s);     // 1D vector
quantity sigma = isq::stress(100.0 * Pa);   // Scalar tensor measure
```

Most engineering extracts scalar measures from tensor fields rather than working with full 3×3 matrix representations — von Mises stress, principal stresses, shear components, hydrostatic stress — which is why arithmetic types cover the tensor character in practice.

### 12.2 Concept Hierarchy

Most of the concepts described below are *exposition-only*: they capture how the library classifies representation types internally and are not part of its public interface. The only public concept in this chapter is `RepresentationOf` — the building-block and character concepts (`Addable`, `ScalableWith`, `RealScalar`, `Vector`, and the rest) exist to define it and to explain how a representation type is recognized.

These concepts are **syntactic**: they constrain which operations are available and that results have a common type with `T` (`std::common_with`). They deliberately do **not** — and a C++ concept fundamentally cannot — enforce the algebraic *laws* (associativity, commutativity, distributivity, existence of identities, compatibility of an order with the arithmetic) that the corresponding mathematical structures require. This is the same limitation `std::regular` and `std::totally_ordered` already accept. For this reason the concepts are named for the *role* a type plays rather than for the structure it resembles; Relationship to algebraic structures below maps each one to the structure it approximates and lists the laws left unchecked.

The requirements summarized in the table above map directly to a hierarchy of C++ concepts. The lowest-level building blocks are:

```cpp
template<typename T>
concept WeaklyRegular = std::copyable<T> && std::equality_comparable<T>;

template<typename T>
concept Addable = requires(const T a, const T b) {
  { -a } -> std::common_with<T>;
  { a + b } -> std::common_with<T>;
  { a - b } -> std::common_with<T>;
};

template<typename T, typename S>
concept ScalableWith = requires(const T v, const S s) {
  { v * s / s } -> std::common_with<T>;
  { s * v / s } -> std::common_with<T>;
  { v / s * s } -> std::common_with<T>;
};
```

`WeaklyRegular` is `std::regular` without default-initialization. Default construction is intentionally not required: some representation types cannot provide a meaningful default-constructed value (see, e.g., [[P2993R0]](https://wg21.link/p2993r0)) yet are otherwise well-behaved as quantity representations. Requiring only copyability and equality comparison keeps such types in scope.

`Addable` requires unary negation (`-a`) alongside `+` and `-`, so it models an additive *group* rather than a mere monoid. Inverses are required because the library forms differences (between quantities, and between quantity points); types that support only accumulation are intentionally out of scope.

`ScalableWith<T, S>` deliberately constrains the *round-trip* `v * s / s` rather than the intermediate `v * s`. Leaving the intermediate unconstrained is intentional: it lets types whose `operator*`/`operator/` change the type — quantities being the canonical example — still satisfy the concept, as long as scaling by `s` and back lands on a type with a common type with `T`. The round-trip requirement simultaneously rejects irreversible silent type promotion, where `operator*` decays to a different type than `T` and never recovers it (e.g. a checked-integer wrapper whose `operator*` returns a raw arithmetic type). The constraint is on the result *type*, not its value: over integer representations `v * s / s` need not equal `v` (integer division truncates). `ScalableWith` certifies that the scalar action is **type-stable**, not that scaling is exactly invertible. Because the round-trip divides by `s`, the scalar type `S` must itself be division-capable (field-like); scaling by ring-only scalars that lack division is not expressible through this concept.

The result types of `+`, `-`, and the scaling round-trip are guarded with `std::common_with<T>` rather than left unconstrained or pinned to a stronger concept, and the choice is a deliberate compromise:

- A bare requirement (`{ a + b };`) is satisfied even by an `operator+` returning `void`, so some return check is needed.
- The natural ideal — requiring the result to be a scalar/vector *again* (true closure, `{ a + b } -> Scalar`) — is **ill-formed**, not merely expensive: those character concepts are defined transitively through `Addable`/`ScalableWith`, so constraining their own results by them would make a concept depend on itself, which 13.5.2.3 [[temp.constr.atomic]](https://wg21.link/temp.constr.atomic) forbids (and which would otherwise recurse without termination).
- Requiring `std::same_as<T>` is well-formed but too strong: it forbids the type-changing arithmetic the round-trip is designed to permit (expression templates, quantities).

`std::common_with<T>` is the non-recursive middle ground: it rejects `void` and unrelated return types while admitting any result that shares a common type with `T`. The standard’s cross-type comparison concepts (`std::equality_comparable_with`, `std::three_way_comparable_with`) constrain with the related `std::common_reference_with`, because they relate operands that may be lvalues or proxy references. Here the constrained expressions yield prvalues, so a common *value* type is the meaningful requirement — and `std::common_with` is the stronger relation anyway, entailing `common_reference_with` for the corresponding `const` lvalue references ([concept.common]).

These compose into the character-specific concepts:

```cpp
template<typename T>
concept RegularAddable = Addable<T> && WeaklyRegular<T>;

// Scalars: self-scalable — T * T and T / T stay in the same type
template<typename T>
concept BaseScalar = RegularAddable<T> && ScalableWith<T, T>;

// Real scalar: totally ordered, opt-out via disable_real<T>
template<typename T>
concept RealScalar = !disable_real<T> && BaseScalar<T> && std::totally_ordered<T>;

// Complex scalar: constructible from real/imag parts; provides real, imag, modulus
template<typename T>
concept ComplexScalar =
  BaseScalar<T> &&
  requires(const T v, const T& ref) {
    requires std::constructible_from<T,
      decltype(mp_units::real(ref)), decltype(mp_units::imag(ref))>;
    mp_units::real(v);
    mp_units::imag(v);
    mp_units::modulus(v);
    requires ScalableWith<T, decltype(mp_units::modulus(v))>;
  };

// Vector: scalable by its magnitude type (a scalar); magnitude need not equal T
template<typename T>
concept Vector =
  !disable_vector<T> &&
  RegularAddable<T> &&
  requires(const T v) {
    mp_units::magnitude(v);
    requires ScalableWith<T, decltype(mp_units::magnitude(v))>;
  };
```

The key structural difference between `BaseScalar` and `Vector` reflects the underlying mathematics. A scalar type must satisfy `ScalableWith<T, T>` — multiplying two scalars yields another scalar of the same kind. A vector type is only required to satisfy `ScalableWith<T, decltype(magnitude(v))>` — it can be scaled by its magnitude (a scalar), but vector × vector is not required and is typically not defined at all.

The concept is named `Vector` to match the `quantity_character::vector` it identifies, not to assert that it models an arbitrary vector space. In the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) sense a vector quantity is characterized by a magnitude and a direction, so the `magnitude(v)` requirement is intrinsic to that character rather than an extra restriction: the representation of a vector quantity is, precisely, an element of a normed space.

`ComplexScalar` takes `modulus(v)` to be the Euclidean modulus \(|z| = \sqrt{\operatorname{re}(z)^2 + \operatorname{im}(z)^2}\) — the same quantity `magnitude` computes for vectors — and *not* the algebraic field norm \(|z|^2\) (see Relationship to algebraic structures).

The character concepts combine with `MagnitudeScalable` (described in How Scaling Works) to form the representation concepts the library checks internally:

```cpp
template<typename T>
concept RealScalarRepresentation = !is_quantity<value_type_t<T>> && RealScalar<T> && MagnitudeScalable<T>;

template<typename T>
concept ComplexScalarRepresentation = !is_quantity<value_type_t<T>> && ComplexScalar<T> && MagnitudeScalable<T>;

template<typename T>
concept VectorRepresentation = !is_quantity<value_type_t<T>> && Vector<T> && MagnitudeScalable<T>;
```

The `!is_quantity<value_type_t<T>>` guard applies to the **element type** of `T`, not to `T` itself. For a plain type like `double`, `value_type_t<double>` is `double` — not a quantity, so the guard is satisfied. For a container-style representation like `cartesian_vector<double>`, `value_type_t<cartesian_vector<double>>` is `double` — also fine. The guard rejects `cartesian_vector<quantity<si::metre, double>>` because its element type is itself a quantity, preventing inadvertent nesting of quantities.

The top-level public concept is `RepresentationOf<T, V>`, where `V` is either a `quantity_spec` or a `quantity_character` value:

```cpp
template<typename T, auto V>
concept RepresentationOf =
  (QuantitySpec<decltype(V)> &&
   ((QuantityKindSpec<decltype(V)> && SomeRepresentation<T>) ||
    IsOfCharacter<T, V.character>)) ||
  (std::same_as<quantity_character, decltype(V)> && IsOfCharacter<T, V>);
```

When `V` is a `quantity_spec`, the concept checks whether `T` matches the character embedded in that spec. For a *kind* spec — one that represents an entire kind without pinning a specific character, such as `kind_of<isq::length>` — any valid representation type is accepted. When `V` is a bare `quantity_character` value (e.g., `quantity_character::vector`), `T` must directly satisfy that character’s requirements.

#### 12.2.1 Relationship to algebraic structures

Each concept above approximates a classical algebraic structure but is named for the role it plays in the library rather than for that structure. We avoid the structural names (`Field`, `OrderedField`, `VectorSpace`, …) on purpose:

- A concept can only check that operations exist and that result types are stable; it cannot verify the defining laws. A concept named `Field` would promise associativity, distributivity, and inverses that the compiler never enforces.
- The library deliberately admits types that are *weaker* than the named structure. `int` is not a field (it has no multiplicative inverses) yet must satisfy `BaseScalar`; `int` and `double` are accepted as one-dimensional vectors although they are not, in the usual sense, elements of a vector space. Role-oriented names (“scalar”, “vector”) communicate the intended use without making algebraic claims the type does not honor.

| Concept | Structure approximated | Principal laws left unchecked |
| --- | --- | --- |
| `Addable` | additive group | associativity & commutativity of `+`, existence of `0` |
| `WeaklyRegular` | a set with value semantics (copy + equality) | — |
| `RegularAddable` | a (regular) abelian group under addition | the group axioms above |
| `ScalableWith<T,S>` | a scalar action of `S` on `T` (module / vector-space multiplication) | distributivity and associativity of the action; closure is approximated by round-trip type stability, not `v*s/s == v` |
| `BaseScalar` | a field (commutative division ring) | commutativity/associativity of `×`, distributivity, existence of `0` and `1` |
| `RealScalar` | an ordered field | compatibility of the order with `+` and `×` (`std::totally_ordered` is only a set order) |
| `ComplexScalar` | the complex field `ℂ` (a 2-D real division algebra with modulus) | field axioms; that `real`/`imag` genuinely coordinatize `ℂ` |
| `Vector` | an element of a normed vector space | the vector-space axioms and the norm axioms (homogeneity, triangle inequality) |

A note on the magnitude vocabulary, where the mathematics is most easily miscommunicated. The word “norm” is overloaded across mathematics:

- the **algebraic (field) norm** \(N(z) = z\bar{z} = |z|^2\) — a multiplicative, quadratic form; and
- the **Euclidean (\(L^2\)) norm** \(\lVert v\rVert = \sqrt{N(z)} = |z|\) — the analytic norm satisfying the triangle inequality.

`std::norm(std::complex)` already exists and computes the *field* norm \(|z|^2\), not \(|z|\). A new customization point named `norm` returning \(\lVert v\rVert\) would therefore both collide with `std::norm` and reuse a word that already carries a different, legitimate meaning in the same namespace. The library avoids the ambiguity by using:

- `modulus(z)` for the complex absolute value \(|z|\) (the standard complex-analysis term), and
- `magnitude(v)` for the vector Euclidean norm \(\lVert v\rVert\),

and by exposing no customization point for the field norm.

Complex types are kept out of the vector character by the `!Scalar` guard on the `norm` fallback (described above) together with `disable_vector<std::complex>`: without those, `std::norm(z)` would supply the real value \(|z|^2\) and make a complex number satisfy `Vector` with a spurious “magnitude”.

### 12.3 Customization Points

The library provides several customization mechanisms for representation types. These fall into two categories: **Character determination** (what kind of representation type you have) and **Behavior and values** (how the library interacts with your type).

#### 12.3.1 Character Determination

##### 12.3.1.1 Customization Point Objects (CPOs)

The library uses several CPOs to support different representation types. Providing these CPOs determines the **character** of the representation type. Each CPO checks for implementations in the following priority order:

**`mp_units::real(c)`** - Returns the real part of a complex number:

1. `c.real()` member function
2. `real(c)` free function found via ADL

**`mp_units::imag(c)`** - Returns the imaginary part of a complex number:

1. `c.imag()` member function
2. `imag(c)` free function found via ADL

**`mp_units::modulus(c)`** - Returns the magnitude of a complex number:

1. `c.modulus()` member function
2. `modulus(c)` free function found via ADL
3. `c.abs()` member function
4. `abs(c)` free function found via ADL

**`mp_units::magnitude(v)`** - Returns the magnitude of a vector or tensor as a scalar:

1. `v.magnitude()` member function
2. `magnitude(v)` free function found via ADL
3. `v.norm()` member function
4. `norm(v)` free function found via ADL
5. For arithmetic types: `std::abs(v)`
6. For real scalar types: `v.abs()` member function
7. For real scalar types: `abs(v)` free function found via ADL

Steps 3–4 are provided so that types from linear algebra libraries that follow the `norm()` naming convention work without adaptation. They are guarded to only apply when `T` is not a `Scalar` (i.e., neither a real nor a complex scalar): `std::norm` is overloaded both for arithmetic types and for `std::complex`, returning |x|² rather than |x| in either case, so scalar types are explicitly directed to the `abs` fallback below instead.

For `modulus()`, `abs()` is accepted as a fallback for compatibility with `std::complex` and similar types that use that name. For `magnitude()`, `abs()` enables arithmetic types to serve as 1-dimensional vectors and scalar tensor measures, which accurately reflects engineering practice where most calculations use scalar values rather than full vector/tensor representations. —

##### 12.3.1.2 `disable_real<T>`

A specializable variable template to opt out a type from being treated as a real scalar:

```cpp
template<typename T>
constexpr bool mp_units::disable_real = false;
```

Specializing to `true` prevents a type from being classified as real scalar character even if it satisfies all syntactic requirements. The library uses this internally to exclude `bool`, which is totally ordered and arithmetic but meaningless as a quantity:

```cpp
template<>
constexpr bool mp_units::disable_real<my_type> = true;
```

> [ *Note:* The `disable_real` and `disable_vector` opt-outs exist for the same underlying reason: both guard against syntactic satisfaction of a concept where the **semantics are wrong**.
> 
> - `disable_real<T>`: `std::totally_ordered` is a ubiquitous, incidental property. Many types support `operator<` purely for container use with no physical meaning as a real scalar. `bool` is the canonical example.
> - `disable_vector<T>`: the `magnitude()` CPO accepts `norm()` as a fallback (for linear algebra library interoperability), but `std::norm` for complex types returns |z|² rather than |z|. `std::complex<T>` is therefore opted out by default.
> 
> There is no `disable_complex<T>`. The `ComplexScalar` contract — `real()`, `imag()`, and `modulus()` by those names, plus `T{re, im}` construction — is too specific to be satisfied accidentally by any standard type or mixin. No opt-out is needed. — *end note* ]

---

##### 12.3.1.3 `disable_vector<T>`

A specializable variable template to opt out a type from being treated as a vector:

```cpp
template<typename T>
constexpr bool mp_units::disable_vector = false;
```

Specializing to `true` prevents a type from satisfying `Vector` even if it provides all required operations. The library uses this internally to exclude `std::complex<T>`: `std::complex<T>` satisfies the syntactic requirements for `Vector` because the non-member `std::norm` (found via ADL) is accepted as a fallback for `mp_units::magnitude()`. However, `std::norm(z)` returns |z|² — the **squared** modulus — not |z|, so the semantics are wrong for a vector magnitude. Opting out prevents this accidental satisfaction:

```cpp
// built-in specialization — do not specialize further for std::complex
template<typename T>
constexpr bool mp_units::disable_vector<std::complex<T>> = true;
```

User-defined complex-like types that provide `real()`, `imag()`, and `norm()` should follow the same pattern:

```cpp
template<>
constexpr bool mp_units::disable_vector<my_complex_type> = true;
```

> [ *Note:* The `disable_real` / `disable_vector` pair share the same rationale: both opt-out mechanisms guard against accidental syntactic satisfaction of a concept where the semantics are wrong. `disable_complex` is not needed because the `ComplexScalar` contract — `real()`, `imag()`, `modulus()` by those names, plus `T{re, im}` construction — is too specific to be satisfied accidentally. — *end note* ]

---

#### 12.3.2 Behavior and Values

##### 12.3.2.1 `representation_underlying_type<T>`

`representation_underlying_type<T>` is the extension point for exposing the underlying arithmetic or element type of a representation to the library. It drives the scaling factor type and the `treat_as_floating_point` check:

```cpp
template<typename T>
struct mp_units::representation_underlying_type;  // primary — empty

template<typename T>
using mp_units::representation_underlying_type_t = representation_underlying_type<T>::type;
```

The library provides partial specializations that detect the underlying type in order:

1. `T::value_type` or `T::element_type` member type (cv-qualification stripped)
2. `std::underlying_type_t<T>` for scoped enumerations (unscoped enumerations are excluded — they already implicitly convert to their underlying type)
3. `T` itself as a fallback

If both `value_type` and `element_type` are present with differing underlying types, the trait is empty and the library treats `T` as a leaf — provide only `value_type` unless there is a specific reason to expose both (e.g., satisfying iterator concepts), in which case ensure they name the same underlying type.

A `value_type` member is the preferred form for types under the user’s control:

```cpp
template<typename T>
class my_wrapper {
public:
  using value_type = T;
  // ...
};
```

When the source of a type cannot be modified, the trait may be specialized directly:

```cpp
// MyFloat wraps long double internally
template<>
struct mp_units::representation_underlying_type<MyFloat> {
  using type = long double;
};
```

> [ *Note:* `std::indirectly_readable_traits` was intentionally not reused: that standard trait answers “what does `*t` yield?” and is the extension point for iterators and smart pointers — specializing it for a non-iterator type is a semantic misuse. — *end note* ]

---

##### 12.3.2.2 Scaling operators

The library scales a representation value by calling `value * factor` and `value / factor`, where `factor` is of type `representation_underlying_type_t<T>` (or a wider integer type for the rational integer path — see How Scaling Works for details). A type may additionally provide `operator*(T, UnitMagnitude)` to receive the full compile-time unit magnitude; when present, this operator is called **first** and the factor-based operators serve as a fallback. The magnitude-aware operator may return a **different type** — see Magnitude-aware scaling for the full pattern.

These operators are found via ADL. Hidden friends are the preferred form for types under the user’s control; non-member operators placed in the type’s namespace serve the same role for third-party types:

```cpp
template<typename T>
class my_wrapper {
  T value_;
public:
  using value_type = T;

  friend constexpr my_wrapper operator*(my_wrapper v, T factor) { return my_wrapper{v.value_ * factor}; }
  friend constexpr my_wrapper operator/(my_wrapper v, T factor) { return my_wrapper{v.value_ / factor}; }

  // Optional: magnitude-aware scaling (return type may differ from my_wrapper)
  // template<mp_units::UnitMagnitude M>
  // friend constexpr auto operator*(const my_wrapper& v, M m) { /* ... */ }
};
```

---

##### 12.3.2.3 `treat_as_floating_point<Rep>`

A specializable variable template that tells the library whether a type should be treated as floating-point for the purpose of allowing implicit conversions:

```cpp
template<typename Rep>
constexpr bool mp_units::treat_as_floating_point = /* implementation-defined */;
```

By default, the value is determined by applying `std::chrono::treat_as_floating_point_v` (hosted) or `std::is_floating_point_v` (freestanding) to the recursively-unwrapped underlying type of `Rep`. When `true`, implicit conversions are enabled; otherwise an explicit `value_cast` is required (see Value conversions). A specialization is needed when automatic detection yields an incorrect result:

```cpp
template<>
constexpr bool mp_units::treat_as_floating_point<my_fixed_point_type> = true;
```

---

##### 12.3.2.4 `implicitly_scalable<FromUnit, FromRep, ToUnit, ToRep>`

A specializable variable template that controls **whether** a conversion from `quantity<FromUnit, FromRep>` to `quantity<ToUnit, ToRep>` is implicit or requires an explicit cast via `value_cast`/`force_in`. It is the policy layer built on top of `treat_as_floating_point`: the default formula derives the implicit-conversion decision from it, and a specialization overrides that decision for types where the derived rule is incorrect:

```cpp
template<auto FromUnit, typename FromRep, auto ToUnit, typename ToRep>
constexpr bool mp_units::implicitly_scalable =
  treat_as_floating_point<ToRep> ||
  (!treat_as_floating_point<FromRep> && is_integral_scaling(FromUnit, ToUnit));
```

`mp_units::is_integral_scaling(from, to)` is a `consteval` predicate that can also be used in user specializations to distinguish the integral-factor case (e.g. `m → mm` (×1000)) from fractional ones (e.g. `mm → m` (÷1000), `ft → m`, `deg → rad`).

The default follows the precedent of `std::chrono::duration`: conversions to a floating-point representation are always implicit, conversions between integer representations are implicit only when the unit ratio is an integer multiplier (exact, no truncation), and all other cases require an explicit cast.

For example, a decimal fixed-point type that represents fractional ratios exactly can permit all unit conversions implicitly:

```cpp
template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, safe_decimal, ToUnit, safe_decimal> = true;
```

When precision is asymmetric between two types, the specialization can be directional:

```cpp
template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, double, ToUnit, my_decimal> = true;

template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, my_decimal, ToUnit, double> = false;
```

`mp_units::is_integral_scaling` may be reused in a specialization to distinguish integral from fractional unit ratios. See Value conversions for details.

---

##### 12.3.2.5 `representation_values<Rep>`

A specializable class template that provides the special values used by `quantity::zero()`, `quantity::min()`, `quantity::max()`, mathematical rounding operations, and division-by-zero checks:

```cpp
template<typename Rep>
struct mp_units::representation_values {
  static constexpr Rep zero() noexcept;
  static constexpr Rep one() noexcept;
  static constexpr Rep min() noexcept;
  static constexpr Rep max() noexcept;
};
```

In hosted environments the primary specialization inherits `zero()`, `min()`, and `max()` from `std::chrono::duration_values<Rep>`; `one()` is always defined in the struct itself, constrained to `std::constructible_from<Rep, int>`. In freestanding environments all four methods are defined directly, each guarded by its own `requires` clause: `zero()` and `one()` require `std::constructible_from<Rep, int>`; `min()` requires `std::numeric_limits<Rep>::is_specialized` and that `std::numeric_limits<Rep>::lowest()` returns `Rep`; `max()` requires the same plus `std::numeric_limits<Rep>::max()` returning `Rep`. An explicit specialization is required for types that cannot satisfy those constraints or that need non-standard special values:

```cpp
template<typename T>
struct mp_units::representation_values<my_custom_type<T>> {
  static constexpr my_custom_type<T> zero() noexcept
  { return my_custom_type<T>{T{0}}; }

  static constexpr my_custom_type<T> one() noexcept
  { return my_custom_type<T>{T{1}}; }

  static constexpr my_custom_type<T> min() noexcept
  { return my_custom_type<T>{std::numeric_limits<T>::lowest()}; }

  static constexpr my_custom_type<T> max() noexcept
  { return my_custom_type<T>{std::numeric_limits<T>::max()}; }
};
```

### 12.4 How Scaling Works

Every representation type must be **unit-conversion scalable** — the library must be able to apply a unit magnitude ratio to it internally. This is captured by the `MagnitudeScalable` concept, which directly names the three built-in scaling paths:

```cpp
concept MagnitudeScalable =
  WeaklyRegular<T> && (UsesMagnitudeAwareScaling<T> || UsesFloatingPointScaling<T> || UsesIntegerScaling<T>);
```

`UsesMagnitudeAwareScaling` is satisfied by any type that provides `operator*(T, UnitMagnitude)` — checked first by the scaling engine, before the two built-in numeric paths. The full pattern is described in Magnitude-aware scaling:

```cpp
concept UsesMagnitudeAwareScaling = requires(const T& v) { v * mag<1>; };
```

`UsesFloatingPointScaling` matches any type — or container thereof — whose underlying type satisfies `treat_as_floating_point`, is constructible from `long double` (the precision at which magnitude constants are evaluated), and supports `operator*` and `operator/` with that underlying type, returning a weakly-regular result:

```cpp
concept UsesFloatingPointScaling =
  (treat_as_floating_point<T> || treat_as_floating_point<representation_underlying_type_t<T>>) &&
  std::constructible_from<representation_underlying_type_t<T>, long double> &&
  requires(T value, representation_underlying_type_t<T> f) {
    { value * f } -> WeaklyRegular;
    { value / f } -> WeaklyRegular;
  };
```

`UsesIntegerScaling` matches any type whose underlying type satisfies `detail::integral` (the scaling engine uses `get_value<wider_t>`, `wider_int_for<element_t>`, and `fixed_point<element_t>` internally, all of which require an integer element type). Scaling is routed through the type’s own `operator*` and `operator/`, so wrappers can check for overflow and containers can scale element-wise. The factor type is `wider_int_for<element_t>` — a wider integer of matching sign (e.g. `int64_t` for `int16_t`, `uint64_t` for `uint16_t`) — to prevent intermediate overflow in rational-magnitude conversions:

```cpp
concept UsesIntegerScaling =
  detail::integral<representation_underlying_type_t<T>> &&
  requires(T value, wider_int_for<representation_underlying_type_t<T>> wf) {
    { value * wf };
    { value / wf };
  };
```

> [ *Note:* `detail::integral` is used rather than `std::integral` because on GCC in strict mode (`-std=c++20`) `std::integral<__int128>` is `false` — the standard traits are not specialized for `__int128` outside GNU extensions. When the platform lacks `__SIZEOF_INT128__` entirely, `int128_t` and `uint128_t` are software-emulation types that also do not satisfy `std::integral`. `detail::integral` patches both gaps:
> 
> ```cpp
> template<typename T>
> concept detail::integral =
>   std::integral<T> ||
>   std::same_as<std::remove_cv_t<T>, int128_t> ||
>   std::same_as<std::remove_cv_t<T>, uint128_t>;
> ```
> 
> The scaling engine internals (`get_value`, `wider_int_for`, `fixed_point`) are all specialized for `int128_t` / `uint128_t`, ensuring the full integer scaling pipeline works correctly for 128-bit element types on all supported compilers. — *end note* ]

Most standard types satisfy `MagnitudeScalable` automatically. See Scaling operators for how to provide `operator*` and `operator/` for custom types.

#### 12.4.1 Built-in scaling algorithm

When two quantities of convertible units are combined or converted, the library applies the unit magnitude `M` to the representation value via `scale<To>(M, value)`. The built-in decision tree is:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPgo8IS0tIEdlbmVyYXRlZCBieSBncmFwaHZpeiB2ZXJzaW9uIDIuNDIuNCAoMCkKIC0tPgo8IS0tIFRpdGxlOiBzY2FsaW5nIFBhZ2VzOiAxIC0tPgo8c3ZnIHdpZHRoPSIxMDAlIiAKIHZpZXdCb3g9IjAuMDAgMC4wMCA4NTYuNTAgNTM1LjAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KPGcgaWQ9ImdyYXBoMCIgY2xhc3M9ImdyYXBoIiB0cmFuc2Zvcm09InNjYWxlKDEgMSkgcm90YXRlKDApIHRyYW5zbGF0ZSg0IDUzMSkiPgo8dGl0bGU+c2NhbGluZzwvdGl0bGU+Cjxwb2x5Z29uIGZpbGw9IndoaXRlIiBzdHJva2U9InRyYW5zcGFyZW50IiBwb2ludHM9Ii00LDQgLTQsLTUzMSA4NTIuNSwtNTMxIDg1Mi41LDQgLTQsNCIvPgo8IS0tIEEgLS0+CjxnIGlkPSJub2RlMSIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+QTwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xNzcuNSwtNTI3QzE3Ny41LC01MjcgMTAwLjUsLTUyNyAxMDAuNSwtNTI3IDk0LjUsLTUyNyA4OC41LC01MjEgODguNSwtNTE1IDg4LjUsLTUxNSA4OC41LC01MDMgODguNSwtNTAzIDg4LjUsLTQ5NyA5NC41LC00OTEgMTAwLjUsLTQ5MSAxMDAuNSwtNDkxIDE3Ny41LC00OTEgMTc3LjUsLTQ5MSAxODMuNSwtNDkxIDE4OS41LC00OTcgMTg5LjUsLTUwMyAxODkuNSwtNTAzIDE4OS41LC01MTUgMTg5LjUsLTUxNSAxODkuNSwtNTIxIDE4My41LC01MjcgMTc3LjUsLTUyNyIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxMzkiIHk9Ii01MDYuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPnNjYWxlKE0sIHZhbHVlKTwvdGV4dD4KPC9nPgo8IS0tIE1BIC0tPgo8ZyBpZD0ibm9kZTIiIGNsYXNzPSJub2RlIj4KPHRpdGxlPk1BPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEyNy4zMSwtNDQzLjMxQzEyNy4zMSwtNDQzLjMxIDExLjY5LC00MTYuNjkgMTEuNjksLTQxNi42OSA1Ljg1LC00MTUuMzUgNS44NSwtNDEyLjY1IDExLjY5LC00MTEuMzEgMTEuNjksLTQxMS4zMSAxMjcuMzEsLTM4NC42OSAxMjcuMzEsLTM4NC42OSAxMzMuMTUsLTM4My4zNSAxNDQuODUsLTM4My4zNSAxNTAuNjksLTM4NC42OSAxNTAuNjksLTM4NC42OSAyNjYuMzEsLTQxMS4zMSAyNjYuMzEsLTQxMS4zMSAyNzIuMTUsLTQxMi42NSAyNzIuMTUsLTQxNS4zNSAyNjYuMzEsLTQxNi42OSAyNjYuMzEsLTQxNi42OSAxNTAuNjksLTQ0My4zMSAxNTAuNjksLTQ0My4zMSAxNDQuODUsLTQ0NC42NSAxMzMuMTUsLTQ0NC42NSAxMjcuMzEsLTQ0My4zMSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxMzkiIHk9Ii00MTcuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPm9wKihULCBVbml0TWFnbml0dWRlKTwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTM5IiB5PSItNDA1LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5wcm92aWRlZD88L3RleHQ+CjwvZz4KPCEtLSBBJiM0NTsmZ3Q7TUEgLS0+CjxnIGlkPSJlZGdlMSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+QSYjNDU7Jmd0O01BPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEzOSwtNDkwLjk0QzEzOSwtNDgxLjE5IDEzOSwtNDY4LjUxIDEzOSwtNDU2LjMxIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjE0Mi41LC00NTYuMjUgMTM5LC00NDYuMjUgMTM1LjUsLTQ1Ni4yNSAxNDIuNSwtNDU2LjI1Ii8+CjwvZz4KPCEtLSBNQVIgLS0+CjxnIGlkPSJub2RlMyIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+TUFSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE4NSwtMzEzQzE4NSwtMzEzIDM1LC0zMTMgMzUsLTMxMyAyOSwtMzEzIDIzLC0zMDcgMjMsLTMwMSAyMywtMzAxIDIzLC0yODkgMjMsLTI4OSAyMywtMjgzIDI5LC0yNzcgMzUsLTI3NyAzNSwtMjc3IDE4NSwtMjc3IDE4NSwtMjc3IDE5MSwtMjc3IDE5NywtMjgzIDE5NywtMjg5IDE5NywtMjg5IDE5NywtMzAxIDE5NywtMzAxIDE5NywtMzA3IDE5MSwtMzEzIDE4NSwtMzEzIi8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjExMCIgeT0iLTI5OC4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+VXNlc01hZ25pdHVkZUF3YXJlU2NhbGluZzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTEwIiB5PSItMjg2LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj52YWx1ZSAqIE17fTwvdGV4dD4KPC9nPgo8IS0tIE1BJiM0NTsmZ3Q7TUFSIC0tPgo8ZyBpZD0iZWRnZTIiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPk1BJiM0NTsmZ3Q7TUFSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEzMS42OCwtMzgzLjQ4QzEyNy4wOCwtMzY0LjkxIDEyMS4xOSwtMzQxLjE1IDExNi43MSwtMzIzLjA3Ii8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjEyMC4wNiwtMzIyLjAzIDExNC4yNiwtMzEzLjE3IDExMy4yNiwtMzIzLjcyIDEyMC4wNiwtMzIyLjAzIi8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjEzNSIgeT0iLTM1MiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnllczwvdGV4dD4KPC9nPgo8IS0tIEIgLS0+CjxnIGlkPSJub2RlNCIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+QjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0zOTcuMTksLTMyNC44NUMzOTcuMTksLTMyNC44NSAyNDQuODEsLTI5Ny4xNSAyNDQuODEsLTI5Ny4xNSAyMzguOSwtMjk2LjA3IDIzOC45LC0yOTMuOTMgMjQ0LjgxLC0yOTIuODUgMjQ0LjgxLC0yOTIuODUgMzk3LjE5LC0yNjUuMTUgMzk3LjE5LC0yNjUuMTUgNDAzLjEsLTI2NC4wNyA0MTQuOSwtMjY0LjA3IDQyMC44MSwtMjY1LjE1IDQyMC44MSwtMjY1LjE1IDU3My4xOSwtMjkyLjg1IDU3My4xOSwtMjkyLjg1IDU3OS4xLC0yOTMuOTMgNTc5LjEsLTI5Ni4wNyA1NzMuMTksLTI5Ny4xNSA1NzMuMTksLTI5Ny4xNSA0MjAuODEsLTMyNC44NSA0MjAuODEsLTMyNC44NSA0MTQuOSwtMzI1LjkzIDQwMy4xLC0zMjUuOTMgMzk3LjE5LC0zMjQuODUiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDA5IiB5PSItMjk4LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj50cmVhdF9hc19mbG9hdGluZ19wb2ludDwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDA5IiB5PSItMjg2LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj4mbHQ7VCZndDsgb3IgJmx0O3VuZGVybHlpbmdfdCZsdDtUJmd0OyZndDs/PC90ZXh0Pgo8L2c+CjwhLS0gTUEmIzQ1OyZndDtCIC0tPgo8ZyBpZD0iZWRnZTMiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPk1BJiM0NTsmZ3Q7QjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xODUuNzIsLTM5Mi43NUMyMzAuOTUsLTM3My4xNSAyOTkuNzMsLTM0My4zNSAzNDguOTksLTMyMiIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIzNTAuNDgsLTMyNS4xNyAzNTguMjYsLTMxNy45OSAzNDcuNywtMzE4Ljc1IDM1MC40OCwtMzI1LjE3Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjI4OS41IiB5PSItMzUyIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+bm88L3RleHQ+CjwvZz4KPCEtLSBGUCAtLT4KPGcgaWQ9Im5vZGU1IiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5GUDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik00MzAsLTIwOEM0MzAsLTIwOCAyMjIsLTIwOCAyMjIsLTIwOCAyMTYsLTIwOCAyMTAsLTIwMiAyMTAsLTE5NiAyMTAsLTE5NiAyMTAsLTE4NCAyMTAsLTE4NCAyMTAsLTE3OCAyMTYsLTE3MiAyMjIsLTE3MiAyMjIsLTE3MiA0MzAsLTE3MiA0MzAsLTE3MiA0MzYsLTE3MiA0NDIsLTE3OCA0NDIsLTE4NCA0NDIsLTE4NCA0NDIsLTE5NiA0NDIsLTE5NiA0NDIsLTIwMiA0MzYsLTIwOCA0MzAsLTIwOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIzMjYiIHk9Ii0xOTMuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPlVzZXNGbG9hdGluZ1BvaW50U2NhbGluZzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMzI2IiB5PSItMTgxLjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5lLmcuIGRvdWJsZSwgY2FydGVzaWFuX3ZlY3RvciZsdDtkb3VibGUmZ3Q7PC90ZXh0Pgo8L2c+CjwhLS0gQiYjNDU7Jmd0O0ZQIC0tPgo8ZyBpZD0iZWRnZTQiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkImIzQ1OyZndDtGUDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0zODcuMTksLTI2Ni45NEMzNzQuNTUsLTI1MS4yNSAzNTguNzMsLTIzMS42MiAzNDYuMzQsLTIxNi4yNSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIzNDguODYsLTIxMy43OSAzMzkuODYsLTIwOC4yIDM0My40MSwtMjE4LjE4IDM0OC44NiwtMjEzLjc5Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjM3NiIgeT0iLTIzMyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnRydWU8L3RleHQ+CjwvZz4KPCEtLSBJTlQgLS0+CjxnIGlkPSJub2RlNiIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+SU5UPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTcwMy41LC0yMDhDNzAzLjUsLTIwOCA0OTAuNSwtMjA4IDQ5MC41LC0yMDggNDg0LjUsLTIwOCA0NzguNSwtMjAyIDQ3OC41LC0xOTYgNDc4LjUsLTE5NiA0NzguNSwtMTg0IDQ3OC41LC0xODQgNDc4LjUsLTE3OCA0ODQuNSwtMTcyIDQ5MC41LC0xNzIgNDkwLjUsLTE3MiA3MDMuNSwtMTcyIDcwMy41LC0xNzIgNzA5LjUsLTE3MiA3MTUuNSwtMTc4IDcxNS41LC0xODQgNzE1LjUsLTE4NCA3MTUuNSwtMTk2IDcxNS41LC0xOTYgNzE1LjUsLTIwMiA3MDkuNSwtMjA4IDcwMy41LC0yMDgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTk3IiB5PSItMTkzLjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5Vc2VzSW50ZWdlclNjYWxpbmc8L3RleHQ+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjU5NyIgeT0iLTE4MS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+ZS5nLiBpbnQsIHNhZmVfaW50LCBjYXJ0ZXNpYW5fdmVjdG9yJmx0O2ludCZndDs8L3RleHQ+CjwvZz4KPCEtLSBCJiM0NTsmZ3Q7SU5UIC0tPgo8ZyBpZD0iZWRnZTUiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkImIzQ1OyZndDtJTlQ8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNDUxLjY2LC0yNzAuNjNDNDgzLjMxLC0yNTMuMjkgNTI2LjE3LC0yMjkuODEgNTU3LjEzLC0yMTIuODQiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNTU4Ljg0LC0yMTUuOSA1NjUuOTMsLTIwOC4wMiA1NTUuNDgsLTIwOS43NiA1NTguODQsLTIxNS45Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjUzOC41IiB5PSItMjMzIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+ZmFsc2U8L3RleHQ+CjwvZz4KPCEtLSBHIC0tPgo8ZyBpZD0ibm9kZTciIGNsYXNzPSJub2RlIj4KPHRpdGxlPkc8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTg1LjM5LC0xMjMuOTZDNTg1LjM5LC0xMjMuOTYgNTM5Ljg0LC0xMTIuMDQgNTM5Ljg0LC0xMTIuMDQgNTM0LjA0LC0xMTAuNTIgNTM0LjA0LC0xMDcuNDggNTM5Ljg0LC0xMDUuOTYgNTM5Ljg0LC0xMDUuOTYgNTg1LjM5LC05NC4wNCA1ODUuMzksLTk0LjA0IDU5MS4yLC05Mi41MiA2MDIuOCwtOTIuNTIgNjA4LjYxLC05NC4wNCA2MDguNjEsLTk0LjA0IDY1NC4xNiwtMTA1Ljk2IDY1NC4xNiwtMTA1Ljk2IDY1OS45NiwtMTA3LjQ4IDY1OS45NiwtMTEwLjUyIDY1NC4xNiwtMTEyLjA0IDY1NC4xNiwtMTEyLjA0IDYwOC42MSwtMTIzLjk2IDYwOC42MSwtMTIzLjk2IDYwMi44LC0xMjUuNDggNTkxLjIsLTEyNS40OCA1ODUuMzksLTEyMy45NiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI1OTciIHk9Ii0xMDYuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPm1hZ25pdHVkZT88L3RleHQ+CjwvZz4KPCEtLSBJTlQmIzQ1OyZndDtHIC0tPgo8ZyBpZD0iZWRnZTYiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPklOVCYjNDU7Jmd0O0c8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTk3LC0xNzEuODZDNTk3LC0xNjEuNzEgNTk3LC0xNDguNjMgNTk3LC0xMzcuMTIiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNjAwLjUsLTEzNy4xMSA1OTcsLTEyNy4xMSA1OTMuNSwtMTM3LjExIDYwMC41LC0xMzcuMTEiLz4KPC9nPgo8IS0tIEkgLS0+CjxnIGlkPSJub2RlOCIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+STwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik00NzksLTM2QzQ3OSwtMzYgMzY5LC0zNiAzNjksLTM2IDM2MywtMzYgMzU3LC0zMCAzNTcsLTI0IDM1NywtMjQgMzU3LC0xMiAzNTcsLTEyIDM1NywtNiAzNjMsMCAzNjksMCAzNjksMCA0NzksMCA0NzksMCA0ODUsMCA0OTEsLTYgNDkxLC0xMiA0OTEsLTEyIDQ5MSwtMjQgNDkxLC0yNCA0OTEsLTMwIDQ4NSwtMzYgNDc5LC0zNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI0MjQiIHk9Ii0yMS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+ZXhhY3QgaW50ZWdlciDDlzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDI0IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGUuZy4gbeKGkm1tLCDDlzEwMDApPC90ZXh0Pgo8L2c+CjwhLS0gRyYjNDU7Jmd0O0kgLS0+CjxnIGlkPSJlZGdlNyIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+RyYjNDU7Jmd0O0k8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTc1LjA5LC05Ni43M0M1NDcuOCwtODIuNjkgNTAwLjU3LC01OC4zOSA0NjYuMTcsLTQwLjY5Ii8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjQ2Ny43NywtMzcuNTggNDU3LjI4LC0zNi4xMiA0NjQuNTcsLTQzLjgxIDQ2Ny43NywtMzcuNTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTQwIiB5PSItNjEiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwLjAwIj5pbnRlZ3JhbDwvdGV4dD4KPC9nPgo8IS0tIFIgLS0+CjxnIGlkPSJub2RlOSIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+UjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik02NTUsLTM2QzY1NSwtMzYgNTM5LC0zNiA1MzksLTM2IDUzMywtMzYgNTI3LC0zMCA1MjcsLTI0IDUyNywtMjQgNTI3LC0xMiA1MjcsLTEyIDUyNywtNiA1MzMsMCA1MzksMCA1MzksMCA2NTUsMCA2NTUsMCA2NjEsMCA2NjcsLTYgNjY3LC0xMiA2NjcsLTEyIDY2NywtMjQgNjY3LC0yNCA2NjcsLTMwIDY2MSwtMzYgNjU1LC0zNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI1OTciIHk9Ii0yMS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+d2lkZW5lZCBpbnQgYXJpdGhtZXRpYzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTk3IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGludDY0X3QgLyAxMjgmIzQ1O2JpdCk8L3RleHQ+CjwvZz4KPCEtLSBHJiM0NTsmZ3Q7UiAtLT4KPGcgaWQ9ImVkZ2U4IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5HJiM0NTsmZ3Q7UjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik01OTcsLTkwLjg0QzU5NywtNzguMjggNTk3LC02MC45OCA1OTcsLTQ2LjUiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNjAwLjUsLTQ2LjExIDU5NywtMzYuMTEgNTkzLjUsLTQ2LjExIDYwMC41LC00Ni4xMSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI2MTYiIHk9Ii02MSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnJhdGlvbmFsPC90ZXh0Pgo8L2c+CjwhLS0gSVIgLS0+CjxnIGlkPSJub2RlMTAiIGNsYXNzPSJub2RlIj4KPHRpdGxlPklSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTgzNi41LC0zNkM4MzYuNSwtMzYgNzE1LjUsLTM2IDcxNS41LC0zNiA3MDkuNSwtMzYgNzAzLjUsLTMwIDcwMy41LC0yNCA3MDMuNSwtMjQgNzAzLjUsLTEyIDcwMy41LC0xMiA3MDMuNSwtNiA3MDkuNSwwIDcxNS41LDAgNzE1LjUsMCA4MzYuNSwwIDgzNi41LDAgODQyLjUsMCA4NDguNSwtNiA4NDguNSwtMTIgODQ4LjUsLTEyIDg0OC41LC0yNCA4NDguNSwtMjQgODQ4LjUsLTMwIDg0Mi41LC0zNiA4MzYuNSwtMzYiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNzc2IiB5PSItMjEuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPmxvbmcgZG91YmxlIGZpeGVkJiM0NTtwb2ludDwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNzc2IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGUuZy4gZGVn4oaScmFkLCDDl8+ALzE4MCk8L3RleHQ+CjwvZz4KPCEtLSBHJiM0NTsmZ3Q7SVIgLS0+CjxnIGlkPSJlZGdlOSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+RyYjNDU7Jmd0O0lSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTYxOS42NywtOTYuNzNDNjQ3LjkxLC04Mi42OSA2OTYuNzcsLTU4LjM5IDczMi4zNywtNDAuNjkiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNzM0LjE3LC00My43MSA3NDEuNTcsLTM2LjEyIDczMS4wNiwtMzcuNDQgNzM0LjE3LC00My43MSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI3MTkuNSIgeT0iLTYxIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+aXJyYXRpb25hbDwvdGV4dD4KPC9nPgo8L2c+Cjwvc3ZnPgo=)

The magnitude-aware path (`operator*(T, UnitMagnitude)`) is checked first — before any of the built-in paths. If a representation type provides this operator, it has full control over how scaling is performed and what type is returned. The built-in paths are only used as a fallback.

The integer path (`UsesIntegerScaling`) never promotes values to floating-point, even for the rational and irrational sub-paths. This is intentional: the user explicitly chose an integer representation type, opting out of floating-point arithmetic. The platform may lack FP hardware (embedded systems, DSPs), rely on software-emulated FP, or enforce a no-FP policy. The library respects that choice throughout unit conversion.

The design preference order is **exact integer > exact rational > approximate irrational**: integer multiplication keeps lossless conversions exact (`42 * m` → `42000 * mm` without floating-point rounding); rational factors are applied as numerator × value ÷ denominator entirely in integer arithmetic; and irrational factors (π/180, √2, …) fall back to a `long double` approximation rounded to the target integer type.

The rational path computes `value * numerator / denominator` entirely in integer arithmetic using widened types to prevent intermediate overflow — for example, converting feet to metres multiplies by 3048 before dividing by 10000, which would overflow a 64-bit integer for values above ~3×10¹⁵ without extra width:

| Source type | Widened to |
| --- | --- |
| Signed ≤ 32 bits (`int8_t`…`int32_t`) | `int64_t` |
| Unsigned ≤ 32 bits | `uint64_t` |
| `int64_t` | `__int128` or equivalent signed 128-bit |
| `uint64_t` | `unsigned __int128` or equivalent unsigned |

Using `long double` instead would violate the no-FP principle and introduce rounding (`0.3048` is not exactly representable in binary floating-point); on ARM / Apple Silicon `long double == double` anyway, giving no extra range.

Double-width arithmetic avoids most UB during intermediate scaling, but cannot prevent overflow in the final result when that result doesn’t fit in the target type. Runtime overflow detection requires a representation type that checks arithmetic operations — a checked-integer wrapper (e.g., `safe_int<T>` from mp-units) satisfies `UsesIntegerScaling` and will trap overflows in the final result.

Aggregate representation types that store multiple independently-scaled fields (e.g., `uncertainty<T>` holding a central value and an error bound) implement `operator*` and `operator/` to distribute scaling across all internal fields; the built-in integer and floating-point paths invoke those operators on the aggregate as a unit.

##### 12.4.1.1 Floating-point precision

For floating-point representation types (`UsesFloatingPointScaling`), the unit magnitude is reduced to a single `constexpr` scalar (a `double` or `long double` value representing the exact mathematical ratio) and applied as a single multiplication: `value * factor`. This matches what equivalent hand-written code would do. The library makes no stronger precision guarantee than the underlying floating-point operations provide — in particular, it does not mandate any specific ULP bound. This is consistent with the rest of the C++ standard library, including `std::chrono::duration`, which likewise leaves floating-point conversion precision to the quality of the implementation.

The concern raised that lazy evaluation could produce results differing from hand-written code by more than a few ULPs does not apply here: the magnitude is always a single compile-time constant representing the full unit ratio, never a chain of intermediate multiplications. Overflow to `+inf` would therefore only occur for values that would also overflow the equivalent hand-written multiplication, which is a property of the value, not the library.

For integer types, widened arithmetic (as described above) prevents intermediate overflow. For floating-point types, implementations are encouraged to choose a representation of the conversion factor that minimises precision loss, but this is a quality-of-implementation concern, not a normative requirement.

#### 12.4.2 Magnitude-aware scaling

A type satisfies `UsesMagnitudeAwareScaling` (see How Scaling Works) by providing `operator*(T, UnitMagnitude)` as a hidden friend. Unlike the built-in numeric paths, this operator receives the full compile-time unit magnitude and may return a **different type** — for example, a range-validated representation can adjust its bounds during conversion: constraining values to [-180, 180] in degrees should produce a type constrained to [-π, π] when converted to radians, otherwise the bounds would be meaningless in the target unit:

```cpp
// Example custom type (not provided by the library)
template<std::treat_as_floating_point T, auto Min, auto Max, typename Policy>
class bounded_value : /* ... */ {
public:
  template<std::UnitMagnitude M>
  [[nodiscard]] friend constexpr auto operator*(const bounded_value& val, M m)
  {
    constexpr T new_lo = std::scale<T>(M{}, T{Min});
    constexpr T new_hi = std::scale<T>(M{}, T{Max});

    const T scaled = std::scale<T>(m, val.value());

    if constexpr (new_lo <= new_hi)
      return bounded_value<T, new_lo, new_hi, Policy>(scaled);
    else
      return bounded_value<T, new_hi, new_lo, Policy>(scaled);
  }
};
```

The `scale` function handles precision optimization automatically — when the magnitude’s inverse is integral (e.g. degree-to-radian with π/180), it divides by the inverse instead of multiplying, avoiding FP rounding errors.

The library calls `value * M{}` in `scale()` before trying the built-in paths. Because the return type may differ from the input, `quantity::in(unit)` propagates the new representation type through `sudo_cast`, and the resulting `quantity` (or `quantity_point`) automatically uses the scaled-bounds representation.

### 12.5 Complex quantities and units

TODO

### 12.6 Vector and tensor quantities

TODO

### 12.7 Logarithmic quantities and units

TODO

## 13 Hello units

This chapter traces a complete, minimal example from user-facing code down through the library’s layers, showing how each piece fits together. The goal is to build an intuition for the design before reading the detailed specifications that follow.

### 13.1 The example

A *smoot* is a unit of length equal to the height of Oliver Smoot (five feet and seven inches), famously used to measure the Harvard Bridge in 1958. Adding it to the library takes exactly one line:

```cpp
import std;

inline constexpr struct smoot : std::named_unit<"smoot", std::mag<67> * std::usc::inch> {} smoot;

int main()
{
  constexpr std::quantity dist = 364.4 * smoot;
  std::println("Harvard Bridge length = {::N[.1f]} ({::N[.1f]}, {::N[.2f]}) ± 1 εar",
               dist, dist.in(std::usc::foot), dist.in(std::si::metre));
}
```

Output:

```
Harvard Bridge length = 364.4 smoot (2034.6 ft, 620.14 m) ± 1 εar
```

Three things happen here: a unit is defined, a quantity is created, and the quantity is converted. Each layer is examined below.

### 13.2 Layer 1: Units — a chain to a base

Every unit ultimately traces back to a *base unit* — a unit associated directly with a quantity kind rather than being defined relative to another unit. The `named_unit<Symbol, kind_of<QS>>` form is used for these coherent base units:

```cpp
// base unit — anchored to the length quantity kind
struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
```

From there, US customary units are defined as a chain of scaled aliases using the `named_unit<Symbol, Scale>` form, each expressed in terms of the one above:

```cpp
struct yard : named_unit<"yd", mag_ratio<9144, 10000> * si::metre> {} yard;  // 0.9144 m
struct foot : named_unit<"ft", mag_ratio<1, 3>        * yard>      {} foot;  // 1/3 yd
struct inch : named_unit<"in", mag_ratio<1, 12>       * foot>      {} inch;  // 1/12 ft
```

Both forms assign a name and symbol to the unit and automatically propagate the quantity kind down the chain — `inch` is a unit of *length* with no extra annotation.

### 13.3 Layer 2: Magnitudes — exact compile-time rationals

The scaling factors `mag_ratio<N, D>` and `mag<N>` are compile-time rational numbers stored as products of prime powers. No floating-point arithmetic occurs in the type system. When the library traverses the chain from `inch` to `metre`, it multiplies the accumulated factors:

```
1 inch = (1/12) × (1/3) × (9144/10000) m  =  127/5000 m  =  0.0254 m  (exact)
```

The conversion factor from `smoot` to `metre` is therefore:

```
1 smoot = 67 × (127/5000) m  =  8509/5000 m  (exact rational)
```

This ratio is available entirely at compile time and applied to the stored value only at the point of an explicit conversion.

### 13.4 Layer 3: Naming a unit — `named_unit<"smoot", mag<67> * usc::inch>`

The expression `mag<67> * usc::inch` produces a `scaled_unit<mag<67>, inch>`. Wrapping it in `named_unit`:

```cpp
struct smoot : named_unit<"smoot", mag<67> * usc::inch> {} smoot;
```

does three things simultaneously:

1. Records the symbol `"smoot"` for use in text output.
2. Inherits the `_base_type_` of the scaled unit, making `smoot` a unit of *length*.
3. Records the scaling so that `get_canonical_unit(smoot)` can recover the exact magnitude relative to `metre` without any additional bookkeeping.

### 13.5 Layer 4: The `quantity` type

The central type of the library is:

```cpp
template<Reference auto R, RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity {
public:
  Rep numerical_value_is_an_implementation_detail_;  // the only runtime datum

  static constexpr Reference auto reference        = R;
  static constexpr QuantitySpec auto quantity_spec = get_quantity_spec(R);    // isq::length
  static constexpr Dimension auto dimension        = quantity_spec.dimension; // dim_length
  static constexpr Unit auto unit                  = get_unit(R);             // smoot
  using rep = Rep;
};
```

The unit, quantity specification, and dimension are part of the **type** — they consume no storage and carry zero runtime overhead. Only the numerical value is stored.

A bare unit such as `smoot` also satisfies the `Reference` concept (since the quantity specification can be recovered from it via `get_quantity_spec`), so it can serve directly as the reference template argument.

### 13.6 Layer 5: Creating a quantity — `364.4 * smoot`

The expression `364.4 * smoot` invokes:

```cpp
template<typename FwdRep, Reference R, ...>
  requires(!OffsetUnit<get_unit(R{})>)
constexpr quantity<R{}, Rep> operator*(FwdRep&& lhs, R) { return quantity{std::forward<FwdRep>(lhs), R{}}; }
```

The result is `quantity<smoot{}, double>` — a type that encodes `smoot` and `double` as compile-time template arguments and stores only `364.4` at runtime.

### 13.7 Layer 6: Unit conversion — `dist.in(si::metre)`

`.in(ToU)` checks at compile time that `ToU` is a valid unit for the same quantity specification, then applies the conversion:

```cpp
template<UnitOf<quantity_spec> ToU>
  requires ImplicitScaling<unit, ToU{}, rep>
constexpr QuantityOf<quantity_spec> auto in(ToU) const;
```

Internally, the conversion ratio is computed entirely at compile time:

```cpp
constexpr UnitMagnitude auto c_mag = get_canonical_unit(From::unit).mag / get_canonical_unit(To::unit).mag;
```

The exact rational `8509/5000` is then applied to the stored value at runtime. The fraction is converted to a `long double` constant **at compile time**, so the actual runtime operation for a `double` representation is a single multiplication:

```
364.4 × 1.7018L ≈ 620.14
```

Scaling behaviour for other representation types (integers, fixed-point, custom types) is discussed in How Scaling Works.

The return type is `quantity<si::metre{}, double>` holding `620.14`. Attempting to convert to an incompatible unit — for example `si::second` — is a compile-time error because `si::second` does not satisfy `UnitOf<isq::length>`.

### 13.8 Layer 7: Formatting — `{::N[.1f]}`

The library provides a `std::formatter` specialization for `quantity`. The format-specification grammar (described fully in Text output) gives independent control over the numerical part and the unit symbol. For `dist.in(si::metre)` formatted with `{::N[.2f]}`, the `N[.2f]` sub-spec is forwarded to the `Rep` formatter (producing `"620.14"`), after which the formatter appends the unit symbol `"m"` — yielding `"620.14 m"`.

---

That is the full path from user code to bits: one stored `double`, with the unit, quantity kind, dimension, and conversion factor living entirely in the C++ type system.

This is intentionally a minimal example. Many library features — quantity convertibility, generic interfaces and concepts, the affine space, representation type constraints, mixed-unit arithmetic, value casts, and more — are not used here and therefore not described. They are covered in the chapters that follow.

## 14 Usage examples

This chapter demonstrates key safety features through minimal compile-time examples.

### 14.1 Basic quantity equations

Let’s start with a really simple example presenting basic operations that every physical quantities and units library should provide:

```cpp
import std;

using namespace std::si::unit_symbols;

// simple numeric operations
static_assert(10 * km / 2 == 5 * km);

// conversions to common units
static_assert(1 * h == 3600 * s);
static_assert(1 * km + 1 * m == 1001 * m);

// derived quantities
static_assert(1 * km / (1 * s) == 1000 * m / s);
static_assert(2 * km / h * (2 * h) == 4 * km);
static_assert(2 * km / (2 * km / h) == 1 * h);

static_assert(2 * m * (3 * m) == 6 * m2);

static_assert(10 * km / (5 * km) == 2);

static_assert(1000 / (1 * s) == 1 * kHz);
```

Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

### 14.2 mp-units showcase

The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.

```cpp
import std;

constexpr std::QuantityOf<std::isq::speed> auto avg_speed(std::QuantityOf<std::isq::length> auto d,
                                                          std::QuantityOf<std::isq::time> auto t)
{
  return d / t;
}

int main()
{
  using namespace std::si::unit_symbols;
  using namespace std::yard_pound::unit_symbols;

  constexpr std::quantity v1 = 110 * km / h;
  constexpr std::quantity v2 = 70 * mph;
  constexpr std::quantity v3 = avg_speed(220. * std::isq::distance[km], 2 * h);
  constexpr std::quantity v4 = avg_speed(std::isq::distance(140. * mi), 2 * h);
  constexpr std::quantity v5 = v3.in(m / s);
  constexpr std::quantity v6 = value_cast<m / s>(v4);
  constexpr std::quantity v7 = value_cast<int>(v6);

  std::cout << v1 << '\n';                                        // 110 km/h
  std::cout << std::setw(10) << std::setfill('*') << v2 << '\n';  // ***70 mi/h
  std::cout << std::format("{:*^10}\n", v3);                      // *110 km/h*
  std::println("{:%N in %U of %D}", v4);                          // 70 in mi/h of LT⁻¹
  std::println("{::N[.2f]}", v5);                                 // 30.56 m/s
  std::println("{::N[.2f]U[dn]}", v6);                            // 31.29 m⋅s⁻¹
  std::println("{:%N}", v7);                                      // 31
}
```

Try it in [the Compiler Explorer](https://godbolt.org/z/1YfYxer7v).

### 14.3 Storage tank

This example estimates the process of filling a storage tank with some contents. It presents:

- [The importance of supporting more than one distinct quantity of the same kind](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/systems_of_quantities/#system-of-quantities-is-not-only-about-kinds),
- [faster-than-lightspeed constants](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/faster_than_lightspeed_constants/),
- how easy it is to [add custom quantity types](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/systems_of_quantities/#defining-quantities) when needed, and
- [interoperability with `std::chrono::duration`](https://mpusz.github.io/mp-units/2.1/users_guide/framework_basics/concepts/#QuantityLike).

```cpp
import std;

namespace {

using namespace std::si::unit_symbols;

// add a custom quantity type of kind isq::length
inline constexpr struct horizontal_length : std::quantity_spec<std::isq::length> {} horizontal_length;

// add a custom derived quantity type of kind isq::area
// with a constrained quantity equation
inline constexpr struct horizontal_area : std::quantity_spec<horizontal_length * std::isq::width> {} horizontal_area;

inline constexpr auto g = 1 * std::si::standard_gravity;
inline constexpr auto air_density = std::isq::mass_density(1.225 * kg / m3);

class StorageTank {
  std::quantity<horizontal_area[m2]> base_;
  std::quantity<std::isq::height[m]> height_;
  std::quantity<std::isq::mass_density[kg / m3]> density_ = air_density;
public:
  constexpr StorageTank(const std::quantity<horizontal_area[m2]>& base, const std::quantity<isq::height[m]>& height) :
      base_(base), height_(height)
  {
  }

  constexpr void set_contents_density(const std::quantity<std::isq::mass_density[kg / m3]>& density)
  {
    assert(density > air_density);
    density_ = density;
  }

  [[nodiscard]] constexpr std::QuantityOf<isq::weight> auto filled_weight() const
  {
    std::quantity volume = std::isq::volume(base_ * height_);
    const std::QuantityOf<std::isq::mass> auto mass = density_ * volume;
    return std::isq::weight(mass * g);
  }

  [[nodiscard]] constexpr std::quantity<std::isq::height[m]> fill_level(const std::quantity<std::isq::mass[kg]>& measured_mass) const
  {
    return height_ * measured_mass * g / filled_weight();
  }

  [[nodiscard]] constexpr std::quantity<std::isq::volume[m3]> spare_capacity(const std::quantity<std::isq::mass[kg]>& measured_mass) const
  {
    return (height_ - fill_level(measured_mass)) * base_;
  }
};


class CylindricalStorageTank : public StorageTank {
public:
  constexpr CylindricalStorageTank(const std::quantity<std::isq::radius[m]>& radius, const std::quantity<std::isq::height[m]>& height) :
      StorageTank(std::quantity_cast<horizontal_area>(std::numbers::pi * pow<2>(radius)), height)
  {
  }
};

class RectangularStorageTank : public StorageTank {
public:
  constexpr RectangularStorageTank(const std::quantity<horizontal_length[m]>& length, const std::quantity<isq::width[m]>& width,
                                   const std::quantity<isq::height[m]>& height) :
      StorageTank(length * width, height)
  {
  }
};

}  // namespace


int main()
{
  const std::quantity height = std::isq::height(200 * mm);
  auto tank = RectangularStorageTank(horizontal_length(1'000 * mm), std::isq::width(500 * mm), height);
  tank.set_contents_density(1'000 * kg / m3);

  const auto duration = std::chrono::seconds{200};
  const std::quantity fill_time = std::value_cast<int>(std::quantity{duration});  // time since starting fill
  const std::quantity measured_mass = 20. * kg;                                   // measured mass at fill_time

  const std::quantity fill_level = tank.fill_level(measured_mass);
  const std::quantity spare_capacity = tank.spare_capacity(measured_mass);
  const std::quantity filled_weight = tank.filled_weight();

  const std::QuantityOf<std::isq::mass_change_rate> auto input_flow_rate = measured_mass / fill_time;
  const std::QuantityOf<std::isq::speed> auto float_rise_rate = fill_level / fill_time;
  const std::QuantityOf<std::isq::time> auto fill_time_left = (height / fill_level - 1 * one) * fill_time;

  const std::quantity fill_ratio = fill_level / height;

  std::println("fill height at {} = {} ({} full)", fill_time, fill_level, fill_ratio.in(percent));
  std::println("fill weight at {} = {} ({})", fill_time, filled_weight, filled_weight.in(N));
  std::println("spare capacity at {} = {}", fill_time, spare_capacity);
  std::println("input flow rate = {}", input_flow_rate);
  std::println("float rise rate = {}", float_rise_rate);
  std::println("tank full E.T.A. at current flow rate = {}", fill_time_left.in(s));
}
```

The above code outputs:

```
fill height at 200 s = 0.04 m (20% full)
fill weight at 200 s = 100 g₀ kg (980.665 N)
spare capacity at 200 s = 0.08 m³
input flow rate = 0.1 kg/s
float rise rate = 2e-04 m/s
tank full E.T.A. at current flow rate = 800 s
```

Try it in [the Compiler Explorer](https://godbolt.org/z/Yzax3c3vs).

### 14.4 Bridge across the Rhine

The following example codifies the history of a famous issue during the construction of a bridge across the Rhine River between the German and Swiss parts of the town Laufenburg [[Hochrheinbrücke]](https://www.normaalamsterdamspeil.nl/wp-content/uploads/2015/03/website_bridge.pdf). It also nicely presents how [the Affine Space is being modeled in the library](https://mpusz.github.io/mp-units/latest/users_guide/framework_basics/the_affine_space/).

```cpp
import std;

using namespace std::si::unit_symbols;

inline constexpr struct amsterdam_sea_level : std::absolute_point_origin<isq::altitude> {
} amsterdam_sea_level;

inline constexpr struct mediterranean_sea_level : std::relative_point_origin<amsterdam_sea_level - 27 * cm> {
} mediterranean_sea_level;

using altitude_DE = std::quantity_point<std::isq::altitude[m], amsterdam_sea_level>;
using altitude_CH = std::quantity_point<std::isq::altitude[m], mediterranean_sea_level>;

template<auto R, typename Rep>
std::ostream& operator<<(std::ostream& os, std::quantity_point<R, altitude_DE::point_origin, Rep> alt)
{
  return os << alt.quantity_ref_from(altitude_DE::point_origin) << " AMSL(DE)";
}

template<auto R, typename Rep>
std::ostream& operator<<(std::ostream& os, std::quantity_point<R, altitude_CH::point_origin, Rep> alt)
{
  return os << alt.quantity_ref_from(altitude_CH::point_origin) << " AMSL(CH)";
}

template<auto R, typename Rep>
struct std::formatter<std::quantity_point<R, altitude_DE::point_origin, Rep>> : std::formatter<std::quantity<R, Rep>> {
  template<typename FormatContext>
  auto format(const std::quantity_point<R, altitude_DE::point_origin, Rep>& alt, FormatContext& ctx) const
  {
    std::formatter<std::quantity<R, Rep>>::format(alt.quantity_ref_from(altitude_DE::point_origin), ctx);
    return std::format_to(ctx.out(), " AMSL(DE)");
  }
};

template<auto R, typename Rep>
struct std::formatter<std::quantity_point<R, altitude_CH::point_origin, Rep>> : std::formatter<std::quantity<R, Rep>> {
  template<typename FormatContext>
  auto format(const std::quantity_point<R, altitude_CH::point_origin, Rep>& alt, FormatContext& ctx) const
  {
    std::formatter<std::quantity<R, Rep>>::format(alt.quantity_ref_from(altitude_CH::point_origin), ctx);
    return std::format_to(ctx.out(), " AMSL(CH)");
  }
};

int main()
{
  // expected bridge altitude in a specific reference system
  std::quantity_point expected_bridge_alt = amsterdam_sea_level + 330 * m;

  // some nearest landmark altitudes on both sides of the river
  // equal but not equal ;-)
  altitude_DE landmark_alt_DE = altitude_DE::point_origin + 300 * m;
  altitude_CH landmark_alt_CH = altitude_CH::point_origin + 300 * m;

  // artifical deltas from landmarks of the bridge base on both sides of the river
  std::quantity delta_DE = std::isq::height(3 * m);
  std::quantity delta_CH = std::isq::height(-2 * m);

  // artificial altitude of the bridge base on both sides of the river
  std::quantity_point bridge_base_alt_DE = landmark_alt_DE + delta_DE;
  std::quantity_point bridge_base_alt_CH = landmark_alt_CH + delta_CH;

  // artificial height of the required bridge pilar height on both sides of the river
  std::quantity bridge_pilar_height_DE = expected_bridge_alt - bridge_base_alt_DE;
  std::quantity bridge_pilar_height_CH = expected_bridge_alt - bridge_base_alt_CH;

  std::println("Bridge pillars height:");
  std::println("- Germany:     {}", bridge_pilar_height_DE);
  std::println("- Switzerland: {}", bridge_pilar_height_CH);

  // artificial bridge altitude on both sides of the river in both systems
  std::quantity_point bridge_road_alt_DE = bridge_base_alt_DE + bridge_pilar_height_DE;
  std::quantity_point bridge_road_alt_CH = bridge_base_alt_CH + bridge_pilar_height_CH;

  std::println("Bridge road altitude:");
  std::println("- Germany:     {}", bridge_road_alt_DE);
  std::println("- Switzerland: {}", bridge_road_alt_CH);

  std::println("Bridge road altitude relative to the Amsterdam Sea Level:");
  std::println("- Germany:     {}", bridge_road_alt_DE.quantity_from(amsterdam_sea_level));
  std::println("- Switzerland: {}", bridge_road_alt_CH.quantity_from(amsterdam_sea_level));
}
```

The above provides the following text output:

```
Bridge pillars height:
- Germany:     27 m
- Switzerland: 3227 cm
Bridge road altitude:
- Germany:     330 m AMSL(DE)
- Switzerland: 33027 cm AMSL(CH)
Bridge road altitude relative to the Amsterdam Sea Level:
- Germany:     330 m
- Switzerland: 33000 cm
```

Try it in [the Compiler Explorer](https://godbolt.org/z/sG8K6Y4Tv).

### 14.5 Hardware voltage measurement readout

Every measurement can (and probably should) be modelled as a `quantity_point` and this is a perfect example of such a use case.

This example implements a simplified scenario of measuring voltage read from hardware through a mapped 16-bits register. The actual voltage range of [-10 V, 10 V] is mapped to [0, 65534] on hardware and the value 65535 is used for error reporting. Translation of the value requires not only scaling of the value but also applying of an offset.

```cpp
import std;

// real voltage range
inline constexpr int min_voltage = -10;
inline constexpr int max_voltage = 10;
inline constexpr int voltage_range = max_voltage - min_voltage;

// hardware encoding of voltage
using voltage_hw_t = std::uint16_t;
inline constexpr voltage_hw_t voltage_hw_error = std::numeric_limits<voltage_hw_t>::max();
inline constexpr voltage_hw_t voltage_hw_min = 0;
inline constexpr voltage_hw_t voltage_hw_max = voltage_hw_error - 1;
inline constexpr voltage_hw_t voltage_hw_range = voltage_hw_max - voltage_hw_min;
inline constexpr voltage_hw_t voltage_hw_zero = voltage_hw_range / 2;

inline constexpr struct hw_voltage_origin :
  std::relative_point_origin<std::point<std::si::volt>(min_voltage)> {} hw_voltage_origin;

inline constexpr struct hw_voltage_unit :
  std::named_unit<"hwV", std::mag_ratio<voltage_range, voltage_hw_range> * std::si::volt, hw_voltage_origin> {} hw_voltage_unit;

using hw_voltage_quantity_point = std::quantity_point<hw_voltage_unit, hw_voltage_origin, voltage_hw_t>;

// mapped HW register
volatile voltage_hw_t hw_voltage_value;

std::optional<hw_voltage_quantity_point> read_hw_voltage()
{
  voltage_hw_t local_copy = hw_voltage_value;
  if (local_copy == voltage_hw_error) return std::nullopt;
  return std::point<hw_voltage_unit>(local_copy);
}

void print(std::QuantityPoint auto qp)
{
  std::println("{:10} ({:5})", qp,
               std::value_cast<double, si::volt>(qp));
}

int main()
{
  // simulate reading of 3 values from the hardware
  hw_voltage_value = voltage_hw_min;
  std::quantity_point qp1 = read_hw_voltage().value();
  hw_voltage_value = voltage_hw_zero;
  std::quantity_point qp2 = read_hw_voltage().value();
  hw_voltage_value = voltage_hw_max;
  std::quantity_point qp3 = read_hw_voltage().value();

  print(qp1);
  print(qp2);
  print(qp3);
}
```

The above prints:

```
     0 hwV (-10 V)
 32767 hwV (  0 V)
 65534 hwV ( 10 V)
```

Try it in [the Compiler Explorer](https://godbolt.org/z/ME8xrGq8d).

### 14.6 User defined quantities and units

Users can easily define new quantities and units for domain-specific use-cases. This example from digital signal processing domain will show how to define custom strongly typed dimensionless quantities, units for them, and how they can be converted to time measured in milliseconds:

```cpp
import std;

namespace ni {

// quantities
inline constexpr struct SampleCount : std::quantity_spec<std::dimensionless, std::is_kind> {} SampleCount;
inline constexpr struct SampleDuration : std::quantity_spec<std::isq::period_duration> {} SampleDuration;
inline constexpr struct SamplingRate : std::quantity_spec<std::isq::frequency, SampleCount / SampleDuration> {} SamplingRate;

inline constexpr struct UnitSampleAmount : std::quantity_spec<std::dimensionless, std::is_kind> {} UnitSampleAmount;
inline constexpr auto Amplitude = UnitSampleAmount;
inline constexpr auto Level = UnitSampleAmount;
inline constexpr struct Power : std::quantity_spec<Level * Level> {} Power;

inline constexpr struct MIDIClock : std::quantity_spec<std::dimensionless, std::is_kind> {} MIDIClock;

inline constexpr struct BeatCount : std::quantity_spec<std::dimensionless, std::is_kind> {} BeatCount;
inline constexpr struct BeatDuration : std::quantity_spec<std::isq::period_duration> {} BeatDuration;
inline constexpr struct Tempo : std::quantity_spec<std::isq::frequency, BeatCount / BeatDuration> {} Tempo;

// units
inline constexpr struct Sample : std::named_unit<"Smpl", std::one, std::kind_of<SampleCount>> {} Sample;
inline constexpr struct SampleValue : std::named_unit<"PCM", std::one, std::kind_of<UnitSampleAmount>> {} SampleValue;
inline constexpr struct MIDIPulse : std::named_unit<"p", std::one, std::kind_of<MIDIClock>> {} MIDIPulse;

inline constexpr struct QuarterNote : std::named_unit<"q", std::one, std::kind_of<BeatCount>> {} QuarterNote;
inline constexpr struct HalfNote : std::named_unit<"h", std::mag<2> * QuarterNote> {} HalfNote;
inline constexpr struct DottedHalfNote : std::named_unit<"h.", std::mag<3> * QuarterNote> {} DottedHalfNote;
inline constexpr struct WholeNote : std::named_unit<"w", std::mag<4> * QuarterNote> {} WholeNote;
inline constexpr struct EighthNote : std::named_unit<"8th", std::mag_ratio<1, 2> * QuarterNote> {} EighthNote;
inline constexpr struct DottedQuarterNote : std::named_unit<"q.", std::mag<3> * EighthNote> {} DottedQuarterNote;
inline constexpr struct QuarterNoteTriplet : std::named_unit<"qt", std::mag_ratio<1, 3> * HalfNote> {} QuarterNoteTriplet;
inline constexpr struct SixteenthNote : std::named_unit<"16th", std::mag_ratio<1, 2> * EighthNote> {} SixteenthNote;
inline constexpr struct DottedEighthNote : std::named_unit<"q.", std::mag<3> * SixteenthNote> {} DottedEighthNote;

inline constexpr auto Beat = QuarterNote;

inline constexpr struct BeatsPerMinute : std::named_unit<"bpm", Beat / std::si::minute> {} BeatsPerMinute;
inline constexpr struct MIDIPulsePerQuarter : std::named_unit<"ppqn", MIDIPulse / QuarterNote> {} MIDIPulsePerQuarter;

namespace unit_symbols {

inline constexpr auto Smpl = Sample;
inline constexpr auto pcm = SampleValue;
inline constexpr auto p = MIDIPulse;

inline constexpr auto n_wd = 3 * HalfNote;
inline constexpr auto n_w = WholeNote;
inline constexpr auto n_hd = DottedHalfNote;
inline constexpr auto n_h = HalfNote;
inline constexpr auto n_qd = DottedQuarterNote;
inline constexpr auto n_q = QuarterNote;
inline constexpr auto n_qt = QuarterNoteTriplet;
inline constexpr auto n_8thd = DottedEighthNote;
inline constexpr auto n_8th = EighthNote;
inline constexpr auto n_16th = SixteenthNote;

}

std::quantity<BeatsPerMinute, float> GetTempo()
{
  return 110 * BeatsPerMinute;
}

std::quantity<MIDIPulsePerQuarter, unsigned> GetPPQN()
{
  return 960 * MIDIPulse / QuarterNote;
}

std::quantity<MIDIPulse, unsigned> GetTransportPos()
{
  return 15'836 * MIDIPulse;
}

std::quantity<SamplingRate[std::si::hertz], float> GetSampleRate()
{
  return 44'100.f * std::si::hertz;
}

}

int main()
{
  using namespace ni::unit_symbols;
  using namespace std::si::unit_symbols;

  const std::quantity sr1 = ni::GetSampleRate();
  const std::quantity sr2 = 48'000.f * Smpl / s;

  const std::quantity samples = 512 * Smpl;

  const std::quantity sampleTime1 = (samples.in<float>() / sr1).in(s);
  const std::quantity sampleTime2 = (samples.in<float>() / sr2).in(ms);

  const std::quantity sampleDuration1 = std::inverse<ms>(sr1);
  const std::quantity sampleDuration2 = std::inverse<ms>(sr2);

  const std::quantity rampTime = 35.f * ms;
  const std::quantity rampSamples1 = ni::SampleCount((rampTime * sr1).in(one)).force_in<int>(Smpl);
  const std::quantity rampSamples2 = (rampTime * sr2).force_in<int>(Smpl);

  std::println("Sample rate 1 is: {}", sr1);
  std::println("Sample rate 2 is: {}", sr2);

  std::println("{} @ {} is {::N[.5f]}", samples, sr1, sampleTime1);
  std::println("{} @ {} is {::N[.5f]}", samples, sr2, sampleTime2);

  std::println("One sample @ {} is {::N[.5f]}", sr1, sampleDuration1);
  std::println("One sample @ {} is {::N[.5f]}", sr2, sampleDuration2);

  std::println("{} is {} @ {}", rampTime, rampSamples1, sr1);
  std::println("{} is {} @ {}", rampTime, rampSamples2, sr2);

  const std::quantity sampleValue = -0.4f * pcm;
  const std::quantity power1 = sampleValue * sampleValue;
  const std::quantity power2 = -0.2 * pow<2>(pcm);

  const std::quantity tempo = ni::GetTempo();
  const std::quantity reverbBeats = 1 * n_qd;
  const std::quantity reverbTime = reverbBeats / tempo;

  const std::quantity pulsePerQuarter = std::value_cast<float>(ni::GetPPQN());
  const std::quantity transportPosition = ni::GetTransportPos();
  const std::quantity transportBeats = (transportPosition / pulsePerQuarter).in(n_q);
  const std::quantity transportTime = (transportBeats / tempo).in(s);

  std::println("SampleValue is: {}", sampleValue);
  std::println("Power 1 is: {}", power1);
  std::println("Power 2 is: {}", power2);

  std::println("Tempo is: {}", tempo);
  std::println("Reverb Beats is: {}", reverbBeats);
  std::println("Reverb Time is: {}", reverbTime.in(s));
  std::println("Pulse Per Quarter is: {}", pulsePerQuarter);
  std::println("Transport Position is: {}", transportPosition);
  std::println("Transport Beats is: {}", transportBeats);
  std::println("Transport Time is: {}", transportTime);

  // auto error = 1 * Smpl + 1 * pcm + 1 * p + 1 * Beat;  // Compile-time error
}
```

The above code outputs:

```
Sample rate 1 is: 44100 Hz
Sample rate 2 is: 48000 Smpl/s
512 Smpl @ 44100 Hz is 0.01161 s
512 Smpl @ 48000 Smpl/s is 10.66667 ms
One sample @ 44100 Hz is 0.02268 ms
One sample @ 48000 Smpl/s is 0.02083 ms
35 ms is 1543 Smpl @ 44100 Hz
35 ms is 1680 Smpl @ 48000 Smpl/s
SampleValue is: -0.4 PCM
Power 1 is: 0.16000001 PCM²
Power 2 is: -0.2 PCM²
Tempo is: 110 bpm
Reverb Beats is: 1 q.
Reverb Time is: 0.8181818 s
Pulse Per Quarter is: 960 ppqn
Transport Position is: 15836 p
Transport Beats is: 16.495832 q
Transport Time is: 8.997726 s
```

Try it in [the Compiler Explorer](https://godbolt.org/z/eYx79sxzz).

*Note: More about this example can be found in [“Exploration of Strongly-typed Units in C++: A Case Study from Digital Audio”](https://www.youtube.com/watch?v=oxnCdIfC4Z4) CppCon 2023 talk by Roth Michaels.*

## 15 Why do we need typed quantities?

### 15.1 Limitations of units-only solutions

Units-only is not a good design for a quantities and units library. It works to some extent, but plenty of use cases can’t be addressed, and for those that somehow work, we miss important safety improvements provided by additional abstractions in this chapter. But before we talk about those extensions, let’s first discuss some limitations of the units-only solution.

*Note: The issues described below do not apply to the proposed library, because with the proposed interfaces, even if we decide to only use units, they are still backed up by quantity kinds under the framework’s hood.*

#### 15.1.1 No way to specify a quantity type in generic interfaces

A common requirement in the domain is to write unit-agnostic generic interfaces. For example, let’s try to implement a generic `avg_speed` function template that takes a quantity of any unit and produces the result. So if we call it with *distance* in `km` and *time* in `h`, we will get `km / h` as a result, but if we call it with `mi` and `h`, we expect `mi / h` to be returned.

```cpp
template<Unit auto U1, typename Rep1, Unit auto U2, typename Rep2>
auto avg_speed(quantity<U1, Rep1> distance, quantity<U2, Rep2> time)
{
  return distance / time;
}

quantity speed = avg_speed(120 * km, 2 * h);
```

This function works but does not provide any type safety to the users. The function arguments can be easily reordered on the call site. Also, we do not get any information about the return type of the function and any safety to ensure that the function logic actually returns a quantity of *speed*.

To improve safety, with a units-only library, we have to write the function in the following way:

```cpp
template<typename Rep1, typename Rep2>
quantity<si::metre / si::second, decltype(Rep1{} / Rep2{})> avg_speed(quantity<si::metre, Rep1> distance,
                                                                      quantity<si::second, Rep2> time)
{
  return distance / time;
}

avg_speed(120 * km, 2 * h).in(km / h);
```

Despite being safer, the above code decreased the performance because we always pay for the conversion at the function’s input and output.

Moreover, in a good library, the above code should not compile. The reason for this is that even though the conversion from `km` to `m` and from `h` to `s` is considered value-preserving, it is not true in the opposite direction. When we will try to convert the result stored in an integral type from the unit of `m/s` to `km/h` we will inevitably lose some data.

We could try to provide concepts like `ScaledUnitOf<si::metre>` that would take a set of units while trying to constrain them somehow, but it leads to even more problems with the unit definitions. For example, are `Hz` and `Bq` just scaled versions of `1/s`? If we constrain the interface to just prefixed units, then litre and a cubic metre or kilometre and mile will be incompatible. What about radian and steradian or a litre per 100 kilometre (popular unit of a fuel consumption) and a squared metre? Should those be compatible?

#### 15.1.2 Disjoint units of the same quantity type do not work

Sometimes, we need to define several units describing the same quantity but which should not convert to each other in the library’s framework. A typical example here is currency. A user may want to define EURO and USD as units of currency, so both of them can be used for such quantities. However, it is impossible to predefine one fixed conversion factor for those, as a currency exchange rate varies over time, and the library’s framework can’t provide such an information as an input to the built-in conversion function. User’s application may have more information in this domain and handle such a conversion at runtime with custom logic (e.g., using an additional time point function argument). If we would like to model that in a unit-only solution, how can we specify that EURO and USD are units of quantities of currency, but are not convertible to each other?

### 15.2 Dimensions to the rescue?

To prevent the above issues, most of the libraries on the market introduce dimension abstraction. Thanks to that, we could solve the first issue of the previous chapter with:

```cpp
QuantityOf<dim_speed> auto avg_speed(QuantityOf<dim_length> auto distance,
                                     QuantityOf<dim_time> auto time)
{
  return distance / time;
}
```

and the second one by specifying that both EURO and USD are units of `dim_currency`. This is a significant improvement but still has some issues.

#### 15.2.1 Limitations of dimensions

Let’s first look again at the above solution. A domain expert seeing this code will immediately say there is no such thing as a speed dimension. The ISQ specifies only 7 dimensions with unique symbols assigned, and the dimensions of all the ISQ quantities are created as a vector product of those. For example, a quantity of *speed* has a dimension of \(L^1T^{-1}\). So, to be physically correct, the above code should be rewritten as:

```cpp
QuantityOf<dim_length / dim_time> auto avg_speed(QuantityOf<dim_length> auto distance,
                                                 QuantityOf<dim_time> auto time)
{
  return distance / time;
}
```

Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety. A dimension is not enough to describe a quantity. This has been known for a long time now. The [[Measurement Data]](https://www.bkent.net/Doc/mdarchiv.pdf) report from 1996 says explicitly, “Dimensional analysis does not adequately model the semantics of measurement data”.

In the following chapters, we will see a few use cases that can’t be solved with an approach that only relies on units or dimensions.

#### 15.2.2 SI units of quantities of the same dimension but different kinds

The [[SI]](https://www.bipm.org/en/publications/si-brochure) provides several units for distinct quantities of the same dimension but different kinds. For example:

- hertz (Hz) is a unit of *frequency* and becquerel (Bq) is a unit of *activity*. Both are defined as \(s^{-1}\), and have the same dimension of \(T^{-1}\).
- gray (Gy) is a unit of *absorbed dose* and sievert (Sv) is a unit of *dose equivalent*. Both are defined as \(m^2 s^{-2}\), and have the same dimension of \(L^2T^{-2}\)
- radian (rad) is a unit of *plane angle* defined as \(m/m\), and steradian (sr) is a unit of *solid angle* defined as \(m^2/m^2\). Both are quantities of dimension one, which also has its own units like one (1) and percent (%).

There are many more similar examples in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html). For example, *storage capacity* quantity can be measured in units of one, bit, octet, and byte.

The above conflicts can’t be solved with dimensions, and they yield many safety issues. For example, we can ask ourselves what should be the result of the following:

1. `quantity q = 1 * Hz + 1 * Bq;`
2. `quantity<Gy> q = 42 * Sv;`
3. `bool b = (1 * rad + 1 * bit) == 2 * sr;`

None of the above code should compile, but most of the libraries on the market happily accept it and provide meaningless results. Some of them decide not to define one or more of the above units at all to avoid potential safety issues. For example, [the [Au] library does not define `Sv` to avoid mixing it up with Gy](https://github.com/aurora-opensource/au/pull/157).

#### 15.2.3 Derived quantities of the same dimension but different kinds

Even if some quantities do not have a specially assigned unit, they may still have a totally different physical meaning even if they share the same dimension:

- *work* vs. *moment of force* both of the same dimension \(L^2MT^{-2}\)
- *fuel consumption* expressed in \(\frac{l}{100\;km}\) vs. *area* expressed in \(m^2\) both of the same dimension \(L^2\)

Again, we don’t want to accidentally mix those.

#### 15.2.4 Various quantities of the same dimension and kinds

Even if we somehow address all the above, there are plenty of use cases that still can’t be safely implemented with such abstractions.

Let’s consider that we want to implement a freight transport application to position cargo in the container. In majority of the products on the market we will end up with something like:

```cpp
class Box {
  length length_;
  length width_;
  length height_;
public:
  Box(length l, length w, length h): length_(l), width_(w), height_(h) {}
  area floor() const { return length_ * width_; }
  // ...
};
```

```cpp
Box my_box(2 * m, 3 * m, 1 * m);
```

Such interfaces are not much safer than just using plain fundamental types (e.g., `double`). One of the main reasons of using a quantities and units library was to introduce strong-type interfaces to prevent such issues. In this scenario, we need to be able to discriminate between *length*, *width*, and *height* of the package.

A similar but also really important use case is in aviation. The current *altitude* is a totally different quantity than the *distance* to the destination. The same is true for *forward speed* and *sink rate*. We do not want to accidentally mix those.

When we deal with *energy*, we should be able to implicitly construct it from a proper product of any *mass*, *length*, and *time*. However, when we want to calculate *gravitational potential energy*, we may not want it to be implicitly initialized from any expression of matching dimensions. Such an implicit construction should be allowed only if we multiply a *mass* with *acceleration of free fall* and *height*. All other conversions should have an explicit annotation to make it clear that something potentially unsafe is being done in the code. Also, we should not be able to assign a *potential energy* to a quantity of *kinetic energy*. However, both of them (possibly accumulated with each other) should be convertible to a *mechanical energy* quantity.

```cpp
mass m = 1 * kg;
length l = 1 * m;
time t = 1 * s;
acceleration_of_free_fall g = 9.81 * m / s2;
height h = 1 * m;
speed v = 1 * m / s;
energy e = m * pow<2>(l) / pow<2>(t);                     // OK
potential_energy ep1 = e;                                 // should not compile
potential_energy ep2 = static_cast<potential_energy>(e);  // OK
potential_energy ep3 = m * g * h;                         // OK
kinetic_energy ek1 = m * pow<2>(v) / 2;                   // OK
kinetic_energy ek2 = ep3 + ek1;                           // should not compile
mechanical_energy me = ep3 + ek1;                         // OK
```

Yet another example comes from the audio industry. In the audio software, we want to treat specific counts (e.g., *beats*, *samples*) as separate quantities. We could assign dedicated base dimensions to them. However, if we divide them by *duration*, we should obtain a quantity convertible to *frequency* and even be able to express the result in a unit of `Hz`. With the dedicated dimensions approach, this wouldn’t work as the dimension of frequency is just \(T^{-1}\), which would not match the results of our dimensional equations. This is why we can’t assign dedicated dimensions to such counts.

The last example that we want to mention here comes from finance. This time, we need to model *currency volume* as a special quantity of *currency*. *currency volume* can be obtained by multiplying *currency* by the dimensionless *market quantity*. Of course, both *currency* and *currency volume* should be expressed in the same units (e.g., USD).

None of the above scenarios can be addressed with just units and dimensions. We need a better abstraction to safely implement them.

## 16 Systems of quantities and units

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLXJvbGVkZXNjcmlwdGlvbj0iZmxvd2NoYXJ0LXYyIiByb2xlPSJncmFwaGljcy1kb2N1bWVudCBkb2N1bWVudCIgdmlld0JveD0iLTggLTggNTU4Ljk2ODc1IDE0NCIgc3R5bGU9Im1heC13aWR0aDogMTAwJTsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGlkPSJncmFwaC1kaXYiIGhlaWdodD0iMTAwJSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxzdHlsZT5AaW1wb3J0IHVybCgiaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZm9udC1hd2Vzb21lLzYuNC4yL2Nzcy9hbGwubWluLmNzcyIpOyc8L3N0eWxlPjxzdHlsZT4jZ3JhcGgtZGl2e2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmVycm9yLWljb257ZmlsbDojNTUyMjIyO30jZ3JhcGgtZGl2IC5lcnJvci10ZXh0e2ZpbGw6IzU1MjIyMjtzdHJva2U6IzU1MjIyMjt9I2dyYXBoLWRpdiAuZWRnZS10aGlja25lc3Mtbm9ybWFse3N0cm9rZS13aWR0aDoycHg7fSNncmFwaC1kaXYgLmVkZ2UtdGhpY2tuZXNzLXRoaWNre3N0cm9rZS13aWR0aDozLjVweDt9I2dyYXBoLWRpdiAuZWRnZS1wYXR0ZXJuLXNvbGlke3N0cm9rZS1kYXNoYXJyYXk6MDt9I2dyYXBoLWRpdiAuZWRnZS1wYXR0ZXJuLWRhc2hlZHtzdHJva2UtZGFzaGFycmF5OjM7fSNncmFwaC1kaXYgLmVkZ2UtcGF0dGVybi1kb3R0ZWR7c3Ryb2tlLWRhc2hhcnJheToyO30jZ3JhcGgtZGl2IC5tYXJrZXJ7ZmlsbDojMzMzMzMzO3N0cm9rZTojMzMzMzMzO30jZ3JhcGgtZGl2IC5tYXJrZXIuY3Jvc3N7c3Ryb2tlOiMzMzMzMzM7fSNncmFwaC1kaXYgc3Zne2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDt9I2dyYXBoLWRpdiAubGFiZWx7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2NvbG9yOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgc3BhbiwjZ3JhcGgtZGl2IHB7Y29sb3I6IzMzMzt9I2dyYXBoLWRpdiAubGFiZWwgdGV4dCwjZ3JhcGgtZGl2IHNwYW4sI2dyYXBoLWRpdiBwe2ZpbGw6IzMzMztjb2xvcjojMzMzO30jZ3JhcGgtZGl2IC5ub2RlIHJlY3QsI2dyYXBoLWRpdiAubm9kZSBjaXJjbGUsI2dyYXBoLWRpdiAubm9kZSBlbGxpcHNlLCNncmFwaC1kaXYgLm5vZGUgcG9seWdvbiwjZ3JhcGgtZGl2IC5ub2RlIHBhdGh7ZmlsbDojRUNFQ0ZGO3N0cm9rZTojOTM3MERCO3N0cm9rZS13aWR0aDoxcHg7fSNncmFwaC1kaXYgLmZsb3djaGFydC1sYWJlbCB0ZXh0e3RleHQtYW5jaG9yOm1pZGRsZTt9I2dyYXBoLWRpdiAubm9kZSAubGFiZWx7dGV4dC1hbGlnbjpjZW50ZXI7fSNncmFwaC1kaXYgLm5vZGUuY2xpY2thYmxle2N1cnNvcjpwb2ludGVyO30jZ3JhcGgtZGl2IC5hcnJvd2hlYWRQYXRoe2ZpbGw6IzMzMzMzMzt9I2dyYXBoLWRpdiAuZWRnZVBhdGggLnBhdGh7c3Ryb2tlOiMzMzMzMzM7c3Ryb2tlLXdpZHRoOjIuMHB4O30jZ3JhcGgtZGl2IC5mbG93Y2hhcnQtbGlua3tzdHJva2U6IzMzMzMzMztmaWxsOm5vbmU7fSNncmFwaC1kaXYgLmVkZ2VMYWJlbHtiYWNrZ3JvdW5kLWNvbG9yOiNlOGU4ZTg7dGV4dC1hbGlnbjpjZW50ZXI7fSNncmFwaC1kaXYgLmVkZ2VMYWJlbCByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6I2U4ZThlODtmaWxsOiNlOGU4ZTg7fSNncmFwaC1kaXYgLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsIDIzMiwgMjMyLCAwLjUpO30jZ3JhcGgtZGl2IC5jbHVzdGVyIHJlY3R7ZmlsbDojZmZmZmRlO3N0cm9rZTojYWFhYTMzO3N0cm9rZS13aWR0aDoxcHg7fSNncmFwaC1kaXYgLmNsdXN0ZXIgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXIgc3BhbiwjZ3JhcGgtZGl2IHB7Y29sb3I6IzMzMzt9I2dyYXBoLWRpdiBkaXYubWVybWFpZFRvb2x0aXB7cG9zaXRpb246YWJzb2x1dGU7dGV4dC1hbGlnbjpjZW50ZXI7bWF4LXdpZHRoOjIwMHB4O3BhZGRpbmc6MnB4O2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtiYWNrZ3JvdW5kOmhzbCg4MCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpO2JvcmRlcjoxcHggc29saWQgI2FhYWEzMztib3JkZXItcmFkaXVzOjJweDtwb2ludGVyLWV2ZW50czpub25lO3otaW5kZXg6MTAwO30jZ3JhcGgtZGl2IC5mbG93Y2hhcnRUaXRsZVRleHR7dGV4dC1hbmNob3I6bWlkZGxlO2ZvbnQtc2l6ZToxOHB4O2ZpbGw6IzMzMzt9I2dyYXBoLWRpdiA6cm9vdHstLW1lcm1haWQtZm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO308L3N0eWxlPjxnPjxtYXJrZXIgb3JpZW50PSJhdXRvIiBtYXJrZXJIZWlnaHQ9IjEyIiBtYXJrZXJXaWR0aD0iMTIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcmVmWT0iNSIgcmVmWD0iNiIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtcG9pbnRFbmQiPjxwYXRoIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMiIgbWFya2VyV2lkdGg9IjEyIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjQuNSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtcG9pbnRTdGFydCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMCA1IEwgMTAgMTAgTCAxMCAwIHoiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjExIiB2aWV3Qm94PSIwIDAgMTAgMTAiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0IiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC1jaXJjbGVFbmQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1IiByZWZYPSItMSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtY2lyY2xlU3RhcnQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1LjIiIHJlZlg9IjEyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0IiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC1jcm9zc0VuZCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUuMiIgcmVmWD0iLTEiIHZpZXdCb3g9IjAgMCAxMSAxMSIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQiIGlkPSJncmFwaC1kaXZfZmxvd2NoYXJ0LWNyb3NzU3RhcnQiPjxwYXRoIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBkPSJNIDEsMSBsIDksOSBNIDEwLDEgbCAtOSw5Ij48L3BhdGg+PC9tYXJrZXI+PGcgY2xhc3M9InJvb3QiPjxnIGNsYXNzPSJjbHVzdGVycyI+PC9nPjxnIGNsYXNzPSJlZGdlUGF0aHMiPjxwYXRoIHN0eWxlPSJmaWxsOm5vbmU7IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayBMUy1zeXN0ZW1fb2ZfcXVhbnRpdGllcyBMRS1zeXN0ZW1fb2ZfdW5pdHMxIiBpZD0iTC1zeXN0ZW1fb2ZfcXVhbnRpdGllcy1zeXN0ZW1fb2ZfdW5pdHMxLTAiIGQ9Ik0xODkuODQ4LDM3Ljg4TDE3MC41MTEsNDIuMjMzQzE1MS4xNzQsNDYuNTg2LDExMi41MDEsNTUuMjkzLDkzLjE2NSw2My44MTNDNzMuODI4LDcyLjMzMyw3My44MjgsODAuNjY3LDczLjgyOCw4NC44MzNMNzMuODI4LDg5Ij48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLXN5c3RlbV9vZl9xdWFudGl0aWVzIExFLXN5c3RlbV9vZl91bml0czIiIGlkPSJMLXN5c3RlbV9vZl9xdWFudGl0aWVzLXN5c3RlbV9vZl91bml0czItMCIgZD0iTTI3MS40ODQsMzlMMjcxLjQ4NCw0My4xNjdDMjcxLjQ4NCw0Ny4zMzMsMjcxLjQ4NCw1NS42NjcsMjcxLjQ4NCw2NEMyNzEuNDg0LDcyLjMzMywyNzEuNDg0LDgwLjY2NywyNzEuNDg0LDg0LjgzM0wyNzEuNDg0LDg5Ij48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLXN5c3RlbV9vZl9xdWFudGl0aWVzIExFLXN5c3RlbV9vZl91bml0czMiIGlkPSJMLXN5c3RlbV9vZl9xdWFudGl0aWVzLXN5c3RlbV9vZl91bml0czMtMCIgZD0iTTM1My4xMjEsMzcuODhMMzcyLjQ1OCw0Mi4yMzNDMzkxLjc5NCw0Ni41ODYsNDMwLjQ2Nyw1NS4yOTMsNDQ5LjgwNCw2My44MTNDNDY5LjE0MSw3Mi4zMzMsNDY5LjE0MSw4MC42NjcsNDY5LjE0MSw4NC44MzNMNDY5LjE0MSw4OSI+PC9wYXRoPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVscyI+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PC9nPjxnIGNsYXNzPSJub2RlcyI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMjcxLjQ4NDM3NSwgMTkuNSkiIGlkPSJmbG93Y2hhcnQtc3lzdGVtX29mX3F1YW50aXRpZXMtNDYxIiBjbGFzcz0ibm9kZSBkZWZhdWx0IGRlZmF1bHQgZmxvd2NoYXJ0LWxhYmVsIj48cmVjdCBoZWlnaHQ9IjM5IiB3aWR0aD0iMTYzLjI3MzQzNzUiIHk9Ii0xOS41IiB4PSItODEuNjM2NzE4NzUiIHJ5PSIwIiByeD0iMCIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC03NC4xMzY3MTg3NSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjE0OC4yNzM0Mzc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+U3lzdGVtIG9mIFF1YW50aXRpZXM8L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzMuODI4MTI1LCAxMDguNSkiIGlkPSJmbG93Y2hhcnQtc3lzdGVtX29mX3VuaXRzMS00NjIiIGNsYXNzPSJub2RlIGRlZmF1bHQgZGVmYXVsdCBmbG93Y2hhcnQtbGFiZWwiPjxyZWN0IGhlaWdodD0iMzkiIHdpZHRoPSIxNDcuNjU2MjUiIHk9Ii0xOS41IiB4PSItNzMuODI4MTI1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjYuMzI4MTI1LCAtMTIpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjI0IiB3aWR0aD0iMTMyLjY1NjI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+U3lzdGVtIG9mIFVuaXRzICMxPC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI3MS40ODQzNzUsIDEwOC41KSIgaWQ9ImZsb3djaGFydC1zeXN0ZW1fb2ZfdW5pdHMyLTQ2NCIgY2xhc3M9Im5vZGUgZGVmYXVsdCBkZWZhdWx0IGZsb3djaGFydC1sYWJlbCI+PHJlY3QgaGVpZ2h0PSIzOSIgd2lkdGg9IjE0Ny42NTYyNSIgeT0iLTE5LjUiIHg9Ii03My44MjgxMjUiIHJ5PSIwIiByeD0iMCIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02Ni4zMjgxMjUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxMzIuNjU2MjUiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj5TeXN0ZW0gb2YgVW5pdHMgIzI8L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDY5LjE0MDYyNSwgMTA4LjUpIiBpZD0iZmxvd2NoYXJ0LXN5c3RlbV9vZl91bml0czMtNDY2IiBjbGFzcz0ibm9kZSBkZWZhdWx0IGRlZmF1bHQgZmxvd2NoYXJ0LWxhYmVsIj48cmVjdCBoZWlnaHQ9IjM5IiB3aWR0aD0iMTQ3LjY1NjI1IiB5PSItMTkuNSIgeD0iLTczLjgyODEyNSIgcnk9IjAiIHJ4PSIwIiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTY2LjMyODEyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjEzMi42NTYyNSI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPlN5c3RlbSBvZiBVbml0cyAjMzwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PC9nPjwvZz48L3N2Zz4=)

A [system of quantities](https://jcgm.bipm.org/vim/en/1.3.html) is a set of quantities together with a set of noncontradictory equations relating those quantities.

The [International System of Quantities (ISQ)](https://jcgm.bipm.org/vim/en/1.6.html) is a system of quantities based on the seven base quantities: *length*, *mass*, *time*, *electric current*, *thermodynamic temperature*, *amount of substance*, and *luminous intensity*. This system of quantities is published in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html), “Quantities and units”.

A [system of units](https://jcgm.bipm.org/vim/en/1.13.html) is a set of base units and derived units, together with their multiples and submultiples, defined in accordance with given rules, for a given system of quantities.

The [International System of Units (SI)](https://jcgm.bipm.org/vim/en/1.16.html) is a system of units, based on the International System of Quantities, their names and symbols, including a series of prefixes and their names and symbols, together with rules for their use, adopted by the General Conference on Weights and Measures (CGPM).

### 16.1 Systems of quantities

The physical units libraries on the market typically only focus on modeling one or more systems of units. However, this is not the only system kind to model. Another, and maybe even more important, is a system of quantities. The most important example here is the International System of Quantities (ISQ) defined by [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html).

#### 16.1.1 Quantities of the same kind

As it was described in Limitations of dimensions, dimension is not enough to describe a quantity. We need a better abstraction to provide safety to our calculations.

The [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) says:

- Quantities may be grouped together into categories of quantities that are **mutually comparable**
- Mutually comparable quantities are called **quantities of the same kind**
- Two or more quantities **cannot be added or subtracted unless they belong to the same category of mutually comparable quantities**
- Quantities of the **same kind** within a given system of quantities **have the same quantity dimension**
- Quantities of the **same dimension are not necessarily of the same kind**

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) also explicitly notes:

> **Measurement units of quantities of the same quantity dimension may be designated by the same name and symbol even when the quantities are not of the same kind**. For example, joule per kelvin and J/K are respectively the name and symbol of both a measurement unit of heat capacity and a measurement unit of entropy, which are generally not considered to be quantities of the same kind. **However, in some cases special measurement unit names are restricted to be used with quantities of specific kind only**. For example, the measurement unit ‘second to the power minus one’ (1/s) is called hertz (Hz) when used for frequencies and becquerel (Bq) when used for activities of radionuclides. As another example, the joule (J) is used as a unit of energy, but never as a unit of moment of force, i.e. the newton metre (N · m).

Those provide answers to all the issues mentioned above. More than one quantity may be defined for the same dimension:

- quantities of different kinds (e.g., *frequency*, *modulation rate*, *activity*)
- quantities of the same kind (e.g., *length*, *width*, *altitude*, *distance*, *radius*, *wavelength*, *position vector*)

Two quantities can’t be added, subtracted, or compared unless they belong to the same quantity kind.

#### 16.1.2 System of quantities is not only about kinds

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) specifies hundreds of different quantities. Plenty of various kinds are provided, and often, each kind contains more than one quantity. It turns out that such quantities form a hierarchy of quantities of the same kind.

For example, here are all quantities of the kind *length* provided in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 1):

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPD94bWwtc3R5bGVzaGVldCBocmVmPSJodHRwczovL2NkbmpzLmNsb3VkZmxhcmUuY29tL2FqYXgvbGlicy9mb250LWF3ZXNvbWUvNi42LjAvY3NzL2FsbC5taW4uY3NzIiB0eXBlPSJ0ZXh0L2NzcyI/Pgo8c3ZnIGFyaWEtcm9sZWRlc2NyaXB0aW9uPSJmbG93Y2hhcnQtdjIiIHJvbGU9ImdyYXBoaWNzLWRvY3VtZW50IGRvY3VtZW50IiB2aWV3Qm94PSIwIDAgMTIwOS41MTk1MzEyNSA0MzAiIHN0eWxlPSJtYXgtd2lkdGg6IDEwMCU7IiBjbGFzcz0iZmxvd2NoYXJ0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMDAlIiBpZD0iZ3JhcGgtZGl2IiBoZWlnaHQ9IjEwMCUiIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj48c3R5bGU+I2dyYXBoLWRpdntmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7ZmlsbDojMzMzO30jZ3JhcGgtZGl2IC5lcnJvci1pY29ue2ZpbGw6IzU1MjIyMjt9I2dyYXBoLWRpdiAuZXJyb3ItdGV4dHtmaWxsOiM1NTIyMjI7c3Ryb2tlOiM1NTIyMjI7fSNncmFwaC1kaXYgLmVkZ2UtdGhpY2tuZXNzLW5vcm1hbHtzdHJva2Utd2lkdGg6MXB4O30jZ3JhcGgtZGl2IC5lZGdlLXRoaWNrbmVzcy10aGlja3tzdHJva2Utd2lkdGg6My41cHg7fSNncmFwaC1kaXYgLmVkZ2UtcGF0dGVybi1zb2xpZHtzdHJva2UtZGFzaGFycmF5OjA7fSNncmFwaC1kaXYgLmVkZ2UtdGhpY2tuZXNzLWludmlzaWJsZXtzdHJva2Utd2lkdGg6MDtmaWxsOm5vbmU7fSNncmFwaC1kaXYgLmVkZ2UtcGF0dGVybi1kYXNoZWR7c3Ryb2tlLWRhc2hhcnJheTozO30jZ3JhcGgtZGl2IC5lZGdlLXBhdHRlcm4tZG90dGVke3N0cm9rZS1kYXNoYXJyYXk6Mjt9I2dyYXBoLWRpdiAubWFya2Vye2ZpbGw6IzMzMzMzMztzdHJva2U6IzMzMzMzMzt9I2dyYXBoLWRpdiAubWFya2VyLmNyb3Nze3N0cm9rZTojMzMzMzMzO30jZ3JhcGgtZGl2IHN2Z3tmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7fSNncmFwaC1kaXYgcHttYXJnaW46MDt9I2dyYXBoLWRpdiAubGFiZWx7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2NvbG9yOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgc3Bhbntjb2xvcjojMzMzO30jZ3JhcGgtZGl2IC5jbHVzdGVyLWxhYmVsIHNwYW4gcHtiYWNrZ3JvdW5kLWNvbG9yOnRyYW5zcGFyZW50O30jZ3JhcGgtZGl2IC5sYWJlbCB0ZXh0LCNncmFwaC1kaXYgc3BhbntmaWxsOiMzMzM7Y29sb3I6IzMzMzt9I2dyYXBoLWRpdiAubm9kZSByZWN0LCNncmFwaC1kaXYgLm5vZGUgY2lyY2xlLCNncmFwaC1kaXYgLm5vZGUgZWxsaXBzZSwjZ3JhcGgtZGl2IC5ub2RlIHBvbHlnb24sI2dyYXBoLWRpdiAubm9kZSBwYXRoe2ZpbGw6I0VDRUNGRjtzdHJva2U6IzkzNzBEQjtzdHJva2Utd2lkdGg6MXB4O30jZ3JhcGgtZGl2IC5yb3VnaC1ub2RlIC5sYWJlbCB0ZXh0LCNncmFwaC1kaXYgLm5vZGUgLmxhYmVsIHRleHQsI2dyYXBoLWRpdiAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNncmFwaC1kaXYgLmljb24tc2hhcGUgLmxhYmVse3RleHQtYW5jaG9yOm1pZGRsZTt9I2dyYXBoLWRpdiAubm9kZSAua2F0ZXggcGF0aHtmaWxsOiMwMDA7c3Ryb2tlOiMwMDA7c3Ryb2tlLXdpZHRoOjFweDt9I2dyYXBoLWRpdiAucm91Z2gtbm9kZSAubGFiZWwsI2dyYXBoLWRpdiAubm9kZSAubGFiZWwsI2dyYXBoLWRpdiAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNncmFwaC1kaXYgLmljb24tc2hhcGUgLmxhYmVse3RleHQtYWxpZ246Y2VudGVyO30jZ3JhcGgtZGl2IC5ub2RlLmNsaWNrYWJsZXtjdXJzb3I6cG9pbnRlcjt9I2dyYXBoLWRpdiAucm9vdCAuYW5jaG9yIHBhdGh7ZmlsbDojMzMzMzMzIWltcG9ydGFudDtzdHJva2Utd2lkdGg6MDtzdHJva2U6IzMzMzMzMzt9I2dyYXBoLWRpdiAuYXJyb3doZWFkUGF0aHtmaWxsOiMzMzMzMzM7fSNncmFwaC1kaXYgLmVkZ2VQYXRoIC5wYXRoe3N0cm9rZTojMzMzMzMzO3N0cm9rZS13aWR0aDoyLjBweDt9I2dyYXBoLWRpdiAuZmxvd2NoYXJ0LWxpbmt7c3Ryb2tlOiMzMzMzMzM7ZmlsbDpub25lO30jZ3JhcGgtZGl2IC5lZGdlTGFiZWx7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3RleHQtYWxpZ246Y2VudGVyO30jZ3JhcGgtZGl2IC5lZGdlTGFiZWwgcHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNncmFwaC1kaXYgLmVkZ2VMYWJlbCByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtmaWxsOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNncmFwaC1kaXYgLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsIDIzMiwgMjMyLCAwLjUpO30jZ3JhcGgtZGl2IC5jbHVzdGVyIHJlY3R7ZmlsbDojZmZmZmRlO3N0cm9rZTojYWFhYTMzO3N0cm9rZS13aWR0aDoxcHg7fSNncmFwaC1kaXYgLmNsdXN0ZXIgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXIgc3Bhbntjb2xvcjojMzMzO30jZ3JhcGgtZGl2IGRpdi5tZXJtYWlkVG9vbHRpcHtwb3NpdGlvbjphYnNvbHV0ZTt0ZXh0LWFsaWduOmNlbnRlcjttYXgtd2lkdGg6MjAwcHg7cGFkZGluZzoycHg7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxMnB4O2JhY2tncm91bmQ6aHNsKDgwLCAxMDAlLCA5Ni4yNzQ1MDk4MDM5JSk7Ym9yZGVyOjFweCBzb2xpZCAjYWFhYTMzO2JvcmRlci1yYWRpdXM6MnB4O3BvaW50ZXItZXZlbnRzOm5vbmU7ei1pbmRleDoxMDA7fSNncmFwaC1kaXYgLmZsb3djaGFydFRpdGxlVGV4dHt0ZXh0LWFuY2hvcjptaWRkbGU7Zm9udC1zaXplOjE4cHg7ZmlsbDojMzMzO30jZ3JhcGgtZGl2IHJlY3QudGV4dHtmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjA7fSNncmFwaC1kaXYgLmljb24tc2hhcGUsI2dyYXBoLWRpdiAuaW1hZ2Utc2hhcGV7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3RleHQtYWxpZ246Y2VudGVyO30jZ3JhcGgtZGl2IC5pY29uLXNoYXBlIHAsI2dyYXBoLWRpdiAuaW1hZ2Utc2hhcGUgcHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7cGFkZGluZzoycHg7fSNncmFwaC1kaXYgLmljb24tc2hhcGUgcmVjdCwjZ3JhcGgtZGl2IC5pbWFnZS1zaGFwZSByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtmaWxsOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNncmFwaC1kaXYgOnJvb3R7LS1tZXJtYWlkLWZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjt9PC9zdHlsZT48Zz48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSI4IiBtYXJrZXJXaWR0aD0iOCIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1IiByZWZYPSI1IiB2aWV3Qm94PSIwIDAgMTAgMTAiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1wb2ludEVuZCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMCAwIEwgMTAgNSBMIDAgMTAgeiI+PC9wYXRoPjwvbWFya2VyPjxtYXJrZXIgb3JpZW50PSJhdXRvIiBtYXJrZXJIZWlnaHQ9IjgiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjQuNSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRTdGFydCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMCA1IEwgMTAgMTAgTCAxMCAwIHoiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjExIiB2aWV3Qm94PSIwIDAgMTAgMTAiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1jaXJjbGVFbmQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1IiByZWZYPSItMSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtdjItY2lyY2xlU3RhcnQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1LjIiIHJlZlg9IjEyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1jcm9zc0VuZCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUuMiIgcmVmWD0iLTEiIHZpZXdCb3g9IjAgMCAxMSAxMSIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIGlkPSJncmFwaC1kaXZfZmxvd2NoYXJ0LXYyLWNyb3NzU3RhcnQiPjxwYXRoIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBkPSJNIDEsMSBsIDksOSBNIDEwLDEgbCAtOSw5Ij48L3BhdGg+PC9tYXJrZXI+PGcgY2xhc3M9InJvb3QiPjxnIGNsYXNzPSJjbHVzdGVycyI+PC9nPjxnIGNsYXNzPSJlZGdlUGF0aHMiPjxwYXRoIG1hcmtlci1lbmQ9InVybCgjZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1wb2ludEVuZCkiIHN0eWxlPSIiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIGlkPSJMX2xlbmd0aF93aWR0aF8wIiBkPSJNNzA4Ljg0NCw1My4xMTdMNjI0LjMsNjIuNzY0QzUzOS43NTcsNzIuNDEyLDM3MC42NjksOTEuNzA2LDI4Ni4xMjYsMTA2Ljg1M0MyMDEuNTgyLDEyMiwyMDEuNTgyLDEzMywyMDEuNTgyLDEzOC41TDIwMS41ODIsMTQ0Ij48L3BhdGg+PHBhdGggbWFya2VyLWVuZD0idXJsKCNncmFwaC1kaXZfZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSIgc3R5bGU9IiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgaWQ9IkxfbGVuZ3RoX2hlaWdodF8xIiBkPSJNNzA4Ljg0NCw1OC41MDFMNjY4LjA1OSw2Ny4yNTFDNjI3LjI3NSw3Ni4wMDEsNTQ1LjcwNiw5My41LDUwNC45MjEsMTA3Ljc1QzQ2NC4xMzcsMTIyLDQ2NC4xMzcsMTMzLDQ2NC4xMzcsMTM4LjVMNDY0LjEzNywxNDQiPjwvcGF0aD48cGF0aCBtYXJrZXItZW5kPSJ1cmwoI2dyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIiBzdHlsZT0iIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBpZD0iTF93aWR0aF90aGlja25lc3NfMiIgZD0iTTE0Ny4zMzMsMjAyTDEzNC45NDMsMjA4LjE2N0MxMjIuNTUzLDIxNC4zMzMsOTcuNzczLDIyNi42NjcsODUuMzgyLDIzNi4zMzNDNzIuOTkyLDI0Niw3Mi45OTIsMjUzLDcyLjk5MiwyNTYuNUw3Mi45OTIsMjYwIj48L3BhdGg+PHBhdGggbWFya2VyLWVuZD0idXJsKCNncmFwaC1kaXZfZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSIgc3R5bGU9IiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgaWQ9Ikxfd2lkdGhfZGlhbWV0ZXJfMyIgZD0iTTIyMi44MjYsMjAyTDIyNy42NzgsMjA4LjE2N0MyMzIuNTMsMjE0LjMzMywyNDIuMjM0LDIyNi42NjcsMjQ3LjA4NiwyMzYuMzMzQzI1MS45MzgsMjQ2LDI1MS45MzgsMjUzLDI1MS45MzgsMjU2LjVMMjUxLjkzOCwyNjAiPjwvcGF0aD48cGF0aCBtYXJrZXItZW5kPSJ1cmwoI2dyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIiBzdHlsZT0iIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBpZD0iTF93aWR0aF9yYWRpdXNfNCIgZD0iTTI5MS4zMDksMjAxLjQ3TDMxMi41MTEsMjA3LjcyNUMzMzMuNzE0LDIxMy45OCwzNzYuMTE4LDIyNi40OSwzOTcuMzIxLDIzNi4yNDVDNDE4LjUyMywyNDYsNDE4LjUyMywyNTMsNDE4LjUyMywyNTYuNUw0MTguNTIzLDI2MCI+PC9wYXRoPjxwYXRoIG1hcmtlci1lbmQ9InVybCgjZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1wb2ludEVuZCkiIHN0eWxlPSIiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIGlkPSJMX2xlbmd0aF9wYXRoX2xlbmd0aF81IiBkPSJNNzMxLjc2OCw4Nkw3MjguNDg5LDkwLjE2N0M3MjUuMjExLDk0LjMzMyw3MTguNjU0LDEwMi42NjcsNzE1LjM3NiwxMTIuMzMzQzcxMi4wOTgsMTIyLDcxMi4wOTgsMTMzLDcxMi4wOTgsMTM4LjVMNzEyLjA5OCwxNDQiPjwvcGF0aD48cGF0aCBtYXJrZXItZW5kPSJ1cmwoI2dyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIiBzdHlsZT0iIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBpZD0iTF9wYXRoX2xlbmd0aF9kaXN0YW5jZV82IiBkPSJNNzEyLjA5OCwyMDJMNzEyLjA5OCwyMDguMTY3QzcxMi4wOTgsMjE0LjMzMyw3MTIuMDk4LDIyNi42NjcsNzEyLjA5OCwyMzYuMzMzQzcxMi4wOTgsMjQ2LDcxMi4wOTgsMjUzLDcxMi4wOTgsMjU2LjVMNzEyLjA5OCwyNjAiPjwvcGF0aD48cGF0aCBtYXJrZXItZW5kPSJ1cmwoI2dyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIiBzdHlsZT0iIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBpZD0iTF9kaXN0YW5jZV9yYWRpYWxfZGlzdGFuY2VfNyIgZD0iTTcxMi4wOTgsMzE4TDcxMi4wOTgsMzIyLjE2N0M3MTIuMDk4LDMyNi4zMzMsNzEyLjA5OCwzMzQuNjY3LDcxMi4wOTgsMzQyLjMzM0M3MTIuMDk4LDM1MCw3MTIuMDk4LDM1Nyw3MTIuMDk4LDM2MC41TDcxMi4wOTgsMzY0Ij48L3BhdGg+PHBhdGggbWFya2VyLWVuZD0idXJsKCNncmFwaC1kaXZfZmxvd2NoYXJ0LXYyLXBvaW50RW5kKSIgc3R5bGU9IiIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgaWQ9IkxfbGVuZ3RoX3dhdmVsZW5ndGhfOCIgZD0iTTgxNi4wNjMsNzAuMjI0TDgzMS43NTEsNzcuMDJDODQ3LjQzOSw4My44MTYsODc4LjgxNSw5Ny40MDgsODk0LjUwMywxMDkuNzA0QzkxMC4xOTEsMTIyLDkxMC4xOTEsMTMzLDkxMC4xOTEsMTM4LjVMOTEwLjE5MSwxNDQiPjwvcGF0aD48cGF0aCBtYXJrZXItZW5kPSJ1cmwoI2dyYXBoLWRpdl9mbG93Y2hhcnQtdjItcG9pbnRFbmQpIiBzdHlsZT0iIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBpZD0iTF9sZW5ndGhfZGlzcGxhY2VtZW50XzkiIGQ9Ik04MTYuMDYzLDU2Ljc4OEw4NjUuNTQ4LDY1LjgyNEM5MTUuMDMzLDc0Ljg1OSwxMDE0LjAwMyw5Mi45MjksMTA2My40ODgsMTA1LjQ2NUMxMTEyLjk3MywxMTgsMTExMi45NzMsMTI1LDExMTIuOTczLDEyOC41TDExMTIuOTczLDEzMiI+PC9wYXRoPjxwYXRoIG1hcmtlci1lbmQ9InVybCgjZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1wb2ludEVuZCkiIHN0eWxlPSIiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIGlkPSJMX2Rpc3BsYWNlbWVudF9wb3NpdGlvbl92ZWN0b3JfMTAiIGQ9Ik0xMTEyLjk3MywyMTRMMTExMi45NzMsMjE4LjE2N0MxMTEyLjk3MywyMjIuMzMzLDExMTIuOTczLDIzMC42NjcsMTExMi45NzMsMjM4LjMzM0MxMTEyLjk3MywyNDYsMTExMi45NzMsMjUzLDExMTIuOTczLDI1Ni41TDExMTIuOTczLDI2MCI+PC9wYXRoPjxwYXRoIG1hcmtlci1lbmQ9InVybCgjZ3JhcGgtZGl2X2Zsb3djaGFydC12Mi1wb2ludEVuZCkiIHN0eWxlPSIiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIGlkPSJMX3JhZGl1c19yYWRpdXNfb2ZfY3VydmF0dXJlXzExIiBkPSJNNDE4LjUyMywzMThMNDE4LjUyMywzMjIuMTY3QzQxOC41MjMsMzI2LjMzMyw0MTguNTIzLDMzNC42NjcsNDE4LjUyMywzNDIuMzMzQzQxOC41MjMsMzUwLDQxOC41MjMsMzU3LDQxOC41MjMsMzYwLjVMNDE4LjUyMywzNjQiPjwvcGF0aD48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbHMiPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIGNsYXNzPSJsYWJlbEJrZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiBjbGFzcz0ibGFiZWxCa2ciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgY2xhc3M9ImxhYmVsQmtnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIGNsYXNzPSJsYWJlbEJrZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiBjbGFzcz0ibGFiZWxCa2ciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgY2xhc3M9ImxhYmVsQmtnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIGNsYXNzPSJsYWJlbEJrZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiBjbGFzcz0ibGFiZWxCa2ciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgY2xhc3M9ImxhYmVsQmtnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIGNsYXNzPSJsYWJlbEJrZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiBjbGFzcz0ibGFiZWxCa2ciIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgY2xhc3M9ImxhYmVsQmtnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZXMiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDc2Mi40NTMxMjUsIDQ3KSIgaWQ9ImZsb3djaGFydC1sZW5ndGgtMTI1IiBjbGFzcz0ibm9kZSBkZWZhdWx0Ij48cmVjdCBoZWlnaHQ9Ijc4IiB3aWR0aD0iMTA3LjIxODc1IiB5PSItMzkiIHg9Ii01My42MDkzNzUiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjMuNjA5Mzc1LCAtMjQpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjQ4IiB3aWR0aD0iNDcuMjE4NzUiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5sZW5ndGg8L2I+PGJyLz5bbV08L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIwMS41ODIwMzEyNSwgMTc1KSIgaWQ9ImZsb3djaGFydC13aWR0aC0xMjciIGNsYXNzPSJub2RlIGRlZmF1bHQiPjxyZWN0IGhlaWdodD0iNTQiIHdpZHRoPSIxNzkuNDUzMTI1IiB5PSItMjciIHg9Ii04OS43MjY1NjI1IiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTU5LjcyNjU2MjUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxMTkuNDUzMTI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+d2lkdGg8L2I+IC8gPGI+YnJlYWR0aDwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ2NC4xMzY3MTg3NSwgMTc1KSIgaWQ9ImZsb3djaGFydC1oZWlnaHQtMTI5IiBjbGFzcz0ibm9kZSBkZWZhdWx0Ij48cmVjdCBoZWlnaHQ9IjU0IiB3aWR0aD0iMjQ1LjY1NjI1IiB5PSItMjciIHg9Ii0xMjIuODI4MTI1IiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTkyLjgyODEyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjE4NS42NTYyNSI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPmhlaWdodDwvYj4gLyA8Yj5kZXB0aDwvYj4gLyA8Yj5hbHRpdHVkZTwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDcyLjk5MjE4NzUsIDI5MSkiIGlkPSJmbG93Y2hhcnQtdGhpY2tuZXNzLTEzMSIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjEyOS45ODQzNzUiIHk9Ii0yNyIgeD0iLTY0Ljk5MjE4NzUiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzQuOTkyMTg3NSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjY5Ljk4NDM3NSI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPnRoaWNrbmVzczwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI1MS45Mzc1LCAyOTEpIiBpZD0iZmxvd2NoYXJ0LWRpYW1ldGVyLTEzMyIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjEyNy45MDYyNSIgeT0iLTI3IiB4PSItNjMuOTUzMTI1IiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTMzLjk1MzEyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjY3LjkwNjI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+ZGlhbWV0ZXI8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MTguNTIzNDM3NSwgMjkxKSIgaWQ9ImZsb3djaGFydC1yYWRpdXMtMTM1IiBjbGFzcz0ibm9kZSBkZWZhdWx0Ij48cmVjdCBoZWlnaHQ9IjU0IiB3aWR0aD0iMTA1LjI2NTYyNSIgeT0iLTI3IiB4PSItNTIuNjMyODEyNSIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yMi42MzI4MTI1LCAtMTIpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjI0IiB3aWR0aD0iNDUuMjY1NjI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+cmFkaXVzPC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzEyLjA5NzY1NjI1LCAxNzUpIiBpZD0iZmxvd2NoYXJ0LXBhdGhfbGVuZ3RoLTEzNyIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjE1MC4yNjU2MjUiIHk9Ii0yNyIgeD0iLTc1LjEzMjgxMjUiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDUuMTMyODEyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjkwLjI2NTYyNSI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPnBhdGhfbGVuZ3RoPC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzEyLjA5NzY1NjI1LCAyOTEpIiBpZD0iZmxvd2NoYXJ0LWRpc3RhbmNlLTEzOSIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjEyMi42NTYyNSIgeT0iLTI3IiB4PSItNjEuMzI4MTI1IiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTMxLjMyODEyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjYyLjY1NjI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+ZGlzdGFuY2U8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg3MTIuMDk3NjU2MjUsIDM5NSkiIGlkPSJmbG93Y2hhcnQtcmFkaWFsX2Rpc3RhbmNlLTE0MSIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjE3NC4xODc1IiB5PSItMjciIHg9Ii04Ny4wOTM3NSIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC01Ny4wOTM3NSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjExNC4xODc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+cmFkaWFsX2Rpc3RhbmNlPC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTEwLjE5MTQwNjI1LCAxNzUpIiBpZD0iZmxvd2NoYXJ0LXdhdmVsZW5ndGgtMTQzIiBjbGFzcz0ibm9kZSBkZWZhdWx0Ij48cmVjdCBoZWlnaHQ9IjU0IiB3aWR0aD0iMTQ1LjkyMTg3NSIgeT0iLTI3IiB4PSItNzIuOTYwOTM3NSIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC00Mi45NjA5Mzc1LCAtMTIpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjI0IiB3aWR0aD0iODUuOTIxODc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+d2F2ZWxlbmd0aDwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDExMTIuOTcyNjU2MjUsIDE3NSkiIGlkPSJmbG93Y2hhcnQtZGlzcGxhY2VtZW50LTE0NSIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI3OCIgd2lkdGg9IjE1OS42NDA2MjUiIHk9Ii0zOSIgeD0iLTc5LjgyMDMxMjUiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDkuODIwMzEyNSwgLTI0KSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSI0OCIgd2lkdGg9Ijk5LjY0MDYyNSI+PGRpdiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPmRpc3BsYWNlbWVudDwvYj48YnIvPnt2ZWN0b3J9PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMTEyLjk3MjY1NjI1LCAyOTEpIiBpZD0iZmxvd2NoYXJ0LXBvc2l0aW9uX3ZlY3Rvci0xNDciIGNsYXNzPSJub2RlIGRlZmF1bHQiPjxyZWN0IGhlaWdodD0iNTQiIHdpZHRoPSIxNzcuMDkzNzUiIHk9Ii0yNyIgeD0iLTg4LjU0Njg3NSIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC01OC41NDY4NzUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxMTcuMDkzNzUiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5wb3NpdGlvbl92ZWN0b3I8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg0MTguNTIzNDM3NSwgMzk1KSIgaWQ9ImZsb3djaGFydC1yYWRpdXNfb2ZfY3VydmF0dXJlLTE0OSIgY2xhc3M9Im5vZGUgZGVmYXVsdCI+PHJlY3QgaGVpZ2h0PSI1NCIgd2lkdGg9IjIxMi4yNSIgeT0iLTI3IiB4PSItMTA2LjEyNSIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC03Ni4xMjUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxNTIuMjUiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5yYWRpdXNfb2ZfY3VydmF0dXJlPC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PC9nPjwvZz48L2c+PC9zdmc+)

Each of the above quantities expresses some kind of *length*, and each can be measured with meters, which is the unit defined by the [[SI]](https://www.bipm.org/en/publications/si-brochure) for quantities of *length*. However, each has different properties, usage, and sometimes even a different character (*position vector* and *displacement* are vector quantities).

The below presents how such a hierarchy tree can be defined in the library:

```cpp
inline constexpr struct dim_length : base_dimension<"L"> {} dim_length;

inline constexpr struct length : quantity_spec<dim_length> {} length;
inline constexpr struct width : quantity_spec<length> {} width;
inline constexpr auto breadth = width;
inline constexpr struct height : quantity_spec<length> {} height;
inline constexpr auto depth = height;
inline constexpr auto altitude = height;
inline constexpr struct thickness : quantity_spec<width> {} thickness;
inline constexpr struct diameter : quantity_spec<width> {} diameter;
inline constexpr struct radius : quantity_spec<width> {} radius;
inline constexpr struct radius_of_curvature : quantity_spec<radius> {} radius_of_curvature;
inline constexpr struct path_length : quantity_spec<length> {} path_length;
inline constexpr auto arc_length = path_length;
inline constexpr struct distance : quantity_spec<path_length> {} distance;
inline constexpr struct radial_distance : quantity_spec<distance> {} radial_distance;
inline constexpr struct wavelength : quantity_spec<length> {} wavelength;
inline constexpr struct displacement : quantity_spec<length, quantity_character::vector> {} displacement;
inline constexpr struct position_vector : quantity_spec<displacement> {} position_vector;
```

In the above code:

- `length` takes the base dimension to indicate that we are creating a base quantity that will serve as a root for a tree of quantities of the same kind,
- `width` and following quantities are branches and leaves of this tree with the parent always provided as the first argument to `quantity_spec` class template,
- `breadth` is an alias name for the same quantity as `width`.

Please note that some quantities may be specified by [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) as vector or tensor quantities (e.g., `displacement`).

#### 16.1.3 Converting between quantities of the same kind

Quantity conversion rules can be defined based on the same hierarchy of quantities of kind length.

1. **Implicit conversions**
   - Every *width* is a *length*.
   - Every *radius* is a *width*.

   ```cpp
   static_assert(implicitly_convertible(isq::width, isq::length));
   static_assert(implicitly_convertible(isq::radius, isq::length));
   static_assert(implicitly_convertible(isq::radius, isq::width));
   ```

   Implicit conversions are allowed on copy-initialization:

   ```cpp
   void foo(quantity<isq::length[m]> q);
   ```

   ```cpp
   quantity<isq::width[m]> q1 = 42 * m;
   quantity<isq::length[m]> q2 = q1;  // implicit quantity conversion
   foo(q1);                           // implicit quantity conversion
   ```
2. **Explicit conversions**
   - Not every *length* is a *width*.
   - Not every *width* is a *radius*.

   ```cpp
   static_assert(!implicitly_convertible(isq::length, isq::width));
   static_assert(!implicitly_convertible(isq::length, isq::radius));
   static_assert(!implicitly_convertible(isq::width, isq::radius));
   static_assert(explicitly_convertible(isq::length, isq::width));
   static_assert(explicitly_convertible(isq::length, isq::radius));
   static_assert(explicitly_convertible(isq::width, isq::radius));
   ```

   Explicit conversions are forced by passing the quantity to a call operator of a `quantity_spec` type or by calling `quantity`’s explicit constructor::

   ```cpp
   void foo(quantity<isq::height[m]> q);
   ```

   ```cpp
   quantity<isq::length[m]> q1 = 42 * m;
   quantity<isq::height[m]> q2 = isq::height(q1);  // explicit quantity conversion
   quantity<isq::height[m]> q3(q1);                // direct initialization
   foo(isq::height(q1));                           // explicit quantity conversion
   ```
3. **Explicit casts**
   - *height* is never a *width*, and vice versa.
   - Both *height* and *width* are quantities of kind *length*.

   ```cpp
   static_assert(!implicitly_convertible(isq::height, isq::width));
   static_assert(!explicitly_convertible(isq::height, isq::width));
   static_assert(castable(isq::height, isq::width));
   ```

   Explicit casts are forced with a dedicated `quantity_cast` function:

   ```cpp
   void foo(quantity<isq::height[m]> q);
   ```

   ```cpp
   quantity<isq::width[m]> q1 = 42 * m;
   quantity<isq::height[m]> q2 = quantity_cast<isq::height>(q1);  // explicit quantity cast
   foo(quantity_cast<isq::height>(q1));                           // explicit quantity cast
   ```
4. **No conversion**
   - *time* has nothing in common with *length*.

   ```cpp
   static_assert(!implicitly_convertible(isq::time, isq::length));
   static_assert(!explicitly_convertible(isq::time, isq::length));
   static_assert(!castable(isq::time, isq::length));
   ```

   Even the explicit casts will not force such a conversion:

   ```cpp
   void foo(quantity<isq::length[m]>);
   ```

   ```cpp
   quantity<isq::length[m]> q1 = 42 * s;    // Compile-time error
   foo(quantity_cast<isq::length>(42 * s)); // Compile-time error
   ```

#### 16.1.4 Comparing, adding, and subtracting quantities of the same kind

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) explicitly states that *width* and *height* are quantities of the same kind and as such they:

- are mutually comparable, and
- can be added and subtracted.

If we take the above for granted, the only reasonable result of `1 * width + 1 * height` is `2 * length`, where the result of `length` is known as a common quantity type. A result of such an equation is always the first common node in a hierarchy tree of the same kind. For example:

```cpp
static_assert((isq::width(1 * m) + isq::height(1 * m)).quantity_spec == isq::length);
static_assert((isq::thickness(1 * m) + isq::radius(1 * m)).quantity_spec == isq::width);
static_assert((isq::distance(1 * m) + isq::path_length(1 * m)).quantity_spec == isq::path_length);
```

One could argue that allowing to add or compare quantities of *height* and *width* might be a safety issue, but we need to be consistent with the requirements of [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html). Moreover, from our experience, disallowing such operations and requiring an explicit cast to a common quantity in every single place makes the code so cluttered with casts that it nearly renders the library unusable.

Fortunately, the above-mentioned conversion rules make the code safe by construction anyway. Let’s analyze the following example:

```cpp
inline constexpr struct horizontal_length : quantity_spec<isq::length> {} horizontal_length;

namespace christmas {

struct gift {
  quantity<horizontal_length[m]> length;
  quantity<isq::width[m]> width;
  quantity<isq::height[m]> height;
};

std::array<quantity<isq::length[m]>, 2> gift_wrapping_paper_size(const gift& g)
{
  quantity dim1 = 2 * g.width + 2 * g.height + 0.5 * g.width;
  quantity dim2 = g.length + 2 * 0.75 * g.height;
  return { dim1, dim2 };
}

}  // namespace christmas

int main()
{
  const christmas::gift lego = { horizontal_length(40 * cm), isq::width(30 * cm), isq::height(15 * cm) };
  auto paper = christmas::gift_wrapping_paper_size(lego);

  std::cout << "Paper needed to pack a lego box:\n";
  std::cout << "- " << paper[0] << " X " << paper[1] << "\n";  // - 1.05 m X 0.625 m
  std::cout << "- area = " << paper[0] * paper[1] << "\n";     // - area = 0.65625 m²
}
```

In the beginning, we introduce a custom quantity `horizontal_length` of a kind *length*, which then, together with `isq::width` and `isq::height`, are used to define the dimensions of a Christmas gift. Next, we provide a function that calculates the dimensions of a gift wrapping paper with some wraparound. The result of both those expressions is a quantity of `isq::length`, as this is the closest common quantity for the arguments used in this quantity equation.

Regarding safety, it is important to mention here, that thanks to the conversion rules provided above, it would be impossible to accidentally do the following:

```cpp
void foo(quantity<horizontal_length[m]> q);

quantity<isq::width[m]> q1 = dim1;  // Compile-time error
quantity<isq::height[m]> q2{dim1};  // Compile-time error
foo(dim1);                          // Compile-time error
```

The reason of compilation errors above is the fact that `isq::length` is not implicitly convertible to the quantities defined based on it. To make the above code compile, an explicit conversion of a quantity type is needed:

```cpp
void foo(quantity<horizontal_length[m]> q);

quantity<isq::width[m]> q1 = isq::width(dim1);
quantity<isq::height[m]> q2{isq::height(dim1)};
foo(horizontal_length(dim1));
```

To summarize, rules for addition, subtraction, and comparison of quantities improve the library usability, while the conversion rules enhance the safety of the library compared to the libraries that do not model quantity kinds.

#### 16.1.5 Hierarchies of derived quantities

The same rules propagate to derived quantities. For example, we can define strongly typed horizontal length and area:

```cpp
inline constexpr struct horizontal_length : quantity_spec<isq::length> {} horizontal_length;
inline constexpr struct horizontal_area : quantity_spec<isq::area, horizontal_length * isq::width> {} horizontal_area;
```

The first definition says that a `horizontal_length` is a more specialized quantity than `isq::length` and belongs to the same quantity kind. The second line defines a `horizontal_area`, which is a more specialized quantity than `isq::area`, so it has a more constrained recipe as well. Thanks to that:

```cpp
static_assert(implicitly_convertible(horizontal_length, isq::length));
static_assert(!implicitly_convertible(isq::length, horizontal_length));
static_assert(explicitly_convertible(isq::length, horizontal_length));

static_assert(implicitly_convertible(horizontal_area, isq::area));
static_assert(!implicitly_convertible(isq::area, horizontal_area));
static_assert(explicitly_convertible(isq::area, horizontal_area));

static_assert(implicitly_convertible(isq::length * isq::length, isq::area));
static_assert(!implicitly_convertible(isq::length * isq::length, horizontal_area));
static_assert(explicitly_convertible(isq::length * isq::length, horizontal_area));

static_assert(implicitly_convertible(horizontal_length * isq::width, isq::area));
static_assert(implicitly_convertible(horizontal_length * isq::width, horizontal_area));
```

Unfortunately, derived quantity equations often do not automatically form a hierarchy tree. This is why sometimes it is not obvious what such a tree should look like. Also, the [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) explicitly states:

> The division of ‘quantity’ according to ‘kind of quantity’ is, to some extent, arbitrary.

The below presents some arbitrary hierarchy of derived quantities of kind *energy*:

![](data:image/svg+xml;base64,PHN2ZyBpZD0ibWVybWFpZC1zdmciIHdpZHRoPSIxMDAlIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGNsYXNzPSJmbG93Y2hhcnQiIHN0eWxlPSJtYXgtd2lkdGg6IDE0NTAuNjk1MzEyNXB4OyIgdmlld0JveD0iMCAwIDE0NTAuNjk1MzEyNSA3MTEuOTg0Mzc1IiByb2xlPSJncmFwaGljcy1kb2N1bWVudCBkb2N1bWVudCIgYXJpYS1yb2xlZGVzY3JpcHRpb249ImZsb3djaGFydC12MiIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxzdHlsZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+QGltcG9ydCB1cmwoImh0dHBzOi8vY2RuanMuY2xvdWRmbGFyZS5jb20vYWpheC9saWJzL2ZvbnQtYXdlc29tZS82LjcuMi9jc3MvYWxsLm1pbi5jc3MiKTs8L3N0eWxlPjxzdHlsZT4jbWVybWFpZC1zdmd7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O2ZpbGw6IzMzMzt9QGtleWZyYW1lcyBlZGdlLWFuaW1hdGlvbi1mcmFtZXtmcm9te3N0cm9rZS1kYXNob2Zmc2V0OjA7fX1Aa2V5ZnJhbWVzIGRhc2h7dG97c3Ryb2tlLWRhc2hvZmZzZXQ6MDt9fSNtZXJtYWlkLXN2ZyAuZWRnZS1hbmltYXRpb24tc2xvd3tzdHJva2UtZGFzaGFycmF5OjksNSFpbXBvcnRhbnQ7c3Ryb2tlLWRhc2hvZmZzZXQ6OTAwO2FuaW1hdGlvbjpkYXNoIDUwcyBsaW5lYXIgaW5maW5pdGU7c3Ryb2tlLWxpbmVjYXA6cm91bmQ7fSNtZXJtYWlkLXN2ZyAuZWRnZS1hbmltYXRpb24tZmFzdHtzdHJva2UtZGFzaGFycmF5OjksNSFpbXBvcnRhbnQ7c3Ryb2tlLWRhc2hvZmZzZXQ6OTAwO2FuaW1hdGlvbjpkYXNoIDIwcyBsaW5lYXIgaW5maW5pdGU7c3Ryb2tlLWxpbmVjYXA6cm91bmQ7fSNtZXJtYWlkLXN2ZyAuZXJyb3ItaWNvbntmaWxsOiM1NTIyMjI7fSNtZXJtYWlkLXN2ZyAuZXJyb3ItdGV4dHtmaWxsOiM1NTIyMjI7c3Ryb2tlOiM1NTIyMjI7fSNtZXJtYWlkLXN2ZyAuZWRnZS10aGlja25lc3Mtbm9ybWFse3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkLXN2ZyAuZWRnZS10aGlja25lc3MtdGhpY2t7c3Ryb2tlLXdpZHRoOjMuNXB4O30jbWVybWFpZC1zdmcgLmVkZ2UtcGF0dGVybi1zb2xpZHtzdHJva2UtZGFzaGFycmF5OjA7fSNtZXJtYWlkLXN2ZyAuZWRnZS10aGlja25lc3MtaW52aXNpYmxle3N0cm9rZS13aWR0aDowO2ZpbGw6bm9uZTt9I21lcm1haWQtc3ZnIC5lZGdlLXBhdHRlcm4tZGFzaGVke3N0cm9rZS1kYXNoYXJyYXk6Mzt9I21lcm1haWQtc3ZnIC5lZGdlLXBhdHRlcm4tZG90dGVke3N0cm9rZS1kYXNoYXJyYXk6Mjt9I21lcm1haWQtc3ZnIC5tYXJrZXJ7ZmlsbDojMzMzMzMzO3N0cm9rZTojMzMzMzMzO30jbWVybWFpZC1zdmcgLm1hcmtlci5jcm9zc3tzdHJva2U6IzMzMzMzMzt9I21lcm1haWQtc3ZnIHN2Z3tmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjE2cHg7fSNtZXJtYWlkLXN2ZyBwe21hcmdpbjowO30jbWVybWFpZC1zdmcgLmxhYmVse2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtjb2xvcjojMzMzO30jbWVybWFpZC1zdmcgLmNsdXN0ZXItbGFiZWwgdGV4dHtmaWxsOiMzMzM7fSNtZXJtYWlkLXN2ZyAuY2x1c3Rlci1sYWJlbCBzcGFue2NvbG9yOiMzMzM7fSNtZXJtYWlkLXN2ZyAuY2x1c3Rlci1sYWJlbCBzcGFuIHB7YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDt9I21lcm1haWQtc3ZnIC5sYWJlbCB0ZXh0LCNtZXJtYWlkLXN2ZyBzcGFue2ZpbGw6IzMzMztjb2xvcjojMzMzO30jbWVybWFpZC1zdmcgLm5vZGUgcmVjdCwjbWVybWFpZC1zdmcgLm5vZGUgY2lyY2xlLCNtZXJtYWlkLXN2ZyAubm9kZSBlbGxpcHNlLCNtZXJtYWlkLXN2ZyAubm9kZSBwb2x5Z29uLCNtZXJtYWlkLXN2ZyAubm9kZSBwYXRoe2ZpbGw6I0VDRUNGRjtzdHJva2U6IzkzNzBEQjtzdHJva2Utd2lkdGg6MXB4O30jbWVybWFpZC1zdmcgLnJvdWdoLW5vZGUgLmxhYmVsIHRleHQsI21lcm1haWQtc3ZnIC5ub2RlIC5sYWJlbCB0ZXh0LCNtZXJtYWlkLXN2ZyAuaW1hZ2Utc2hhcGUgLmxhYmVsLCNtZXJtYWlkLXN2ZyAuaWNvbi1zaGFwZSAubGFiZWx7dGV4dC1hbmNob3I6bWlkZGxlO30jbWVybWFpZC1zdmcgLm5vZGUgLmthdGV4IHBhdGh7ZmlsbDojMDAwO3N0cm9rZTojMDAwO3N0cm9rZS13aWR0aDoxcHg7fSNtZXJtYWlkLXN2ZyAucm91Z2gtbm9kZSAubGFiZWwsI21lcm1haWQtc3ZnIC5ub2RlIC5sYWJlbCwjbWVybWFpZC1zdmcgLmltYWdlLXNoYXBlIC5sYWJlbCwjbWVybWFpZC1zdmcgLmljb24tc2hhcGUgLmxhYmVse3RleHQtYWxpZ246Y2VudGVyO30jbWVybWFpZC1zdmcgLm5vZGUuY2xpY2thYmxle2N1cnNvcjpwb2ludGVyO30jbWVybWFpZC1zdmcgLnJvb3QgLmFuY2hvciBwYXRoe2ZpbGw6IzMzMzMzMyFpbXBvcnRhbnQ7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlOiMzMzMzMzM7fSNtZXJtYWlkLXN2ZyAuYXJyb3doZWFkUGF0aHtmaWxsOiMzMzMzMzM7fSNtZXJtYWlkLXN2ZyAuZWRnZVBhdGggLnBhdGh7c3Ryb2tlOiMzMzMzMzM7c3Ryb2tlLXdpZHRoOjIuMHB4O30jbWVybWFpZC1zdmcgLmZsb3djaGFydC1saW5re3N0cm9rZTojMzMzMzMzO2ZpbGw6bm9uZTt9I21lcm1haWQtc3ZnIC5lZGdlTGFiZWx7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO3RleHQtYWxpZ246Y2VudGVyO30jbWVybWFpZC1zdmcgLmVkZ2VMYWJlbCBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I21lcm1haWQtc3ZnIC5lZGdlTGFiZWwgcmVjdHtvcGFjaXR5OjAuNTtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7ZmlsbDpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO30jbWVybWFpZC1zdmcgLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsIDIzMiwgMjMyLCAwLjUpO30jbWVybWFpZC1zdmcgLmNsdXN0ZXIgcmVjdHtmaWxsOiNmZmZmZGU7c3Ryb2tlOiNhYWFhMzM7c3Ryb2tlLXdpZHRoOjFweDt9I21lcm1haWQtc3ZnIC5jbHVzdGVyIHRleHR7ZmlsbDojMzMzO30jbWVybWFpZC1zdmcgLmNsdXN0ZXIgc3Bhbntjb2xvcjojMzMzO30jbWVybWFpZC1zdmcgZGl2Lm1lcm1haWRUb29sdGlwe3Bvc2l0aW9uOmFic29sdXRlO3RleHQtYWxpZ246Y2VudGVyO21heC13aWR0aDoyMDBweDtwYWRkaW5nOjJweDtmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjEycHg7YmFja2dyb3VuZDpoc2woODAsIDEwMCUsIDk2LjI3NDUwOTgwMzklKTtib3JkZXI6MXB4IHNvbGlkICNhYWFhMzM7Ym9yZGVyLXJhZGl1czoycHg7cG9pbnRlci1ldmVudHM6bm9uZTt6LWluZGV4OjEwMDt9I21lcm1haWQtc3ZnIC5mbG93Y2hhcnRUaXRsZVRleHR7dGV4dC1hbmNob3I6bWlkZGxlO2ZvbnQtc2l6ZToxOHB4O2ZpbGw6IzMzMzt9I21lcm1haWQtc3ZnIHJlY3QudGV4dHtmaWxsOm5vbmU7c3Ryb2tlLXdpZHRoOjA7fSNtZXJtYWlkLXN2ZyAuaWNvbi1zaGFwZSwjbWVybWFpZC1zdmcgLmltYWdlLXNoYXBle2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt0ZXh0LWFsaWduOmNlbnRlcjt9I21lcm1haWQtc3ZnIC5pY29uLXNoYXBlIHAsI21lcm1haWQtc3ZnIC5pbWFnZS1zaGFwZSBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtwYWRkaW5nOjJweDt9I21lcm1haWQtc3ZnIC5pY29uLXNoYXBlIHJlY3QsI21lcm1haWQtc3ZnIC5pbWFnZS1zaGFwZSByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtmaWxsOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7fSNtZXJtYWlkLXN2ZyAubGFiZWwtaWNvbntkaXNwbGF5OmlubGluZS1ibG9jaztoZWlnaHQ6MWVtO292ZXJmbG93OnZpc2libGU7dmVydGljYWwtYWxpZ246LTAuMTI1ZW07fSNtZXJtYWlkLXN2ZyAubm9kZSAubGFiZWwtaWNvbiBwYXRoe2ZpbGw6Y3VycmVudENvbG9yO3N0cm9rZTpyZXZlcnQ7c3Ryb2tlLXdpZHRoOnJldmVydDt9I21lcm1haWQtc3ZnIDpyb290ey0tbWVybWFpZC1mb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7fTwvc3R5bGU+PGc+PG1hcmtlciBpZD0ibWVybWFpZC1zdmdfZmxvd2NoYXJ0LXYyLXBvaW50RW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSI1IiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjgiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAwIDAgTCAxMCA1IEwgMCAxMCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWQtc3ZnX2Zsb3djaGFydC12Mi1wb2ludFN0YXJ0IiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSI0LjUiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iOCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDAgNSBMIDEwIDEwIEwgMTAgMCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im1lcm1haWQtc3ZnX2Zsb3djaGFydC12Mi1jaXJjbGVFbmQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjExIiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkLXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlU3RhcnQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9Ii0xIiByZWZZPSI1IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VySGVpZ2h0PSIxMSIgb3JpZW50PSJhdXRvIj48Y2lyY2xlIGN4PSI1IiBjeT0iNSIgcj0iNSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48bWFya2VyIGlkPSJtZXJtYWlkLXN2Z19mbG93Y2hhcnQtdjItY3Jvc3NFbmQiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIHJlZlg9IjEyIiByZWZZPSI1LjIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibWVybWFpZC1zdmdfZmxvd2NoYXJ0LXYyLWNyb3NzU3RhcnQiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIHJlZlg9Ii0xIiByZWZZPSI1LjIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PGcgY2xhc3M9InJvb3QiPjxnIGNsYXNzPSJjbHVzdGVycyIvPjxnIGNsYXNzPSJlZGdlUGF0aHMiPjxwYXRoIGQ9Ik02MTAuNjUyLDc2LjE5Mkw1MzUuMjkyLDg2LjU0OEM0NTkuOTMyLDk2LjkwNCwzMDkuMjEyLDExNy42MTYsMjMzLjg1MiwxMzIuMTM5QzE1OC40OTIsMTQ2LjY2MSwxNTguNDkyLDE1NC45OTUsMTU4LjQ5MiwxNTkuMTYxTDE1OC40OTIsMTYzLjMyOCIgaWQ9IkxfZW5lcmd5X3NpZ25hbF9lbmVyZ3lfcGVyX2JpbmFyeV9kaWdpdF8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9lbmVyZ3lfc2lnbmFsX2VuZXJneV9wZXJfYmluYXJ5X2RpZ2l0XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk5qRXdMalkxTWpNME16YzFMQ0o1SWpvM05pNHhPVEkwTnpNeU56azFOemN4Tkgwc2V5SjRJam94TlRndU5Ea3lNVGczTlN3aWVTSTZNVE00TGpNeU9ERXlOWDBzZXlKNElqb3hOVGd1TkRreU1UZzNOU3dpZVNJNk1UWXpMak15T0RFeU5YMWQiLz48cGF0aCBkPSJNNjEwLjY1Miw5NC44MzFMNTg2LjY3NiwxMDIuMDgxQzU2Mi43MDEsMTA5LjMzLDUxNC43NDksMTIzLjgyOSw0OTAuNzczLDEzNy4yNDVDNDY2Ljc5NywxNTAuNjYxLDQ2Ni43OTcsMTYyLjk5NSw0NjYuNzk3LDE2OS4xNjFMNDY2Ljc5NywxNzUuMzI4IiBpZD0iTF9lbmVyZ3lfbWVjaGFuaWNhbF93b3JrXzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2VuZXJneV9tZWNoYW5pY2FsX3dvcmtfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TmpFd0xqWTFNak0wTXpjMUxDSjVJam81TkM0NE16RXlPRGt6TWpZNE5UY3lOMzBzZXlKNElqbzBOall1TnprMk9EYzFMQ0o1SWpveE16Z3VNekk0TVRJMWZTeDdJbmdpT2pRMk5pNDNPVFk0TnpVc0lua2lPakUzTlM0ek1qZ3hNalY5WFE9PSIvPjxwYXRoIGQ9Ik03MTUuNzMsMTEzLjMyOEw3MTUuMTAzLDExNy40OTVDNzE0LjQ3NiwxMjEuNjYxLDcxMy4yMjIsMTI5Ljk5NSw3MTIuNTk2LDE0Mi4zMjhDNzExLjk2OSwxNTQuNjYxLDcxMS45NjksMTcwLjk5NSw3MTEuOTY5LDE3OS4xNjFMNzExLjk2OSwxODcuMzI4IiBpZD0iTF9lbmVyZ3lfcmFkaWFudF9lbmVyZ3lfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfZW5lcmd5X3JhZGlhbnRfZW5lcmd5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk56RTFMamN5T1RZNE9UVTBNek13TlRVc0lua2lPakV4TXk0ek1qZ3hNalY5TEhzaWVDSTZOekV4TGprMk9EYzFMQ0o1SWpveE16Z3VNekk0TVRJMWZTeDdJbmdpT2pjeE1TNDVOamczTlN3aWVTSTZNVGczTGpNeU9ERXlOWDFkIi8+PHBhdGggZD0iTTgzNi42NTIsOTIuMTE1TDg2NC4zMjYsOTkuODE3Qzg5MiwxMDcuNTE5LDk0Ny4zNDgsMTIyLjkyNCw5NzUuMDIxLDEzNi43OTNDMTAwMi42OTUsMTUwLjY2MSwxMDAyLjY5NSwxNjIuOTk1LDEwMDIuNjk1LDE2OS4xNjFMMTAwMi42OTUsMTc1LjMyOCIgaWQ9IkxfZW5lcmd5X2ludGVybmFsX2VuZXJneV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9lbmVyZ3lfaW50ZXJuYWxfZW5lcmd5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk9ETTJMalkxTWpNME16YzFMQ0o1SWpvNU1pNHhNVFExTlRVNU5UVTFPRGw5TEhzaWVDSTZNVEF3TWk0Mk9UVXpNVEkxTENKNUlqb3hNemd1TXpJNE1USTFmU3g3SW5naU9qRXdNREl1TmprMU16RXlOU3dpZVNJNk1UYzFMak15T0RFeU5YMWQiLz48cGF0aCBkPSJNODM2LjY1Miw3NS41NjNMOTE1Ljk5Myw4Ni4wMjRDOTk1LjMzMyw5Ni40ODUsMTE1NC4wMTQsMTE3LjQwNiwxMjMzLjM1NSwxMzIuMDM0QzEzMTIuNjk1LDE0Ni42NjEsMTMxMi42OTUsMTU0Ljk5NSwxMzEyLjY5NSwxNTkuMTYxTDEzMTIuNjk1LDE2My4zMjgiIGlkPSJMX2VuZXJneV9hY3RpdmVfZW5lcmd5XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2VuZXJneV9hY3RpdmVfZW5lcmd5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk9ETTJMalkxTWpNME16YzFMQ0o1SWpvM05TNDFOakk0TnpJeE5ESXlNamsxTW4wc2V5SjRJam94TXpFeUxqWTVOVE14TWpVc0lua2lPakV6T0M0ek1qZ3hNalY5TEhzaWVDSTZNVE14TWk0Mk9UVXpNVEkxTENKNUlqb3hOak11TXpJNE1USTFmVjA9Ii8+PHBhdGggZD0iTTQ2Ni43OTcsMjUzLjMyOEw0NjYuNzk3LDI1OS40OTVDNDY2Ljc5NywyNjUuNjYxLDQ2Ni43OTcsMjc3Ljk5NSw0NjYuNzk3LDI4OC4zMjhDNDY2Ljc5NywyOTguNjYxLDQ2Ni43OTcsMzA2Ljk5NSw0NjYuNzk3LDMxMS4xNjFMNDY2Ljc5NywzMTUuMzI4IiBpZD0iTF9tZWNoYW5pY2FsX3dvcmtfbWVjaGFuaWNhbF9lbmVyZ3lfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfbWVjaGFuaWNhbF93b3JrX21lY2hhbmljYWxfZW5lcmd5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk5EWTJMamM1TmpnM05Td2llU0k2TWpVekxqTXlPREV5Tlgwc2V5SjRJam8wTmpZdU56azJPRGMxTENKNUlqb3lPVEF1TXpJNE1USTFmU3g3SW5naU9qUTJOaTQzT1RZNE56VXNJbmtpT2pNeE5TNHpNamd4TWpWOVhRPT0iLz48cGF0aCBkPSJNMzk1LjEwOSwzOTYuNjU2TDM4Ny43NjMsNDAwLjgyM0MzODAuNDE3LDQwNC45OSwzNjUuNzI2LDQxMy4zMjMsMzU4LjM4MSw0MjMuOTM0QzM1MS4wMzUsNDM0LjU0NCwzNTEuMDM1LDQ0Ny40MzIsMzUxLjAzNSw0NTMuODc2TDM1MS4wMzUsNDYwLjMyIiBpZD0iTF9tZWNoYW5pY2FsX2VuZXJneV9wb3RlbnRpYWxfZW5lcmd5XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX21lY2hhbmljYWxfZW5lcmd5X3BvdGVudGlhbF9lbmVyZ3lfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TXprMUxqRXdPRFl5TkRReU16Y3dOakUxTENKNUlqb3pPVFl1TmpVMk1qVjlMSHNpZUNJNk16VXhMakF6TlRFMU5qSTFMQ0o1SWpvME1qRXVOalUyTWpWOUxIc2llQ0k2TXpVeExqQXpOVEUxTmpJMUxDSjVJam8wTmpBdU16SXdNekV5TlgxZCIvPjxwYXRoIGQ9Ik01NDkuOTAxLDM5Ni42NTZMNTU4LjQxNiw0MDAuODIzQzU2Ni45MzEsNDA0Ljk5LDU4My45NjIsNDEzLjMyMyw1OTIuNDc3LDQyMS42NTZDNjAwLjk5Miw0MjkuOTksNjAwLjk5Miw0MzguMzIzLDYwMC45OTIsNDQyLjQ5TDYwMC45OTIsNDQ2LjY1NiIgaWQ9IkxfbWVjaGFuaWNhbF9lbmVyZ3lfa2luZXRpY19lbmVyZ3lfMCIgY2xhc3M9IiBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfbWVjaGFuaWNhbF9lbmVyZ3lfa2luZXRpY19lbmVyZ3lfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TlRRNUxqa3dNRFUzTlRNMk5ETTJOalFzSW5raU9qTTVOaTQyTlRZeU5YMHNleUo0SWpvMk1EQXVPVGt5TVRnM05Td2llU0k2TkRJeExqWTFOakkxZlN4N0luZ2lPall3TUM0NU9USXhPRGMxTENKNUlqbzBORFl1TmpVMk1qVjlYUT09Ii8+PHBhdGggZD0iTTI4NC4wMDYsNTE0LjMyTDI2OC4wMDgsNTIwLjc2NEMyNTIuMDEsNTI3LjIwOCwyMjAuMDE1LDU0MC4wOTYsMjA0LjAxNyw1NTAuNzA3QzE4OC4wMiw1NjEuMzE4LDE4OC4wMiw1NjkuNjUxLDE4OC4wMiw1NzMuODE4TDE4OC4wMiw1NzcuOTg0IiBpZD0iTF9wb3RlbnRpYWxfZW5lcmd5X2dyYXZpdGF0aW9uYWxfcG90ZW50aWFsX2VuZXJneV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9wb3RlbnRpYWxfZW5lcmd5X2dyYXZpdGF0aW9uYWxfcG90ZW50aWFsX2VuZXJneV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNamcwTGpBd05UYzJPRGs0TURVeE56VXpMQ0o1SWpvMU1UUXVNekl3TXpFeU5YMHNleUo0SWpveE9EZ3VNREU1TlRNeE1qVXNJbmtpT2pVMU1pNDVPRFF6TnpWOUxIc2llQ0k2TVRnNExqQXhPVFV6TVRJMUxDSjVJam8xTnpjdU9UZzBNemMxZlYwPSIvPjxwYXRoIGQ9Ik00MTguMDY1LDUxNC4zMkw0MzQuMDYyLDUyMC43NjRDNDUwLjA2LDUyNy4yMDgsNDgyLjA1NSw1NDAuMDk2LDQ5OC4wNTMsNTUyLjQzQzUxNC4wNTEsNTY0Ljc2Myw1MTQuMDUxLDU3Ni41NDIsNTE0LjA1MSw1ODIuNDMxTDUxNC4wNTEsNTg4LjMyIiBpZD0iTF9wb3RlbnRpYWxfZW5lcmd5X2VsYXN0aWNfcG90ZW50aWFsX2VuZXJneV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9wb3RlbnRpYWxfZW5lcmd5X2VsYXN0aWNfcG90ZW50aWFsX2VuZXJneV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZOREU0TGpBMk5EVTBNelV4T1RRNE1qUTNMQ0o1SWpvMU1UUXVNekl3TXpFeU5YMHNleUo0SWpvMU1UUXVNRFV3TnpneE1qVXNJbmtpT2pVMU1pNDVPRFF6TnpWOUxIc2llQ0k2TlRFMExqQTFNRGM0TVRJMUxDSjVJam8xT0RndU16SXdNekV5TlgxZCIvPjxwYXRoIGQ9Ik04NzguMDUsMjUzLjMyOEw4NTguMzQxLDI1OS40OTVDODM4LjYzMiwyNjUuNjYxLDc5OS4yMTUsMjc3Ljk5NSw3NzkuNTA2LDI4OC42MDVDNzU5Ljc5NywyOTkuMjE2LDc1OS43OTcsMzA4LjEwNCw3NTkuNzk3LDMxMi41NDhMNzU5Ljc5NywzMTYuOTkyIiBpZD0iTF9pbnRlcm5hbF9lbmVyZ3lfSGVsbWhvbHR6X2VuZXJneV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9pbnRlcm5hbF9lbmVyZ3lfSGVsbWhvbHR6X2VuZXJneV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZPRGM0TGpBMU1EQTJNVFkzTnpZek1UWXNJbmtpT2pJMU15NHpNamd4TWpWOUxIc2llQ0k2TnpVNUxqYzVOamczTlN3aWVTSTZNamt3TGpNeU9ERXlOWDBzZXlKNElqbzNOVGt1TnprMk9EYzFMQ0o1SWpvek1UWXVPVGt5TVRnM05YMWQiLz48cGF0aCBkPSJNMTAwMi42OTUsMjUzLjMyOEwxMDAyLjY5NSwyNTkuNDk1QzEwMDIuNjk1LDI2NS42NjEsMTAwMi42OTUsMjc3Ljk5NSwxMDAyLjY5NSwyOTAuNjA1QzEwMDIuNjk1LDMwMy4yMTYsMTAwMi42OTUsMzE2LjEwNCwxMDAyLjY5NSwzMjIuNTQ4TDEwMDIuNjk1LDMyOC45OTIiIGlkPSJMX2ludGVybmFsX2VuZXJneV9lbnRoYWxweV8wIiBjbGFzcz0iIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9pbnRlcm5hbF9lbmVyZ3lfZW50aGFscHlfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TVRBd01pNDJPVFV6TVRJMUxDSjVJam95TlRNdU16STRNVEkxZlN4N0luZ2lPakV3TURJdU5qazFNekV5TlN3aWVTSTZNamt3TGpNeU9ERXlOWDBzZXlKNElqb3hNREF5TGpZNU5UTXhNalVzSW5raU9qTXlPQzQ1T1RJeE9EYzFmVjA9Ii8+PHBhdGggZD0iTTExMzIuMTMxLDI1My4zMjhMMTE1Mi41OTgsMjU5LjQ5NUMxMTczLjA2NCwyNjUuNjYxLDEyMTMuOTk3LDI3Ny45OTUsMTIzNC40NjMsMjkwLjYwNUMxMjU0LjkzLDMwMy4yMTYsMTI1NC45MywzMTYuMTA0LDEyNTQuOTMsMzIyLjU0OEwxMjU0LjkzLDMyOC45OTIiIGlkPSJMX2ludGVybmFsX2VuZXJneV9oZWF0XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2ludGVybmFsX2VuZXJneV9oZWF0XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1URXpNaTR4TXpFek56TXpOVFV5TmpNeExDSjVJam95TlRNdU16STRNVEkxZlN4N0luZ2lPakV5TlRRdU9USTVOamczTlN3aWVTSTZNamt3TGpNeU9ERXlOWDBzZXlKNElqb3hNalUwTGpreU9UWTROelVzSW5raU9qTXlPQzQ1T1RJeE9EYzFmVjA9Ii8+PHBhdGggZD0iTTEwMDIuNjk1LDM4Mi45OTJMMTAwMi42OTUsMzg5LjQzNkMxMDAyLjY5NSwzOTUuODgsMTAwMi42OTUsNDA4Ljc2OCwxMDAyLjY5NSw0MTkuNjU2QzEwMDIuNjk1LDQzMC41NDQsMTAwMi42OTUsNDM5LjQzMiwxMDAyLjY5NSw0NDMuODc2TDEwMDIuNjk1LDQ0OC4zMiIgaWQ9IkxfZW50aGFscHlfR2liYnNfZW5lcmd5XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2VudGhhbHB5X0dpYmJzX2VuZXJneV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVEF3TWk0Mk9UVXpNVEkxTENKNUlqb3pPREl1T1RreU1UZzNOWDBzZXlKNElqb3hNREF5TGpZNU5UTXhNalVzSW5raU9qUXlNUzQyTlRZeU5YMHNleUo0SWpveE1EQXlMalk1TlRNeE1qVXNJbmtpT2pRME9DNHpNakF6TVRJMWZWMD0iLz48cGF0aCBkPSJNMTI1NC45MywzODIuOTkyTDEyNTQuOTMsMzg5LjQzNkMxMjU0LjkzLDM5NS44OCwxMjU0LjkzLDQwOC43NjgsMTI1NC45Myw0MjEuNjU2QzEyNTQuOTMsNDM0LjU0NCwxMjU0LjkzLDQ0Ny40MzIsMTI1NC45Myw0NTMuODc2TDEyNTQuOTMsNDYwLjMyIiBpZD0iTF9oZWF0X2xhdGVudF9oZWF0XzAiIGNsYXNzPSIgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2hlYXRfbGF0ZW50X2hlYXRfMCIgZGF0YS1wb2ludHM9Ilczc2llQ0k2TVRJMU5DNDVNamsyT0RjMUxDSjVJam96T0RJdU9Ua3lNVGczTlgwc2V5SjRJam94TWpVMExqa3lPVFk0TnpVc0lua2lPalF5TVM0Mk5UWXlOWDBzZXlKNElqb3hNalUwTGpreU9UWTROelVzSW5raU9qUTJNQzR6TWpBek1USTFmVjA9Ii8+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWxzIj48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZW5lcmd5X3NpZ25hbF9lbmVyZ3lfcGVyX2JpbmFyeV9kaWdpdF8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZW5lcmd5X21lY2hhbmljYWxfd29ya18wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZW5lcmd5X3JhZGlhbnRfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9lbmVyZ3lfaW50ZXJuYWxfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9lbmVyZ3lfYWN0aXZlX2VuZXJneV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfbWVjaGFuaWNhbF93b3JrX21lY2hhbmljYWxfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9tZWNoYW5pY2FsX2VuZXJneV9wb3RlbnRpYWxfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9tZWNoYW5pY2FsX2VuZXJneV9raW5ldGljX2VuZXJneV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfcG90ZW50aWFsX2VuZXJneV9ncmF2aXRhdGlvbmFsX3BvdGVudGlhbF9lbmVyZ3lfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwgIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX3BvdGVudGlhbF9lbmVyZ3lfZWxhc3RpY19wb3RlbnRpYWxfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9pbnRlcm5hbF9lbmVyZ3lfSGVsbWhvbHR6X2VuZXJneV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfaW50ZXJuYWxfZW5lcmd5X2VudGhhbHB5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9pbnRlcm5hbF9lbmVyZ3lfaGVhdF8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCAiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZW50aGFscHlfR2liYnNfZW5lcmd5XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9oZWF0X2xhdGVudF9oZWF0XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsICI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZXMiPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1lbmVyZ3ktMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzIzLjY1MjM0Mzc1LCA2MC42NjQwNjI1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTExMyIgeT0iLTUyLjY2NDA2MjUiIHdpZHRoPSIyMjYiIGhlaWdodD0iMTA1LjMyODEyNSIvPjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTgzLCAtMzcuNjY0MDYyNSkiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMTY2IiBoZWlnaHQ9Ijc1LjMyODEyNSI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5lbmVyZ3k8L2I+PGJyIC8+PGk+KG1hc3MgKiBsZW5ndGg8c3VwPjI8L3N1cD4gLyB0aW1lPHN1cD4yPC9zdXA+KTwvaT48YnIgLz5bSl08L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1zaWduYWxfZW5lcmd5X3Blcl9iaW5hcnlfZGlnaXQtMSIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU4LjQ5MjE4NzUsIDIxNC4zMjgxMjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTUwLjQ5MjE4NzUiIHk9Ii01MSIgd2lkdGg9IjMwMC45ODQzNzUiIGhlaWdodD0iMTAyIi8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTIwLjQ5MjE4NzUsIC0zNikiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMjQwLjk4NDM3NSIgaGVpZ2h0PSI3MiI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5zaWduYWxfZW5lcmd5X3Blcl9iaW5hcnlfZGlnaXQ8L2I+PGJyIC8+PGk+KGNhcnJpZXJfcG93ZXIgKiBwZXJpb2Rfb2ZfYmluYXJ5X2RpZ2l0cyk8L2k+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtbWVjaGFuaWNhbF93b3JrLTIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ2Ni43OTY4NzUsIDIxNC4zMjgxMjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTA3LjgxMjUiIHk9Ii0zOSIgd2lkdGg9IjIxNS42MjUiIGhlaWdodD0iNzgiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC03Ny44MTI1LCAtMjQpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjE1NS42MjUiIGhlaWdodD0iNDgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+PGI+bWVjaGFuaWNhbF93b3JrPC9iPjxiciAvPjxpPihmb3JjZSAqIGRpc3BsYWNlbWVudCk8L2k+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtcmFkaWFudF9lbmVyZ3ktMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNzExLjk2ODc1LCAyMTQuMzI4MTI1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTg3LjM1OTM3NSIgeT0iLTI3IiB3aWR0aD0iMTc0LjcxODc1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNTcuMzU5Mzc1LCAtMTIpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjExNC43MTg3NSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5yYWRpYW50X2VuZXJneTwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1pbnRlcm5hbF9lbmVyZ3ktNCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAwMi42OTUzMTI1LCAyMTQuMzI4MTI1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTM5IiB3aWR0aD0iMjYwIiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMjQpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5pbnRlcm5hbF9lbmVyZ3k8L2I+IHwgPGI+dGhlcm1vZHluYW1pY19lbmVyZ3k8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtYWN0aXZlX2VuZXJneS01IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMzEyLjY5NTMxMjUsIDIxNC4zMjgxMjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwIiB5PSItNTEiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTAyIi8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMzYpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI3MiI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5hY3RpdmVfZW5lcmd5PC9iPjxiciAvPjxpPihpbnN0YW50YW5lb3VzX3Bvd2VyICogdGltZSk8L2k+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtbWVjaGFuaWNhbF9lbmVyZ3ktNyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNDY2Ljc5Njg3NSwgMzU1Ljk5MjE4NzUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTEzIiB5PSItNDAuNjY0MDYyNSIgd2lkdGg9IjIyNiIgaGVpZ2h0PSI4MS4zMjgxMjUiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC04MywgLTI1LjY2NDA2MjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjE2NiIgaGVpZ2h0PSI1MS4zMjgxMjUiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+PGI+bWVjaGFuaWNhbF9lbmVyZ3k8L2I+PGJyIC8+PGk+KG1hc3MgKiBsZW5ndGg8c3VwPjI8L3N1cD4gLyB0aW1lPHN1cD4yPC9zdXA+KTwvaT48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1wb3RlbnRpYWxfZW5lcmd5LTkiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDM1MS4wMzUxNTYyNSwgNDg3LjMyMDMxMjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItOTQuMDE1NjI1IiB5PSItMjciIHdpZHRoPSIxODguMDMxMjUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02NC4wMTU2MjUsIC0xMikiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMTI4LjAzMTI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPjxiPnBvdGVudGlhbF9lbmVyZ3k8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQta2luZXRpY19lbmVyZ3ktMTAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDYwMC45OTIxODc1LCA0ODcuMzIwMzEyNSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii04Ny41MDc4MTI1IiB5PSItNDAuNjY0MDYyNSIgd2lkdGg9IjE3NS4wMTU2MjUiIGhlaWdodD0iODEuMzI4MTI1Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNTcuNTA3ODEyNSwgLTI1LjY2NDA2MjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjExNS4wMTU2MjUiIGhlaWdodD0iNTEuMzI4MTI1Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPjxiPmtpbmV0aWNfZW5lcmd5PC9iPjxiciAvPjxpPihtYXNzICogc3BlZWQ8c3VwPjI8L3N1cD4pPC9pPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LWdyYXZpdGF0aW9uYWxfcG90ZW50aWFsX2VuZXJneS0xMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTg4LjAxOTUzMTI1LCA2NDAuOTg0Mzc1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTE0Ni4wMzEyNSIgeT0iLTYzIiB3aWR0aD0iMjkyLjA2MjUiIGhlaWdodD0iMTI2Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTE2LjAzMTI1LCAtNDgpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIzMi4wNjI1IiBoZWlnaHQ9Ijk2Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPjxiPmdyYXZpdGF0aW9uYWxfcG90ZW50aWFsX2VuZXJneTwvYj48YnIgLz48aT4obWFzcyAqIGFjY2VsZXJhdGlvbl9vZl9mcmVlX2ZhbGwgKiBoZWlnaHQpPC9pPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LWVsYXN0aWNfcG90ZW50aWFsX2VuZXJneS0xMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTE0LjA1MDc4MTI1LCA2NDAuOTg0Mzc1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTUyLjY2NDA2MjUiIHdpZHRoPSIyNjAiIGhlaWdodD0iMTA1LjMyODEyNSIvPjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTEwMCwgLTM3LjY2NDA2MjUpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI3NS4zMjgxMjUiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZTsgd2hpdGUtc3BhY2U6IGJyZWFrLXNwYWNlczsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyB3aWR0aDogMjAwcHg7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+PGI+ZWxhc3RpY19wb3RlbnRpYWxfZW5lcmd5PC9iPjxiciAvPjxpPihzcHJpbmdfY29uc3RhbnQgKiBhbW91bnRfb2ZfY29tcHJlc3Npb248c3VwPjI8L3N1cD4pPC9pPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCAgIiBpZD0iZmxvd2NoYXJ0LUhlbG1ob2x0el9lbmVyZ3ktMTUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDc1OS43OTY4NzUsIDM1NS45OTIxODc1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTM5IiB3aWR0aD0iMjYwIiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMjQpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5IZWxtaG9sdHpfZW5lcmd5PC9iPiB8IDxiPkhlbG1ob2x0el9mdW5jdGlvbjwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQgICIgaWQ9ImZsb3djaGFydC1lbnRoYWxweS0xNiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAwMi42OTUzMTI1LCAzNTUuOTkyMTg3NSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii02Mi44OTg0Mzc1IiB5PSItMjciIHdpZHRoPSIxMjUuNzk2ODc1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzIuODk4NDM3NSwgLTEyKSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSI2NS43OTY4NzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+PGI+ZW50aGFscHk8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtaGVhdC0xNyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTI1NC45Mjk2ODc1LCAzNTUuOTkyMTg3NSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xMTQuNzY1NjI1IiB5PSItMjciIHdpZHRoPSIyMjkuNTMxMjUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC04NC43NjU2MjUsIC0xMikiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMTY5LjUzMTI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCAiPjxwPjxiPmhlYXQ8L2I+IHwgPGI+YW1vdW50X29mX2hlYXQ8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtR2liYnNfZW5lcmd5LTE5IiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMDAyLjY5NTMxMjUsIDQ4Ny4zMjAzMTI1KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTEzMCIgeT0iLTM5IiB3aWR0aD0iMjYwIiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTAwLCAtMjQpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlOyB3aGl0ZS1zcGFjZTogYnJlYWstc3BhY2VzOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7IHdpZHRoOiAyMDBweDsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwgIj48cD48Yj5HaWJic19lbmVyZ3k8L2I+IHwgPGI+R2liYnNfZnVuY3Rpb248L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0ICAiIGlkPSJmbG93Y2hhcnQtbGF0ZW50X2hlYXQtMjEiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEyNTQuOTI5Njg3NSwgNDg3LjMyMDMxMjUpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItNzIuMjM0Mzc1IiB5PSItMjciIHdpZHRoPSIxNDQuNDY4NzUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC00Mi4yMzQzNzUsIC0xMikiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iODQuNDY4NzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsICI+PHA+PGI+bGF0ZW50X2hlYXQ8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PC9nPjwvZz48L3N2Zz4=)

Notice, that even though all of those quantities have the same dimension and can be expressed in the same units, they have different quantity equations used to create them implicitly:

- `energy` is the most generic one and thus can be created from base quantities of `mass`, `length`, and `time`. As those are also the roots of quantities of their kinds and all other quantities are implicitly convertible to them, it means that an `energy` can be implicitly constructed from any quantity having proper powers of *mass*, *length*, and *time*.

  ```cpp
  static_assert(implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::energy));
  static_assert(implicitly_convertible(isq::mass * pow<2>(isq::height) / pow<2>(isq::time), isq::energy));
  ```
- `mechanical_energy` is a more “specialized” quantity than `energy` (not every `energy` is a `mechanical_energy`). It is why an explicit cast is needed to convert from either `energy` or the results of its quantity equation.

  ```cpp
  static_assert(!implicitly_convertible(isq::energy, isq::mechanical_energy));
  static_assert(explicitly_convertible(isq::energy, isq::mechanical_energy));
  static_assert(!implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::mechanical_energy));
  static_assert(explicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::mechanical_energy));
  ```
- `gravitational_potential_energy` is not only even more specialized one but additionally, it is special in a way that it provides its own “constrained” quantity equation. Maybe not every `mass * pow<2>(length) / pow<2>(time)` is a `gravitational_potential_energy`, but every `mass * acceleration_of_free_fall * height` is.

  ```cpp
  static_assert(!implicitly_convertible(isq::energy, gravitational_potential_energy));
  static_assert(explicitly_convertible(isq::energy, gravitational_potential_energy));
  static_assert(!implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), gravitational_potential_energy));
  static_assert(explicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), gravitational_potential_energy));
  static_assert(implicitly_convertible(isq::mass * isq::acceleration_of_free_fall * isq::height, gravitational_potential_energy));
  ```

#### 16.1.6 Modeling a quantity kind

In the physical units library, we also need an abstraction describing an entire family of quantities of the same kind. Such quantities have not only the same dimension but also can be expressed in the same units.

To annotate a quantity to represent its kind (and not just a hierarchy tree’s root quantity), we introduced a `kind_of<>` specifier. For example, to express any quantity of *length*, we need to specify `kind_of<isq::length>`. That entity behaves as any quantity of its kind. This means that it is implicitly convertible to any quantity in a tree:

```cpp
static_assert(!implicitly_convertible(isq::length, isq::height));
static_assert(implicitly_convertible(kind_of<isq::length>, isq::height));
```

Additionally, the result of operations on quantity kinds is also a quantity kind:

```cpp
static_assert(same_type<kind_of<isq::length> / kind_of<isq::time>, kind_of<isq::length / isq::time>>);
```

However, if at least one equation’s operand is not a quantity kind, the result becomes a “strong” quantity where all the kinds are converted to the hierarchy tree’s root quantities:

```cpp
static_assert(!same_type<kind_of<isq::length> / isq::time, kind_of<isq::length / isq::time>>);
static_assert(same_type<kind_of<isq::length> / isq::time, isq::length / isq::time>);
```

Please note that only a root quantity from the hierarchy tree or the one marked with `is_kind` specifier in the `quantity_spec` definition can be put as a template parameter to the `kind_of` specifier. For example, `kind_of<isq::width>` will fail to compile. However, we can call `get_kind(q)` to obtain a kind of any quantity:

```cpp
static_assert(get_kind(isq::width) == kind_of<isq::length>);
```

#### 16.1.7 Creating distinct quantity kinds with `is_kind`

Dimension-based type safety prevents many errors, but quantities may share the same dimension while representing fundamentally incompatible physical concepts. The `is_kind` specifier creates distinct quantity types within a hierarchy that cannot be mixed despite sharing dimension and parent quantity properties.

##### 16.1.7.1 Design rationale

The `is_kind` specifier addresses cases where multiple incompatible concepts must share a parent quantity’s properties (unit, quantity type) while remaining isolated from each other. This is necessary when quantities cannot be meaningfully added or compared without explicit conversion, yet derive from the same physical basis.

The `is_kind` specifier creates subkinds within an existing quantity hierarchy tree, not independent trees. Subkinds inherit properties from their parent:

- Unit of measure: *fluid head* and *water head* inherit metre from *height*; *angular measure* inherits one from *dimensionless*
- Quantity type: Subkinds inherit their parent’s quantity type, essential when they appear in derived quantities (e.g., *sampling rate* and *tempo* can use Hz because they properly model a dimensionless component divided by *duration*)

For completely independent quantities with different dimension trees, separate root quantities should be defined instead (e.g., *frequency* and *activity* are independent roots, not subkinds).

Examples:

- *Angular measure* (rad), *solid angular measure* (sr), *storage capacity* (bit) — subkinds of *dimensionless*
- *Fluid head* and *water head* in hydraulic engineering — subkinds of *height* (dimension of *length*)

##### 16.1.7.2 Syntax

A distinct quantity kind is defined by adding `is_kind` to the `quantity_spec` definition:

```cpp
inline constexpr struct fluid_head : quantity_spec<isq::height, is_kind> {} fluid_head;
inline constexpr struct water_head : quantity_spec<isq::height, is_kind> {} water_head;
```

Both `fluid_head` and `water_head` are subkinds of *height* (inheriting dimension of *length* and unit of metre), but `is_kind` makes them distinct incompatible kinds requiring explicit conversion.

##### 16.1.7.3 Type safety properties

Quantities marked with `is_kind` enforce strict type boundaries:

1. No implicit or explicit conversion between different kinds:

   ```cpp
   static_assert(!implicitly_convertible(fluid_head, water_head));
   static_assert(!explicitly_convertible(fluid_head, water_head));
   static_assert(!castable(fluid_head, water_head));
   ```
2. No arithmetic operations or comparisons between different kinds:

   ```cpp
   quantity h_fluid = fluid_head(2 * m);
   quantity h_water = water_head(10 * m);
   
   // auto sum = h_fluid + h_water;  // Compile-time error
   // bool cmp = h_fluid < h_water;  // Compile-time error
   ```
3. Explicit conversion to base quantity required for generic operations:

   ```cpp
   quantity h1 = isq::height(h_fluid);
   quantity h2 = isq::height(h_water);
   quantity sum = h1 + h2;  // OK: both are isq::height
   ```

   Note: Implicit conversion from `is_kind` quantities to their base is not allowed:

   ```cpp
   quantity<isq::height[m]> h = h_fluid;  // Compile-time error
   ```
4. Compatible with `kind_of` introspection:

   ```cpp
   static_assert(get_kind(fluid_head) == kind_of<fluid_head>);
   static_assert(get_kind(water_head) == kind_of<water_head>);
   static_assert(get_kind(isq::height) == kind_of<isq::length>);
   
   static_assert(get_kind(fluid_head) != get_kind(water_head));
   static_assert(get_kind(fluid_head) != get_kind(isq::height));
   ```

### 16.2 Systems of units

Modeling a system of units is the most important feature and a selling point of every physical units library. Thanks to that, the library can protect users from performing invalid operations on quantities and provide automated conversion factors between various compatible units.

Probably all the libraries in the wild model the [[SI]](https://www.bipm.org/en/publications/si-brochure) or at least most of it (refer to SI units of quantities of the same dimension but different kinds for more details) and many of them provide support for additional units belonging to various other systems (e.g., imperial).

#### 16.2.1 Systems of units are based on systems of quantities

Systems of quantities specify a set of quantities and equations relating to those quantities. Those equations do not take any unit or a numerical representation into account at all. In order to create a quantity, we need to add those missing pieces of information. This is where a system of units kicks in.

The [[SI]](https://www.bipm.org/en/publications/si-brochure) is explicitly stated to be based on the ISQ. Among others, it defines seven base units, one for each base quantity. In the library, this is expressed by associating a quantity kind to a unit being defined:

```cpp
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
```

The `kind_of<isq::length>` above states explicitly that this unit has an associated quantity kind. In other words, `si::metre` (and scaled units based on it) can be used to express the amount of any quantity of kind *length*.

#### 16.2.2 Units compose

One of the strongest points of the [[SI]](https://www.bipm.org/en/publications/si-brochure) system is that its units compose. This allows providing thousands of different units for hundreds of various quantities with a really small set of predefined units and prefixes. For example, one can write:

```cpp
quantity<si::metre / si::second> q;
```

to express a quantity of speed. The resulting quantity type is implicitly inferred from the unit equation by repeating exactly the same operations on the associated quantity kinds.

As units are regular values, we can easily provide a helper ad-hoc unit with:

```cpp
constexpr auto mps = si::metre / si::second;
quantity<mps> q;
```

#### 16.2.3 Many shades of the same unit

The [[SI]](https://www.bipm.org/en/publications/si-brochure) provides the names for 22 common coherent units of 22 derived quantities.

Each such named derived unit is a result of a specific predefined unit equation. For example, a unit of power quantity is defined as:

```cpp
inline constexpr struct watt : named_unit<"W", joule / second> {} watt;
```

However, a power quantity can be expressed in other units as well. For example, the following:

```cpp
auto q1 = 42 * W;
std::cout << q1 << "\n";
std::cout << q1.in(J / s) << "\n";
std::cout << q1.in(N * m / s) << "\n";
std::cout << q1.in(kg * m2 / s3) << "\n";
```

prints:

```
42 W
42 J/s
42 N m/s
42 kg m²/s³
```

All of the above quantities are equivalent and mean exactly the same.

#### 16.2.4 Constraining a derived unit to work only with a specific derived quantity

Some derived units are valid only for specific derived quantities. For example, [[SI]](https://www.bipm.org/en/publications/si-brochure) specifies both hertz and becquerel derived units with the same unit equation \(s^{-1}\). However, it also explicitly states:

> The hertz shall only be used for periodic phenomena and the becquerel shall only be used for stochastic processes in activity referred to a radionuclide.

This is why it is important for the library to allow constraining such units to be used only with a specific quantity kind:

```cpp
inline constexpr struct hertz : named_unit<"Hz", one / second, kind_of<isq::frequency>> {} hertz;
inline constexpr struct becquerel : named_unit<"Bq", one / second, kind_of<isq::activity>> {} becquerel;
```

With the above, `hertz` can only be used for *frequencies*, while `becquerel` should only be used for quantities of *activity*. This means that the following equation will not compile, improving the type-safety of the library:

```cpp
auto q = 1 * Hz + 1 * Bq;   // Fails to compile
```

#### 16.2.5 Prefixed units

Besides named units, the SI specifies also 24 prefixes (all being a power of `10`) that can be prepended to all named units to obtain various scaled versions of them.

Implementation of `std::ratio` provided by all major compilers is able to express only 16 of them. This is why, we had to find an alternative way to represent a unit’s magnitude in a more flexible way.

Each prefix is implemented as:

```cpp
template<PrefixableUnit U> struct quecto_ : prefixed_unit<"q", mag_power<10, -30>, U{}> {};
template<PrefixableUnit auto U> constexpr quecto_<decltype(U)> quecto;
```

and then a unit can be prefixed in the following way:

```cpp
inline constexpr auto qm = quecto<metre>;
```

The usage of `mag_power` not only enables providing support for SI prefixes, but it can also efficiently represent any rational magnitude. For example, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) prefixes used in the IT industry can be implemented as:

```cpp
template<PrefixableUnit U> struct yobi_ : prefixed_unit<"Yi", mag_power<2, 80>, U{}> {};
template<PrefixableUnit auto U> constexpr yobi_<decltype(U)> yobi;
```

*Please note that to improve the readability of generated types that are exposed in compiler errors and debugger, the variable template takes an NTTP and converts it to its type before passing the argument to the associated class template.*

#### 16.2.6 Scaled units

In the [[SI]](https://www.bipm.org/en/publications/si-brochure), all units are either base or derived units or prefixed versions of those. However, those are not the only options possible.

For example, there is a list of off-system units accepted for use with [[SI]](https://www.bipm.org/en/publications/si-brochure). All of those are scaled versions of the [[SI]](https://www.bipm.org/en/publications/si-brochure) units with ratios that can’t be explicitly expressed with predefined SI prefixes. Those include units like minute, hour, or electronvolt:

```cpp
inline constexpr struct minute : named_unit<"min", mag<60> * si::second> {} minute;
inline constexpr struct hour : named_unit<"h", mag<60> * minute> {} hour;
inline constexpr struct electronvolt : named_unit<"eV",
    mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * si::joule> {} electronvolt;
```

Also, units of other systems of units are often defined in terms of scaled versions of other (often SI) units. For example, the international yard is defined as:

```cpp
inline constexpr struct yard : named_unit<"yd", mag_ratio<9'144, 10'000> * si::metre> {} yard;
```

and then a `foot` can be defined as:

```cpp
inline constexpr struct foot : named_unit<"ft", mag_ratio<1, 3> * yard> {} foot;
```

For some units, a magnitude might also be irrational. The best example here is a `degree` which is defined using a floating-point magnitude having a factor of the number π (Pi):

```cpp
inline constexpr struct pi_c : mag_constant<{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, std::numbers::pi_v<long double>> {} pi_c;
inline constexpr struct pi : named_constant<symbol_text{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, mag<pi_c> * one> {} pi;
inline constexpr auto π /* U+03C0 GREEK SMALL LETTER PI */ = pi;
```

```cpp
inline constexpr struct degree : named_unit<{u8"°", "deg"}, mag_ratio<1, 180> * π * si::radian> {} degree;
```

#### 16.2.7 Common units

Adding, subtracting, or comparing two quantities of different units will force the library to find a common unit for those. This is to prevent data truncation. For the cases when one of the units is an integral multiple of the other, the resulting quantity will use a “smaller” one in its result. For example:

```cpp
static_assert((1 * kg + 1 * g).unit == g);
static_assert((1 * km + 1 * mm).unit == mm);
static_assert((1 * yd + 1 * mi).unit == yd);
```

However, in many cases an arithmetic operation on quantities of different units will result in a yet another unit. This happens when none of the source units is an integral multiple of another. In such cases, the library returns a special type that denotes that we are dealing with a common unit of such an equation:

```cpp
quantity q1 = 1 * km + 1 * mi; // quantity<common_unit<international::mile, si::kilo_<si::metre>>{}, int>
quantity q2 = 1. * rad + 1. * deg; // quantity<common_unit<si::degree, si::radian>{}, double>
```

The above is to not privilege any unit in the library:

- we shouldn’t introduce an unmentioned unit into computations (e.g., converting a `1 * mi + 1 * nmi` computation to `m` because `m` could be the privileged SI base unit),
- we shouldn’t go looking for specific units (e.g., converting a `1 * m + 1 * cm` computation to `m` because `m` is the privileged SI base unit).

Please note, that a user should never explicitly instantiate a `common_unit` class template. The library’s framework will do it based on the provided quantity equation.

#### 16.2.8 Unit symbols

Units are available via their full names or through their short symbols. To use a long version, it is enough to type:

```cpp
quantity q1 = 42 * si::metre / si::second;
quantity q2 = 42 * si::kilo<si::metre> / si::hour;
```

To simplify how we spell it a short, user-friendly symbols are provided in a dedicated subnamespace in systems definitions:

```cpp
namespace si::unit_symbols {

constexpr auto m = si::metre;
constexpr auto km = si::kilo<si::metre>;
constexpr auto s = si::second;
constexpr auto h = si::hour;

}
```

Unit symbols introduce a lot of short identifiers into the current namespace. This is why they are opt-in. A user has to explicitly “import” them from a dedicated `unit_symbols` namespace:

```cpp
using namespace si::unit_symbols;

quantity q1 = 42 * m / s;
quantity q2 = 42 * km / h;
```

or:

```cpp
using si::unit_symbols::m;
using si::unit_symbols::km;
using si::unit_symbols::s;
using si::unit_symbols::h;

quantity q1 = 42 * m / s;
quantity q2 = 42 * km / h;
```

Thanks to [[P1949R7]](https://wg21.link/p1949r7) we also provide alternative object identifiers using Unicode characters in their names for most unit symbols. The code using Unicode looks nicer, but it is harder to type on the keyboard. This is why we provide both versions of identifiers for such units.

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Portable only</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">With Unicode characters</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity resistance = 60 * kohm;
quantity capacitance = 100 * uF;</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity resistance = 60 * kΩ;
quantity capacitance = 100 * µF;</code></pre></td>
</tr>
</table>

It is worth noting that not all such units may get Unicode identifiers. Some of them do not have the XID_Start property. For example:

- ℃ (degree Celsius),
- ° (degree)
- ′ (minute)
- ″ (second)

## 17 Text output

A quantity value contains a numerical value and a unit. Both of them may have various text representations. Not only numbers but also units can be formatted in many different ways. Additionally, every dimension can be represented as a text as well.

This chapter will discuss the different options we have here.

*Note: For now, there is no standardized way to handle formatted text input in the C++ standard library, so this paper does not propose any approach to convert text to quantities. If [[P1729R3]](https://wg21.link/p1729r3) will be accepted by the LEWG, then we will add a proper “Text input” chapter as well.*

### 17.1 Symbols

The definitions of dimensions, units, prefixes, and constants require unique text symbols to be assigned for each entity. Those symbols can be composed to express dimensions and units of base and derived quantities.

#### 17.1.1 Symbol definition examples

*Note: The below code examples are based on the latest version of the [[mp-units]](https://mpusz.github.io/mp-units) library and might not be the final version proposed for standardization.*

Dimensions:

```cpp
inline constexpr struct dim_length : base_dimension<"L"> {} dim_length;
inline constexpr struct dim_mass : base_dimension<"M"> {} dim_mass;
inline constexpr struct dim_time : base_dimension<"T"> {} dim_time;
inline constexpr struct dim_electric_current : base_dimension<"I"> {} dim_electric_current;
inline constexpr struct dim_thermodynamic_temperature : base_dimension<{u8"Θ", "O"}> {} dim_thermodynamic_temperature;
inline constexpr struct dim_amount_of_substance : base_dimension<"N"> {} dim_amount_of_substance;
inline constexpr struct dim_luminous_intensity : base_dimension<"J"> {} dim_luminous_intensity;
```

Units:

```cpp
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct gram : named_unit<"g", kind_of<isq::mass>> {} gram;
inline constexpr auto kilogram = kilo<gram>;

inline constexpr struct newton : named_unit<"N", kilogram * metre / square(second)> {} newton;
inline constexpr struct joule : named_unit<"J", newton * metre> {} joule;
inline constexpr struct watt : named_unit<"W", joule / second> {} watt;
inline constexpr struct coulomb : named_unit<"C", ampere * second> {} coulomb;
inline constexpr struct volt : named_unit<"V", watt / ampere> {} volt;
inline constexpr struct farad : named_unit<"F", coulomb / volt> {} farad;
inline constexpr struct ohm : named_unit<{u8"Ω", "ohm"}, volt / ampere> {} ohm;
```

Prefixes:

```cpp
template<PrefixableUnit U> struct micro_ : prefixed_unit<{u8"µ", "u"}, mag_power<10, -6>, U{}> {};
template<PrefixableUnit U> struct milli_ : prefixed_unit<"m", mag_power<10, -3>, U{}> {};
template<PrefixableUnit U> struct centi_ : prefixed_unit<"c", mag_power<10, -2>, U{}> {};
template<PrefixableUnit U> struct deci_  : prefixed_unit<"d", mag_power<10, -1>, U{}> {};
template<PrefixableUnit U> struct deca_  : prefixed_unit<"da", mag_power<10, 1>, U{}> {};
template<PrefixableUnit U> struct hecto_ : prefixed_unit<"h", mag_power<10, 2>, U{}> {};
template<PrefixableUnit U> struct kilo_  : prefixed_unit<"k", mag_power<10, 3>, U{}> {};
template<PrefixableUnit U> struct mega_  : prefixed_unit<"M", mag_power<10, 6>, U{}> {};
```

Constants:

```cpp
inline constexpr struct hyperfine_structure_transition_frequency_of_cs :
  named_constant<{u8"Δν_Cs", "dv_Cs"}, mag<9'192'631'770> * hertz> {} hyperfine_structure_transition_frequency_of_cs;
inline constexpr struct speed_of_light_in_vacuum :
  named_constant<"c", mag<299'792'458> * metre / second> {} speed_of_light_in_vacuum;
inline constexpr struct planck_constant :
  named_constant<"h", mag_ratio<662'607'015, 100'000'000> * mag_power<10, -34> * joule * second> {} planck_constant;
inline constexpr struct elementary_charge :
  named_constant<"e", mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * coulomb> {} elementary_charge;
inline constexpr struct boltzmann_constant :
  named_constant<"k", mag_ratio<1'380'649, 1'000'000> * mag_power<10, -23> * joule / kelvin> {} boltzmann_constant;
inline constexpr struct avogadro_constant :
  named_constant<"N_A", mag_ratio<602'214'076, 100'000'000> * mag_power<10, 23> / mole> {} avogadro_constant;
inline constexpr struct luminous_efficacy :
  named_constant<"K_cd", mag<683> * lumen / watt> {} luminous_efficacy;
```

*Note: Two symbols always have to be provided if the primary symbol contains characters outside of the [basic literal character set](https://en.cppreference.com/w/cpp/language/charset). The first must be provided as a UTF-8 literal and may contain any Unicode characters. The second one must provide an alternative spelling and only use characters from within of [basic literal character set](https://en.cppreference.com/w/cpp/language/charset).*

#### 17.1.2 Lack of Unicode subscript characters

Unicode provides only a minimal set of characters available as subscripts, which are often used to differentiate various constants and quantities of the same kind. To workaround this issue, [[mp-units]](https://mpusz.github.io/mp-units) uses `'_'` character to specify that the following characters should be considered a subscript of the symbol.

#### 17.1.3 Symbols for quantity types

Although the ISQ defined in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides symbols for each quantity type, there is little use for them in the C++ code. In the [[mp-units]](https://mpusz.github.io/mp-units) project, we never had a request to provide such symbol definitions. Even though having them for completeness could be nice, they seem to not be required by the domain experts for their daily jobs. Also, it is worth noting that providing those raises some additional standardization and implementation challenges.

If we decide to provide symbols, the rest of this chapter provides the domain information to assess the complexity and potential issues with standardization and implementation of those.

All ISQ quantities have an official symbol assigned in their definitions, and how those should be printed is exactly specified. [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly states:

> The quantity symbols shall be written in italic (sloping) type, irrespective of the type used in the rest of the text.

Additionally, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides additional requirements for printing quantities of vector and tensor characters:

- vectors should be printed with a boldface type or have a right arrow above the letter symbol (e.g., ***a*** or \(\mathit{\overrightarrow{a}}\)),
- tensors should use either boldface sans serif type or have two arrows above the letter symbol (e.g., ***T*** or \(\overrightarrow{\overrightarrow{T}}\)).

*Note: In the above examples, the second symbol with arrows above should also use letters written in italics. The author could not find a way to format it properly in this document.*

There are also a few requirements for printing subscripts of quantity types. [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) states:

> The following principles for the printing of subscripts apply:
> 
> - A subscript that represents a physical quantity or a mathematical variable, such as a running number, is printed in italic (sloping) type.
> - Other subscripts, such as those representing words or fixed numbers, are printed in roman (upright) type.

It is worth noting that only a limited set of Unicode characters are available as subscripts. Those are often used to differentiate various quantities of the same kind.

For example, it is impossible to encode the symbols of the following quantities:

- *c*<sub>sat</sub> - *specific heat capacity at saturated vapour pressure*,
- *μ*<sub>JT</sub> - *Joule-Thomson coefficient*,
- *w*<sub>H<sub>2</sub>O</sub> - *mass fraction of water*,
- *σ*<sub>Ω,E</sub> - *direction and energy distribution of cross section*,
- *d*<sub>1/2</sub> - *half-value thickness*,
- *Φ*<sub>e,λ</sub> - *spectral radiant flux*.

It is important to state that the same issues are related to constant definitions. For them, in the Symbol definition examples chapter, we proposed to use the `'_'` character instead, as stated in Lack of Unicode subscript characters. We could use the same practice here.

Another challenge here might be related to the fact that [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) often provides more than one symbol for the same quantity. For example:

- *frequency* can use *f* or *ν*,
- *time constant* can use *τ* or *T* (*T* is also the only symbol provided for the *period duration* quantity),
- *thickness* can use *d* or *δ*,
- *diameter* can use *d* or *D* (which again conflicts with the *diameter* symbol).

Last but not least, it is worth noting that symbols of ISQ base quantities are not necessary the same as official dimension symbols of those quantities:

| Quantity type | Quantity type symbol | Dimension symbol |
| --- | --- | --- |
| *length* | *l*, *L* | L |
| *mass* | *m* | M |
| *time* | *t* | T |
| *electric current* | *I*, *i* | I |
| *thermodynamic temperature* | *T*, *Θ* | Θ |
| *amount of substance* | *n*(X) | N |
| *luminous intensity* | *I*<sub>v</sub>, (*I*) | J |

Founding a way to define, use, and print named quantity types is not enough. What should also be covered here is the text output of derived quantities. There are plenty of operations that one might do on scalar, vector, and tensor quantities, and all of them result in another quantity type, which should also be able to be printed in the console text output.

Taking all the challenges and issues mentioned above, we do not propose providing quantity type symbols in their definitions and any text input/output support for those.

#### 17.1.4 `fixed_string`

As shown above, symbols are provided as class NTTPs in the library. This means that the string type used for such a purpose has to satisfy the structural type requirements of the C++ language. One of such requirements is to expose all the data members publicly. So far, none of the existing string types in the C++ standard library satisfies such requirements. This is why we need to introduce a new type.

Such type should:

- satisfy structural type requirements,
- be equality comparable and potentially totally ordered,
- store and provide concatenation support for zero-ended strings,
- provide storage that, if set at compile time, would also be available for read-only access at runtime,
- provide at least read-only access to the contained storage.

Such a type does not need to expose a string-like interface. In case its interface is immutable, we can easily wrap it with `std::string_view` to get such an interface for free.

This type is being proposed separately in [[P3094R6]](https://wg21.link/p3094r6).

#### 17.1.5 `symbol_text`

Many symbols of units, prefixes, and constants require using a Unicode character set. For example:

- Θ - thermodynamic temperature dimension
- µ - micro
- Ω - ohm
- ℃ - degree Celsius
- ℉ - degree Fahrenheit
- ° - degree
- ′ - arcminute
- ″ - arcsecond
- ᵍ - gradian
- Å - angstrom
- M_☉ - solar mass
- Δν_Cs - hyperfine structure transition frequency of Cs
- g₀ - standard gravity
- μ₀ - magnetic constant
- c₀ - speed of light
- H₀ - hubble constant

The library should provide such Unicode output by default to be consistent with official systems’ specifications.

On the other hand, plenty of terminals do not support Unicode characters. Also, general engineering experience shows that people often prefer to work with a basic literal character set. This is why all such entities should provide an alternative spelling in their definitions.

This is where `symbol_text` comes into play. It is a simple wrapper over the two `fixed_string` objects:

```cpp
template<std::size_t N, std::size_t M>
class symbol_text {
public:
  fixed_u8string<N> utf8_;    // exposition only
  fixed_string<M> portable_;  // exposition only

  constexpr explicit(false) symbol_text(char ch);
  consteval explicit(false) symbol_text(const char (&txt)[N + 1]);
  constexpr explicit(false) symbol_text(const fixed_string<N>& txt);
  consteval symbol_text(const char8_t (&u)[N + 1], const char (&a)[M + 1]);
  constexpr symbol_text(const fixed_u8string<N>& u, const fixed_string<M>& a);

  constexpr const auto& utf8() const;
  constexpr const auto& portable() const;

  constexpr bool empty() const;

  template<std::size_t N2, std::size_t M2>
  constexpr friend symbol_text<N + N2, M + M2> operator+(const symbol_text& lhs, const symbol_text<N2, M2>& rhs);

  template<std::size_t N2, std::size_t M2>
  friend constexpr auto operator<=>(const symbol_text& lhs, const symbol_text<N2, M2>& rhs) noexcept;

  template<std::size_t N2, std::size_t M2>
  friend constexpr bool operator==(const symbol_text& lhs, const symbol_text<N2, M2>& rhs) noexcept;
};

symbol_text(char) -> symbol_text<1, 1>;

template<std::size_t N>
symbol_text(const char (&)[N]) -> symbol_text<N - 1, N - 1>;

template<std::size_t N>
symbol_text(const fixed_string<N>&) -> symbol_text<N, N>;

template<std::size_t N, std::size_t M>
symbol_text(const char8_t (&)[N], const char (&)[M]) -> symbol_text<N - 1, M - 1>;

template<std::size_t N, std::size_t M>
symbol_text(const fixed_u8string<N>&, const fixed_string<M>&) -> symbol_text<N, M>;
```

It is important to note that the `utf8_` text representation is used only when the output is of either:

- `char8_t` type,
- `char` and `std::text_encoding::literal().mib() == std::text_encoding::id::UTF8`.

Otherwise, `portable_` is used.

#### 17.1.6 Symbols for derived entities

##### 17.1.6.1 `character_set`

ISQ and [[SI]](https://www.bipm.org/en/publications/si-brochure) standards always specify symbols using Unicode encoding. This is why it is a default and primary target for text output. However, in some applications or environments, a standard portable text output using only the characters from the [basic literal character set](https://en.cppreference.com/w/cpp/language/charset) can be preferred by users.

This is why the library provides an option to change the default encoding to the portable one with:

```cpp
enum class character_set : std::int8_t {
  utf8,        // µs; m³;  L²MT⁻³
  portable,    // us; m^3; L^2MT^-3
  default_encoding = utf8
};
```

##### 17.1.6.2 Symbols of derived dimensions

###### 17.1.6.2.1 `dimension_symbol_formatting`

`dimension_symbol_formatting` is a data type describing the configuration of the symbol generation algorithm.

```cpp
struct dimension_symbol_formatting {
  character_set char_set = character_set::default_encoding;
};
```

###### 17.1.6.2.2 `dimension_symbol()`

Returns a `std::string_view` with the symbol of a dimension for the provided configuration:

```cpp
template<dimension_symbol_formatting fmt = dimension_symbol_formatting{}, typename CharT = char, Dimension D>
consteval std::string_view dimension_symbol(D);
```

*Note: It could be refactored to `dimension_symbol(D, fmt)` when [[P1045R1]](https://wg21.link/p1045r1) is available.*

For example:

```cpp
static_assert(dimension_symbol<{.char_set = character_set::portable}>(isq::power.dimension) == "L^2MT^-3");
```

###### 17.1.6.2.3 `dimension_symbol_to()`

Inserts the generated dimension symbol into the output text iterator at runtime.

```cpp
template<typename CharT = char, std::output_iterator<CharT> Out, Dimension D>
constexpr Out dimension_symbol_to(Out out, D d, dimension_symbol_formatting fmt = dimension_symbol_formatting{});
```

For example:

```cpp
std::string txt;
dimension_symbol_to(std::back_inserter(txt), isq::power.dimension, {.char_set = character_set::portable});
std::cout << txt << "\n";
```

The above prints:

```
L^2MT^-3
```

##### 17.1.6.3 Symbols of derived units

###### 17.1.6.3.1 `unit_symbol_formatting`

`unit_symbol_formatting` is a data type describing the configuration of the symbol generation algorithm. It contains three orthogonal fields, each with a default value.

```cpp
enum class unit_symbol_solidus : std::int8_t {
  one_denominator,  // m/s;   kg m⁻¹ s⁻¹
  always,           // m/s;   kg/(m s)
  never,            // m s⁻¹; kg m⁻¹ s⁻¹
  default_solidus = one_denominator
};

enum class unit_symbol_separator : std::int8_t {
  space,          // kg m²/s²
  half_high_dot,  // kg⋅m²/s²  (valid only for Unicode encoding)
  default_separator = space
};

struct unit_symbol_formatting {
  character_set char_set = character_set::default_encoding;
  unit_symbol_solidus solidus = unit_symbol_solidus::default_solidus;
  unit_symbol_separator separator = unit_symbol_separator::default_separator;
};
```

`unit_symbol_solidus` impacts how the division of unit symbols is being presented in the text output. By default, the ‘/’ will be printed if only one unit component is in the denominator. Otherwise, the exponent syntax will be used.

`unit_symbol_separator` specifies how multiple multiplied units should be separated from each other. By default, the space (’ ’) will be used as a separator.

###### 17.1.6.3.2 `unit_symbol()`

Returns a `std::string_view` with the symbol of a unit for the provided configuration:

```cpp
template<unit_symbol_formatting fmt = unit_symbol_formatting{}, typename CharT = char, Unit U>
consteval std::string_view unit_symbol(U);
```

*Note: It could be refactored to `unit_symbol(U, fmt)` when [[P1045R1]](https://wg21.link/p1045r1) is available.*

For example:

```cpp
static_assert(unit_symbol<{.solidus = unit_symbol_solidus::never,
                           .separator = unit_symbol_separator::half_high_dot}>(kg * m / s2) == "kg⋅m⋅s⁻²");
```

###### 17.1.6.3.3 `unit_symbol_to()`

Inserts the generated unit symbol into the output text iterator at runtime.

```cpp
template<typename CharT = char, std::output_iterator<CharT> Out, Unit U>
constexpr Out unit_symbol_to(Out out, U u, unit_symbol_formatting fmt = unit_symbol_formatting{});
```

For example:

```cpp
std::string txt;
unit_symbol_to(std::back_inserter(txt), kg * m / s2,
               {.solidus = unit_symbol_solidus::never, .separator = unit_symbol_separator::half_high_dot});
std::cout << txt << "\n";
```

The above prints:

```
kg⋅m⋅s⁻²
```

#### 17.1.7 Symbols of scaled units

Here are a few examples of scaled unit text output in action:

```cpp
inline constexpr Unit auto my_unit_1 = mag_ratio<1, 4> * si::second;
inline constexpr Unit auto my_unit_2 = mag_power<10, 4> * si::metre;
inline constexpr Unit auto my_unit_3 = mag<25> * mag_power<10, 4> * si::metre;

std::cout << 100 * my_unit_1 << "\n";
std::cout << 100 * my_unit_2 << "\n";
std::cout << 100 * my_unit_3 << "\n";
```

The above prints:

```
100 (1/4 s)
100 (10⁴ m)
100 (25 × 10⁴ m)
```

As we can see a scaled unit has a magnitude and a reference unit. To denote the scope of such a unit, we currently enclose it in `(...)`.

In most cases scaled units are hidden behind named units so the above outputs are a bit artifical. However, there are a few real-life where a user directly faces a scaled unit. For example:

```cpp
inline constexpr Unit auto L_per_100km = L / (mag<100> * km);
```

The above is a derived unit of litre divided by a scaled unit of `100` kilometers. For example, the following:

```cpp
std::cout << 6.7 * L_per_100km << "\n";
```

prints:

```
6.7 L/(100 km)
```

The current output of the fuel consumption unit is only one of the options here. It favors a derived unit over a scaled unit (i.e., the resulting type is `derived_unit<non_si::litre, per<scaled_unit<{some magnitude representing 100}, si::kilo<si::metre>>>>`). Another option would be to prefer a scaled unit so the result would be `scaled_unit<{some magnitude representing 1/100}, derived_unit<non_si::litre, per<si::kilo<si::metre>>>` and the output would look like:

```
6.7 (1/100 L/km)
```

The output could also look like this:

```
6.7 × 10⁻² L/km
```

but this, even though it is mathematically correct, is the poorest to express the intent here. The unit we use daily is the number of liters consumed for `100 km`, and not for a single `km`, which the last output suggests (i.e., “6.7 hundredths of a liter per kilometer”).

This is why we initially proposed the first version. However, on one of the meetings it was brought that this approach also leads to some issues in case of other quantities.

According to the current rules, the following code:

```cpp
std::cout << 10 * L_per_100km * (20 * km) << "\n";
```

prints the following output:

```
200 L km/(100 km)
```

At least for now, the units do not simplify which may look suprising.

Another thing worth noting here is that in case a value of a numerator or denumerator is greater or equal `1000` we use an exponential notation:

```cpp
inline constexpr Unit auto L_per_1000km = L / (mag<1000> * km);
std::cout << 10 * L_per_1000km << "\n";
```

prints:

```
10 L/(10³ km)
```

A motivation for that is that typically, for a value of `1000` or greater, a user could use a larger SI prefix (even though it would not make sense for kilometers).

All of the above are the inputs for a discussion and we are open to fine-tuning this behavior according to the LEWG guidelines.

#### 17.1.8 Symbols of common units

Some common units expressed with a specialization of the `common_unit` class template need special printing rules for their symbols. As they represent a minimum set of equivalent common units resulting from the addition or subtraction of multiple quantities, we print all of them as a scaled version of the source unit. For example, the following:

```cpp
std::cout << 1 * km + 1 * mi << "\n";
std::cout << 1 * nmi + 1 * mi << "\n";
std::cout << 1 * km / h + 1 * m / s << "\n";
std::cout << 1. * rad + 1. * deg << "\n";
```

prints:

```
40771 [(1/25146 mi), (1/15625 km)]
108167 [(1/50292 mi), (1/57875 nmi)]
23 [(1/5 km/h), (1/18 m/s)]
183.142 [(1/π°), (1/180 rad)]
```

Thanks to the above, it might be easier for the user to reason about the magnitude of the resulting unit and its impact on the value stored in the quantity.

It is important to note that this output is provided only for intermediate results of the equations, as shown above. A user usually knows which unit should be used, and explicit conversion can be made to achieve that. For example:

```cpp
std::cout << (1 * km + 1 * mi).in<double>(km) << "\n";
```

prints:

```
2.60934 km
```

#### 17.1.9 Unicode characters and their portable replacements

Library’s framework requires some Unicode characters for text output. The below table lists all of them together with the recommended portable replacements:

| Name | Symbol | C++ code | Portable alternative |
| --- | --- | --- | --- |
| SUPERSCRIPT ZERO | ⁰ | `u8"\u2070"` | `"0"` |
| SUPERSCRIPT ONE | ¹ | `u8"\u00b9"` | `"1"` |
| SUPERSCRIPT TWO | ² | `u8"\u00b2"` | `"2"` |
| SUPERSCRIPT THREE | ³ | `u8"\u00b3"` | `"3"` |
| SUPERSCRIPT FOUR | ⁴ | `u8"\u2074"` | `"4"` |
| SUPERSCRIPT FIVE | ⁵ | `u8"\u2075"` | `"5"` |
| SUPERSCRIPT SIX | ⁶ | `u8"\u2076"` | `"6"` |
| SUPERSCRIPT SEVEN | ⁷ | `u8"\u2077"` | `"7"` |
| SUPERSCRIPT EIGHT | ⁸ | `u8"\u2078"` | `"8"` |
| SUPERSCRIPT NINE | ⁹ | `u8"\u2079"` | `"9"` |
| SUPERSCRIPT MINUS | ⁻ | `u8"\u207b"` | `"-"` |
| MULTIPLICATION SIGN | × | `u8"\u00d7"` | `"x"` |
| GREEK SMALL LETTER PI | π | `u8"\u03c0"` | `"pi"` |
| DOT OPERATOR | ⋅ | `u8"\u22C5"` | `<none>`<sup>1</sup> |

Here is an example of how the above are being used in a code:

```cpp
static_assert(unit_symbol(kilogram * metre / square(second)) == "kg m/s²");
static_assert(unit_symbol<usf{.separator = half_high_dot}>(kilogram * metre / square(second)) == "kg⋅m/s²");
static_assert(unit_symbol<usf{.char_set = portable}>(kilogram * metre / square(second)) == "kg m/s^2");
static_assert(unit_symbol<usf{.solidus = never}>(kilogram * metre / square(second)) == "kg m s⁻²");
static_assert(unit_symbol<usf{.char_set = portable, .solidus = never}>(kilogram * metre / square(second)) == "kg m s^-2");

static_assert(unit_symbol(mag_ratio<1, 18000> * metre / second) == "[1/18 × 10⁻³ m]/s");
static_assert(unit_symbol<usf{.char_set = portable}>(mag_ratio<1, 18000> * metre / second) == "[1/18 x 10^-3 m]/s");

static_assert(unit_symbol(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[2⁻¹ π⁻¹ m]");
static_assert(unit_symbol<usf{.solidus = always}>(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[1/(2 π) m]");
static_assert(unit_symbol<usf{.char_set = portable, .solidus = always}>(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[1/(2 pi) m]");
```

Additionally, if we decide to provide `per_mille` unit together with the framework (next to `one`, `percent`, and `parts_per_million`) we will need a symbol for it as well:

| Name | Symbol | C++ code | Portable alternative |
| --- | --- | --- | --- |
| PER MILLE SIGN | ‰ | u8”030” | ??? |

There is no good choice for a portable replacement here. We may try to be brief and use “%o” ([Wikipedia uses this symbol as a redirect for per mille](https://en.wikipedia.org/wiki/Per_mille)) or provide a longer textual string. The problem is that there is more than one option to chose from here ([names mentioned in Wikipedia](https://en.wikipedia.org/wiki/Per_mille)):

- “per mille” (even though it is consistent with the official name it is not a good option here as it looks like multiplication of two symbols),
- “per mil” and “per mill” (same as above),
- “permil”, “permill”, and “permille” (how to spell it correctly?).

### 17.2 `space_before_unit_symbol` customization point

The [[SI]](https://www.bipm.org/en/publications/si-brochure) says:

> The numerical value always precedes the unit and a space is always used to separate the unit from the number. … The only exceptions to this rule are for the unit symbols for degree, minute and second for plane angle, `°`, `′` and `″`, respectively, for which no space is left between the numerical value and the unit symbol.

There are more units with such properties. For example, per mille(`‰`).

To support the above, the library exposes `space_before_unit_symbol` customization point. By default, its value is `true` for all the units. This means that a number and a unit will be separated by the space in the output text. To change this behavior, a user should provide a explicit specialization for a specific unit:

```cpp
template<>
constexpr bool space_before_unit_symbol<non_si::degree> = false;
```

The above works only for the default formatting or for the format strings that use `%?` placement field (`std::format("{}", q)` is equivalent to `std::format("{:%N%?%U}", q)`).

In case a user provides custom format specification (e.g., `std::format("{:%N %U}", q)`), the library will always obey this specification for all the units (no matter what the actual value of the `space_before_unit_symbol` customization point is) and the separating space will always be used in this case.

### 17.3 Output streams

The easiest way to print a dimension, unit, or quantity is to provide its object to the output stream:

```cpp
const quantity v1 = avg_speed(220. * km, 2 * h);
const quantity v2 = avg_speed(140. * mi, 2 * h);
std::cout << v1 << '\n';            // 110 km/h
std::cout << v2 << '\n';            // 70 mi/h
std::cout << v2.unit << '\n';       // mi/h
std::cout << v2.dimension << '\n';  // LT⁻¹
```

The text output will always print the value using the default formatting for this entity.

#### 17.3.1 Output stream formatting

Only basic formatting can be applied for output streams. It includes control over width, fill, and alignment.

The numerical value of the quantity will be printed according to the current stream state and standard manipulators may be used to customize that (assuming that the underlying representation type respects them).

```cpp
std::cout << "|" << std::setw(10) << 123 * m << "|\n";                       // |     123 m|
std::cout << "|" << std::setw(10) << std::left << 123 * m << "|\n";          // |123 m     |
std::cout << "|" << std::setw(10) << std::setfill('*') << 123 * m << "|\n";  // |123 m*****|
```

Detailed formatting of any entity may be obtained with `std::format()` usage and then provided to the stream output if needed.

*Note: Custom stream manipulators may be provided to control a dimension and unit symbol output if requested by WG21.*

### 17.4 Text formatting

The library provides custom formatters for `std::format` facility, which allows fine-grained control over what and how it is being printed in the text output.

#### 17.4.1 Controlling width, fill, and alignment

Formatting grammar for all the entities provides control over width, fill, and alignment. The C++ standard grammar tokens `fill-and-align` and `width` are being used. They treat the entity as a contiguous text to be aligned. For example, here are a few examples of the quantity numerical value and symbol formatting:

```cpp
std::println("|{:0}|", 123 * m);     // |123 m|
std::println("|{:10}|", 123 * m);    // |     123 m|
std::println("|{:<10}|", 123 * m);   // |123 m     |
std::println("|{:>10}|", 123 * m);   // |     123 m|
std::println("|{:^10}|", 123 * m);   // |  123 m   |
std::println("|{:*<10}|", 123 * m);  // |123 m*****|
std::println("|{:*>10}|", 123 * m);  // |*****123 m|
std::println("|{:*^10}|", 123 * m);  // |**123 m***|
```

It is important to note that in the second line above, the quantity text is aligned to the right by default, which is consistent with the formatting of numeric types. Units and dimensions behave as text and, thus, are aligned to the left by default.

#### 17.4.2 Dimension formatting

```
dimension-format-spec = [fill-and-align], [width], [dimension-spec];
dimension-spec        = [character-set];
character-set         = 'U' | 'P';
```

In the above grammar:

- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `character-set` token specifies the symbol text encoding:
  - `U` (default) uses the **UTF-8** symbols defined by [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (e.g., `LT⁻²`),
  - `P` forces non-standard **portable** output (e.g., `LT^-2`).

Dimension symbols of some quantities are specified to use Unicode signs by the ISQ (e.g., `Θ` symbol for the *thermodynamic temperature* dimension). The library follows this by default. From the engineering point of view, sometimes Unicode text might not be the best solution as terminals of many (especially embedded) devices can output only letters from the basic literal character set only. In such a case, the dimension symbol can be forced to be printed using such characters thanks to `character-set` token:

```cpp
std::println("{}", isq::dim_thermodynamic_temperature);   // Θ
std::println("{:P}", isq::dim_thermodynamic_temperature); // O
std::println("{}", isq::power.dimension);                 // L²MT⁻³
std::println("{:P}", isq::power.dimension);               // L^2MT^-3
```

#### 17.4.3 Unit formatting

```
unit-format-spec      = [fill-and-align], [width], [unit-spec];
unit-spec             = [character-set], [unit-symbol-solidus], [unit-symbol-separator], [L]
                      | [character-set], [unit-symbol-separator], [unit-symbol-solidus], [L]
                      | [unit-symbol-solidus], [character-set], [unit-symbol-separator], [L]
                      | [unit-symbol-solidus], [unit-symbol-separator], [character-set], [L]
                      | [unit-symbol-separator], [character-set], [unit-symbol-solidus], [L]
                      | [unit-symbol-separator], [unit-symbol-solidus], [character-set], [L];
unit-symbol-solidus   = '1' | 'a' | 'n';
unit-symbol-separator = 's' | 'd';
```

In the above grammar:

- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `unit-symbol-solidus` token specifies how the division of units should look like:
  - ‘1’ (default) outputs `/` only when there is only **one** unit in the denominator, otherwise negative exponents are printed (e.g., `m/s`, `kg m⁻¹ s⁻¹`)
  - ‘a’ **always** uses solidus (e.g., `m/s`, `kg/(m s)`)
  - ‘n’ **never** prints solidus, which means that negative exponents are always used (e.g., `m s⁻¹`, `kg m⁻¹ s⁻¹`)
- `unit-symbol-separator` token specifies how multiplied unit symbols should be separated:
  - ‘s’ (default) uses **space** as a separator (e.g., `kg m²/s²`)
  - ‘d’ uses half-high **dot** (`⋅`) as a separator (e.g., `kg⋅m²/s²`) (requires the UTF-8 encoding)
- ‘L’ is reserved for possible future localization use in case C++ standard library gets access to the ICU-like database.

*Note: The intent of the above grammar was that the elements of `unit-spec` can appear in any order as they have unique characters. Users shouldn’t have to remember the order of those tokens to control the formatting of a unit symbol.*

The above grammar for `unit-symbol-solidus` is consistent with the current state of [[mp-units]](https://mpusz.github.io/mp-units). However, a few aternatives are possible:

```
unit-symbol-solidus   = '1' | 'a' | 'n';
unit-symbol-solidus   = 'o' | 'a' | 'n';
unit-symbol-solidus   = '1' | '*' | '0';
unit-symbol-solidus   = '1' | '*' | '-';
unit-symbol-solidus   = '1' | '+' | '-';
```

Unit symbols of some quantities are specified to use Unicode signs by the [[SI]](https://www.bipm.org/en/publications/si-brochure) (e.g., `Ω` symbol for the *resistance* quantity). The library follows this by default. From the engineering point of view, sometimes Unicode text might not be the best solution as terminals of many (especially embedded) devices can output only letters from the basic literal character set only. In such a case, the unit symbol can be forced to be printed using such characters thanks to `character-set` token:

```cpp
std::println("{}", si::ohm);      // Ω
std::println("{:P}", si::ohm);    // ohm
std::println("{}", us);           // µs
std::println("{:P}", us);         // us
std::println("{}", m / s2);       // m/s²
std::println("{:P}", m / s2);     // m/s^2
```

Additionally, both [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) leave some freedom on how to print unit symbols. This is why two additional tokens were introduced.

`unit-symbol-solidus` specifies how the division of units should look like. By default, `/` will be used only when the denominator contains only one unit. However, with the ‘a’ or ‘n’ options, we can force the facility to print the `/` character always (even when there are more units in the denominator), or never, in which case a parenthesis will be added to enclose all denominator units.

```cpp
std::println("{}", m / s);          // m/s
std::println("{}", kg / m / s2);    // kg m⁻¹ s⁻²
std::println("{:a}", m / s);        // m/s
std::println("{:a}", kg / m / s2);  // kg/(m s²)
std::println("{:n}", m / s);        // m s⁻¹
std::println("{:n}", kg / m / s2);  // kg m⁻¹ s⁻²
```

The `unit-symbol-separator` token allows us to obtain the following outputs:

```cpp
std::println("{}", kg * m2 / s2);    // kg m²/s²
std::println("{:d}", kg * m2 / s2);  // kg⋅m²/s²
```

*Note: ‘d’ requires the UTF-8 encoding to be set.*

#### 17.4.4 Quantity formatting

```
quantity-format-spec        = [fill-and-align], [width], [quantity-specs], [defaults-specs];
quantity-specs              = conversion-spec;
                            | quantity-specs, conversion-spec;
                            | quantity-specs, literal-char;
literal-char                = ? any character other than '{', '}', or '%' ?;
conversion-spec             = '%', placement-type;
placement-type              = subentity-id | '?' | '%';
defaults-specs              = ':', default-spec-list;
default-spec-list           = default-spec;
                            | default-spec-list, default-spec;
default-spec                = subentity-id, '[' format-spec ']';
subentity-id                = 'N' | 'U' | 'D';
format-spec                 = ? as specified by the formatter for the argument type ?;
```

In the above grammar:

- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `placement-type` token specifies which entity should be put and where:
  - ‘N’ inserts a default-formatted numerical value of the quantity,
  - ‘U’ inserts a default-formatted unit of the quantity,
  - ‘D’ inserts a default-formatted dimension of the quantity,
  - ‘?’ inserts an optional separator between the number and a unit based on the value of `space_before_unit_symbol` for this unit,
  - ‘%’ just inserts ‘%’ character.
- `defaults-specs` token allows overwriting defaults for the underlying formatters with the custom format string. Each override starts with a subentity identifier (‘N’, ‘U’, or ‘D’) followed by the format string enclosed in square brackets.

##### 17.4.4.1 Two levels of format specification

The grammar above introduces a two-level design that may initially look unfamiliar, so it is worth describing in detail. A `quantity` is a wrapper over a numerical value tagged with a unit (and, indirectly, a dimension). When formatting it, there are two independent concerns, and each `:` delimiter opens the section that addresses one of them:

- The first `:` (as in any `std::format` replacement field) starts the **quantity-level** format specification. Here we provide `fill-and-align` and `width` that treat the entire quantity output as one contiguous piece of text, and `quantity-specs` — a small layout language built from the `%N`, `%U`, `%D`, `%?`, and `%%` placeholders — that decides *which* components (numerical value, unit, dimension) are printed and *how* they are arranged.
- The second `:` starts the **component-level** format specifications (`defaults-specs`). A `quantity` is only a numerical wrapper. It does not — and should not — assume any knowledge about the format-spec grammar of the representation type it stores. This is why the specs provided in `N[...]`, `U[...]`, and `D[...]` are not interpreted by the quantity formatter at all. They are forwarded verbatim to the formatters of the respective components and processed there.

We deliberately chose *not* to follow the `%Q`/`%q` convention that `std::chrono::duration` uses for its value and unit suffix. Those identifiers are easy to confuse with one another, do not hint at what they stand for, and — being lower/upper-case variants of the same letter — leave no room for a mnemonic third option. A `quantity` additionally exposes its *dimension*, which the `chrono` grammar has no concept of and therefore no placeholder for. We instead use the self-explanatory `%N` (numerical value), `%U` (unit), and `%D` (dimension), where each letter directly evokes the component it inserts.

Separating the two concerns means that overriding how a single component is formatted does not force us to respell the default quantity layout. For example, to round the number to two decimal places while keeping the default arrangement of the components intact, it is enough to leave the quantity-level spec empty and provide only the component-level override:

```cpp
std::println("{::N[.2f]}", 100. * km / (3 * h));  // 33.33 km/h
```

We did not have to write out the default `%N%?%U` layout just to attach a precision to the number. Had numerical-value modifiers been embedded directly in the quantity format-spec (as is the case for `std::chrono::duration`), every such customization would have required repeating the entire default format string verbatim.

This two-level `{::...}` shape is not novel. The C++ standard library already uses it to format the elements of a range. For a range, the first `:` opens the range’s own format spec, and the optional second `:` introduces a format spec that is forwarded to the formatter of each element:

```cpp
std::vector v{1.2345, 2.3456, 3.4567};
std::println("{}", v);        // [1.2345, 2.3456, 3.4567]
std::println("{::.2f}", v);   // [1.23, 2.35, 3.46]
std::println("{:n:.2f}", v);  // 1.23, 2.35, 3.46
```

Here `.2f` after the second `:` is not interpreted by the range formatter — it is handed unchanged to the `double` formatter used for every element. The `quantity` formatter follows exactly the same principle, so users already familiar with formatting the contents of a container should find the `quantity` grammar consistent with their expectations.

##### 17.4.4.2 Default formatting

To format `quantity` values, the formatting facility uses `quantity-format-spec`. If left empty, the default formatting is applied. The same default formatting is also applied to the output streams. This is why the following code lines produce the same output:

```cpp
std::cout << "Distance: " << 123 * km << "\n";
std::cout << std::format("Distance: {}\n", 123 * km);
std::cout << std::format("Distance: {:%N%?%U}\n", 123 * km);
```

Please note that for some quantities the `{:%N %U}` format may provide a different output than the default one, as some units have `space_before_unit_symbol` customization point explicitly set to `false` (e.g., `%` and `°`).

##### 17.4.4.3 Quantity numerical value, unit symbol, or both?

Thanks to the grammar provided above, the user can easily decide to either:

- print a whole quantity:

  ```cpp
  std::println("Speed: {}", 120 * km / h);
  ```

  ```
  Speed: 120 km/h
  ```
- provide custom quantity formatting:

  ```cpp
  std::println("Speed: {:%N in %U}", 120 * km / h);
  ```

  ```
  Speed: 120 in km/h
  ```
- provide custom formatting for components:

  ```cpp
  std::println("Speed: {::N[.2f]U[n]}", 100. * km / (3 * h));
  ```

  ```
  Speed: 33.33 km h⁻¹
  ```
- print only specific components (numerical value, unit, or dimension):

  ```cpp
  std::println("Speed:\n- number: {0:%N}\n- unit: {0:%U}\n- dimension: {0:%D}", 120 * km / h);
  ```

  ```
  Speed:
  - number: 120
  - unit: km/h
  - dimension: LT⁻¹
  ```

`placement-type` greatly simplify element access to the elements of the quantity. Without them the second case above would require the following:

```cpp
const quantity q = 120 * km / h;
std::println("Speed:\n- number: {}\n- unit: {}\n- dimension: {}",
             q.numerical_value_ref_in(q.unit), q.unit, q.dimension);
```

`default-spec` is crutial to provide formatting of user-defined representation types. Initially, [[mp-units]](https://mpusz.github.io/mp-units) library was providing numerical value modifiers inplace of its format specification similarly to `std::chrono::duration` formatter. However, it:

- worked only with fundamental arithmetic types and was not able to adjust to different format specifications of custom representation types,
- was quite hard to parse and format everything in a 100% compatible way with the formatting specified in the C++ standard and already implemented in the underlying standard library.

##### 17.4.4.4 Formatting of the quantity numerical value

The representation type used as a numerical value of a quantity must provide its own formatter specialization. It will be called by the quantity formatter with the format-spec provided by the user in the `N` defaults specification.

In case we use C++ fundamental arithmetic types with our quantities the standard formatter specified in [format.string.std](https://wg21.link/format.string.std) will be used. The rest of this chapter assumes that it is the case and provides some usage examples.

`sign` token allows us to specify how the value’s sign is being printed:

```cpp
std::println("{0},{0::N[+]},{0::N[-]},{0::N[ ]}", 1 * m);   // 1 m,+1 m,1 m, 1 m
std::println("{0},{0::N[+]},{0::N[-]},{0::N[ ]}", -1 * m);  // -1 m,-1 m,-1 m,-1 m
```

where:

- `+` indicates that a sign should be used for both non-negative and negative numbers,
- `-` indicates that a sign should be used for negative numbers and negative zero only (this is the default behavior),
- `<space>` indicates that a leading space should be used for non-negative numbers other than negative zero, and a minus sign for negative numbers and negative zero.

`precision` token is allowed only for floating-point representation types:

```cpp
std::println("{::N[.0]}", 1.2345 * m);   // 1 m
std::println("{::N[.1]}", 1.2345 * m);   // 1 m
std::println("{::N[.2]}", 1.2345 * m);   // 1.2 m
std::println("{::N[.3]}", 1.2345 * m);   // 1.23 m
std::println("{::N[.0f]}", 1.2345 * m);  // 1 m
std::println("{::N[.1f]}", 1.2345 * m);  // 1.2 m
std::println("{::N[.2f]}", 1.2345 * m);  // 1.23 m
```

`type` specifies how a value of the representation type is being printed. For integral types:

```cpp
std::println("{::N[b]}", 42 * m);    // 101010 m
std::println("{::N[B]}", 42 * m);    // 101010 m
std::println("{::N[d]}", 42 * m);    // 42 m
std::println("{::N[o]}", 42 * m);    // 52 m
std::println("{::N[x]}", 42 * m);    // 2a m
std::println("{::N[X]}", 42 * m);    // 2A m
```

The above can be printed in an alternate version thanks to the `#` token:

```cpp
std::println("{::N[#b]}", 42 * m);   // 0b101010 m
std::println("{::N[#B]}", 42 * m);   // 0B101010 m
std::println("{::N[#o]}", 42 * m);   // 052 m
std::println("{::N[#x]}", 42 * m);   // 0x2a m
std::println("{::N[#X]}", 42 * m);   // 0X2A m
```

For floating-point values, the `type` token works as follows:

```cpp
std::println("{::N[a]}",   1.2345678 * m);      // 1.3c0ca2a5b1d5dp+0 m
std::println("{::N[.3a]}", 1.2345678 * m);      // 1.3c1p+0 m
std::println("{::N[A]}",   1.2345678 * m);      // 1.3C0CA2A5B1D5DP+0 m
std::println("{::N[.3A]}", 1.2345678 * m);      // 1.3C1P+0 m
std::println("{::N[e]}",   1.2345678 * m);      // 1.234568e+00 m
std::println("{::N[.3e]}", 1.2345678 * m);      // 1.235e+00 m
std::println("{::N[E]}",   1.2345678 * m);      // 1.234568E+00 m
std::println("{::N[.3E]}", 1.2345678 * m);      // 1.235E+00 m
std::println("{::N[g]}",   1.2345678 * m);      // 1.23457 m
std::println("{::N[g]}",   1.2345678e8 * m);    // 1.23457e+08 m
std::println("{::N[.3g]}", 1.2345678 * m);      // 1.23 m
std::println("{::N[.3g]}", 1.2345678e8 * m);    // 1.23e+08 m
std::println("{::N[G]}",   1.2345678 * m);      // 1.23457 m
std::println("{::N[G]}",   1.2345678e8 * m);    // 1.23457E+08 m
std::println("{::N[.3G]}", 1.2345678 * m);      // 1.23 m
std::println("{::N[.3G]}", 1.2345678e8 * m);    // 1.23E+08 m
```

##### 17.4.4.5 Extensions to `std-format-spec`

Both [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) are recommending printing numbers into separated into groups of three:

> To facilitate the reading of numbers with many digits, these may be separated into groups of three, counting from the decimal sign towards the left and the right. In the case where there is no decimal part (and thus no decimal marker), the counting shall be from the right-most digit, towards the left. No group shall contain more than three digits, except that when there are only four digits before or after the decimal marker it is customary not to use a space to isolate a single digit. Where such separation into groups of three is used, the groups shall be separated by a small space and not by a point or a comma or by any other means.
> 
> EXAMPLE 1: 12 345
> 
> The practice of grouping digits in this way is a matter of choice. It is not always followed in certain specialized applications such as engineering drawings and scripts to be read by a computer. The separation into groups of three should not be used for ordinal numbers used as reference numbers. A year, when given by four digits, shall always be written without a space between the digits.

As of today, no flag in `std-format-spec` would force it. Similar output may be obtained thanks to localization, but international standards mentioned above recommend that for every user, no matter what localization option is being used.

##### 17.4.4.6 Inconsistencies with `std::chrono::duration`

This library prints the quantities and their units according to specific ISO specifications. Unfortunately, this is not the case for `std::chrono::duration`:

```cpp
using my_duration = std::chrono::duration<int, std::ratio<1, 4>>;

inline constexpr Unit auto my_unit = mag_ratio<1, 4> * si::second;

std::println("{}", std::chrono::seconds(42));
std::println("{}", 42 * s);
std::println("{}", my_duration(100));
std::println("{}", 100 * my_unit);
```

The above prints:

```
42s
42 s
100[1/4]s
100 (1/4 s)
```

We are unsure if that is a problem that we should be worried about. If so, we could consider adding ISO-compatible formatting to `std::chrono` abstractions, but it is not planned in the scope of this paper.

### 17.5 Quantity point text output

Text output is provided for `quantity_point` when its point origin equals `default_point_origin(R)` — the library-chosen default for the given reference:

- For references without an offset unit (e.g., `quantity_point<isq::length[m]>`), `default_point_origin` is `natural_point_origin<QuantitySpec>`, the mathematical zero. The stored quantity is unambiguous and can be printed directly:

  ```cpp
  quantity_point qp{42 * m};
  std::println("{}", qp);          // "42 m"
  ```
- For references whose unit carries a built-in origin (e.g., `quantity_point<deg_C>`), `default_point_origin` is the unit’s canonical reference point (`si::ice_point`). The output matches the conventional notation:

  ```cpp
  quantity_point temp = point<deg_C>(20.);
  std::println("{}", temp);        // "20 ℃"
  ```

Text output is **not** provided when a non-default origin is used. The stored value is a displacement from a domain-specific reference whose name the library cannot know. The same numeric value can describe entirely different physical locations depending on the origin — `42 m` above sea level, a mountain top, or the centre of Mars are all distinct points. For such cases the displacement should be extracted explicitly, with an application-defined label added to make the value unambiguous:

```cpp
std::cout << altitude.quantity_ref_from(sea_level) << " AMSL";  // "42 m AMSL"
```

## 18 Core Library Framework scope

After a rough introduction of most of the features and abstractions in the library, it might be good to discuss the scope for the Core Library Framework.

We have several significant features to consider here:

- **Core library**: `quantity`, symbolic expressions, dimensions, units, references, and concepts for them,
- **Quantity kinds**: support quantities of the same dimension that should be distinct, e.g., *frequency*, *activity*, and *modulation_rate*, or *energy* and *moment_of_force*
- **Various quantities of the same kind**: support quantities of the same kind that should be distinct, e.g., *width*, *height*, *wavelength* (all of the kind *length*),
- **The affine space**: `quantity_point`, point origins, and concepts for them,
- **Text output**: for `quantity`, units, and dimensions,

Please note that the above only lists the features present in this proposal. Additional features, like definitions of specific systems of quantities and units, math utilities, and other extensions, may be provided in the follow-up papers. We chose not to include those features here because they can be separately added later. This also means that we believe that all of the features listed above should be provided in the first release of the library.

To prove that, let’s try to identify possible problems if a specific feature is excluded from the MVP scope:

1. **Core library**

   It just has to be there with all of the components listed. Otherwise, nothing works.
2. **Quantity kinds**

   If we remove this feature, we would not be able to make a distinction between `Hz`, `Bq`, and `Bd`, or `rad`, `sr` and `bit`, or `Gy` and `Sv` as the quantities associated with those units have the same dimensions. It is not only about units. It also means that we will be able to pass a quantity of *solid angular measure* to a function that takes `angular measure`. Users will also not be able to model their own distinct abstractions like we showed in the case of the audio example (samples, beats, etc.). We also need to note that we need that feature to be able to model the International System of Quantities (ISQ). Skipping it is a serious usability and safety issue that we should prevent.

   Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds (possibly of the same dimension).
3. **Various quantities of the same kind**

   Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

   Beyond convertibility, hierarchies validate derived quantity construction: *kinetic energy* cannot implicitly convert from `m g h` (recipe for *gravitational potential energy*). This validates correct ingredients in quantity equations.

   Without hierarchies, we cannot:
   - Distinguish specific *lengths* (*width*, *height*, *radius*), *energies* (*kinetic*, *potential*, *thermal*, *enthalpy*), or custom dimensions
   - Validate specific *energy* ingredients (e.g., *height* for *gravitational potential energy*)
   - Separate *plane angle* (radian) from *solid angle* (steradian) in dimensionless hierarchy
   - Discriminate between ratios, storage capacities, or algorithmic complexities
   - Support quantity characters (scalar vs. vector operations, character-specific operations)
   - Enforce correct units for different *power* types (`W` vs `VA` vs `var` in AC circuits)
   - Model physical systems like *water head*, *mass density* specializations, or audio examples (samples, beats, sounds)
   - Provide strongly-typed counts extending the dimensionless tree without custom dimension overhead

   **Removing quantity hierarchies eliminates quantity-safety entirely**, reducing the library to basic dimensional analysis. Postponing affects SI system modeling irreversibly—SI units provided without quantity specifications cannot be improved later. ISQ modeling becomes impossible.
4. **The affine space**

   This looks like a feature that can be added later, and it is partially true. However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin. If we postpone and release SI first, then we will not be able to improve the degree Celsius definition later on.

   Skipping this feature also means that we will lack very important building block in modeling many problems in engineering. Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.

   Also, without it, we will not be able to provide proper `std::chrono` compatibility.
5. **Text output**

   Again, this looks like a purely additive feature, but if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless. If we do not intend to have text output, we should remove symbol text from the core framework class templates. This is why we should take that decision now.

## 19 Safety

Physical quantities and units libraries prevent errors at compile time through multiple safety layers. All safety features described here have **zero runtime overhead**—they’re enforced entirely at compile time, providing safety without performance cost.

### 19.1 Overview of safety levels

This library provides six distinct safety levels:

1. **Dimension Safety** - Prevents mixing incompatible dimensions (e.g., adding *length* to *time*)
2. **Unit Safety** - Prevents unit mismatches and eliminates manual scaling factors
3. **Representation Safety** - Protects against overflows and precision loss
4. **Quantity Kind Safety** - Prevents arithmetic on quantities of different kinds (e.g., `Hz` vs `Bq`)
5. **Quantity Safety** - Enforces correct quantity relationships and equation ingredients
6. **Mathematical Space Safety** - Distinguishes points (absolute positions) from vectors (differences)

All major C++ units libraries provide dimension safety (level 1) and unit safety (level 2). Some provide representation safety (level 3) and mathematical space safety (level 6). However, [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.

### 19.2 Dimension safety

Dimension safety prevents mixing quantities with incompatible dimensions through automatic dimensional analysis:

```cpp
quantity<si::metre / si::second> speed = 100 * km / h;  // OK: km/h is speed (same as m/s)
quantity<si::second> time = 2 * h;                      // OK: hour is time (same as second)
quantity<si::metre> distance = speed * time;            // OK: length
// quantity<si::metre> distance = 2 * h;                // Error: incompatible dimensions!
// quantity<si::metre> distance = speed / time;         // Error: wrong dimension!
// auto result = distance + time;                       // Error: cannot add length and time!
```

All major C++ units libraries provide this foundational feature enabling dimensional analysis.

### 19.3 Unit safety

Unit safety ensures compatible units at interface boundaries (function arguments, return types, component integration).

```cpp
// Function accepts any length and time units
quantity<si::metre / si::second> avg_speed(quantity<si::metre> d, quantity<si::second> t)
{
  return d / t;
}

quantity distance = 220 * km;
quantity time = 2 * h;
quantity<km / h> speed = avg_speed(distance, time);  // 110 km/h - automatic conversion
```

Unit conversions are automated and checked at compile-time:

```cpp
auto q1 = 5 * km;
std::cout << q1.in(m) << '\n';           // prints: 5000 m
quantity<si::metre, int> q2 = q1;        // OK: km → m
```

Unlike `std::chrono::duration` which uses `std::ratio`, this library supports arbitrary conversion factors including irrational numbers (π for radians/degrees) and extreme ratios (electronvolt: 1 eV = 1.602176634×10⁻¹⁹ J).

#### 19.3.1 Safe quantity numerical value getters

Legacy APIs often require raw numerical values. Always specify the unit explicitly:

```cpp
void legacy_func(std::int64_t seconds);
```

**Bad** (like `std::chrono::duration::count()` - doesn’t specify unit):

```cpp
struct X {
  std::vector<std::chrono::milliseconds> vec;
};

X x;
x.vec.emplace_back(42s);
legacy_func(x.vec[0].count());  // Wrong if storage does not match seconds!
```

**Good** (explicit unit specification):

```cpp
struct X {
  std::vector<quantity<si::milli<si::second>>> vec;
};

X x;
x.vec.emplace_back(42 * s);
legacy_func(x.vec[0].numerical_value_in(si::second));        // Safe
legacy_func(x.vec[0].force_numerical_value_in(si::second));  // If truncation OK
```

The member function `numerical_value_ref_in(Unit)` enables direct access without conversion or copying:

```cpp
void legacy_func(const int& joules);

quantity q1 = 42 * J;
quantity q2 = 42 * N * (2 * m);
quantity q3 = 42 * kJ;

legacy_func(q1.numerical_value_ref_in(si::joule));  // OK
legacy_func(q2.numerical_value_ref_in(si::joule));  // OK (equivalent unit)
legacy_func(q3.numerical_value_ref_in(si::joule));  // Compile-time error (different magnitude)
legacy_func((4 * J + 2 * J).numerical_value_ref_in(si::joule));  // Compile-time error (rvalue)
```

This prevents most dangling references while acknowledging the value category ≠ lifetime limitation (see [[Value Category Is Not Lifetime]](https://quuxplusone.github.io/blog/2019/03/11/value-category-is-not-lifetime/)).

### 19.4 Representation safety

Representation safety protects against numerical issues like overflow, underflow, and precision loss during conversions and arithmetic operations.

#### 19.4.1 Truncation prevention

Conversions that would lose precision with integral types are prevented at compile-time:

```cpp
quantity q1 = 5 * m;
std::cout << q1.in(km) << '\n';              // Compile-time error
quantity<si::kilo<si::metre>, int> q2 = q1;  // Compile-time error
```

Converting 5 meters to kilometers with `int` would truncate to 0. To allow such conversions, use floating-point types or explicit casts:

```cpp
quantity q1 = 5. * m;                        // double representation
std::cout << q1.in(km) << '\n';              // OK: prints 0.005 km
```

```cpp
quantity q1 = 5 * m;                         // int representation  
std::cout << q1.in<double>(km) << '\n';      // OK: explicit conversion to double
std::cout << q1.force_in(km) << '\n';        // OK: explicit truncation (prints 0 km)
quantity<si::kilo<si::metre>, int> q2 = value_cast<km>(q1);  // OK: explicit cast
```

The same protection applies to representation type conversions:

```cpp
quantity q1 = 2.5 * m;
quantity<si::metre, int> q2 = q1;                   // Compile-time error
quantity<si::metre, int> q3 = value_cast<int>(q1);  // OK: explicit truncation
```

Combined conversions (unit + representation) are supported to prevent intermediate overflow:

```cpp
value_cast<Unit, Representation>(Quantity);
value_cast<Representation, Unit>(Quantity);
value_cast<Unit, Representation>(QuantityPoint);
value_cast<Representation, Unit>(QuantityPoint);
q.force_in<Representation>(Unit);
qp.force_in<Representation>(Unit);
```

#### 19.4.2 Scaling overflow prevention

Converting small integral types between units can overflow even for non-zero values:

```cpp
quantity q1 = std::int8_t(1) * km;
quantity q2 = q1.force_in(m);   // Compile-time error (factor 1'000 > max int8_t)
if(q1 != 1 * m) { /* ... */ }   // Compile-time error
```

The conversion factor (1000) exceeds `std::int8_t` range, so the library prevents the conversion even though `0 * km` would technically work. See Integer overflow for details.

*Note: No library can prevent runtime arithmetic overflow at compile time (e.g., `quantity * 2`), nor can they prevent floating-point overflow/underflow. For such cases, use custom representation types with runtime checks.*

#### 19.4.3 `explicit` is not explicit enough

Consider:

```cpp
struct X {
  std::vector<std::chrono::milliseconds> vec;
};
X x;
x.vec.emplace_back(42);  // Compiles but fragile!
```

If someone changes `milliseconds` to `microseconds`, the code still compiles but calculations are wrong by 1000×. The solution: require both number and unit:

```cpp
struct X {
  std::vector<quantity<si::milli<si::second>>> vec;
};
X x;
x.vec.emplace_back(42);       // Compile-time error
x.vec.emplace_back(42 * ms);  // OK
```

Similarly, `quantity_point` requires explicit origin association (unlike `std::chrono::time_point`):

```cpp
quantity_point qp1 = mean_sea_level + 42 * m;
quantity_point qp2 = default_ac_temperature + 2 * delta<deg_C>;
```

### 19.5 Quantity kind safety

Quantity kind safety distinguishes between quantities sharing the same dimension but representing different physical concepts.

What should `1 * Hz + 1 * Bq + 1 * Bd` equal? Several leading libraries disagree:

- [[Boost.Units]](https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html) claims the answer to be 2 Hz (bauds not supported),
- [[nholthaus/units]](https://github.com/nholthaus/units) claims it is 2 s<sup>-1</sup> (bauds not supported),
- [[Pint]](https://pint.readthedocs.io/en/stable/index.html) library in Python claims the result is 3.0 Hz,
- [[JSR 385]](https://unitsofmeasurement.github.io/indriya) library in Java throws an exception—**the only correct answer**.

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) states:

- Quantities may be grouped into categories that are **mutually comparable**
- Mutually comparable quantities are **quantities of the same kind**
- Quantities **cannot be added or subtracted unless they belong to the same category**
- Quantities of the **same kind** have the **same dimension**
- Quantities of the **same dimension are not necessarily of the same kind**

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly notes:

> Measurement units of quantities of the same quantity dimension may be designated by the same name and symbol even when the quantities are not of the same kind. For example, joule per kelvin and J/K are respectively the name and symbol of both a measurement unit of heat capacity and a measurement unit of entropy, which are generally not considered to be quantities of the same kind. **However, in some cases special measurement unit names are restricted to be used with quantities of specific kind only**. For example, the measurement unit ‘second to the power minus one’ (1/s) is called hertz (Hz) when used for frequencies and becquerel (Bq) when used for activities of radionuclides.

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly states that *frequency* (Hz) and *activity* (Bq) are different kinds—they should not be comparable, added, or subtracted. Allowing such operations leads to safety issues when unrelated quantities of the same dimension are accidentally added or assigned:

```cpp
quantity absorbed_dose = 1.5 * Gy;
quantity dose_equivalent = 2.0 * Sv;

// auto result = absorbed_dose + dose_equivalent;           // Compile-time error!
// Error: cannot add absorbed dose and dose equivalent (both L²T⁻², but different kinds)

// QuantityOf<isq::absorbed_dose> auto d = 2.5 * Sv;        // Compile-time error!
// Error: cannot initialize absorbed dose with dose equivalent
```

*[[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety, fully distinguishing all SI quantity kinds including Gy/Sv, Hz/Bq, and rad/sr.*

### 19.6 Quantity safety

Quantity safety is the highest level, ensuring semantic correctness through:

1. **Quantity Type Correctness** - Hierarchies, conversions, and quantity equation ingredient validation
2. **Quantity Character Correctness** - Representation types and character-specific operations

#### 19.6.1 Quantity hierarchies

Dimension-only libraries can’t distinguish between different quantities of the same kind:

```cpp
class Box {
  quantity<isq::area[m2]> base_;
  quantity<isq::length[m]> height_;  // Can't distinguish length, width, height!
public:
  Box(quantity<isq::length[m]> l, quantity<isq::length[m]> w, quantity<isq::length[m]> h)
    : base_(l * w), height_(h) {}
};
```

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) defines hierarchies: *width*, *height*, *radius* are distinct but all are *lengths*. This library models these hierarchies to prevent errors:

```cpp
// Quantity Type: Hierarchy prevents mixing energy types
void process_kinetic(quantity<isq::kinetic_energy[J]> ke) { /* ... */ }

quantity pe = isq::potential_energy(100 * J);
// process_kinetic(pe);                                                   // Compile-time error!
// Error: cannot pass potential_energy where kinetic_energy is required

// Quantity Type: Ingredient validation requires specific quantity types
quantity<isq::height[m]> h = 5 * m;
quantity<isq::gravitational_potential_energy[J]> Ep = mass * g * height;  
// quantity<isq::gravitational_potential_energy[J]> wrong = mass * g * width;  // Compile-time error!
// Error: cannot form gravitational potential energy from width
```

See Systems of quantities for details.

#### 19.6.2 Safe operations of vector and tensor quantities

While talking about quantities and units libraries, everyone expects that the library will protect (preferably at compile-time) from accidentally replacing multiplication with division operations or vice versa. Everyone knows and expects that the multiplication of *length* and *time* should not result in *speed*. It does not mean that such a quantity equation is invalid. It just results in a quantity of a different type.

If we expect the above protection for scalar quantities, we should also strive to provide similar guarantees for vector and tensor quantities. First, the multiplication or division of two vectors or tensors is not even mathematically defined. Such operations should be impossible on quantities using vector or tensor representation types.

What multiplication and division are for scalars, the dot and cross products are for vector quantities. The result of the first one is a scalar. The second one results in a vector perpendicular to both vectors passed as arguments. A good quantities and units library should protect the user from making such an error of accidentally replacing those operations.

Vector and tensor quantities can be implemented in two ways:

1. Encapsulating multiple quantities into a homogeneous vector or tensor representation type

   This solution is the most common in the C++ market. It requires the quantities library to provide only basic arithmetic operations (addition, subtraction, multiplication, and division) which are being used to calculate the result of linear algebra math. However, this solution can’t provide any compile-time safety described above, and will also crash when someone passes a proper vector and tensor representation type to a quantity, expecting it to work.
2. Encapsulating a vector or tensor as a representation type of a quantity

   This provides all the required type safety, but requires the library to implement more operations on quantities and properly constrain them so they are selectively enabled when needed. Besides [[mp-units]](https://mpusz.github.io/mp-units), the only library that supports such an approach is [[Pint]](https://pint.readthedocs.io/en/stable/index.html). Such a solution requires the following operations to be exposed for quantity types (note that character refers to the algebraic structure of either scalar, vector and tensor):
   - `a + b` - addition where both arguments should be of the same quantity kind and character
   - `a - b` - subtraction where both arguments should be of the same quantity kind and character
   - `a % b` - modulo where both arguments should be of the same quantity kind and character
   - `a * b` - multiplication where one of the arguments has to be a scalar
   - `a / b` - division where the divisor has to be scalar
   - `a ⋅ b` - dot product of two vectors
   - `a × b` - cross product of two vectors
   - `|a|` - magnitude (norm) of a vector, i.e., `norm(a)`
   - `a ⊗ b` - tensor product of two vectors or tensors
   - `a ⋅ b` - inner product of two tensors
   - `a ⋅ b` - inner product of tensor and vector
   - `a : b` - scalar product of two tensors

Additionally, the library knows the expected quantity character, which is provided (implicitly or explicitly) in the definition of each quantity type. Thanks to that, it prevents the user, for example, from providing a vector representation type for *speed*.

```cpp
quantity q1 = isq::speed(60 * km / h);                       // OK
quantity q2 = isq::speed(la_vector{0, 0, -60} * km / h);     // Compile-time error
quantity q3 = isq::velocity(60 * km / h);                    // OK
quantity q4 = isq::velocity(la_vector{0, 0, -60} * km / h);  // OK
```

As we can see above, such features additionally improves the compile-time safety of the library by ensuring that quantities are created with proper quantity equations and are using correct representation types.

#### 19.6.3 Complex quantities

Complex quantities enforce domain-specific construction rules. Example: *complex power* requires *active power* and *reactive power* in correct order:

```cpp
quantity<isq::complex_power[V * A], std::complex<double>> complex = get_power();
quantity<isq::active_power[W]> active = complex.real();
quantity<isq::reactive_power[var]> reactive = complex.imag();
quantity<isq::apparent_power[V * A]> apparent = complex.modulus();
```

### 19.7 Mathematical space safety

Mathematical space safety distinguishes between **quantity points** (absolute positions) and **quantity vectors** (differences/displacements). `quantity` represents vectors; `quantity_point` represents points. This prevents nonsensical operations:

**Forbidden operations:**

- Adding two points: `home + airport` (what is “Boston + New York”?)
- Subtracting vector from point: `distance - airport`
- Scaling points: `2 * airport`
- Mixing incompatible point origins

**Allowed operations:**

- Subtracting points yields vector: `airport - home` → distance
- Adding vector to point: `home + distance` → new location
- Scaling vectors: `2 * distance`

Example with temperature: *Temperatures* are points on a scale with an origin; *temperature changes* are vectors. You can add *temperature changes*, but adding two *temperatures* is meaningless:

```cpp
// Points: Positions on a scale with an origin
quantity_point room_temp = point<deg_C>(20.);
quantity_point outside_temp = point<deg_C>(5.);

quantity temp_diff = room_temp - outside_temp;      // OK: 15 K (vector)
// auto temp_sum = room_temp + outside_temp;        // Compile-time error!
// Error: cannot add points (meaningless: what is 20 °C + 5 °C?)

// Vectors: Differences between values
quantity temp_change = delta<K>(10);
quantity_point new_temp = room_temp + temp_change;  // OK: point + vector = 30 °C
quantity total_change = temp_change + temp_change;  // OK: vector + vector = 20 K

// auto wrong = temp_change - room_temp;            // Compile-time error!
// Error: cannot subtract point from vector (meaningless: what is 10 K - 20 °C?)
```

Examples where mathematical space safety prevents errors: *temperature* (cannot add 20 °C + 10 °C, but can compute difference), *time* (cannot add two *timestamps*, but can subtract them), *position* (cannot add GPS coordinates, but can compute *displacement*), *altitude* (cannot add two *elevations*, but can compute *height* difference).

### 19.8 Safety pitfalls

#### 19.8.1 Integer division

If we expect `120 * km / (2 * h)` to return `60 km / h`, we have to agree with the fact that `5 * km / (24 * h)` returns `0 km/h`. We can’t do a range check at runtime to dynamically adjust scales and types based on the values of provided function arguments.

The same applies to:

```cpp
static_assert(5 * h / (120 * min) == 0 * one);
```

We may consider adding a special mode to detect the above cases at compile-time and try to bring the unit to a common unit before doing the operation. However, it will make it inconsistent with the following code:

```cpp
static_assert(2 * m * (5 * h) / (120 * min) == 0 * m);
```

If we decide to change the current behavior, it would:

- make generic programming harder,
- should be enabled only for integers (inconsistent resulting units with floating-point mode),
- would make it harder to express ratios of hugely different units of the same dimension (e.g., Hubble constant is expressed in `km/s/Mpc`).

This is why floating-point representation types are recommended as a default to store the numerical value of a quantity. Some popular physical units libraries even [forbid integer division at all](https://aurora-opensource.github.io/au/main/troubleshooting/#integer-division-forbidden).

#### 19.8.2 Integer overflow

**The problem**: Unit conversions multiply by hidden factors. Comparing `11 * m > 12 * yd` converts both to a common unit (800 μm), multiplying by ~1000× under the hood—easy to overflow small integer types.

**Mitigation strategies:** in fact, at the time of writing, new strategies are still being developed and tested. Here are the main strategies we have seen.

##### 19.8.2.1 Do nothing

This is the simplest approach, and probably also the most popular: make the users responsible for avoiding overflow. The documentation may simply warn them to check their values ahead of time, as in this [example from the bernedom/SI library](https://github.com/bernedom/SI/blob/main/doc/implementation-details.md#implicit-ratio-conversion--possible-loss-of-precision). This valid approach places substantial responsibility on users, many unaware of the risk. Since unit conversions are hard to spot, this likely leads to the highest incidence of overflow bugs.

##### 19.8.2.2 Curate user-facing types

[`std::chrono`](https://en.cppreference.com/w/cpp/chrono/duration) crafts user-facing types with generous ranges: all named durations shorter than a day (hours to nanoseconds) represent ±292 years. Users within this range who stick to these primary types avoid overflow.

This works well for time-only libraries but doesn’t scale to multi-dimensional units libraries where quantity types proliferate and users can create arbitrary combinations on the fly.

##### 19.8.2.3 Adapt to risk

Overflow risk depends on: (1) conversion factor size (bigger = more risk)<sup>2</sup>, and (2) maximum representable value (larger = less risk).

An adaptive policy can forbid conversions where the “smallest overflowing value” is “small enough to be scary”. [[Au]](https://aurora-opensource.github.io/au) uses threshold 2,147: if this value converts without overflow, permit the operation. This prevents operations failing on values under 1,000 while allowing common patterns like `500 * mega<hertz>` in `int32_t`. Production experience confirms this provides good default protection.

This paper is more conservative: we fail conversion if the representation can’t handle value `1` converted to the destination unit (see Scaling overflow prevention), pessimizing only the `0` case.

##### 19.8.2.4 Check every conversion at runtime

Runtime checks guarantee perfect safety. While unit conversions rarely appear in hot loops, making runtime cost worthwhile, the main challenge is error handling (exceptions, `optional`, `expected`, contracts, etc.).

A promising approach separates error detection and response: the library provides boolean checkers for overflow/truncation, then each project uses these with their preferred error handling mechanism.

##### 19.8.2.5 Delegate to rep

Perhaps the most appealing approach to overflow in units libraries is to delegate the problem to another library entirely. Quantity types can work with any underlying numeric type (called the “rep”, as in the `chrono` library) that satisfies certain concepts related to basic arithmetic. If that rep comes from a library that is dedicated to providing overflow-safe numeric types, then the problem is solved without any additional effort on the units library side.

This approach currently suffers from at least two significant downsides. First, it is less thoroughly tested in production usage, so we don’t know what the practical pitfalls are. Second, raw numeric types are likely to be overwhelmingly common in practice, and using this approach alone would leave this group of users unprotected—a group where less-experienced users are likely to be over-represented. Therefore, this can’t be the *only* solution to overflow.

#### 19.8.3 Lack of safe numeric types

Integers overflow on arithmetic (causing expensive failures [[Ariane flight V88]](https://en.wikipedia.org/wiki/Ariane_flight_V88)) and truncate on narrowing assignment. Floating-point types lose precision on narrowing, and `int64_t` to `double` conversion also loses precision.

Safe numeric types in the standard library would address these concerns as `quantity` reps. A type trait indicating value-preserving conversions would also help.

#### 19.8.4 Potential surprises during units composition

Units compose to create derived units (`constexpr Unit auto kmph = km / h;`), an industry standard in [[Boost.Units]](https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html) and [[Pint]](https://pint.readthedocs.io/en/stable/index.html).

However, order of operations can surprise users:

```cpp
quantity q = 60 * km / 2 * h;  // Results in 30 km⋅h, not 30 km/h
quantity q = 60 * km / (2 * h); // Requires parentheses for 30 km/h
```

Generic code can also produce unexpected types:

```cpp
template<typename T>
auto make_length(T v) { return v * si::metre; }

quantity v = 42 * m;
quantity q = make_length(v);  // Returns area (m²), not length!
```

[[mp-units]](https://mpusz.github.io/mp-units) initially disallowed multiplying/dividing quantities by units to prevent this, but requiring `60 * (km / h)` proved too verbose and confusing.

These issues always surface as compile-time errors when assigning to explicitly-typed quantities:

```cpp
quantity<si::kilo<si::metre> / non_si::hour, int> q1 = 60 * km / 2 * h;  // Error
QuantityOf<isq::speed> auto q3 = 60 * km / 2 * h;                        // Error
quantity<si::metre, int> q1 = make_length(42 * m);                       // Error
QuantityOf<isq::length> auto make_length(T v) { return v * si::metre; }  // Constrains return type
```

#### 19.8.5 Limitations of systems of quantities

Modeling systems of quantities improves safety but has pitfalls in corner cases.

##### 19.8.5.1 Allowing irrational quantity combinations

While `length * length → area` makes sense bidirectionally, `width * height → area` is unidirectional—not all areas are width×height products:

```cpp
static_assert(implicitly_convertible(isq::width * isq::height, isq::area));
static_assert(!implicitly_convertible(isq::area, isq::width * isq::height));
```

Surprisingly, `height * height → area` behaves similarly. While hard to imagine physically, the library cannot prevent such operations.

##### 19.8.5.2 Arithmetic and compatibility of quantities of dimension one

Dividing quantities of the same kind yields dimension-one quantities with different meanings (*slope of ramp*, *clock accuracy*), yet they’re mutually comparable per dimensional analysis.

The above means that the following code is valid:

```cpp
quantity q1 = isq::length(1. * m) / isq::length(10. * m) + isq::time(1. * us) / isq::time(1 * h);
quantity q2 = isq::height(1. * m) / isq::length(10. * m) + isq::time(1. * us) / isq::time(1 * h);
```

Both produce `dimensionless` (root of hierarchy). Converting `q2` and `q3` to specific dimension-one quantities works for general forms but requires explicit conversion for specific combinations:

```cpp
quantity<(isq::length / isq::length)[m / m]> ok1 = q1;     // OK (same quantity)
quantity<(isq::length / isq::length)[m / m]> ok2 = q2;     // OK (same quantity)
quantity<(isq::height / isq::length)[m / m]> bad1 = q1;    // Error (not every dimensionless is height/length)
quantity<(isq::height / isq::length)[m / m]> bad2 = q2;    // Error (not every dimensionless is height/length)
```

#### 19.8.6 Structural types

The `quantity` and `quantity_point` class templates are structural types to allow them to be passed as template arguments. For example, we can write the following:

```cpp
constexpr struct amsterdam_sea_level : absolute_point_origin<isq::altitude> {
} amsterdam_sea_level;

constexpr struct mediterranean_sea_level : relative_point_origin<amsterdam_sea_level + isq::altitude(-27 * cm)> {
} mediterranean_sea_level;

using altitude_DE = quantity_point<isq::altitude[m], amsterdam_sea_level>;
using altitude_CH = quantity_point<isq::altitude[m], mediterranean_sea_level>;
```

Unfortunately, current language rules require that all member data of a structural type are public. This could be considered a safety issue. We try really hard to provide unit-safe interfaces, but at the same time expose the public “naked” data member that can be freely read or manipulated by anyone.

Hopefully, this requirement on structural types will be relaxed before the library gets standardized.

## 20 Design details and rationale

*Note: This chapter provides more design details and rationale for them. It tries to not repeat information already provided in the previous chapters so a reader is expected to be familar with them already.*

### 20.1 Conventions

#### 20.1.1 New style of definitions

Before we dig into details, it is worth reminding that compile-time errors generation is the most important feature of the library. If we did not make errors in our code and could handle quantities and write all the conversions correctly by hand, such a library would be of little use. We are humans and make mistakes.

Also, the library is about to be used by many engineers who use C++ as a tool to get their work done and are not C++ template metaprogramming experts. This is why the compilation errors generated by this library should be as easy to understand as possible. Users should be able to quickly identify the cause of the issue and understand how to fix it.

With the above in mind, the [[mp-units]](https://mpusz.github.io/mp-units) library decided to use a rather unusual pattern to define entities, but it proved really successful, and we have received great feedback from users.

To improve the readability of compiler errors and types presented in a debugger, and to make it easier to correlate them with a user’s written code, a new idiom in the library is to use the same identifier for a tag type and its instance.

Here is how we define `metre` and `second` [[SI]](https://www.bipm.org/en/publications/si-brochure) base units:

```cpp
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
```

Please note that the above reuses the same identifier for a type and its value. The rationale behind this is that:

- Users always work with values and never have to spell the name of such a type.
- The types appear in the compilation errors and during debugging.

Ordinary users don’t care about what is a type and what is a value in the error message. They want to be able to easily read and analyze the error message and understand where in the code they made the calculation error.

Unfortunately, we can’t be consistent here. The C++ language rules do not allow to use the same identifier for a template and the object resulting from its instantiation. For such cases, we decided to postfix the template identifier with `'_'`.

Let’s compare the readability of the current practices with an alternative and popular usage of `_t` postfixes for type identifiers (after removing the project namespace prefix):

Current practice:

| User’s code | Resulting type |
| --- | --- |
| `quantity<si::metre>` | `quantity<si::metre{}, double>` |
| `quantity<si::metre / si::second>` | `quantity<derived_unit<si::metre, per<si::second>>{}, double>` |
| `isq::speed(50 * km / h) / (5 * s)` | `quantity<reference<derived_quantity_spec<isq::speed, per<isq::time>>, derived_unit<si::kilo_<si::metre>, per<non_si::hour, si::second>>>{}, int>` |

With `_t` postfixes:

| User’s code | Resulting type |
| --- | --- |
| `quantity<si::metre>` | `quantity<si::metre_t{}, double>` |
| `quantity<si::metre / si::second>` | `quantity<derived_unit<si::metre_t, per<si::second_t>>{}, double>` |
| `isq::speed(50 * km / h) / (5 * s)` | `quantity<reference<derived_quantity_spec<isq::speed_t, per<isq::time_t>>, derived_unit<si::kilo_t<si::metre_t>, per<non_si::hour_t, si::second_t>>>{}, int>` |

To improve the types readability we also prefer to use type identifiers for template parameters (if possible) rather than NTTPs directly. Without it, the last type would look as follows:

| User’s code | Resulting type |
| --- | --- |
| `isq::speed(50 * km / h) / (5 * s)` | `quantity<reference<derived_quantity_spec<isq::speed_t{}, per<isq::time_t{}>>{}, derived_unit<si::kilo_t<si::metre_t{}>{}, per<non_si::hour_t{}, si::second_t{}>>{}>{}, int>` |

#### 20.1.2 Strong types instead of aliases

Let’s look again at the above units definitions. Another essential point to notice is that all the types describing entities in the library are short, nicely named identifiers that derive from longer, more verbose class template instantiations. This is really important to improve the user experience while debugging the program or analyzing the compilation error.

*Note: Such a practice is rare in the industry. Some popular C++ physical units libraries generate enormously long error messages.*

#### 20.1.3 Entities composability

Many physical units libraries (in C++ or any other programming language) assign strong types to library entities (e.g., derived units). While `metre_per_second` as a type may not look too scary, consider, for example, units of angular momentum. If we followed this path, its coherent unit would look like `kilogram_metre_sq_per_second`. Now, consider how many scaled versions of this unit you would predefine in the library to ensure that all users are happy with your choice? How expensive would it be from the implementation point of view? How expensive would it be to standardize?

This is why, in this library, we put a strong requirement to make everything as composable as possible. For example, to create a quantity with a unit of *speed*, one may write:

```cpp
quantity<si::metre / si::second> q;
```

In case we use such a unit often and would prefer to have a handy helper for it, we can always do something like this:

```cpp
constexpr auto metre_per_second = si::metre / si::second;
quantity<metre_per_second> q;
```

or choose any shorter identifier of our choice.

The unit composition works not only on the “unit-level”. We can multiply or divide a quantity to get another type of quantity expressed in a composed unit:

```cpp
quantity pace = (4. * min + 40. * s) / km;
```

Coming back to the angular momentum case, thanks to the composability of units, a user can create such a quantity in the following way:

```cpp
using namespace si::unit_symbols;
auto q = la_vector{1, 2, 3} * isq::angular_momentum[kg * m2 / s];
```

It is a much better solution. It is terse and easy to understand. Please also notice how easy it is to obtain any scaled version of such a unit (e.g., `mg * square(mm) / min`) without having to introduce hundreds of types to predefine them.

#### 20.1.4 Value-based equations

This library is based on C++20, significantly improving user experience. One such improvement is the usage of value-based equations.

As we have learned above, the entities are being used as values in the code, and they compose. Moreover, derived entities can be defined in the library using such value-based equations. This is a considerable improvement compared to what we can find in other physical units libraries or what we have to deal with when we want to write some equations for `std::ratio`.

For example, below are a few definitions of the [[SI]](https://www.bipm.org/en/publications/si-brochure) derived units showing the power of C++20 extensions to Non-Type Template Parameters, which allow us to directly pass a result of the value-based unit equation to a class template definition:

```cpp
inline constexpr struct newton : named_unit<"N", kilogram * metre / square(second)> {} newton;
inline constexpr struct pascal : named_unit<"Pa", newton / square(metre)> {} pascal;
inline constexpr struct joule : named_unit<"J", newton * metre> {} joule;
```

#### 20.1.5 Framework-only class templates

Several proposed class templates like:

- `derived_unit`, `derived_dimension`, `derived_quantity_spec`,
- `per`, `power`,

should not be explicitly instantiated by the user.

Those types are the results of running operators on objects and have strict requirements on how the template arguments are provided. The library instantiates such class templates in a particular way (i.e., the arguments must be provided in the correct order). This logic might be partially implementation-defined (e.g., the order of elements in a numerator or denominator is sorted by type-id (whatever it means)). The important part here is to keep the ordering rules consistent within a specific implementation. Otherwise, the library cannot do its job properly (e.g., units simplification will not work).

Here are some examples:

```cpp
constexpr auto u1 = kg * m / s2;
constexpr auto u2 = kg * (m / s2);
constexpr auto u3 = kg / s2 * m;
```

All of the above yield the same instantiation of the `derived_unit<si::kilo_<si::gram>, si::metre, per<power<si::second, 2>>>`.

The user never needs to instantiate the class templates explicitly. Allowing this can cause problems, as the user can make ordering errors. Of course, we can constrain the class template to require arguments in a particular order, but it will only slow down the compile times for every instantiation by the library’s engine.

Please note that a user in this library always works with values of tag types (e.g., unit), but the `derived_unit` class template takes those tag types as type parameters. This yields more readable types and prevents users from instantiating the template by themselves.

Here is how units are defined:

```cpp
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct gram : named_unit<"g", kind_of<isq::mass>> {} gram;

inline constexpr auto m = metre;
inline constexpr auto s = second;
inline constexpr auto g = gram;
inline constexpr auto s2 = square(second);
```

Because of the above, to explicitly instantiate a class template, a user would need to type the following:

```cpp
derived_unit<si::kilo_<struct si::gram>, per<power<struct si::second, 2>>> u4;
```

The usage of the explicit `struct` keyword might be surprising to many users.

Also, when dealing with quantities, a user does not need to spell a unit’s type:

```cpp
void foo(quantity<si::kilo<si::gram> * si::metre / square(si::second)>) {}

foo(42. * kg * m / s2);
```

The above instantiates a `quantity<derived_unit<si::kilo_<si::gram>, si::metre, per<power<si::second, 2>>>{}, double>` behind the scenes.

Please note that in the above examples, all the class templates `derived_unit`, `per`, `power`, and `kilo_` have the same property. They are well-defined identifiers that users expect to see in types presented in the debugger or compilation errors. This is why they should not be exposition-only and be regular members of the `std` namespace. Every implementation has to spell and use them in the same way.

[[mp-units]](https://mpusz.github.io/mp-units) library decided to define those class templates in the `mp_units` namespace, but to not export them from the `mp_units.core` module. With this, users will have no way to instantiate those templates by themselves, which is the exact intent of this library. Initially, we wanted to propose something similar for the Standard Library, but [the LWG did not like the idea](https://lists.isocpp.org/lib/2024/10/29544.php).

An alternative might be to state that it is IFNDR or UB to instantiate those by the user. It does not technically prevent users from doing so, but if they do it, they are on their own.

Last but not least, we can allow such instantiations and add restrictive constraints to verify template arguments, which could affect compilation times.

### 20.2 Framework entities

The below graph presents the most important entities of the library’s framework and how they relate to each other.

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLXJvbGVkZXNjcmlwdGlvbj0iZmxvd2NoYXJ0LXYyIiByb2xlPSJncmFwaGljcy1kb2N1bWVudCBkb2N1bWVudCIgdmlld0JveD0iLTggLTggNDUxLjQxNzk2ODc1IDQxMSIgc3R5bGU9Im1heC13aWR0aDogMTAwJTsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEwMCUiIGlkPSJncmFwaC1kaXYiIGhlaWdodD0iMTAwJSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxzdHlsZT5AaW1wb3J0IHVybCgiaHR0cHM6Ly9jZG5qcy5jbG91ZGZsYXJlLmNvbS9hamF4L2xpYnMvZm9udC1hd2Vzb21lLzYuNC4yL2Nzcy9hbGwubWluLmNzcyIpOyc8L3N0eWxlPjxzdHlsZT4jZ3JhcGgtZGl2e2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmVycm9yLWljb257ZmlsbDojNTUyMjIyO30jZ3JhcGgtZGl2IC5lcnJvci10ZXh0e2ZpbGw6IzU1MjIyMjtzdHJva2U6IzU1MjIyMjt9I2dyYXBoLWRpdiAuZWRnZS10aGlja25lc3Mtbm9ybWFse3N0cm9rZS13aWR0aDoycHg7fSNncmFwaC1kaXYgLmVkZ2UtdGhpY2tuZXNzLXRoaWNre3N0cm9rZS13aWR0aDozLjVweDt9I2dyYXBoLWRpdiAuZWRnZS1wYXR0ZXJuLXNvbGlke3N0cm9rZS1kYXNoYXJyYXk6MDt9I2dyYXBoLWRpdiAuZWRnZS1wYXR0ZXJuLWRhc2hlZHtzdHJva2UtZGFzaGFycmF5OjM7fSNncmFwaC1kaXYgLmVkZ2UtcGF0dGVybi1kb3R0ZWR7c3Ryb2tlLWRhc2hhcnJheToyO30jZ3JhcGgtZGl2IC5tYXJrZXJ7ZmlsbDojMzMzMzMzO3N0cm9rZTojMzMzMzMzO30jZ3JhcGgtZGl2IC5tYXJrZXIuY3Jvc3N7c3Ryb2tlOiMzMzMzMzM7fSNncmFwaC1kaXYgc3Zne2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTZweDt9I2dyYXBoLWRpdiAubGFiZWx7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2NvbG9yOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXItbGFiZWwgc3BhbiwjZ3JhcGgtZGl2IHB7Y29sb3I6IzMzMzt9I2dyYXBoLWRpdiAubGFiZWwgdGV4dCwjZ3JhcGgtZGl2IHNwYW4sI2dyYXBoLWRpdiBwe2ZpbGw6IzMzMztjb2xvcjojMzMzO30jZ3JhcGgtZGl2IC5ub2RlIHJlY3QsI2dyYXBoLWRpdiAubm9kZSBjaXJjbGUsI2dyYXBoLWRpdiAubm9kZSBlbGxpcHNlLCNncmFwaC1kaXYgLm5vZGUgcG9seWdvbiwjZ3JhcGgtZGl2IC5ub2RlIHBhdGh7ZmlsbDojRUNFQ0ZGO3N0cm9rZTojOTM3MERCO3N0cm9rZS13aWR0aDoxcHg7fSNncmFwaC1kaXYgLmZsb3djaGFydC1sYWJlbCB0ZXh0e3RleHQtYW5jaG9yOm1pZGRsZTt9I2dyYXBoLWRpdiAubm9kZSAubGFiZWx7dGV4dC1hbGlnbjpjZW50ZXI7fSNncmFwaC1kaXYgLm5vZGUuY2xpY2thYmxle2N1cnNvcjpwb2ludGVyO30jZ3JhcGgtZGl2IC5hcnJvd2hlYWRQYXRoe2ZpbGw6IzMzMzMzMzt9I2dyYXBoLWRpdiAuZWRnZVBhdGggLnBhdGh7c3Ryb2tlOiMzMzMzMzM7c3Ryb2tlLXdpZHRoOjIuMHB4O30jZ3JhcGgtZGl2IC5mbG93Y2hhcnQtbGlua3tzdHJva2U6IzMzMzMzMztmaWxsOm5vbmU7fSNncmFwaC1kaXYgLmVkZ2VMYWJlbHtiYWNrZ3JvdW5kLWNvbG9yOiNlOGU4ZTg7dGV4dC1hbGlnbjpjZW50ZXI7fSNncmFwaC1kaXYgLmVkZ2VMYWJlbCByZWN0e29wYWNpdHk6MC41O2JhY2tncm91bmQtY29sb3I6I2U4ZThlODtmaWxsOiNlOGU4ZTg7fSNncmFwaC1kaXYgLmxhYmVsQmtne2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsIDIzMiwgMjMyLCAwLjUpO30jZ3JhcGgtZGl2IC5jbHVzdGVyIHJlY3R7ZmlsbDojZmZmZmRlO3N0cm9rZTojYWFhYTMzO3N0cm9rZS13aWR0aDoxcHg7fSNncmFwaC1kaXYgLmNsdXN0ZXIgdGV4dHtmaWxsOiMzMzM7fSNncmFwaC1kaXYgLmNsdXN0ZXIgc3BhbiwjZ3JhcGgtZGl2IHB7Y29sb3I6IzMzMzt9I2dyYXBoLWRpdiBkaXYubWVybWFpZFRvb2x0aXB7cG9zaXRpb246YWJzb2x1dGU7dGV4dC1hbGlnbjpjZW50ZXI7bWF4LXdpZHRoOjIwMHB4O3BhZGRpbmc6MnB4O2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtmb250LXNpemU6MTJweDtiYWNrZ3JvdW5kOmhzbCg4MCwgMTAwJSwgOTYuMjc0NTA5ODAzOSUpO2JvcmRlcjoxcHggc29saWQgI2FhYWEzMztib3JkZXItcmFkaXVzOjJweDtwb2ludGVyLWV2ZW50czpub25lO3otaW5kZXg6MTAwO30jZ3JhcGgtZGl2IC5mbG93Y2hhcnRUaXRsZVRleHR7dGV4dC1hbmNob3I6bWlkZGxlO2ZvbnQtc2l6ZToxOHB4O2ZpbGw6IzMzMzt9I2dyYXBoLWRpdiA6cm9vdHstLW1lcm1haWQtZm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO308L3N0eWxlPjxnPjxtYXJrZXIgb3JpZW50PSJhdXRvIiBtYXJrZXJIZWlnaHQ9IjEyIiBtYXJrZXJXaWR0aD0iMTIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgcmVmWT0iNSIgcmVmWD0iNiIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtcG9pbnRFbmQiPjxwYXRoIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMiIgbWFya2VyV2lkdGg9IjEyIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjQuNSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtcG9pbnRTdGFydCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMCA1IEwgMTAgMTAgTCAxMCAwIHoiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUiIHJlZlg9IjExIiB2aWV3Qm94PSIwIDAgMTAgMTAiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0IiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC1jaXJjbGVFbmQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1IiByZWZYPSItMSIgdmlld0JveD0iMCAwIDEwIDEwIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydCIgaWQ9ImdyYXBoLWRpdl9mbG93Y2hhcnQtY2lyY2xlU3RhcnQiPjxjaXJjbGUgc3R5bGU9InN0cm9rZS13aWR0aDogMTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHI9IjUiIGN5PSI1IiBjeD0iNSI+PC9jaXJjbGU+PC9tYXJrZXI+PG1hcmtlciBvcmllbnQ9ImF1dG8iIG1hcmtlckhlaWdodD0iMTEiIG1hcmtlcldpZHRoPSIxMSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiByZWZZPSI1LjIiIHJlZlg9IjEyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0IiBpZD0iZ3JhcGgtZGl2X2Zsb3djaGFydC1jcm9zc0VuZCI+PHBhdGggc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiPjwvcGF0aD48L21hcmtlcj48bWFya2VyIG9yaWVudD0iYXV0byIgbWFya2VySGVpZ2h0PSIxMSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIHJlZlk9IjUuMiIgcmVmWD0iLTEiIHZpZXdCb3g9IjAgMCAxMSAxMSIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQiIGlkPSJncmFwaC1kaXZfZmxvd2NoYXJ0LWNyb3NzU3RhcnQiPjxwYXRoIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBkPSJNIDEsMSBsIDksOSBNIDEwLDEgbCAtOSw5Ij48L3BhdGg+PC9tYXJrZXI+PGcgY2xhc3M9InJvb3QiPjxnIGNsYXNzPSJjbHVzdGVycyI+PC9nPjxnIGNsYXNzPSJlZGdlUGF0aHMiPjxwYXRoIHN0eWxlPSJmaWxsOm5vbmU7IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayBMUy1Vbml0IExFLVJlZmVyZW5jZSIgaWQ9IkwtVW5pdC1SZWZlcmVuY2UtMCIgZD0iTTIyLjUxMiwxMjhMMjIuNTEyLDEzMi4xNjdDMjIuNTEyLDEzNi4zMzMsMjIuNTEyLDE0NC42NjcsMjkuOTYzLDE1M0MzNy40MTUsMTYxLjMzMyw1Mi4zMTgsMTY5LjY2Nyw1OS43NjksMTczLjgzM0w2Ny4yMjEsMTc4Ij48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLURpbWVuc2lvbiBMRS1RdWFudGl0eVNwZWMiIGlkPSJMLURpbWVuc2lvbi1RdWFudGl0eVNwZWMtMCIgZD0iTTE3MS42NzYsMzlMMTcxLjY3Niw0My4xNjdDMTcxLjY3Niw0Ny4zMzMsMTcxLjY3Niw1NS42NjcsMTcyLjYxMiw2NEMxNzMuNTQ4LDcyLjMzMywxNzUuNDIxLDgwLjY2NywxNzYuMzU3LDg0LjgzM0wxNzcuMjk0LDg5Ij48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLXF1YW50aXR5X2NoYXJhY3RlciBMRS1RdWFudGl0eVNwZWMiIGlkPSJMLXF1YW50aXR5X2NoYXJhY3Rlci1RdWFudGl0eVNwZWMtMCIgZD0iTTMxOS4wNzcsMzlMMzEwLjMwNCw0My4xNjdDMzAxLjUzMiw0Ny4zMzMsMjgzLjk4Nyw1NS42NjcsMjY3LjI3Nyw2NEMyNTAuNTY4LDcyLjMzMywyMzQuNjk0LDgwLjY2NywyMjYuNzU3LDg0LjgzM0wyMTguODIsODkiPjwvcGF0aD48cGF0aCBzdHlsZT0iZmlsbDpub25lOyIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsgTFMtUXVhbnRpdHlTcGVjIExFLVJlZmVyZW5jZSIgaWQ9IkwtUXVhbnRpdHlTcGVjLVJlZmVyZW5jZS0wIiBkPSJNMTgxLjY3NiwxMjhMMTgxLjY3NiwxMzIuMTY3QzE4MS42NzYsMTM2LjMzMywxODEuNjc2LDE0NC42NjcsMTc0LjIyNCwxNTNDMTY2Ljc3MywxNjEuMzMzLDE1MS44NywxNjkuNjY3LDE0NC40MTgsMTczLjgzM0wxMzYuOTY3LDE3OCI+PC9wYXRoPjxwYXRoIHN0eWxlPSJmaWxsOm5vbmU7IiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayBMUy1SZWZlcmVuY2UgTEUtUXVhbnRpdHkiIGlkPSJMLVJlZmVyZW5jZS1RdWFudGl0eS0wIiBkPSJNMTAyLjA5NCwyMTdMMTAyLjA5NCwyMjEuMTY3QzEwMi4wOTQsMjI1LjMzMywxMDIuMDk0LDIzMy42NjcsMTExLjMwNSwyNDIuMjA5QzEyMC41MTcsMjUwLjc1LDEzOC45NCwyNTkuNTAxLDE0OC4xNTIsMjYzLjg3NkwxNTcuMzYzLDI2OC4yNTEiPjwvcGF0aD48cGF0aCBzdHlsZT0iZmlsbDpub25lO3N0cm9rZS13aWR0aDoycHg7c3Ryb2tlLWRhc2hhcnJheTozOyIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tZG90dGVkIGZsb3djaGFydC1saW5rIExTLXF1YW50aXR5X2NoYXJhY3RlciBMRS1SZXByZXNlbnRhdGlvbiIgaWQ9IkwtcXVhbnRpdHlfY2hhcmFjdGVyLVJlcHJlc2VudGF0aW9uLTAiIGQ9Ik0zNjQuNTE1LDM5TDM2NS40NTEsNDMuMTY3QzM2Ni4zODcsNDcuMzMzLDM2OC4yNiw1NS42NjcsMzY5LjE5Niw2Ny4yNUMzNzAuMTMzLDc4LjgzMywzNzAuMTMzLDkzLjY2NywzNzAuMTMzLDEwOC41QzM3MC4xMzMsMTIzLjMzMywzNzAuMTMzLDEzOC4xNjcsMzcwLjEzMywxNDkuNzVDMzcwLjEzMywxNjEuMzMzLDM3MC4xMzMsMTY5LjY2NywzNzAuMTMzLDE3My44MzNMMzcwLjEzMywxNzgiPjwvcGF0aD48cGF0aCBzdHlsZT0iZmlsbDpub25lOyIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsgTFMtUmVwcmVzZW50YXRpb24gTEUtUXVhbnRpdHkiIGlkPSJMLVJlcHJlc2VudGF0aW9uLVF1YW50aXR5LTAiIGQ9Ik0zNzAuMTMzLDIxN0wzNzAuMTMzLDIyMS4xNjdDMzcwLjEzMywyMjUuMzMzLDM3MC4xMzMsMjMzLjY2NywzNDcuNDc5LDI0My42MTZDMzI0LjgyNCwyNTMuNTY0LDI3OS41MTYsMjY1LjEyOSwyNTYuODYxLDI3MC45MTFMMjM0LjIwNywyNzYuNjkzIj48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLVF1YW50aXR5IExFLVF1YW50aXR5UG9pbnQiIGlkPSJMLVF1YW50aXR5LVF1YW50aXR5UG9pbnQtMCIgZD0iTTE5NS43ODUsMzA2TDE5NS43ODUsMzEwLjE2N0MxOTUuNzg1LDMxNC4zMzMsMTk1Ljc4NSwzMjIuNjY3LDIwMi4xOTQsMzMxQzIwOC42MDIsMzM5LjMzMywyMjEuNDE5LDM0Ny42NjcsMjI3LjgyOCwzNTEuODMzTDIzNC4yMzYsMzU2Ij48L3BhdGg+PHBhdGggc3R5bGU9ImZpbGw6bm9uZTsiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIExTLVBvaW50T3JpZ2luIExFLVF1YW50aXR5UG9pbnQiIGlkPSJMLVBvaW50T3JpZ2luLVF1YW50aXR5UG9pbnQtMCIgZD0iTTMzMi42NzIsMzA2TDMzMi42NzIsMzEwLjE2N0MzMzIuNjcyLDMxNC4zMzMsMzMyLjY3MiwzMjIuNjY3LDMyNi4yNjMsMzMxQzMxOS44NTUsMzM5LjMzMywzMDcuMDM4LDM0Ny42NjcsMzAwLjYyOSwzNTEuODMzTDI5NC4yMjEsMzU2Ij48L3BhdGg+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWxzIj48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSIgY2xhc3M9ImxhYmVsIj48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjAiIHdpZHRoPSIwIj48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIiBjbGFzcz0ibGFiZWwiPjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMCIgd2lkdGg9IjAiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiIGNsYXNzPSJsYWJlbCI+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIwIiB3aWR0aD0iMCI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PGcgY2xhc3M9Im5vZGVzIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMi41MTE3MTg3NSwgMTA4LjUpIiBpZD0iZmxvd2NoYXJ0LVVuaXQtNDIiIGNsYXNzPSJub2RlIGRlZmF1bHQgZGVmYXVsdCBmbG93Y2hhcnQtbGFiZWwiPjxyZWN0IGhlaWdodD0iMzkiIHdpZHRoPSI0NS4wMjM0Mzc1IiB5PSItMTkuNSIgeD0iLTIyLjUxMTcxODc1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTUuMDExNzE4NzUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIzMC4wMjM0Mzc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+VW5pdDwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMDIuMDkzNzUsIDE5Ny41KSIgaWQ9ImZsb3djaGFydC1SZWZlcmVuY2UtNDMiIGNsYXNzPSJub2RlIGRlZmF1bHQgZGVmYXVsdCBmbG93Y2hhcnQtbGFiZWwiPjxyZWN0IGhlaWdodD0iMzkiIHdpZHRoPSIxNTEuNTg1OTM3NSIgeT0iLTE5LjUiIHg9Ii03NS43OTI5Njg3NSIgcnk9IjAiIHJ4PSIwIiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTY4LjI5Mjk2ODc1LCAtMTIpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjI0IiB3aWR0aD0iMTM2LjU4NTkzNzUiPjxkaXYgc3R5bGU9ImRpc3BsYXk6IGlubGluZS1ibG9jazsgd2hpdGUtc3BhY2U6IG5vd3JhcDsiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIj48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj5RdWFudGl0eSByZWZlcmVuY2U8L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTcxLjY3NTc4MTI1LCAxOS41KSIgaWQ9ImZsb3djaGFydC1EaW1lbnNpb24tNDQiIGNsYXNzPSJub2RlIGRlZmF1bHQgZGVmYXVsdCBmbG93Y2hhcnQtbGFiZWwiPjxyZWN0IGhlaWdodD0iMzkiIHdpZHRoPSI4OC40OTIxODc1IiB5PSItMTkuNSIgeD0iLTQ0LjI0NjA5Mzc1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMzYuNzQ2MDkzNzUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSI3My40OTIxODc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+RGltZW5zaW9uPC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE4MS42NzU3ODEyNSwgMTA4LjUpIiBpZD0iZmxvd2NoYXJ0LVF1YW50aXR5U3BlYy00NSIgY2xhc3M9Im5vZGUgZGVmYXVsdCBkZWZhdWx0IGZsb3djaGFydC1sYWJlbCI+PHJlY3QgaGVpZ2h0PSIzOSIgd2lkdGg9IjE3My4zMDQ2ODc1IiB5PSItMTkuNSIgeD0iLTg2LjY1MjM0Mzc1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNzkuMTUyMzQzNzUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxNTguMzA0Njg3NSI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPlF1YW50aXR5IHNwZWNpZmljYXRpb248L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzYwLjEzMjgxMjUsIDE5LjUpIiBpZD0iZmxvd2NoYXJ0LXF1YW50aXR5X2NoYXJhY3Rlci00NiIgY2xhc3M9Im5vZGUgZGVmYXVsdCBkZWZhdWx0IGZsb3djaGFydC1sYWJlbCI+PHJlY3QgaGVpZ2h0PSIzOSIgd2lkdGg9IjE1MC41NzAzMTI1IiB5PSItMTkuNSIgeD0iLTc1LjI4NTE1NjI1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjcuNzg1MTU2MjUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxMzUuNTcwMzEyNSI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPlF1YW50aXR5IGNoYXJhY3Rlcjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxOTUuNzg1MTU2MjUsIDI4Ni41KSIgaWQ9ImZsb3djaGFydC1RdWFudGl0eS01MSIgY2xhc3M9Im5vZGUgZGVmYXVsdCBkZWZhdWx0IGZsb3djaGFydC1sYWJlbCI+PHJlY3QgaGVpZ2h0PSIzOSIgd2lkdGg9Ijc2Ljg0Mzc1IiB5PSItMTkuNSIgeD0iLTM4LjQyMTg3NSIgcnk9IjAiIHJ4PSIwIiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTMwLjkyMTg3NSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjYxLjg0Mzc1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+UXVhbnRpdHk8L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzcwLjEzMjgxMjUsIDE5Ny41KSIgaWQ9ImZsb3djaGFydC1SZXByZXNlbnRhdGlvbi01MyIgY2xhc3M9Im5vZGUgZGVmYXVsdCBkZWZhdWx0IGZsb3djaGFydC1sYWJlbCI+PHJlY3QgaGVpZ2h0PSIzOSIgd2lkdGg9IjEyMy4xNzk2ODc1IiB5PSItMTkuNSIgeD0iLTYxLjU4OTg0Mzc1IiByeT0iMCIgcng9IjAiIHN0eWxlPSIiIGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiPjwvcmVjdD48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNTQuMDg5ODQzNzUsIC0xMikiIHN0eWxlPSIiIGNsYXNzPSJsYWJlbCI+PHJlY3Q+PC9yZWN0Pjxmb3JlaWduT2JqZWN0IGhlaWdodD0iMjQiIHdpZHRoPSIxMDguMTc5Njg3NSI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPlJlcHJlc2VudGF0aW9uPC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDI2NC4yMjg1MTU2MjUsIDM3NS41KSIgaWQ9ImZsb3djaGFydC1RdWFudGl0eVBvaW50LTU3IiBjbGFzcz0ibm9kZSBkZWZhdWx0IGRlZmF1bHQgZmxvd2NoYXJ0LWxhYmVsIj48cmVjdCBoZWlnaHQ9IjM5IiB3aWR0aD0iMTE4LjgxMjUiIHk9Ii0xOS41IiB4PSItNTkuNDA2MjUiIHJ5PSIwIiByeD0iMCIgc3R5bGU9IiIgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciI+PC9yZWN0PjxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKC01MS45MDYyNSwgLTEyKSIgc3R5bGU9IiIgY2xhc3M9ImxhYmVsIj48cmVjdD48L3JlY3Q+PGZvcmVpZ25PYmplY3QgaGVpZ2h0PSIyNCIgd2lkdGg9IjEwMy44MTI1Ij48ZGl2IHN0eWxlPSJkaXNwbGF5OiBpbmxpbmUtYmxvY2s7IHdoaXRlLXNwYWNlOiBub3dyYXA7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+UXVhbnRpdHkgcG9pbnQ8L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMzMyLjY3MTg3NSwgMjg2LjUpIiBpZD0iZmxvd2NoYXJ0LVBvaW50T3JpZ2luLTU4IiBjbGFzcz0ibm9kZSBkZWZhdWx0IGRlZmF1bHQgZmxvd2NoYXJ0LWxhYmVsIj48cmVjdCBoZWlnaHQ9IjM5IiB3aWR0aD0iOTYuOTI5Njg3NSIgeT0iLTE5LjUiIHg9Ii00OC40NjQ4NDM3NSIgcnk9IjAiIHJ4PSIwIiBzdHlsZT0iIiBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIj48L3JlY3Q+PGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTQwLjk2NDg0Mzc1LCAtMTIpIiBzdHlsZT0iIiBjbGFzcz0ibGFiZWwiPjxyZWN0PjwvcmVjdD48Zm9yZWlnbk9iamVjdCBoZWlnaHQ9IjI0IiB3aWR0aD0iODEuOTI5Njg3NSI+PGRpdiBzdHlsZT0iZGlzcGxheTogaW5saW5lLWJsb2NrOyB3aGl0ZS1zcGFjZTogbm93cmFwOyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPlBvaW50IG9yaWdpbjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PC9nPjwvZz48L3N2Zz4=)

Some of the entities were already introduced in the Quick domain introduction chapter. Below we describe the remaining ones.

#### 20.2.1 Quantity character

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly states that quantities (even of the same kind) may have different characters:

- real scalar,
- complex scalar,
- vector,
- tensor.

The quantity character in the library is implemented with the `quantity_character` enumeration:

```cpp
enum class quantity_character { real_scalar, complex_scalar, vector, tensor };
```

More information on quantity characters can be found in the Safe operations of vector and tensor quantities chapter.

#### 20.2.2 Quantity specification

Dimension is not enough to describe a quantity. This is why [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides hundreds of named quantity types. It turns out that there are many more quantity types in the ISQ than the named units in the [[SI]](https://www.bipm.org/en/publications/si-brochure).

This is why the library introduces a quantity specification entity that stores:

- Dimension,
- Quantity kind & type,
- Quantity character,
- the quantity equation being the recipe to create this quantity (only for derived quantities that specify such a recipe).

For example:

| Quantity Specification | Dimension | Quantity Kind | Character | Equation |
| --- | --- | --- | --- | --- |
| `isq::duration` | T | `isq::duration` | scalar | base quantity |
| `isq::length` | L | `isq::length` | scalar | base quantity |
| `isq::mass` | M | `isq::mass` | scalar | base quantity |
| `isq::width` | L | `isq::length` | scalar | `isq::length` |
| `isq::height` | L | `isq::length` | scalar | `isq::length` |
| `isq::position_vector` | L | `isq::length` | vector | `isq::length` |
| `isq::displacement` | L | `isq::length` | vector | `isq::length` |
| `isq::area` | L² | `isq::area` | scalar | `isq::length²` |
| `isq::speed` | LT⁻¹ | `isq::speed` | scalar | `isq::length / isq::duration` |
| `isq::velocity` | LT⁻¹ | `isq::speed` | vector | `isq::displacement / isq::duration` |
| `isq::acceleration` | LT⁻² | `isq::acceleration` | vector | `isq::velocity / isq::duration` |
| `isq::force` | LMT⁻² | `isq::force` | vector | `isq::mass * isq::acceleration` |
| `isq::moment_of_force` | L²MT⁻² | `isq::moment_of_force` | vector | `isq::position_vector * isq::force` |

#### 20.2.3 Unit

A unit is a concrete amount of a quantity that allows us to measure the values of quantities of the same kind and represent the result as a number being the ratio of the two quantities.

For example:

- `si::second`, `si::metre`, `si::kilogram`, `si::ampere`, `si::kelvin`, `si::mole`, and `si::candela` are the base units of the [[SI]](https://www.bipm.org/en/publications/si-brochure).
- `si::kilo<si::metre>` is a prefixed unit of *length*.
- `si::radian`, `si::newton`, and `si::watt` are examples of named derived units within the [[SI]](https://www.bipm.org/en/publications/si-brochure).
- `non_si::minute` is an example of a scaled unit of time.
- `si::si2019::speed_of_light_in_vacuum` is a physical constant standardized by the SI in 2019.

*Note: In this library, physical constants are also implemented as units.*

#### 20.2.4 Quantity representation

Quantity representation defines the type used to store the numerical value of a quantity. Such a type should be of a specific quantity character provided in the quantity specification.

*Note: By default, all floating-point and integral (besides `bool`) types are treated as real scalars and `std::complex` as a complex scalar.*

#### 20.2.5 Point origin

In the affine space theory, the point origin specifies where the “zero” of our measurement’s scale is.

In this library, we have two types of point origins:

- absolute - defines an absolute “zero” for our point,
- relative - defines an origin that has some “offset” relative to an absolute point.

*Note: More information on this subject can be found in The affine space chapter.*

#### 20.2.6 Quantity point

Quantity point implements a point in the affine space theory. Its value can be easily created by adding/subtracting the quantity with a point origin.

*Note: More information on this subject can be found in The affine space chapter.*

### 20.3 Library namespace

The library’s names fall into two distinct categories with different placement requirements.

#### 20.3.1 Framework entities — proposed in `std::`

The framework types (`quantity`, `quantity_point`, `quantity_spec`, `named_unit`, `dimension`, `mag`, concepts, …) are a small, fixed set. They provide long-awaited strong-type support not only for physical quantities and units but also for anything that resembles a measurable number (e.g., *longitude* and *latitude*, pixel *coordinates*, *prices*). The affine space abstraction has similarly broad applicability.

We propose placing all framework entities directly in namespace `std`. The primary motivation is **error message quality**: when a type mismatch occurs, the compiler reports the full qualified name of every type involved. Nesting framework types inside `std::units` or a similar intermediate namespace adds that prefix to every diagnostic line, making already-complex template error messages significantly harder to read. Since the library’s chief value proposition is catching unit errors at compile time, readable diagnostics are a first-class concern — arguably more so than for any other library.

Some entities would need to be renamed to avoid ambiguity with existing `std` identifiers (e.g., `reference`).

##### 20.3.1.1 Counterarguments considered

During Croydon 2026 (SG18), three concerns were raised:

- **Coherence with the rest of the standard library.** Short names aid error messages *within* the library but may feel inconsistent alongside the rest of `std::`. We acknowledge this tension; however, the alternative of longer qualified names measurably harms the user experience that motivates the library’s existence. Implementations also have scope to improve diagnostics beyond what the library alone can do.
- **Volume of names in `std::`.** The framework itself contributes a bounded, modest number of names. System definitions (SI units, ISQ quantities) live in their own subnamespaces and do not pollute `std::` directly.
- **Naming conflicts with existing identifiers.** The most concrete example raised was `pi`: `std::numbers::pi` is an existing floating-point constant, while this library defines `pi` as a *unit* (a dimensionless scaling factor). These are different things with different types, so they cannot be confused by the compiler, but they are conceptually distinct and having two entities called `pi` in closely related namespaces may surprise users. This is an open question — see [Dimensionless and framework-level units] below.

#### 20.3.2 System definitions — in subnamespaces

Quantity types and units from concrete systems (SI, ISQ, US customary, …) are placed in their own subnamespaces under `std`:

```cpp
using namespace std::si::unit_symbols;

std::quantity<std::si::metre> q = 42 * m;
```

This keeps the system-specific vocabulary scoped and avoids polluting `std::` with an unbounded set of unit and quantity names.

#### 20.3.3 Dimensionless and framework-level entities

Beyond the framework types and the named systems, there are several entities that do not naturally belong to any concrete system namespace yet are more than just library machinery. They fall into roughly three categories with potentially different placement requirements.

##### 20.3.3.1 Algebraic identities

`dimension_one`, `dimensionless`, and `one` are the algebraic identity elements of the framework’s type system — the dimension, quantity specification, and unit of dimensionless quantities respectively. They are mandatory infrastructure: any quantity equation that produces a dimensionless result relies on them implicitly. As such they are arguably framework entities and could live in `std::` alongside `quantity` and `named_unit`. However, placing `one` directly in `std::` raises a naming concern: to be consistent with the existing `dimension_one` and `dimensionless` names in the same group, and to avoid potential conflicts with user-defined `one` identifiers, it may need to be renamed to `unit_one`.

##### 20.3.3.2 `pi` — a system-required constant

`pi` occupies a special position: it is a mandatory magnitude factor for defining SI units. The SI `degree` (plane angle) is defined as `mag<pi> / mag<180> * rad`, making `pi` a dependency of the SI system itself, not merely a convenience for user code. Placing it in `std::si::` is therefore tempting, but wrong: users working with angles in non-SI contexts (custom unit systems, pure mathematics, signal processing) need `pi` independently of the SI system, so requiring `std::si::pi` would impose an unwanted SI dependency.

Placing it in `std::` alongside the framework types is the most accessible option. The proximity to `std::numbers::pi` might initially appear problematic — both represent π but are fundamentally different kinds of entity: `std::numbers::pi` is a floating-point approximation, while `std::pi` would be a compile-time exact symbolic constant, evaluated to floating-point only when applied to a concrete value. However, this paper argues throughout that `quantity` is not merely a physics type but a safer numeric wrapper for any arithmetic value. Under that framing, `pi` can be seen as a safer version of `std::numbers::pi`: it carries the same mathematical meaning but defers floating-point evaluation and composes exactly with unit magnitudes. The naming proximity in `std::` would then reflect a genuine relationship rather than a collision — especially since the library uses `std::numbers::pi` under the hood when materialising the floating-point value of `pi`. Whether this reasoning is sufficient to justify `std::pi` is ultimately a question for LEWG.

##### 20.3.3.3 Useful dimensionless units with no system home

`percent` (`%`), `per_mille` (`‰`), and `parts_per_million` (`ppm`) are widely used in production code but, to our knowledge, are not defined by any standard system of units (neither SI nor any other system included in this proposal). They are convenient extensions of `one` that belong to no particular domain. Whether they should share a namespace with the algebraic identities or be grouped separately is unclear.

##### 20.3.3.4 Short helpers and factory functions

`per<U>` (reciprocal unit), `delta<U>()` and `point<U>()` (affine space constructors) are intentionally terse to keep quantity equations and construction syntax readable. Their brevity could be problematic in the flat `std::` namespace. However, unlike the units and quantity specs above, these are helpers that form part of the core API and are arguably framework entities in the same sense as `quantity` itself.

##### 20.3.3.5 Summary

The placement of all of the above is an **open question for LEWG**. The three or four categories above may warrant different namespaces, or a single shared subnamespace (e.g., `std::units::` or `std::qty::`). The tradeoff is consistent with the broader framework discussion: a subnamespace reduces name-conflict risk but requires `using namespace` to keep equations readable.

### 20.4 Concepts

This chapter enumerates all the user-facing concepts in the library.

*Note: Initially, C++20 was meant to use `CamelCase` for all the concept identifiers. Frustratingly, `CamelCase` concepts got dropped from the C++ standard at the last moment before releasing C++20. Now, we are facing the predictable consequences of running out of names. As long as some concepts in the library could be easily named with a `standard_case` there are some that are hard to distinguish from the corresponding type names, such as `Quantity` or `QuantitySpec`. This is why we decided to use `CamelCase` consistently for all the concept identifiers to make it clear when we are talking about a type or concept identifier. However, we are aware that this might be a temporary solution. In case the library gets standardized, we can expect the LEWG to bikeshed/rename all of the concept identifiers to a `standard_case`, even if it will result in a harder to understand code. We propose some suggestions at the end of the chapter.*

#### 20.4.1 `Dimension<T> concept`

`Dimension` concept matches a dimension of either a base or derived quantity:

- Base dimensions are explicitly defined by the user by inheriting from the instantiation of a `base_dimension` class template. It should be instantiated with a unique symbol identifier describing this dimension in a specific system of quantities.
- Derived dimensions are implicitly created by the library’s framework based on the quantity equation provided in the quantity specification.

##### 20.4.1.1 `DimensionOf<T, V>` concept

`DimensionOf` concept is satisfied when both arguments satisfy a `Dimension` concept and when they compare equal.

#### 20.4.2 `QuantitySpec<T> concept`

`QuantitySpec` concept matches all the quantity specifications including:

- Base quantities defined by a user by inheriting from the `quantity_spec` class template instantiated with a base dimension argument.
- Derived named quantities defined by a user by inheriting from the `quantity_spec` class template instantiated with a result of a quantity equation passed as an argument.
- Other named quantities forming a hierarchy of quantities of the same kind defined by a user by inheriting from the `quantity_spec` class template instantiated with another “parent” quantity specification passed as an argument.
- Quantity kinds describing a family of mutually comparable quantities.
- Intermediate derived quantity specifications being a result of a quantity equations on other specifications.

##### 20.4.2.1 `QuantitySpecOf<T, V>` concept

`QuantitySpecOf` concept is satisfied when both arguments satisfy a `QuantitySpec` concept and when `T` is implicitly convertible to `V`.

#### 20.4.3 `UnitMagnitude<T>`

`UnitMagnitude` concept is satisfied by all types defining a unit magnitude.

*Note:* Unit magnitude implementation is a private implementation detail of the library.

#### 20.4.4 `Unit<T>` concept

`Unit` concept matches all the units in the library including:

- Base units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier describing this unit in a specific system of units.
- Named scaled units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier and a product of multiplying another unit with some magnitude.
- Prefixed units defined by a user by inheriting from the `prefixed_unit` class template instantiated with a prefix symbol, a magnitude, and a unit to be prefixed.
- Derived named units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier and a result of unit equation passed as an argument.
- Derived unnamed units being a result of a unit equations on other units.
- Physical constants defined by a user by inheriting from the `named_constant` class template instantiated with a unique symbol identifier and a product of multiplying another unit with some magnitude.

##### 20.4.4.1 `PrefixableUnit<T>`

`PrefixableUnit` concept is satisfied by all units derived from a `named_unit` class template. Such units can be passed as an argument to a `prefixed_unit` class template.

##### 20.4.4.2 `UnitOf<T, V>` concept

`UnitOf` concept is satisfied for all units `T` for which an associated quantity spec is implicitly convertible to the provided `QuantitySpec` value..

#### 20.4.5 `Reference<T>` concept

`Reference` concept is satisfied by all quantity reference types. Such types provide all the meta-information required to create a `Quantity`.

A `Reference` can either be:

- A `Unit`.
- The instantiation of a `reference` class template with a `QuantitySpec` passed as the first template argument and a `Unit` passed as the second one.

##### 20.4.5.1 `ReferenceOf<T, V>` concept

`ReferenceOf` concept is satisfied by references `T` which have a quantity specification that satisfies `QuantitySpecOf<V>` concept.

#### 20.4.6 `RepresentationOf<T, V>`

`RepresentationOf` concept constrains a type `T` of a number that stores the numerical value of a quantity.

Every representation type must satisfy a common baseline:

- **Weakly regular**: copyable and equality comparable (default-constructibility is not required).
- **`MagnitudeScalable`**: the library must be able to apply a unit magnitude ratio to it internally. Most standard types satisfy this automatically; see Representation Types for details.
- **Character-specific operations**: additional arithmetic operations required by the quantity character (e.g. total ordering for real scalars, `real()`/`imag()`/`modulus()` CPOs for complex scalars, `norm()`/`magnitude()` CPO for vectors).

The second template argument `V` further constrains which characters are accepted:

- if the type of `V` satisfies `QuantitySpec`:
  - by all representation types when `V` describes a quantity kind,
  - otherwise, by representation types that are of a quantity character associated with a provided quantity specification `V`.
- if `V` is of `quantity_character` type:
  - by representation types that are of a provided quantity character.

#### 20.4.7 `Quantity<T>` concept

`Quantity` concept matches every quantity in the library and is satisfied by all types being or deriving from an instantiation of a `quantity` class template.

##### 20.4.7.1 `QuantityOf<T, V>` concept

`QuantityOf` concept is satisfied by all the quantities for which a `ReferenceOf<V>` is `true`.

##### 20.4.7.2 `QuantityLike<T>` concept

`QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type that provides:

- `reference` static data member that matches the `Reference` concept,
- `rep` type that matches `RepresentationOf` concept with the character provided in `reference`.
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the quantity,
- `from_numerical_value(rep)` static member function returning `T`.

For example, this is how support for `std::chrono::seconds` can be provided:

```cpp
template<>
struct quantity_like_traits<std::chrono::seconds> {
  static constexpr auto reference = detail::time_unit_from_chrono_period<Period>();
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = Rep;
  using T = std::chrono::duration<Rep, Period>;

  [[nodiscard]] static constexpr rep to_numerical_value(const T& q) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return q.count();
  }

  [[nodiscard]] static constexpr T from_numerical_value(const rep& v) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return T(v);
  }
};

quantity q = 42s;
std::chrono::seconds dur = 42 * s;
```

#### 20.4.8 `PointOrigin<T>` concept

`PointOrigin` concept matches all quantity point origins in the library. It is satisfied by either:

- All types derived from an `absolute_point_origin` class template.
- All types derived from a `relative_point_origin` class template.

##### 20.4.8.1 `PointOriginFor<T, V>` concept

`PointOriginFor` concept is satisfied by all `PointOrigin` types that have quantity type implicitly convertible from quantity specification `V`, which means that `V` must satisfy `QuantitySpecOf<T::quantity_spec>`.

For example, `si::ice_point` can serve as a point origin for *points* of `isq::Celsius_temperature` because this quantity type implicitly converts to `isq::thermodynamic_temperature`.

However, if we define `mean_sea_level` in the following way:

```cpp
inline constexpr struct mean_sea_level : absolute_point_origin<isq::altitude> {} mean_sea_level;
```

then it can’t be used as a point origin for *points* of `isq::length` or `isq::width` as none of them is implicitly convertible to `isq::altitude`:

- not every *length* is an *altitude*,
- *width* is not compatible with *altitude*.

#### 20.4.9 `QuantityPoint<T>` concept

`QuantityPoint` concept is satisfied by all types being either a specialization or derived from `quantity_point` class template.

##### 20.4.9.1 `QuantityPointOf<T, V>` concept

`QuantityPointOf` concept is satisfied by all the quantity points `T` that match the following value `V`:

| `V` | Condition |
| --- | --- |
| `QuantitySpec` | The quantity point quantity specification satisfies `ReferenceOf<V>` concept. |
| `PointOrigin` | The *point* and `V` have the same absolute point origin. |

##### 20.4.9.2 `QuantityPointLike<T>` concept

`QuantityPointLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_point_like_traits` type trait yields a valid type that provides:

- `reference` static data member that matches the `Reference` concept.
- `point_origin` static data member that matches the `PointOrigin` concept.
- `rep` type that matches `RepresentationOf` concept with the character provided in `reference`.
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity_point` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity_point` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the quantity being the offset of the point from the origin,
- `from_numerical_value(rep)` static member function returning `T`.

For example, this is how support for a `std::chrono::time_point` of `std::chrono::seconds` can be provided:

```cpp
template<typename C>
struct quantity_point_like_traits<std::chrono::time_point<C, std::chrono::seconds>> {
  static constexpr auto reference = detail::time_unit_from_chrono_period<Period>();
  static constexpr auto point_origin = chrono_point_origin<C>;
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = Rep;
  using T = std::chrono::time_point<C, std::chrono::duration<Rep, Period>>;

  [[nodiscard]] static constexpr rep to_numerical_value(const T& tp) noexcept(std::is_nothrow_copy_constructible_v<rep>)
  {
    return tp.time_since_epoch().count();
  }

  [[nodiscard]] static constexpr T from_numerical_value(const rep& v) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return T(std::chrono::duration<Rep, Period>(v));
  }
};

quantity_point qp = time_point_cast<std::chrono::seconds>(std::chrono::system_clock::now());
std::chrono::sys_seconds q = qp + 42 * s;
```

#### 20.4.10 Bikeshedding concepts

This chapter provides some alternative names in `standard_case` for concepts.

| Before | After | Alternative | Comments |
| --- | --- | --- | --- |
| `Dimension` | `dimension` | `some_dimension` |  |
| `DimensionOf` | `dimension_of` |  | This concept is never used in the framework but might be useful to users. |
| `QuantitySpec` | `quantity_spec` | `some_quantity_spec` | “After” requires renaming `quantity_spec` to `named_quantity_spec` for a class template. |
| `QuantitySpecOf` | `quantity_spec_of` |  |  |
| `UnitMagnitude` | `unit_magnitude` | `some_unit_magnitude` |  |
| `Unit` | `unit` | `some_unit` | “Alternative” allows renaming named_unit class template to unit |
| `PrefixableUnit` | `prefixable_unit` |  |  |
| `UnitOf` | `unit_of` |  |  |
| `Reference` | `reference` | `some_reference` | Collides with `reference` class template, but we have some ideas how to remove the class template. |
| `ReferenceOf` | `reference_of` |  |  |
| `RepresentationOf` | `representation_of` |  |  |
| `Quantity` | `delta_quantity` | `some_quantity` | Collides with `quantity` class template. |
| `QuantityOf` | `delta_quantity_of` | `quantity_of` |  |
| `QuantityLike` | `delta_quantity_like` | `quantity_like` |  |
| `PointOrigin` | `point_origin` | `some_point_origin` |  |
| `PointOriginFor` | `point_origin_for` |  |  |
| `QuantityPoint` | `point_quantity` | `some_quantity_point` | Collides with `quantity_point` class template. |
| `QuantityPointOf` | `point_quantity_of` | `quantity_point_of` |  |
| `QuantityPointLike` | `point_quantity_like` | `quantity_point_like` |  |

How do we like `some_XXX` practice? It is already being used in some open source projects. It also reads nicely against `XXX_of`, which provides more restrictive constraints. If we are OK with it, should we apply it only in the conflicting cases or apply everywhere for consistency?

If we go for `some_XXX` then we can leave `quantity_spec` as the class template, and also we could rename `named_unit` class template to `unit` so the user can type less while defining their own system entities.

Here is a comparison of quantity specification and units definitions in both alternatives:

Today (inconsistent?):

```cpp
inline constexpr struct length : quantity_spec<dim_length> {} length;
inline constexpr struct time   : quantity_spec<dim_time> {} time;
inline constexpr struct speed  : quantity_spec<length / time> {} speed;

inline constexpr struct metre  : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
```

Option 1:

```cpp
inline constexpr struct length : named_quantity_spec<dim_length> {} length;
inline constexpr struct time   : named_quantity_spec<dim_time> {} time;
inline constexpr struct speed  : named_quantity_spec<length / time> {} speed;

inline constexpr struct metre  : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
```

Option 2:

```cpp
inline constexpr struct length : quantity_spec<dim_length> {} length;
inline constexpr struct time   : quantity_spec<dim_time> {} time;
inline constexpr struct speed  : quantity_spec<length / time> {} speed;

inline constexpr struct metre  : unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : unit<"s", kind_of<isq::time>> {} second;
```

Please also note, that we’ve added `point_quantityXXX` alternatives as we consider replacing `quantity_point<..., Rep>` with `quantity<point<...>, Rep>`. In such a case, we could still need `some_quantity = delta_quantity || point_quantity`.

### 20.5 Symbolic expressions

Modern C++ physical quantities and units libraries use opaque types to improve the user experience while analyzing compile-time errors or inspecting types in a debugger. This is a huge usability improvement over the older libraries that use aliases to refer to long instantiations of class templates.

#### 20.5.1 Derived entities

Having such strong types for entities is not enough. While doing arithmetics on them, we get derived entities, and they also should be easy to understand and correlate with the code written by the user. This is where symbolic expressions come into play.

The library should use the same unified approach to represent the results of arithmetics on all kinds of entities. It is worth mentioning that a generic purpose symbolic expressions library is not a good solution for a physical quantities and units library.

Let’s assume that we want to represent the results of the following two unit equations:

- `metre / second * second`
- `metre * metre / metre`

Both of them should result in a type equivalent to `metre`. A general-purpose library will probably result with the types similar to the below:

- `mul<div<metre, second>, second>`
- `div<mul<metre, metre>, metre>`

Comparing such types for equivalence would not only be very expensive at compile-time but would also be really confusing to the users observing them in the compilation logs. This is why we need a dedicated solution here.

In a physical quantities and units library, we need symbolic expressions to express the results of

- dimension equations,
- quantity type equations,
- unit equations, and
- unit magnitude equations.

If the above equation results in a derived entity, we must create a type that clearly describes what we are dealing with. We need to pack a simplified expression template into some container for that. There are various possibilities here. The table below presents the types generated from unit expressions by two leading products on the market in this subject:

| Unit | [[mp-units]](https://mpusz.github.io/mp-units) | [[Au]](https://aurora-opensource.github.io/au) |
| --- | --- | --- |
| `N⋅m` | `derived_unit<metre, newton>` | `UnitProduct<Meters, Newtons>` |
| `1/s` | `derived_unit<one, per<second>>` | `Pow<Seconds, -1>` |
| `km/h` | `derived_unit<kilo_<metre>, per<hour>>` | `UnitProduct<Kilo<Meters>, Pow<Hours, -1>>` |
| `kg⋅m²/(s³⋅K)` | `derived_unit<kilogram, pow<metre, 2>, per<kelvin, power<second, 3>>>` | `UnitProduct<Pow<Meters, 2>, Kilo<Grams>, Pow<Seconds, -3>, Pow<Kelvins, -1>>` |
| `m²/m` | `metre` | `Meters` |
| `km/m` | `derived_unit<kilo_<metre>, per<metre>>` | `UnitProduct<Pow<Meters, -1>, Kilo<Meters>>` |
| `m/m` | `one` | `UnitProduct<>` |

It is a matter of taste which solution is better. While discussing the pros and cons here, we should remember that our users often do not have a scientific background. This is why we recommend to use syntax that is as similar to the correct English language as possible. It consistently uses the `derived_` prefix for types representing derived units, dimensions, and quantity specifications. Those are instantiated first with the contents of the numerator followed by the entities of the denominator (if present) enclosed in the `per<...>` symbolic expression.

#### 20.5.2 Identities

The arithmetics on units, dimensions, and quantity types require a special identity value. Such value can be returned as a result of the division of the same entities, or using it should not modify the symbolic expression on multiplication.

We chose the following names here:

- `one` in the domain of units,
- `dimension_one` in the domain of dimensions,
- `dimensionless` in the domain of quantity types.

The above names were selected based on the following quote from [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html):

> A quantity whose dimensional exponents are all equal to zero has the dimensional product denoted A<sup>0</sup>B<sup>0</sup>C<sup>0</sup>… = 1, where the symbol 1 denotes the corresponding dimension. There is no agreement on how to refer to such quantities. They have been called **dimensionless** quantities (although this term should now be avoided), quantities with **dimension one**, quantities with dimension number, or quantities with the **unit one**. Such quantities are dimensionally simply numbers. To avoid confusion, it is helpful to use explicit units with these quantities where possible, e.g., m/m, nmol/mol, rad, as specified in the SI Brochure.

#### 20.5.3 Supported operations and their results

The table below presents all the operations that can be done on units, dimensions, and quantity types in a quantities and units library. The right column presents corresponding expression templates being their results:

| Operation | Resulting template expression arguments |
| --- | --- |
| `A * B` | `A, B` |
| `B * A` | `A, B` |
| `A * A` | `power<A, 2>` |
| `{identity} * A` | `A` |
| `A * {identity}` | `A` |
| `A / B` | `A, per<B>` |
| `A / A` | `{identity}` |
| `A / {identity}` | `A` |
| `{identity} / A` | `{identity}, per<A>` |
| `pow<2>(A)` | `power<A, 2>` |
| `pow<2>({identity})` | `{identity}` |
| `sqrt(A)` or `pow<1, 2>(A)` | `power<A, 1, 2>` |
| `sqrt({identity})` or `pow<1, 2>({identity})` | `{identity}` |

#### 20.5.4 Simplifying the resulting symbolic expressions

To limit the length and improve the readability of generated types, there are many rules to simplify the resulting symbolic expression.

1. **Ordering**

   The resulting comma-separated arguments of multiplication are always sorted according to a specific predicate. This is why:

   ```cpp
   static_assert(A * B == B * A);
   static_assert(std::is_same_v<decltype(A * B), decltype(B * A)>);
   ```

   This is probably the most important of all the steps, as it allows comparing types and enables the rest of the simplification rules.

   User-provided symbols (when available) are not guaranteed to be unique in the project. For example, someone may use `"s"` as a symbol for a count of samples, which, when used in a unit expression with seconds, would cause fatal consequences (e.g., `sample * second` would yield `s²`, or `sample / second` would result in `one`).

   This is why the library chose to use type name identifiers in such cases. As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list. If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
2. **Aggregation**

   In case two of the same type identifiers are found next to each other on the argument list, they will be aggregated in one entry:

   | Before | After |
   | --- | --- |
   | `A, A` | `power<A, 2>` |
   | `A, power<A, 2>` | `power<A, 3>` |
   | `power<A, 1, 2>, power<A, 2>` | `power<A, 5, 2>` |
   | `power<A, 1, 2>, power<A, 1, 2>` | `A` |
3. **Simplification**

   In case two of the same type identifiers are found in the numerator and denominator argument lists, they are being simplified into one entry:

   | Before | After |
   | --- | --- |
   | `A, per<A>` | `{identity}` |
   | `power<A, 2>, per<A>` | `A` |
   | `power<A, 3>, per<A>` | `power<A, 2>` |
   | `A, per<power<A, 2>>` | `{identity}, per<A>` |

   It is important to notice here that only the elements with exactly the same type are being simplified. This means that, for example, `m/m` results in `one`, but `km/m` will not be simplified. The resulting derived unit will preserve both symbols and their relative magnitude. This allows us to properly print symbols of some units or constants that require such behavior. For example, the Hubble constant is expressed in `km⋅s⁻¹⋅Mpc⁻¹`, where both `km` and `Mpc` are units of *length*.

   In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results. The generated types were much longer and harder to reason about, which decreased the compile-time errors user experience. We’ve also got issues with basic library operations (e.g., determining the best common unit). More details can be found in [Refining symbolic expressions simplification rules](https://github.com/mpusz/mp-units/discussions/582) discussion.
4. **Repacking**

   In case an expression uses two results of some other operations, the components of its arguments are repacked into one resulting type and simplified there.

   For example, assuming:

   ```cpp
   constexpr auto X = A / B;
   ```

   then:

   | Operation | Resulting template expression arguments |
   | --- | --- |
   | `X * B` | `A` |
   | `X * A` | `power<A, 2>, per<B>` |
   | `X * X` | `power<A, 2>, per<power<B, 2>>` |
   | `X / X` | `{identity}` |
   | `X / A` | `{identity}, per<B>` |
   | `X / B` | `A, per<power<B, 2>>` |

#### 20.5.5 Symbolic expressions in action

Thanks to all of the steps described above, a user may write the code like this one:

```cpp
using namespace si::unit_symbols;
quantity speed = isq::speed(60. * km / h);
quantity duration = 8 * s;
quantity acceleration1 = speed / duration;
quantity acceleration2 = isq::acceleration(acceleration1.in(m / s2));
std::cout << "acceleration: " << acceleration1 << " (" << acceleration2 << ")\n";
```

the text output provides:

```
acceleration: 7.5 km h⁻¹ s⁻¹ (2.08333 m/s²)
```

The above program will produce the following types for *acceleration* quantities:

- `acceleration1`

  ```
  quantity<reference<derived_quantity_spec<isq::speed, per<isq::time>>,
                     derived_unit<si::kilo_<si::metre>, per<non_si::hour, si::second>>>{},
           double>
  ```
- `acceleration2`

  ```
  quantity<reference<isq::acceleration,
                     derived_unit<si::metre, per<power<si::second, 2>>>>{},
           double>>
  ```

### 20.6 Operations on units, dimensions, quantity types, and references

Modern C++ physical quantities and units library should expose compile-time constants for units, dimensions, and quantity types. Each of such constants should be of a different type. Said otherwise, every unit, dimension, and quantity type has a unique type and a compile-time instance. This allows us to do regular algebra on such identifiers and get proper types as results of such operations.

The operations exposed by such a library should include at least:

- multiplication (e.g., `newton * metre`),
- division (e.g., `metre / second`),
- power (e.g., `pow<2>(metre)` or `pow<1, 2>(metre * metre)`).

To improve the usability of the library, we also recommend adding:

- square root (e.g., `sqrt(metre * metre)` as equivalent to `pow<1, 2>(metre * metre)`),
- cubic root (e.g., `cbrt(metre * metre * metre)` as equivalent to `pow<1, 3>(metre * metre * metre)`),
- inversion (e.g., `inverse(second)` as equivalent to `one / second`).

Additionally, for units only, to improve the readability of the code, it makes sense to expose the following:

- square power (e.g., `square(metre)` is equivalent to `pow<2>(metre)`),
- cubic power (e.g., `cubic(metre)` is equivalent to `pow<3>(metre)`).

The above two functions could also be considered for dimensions and quantity types. However, `cubic(length)` does not seem to make much sense, and probably `pow<3>(length)` should be preferred instead.

Please note that we want to keep most of the unit magnitude’s interface *implementation-defined*. This is why we provide only a minimal mandatory interface for them. For example, we have introduced a `mag_power<Basis, Num, Den = 1>` helper to get a power of a magnitude. With that, a user should probably never need to reach for an alternative `pow<Num, Den>(mag<Base>)` version. However, the latter could be considered more consistent with the same operation done on other abstractions. Let’s compare how a unit can be defined using both of those syntaxes:

- with `mag_power`:

```cpp
 inline constexpr struct electronvolt :
  named_unit<"eV", mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * si::joule> {} electronvolt;
```

- with `pow<>(mag<>)`:

```cpp
 inline constexpr struct electronvolt :
   named_unit<"eV", mag_ratio<1'602'176'634, 1'000'000'000> * pow<-19>(mag<10>) * si::joule> {} electronvolt;
```

Even though it might be inconsistent with operations on other abstractions, we’ve decided to use the first one as it seems easier to read and better resembles what we write on paper. However, we are not married to it, and we can change it if the LEWG prefers consistency here. Please note, that in such a case, for consistency, we probably should also provide `sqrt()` and `cbrt()` operations. However, those are really rare operations for magnitudes (we have not found any use cases for those in [[mp-units]](https://mpusz.github.io/mp-units) so far).

#### 20.6.1 Equality and equivalence

Units, their magnitudes, dimensions, quantity types, and references can be checked for equality with `operator==`. Equality for all the tag types is a simple check if both arguments are of the same type. For example, for dimensions, we do the following:

```cpp
template<Dimension Lhs, Dimension Rhs>
consteval bool operator==(Lhs lhs, Rhs rhs)
{
  return is_same_v<Lhs, Rhs>;
}
```

Equality for references is a bit more complex:

```cpp
template<typename Q1, typename U1, typename Q2, typename U2>
consteval bool operator==(reference<Q1, U1>, reference<Q2, U2>)
{
  return is_same_v<reference<Q1, U1>, reference<Q2, U2>>;
}

template<typename Q1, typename U1, Unit U2>
consteval bool operator==(reference<Q1, U1>, U2 u2)
{
  return Q1{} == get_quantity_spec(u2) && U1{} == u2;
}
```

The second overload allows us to mix associated units and specializations of `reference` class template (both of them satisfy `Reference` concept). Thanks to this, we can check the following:

```cpp
static_assert(isq::time[second] != second);
static_assert(kind_of<isq::time>[second] == second);
```

Units may have many shades. This is why an equality check is not enough for them. In many cases, we don’t need to check against a concrete unit, but we want to ensure that the underlying numerical value will not change during a unit conversion. In such cases we check for equivalence. Watt (`W`) should be equivalent to `J/s` and `kg m²/s³`. Also, a litre (`l`) should be equivalent to a cubic decimetre (`dm³`).

To check for unit equivalence, currently we convert each unit to its canonical representation (scaled unit with magnitude expressed relative to some “blessed” implementation-specific reference unit) and then, we compare if the reference units and the magnitudes are the same:

```cpp
consteval bool equivalent(Unit auto lhs, Unit auto rhs)
{
  const auto lhs_canonical = get_canonical_unit(lhs);
  const auto rhs_canonical = get_canonical_unit(rhs);
  return lhs_canonical.mag == rhs_canonical.mag && lhs_canonical.reference_unit == rhs_canonical.reference_unit;
}
```

*Note: A `canonical_unit` is an implementation detail and is not exposed in public APIs for now.*

For example:

```cpp
static_assert(N != kg * m / s2);
static_assert(equivalent(N, kg * m / s2));
```

It is also worth noting that the above implementation makes the last line below pass, even though we can’t convert a quantity measured in `Hz` to the one in `Bq`:

```cpp
quantity q1 = (42 * Hz).in(one / s);
quantity q2 = (42 * Bq).in(one / s);
quantity q3 = (42 * one / s).in(Hz);
quantity q4 = (42 * one / s).in(Bq);
// quantity q5 = (42 * Hz).in(Bq);  // does not compile

quantity q6 = 1 * Hz + 1 * one / s;
quantity q7 = 1 * Bq + 1 * one / s;
// quantity q8 = 1 * Hz + 1 * Bq;   // does not compile

static_assert(Hz != Bq);
static_assert(Hz != one / s);
static_assert(Bq != one / s);
static_assert(equivalent(Hz, one / s));
static_assert(equivalent(Bq, one / s));
static_assert(equivalent(Hz, Bq));  // OK ???
```

Depending on the desired semanthics of `equivalent` function, we may want to make the last line to fail as well.

#### 20.6.2 Ordering

Ordering for dimensions and quantity types has no physical sense.

We could entertain adding ordering for units, but this would work only for quantities having the same reference unit, which would be inconsistent with how equality works.

Let’s see the following example:

```cpp
constexpr Unit auto my_unit = si::second;
if constexpr (my_unit == si::metre) {
 // ...
}
if constexpr (my_unit > si::metre) {
 // ...
}
if constexpr (my_unit > si::nano(si::second)) {
 // ...
}
```

In the above code, the first check could be useful for some use cases. However, the second one is impossible to implement and should not compile. The third one could be considered useful, but the current version of [[mp-units]](https://mpusz.github.io/mp-units) does not expose such an interface to limit potential confusion. Also, it is really hard to mathematically prove that the unit magnitude representation that we use in the library (based on primes factorization) is greater or smaller than the other one in some cases.

This is why we discourage providing ordering operations for any of those entities.

#### 20.6.3 Arithmetics

For consistency, we could also define arithmetic `operator+` and `operator-` for such entities to resemble the operations performed on quantities. For example:

```cpp
quantity q1 = isq::radius(1 * m) + isq::distance(1 * cm);
quantity q2 = isq::position_vector(1 * m) - isq::position_vector(1 * cm);
// quantity q3 = isq::position_vector(1 * m) + isq::position_vector(1 * cm);  // should not compile
```

returns:

- `quantity<isq::length[cm], int>` for `q1`,
- `quantity<isq::displacement[cm], int>` for `q2`.

Users may be interested to check what will be the result of performing such operations on ingredients of the quantity. As we say that “addition of a radius and a distance should yield a length” it would be good to model this arithmetics on our symbolic constants as well:

```cpp
static_assert(isq::radius + isq::distance == isq::length);
static_assert(isq::position_vector - isq::position_vector == isq::displacement);
// constexpr auto qs = isq::position_vector + isq::position_vector;  // should not compile
```

The operations that we expose must cover all of the operations we can do on quantities. This is why we not only have to overload operators but also expose other operations that can be performed on vector, tensor, and complex quantities:

```cpp
static_assert(implicitly_convertible(magnitude(isq::velocity), isq::speed));
static_assert(implicitly_convertible(scalar_product(isq::force, isq::displacement), isq::work));
static_assert(implicitly_convertible(vector_product(isq::position_vector, isq::force), isq::moment_of_force));
static_assert(implicitly_convertible(real(isq::complex_power), isq::active_power));
static_assert(implicitly_convertible(imag(isq::complex_power), isq::reactive_power));
static_assert(implicitly_convertible(modulus(isq::complex_power), isq::apparent_power));
```

Addition and subtractions on units is also possible, but it is more controverisal and less useful, so we do not propose them at this time:

```cpp
static_assert(m + cm == cm);
static_assert(km + mi == get_common_unit(km, mi));
```

### 20.7 Units

ISO specifies a measurement unit as a real scalar quantity, defined and adopted by convention, with which any other quantity of the same kind can be compared to express the ratio of the two quantities as a number.

In other words, a unit is a specific amount of a quantity. Such a definition is impractical from the programming language point of view. Let’s see the following hypothetical example (the below API is not a part of this proposal):

```cpp
namespace si {

constexpr auto metre = quantity<length>{1};
constexpr auto kilometre = 1000 * metre;

}

quantity<si::kilometre> distance = 42 * si::kilometre;
```

The above code would be consistent with the ISO definition however, it imposes several issues:

- creates a circular dependency for a `quantity` class,
- embeds a concrete representation type in the unit,
- loses all the benefits associated with our prime-factorized unit magnitudes (i.e., being able to express any ratio without the overflow of the underlying representation type),
- `quantity<length>{1}` may mean different things in namespaces of different systems which makes it much harder to provide interoperability between them,
- does not provide an opportunity to specify the unit symbol.

This is why decided to base unit definitions on tag types.

#### 20.7.1 `space_before_unit_symbol` alternatives

As described in the `space_before_unit_symbol` customization point chapter, some units should not be prepended with a space. We proposed the following customization point:

```cpp
template<Unit auto U>
constexpr bool space_before_unit_symbol = true;
```

It is important to note that the need for some customization is only for a small fraction of all units. It works but it has some disadvantages. First, it might be harder to reason about the units definitions because the spacialization of this variable template may be in a different location in the source code than the unit definition. Also, it breaks our assumption that we can define all the properties of the entity with a single line of a C++ code.

Maybe we should add an additional parameter (defaulted to `true`) to the `named_unit` class template to handle this?

#### 20.7.2 Prefixing units with prefixes

Initially [[mp-units]](https://mpusz.github.io/mp-units) library had one additional customization point for units:

```cpp
template<PrefixableUnit auto U>
constexpr bool unit_can_be_prefixed = true;
```

The above was used to disallow prefixes for some units, such as hours or degrees Celsius. However, after some time, we got [the issue on GitHub](https://github.com/mpusz/mp-units/issues/604) asking to allow prefixes for the latter.

It turns out that the certification organizations are not consistent here. ISO 80000-5 says:

> Prefixes are not allowed in combination with the unit °C.

However, [NIST states](https://www.nist.gov/pml/owm/writing-si-metric-system-units):

> Prefix symbols may be used with the unit symbol ºC, and prefix names may be used with the unit name “degree Celsius.” For example, 12 mºC (12 millidegrees Celsius) is acceptable. However, to avoid confusion, prefix symbols (and prefix names) are not used with the time-related unit symbols (names) min (minute), h (hour), d (day); nor with the angle-related symbols (names) º (degree), ’ (minute), and ” (second).

As a result of this issue and associated discussion, we decided to remove `unit_can_be_prefixed` support from the library, and we do not propose it here either.

### 20.8 Unit magnitudes

> [ *Note:* The word “magnitude” appears in this paper with three distinct meanings:
> 
> - **Quantity magnitude** (ISO 80000): the “magnitude of a quantity” is the quantity value itself — a number and a reference together expressing how large the quantity is.
> - **Vector magnitude**: the Euclidean norm of a vector, `|v|`, provided by the `norm()` CPO (also accessible as `magnitude(v)` for compatibility with physics terminology).
> - **Unit magnitude** (this section): a compile-time scaling factor relating a unit to other units of the same dimension.
> 
>  — *end note* ]

Each unit is associated with a magnitude representing its scaling factor relative to other units of the same dimension. However, absolute magnitude values have no physical meaning—only the *ratio* between magnitudes matters. For example, once we assign magnitude \(m_f\) to *foot*, we must assign \(3m_f\) to *yard* and \(m_f/12\) to *inch*.

We make magnitude interfaces mostly *implementation-defined*, exposing only minimal public APIs for interoperability while leaving freedom to implementers.

#### 20.8.1 Requirements beyond `std::ratio`

Magnitudes must support operations that units require: products and rational powers. Additionally, they must handle irrational ratios like \(\frac{\pi}{180}\) between degrees and radians.

`std::ratio` fails these requirements:

- Integral types too small for eight SI prefixes
- Not closed under rational powers (e.g., \(\sqrt{2}\))
- Cannot represent irrational factors like \(\pi\)
- Vulnerable to overflow when raised to powers

#### 20.8.2 Vector space representation with prime factorization

The solution uses prime factorization as a vector space basis. Each magnitude is a product of prime powers, with irrational constants (like \(\pi\)) added as additional basis elements when needed.

Examples using Astronomical Units (au), meters (m), degrees (deg), and radians (rad):

| Unit ratio | `std::ratio` | Vector space magnitude |
| --- | --- | --- |
| \(\left(\frac{\text{au}}{\text{m}}\right)\) | `std::ratio<149'597'870'700>` | `magnitude<power_v<2, 2>(), 3, power_v<5, 2>(), 73, 877, 7789>` |
| \(\left(\frac{\text{au}}{\text{m}}\right)^2\) | Overflow | `magnitude<power_v<2, 4>(), power_v<3, 2>(), power_v<5, 4>(), power_v<73, 2>(), power_v<877, 2>(), power_v<7789, 2>()>` |
| \(\sqrt{\frac{\text{au}}{\text{m}}}\) | Unrepresentable | `magnitude<2, power_v<3, 1, 2>(), 5, power_v<73, 1, 2>(), power_v<877, 1, 2>(), power_v<7789, 1, 2>()>` |
| \(\left(\frac{\text{rad}}{\text{deg}}\right)\) | Unrepresentable | `magnitude<power_v<2, 2>(), power_v<3, 2>(), power_v<pi_c{}, -1>(), 5>` |

Trade-offs: more verbose type names (mitigated by opaque types) and dependency on compile-time prime factorization.

#### 20.8.3 Compile-time factorization challenge

Users write `mag<149'597'870'700>`, which the library expands to its prime factorization. Large primes (e.g., 334,524,384,739 in the proton mass) cause compilers to assume infinite loops and terminate compilation when using trial division.

[[P3133R0]](https://wg21.link/p3133r0) explored `std::first_factor(uint64_t)` as a solution. Feedback showed a fast primality checker suffices for practical cases, though the function would still benefit the standard library and other domains.

#### 20.8.4 Common unit magnitude

Computing common magnitude: for each basis vector, take the minimum exponent across participating magnitudes (using implicit “0” for omitted vectors).

Example: \(\text{COM}[18, \frac{80}{3}] = \text{COM}[(2 \cdot 3^2), (2^4 \cdot 3^{-1} \cdot 5)] = 2^{\min[1,4]} \cdot 3^{\min[2,-1]} \cdot 5^{\min[0,1]} = \frac{2}{3}\)

### 20.9 Physical constants

#### 20.9.1 Constants as units

Physical constants are implemented as units rather than `constexpr` quantity values. Benefits:

- Constants in both numerator and denominator simplify at compile-time (like regular units)
- Expensive multiplication/division delayed until user selects output unit
- Enables simpler/faster representation types (e.g., integral instead of floating-point)

Example definitions:

```cpp
namespace si {

namespace si2019 {

inline constexpr struct speed_of_light_in_vacuum :
  named_constant<"c", mag<299'792'458> * metre / second> {} speed_of_light_in_vacuum;

}  // namespace si2019

inline constexpr struct magnetic_constant :
  named_constant<{u8"μ₀", "u_0"}, mag<4> * mag_power<10, -7> * π * henry / metre> {} magnetic_constant;

}  // namespace si
```

Usage example (vacuum permittivity):

```cpp
constexpr auto permeability_of_vacuum = 1. * si::magnetic_constant;
constexpr auto speed_of_light_in_vacuum = 1 * si::si2019::speed_of_light_in_vacuum;
QuantityOf<isq::permittivity_of_vacuum> auto q = 1 / (permeability_of_vacuum * pow<2>(speed_of_light_in_vacuum));
std::cout << q << " = " << q.in(F / m) << "\n";  // prints: 1  μ₀⁻¹ c⁻² = 8.85419e-12 F/m
```

#### 20.9.2 Negative constants

Named units may not be enough to model all of the constants out there. It turns out that there are many negative constants. Some of them can be found in [CODATA](https://physics.nist.gov/cuu/Constants). One such constant is [*helion g factor*](https://physics.nist.gov/cgi-bin/cuu/Value?ghn).

Trying to model this with `named_unit` fails to compile. The reason of the error is the fact that the conversion factors between units should be positive. This means that reusing `named_unit` to define constants may not be the best idea and we probably need to introduce a dedicated class.

This is why we need to introduce a new class template:

```cpp
inline constexpr struct helion_g_factor :
  named_constant<basic_symbol_text{"𝘨ₕ", "g_h"}, mag<-ratio{4'255'250'615, 1'000'000'000}> * one> {} helion_g_factor;
```

Additionally, such a solution does not allow the constant to be prefixed or associated with a `quantity_spec`.

### 20.10 Quantity specifications

Quantity specification provides all the data about the quantity type (i.e., kind, character, recipe, relation to other quantities in the hierarchy). It does not specify a unit, though.

#### 20.10.1 Bikeshedding `quantity_spec`

The “quantity specification” term is not provided in ISO or BIPM metrology dictonaries and was invented for the need of this library. This means that we should probably consider some other names for this abstraction:

- `quantity_specification`,
- `q_spec`,
- `q_specification`,
- `quantity_definition`,
- `quantity_def`,
- `quantity_data`,
- `q_data`.

### 20.11 Quantity references

*Note: We know that probably the term “reference” will not survive too long in the Committee, but we couldn’t find a better name for it in the [[mp-units]](https://mpusz.github.io/mp-units) library ([https://github.com/mpusz/mp-units/issues/486](https://github.com/mpusz/mp-units/issues/486)).*

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) says:

> **quantity** - property of a phenomenon, body, or substance, where the property has a magnitude that can be expressed as a number and a reference. … A reference can be a measurement unit, a measurement procedure, a reference material, or a combination of such.

In the library a quantity reference represents all the domain-specific meta-data about the quantity besides its representation type and its value. A `Reference` concept is satisfied by either of:

- an associated unit (e.g., `si::metre`),
- an instantiation of the `reference<QuantitySpec, Unit>` class template explicitly specifying the quantity type and its unit.

A reference type is implicitly created as a result of the following expression:

```cpp
constexpr Reference auto distance = isq::distance[m];
```

The above example defines a variable of type `reference<isq::distance, si::metre>`.

The `reference` class template also exposes an arithmetic interface similar to the one that we have already discussed in case of units and quantity types. It simply forwards the operation to its quantity type and unit members.

```cpp
constexpr ReferenceOf<isq::speed> auto speed = distance / si::second;
```

As a result we get a `reference<derived_quantity_spec<distance, per<time>>, derived_unit<metre, per<second>>>` type.

Similarly to the `Unit`, such a reference can be used to construct a quantity:

```cpp
QuantityOf<isq::speed> auto s = 60 * speed;
```

#### 20.11.1 Bikeshedding `reference`

The term `reference` is highly overloaded in the C++ domain. This is why we should probably rename the type that was successfully used in [[mp-units]](https://mpusz.github.io/mp-units). Here are a few proposals:

- `quantity_reference`
- `quantity_ref`
- `q_reference`
- `q_ref`

Please note that the longer the identifier we choose, the longer and harder it will be to grasp compiler error messages. A user never types this type identifier in the code (although a user might type an associated concept `Reference` or `ReferenceOf`).

### 20.12 Quantities

The `quantity` class template is a workhorse of the library. It can be considered a generalization of `std::chrono::duration`, but is not directly compatible with it.

Based on the ISO definition provided in the Quantity references chapter, the `quantity` class template has the following signature:

```cpp
template<Reference auto R, RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity;
```

It stores only one data member of `Rep` type. Unfortunately, this data member has to be publicly exposed to satisfy the C++ language requirements for [structural types](https://eel.is/c++draft/temp.param#def:type,structural). Hopefully, the language rules for structural types will improve with time before this library gets standardized.

#### 20.12.1 Multiply syntax commutativity

As of today, the multiply syntax that creates quantities is not commutative:

```cpp
quantity q1 = 1 * m;  // OK
quantity q2 = m * 1;  // Compile-time error
```

We decided to go this way to increase the readability of the code and limit possible confusion with this syntax. After a while, we extended it to support also the following:

```cpp
quantity q3 = 1 * m / s;    // OK
quantity q4 = 1 * m * m;    // OK
quantity q5 = 1 / s * m;    // OK
quantity q6 = s / 2;        // Compile-time error
quantity q7 = m * (1 / s);  // Compile-time error
quantity q8 = m * (1 * m);  // Compile-time error
```

However, [[mp-units]](https://mpusz.github.io/mp-units) users [requested the following use case](https://github.com/mpusz/mp-units/issues/621):

```cpp
if(num < Unit / 1'000'000'000'000) {
  quantity<si::femto<Unit>, double> n{num};
  out << n;
} else if(num < Unit / 1'000'000'000) {
  quantity<si::pico<Unit>, double> n{num};
  out << n;
} else // ...
```

Today, this does not compile. Should we extend the multiply syntax to support such use cases and with this have entire commutative property?

#### 20.12.2 Why don’t we use UDLs to create quantities?

Quantity construction chapter describes and explains why we introduced the multiply syntax as a construction helper for quantities. Many people ask why we chose this approach over battle-proven User Defined Literals (UDLs) that work well for the `std::chrono` library.

It turns out that many reasons make UDLs a poor choice for a physical units library:

1. UDLs work only with literals (compile-time known values). Our observation is that besides the unit tests, only a few compile-time known quantity values are used in the production code. Please note that for Physical constants, we recommend using units rather than compile-time constants.
2. Typical implementations of UDLs tend to always use the widest representation type available. In the case of `std::chrono::duration`, the following is true:

   ```cpp
   using namespace std::chrono_literals;
   auto d1 = 42s;
   auto d2 = 42.s;
   static_assert(std::is_same_v<decltype(d1)::rep, std::int64_t>);
   static_assert(std::is_same_v<decltype(d2)::rep, long double>);
   ```

   When such UDL is intermixed in arithmetics with any quantity type of a shorter representation type, it will always expand it to the longest one. In other words, such long type spreads until all types use it everywhere.
3. While increasing the coverage for the [[mp-units]](https://mpusz.github.io/mp-units) library, we learned that many unit symbols conflict with built-in types or numeric extensions. A few of those are: `F` (farad), `J` (joule), `W` (watt), `K` (kelvin), `d` (day), `l` or `L` (litre), `erg`, `ergps`. Using the `'_'` prefix would make it work for [[mp-units]](https://mpusz.github.io/mp-units), but if the library is standardized, those naming collisions would be a big issue. This is why we came up with the `_q_` prefix that would become `q_` after standardization (e.g., `42q_s`), which is not that nice anymore.
4. UDLs with the same identifiers defined in different namespace can’t be disambiguated in the C++ language. If both SI and CGS systems define `q_s` UDL for a second unit, then it would not be possible to specify which one to use in case both namespaces are “imported” with using directives.
5. Another bad property of UDLs is that they do not compose. A coherent unit of angular momentum would have a UDL specified as `q_kg_m2_per_s`. Now imagine that we want to make every possible user happy. How many variations of that unit would we predefine for differently scaled versions of all unit ingredients?
6. UDLs are also really expensive to define and specify. Typically, for each unit, we need two definitions. One for integral and another one for floating-point representation. In version 0.8.0 of the [[mp-units]](https://mpusz.github.io/mp-units) library, the coherent unit of angular momentum was defined as:

   ```cpp
   constexpr auto operator"" _q_kg_m2_per_s(unsigned long long l)
   {
     gsl_ExpectsAudit(std::in_range<std::int64_t>(l));
     return angular_momentum<kilogram_metre_sq_per_second, std::int64_t>(static_cast<std::int64_t>(l));
   }
   
   constexpr auto operator"" _q_kg_m2_per_s(long double l)
   {
     return angular_momentum<kilogram_metre_sq_per_second, long double>(l);
   }
   ```

The multiply syntax that we chose for this library does not have any of those issues.

#### 20.12.3 Special values of a quantity

`quantity` class template, similarly to `std::chrono::duration`, exposes some special values as `static` member functions:

- `min()`,
- `max()`,
- `zero()`.

Also, similarly to `std::chrono::duration` those functions are implemented in terms of a type trait:

```cpp
template<typename Rep>
struct representation_values : std::chrono::duration_values<Rep> {
  static constexpr Rep one() noexcept
    requires std::constructible_from<Rep, int>
 {
    return Rep(1);
 }
};
```

An additional the `one()` function in `representation_values` is provided for use with the multiply syntax when constructing quantities. Users can create a quantity with numerical value of one using: `representation_values<double>::one() * si::metre`. This function is not exposed as a static member of `quantity` because `one()` is not a true multiplicative identity for dimensional quantities—for example, `pow<2>(quantity<si::metre>::one())` would change the dimension from *length* to *area*.

Please also note that in C++26, `std::chrono::duration_values` is not a part of the freestanding library.

#### 20.12.4 Quantity arithmetics

##### 20.12.4.1 `quantity` is a numeric wrapper

If we think about it, the `quantity` class template is just a “smart” numeric wrapper. It exposes properly constrained set of arithmetic operations on one or two operands.

Every single arithmetic operator is exposed by the `quantity` class template only if the underlying representation type provides it as well and its implementation has proper semantics (e.g., returns a reasonable type).

For example, in the following code, `-a` will compile only if `MyInt` exposes such an operation as well:

```cpp
quantity a = MyInt{42} * m;
quantity b = -a;
```

Assuming that:

- `q` is our quantity,
- `qq` is a quantity implicitly convertible to `q`,
- `q2` is any other quantity,
- `kind` is a quantity of the same kind as `q`,
- `one` is a quantity of `dimension_one` with the unit `one`,
- `number` is a value of a type “compatible” with `q`’s representation type,

here is the list of all the supported operators:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Unary</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Compound assignment</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Binary</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Ordering &amp; comparison</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp"><span class="op">+</span>q</code><br/><code class="sourceCode cpp"><span class="op">-</span>q</code><br/><code class="sourceCode cpp"><span class="op">++</span>q</code><br/><code class="sourceCode cpp">q<span class="op">++</span></code><br/><code class="sourceCode cpp"><span class="op">--</span>q</code><br/><code class="sourceCode cpp">q<span class="op">--</span></code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">+=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">-=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">%=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">*=</span> number</code><br/><code class="sourceCode cpp">q <span class="op">*=</span> one</code><br/><code class="sourceCode cpp">q <span class="op">/=</span> number</code><br/><code class="sourceCode cpp">q <span class="op">/=</span> one</code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">+</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">-</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">%</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">*</span> q2</code><br/><code class="sourceCode cpp">q <span class="op">*</span> number</code><br/><code class="sourceCode cpp">number <span class="op">*</span> q</code><br/><code class="sourceCode cpp">q <span class="op">/</span> q2</code><br/><code class="sourceCode cpp">q <span class="op">/</span> number</code><br/><code class="sourceCode cpp">number <span class="op">/</span> q</code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">==</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">&lt;=&gt;</span> kind</code></td>
</tr>
</table>

As we can see, there are plenty of operations one can do on a value of a `quantity` type. As most of them are obvious, in the following chapters, we will discuss only the most important or non-trivial aspects of quantity arithmetics.

##### 20.12.4.2 Addition and subtraction

Quantities can easily be added or subtracted from each other:

```cpp
static_assert(1 * m + 1 * m == 2 * m);
static_assert(2 * m - 1 * m == 1 * m);
static_assert(isq::height(1 * m) + isq::height(1 * m) == isq::height(2 * m));
static_assert(isq::height(2 * m) - isq::height(1 * m) == isq::height(1 * m));
```

The above uses the same types for LHS, RHS, and the result, but in general, we can add, subtract, or compare the values of any quantity type as long as both quantities are of the same kind. The result of addition and subtraction will be the common type of the arguments:

```cpp
static_assert(1 * km + 1.5 * m == 1001.5 * m);
static_assert(isq::height(1 * m) + isq::width(1 * m) == isq::length(2 * m));
static_assert(isq::height(2 * m) - isq::distance(0.5 * m) == 1.5 * m);
static_assert(isq::radius(1 * m) - 0.5 * m == isq::radius(0.5 * m));
```

Please note that for the compound assignment operators, we always need to end up with the left-hand-side argument type:

```cpp
static_assert((1 * m += 1 * km) == 1001 * m);
static_assert((isq::length(1 * m) += isq::height(1 * m)) == isq::length(1 * m));
static_assert((isq::height(1.5 * m) -= 1 * m) == isq::height(0.5 * m));
```

If we break those rules, the code will not compile:

```cpp
quantity q1 = 1 * m -= 0.5 * m;                         // Compile-time error (1)
quantity q2 = 1 * km += 1 * m;                          // Compile-time error (2)
quantity q3 = isq::height(1 * m) += isq::length(1 * m); // Compile-time error (3)
```

`(1)` Convertions of the floating-point to integral representation type is considered narrowing.

`(2)` Conversion of quantity with integral representation type from a unit of a higher resolution to the one with a lower resolution is considered narrowing.

`(3)` Conversion from a more generic quantity type to a more specific one is considered unsafe.

Please note that all the above operations either preserved the input representation types or returned a common type if those were different for both arguments. This is not the case for irrational conversion factors. In such cases, the library will force the user to use at least one floating-point representation type to prevent truncation:

```cpp
template<typename... Ts>
consteval bool invalid_arithmetic(Ts... ts)
{
  return !requires { (... + ts); } && !requires { (... - ts); };
}

static_assert(invalid_arithmetic(1 * rad, 1 * deg));
static_assert(is_of_type<1. * rad + 1 * deg, quantity<deg, double>>);
static_assert(is_of_type<1 * rad + 1. * deg, quantity<deg, double>>);
static_assert(is_of_type<1. * rad + 1. * deg, quantity<deg, double>>);
```

##### 20.12.4.3 Multiplication and division

Multiplying or dividing a quantity by a number does not change its quantity type or unit. However, its representation type may change. For example:

```cpp
static_assert(isq::height(3 * m) * 0.5 == isq::height(1.5 * m));
```

Unless we use a compound assignment operator, in which case we always have to result with the type of the left-hand-side argument. This, together with the fact that this library tries to prevent truncation of a quantity value means, that the following does not compile:

```cpp
quantity q = isq::height(3 * m) *= 0.5; // Compile-time error
```

However, suppose we multiply or divide quantities of the same or different types, or we divide a raw number by a quantity. In that case, we most probably will end up in a quantity of yet another type:

```cpp
static_assert(120 * km / (2 * h) == 60 * km / h);
static_assert(isq::width(2 * m) * isq::length(2 * m) == isq::area(4 * m2));
static_assert(50 / isq::time(1 * s) == isq::frequency(50 * Hz));
```

An exception from the above rule happens when one of the arguments is a dimensionless quantity. If we multiply or divide by such a quantity, the quantity type will not change. If such a quantity has a unit `one`, also the unit of a quantity will not change:

```cpp
static_assert(120 * m / (2 * one) == 60 * m);
```

An interesting special case happens when we divide the same quantity kinds or multiply a quantity by its inverted type. In such a case, we end up with a dimensionless quantity.

```cpp
static_assert(isq::height(4 * m) / isq::width(2 * m) == 2 * one); // (1)
static_assert(5 * h / (120 * min) == 0 * one);                    // (2)
static_assert(5. * h / (120 * min) == 2.5 * one);
```

`(1)` The resulting quantity type of the LHS is `isq::height / isq::width`, which is a quantity of the dimensionless kind.

`(2)` The resulting quantity of the LHS is `0 * dimensionless[h / min]`. To be consistent with the division of different quantity types, we do not convert quantity values to a common unit before the division.

###### 20.12.4.3.1 Beware of integral division

The physical units library can’t do any runtime branching logic for the division operator. All logic has to be done at compile-time when the actual values are not known, and the quantity types can’t change at runtime.

If we expect `120 * km / (2 * h)` to return `60 km/h`, we have to agree with the fact that `5 * km / (24 * h)` returns `0 km/h`. We can’t do a range check at runtime to dynamically adjust scales and types based on the values of provided function arguments.

This is why we often prefer floating-point representation types when dealing with units. Some popular physical units libraries even [forbid integer division at all](https://aurora-opensource.github.io/au/main/troubleshooting/#integer-division-forbidden).

##### 20.12.4.4 Modulo

Now that we know how addition, subtraction, multiplication, and division work, it is time to talk about modulo. What would we expect to be returned from the following quantity equation?

```cpp
auto q = 5 * h % (120 * min);
```

Most of us would probably expect to see `1 h` or `60 min` as a result. And this is where the problems start.

The C++ language defines its `/` and `%` operators with the [quotient-remainder theorem](https://eel.is/c++draft/expr.mul#4):

```
q = a / b;
r = a % b;
q * b + r == a;
```

The important property of the modulo operator is that it only works for integral representation types (it is undefined what modulo for floating-point types means). However, as we saw in the previous chapter, integral types are tricky because they often truncate the value.

From the quotient-remainder theorem, the result of modulo operation is `r = a - q * b`. Let’s see what we get from such a quantity equation on integral representation types:

```cpp
quantity a = 5 * h;
quantity b = 120 * min;
quantity q = a / b;
quantity r = a - q * b;

std::cout << "reminder: " << r << "\n";
```

The above code outputs:

```
reminder: 5 h
```

And now, a tough question needs an answer. Do we really want modulo operator on physical units to be consistent with the quotient-remainder theorem and return `5 h` for `5 * h % (120 * min)`?

This is exactly why we decided not to follow this hugely surprising path in this library. The selected approach was also consistent with the feedback from C++ experts. For example, this is what Richard Smith said about this issue:

> I think the quotient-remainder property is a less important motivation here than other factors – the constraints on `%` and `/` are quite different, so they lack the inherent connection they have for integers. In particular, I would expect that `A / B` works for all quantities `A` and `B`, whereas `A % B` is only meaningful when `A` and `B` have the same dimension. It seems like a nice-to-have for the property to apply in the case where both `/` and `%` are defined, but internal consistency of `/` across all cases seems much more important to me.
> 
> I would expect `61 min % 1 h` to be `1 min`, and `1 h % 59 min` to also be `1 min`, so my intuition tells me that the result type of `A % B`, where `A` and `B` have the same dimension, should have the smaller unit of `A` and `B` (and if the smaller one doesn’t divide the larger one, we should either use the `gcd / std::common_type` of the units of `A` and `B` or perhaps just produce an error). I think any other behavior for `%` is hard to defend.
> 
> On the other hand, for division it seems to me that the choice of unit should probably not affect the result, and so if we want that `5 mm / 120 min = 0 mm/min`, then `5 h / 120 min == 0 hc` (where `hc` is a dimensionless “hexaconta”, or `60x`, unit). I don’t like the idea of taking SI base units into account; that seems arbitrary and like it would do the wrong thing as often as it does the right thing, especially when the units have a multiplier that is very large or small. We could special-case the situation of a dimensionless quantity, but that could lead to problematic overflow pretty easily: a calculation such as `10 s * 5 GHz * 2 uW` would overflow an `int` if it produces a dimensionless quantity for `10 s * 5 GHz`, but it could equally produce `50 G * 2 uW = 100 kW` without any overflow, and presumably would if the terms were merely reordered.
> 
> If people want to use integer-valued quantities, I think it’s fundamental that you need to know what the units of the result of an operation will be, and take that into account in how you express computations; the simplest rule for heterogeneous operators like `*` or `/` seems to be that the units of the result are determined by applying the operator to the units of the operands – and for homogeneous operators like `+` or `%`, it seems like the only reasonable option is that you get the `std::common_type` of the units of the operands.

To summarize, the modulo operator on physical units has more in common with addition and division operators than with the quotient-remainder theorem. To avoid surprising results, the operation uses a common unit to do the calculation and provide its result:

```cpp
static_assert(5 * h / (120 * min) == 0 * one);
static_assert(5 * h % (120 * min) == 60 * min);
static_assert(61 * min % (1 * h) == 1 * min);
static_assert(1 * h % (59 * min) == 1 * min);
```

##### 20.12.4.5 Comparison against zero

Zero is special. It is the only number that unambiguously defines the value of any kind of quantity, regardless of its units: zero inches and zero meters and zero miles are all identical. For this reason, it’s very common to compare the value of a quantity against zero. For example, when checking the sign of a quantity, or when making sure that it’s nonzero.

We could implement such checks in the following way:

```cpp
if(q1 / q2 != 0 * m / s)
  // ...
```

The above would work (assuming we are dealing with the quantity of *speed*), but it’s not ideal. If the result of `q1 / q2` is not expressed in `m / s`, we’ll incur an extra unit conversion. Even if it is in `m / s`, it’s cumbersome to repeat the unit in a context where it makes no difference.

We could avoid repeating the unit, and guarantee there won’t be an extra conversion, by writing:

```cpp
if(auto q = q1 / q2; q != q.zero())
  // ...
```

But that is a bit inconvenient, and inexperienced users could be unaware of this technique and its rationale.

For the above reasons, the library provides special support for comparisons against the literal `0`. Only this one value has elevated privileges and does not have to state the unit — the numerical value zero is common to all scaled units of any kind.

Thanks to that, to save typing and not pay for unneeded conversions, our check could be implemented as follows:

```cpp
if (q1 / q2 != 0)
  // ...
```

All six comparison operators support comparison against zero without specifying a unit. This works with any representation type `rep` for which `representation_values<rep>::zero()` is provided.

Only a compile-time zero is accepted: an integer or floating-point literal that is zero (e.g., `0`, `0.`, `0.f`, `0LL`). Passing another literal or a runtime variable — even one whose value happens to be zero — is rejected at compile time.

##### 20.12.4.6 Other maths

This chapter scoped only on the `quantity` type’s operators. However, there are many named math functions provided in the [[mp-units]](https://mpusz.github.io/mp-units) library. Among others, we can find there the following:

- `pow()`, `sqrt()`, `cbrt()`,
- `exp()`,
- `abs()`,
- `epsilon()`,
- `fma()`, `fmod()`, `remainder()`,
- `isfinite()`, `isinf()`, `isnan()`,
- `floor()`, `ceil()`, `round()`,
- `inverse()`,
- `hypot()`,
- `sin()`, `cos()`, `tan()`,
- `asin()`, `acos()`, `atan()`, `atan2()`.

In the library, we can also find the `<mp-units/random.h>` header file with all the pseudo-random number generators.

We plan to provide a separate paper on those in the future.

#### 20.12.5 Dimensionless quantities

The quantities we discussed so far always had some specific type and physical dimension. However, this is not always the case. While performing various computations, we sometimes end up with so-called “dimensionless” quantities, which [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) correctly defines as quantities of dimension one:

> - Quantity for which all the exponents of the factors corresponding to the base quantities in its quantity dimension are zero.
> - The measurement units and values of quantities of dimension one are numbers, but such quantities convey more information than a number.
> - Some quantities of dimension one are defined as the ratios of two quantities of the same kind.
> - Numbers of entities are quantities of dimension one.

##### 20.12.5.1 Dividing two quantities of the same kind

Dividing two quantities of the same kind always results in a quantity of dimension one. However, depending on what type of quantities we divide or what their units are, we may end up with slightly different types.

Dividing two quantities of the same dimension always results in a quantity with the dimension being `dimension_one`. This is often different for other physical units libraries, which may return a raw representation type for such cases. A raw value is also always returned from the division of two `std::chrono::duration` values.

In the initial design of the [[mp-units]](https://mpusz.github.io/mp-units) library, the resulting type of division of two quantities was their common representation type (just like `std::chrono::duration`):

```cpp
static_assert(std::is_same_v<decltype(10 * km / (5 * km)), int>);
```

The reasoning behind it was not providing a false impression of a strong `quantity` type for something that looks and feels like a regular number. Also, all of the mathematic and trigonometric functions were working fine out of the box with such representation types, so we did not have to rewrite `sin()`, `cos()`, `exp()`, and others.

However, the feedback we got from the production usage was that such an approach is really bad for generic programming. It is hard to handle the result of the two quantities’ division (or multiplication) as it might be either a quantity or a fundamental type. If we want to raise such a result to some power, we must use `units::pow` or `std::pow` depending on the resulting type (`units::pow` takes the power as template arguments). Those are only a few issues related to such an approach.

Moreover, suppose we divide quantities of the same dimension, but with units of significantly different magnitudes. In such case, we may end up with a really small or a huge floating-point value, which may result in losing lots of precision. Returning a dimensionless quantity from such cases allows us to benefit from all the properties of scaled units and is consistent with the rest of the library.

###### 20.12.5.1.1 Dividing quantities of the same type

First, let’s analyze what happens if we divide two quantities of the same type:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::height(200 * m) / isq::height(50 * m);
```

In such a case, we end up with a dimensionless quantity that has the following properties:

```cpp
static_assert(q.quantity_spec == dimensionless);
static_assert(q.dimension == dimension_one);
static_assert(q.unit == one);
```

In case we would like to print its value, we would see a raw value of `4` in the output with no unit being printed.

###### 20.12.5.1.2 Dividing quantities of different types

We can divide quantities of the same dimension and unit but of different quantity types:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::work(200 * J) / isq::heat(50 * J);
```

Again we end up with `dimension_one` and `one`, but this time:

```cpp
static_assert(q.quantity_spec == isq::work / isq::heat);
```

As shown above, the result is not of a `dimensionless` type anymore. Instead, we get a quantity type derived from the performed quantity equation. According to the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html), *work* divided by *heat* is the recipe for the *thermodynamic efficiency* quantity, thus:

```cpp
static_assert(implicitly_convertible(q.quantity_spec, isq::efficiency_thermodynamics));
```

Please note that the quantity of `isq::efficiency_thermodynamics` is of a kind `dimensionless`, so it is implicitly convertible to `dimensionless` and satisfies the `QuantityOf<dimensionless>` concept.

###### 20.12.5.1.3 Dividing quantities of different units

Now, let’s see what happens when we divide two quantities of the same type but different units:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::height(4 * km) / isq::height(2 * m);
```

This time we get a quantity of `dimensionless` type with a `dimension_one` as its dimension. However, the resulting unit is not `one` anymore:

```cpp
static_assert(q.unit == mag_power<10, 3> * one);
```

In case we would print the text output of this quantity, we would not see a raw value of `2000`, but `2 km/m`.

First, it may look surprising, but this is actually consistent with the division of quantities of different dimensions. For example, if we divide `4 * km / (2 * s)`, we do not expect `km` to be “expanded” to `m` before the division, right? We would expect the result of `2 * (km / s)`, which is exactly what we get when we divide quantities of the same kind.

This is a compelling feature that allows us to express huge or tiny ratios without the need for big and expensive representation types. With this, we can easily define things like a [Hubble’s constant](https://en.wikipedia.org/wiki/Hubble%27s_law#Dimensionless_Hubble_constant) that uses a unit that is proportional to the ratio of kilometers per megaparsecs, which are both units of length:

```cpp
inline constexpr struct hubble_constant :
    named_constant<{u8"H₀", "H_0"}, mag_ratio<701, 10> * si::kilo<si::metre> / si::second / si::mega<parsec>> {
} hubble_constant;
```

##### 20.12.5.2 Counts of things

Another important use case for dimensionless quantities is to provide strong types for counts of things. For example:

- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 3) provides a *rotation* quantity defined as the number of revolutions,
- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 6) provides a *number of turns in a winding* quantity,
- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) provides a *Hamming distance* quantity defined as the number of digit positions in which the corresponding digits of two words of the same length are different.

Thanks to assigning strong names to such quantities, they can be used in the quantity equation of other quantities. For example, *rotational frequency* is defined by `rotation / duration`.

##### 20.12.5.3 Predefined units of the dimensionless quantity

As we observed above, the most common unit for dimensionless quantities is `one`. It has the ratio of `1` and does not output any textual symbol.

A unit `one` is special in the entire type system of units as it is considered to be an identity operand in the unit symbolic expressions. This means that, for example:

```cpp
static_assert(one * one == one);
static_assert(one * si::metre == si::metre);
static_assert(si::metre / si::metre == one);
```

The same is also true for `dimension_one` and `dimensionless` in the domains of dimensions and quantity specifications, respectively.

Besides the unit `one`, there are a few other scaled units predefined in the library for usage with dimensionless quantities:

```cpp
inline constexpr struct percent : named_unit<"%", mag_ratio<1, 100> * one> {} percent;
inline constexpr struct per_mille : named_unit<{u8"‰", "%o"}, mag_ratio<1, 1000> * one> {} per_mille;
inline constexpr struct parts_per_million : named_unit<"ppm", mag_ratio<1, 1'000'000> * one> {} parts_per_million;
inline constexpr auto ppm = parts_per_million;

inline constexpr struct pi : named_constant<symbol_text{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, mag<pi_c> * one> {} pi;
inline constexpr auto π /* U+03C0 GREEK SMALL LETTER PI */ = pi;
```

###### 20.12.5.3.1 Superpowers of the unit `one`

Quantities implicitly convertible to `dimensionless` with the unit equivalent to `one` are the only ones that are:

- implicitly constructible from the raw value,
- explicitly convertible to a raw value,
- comparable to a raw value.

```cpp
quantity<one> inc(quantity<one> q) { return q + 1; }
void legacy(double) { /* ... */ }

if (auto q = inc(42); q != 0)
  legacy(static_cast<int>(q));
```

This property also expands to usual arithmetic operators.

Please note that those rules do not apply to all the dimensionless quantities. It would be unsafe and misleading to allow such operations on units with a magnitude different than `1` (e.g., `percent`) or for quantities that are not implicitly convertible to `dimensionless` (e.g., `angular_measure`).

##### 20.12.5.4 Angular quantities

Special, often controversial, examples of dimensionless quantities are the *angular measure* and *solid angular measure* quantities that are defined in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 3) to be the result of a division of `arc_length / radius` and `area / pow<2>(radius)` respectively. Moreover, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) also explicitly states that both can be expressed in the unit `one`. This means that both `isq::angular_measure` and `isq::solid_angular_measure` should be of a kind of `dimensionless`.

On the other hand, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) also specifies that the unit `radian` can be used for *angular measure*, and the unit `steradian` can be used for *solid angular measure*. Those should not be mixed or used to express other types of dimensionless quantities. We should not be able to measure:

- basic dimensionless quantity in radians or steradians,
- *angular measure* in steradians,
- *solid angular measure* in radians.

This means that both `isq::angular_measure` and `isq::solid_angular_measure` should also be quantity kinds by themselves.

*Note: Many people claim that angle being a dimensionless quantity is a bad idea. There are proposals submitted to make an angle a base quantity and `rad` to become a base unit in both [[SI]](https://www.bipm.org/en/publications/si-brochure) and [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html).*

###### 20.12.5.4.1 Radians and degrees support

Thanks to the usage of magnitudes the library provides efficient strong types for all angular types. This means that with the built-in support for magnitudes of \(\pi\) we can provide accurate conversions between radians and degrees. The library also provides common trigonometric functions for angular quantities:

```cpp
quantity speed = 110 * km / h;
quantity rate_of_climb = -0.63657 * m / s;
quantity glide_ratio = speed / -rate_of_climb;
quantity glide_angle = angular::asin(1 / glide_ratio);

std::println("Glide ratio: {::N[.1f]}", glide_ratio.in(one));
std::println("Glide angle:");
std::println(" - {::N[.4f]}", glide_angle);
std::println(" - {::N[.2f]}", glide_angle.in(angular::degree));
std::println(" - {::N[.2f]}", glide_angle.in(angular::gradian));
```

The above program prints:

```
Glide ratio: 48.0
Glide angle:
 - 0.0208 rad
 - 1.19°
 - 1.33ᵍ
```

##### 20.12.5.5 Nested quantity kinds

Angular quantities are not the only ones with such a “strange” behavior. A similar case is the *storage capacity* quantity specified in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) that again allows expressing it in both `one` and `bit` units.

Those cases make dimensionless quantities an exceptional tree in the library. This quantity hierarchy contains more than one quantity kind and more than one unit in its tree:

![](data:image/svg+xml;base64,PHN2ZyBpZD0ibXktc3ZnIiB3aWR0aD0iMTAwJSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgY2xhc3M9ImZsb3djaGFydCIgc3R5bGU9Im1heC13aWR0aDogMjEwMy4xcHg7IGJhY2tncm91bmQtY29sb3I6IHRyYW5zcGFyZW50OyIgdmlld0JveD0iMCAwIDIxMDMuMDk3NjU2MjUgNDAxIiByb2xlPSJncmFwaGljcy1kb2N1bWVudCBkb2N1bWVudCIgYXJpYS1yb2xlZGVzY3JpcHRpb249ImZsb3djaGFydC12MiI+PHN0eWxlPiNteS1zdmd7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O2ZpbGw6IzMzMzt9QGtleWZyYW1lcyBlZGdlLWFuaW1hdGlvbi1mcmFtZXtmcm9te3N0cm9rZS1kYXNob2Zmc2V0OjA7fX1Aa2V5ZnJhbWVzIGRhc2h7dG97c3Ryb2tlLWRhc2hvZmZzZXQ6MDt9fSNteS1zdmcgLmVkZ2UtYW5pbWF0aW9uLXNsb3d7c3Ryb2tlLWRhc2hhcnJheTo5LDUhaW1wb3J0YW50O3N0cm9rZS1kYXNob2Zmc2V0OjkwMDthbmltYXRpb246ZGFzaCA1MHMgbGluZWFyIGluZmluaXRlO3N0cm9rZS1saW5lY2FwOnJvdW5kO30jbXktc3ZnIC5lZGdlLWFuaW1hdGlvbi1mYXN0e3N0cm9rZS1kYXNoYXJyYXk6OSw1IWltcG9ydGFudDtzdHJva2UtZGFzaG9mZnNldDo5MDA7YW5pbWF0aW9uOmRhc2ggMjBzIGxpbmVhciBpbmZpbml0ZTtzdHJva2UtbGluZWNhcDpyb3VuZDt9I215LXN2ZyAuZXJyb3ItaWNvbntmaWxsOiM1NTIyMjI7fSNteS1zdmcgLmVycm9yLXRleHR7ZmlsbDojNTUyMjIyO3N0cm9rZTojNTUyMjIyO30jbXktc3ZnIC5lZGdlLXRoaWNrbmVzcy1ub3JtYWx7c3Ryb2tlLXdpZHRoOjFweDt9I215LXN2ZyAuZWRnZS10aGlja25lc3MtdGhpY2t7c3Ryb2tlLXdpZHRoOjMuNXB4O30jbXktc3ZnIC5lZGdlLXBhdHRlcm4tc29saWR7c3Ryb2tlLWRhc2hhcnJheTowO30jbXktc3ZnIC5lZGdlLXRoaWNrbmVzcy1pbnZpc2libGV7c3Ryb2tlLXdpZHRoOjA7ZmlsbDpub25lO30jbXktc3ZnIC5lZGdlLXBhdHRlcm4tZGFzaGVke3N0cm9rZS1kYXNoYXJyYXk6Mzt9I215LXN2ZyAuZWRnZS1wYXR0ZXJuLWRvdHRlZHtzdHJva2UtZGFzaGFycmF5OjI7fSNteS1zdmcgLm1hcmtlcntmaWxsOiMzMzMzMzM7c3Ryb2tlOiMzMzMzMzM7fSNteS1zdmcgLm1hcmtlci5jcm9zc3tzdHJva2U6IzMzMzMzMzt9I215LXN2ZyBzdmd7Zm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO2ZvbnQtc2l6ZToxNnB4O30jbXktc3ZnIHB7bWFyZ2luOjA7fSNteS1zdmcgLmxhYmVse2ZvbnQtZmFtaWx5OiJ0cmVidWNoZXQgbXMiLHZlcmRhbmEsYXJpYWwsc2Fucy1zZXJpZjtjb2xvcjojMzMzO30jbXktc3ZnIC5jbHVzdGVyLWxhYmVsIHRleHR7ZmlsbDojMzMzO30jbXktc3ZnIC5jbHVzdGVyLWxhYmVsIHNwYW57Y29sb3I6IzMzMzt9I215LXN2ZyAuY2x1c3Rlci1sYWJlbCBzcGFuIHB7YmFja2dyb3VuZC1jb2xvcjp0cmFuc3BhcmVudDt9I215LXN2ZyAubGFiZWwgdGV4dCwjbXktc3ZnIHNwYW57ZmlsbDojMzMzO2NvbG9yOiMzMzM7fSNteS1zdmcgLm5vZGUgcmVjdCwjbXktc3ZnIC5ub2RlIGNpcmNsZSwjbXktc3ZnIC5ub2RlIGVsbGlwc2UsI215LXN2ZyAubm9kZSBwb2x5Z29uLCNteS1zdmcgLm5vZGUgcGF0aHtmaWxsOiNFQ0VDRkY7c3Ryb2tlOiM5MzcwREI7c3Ryb2tlLXdpZHRoOjFweDt9I215LXN2ZyAucm91Z2gtbm9kZSAubGFiZWwgdGV4dCwjbXktc3ZnIC5ub2RlIC5sYWJlbCB0ZXh0LCNteS1zdmcgLmltYWdlLXNoYXBlIC5sYWJlbCwjbXktc3ZnIC5pY29uLXNoYXBlIC5sYWJlbHt0ZXh0LWFuY2hvcjptaWRkbGU7fSNteS1zdmcgLm5vZGUgLmthdGV4IHBhdGh7ZmlsbDojMDAwO3N0cm9rZTojMDAwO3N0cm9rZS13aWR0aDoxcHg7fSNteS1zdmcgLnJvdWdoLW5vZGUgLmxhYmVsLCNteS1zdmcgLm5vZGUgLmxhYmVsLCNteS1zdmcgLmltYWdlLXNoYXBlIC5sYWJlbCwjbXktc3ZnIC5pY29uLXNoYXBlIC5sYWJlbHt0ZXh0LWFsaWduOmNlbnRlcjt9I215LXN2ZyAubm9kZS5jbGlja2FibGV7Y3Vyc29yOnBvaW50ZXI7fSNteS1zdmcgLnJvb3QgLmFuY2hvciBwYXRoe2ZpbGw6IzMzMzMzMyFpbXBvcnRhbnQ7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlOiMzMzMzMzM7fSNteS1zdmcgLmFycm93aGVhZFBhdGh7ZmlsbDojMzMzMzMzO30jbXktc3ZnIC5lZGdlUGF0aCAucGF0aHtzdHJva2U6IzMzMzMzMztzdHJva2Utd2lkdGg6MXB4O30jbXktc3ZnIC5mbG93Y2hhcnQtbGlua3tzdHJva2U6IzMzMzMzMztmaWxsOm5vbmU7fSNteS1zdmcgLmVkZ2VMYWJlbHtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7dGV4dC1hbGlnbjpjZW50ZXI7fSNteS1zdmcgLmVkZ2VMYWJlbCBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I215LXN2ZyAuZWRnZUxhYmVsIHJlY3R7b3BhY2l0eTowLjU7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO2ZpbGw6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTt9I215LXN2ZyAubGFiZWxCa2d7YmFja2dyb3VuZC1jb2xvcjpyZ2JhKDIzMiwgMjMyLCAyMzIsIDAuNSk7fSNteS1zdmcgLmNsdXN0ZXIgcmVjdHtmaWxsOiNmZmZmZGU7c3Ryb2tlOiNhYWFhMzM7c3Ryb2tlLXdpZHRoOjFweDt9I215LXN2ZyAuY2x1c3RlciB0ZXh0e2ZpbGw6IzMzMzt9I215LXN2ZyAuY2x1c3RlciBzcGFue2NvbG9yOiMzMzM7fSNteS1zdmcgZGl2Lm1lcm1haWRUb29sdGlwe3Bvc2l0aW9uOmFic29sdXRlO3RleHQtYWxpZ246Y2VudGVyO21heC13aWR0aDoyMDBweDtwYWRkaW5nOjJweDtmb250LWZhbWlseToidHJlYnVjaGV0IG1zIix2ZXJkYW5hLGFyaWFsLHNhbnMtc2VyaWY7Zm9udC1zaXplOjEycHg7YmFja2dyb3VuZDpoc2woODAsIDEwMCUsIDk2LjI3NDUwOTgwMzklKTtib3JkZXI6MXB4IHNvbGlkICNhYWFhMzM7Ym9yZGVyLXJhZGl1czoycHg7cG9pbnRlci1ldmVudHM6bm9uZTt6LWluZGV4OjEwMDt9I215LXN2ZyAuZmxvd2NoYXJ0VGl0bGVUZXh0e3RleHQtYW5jaG9yOm1pZGRsZTtmb250LXNpemU6MThweDtmaWxsOiMzMzM7fSNteS1zdmcgcmVjdC50ZXh0e2ZpbGw6bm9uZTtzdHJva2Utd2lkdGg6MDt9I215LXN2ZyAuaWNvbi1zaGFwZSwjbXktc3ZnIC5pbWFnZS1zaGFwZXtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7dGV4dC1hbGlnbjpjZW50ZXI7fSNteS1zdmcgLmljb24tc2hhcGUgcCwjbXktc3ZnIC5pbWFnZS1zaGFwZSBwe2JhY2tncm91bmQtY29sb3I6cmdiYSgyMzIsMjMyLDIzMiwgMC44KTtwYWRkaW5nOjJweDt9I215LXN2ZyAuaWNvbi1zaGFwZSAubGFiZWwgcmVjdCwjbXktc3ZnIC5pbWFnZS1zaGFwZSAubGFiZWwgcmVjdHtvcGFjaXR5OjAuNTtiYWNrZ3JvdW5kLWNvbG9yOnJnYmEoMjMyLDIzMiwyMzIsIDAuOCk7ZmlsbDpyZ2JhKDIzMiwyMzIsMjMyLCAwLjgpO30jbXktc3ZnIC5sYWJlbC1pY29ue2Rpc3BsYXk6aW5saW5lLWJsb2NrO2hlaWdodDoxZW07b3ZlcmZsb3c6dmlzaWJsZTt2ZXJ0aWNhbC1hbGlnbjotMC4xMjVlbTt9I215LXN2ZyAubm9kZSAubGFiZWwtaWNvbiBwYXRoe2ZpbGw6Y3VycmVudENvbG9yO3N0cm9rZTpyZXZlcnQ7c3Ryb2tlLXdpZHRoOnJldmVydDt9I215LXN2ZyAubm9kZSAubmVvLW5vZGV7c3Ryb2tlOiM5MzcwREI7fSNteS1zdmcgW2RhdGEtbG9vaz0ibmVvIl0ubm9kZSByZWN0LCNteS1zdmcgW2RhdGEtbG9vaz0ibmVvIl0uY2x1c3RlciByZWN0LCNteS1zdmcgW2RhdGEtbG9vaz0ibmVvIl0ubm9kZSBwb2x5Z29ue3N0cm9rZTojOTM3MERCO2ZpbHRlcjpkcm9wLXNoYWRvdygxcHggMnB4IDJweCByZ2JhKDE4NSwgMTg1LCAxODUsIDEpKTt9I215LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIHBhdGh7c3Ryb2tlOiM5MzcwREI7c3Ryb2tlLXdpZHRoOjFweDt9I215LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIC5vdXRlci1wYXRoe2ZpbHRlcjpkcm9wLXNoYWRvdygxcHggMnB4IDJweCByZ2JhKDE4NSwgMTg1LCAxODUsIDEpKTt9I215LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIC5uZW8tbGluZSBwYXRoe3N0cm9rZTojOTM3MERCO2ZpbHRlcjpub25lO30jbXktc3ZnIFtkYXRhLWxvb2s9Im5lbyJdLm5vZGUgY2lyY2xle3N0cm9rZTojOTM3MERCO2ZpbHRlcjpkcm9wLXNoYWRvdygxcHggMnB4IDJweCByZ2JhKDE4NSwgMTg1LCAxODUsIDEpKTt9I215LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5ub2RlIGNpcmNsZSAuc3RhdGUtc3RhcnR7ZmlsbDojMDAwMDAwO30jbXktc3ZnIFtkYXRhLWxvb2s9Im5lbyJdLmljb24tc2hhcGUgLmljb257ZmlsbDojOTM3MERCO2ZpbHRlcjpkcm9wLXNoYWRvdygxcHggMnB4IDJweCByZ2JhKDE4NSwgMTg1LCAxODUsIDEpKTt9I215LXN2ZyBbZGF0YS1sb29rPSJuZW8iXS5pY29uLXNoYXBlIC5pY29uLW5lbyBwYXRoe3N0cm9rZTojOTM3MERCO2ZpbHRlcjpkcm9wLXNoYWRvdygxcHggMnB4IDJweCByZ2JhKDE4NSwgMTg1LCAxODUsIDEpKTt9I215LXN2ZyA6cm9vdHstLW1lcm1haWQtZm9udC1mYW1pbHk6InRyZWJ1Y2hldCBtcyIsdmVyZGFuYSxhcmlhbCxzYW5zLXNlcmlmO308L3N0eWxlPjxnPjxtYXJrZXIgaWQ9Im15LXN2Z19mbG93Y2hhcnQtdjItcG9pbnRFbmQiIGNsYXNzPSJtYXJrZXIgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTAgMTAiIHJlZlg9IjUiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iOCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDAgMCBMIDEwIDUgTCAwIDEwIHoiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1wb2ludFN0YXJ0IiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSI0LjUiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iOCIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDAgNSBMIDEwIDEwIEwgMTAgMCB6IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im15LXN2Z19mbG93Y2hhcnQtdjItcG9pbnRFbmQtbWFyZ2luIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDExLjUgMTQiIHJlZlg9IjExLjUiIHJlZlk9IjciIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjEwLjUiIG1hcmtlckhlaWdodD0iMTQiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAwIDAgTCAxMS41IDcgTCAwIDE0IHoiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDA7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1wb2ludFN0YXJ0LW1hcmdpbiIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMS41IDE0IiByZWZYPSIxIiByZWZZPSI3IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMS41IiBtYXJrZXJIZWlnaHQ9IjE0IiBvcmllbnQ9ImF1dG8iPjxwb2x5Z29uIHBvaW50cz0iMCw3IDExLjUsMTQgMTEuNSwwIiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAwOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im15LXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlRW5kIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSIxMSIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PGNpcmNsZSBjeD0iNSIgY3k9IjUiIHI9IjUiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDE7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1jaXJjbGVTdGFydCIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWD0iLTEiIHJlZlk9IjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxjaXJjbGUgY3g9IjUiIGN5PSI1IiByPSI1IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAxOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im15LXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlRW5kLW1hcmdpbiIgY2xhc3M9Im1hcmtlciBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMCAxMCIgcmVmWT0iNSIgcmVmWD0iMTIuMjUiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjE0IiBtYXJrZXJIZWlnaHQ9IjE0IiBvcmllbnQ9ImF1dG8iPjxjaXJjbGUgY3g9IjUiIGN5PSI1IiByPSI1IiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAwOyBzdHJva2UtZGFzaGFycmF5OiAxLCAwOyIvPjwvbWFya2VyPjxtYXJrZXIgaWQ9Im15LXN2Z19mbG93Y2hhcnQtdjItY2lyY2xlU3RhcnQtbWFyZ2luIiBjbGFzcz0ibWFya2VyIGZsb3djaGFydC12MiIgdmlld0JveD0iMCAwIDEwIDEwIiByZWZYPSItMiIgcmVmWT0iNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTQiIG1hcmtlckhlaWdodD0iMTQiIG9yaWVudD0iYXV0byI+PGNpcmNsZSBjeD0iNSIgY3k9IjUiIHI9IjUiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDA7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1jcm9zc0VuZCIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxMSAxMSIgcmVmWD0iMTIiIHJlZlk9IjUuMiIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTEiIG1hcmtlckhlaWdodD0iMTEiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAxLDEgbCA5LDkgTSAxMCwxIGwgLTksOSIgY2xhc3M9ImFycm93TWFya2VyUGF0aCIgc3R5bGU9InN0cm9rZS13aWR0aDogMjsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48bWFya2VyIGlkPSJteS1zdmdfZmxvd2NoYXJ0LXYyLWNyb3NzU3RhcnQiIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTEgMTEiIHJlZlg9Ii0xIiByZWZZPSI1LjIiIG1hcmtlclVuaXRzPSJ1c2VyU3BhY2VPblVzZSIgbWFya2VyV2lkdGg9IjExIiBtYXJrZXJIZWlnaHQ9IjExIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0gMSwxIGwgOSw5IE0gMTAsMSBsIC05LDkiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDI7IHN0cm9rZS1kYXNoYXJyYXk6IDEsIDA7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1jcm9zc0VuZC1tYXJnaW4iIGNsYXNzPSJtYXJrZXIgY3Jvc3MgZmxvd2NoYXJ0LXYyIiB2aWV3Qm94PSIwIDAgMTUgMTUiIHJlZlg9IjE3LjciIHJlZlk9IjcuNSIgbWFya2VyVW5pdHM9InVzZXJTcGFjZU9uVXNlIiBtYXJrZXJXaWR0aD0iMTIiIG1hcmtlckhlaWdodD0iMTIiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTSAxLDEgTCAxNCwxNCBNIDEsMTQgTCAxNCwxIiBjbGFzcz0iYXJyb3dNYXJrZXJQYXRoIiBzdHlsZT0ic3Ryb2tlLXdpZHRoOiAyLjU7Ii8+PC9tYXJrZXI+PG1hcmtlciBpZD0ibXktc3ZnX2Zsb3djaGFydC12Mi1jcm9zc1N0YXJ0LW1hcmdpbiIgY2xhc3M9Im1hcmtlciBjcm9zcyBmbG93Y2hhcnQtdjIiIHZpZXdCb3g9IjAgMCAxNSAxNSIgcmVmWD0iLTMuNSIgcmVmWT0iNy41IiBtYXJrZXJVbml0cz0idXNlclNwYWNlT25Vc2UiIG1hcmtlcldpZHRoPSIxMiIgbWFya2VySGVpZ2h0PSIxMiIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNIDEsMSBMIDE0LDE0IE0gMSwxNCBMIDE0LDEiIGNsYXNzPSJhcnJvd01hcmtlclBhdGgiIHN0eWxlPSJzdHJva2Utd2lkdGg6IDIuNTsgc3Ryb2tlLWRhc2hhcnJheTogMSwgMDsiLz48L21hcmtlcj48ZyBjbGFzcz0icm9vdCI+PGcgY2xhc3M9ImNsdXN0ZXJzIj48ZyBjbGFzcz0iY2x1c3RlciIgaWQ9Im15LXN2Zy1raW5kX3N0b3JhZ2UiIGRhdGEtbG9vaz0iY2xhc3NpYyI+PHJlY3Qgc3R5bGU9IiIgeD0iOCIgeT0iMTM2IiB3aWR0aD0iNDA1LjY4NzUiIGhlaWdodD0iMjU3Ii8+PGcgY2xhc3M9ImNsdXN0ZXItbGFiZWwiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIxMC44NDM3NSwgMTM2KSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImNsdXN0ZXIiIGlkPSJteS1zdmcta2luZF9zb2xpZF9hbmd1bGFyIiBkYXRhLWxvb2s9ImNsYXNzaWMiPjxyZWN0IHN0eWxlPSIiIHg9IjEyMzYuNDY4NzUiIHk9IjEzNiIgd2lkdGg9IjMwOC43NSIgaGVpZ2h0PSIxMjgiLz48ZyBjbGFzcz0iY2x1c3Rlci1sYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTM5MC44NDM3NSwgMTM2KSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImNsdXN0ZXIiIGlkPSJteS1zdmcta2luZF9hbmd1bGFyIiBkYXRhLWxvb2s9ImNsYXNzaWMiPjxyZWN0IHN0eWxlPSIiIHg9IjE1NjUuMjE4NzUiIHk9IjEzNiIgd2lkdGg9IjUyOS44Nzg5MDYyNSIgaGVpZ2h0PSIyNTciLz48ZyBjbGFzcz0iY2x1c3Rlci1sYWJlbCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTgzMC4xNTgyMDMxMjUsIDEzNikiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZVBhdGhzIj48cGF0aCBkPSJNOTE4LjUzMSw1OC4wNUw4NTAuMTg2LDY2Ljg3NUM3ODEuODQxLDc1LjcsNjQ1LjE1MSw5My4zNSw1NzYuODA2LDEwNi4zNDJDNTA4LjQ2MSwxMTkuMzMzLDUwOC40NjEsMTI3LjY2Nyw1MDguNDYxLDEzOEM1MDguNDYxLDE0OC4zMzMsNTA4LjQ2MSwxNjAuNjY3LDUwOC40NjEsMTY2LjgzM0w1MDguNDYxLDE3MyIgaWQ9Im15LXN2Zy1MX2RpbWVuc2lvbmxlc3Nfcm90YXRpb25fMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX3JvdGF0aW9uXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk9URTRMalV6TVRJMUxDSjVJam8xT0M0d05UQXhOekV3TVRrMk5UVTBOSDBzZXlKNElqbzFNRGd1TkRZd09UTTNOU3dpZVNJNk1URXhmU3g3SW5naU9qVXdPQzQwTmpBNU16YzFMQ0o1SWpveE16WjlMSHNpZUNJNk5UQTRMalEyTURrek56VXNJbmtpT2pFM00zMWQiIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjxwYXRoIGQ9Ik05MTguNTMxLDY4LjQ4M0w4OTAuMzAzLDc1LjU2OUM4NjIuMDc2LDgyLjY1NSw4MDUuNjIsOTYuODI4LDc3Ny4zOTIsMTA4LjA4MUM3NDkuMTY0LDExOS4zMzMsNzQ5LjE2NCwxMjcuNjY3LDc0OS4xNjQsMTM4Qzc0OS4xNjQsMTQ4LjMzMyw3NDkuMTY0LDE2MC42NjcsNzQ5LjE2NCwxNjYuODMzTDc0OS4xNjQsMTczIiBpZD0ibXktc3ZnLUxfZGltZW5zaW9ubGVzc190aGVybW9keW5hbWljX2VmZmljaWVuY3lfMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX3RoZXJtb2R5bmFtaWNfZWZmaWNpZW5jeV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZPVEU0TGpVek1USTFMQ0o1SWpvMk9DNDBPRE13TXpnMk5ERTROalUxT1gwc2V5SjRJam8zTkRrdU1UWTBNRFl5TlN3aWVTSTZNVEV4ZlN4N0luZ2lPamMwT1M0eE5qUXdOakkxTENKNUlqb3hNelo5TEhzaWVDSTZOelE1TGpFMk5EQTJNalVzSW5raU9qRTNNMzFkIiBkYXRhLWxvb2s9ImNsYXNzaWMiLz48cGF0aCBkPSJNMTAwNC4xMDksODZMMTAwNC4xMDksOTAuMTY3QzEwMDQuMTA5LDk0LjMzMywxMDA0LjEwOSwxMDIuNjY3LDEwMDQuMTA5LDExMUMxMDA0LjEwOSwxMTkuMzMzLDEwMDQuMTA5LDEyNy42NjcsMTAwNC4xMDksMTM4QzEwMDQuMTA5LDE0OC4zMzMsMTAwNC4xMDksMTYwLjY2NywxMDA0LjEwOSwxNjYuODMzTDEwMDQuMTA5LDE3MyIgaWQ9Im15LXN2Zy1MX2RpbWVuc2lvbmxlc3NfZHJhZ19mYWN0b3JfMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX2RyYWdfZmFjdG9yXzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UQXdOQzR4TURrek56VXNJbmtpT2pnMmZTeDdJbmdpT2pFd01EUXVNVEE1TXpjMUxDSjVJam94TVRGOUxIc2llQ0k2TVRBd05DNHhNRGt6TnpVc0lua2lPakV6Tm4wc2V5SjRJam94TURBMExqRXdPVE0zTlN3aWVTSTZNVGN6ZlYwPSIgZGF0YS1sb29rPSJjbGFzc2ljIi8+PHBhdGggZD0iTTEwODkuNjg4LDgxLjA4NUwxMTAyLjIwNiw4Ni4wNzFDMTExNC43MjQsOTEuMDU3LDExMzkuNzYsMTAxLjAyOCwxMTUyLjI3OSwxMTAuMTgxQzExNjQuNzk3LDExOS4zMzMsMTE2NC43OTcsMTI3LjY2NywxMTY0Ljc5NywxMzhDMTE2NC43OTcsMTQ4LjMzMywxMTY0Ljc5NywxNjAuNjY3LDExNjQuNzk3LDE2Ni44MzNMMTE2NC43OTcsMTczIiBpZD0ibXktc3ZnLUxfZGltZW5zaW9ubGVzc18uLi5fMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzXy4uLl8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVEE0T1M0Mk9EYzFMQ0o1SWpvNE1TNHdPRFEzT1RFNU1EazNOakkzTkgwc2V5SjRJam94TVRZMExqYzVOamczTlN3aWVTSTZNVEV4ZlN4N0luZ2lPakV4TmpRdU56azJPRGMxTENKNUlqb3hNelo5TEhzaWVDSTZNVEUyTkM0M09UWTROelVzSW5raU9qRTNNMzFkIiBkYXRhLWxvb2s9ImNsYXNzaWMiLz48cGF0aCBkPSJNMTA4OS42ODgsNTMuNDk0TDEyMTUuOTg4LDYzLjA3OEMxMzQyLjI4OCw3Mi42NjMsMTU5NC44ODgsOTEuODMxLDE3MjEuMTg4LDEwNS41ODJDMTg0Ny40ODgsMTE5LjMzMywxODQ3LjQ4OCwxMjcuNjY3LDE4NDcuNDg4LDEzNkMxODQ3LjQ4OCwxNDQuMzMzLDE4NDcuNDg4LDE1Mi42NjcsMTg0Ny40ODgsMTU2LjgzM0wxODQ3LjQ4OCwxNjEiIGlkPSJteS1zdmctTF9kaW1lbnNpb25sZXNzX2FuZ3VsYXJfbWVhc3VyZV8wIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1kb3R0ZWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX2FuZ3VsYXJfbWVhc3VyZV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVEE0T1M0Mk9EYzFMQ0o1SWpvMU15NDBPVFF4TVRVME5qYzBOVEE1Tm4wc2V5SjRJam94T0RRM0xqUTRPREk0TVRJMUxDSjVJam94TVRGOUxIc2llQ0k2TVRnME55NDBPRGd5T0RFeU5Td2llU0k2TVRNMmZTeDdJbmdpT2pFNE5EY3VORGc0TWpneE1qVXNJbmtpT2pFMk1YMWQiIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjxwYXRoIGQ9Ik0xMDg5LjY4OCw2MS4xNjJMMTEzOS44OCw2OS40NjhDMTE5MC4wNzMsNzcuNzc1LDEyOTAuNDU4LDk0LjM4NywxMzQwLjY1MSwxMDYuODZDMTM5MC44NDQsMTE5LjMzMywxMzkwLjg0NCwxMjcuNjY3LDEzOTAuODQ0LDEzNkMxMzkwLjg0NCwxNDQuMzMzLDEzOTAuODQ0LDE1Mi42NjcsMTM5MC44NDQsMTU2LjgzM0wxMzkwLjg0NCwxNjEiIGlkPSJteS1zdmctTF9kaW1lbnNpb25sZXNzX3NvbGlkX2FuZ3VsYXJfbWVhc3VyZV8wIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1kb3R0ZWQgZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBmbG93Y2hhcnQtbGluayIgc3R5bGU9IjsiIGRhdGEtZWRnZT0idHJ1ZSIgZGF0YS1ldD0iZWRnZSIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX3NvbGlkX2FuZ3VsYXJfbWVhc3VyZV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVEE0T1M0Mk9EYzFMQ0o1SWpvMk1TNHhOakl4TnpVeU5qVTJORFU0TTMwc2V5SjRJam94TXprd0xqZzBNemMxTENKNUlqb3hNVEY5TEhzaWVDSTZNVE01TUM0NE5ETTNOU3dpZVNJNk1UTTJmU3g3SW5naU9qRXpPVEF1T0RRek56VXNJbmtpT2pFMk1YMWQiIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjxwYXRoIGQ9Ik05MTguNTMxLDUzLjkwNEw4MDAuNTgzLDYzLjQyQzY4Mi42MzUsNzIuOTM2LDQ0Ni43NCw5MS45NjgsMzI4Ljc5MiwxMDUuNjUxQzIxMC44NDQsMTE5LjMzMywyMTAuODQ0LDEyNy42NjcsMjEwLjg0NCwxMzZDMjEwLjg0NCwxNDQuMzMzLDIxMC44NDQsMTUyLjY2NywyMTAuODQ0LDE1Ni44MzNMMjEwLjg0NCwxNjEiIGlkPSJteS1zdmctTF9kaW1lbnNpb25sZXNzX3N0b3JhZ2VfY2FwYWNpdHlfMCIgY2xhc3M9ImVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tZG90dGVkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfZGltZW5zaW9ubGVzc19zdG9yYWdlX2NhcGFjaXR5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk9URTRMalV6TVRJMUxDSjVJam8xTXk0NU1EUXpOekEzTnpjME5ESTVNMzBzZXlKNElqb3lNVEF1T0RRek56VXNJbmtpT2pFeE1YMHNleUo0SWpveU1UQXVPRFF6TnpVc0lua2lPakV6Tm4wc2V5SjRJam95TVRBdU9EUXpOelVzSW5raU9qRTJNWDFkIiBkYXRhLWxvb2s9ImNsYXNzaWMiLz48cGF0aCBkPSJNMTc3MS4xNjYsMjM5TDE3NjMuMDEyLDI0My4xNjdDMTc1NC44NTgsMjQ3LjMzMywxNzM4LjU1LDI1NS42NjcsMTczMC4zOTYsMjY0QzE3MjIuMjQyLDI3Mi4zMzMsMTcyMi4yNDIsMjgwLjY2NywxNzIyLjI0MiwyODlDMTcyMi4yNDIsMjk3LjMzMywxNzIyLjI0MiwzMDUuNjY3LDE3MjIuMjQyLDMwOS44MzNMMTcyMi4yNDIsMzE0IiBpZD0ibXktc3ZnLUxfYW5ndWxhcl9tZWFzdXJlX3JvdGF0aW9uYWxfZGlzcGxhY2VtZW50XzAiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9IkxfYW5ndWxhcl9tZWFzdXJlX3JvdGF0aW9uYWxfZGlzcGxhY2VtZW50XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1UYzNNUzR4TmpZME5ESTROekV3T1RNNExDSjVJam95TXpsOUxIc2llQ0k2TVRjeU1pNHlOREl4T0RjMUxDSjVJam95TmpSOUxIc2llQ0k2TVRjeU1pNHlOREl4T0RjMUxDSjVJam95T0RsOUxIc2llQ0k2TVRjeU1pNHlOREl4T0RjMUxDSjVJam96TVRSOVhRPT0iIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjxwYXRoIGQ9Ik0xOTIzLjgxLDIzOUwxOTMxLjk2NCwyNDMuMTY3QzE5NDAuMTE4LDI0Ny4zMzMsMTk1Ni40MjYsMjU1LjY2NywxOTY0LjU4LDI2NEMxOTcyLjczNCwyNzIuMzMzLDE5NzIuNzM0LDI4MC42NjcsMTk3Mi43MzQsMjg5QzE5NzIuNzM0LDI5Ny4zMzMsMTk3Mi43MzQsMzA1LjY2NywxOTcyLjczNCwzMDkuODMzTDE5NzIuNzM0LDMxNCIgaWQ9Im15LXN2Zy1MX2FuZ3VsYXJfbWVhc3VyZV9waGFzZV9hbmdsZV8wIiBjbGFzcz0iZWRnZS10aGlja25lc3Mtbm9ybWFsIGVkZ2UtcGF0dGVybi1zb2xpZCBlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGZsb3djaGFydC1saW5rIiBzdHlsZT0iOyIgZGF0YS1lZGdlPSJ0cnVlIiBkYXRhLWV0PSJlZGdlIiBkYXRhLWlkPSJMX2FuZ3VsYXJfbWVhc3VyZV9waGFzZV9hbmdsZV8wIiBkYXRhLXBvaW50cz0iVzNzaWVDSTZNVGt5TXk0NE1UQXhNVGsyTWpnNU1EWXlMQ0o1SWpveU16bDlMSHNpZUNJNk1UazNNaTQzTXpRek56VXNJbmtpT2pJMk5IMHNleUo0SWpveE9UY3lMamN6TkRNM05Td2llU0k2TWpnNWZTeDdJbmdpT2pFNU56SXVOek0wTXpjMUxDSjVJam96TVRSOVhRPT0iIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjxwYXRoIGQ9Ik0yMTAuODQ0LDIzOUwyMTAuODQ0LDI0My4xNjdDMjEwLjg0NCwyNDcuMzMzLDIxMC44NDQsMjU1LjY2NywyMTAuODQ0LDI2NEMyMTAuODQ0LDI3Mi4zMzMsMjEwLjg0NCwyODAuNjY3LDIxMC44NDQsMjg5QzIxMC44NDQsMjk3LjMzMywyMTAuODQ0LDMwNS42NjcsMjEwLjg0NCwzMDkuODMzTDIxMC44NDQsMzE0IiBpZD0ibXktc3ZnLUxfc3RvcmFnZV9jYXBhY2l0eV9lcXVpdmFsZW50X2JpbmFyeV9zdG9yYWdlX2NhcGFjaXR5XzAiIGNsYXNzPSJlZGdlLXRoaWNrbmVzcy1ub3JtYWwgZWRnZS1wYXR0ZXJuLXNvbGlkIGVkZ2UtdGhpY2tuZXNzLW5vcm1hbCBlZGdlLXBhdHRlcm4tc29saWQgZmxvd2NoYXJ0LWxpbmsiIHN0eWxlPSI7IiBkYXRhLWVkZ2U9InRydWUiIGRhdGEtZXQ9ImVkZ2UiIGRhdGEtaWQ9Ikxfc3RvcmFnZV9jYXBhY2l0eV9lcXVpdmFsZW50X2JpbmFyeV9zdG9yYWdlX2NhcGFjaXR5XzAiIGRhdGEtcG9pbnRzPSJXM3NpZUNJNk1qRXdMamcwTXpjMUxDSjVJam95TXpsOUxIc2llQ0k2TWpFd0xqZzBNemMxTENKNUlqb3lOalI5TEhzaWVDSTZNakV3TGpnME16YzFMQ0o1SWpveU9EbDlMSHNpZUNJNk1qRXdMamcwTXpjMUxDSjVJam96TVRSOVhRPT0iIGRhdGEtbG9vaz0iY2xhc3NpYyIvPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVscyI+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX2RpbWVuc2lvbmxlc3Nfcm90YXRpb25fMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZGltZW5zaW9ubGVzc190aGVybW9keW5hbWljX2VmZmljaWVuY3lfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfZGltZW5zaW9ubGVzc19kcmFnX2ZhY3Rvcl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzXy4uLl8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX2FuZ3VsYXJfbWVhc3VyZV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX3NvbGlkX2FuZ3VsYXJfbWVhc3VyZV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9kaW1lbnNpb25sZXNzX3N0b3JhZ2VfY2FwYWNpdHlfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0iZWRnZUxhYmVsIj48ZyBjbGFzcz0ibGFiZWwiIGRhdGEtaWQ9IkxfYW5ndWxhcl9tZWFzdXJlX3JvdGF0aW9uYWxfZGlzcGxhY2VtZW50XzAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsIDApIj48Zm9yZWlnbk9iamVjdCB3aWR0aD0iMCIgaGVpZ2h0PSIwIj48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBjbGFzcz0ibGFiZWxCa2ciIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0iZWRnZUxhYmVsIj48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9ImVkZ2VMYWJlbCI+PGcgY2xhc3M9ImxhYmVsIiBkYXRhLWlkPSJMX2FuZ3VsYXJfbWVhc3VyZV9waGFzZV9hbmdsZV8wIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLCAwKSI+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjAiIGhlaWdodD0iMCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgY2xhc3M9ImxhYmVsQmtnIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9ImVkZ2VMYWJlbCI+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJlZGdlTGFiZWwiPjxnIGNsYXNzPSJsYWJlbCIgZGF0YS1pZD0iTF9zdG9yYWdlX2NhcGFjaXR5X2VxdWl2YWxlbnRfYmluYXJ5X3N0b3JhZ2VfY2FwYWNpdHlfMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMCwgMCkiPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIwIiBoZWlnaHQ9IjAiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIGNsYXNzPSJsYWJlbEJrZyIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJlZGdlTGFiZWwiPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48L2c+PGcgY2xhc3M9Im5vZGVzIj48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0ibXktc3ZnLWZsb3djaGFydC1kaW1lbnNpb25sZXNzLTAiIGRhdGEtbG9vaz0iY2xhc3NpYyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTAwNC4xMDkzNzUsIDQ3KSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTg1LjU3ODEyNSIgeT0iLTM5IiB3aWR0aD0iMTcxLjE1NjI1IiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNTUuNTc4MTI1LCAtMjQpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjExMS4xNTYyNSIgaGVpZ2h0PSI0OCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPmRpbWVuc2lvbmxlc3M8L2I+PGJyIC8+W29uZV08L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQiIGlkPSJteS1zdmctZmxvd2NoYXJ0LXJvdGF0aW9uLTIiIGRhdGEtbG9vaz0iY2xhc3NpYyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTA4LjQ2MDkzNzUsIDIwMCkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii01OS43NzM0Mzc1IiB5PSItMjciIHdpZHRoPSIxMTkuNTQ2ODc1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMjkuNzczNDM3NSwgLTEyKSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSI1OS41NDY4NzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5yb3RhdGlvbjwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQiIGlkPSJteS1zdmctZmxvd2NoYXJ0LXRoZXJtb2R5bmFtaWNfZWZmaWNpZW5jeS00IiBkYXRhLWxvb2s9ImNsYXNzaWMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDc0OS4xNjQwNjI1LCAyMDApIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTMwLjkyOTY4NzUiIHk9Ii0yNyIgd2lkdGg9IjI2MS44NTkzNzUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0xMDAuOTI5Njg3NSwgLTEyKSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIyMDEuODU5Mzc1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+dGhlcm1vZHluYW1pY19lZmZpY2llbmN5PC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9Im15LXN2Zy1mbG93Y2hhcnQtZHJhZ19mYWN0b3ItNiIgZGF0YS1sb29rPSJjbGFzc2ljIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMDA0LjEwOTM3NSwgMjAwKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTc0LjAxNTYyNSIgeT0iLTI3IiB3aWR0aD0iMTQ4LjAzMTI1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDQuMDE1NjI1LCAtMTIpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9Ijg4LjAzMTI1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+ZHJhZ19mYWN0b3I8L2I+PC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0ibXktc3ZnLWZsb3djaGFydC0uLi4tOCIgZGF0YS1sb29rPSJjbGFzc2ljIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMTY0Ljc5Njg3NSwgMjAwKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTM2LjY3MTg3NSIgeT0iLTI3IiB3aWR0aD0iNzMuMzQzNzUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC02LjY3MTg3NSwgLTEyKSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMy4zNDM3NSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPi4uLjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9Im15LXN2Zy1mbG93Y2hhcnQtYW5ndWxhcl9tZWFzdXJlLTEwIiBkYXRhLWxvb2s9ImNsYXNzaWMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE4NDcuNDg4MjgxMjUsIDIwMCkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii05Ni4yNTc4MTI1IiB5PSItMzkiIHdpZHRoPSIxOTIuNTE1NjI1IiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjYuMjU3ODEyNSwgLTI0KSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMzIuNTE1NjI1IiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+YW5ndWxhcl9tZWFzdXJlPC9iPjxiciAvPltyYWRdPC9wPjwvc3Bhbj48L2Rpdj48L2ZvcmVpZ25PYmplY3Q+PC9nPjwvZz48ZyBjbGFzcz0ibm9kZSBkZWZhdWx0IiBpZD0ibXktc3ZnLWZsb3djaGFydC1zb2xpZF9hbmd1bGFyX21lYXN1cmUtMTIiIGRhdGEtbG9vaz0iY2xhc3NpYyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTM5MC44NDM3NSwgMjAwKSI+PHJlY3QgY2xhc3M9ImJhc2ljIGxhYmVsLWNvbnRhaW5lciIgc3R5bGU9IiIgeD0iLTExOS4zNzUiIHk9Ii0zOSIgd2lkdGg9IjIzOC43NSIgaGVpZ2h0PSI3OCIvPjxnIGNsYXNzPSJsYWJlbCIgc3R5bGU9IiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoLTg5LjM3NSwgLTI0KSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIxNzguNzUiIGhlaWdodD0iNDgiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5zb2xpZF9hbmd1bGFyX21lYXN1cmU8L2I+PGJyIC8+W3NyXTwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9Im15LXN2Zy1mbG93Y2hhcnQtc3RvcmFnZV9jYXBhY2l0eS0xNCIgZGF0YS1sb29rPSJjbGFzc2ljIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMTAuODQzNzUsIDIwMCkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii05NS4zNjcxODc1IiB5PSItMzkiIHdpZHRoPSIxOTAuNzM0Mzc1IiBoZWlnaHQ9Ijc4Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNjUuMzY3MTg3NSwgLTI0KSI+PHJlY3QvPjxmb3JlaWduT2JqZWN0IHdpZHRoPSIxMzAuNzM0Mzc1IiBoZWlnaHQ9IjQ4Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGUtY2VsbDsgd2hpdGUtc3BhY2U6IG5vd3JhcDsgbGluZS1oZWlnaHQ6IDEuNTsgbWF4LXdpZHRoOiAyMDBweDsgdGV4dC1hbGlnbjogY2VudGVyOyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+c3RvcmFnZV9jYXBhY2l0eTwvYj48YnIgLz5bYml0XTwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9Im15LXN2Zy1mbG93Y2hhcnQtcm90YXRpb25hbF9kaXNwbGFjZW1lbnQtMTciIGRhdGEtbG9vaz0iY2xhc3NpYyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTcyMi4yNDIxODc1LCAzNDEpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItMTIyLjAyMzQzNzUiIHk9Ii0yNyIgd2lkdGg9IjI0NC4wNDY4NzUiIGhlaWdodD0iNTQiLz48ZyBjbGFzcz0ibGFiZWwiIHN0eWxlPSIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKC05Mi4wMjM0Mzc1LCAtMTIpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjE4NC4wNDY4NzUiIGhlaWdodD0iMjQiPjxkaXYgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGh0bWwiIHN0eWxlPSJkaXNwbGF5OiB0YWJsZS1jZWxsOyB3aGl0ZS1zcGFjZTogbm93cmFwOyBsaW5lLWhlaWdodDogMS41OyBtYXgtd2lkdGg6IDIwMHB4OyB0ZXh0LWFsaWduOiBjZW50ZXI7Ij48c3BhbiBjbGFzcz0ibm9kZUxhYmVsIj48cD48Yj5yb3RhdGlvbmFsX2Rpc3BsYWNlbWVudDwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjxnIGNsYXNzPSJub2RlIGRlZmF1bHQiIGlkPSJteS1zdmctZmxvd2NoYXJ0LXBoYXNlX2FuZ2xlLTE5IiBkYXRhLWxvb2s9ImNsYXNzaWMiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE5NzIuNzM0Mzc1LCAzNDEpIj48cmVjdCBjbGFzcz0iYmFzaWMgbGFiZWwtY29udGFpbmVyIiBzdHlsZT0iIiB4PSItNzguNDY4NzUiIHk9Ii0yNyIgd2lkdGg9IjE1Ni45Mzc1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtNDguNDY4NzUsIC0xMikiPjxyZWN0Lz48Zm9yZWlnbk9iamVjdCB3aWR0aD0iOTYuOTM3NSIgaGVpZ2h0PSIyNCI+PGRpdiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94aHRtbCIgc3R5bGU9ImRpc3BsYXk6IHRhYmxlLWNlbGw7IHdoaXRlLXNwYWNlOiBub3dyYXA7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsiPjxzcGFuIGNsYXNzPSJub2RlTGFiZWwiPjxwPjxiPnBoYXNlX2FuZ2xlPC9iPjwvcD48L3NwYW4+PC9kaXY+PC9mb3JlaWduT2JqZWN0PjwvZz48L2c+PGcgY2xhc3M9Im5vZGUgZGVmYXVsdCIgaWQ9Im15LXN2Zy1mbG93Y2hhcnQtZXF1aXZhbGVudF9iaW5hcnlfc3RvcmFnZV9jYXBhY2l0eS0yMyIgZGF0YS1sb29rPSJjbGFzc2ljIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyMTAuODQzNzUsIDM0MSkiPjxyZWN0IGNsYXNzPSJiYXNpYyBsYWJlbC1jb250YWluZXIiIHN0eWxlPSIiIHg9Ii0xNjcuODQzNzUiIHk9Ii0yNyIgd2lkdGg9IjMzNS42ODc1IiBoZWlnaHQ9IjU0Ii8+PGcgY2xhc3M9ImxhYmVsIiBzdHlsZT0iIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTM3Ljg0Mzc1LCAtMTIpIj48cmVjdC8+PGZvcmVpZ25PYmplY3Qgd2lkdGg9IjI3NS42ODc1IiBoZWlnaHQ9IjI0Ij48ZGl2IHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hodG1sIiBzdHlsZT0iZGlzcGxheTogdGFibGU7IHdoaXRlLXNwYWNlOiBicmVhay1zcGFjZXM7IGxpbmUtaGVpZ2h0OiAxLjU7IG1heC13aWR0aDogMjAwcHg7IHRleHQtYWxpZ246IGNlbnRlcjsgd2lkdGg6IDIwMHB4OyI+PHNwYW4gY2xhc3M9Im5vZGVMYWJlbCI+PHA+PGI+ZXF1aXZhbGVudF9iaW5hcnlfc3RvcmFnZV9jYXBhY2l0eTwvYj48L3A+PC9zcGFuPjwvZGl2PjwvZm9yZWlnbk9iamVjdD48L2c+PC9nPjwvZz48L2c+PC9nPjxkZWZzPjxmaWx0ZXIgaWQ9Im15LXN2Zy1kcm9wLXNoYWRvdyIgaGVpZ2h0PSIxMzAlIiB3aWR0aD0iMTMwJSI+PGZlRHJvcFNoYWRvdyBkeD0iNCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iMCIgZmxvb2Qtb3BhY2l0eT0iMC4wNiIgZmxvb2QtY29sb3I9IiMwMDAwMDAiLz48L2ZpbHRlcj48L2RlZnM+PGRlZnM+PGZpbHRlciBpZD0ibXktc3ZnLWRyb3Atc2hhZG93LXNtYWxsIiBoZWlnaHQ9IjE1MCUiIHdpZHRoPSIxNTAlIj48ZmVEcm9wU2hhZG93IGR4PSIyIiBkeT0iMiIgc3RkRGV2aWF0aW9uPSIwIiBmbG9vZC1vcGFjaXR5PSIwLjA2IiBmbG9vZC1jb2xvcj0iIzAwMDAwMCIvPjwvZmlsdGVyPjwvZGVmcz48L3N2Zz4=)

*Dotted lines denote `is_kind` relationships, where a child quantity forms a distinct kind incompatible with quantities of the same parent.*

To provide such support in the library, we provided an `is_kind` specifier that can be appended to the quantity specification:

```cpp
inline constexpr struct angular_measure : quantity_spec<dimensionless, arc_length / radius, is_kind> {} angular_measure;
inline constexpr struct solid_angular_measure : quantity_spec<dimensionless, area / pow<2>(radius), is_kind> {} solid_angular_measure;
inline constexpr struct storage_capacity : quantity_spec<dimensionless, is_kind> {} storage_capacity;
```

With the above, we can constrain `radian`, `steradian`, and `bit` to be allowed for usage with specific quantity kinds only:

```cpp
inline constexpr struct radian : named_unit<"rad", metre / metre, kind_of<isq::angular_measure>> {} radian;
inline constexpr struct steradian : named_unit<"sr", square(metre) / square(metre), kind_of<isq::solid_angular_measure>> {} steradian;
inline constexpr struct bit : named_unit<"bit", one, kind_of<storage_capacity>> {} bit;
```

This still allows the usage of `one` (possibly scaled) for such quantities which is exactly what we wanted to achieve.

It is worth mentioning here that converting up the hierarchy beyond a subkind requires an explicit conversion. For example:

```cpp
static_assert(implicitly_convertible(isq::rotation, dimensionless));
static_assert(!implicitly_convertible(isq::angular_measure, dimensionless));
static_assert(explicitly_convertible(isq::angular_measure, dimensionless));
```

This increases type safety and prevents accidental quantities with invalid units. For example, a result of a conversion from `isq::angular_measure[rad]` to `dimensionless` would be a reference of `dimensionless[rad]`, which contains an incorrect unit for a `dimensionless` quantity. Such a conversion must be explicit and be preceded by an explicit unit conversion:

```cpp
quantity q1 = isq::angular_measure(42. * rad);
quantity<dimensionless[one]> q2 = dimensionless(q1.in(one));
```

#### 20.12.6 Value conversions

Truncation prevention and Unit safety chapters describe the motivation, usage, and safety benefits of the `value_cast`, `in`, and `force_in` value conversion functions.

##### 20.12.6.1 `template` disambiguation concerns

Initially **mp-units** library allowed changing of the `quantity` representation type only via the `value_cast` non-member function. Introducing such a functionality to `in` and `force_in` member functions would mandate the usage of the `template` disambiguator in generic contexts that we encorage with Generic interfaces.

After bringing those concerns to LEWGI in St. Louis, the room agreed that we should provide this functionality for member functions as well. It is really useful and user-friendly in non-generic contexts and for the cases where we deal with a dependent name, we should leave `value_cast` even if it is an always conversion-forcing operation.

##### 20.12.6.2 Value conversions summary

The table below provides all the value conversions functions that may be run on `x` being the instance of either `quantity` or `quantity_point`:

| Forcing | Representation | Unit | Member function | Non-member function |
| --- | --- | --- | --- | --- |
| No | Same | `u` | `x.in(u)` |  |
| No | `T` | Same | `x.in<T>()` |  |
| No | `T` | `u` | `x.in<T>(u)` |  |
| Yes | Same | `u` | `x.force_in(u)` | `value_cast<u>(x)` |
| Yes | `T` | Same | `x.force_in<T>()` | `value_cast<T>(x)` |
| Yes | `T` | `u` | `x.force_in<T>(u)` | `value_cast<u, T>(x)` or `value_cast<T, u>(x)` |

##### 20.12.6.3 Bikeshedding `force_in(U)`

`force_in` is a bit ambiguous name for the conversion function in a quantities and units library. Writing `x.force_in(s)` may be misleading for a quantity of *time* rather than *force*. However, we do not have good alternatives here.

Before we provide some alternatives it is good to mention that we also heve a `x.force_numerical_value_in(u)` to force a truncation while obtaining a numerical value of the quantity.

[[Au]](https://aurora-opensource.github.io/au) library uses `x.coerce_in(u)` for this operation. We could also consider different names. Here are a few possbile alternatives:

- `x.force_in(u)`, `x.force_numerical_value_in(u)`,
- `x.forced_into(u)`, `x.forced_numerical_value_into(u)`,
- `x.unsafe_in(u)`, `x.unsafe_numerical_value_in(u)`,
- `x.lossy_in(u)`, `x.lossy_numerical_value_in(u)`,
- `x.unchecked_in(u)`, `x.unchecked_numerical_value_in(u)`,
- `x.coerce_in(u)`, `x.coerce_numerical_value_in(u)`,
- `x.cast_in(u)`, `x.cast_numerical_value_in(u)`,
- `x.cast_to(u)`, `x.cast_numerical_value_to(u)`.

In case we select `x.cast_to(u)` we probably should also rename `q.in(u)` to `q.to(u)`.

##### 20.12.6.4 Bikeshedding `quantity::rep`

[[mp-units]](https://mpusz.github.io/mp-units) initially tried to be compatible with `std::chrono::duration`. This is why we chose `rep` as the name for a public member type exposed from `quantity` to denote its representation type. This is consistent but may not be the best name.

First, we use `q.numerical_value_in()` to get the underlying value which is already inconsistent with `std::chrono::duration::count()`. Also, as we mentioned already, `quantity` is a numeric wrapper. To provide compatibility between different numeric types maybe we should set a policy that those should expose `value_type` or `element_type`? Both seem to be valid choices here as well.

#### 20.12.7 Binary operators

Binary operators for quantities (and quantity points) should take both arguments as template parameters. Implementing them in terms of implicit convertibility leads to invalid resulting types. Let’s see the following example:

```cpp
static_assert(std::convertible_to<quantity<isq::speed[m/s], int>,
                                  quantity<(isq::length / isq::time)[m/s], double>>);
static_assert(!std::convertible_to<quantity<(isq::length / isq::time)[m/s], double>,
                                   quantity<isq::speed[m/s], int>>);
```

As we see above, `quantity<isq::speed[m/s], int>` converts to `quantity<(isq::length / isq::time)[m/s], double>`, but this is not the case in the other direction. This is caused by the fact that conversion from `double` to `int` is considered truncating. If we would implement the operators in terms of the implicit conversion then we would end up with the quantity of `isq::length / isq::time` as a result, which is suboptimal. We prefer `isq::speed` in this case:

```cpp
quantity q1 = isq::speed(1 * m/s);
quantity q2 = isq::length(1. * m) / isq::time(1. * s);
static_assert(is_of_type<q1 + q2, quantity<isq::speed[m/s], double>>);
```

In the following example, we consistently use floating-point representation types and both quantities are interconvertible:

```cpp
static_assert(std::convertible_to<quantity<(isq::mass * pow<2>(isq::length / isq::time))[J], double>,
                                  quantity<isq::energy[kg*m2/s2], double>>);
static_assert(std::convertible_to<quantity<isq::energy[kg*m2/s2], double>,
                                  quantity<(isq::mass * pow<2>(isq::length / isq::time))[J], double>>);
```

We could think that the problem is gone, and we can use implicit conversions. However, depending on how we implement it, this might lead to an ambiguous overload resolution or lack of substitutability of addition. Even if we somehow solve those issues, none of the types would be perfect as a return type. While forming a resulting type `isq::energy` should have a priority over `isq::mass * pow<2>(isq::length / isq::time)` and `J` should have a priority over `kg*m2/s2`:

```cpp
quantity q1 = (isq::mass(1 * kg) * pow<2>(isq::length(1 * m) / isq::time(1 * s))).in(J);
quantity q2 = isq::energy(1 * kg*m2/s2);
static_assert(is_of_type<q1 + q2, quantity<isq::energy[J], int>>);
```

It is also worth noting that this approach is compatible with [binary operators for `std::chrono::duration`](https://eel.is/c++draft/time.duration.nonmember). As we can read in the Interoperability with the `std::chrono` abstractions chapter, `std::chrono::duration` is interconvertible with the quantity. Nevertheless, with the above, we always need to explicitly convert the argument to a proper entity before doing any arithmetic:

```cpp
static_assert(1 * s + 1s == 2 * s); // does not compile
static_assert(1 * s + quantity{1s} == 2 * s); // OK
```

This prevents ambiguity with `std::chrono::duration` operators and works the same for any user-defined `QuantityLike` type or any other type that is convertible to a `quantity`.

### 20.13 Quantity Points

#### 20.13.1 `delta` and `point` creation helpers

The features described in this chapter directly solve an issue raised on [std-proposals reflector](https://lists.isocpp.org/std-proposals/2024/06/10118.php). As it was reported, the code below may look correct, but it provides an invalid result:

```cpp
quantity Volume = 1.0 * m3;
quantity Temperature = 28.0 * deg_C;
quantity n_ = 0.04401 * kg / mol;
quantity R_boltzman = 8.314 * N * m / (K * mol);
quantity mass = 40.0 * kg;
quantity Pressure = R_boltzman * Temperature.in(K) * mass / n_ / Volume;
std::cout << Pressure << "\n";
```

The problem is related to the accidental usage of a `quantity` rather than `quantity_point` for `Temperature`. This means that after conversion to kelvins, we will get `28 K` instead of the expected `301.15 K`, corrupting all further calculations.

A correct code should use a `quantity_point`:

```cpp
quantity_point Temperature(28.0 * deg_C);
```

This might be an obvious thing for domain experts, but new users of the library may not be aware of the affine space abstractions and how they influence temperature handling.

After a lengthy discussion on handling such scenarios, we decided to:

- make the above code ill-formed,
- provide an alternative way to create `quantity` and `quantity_point` with the `delta` and `point` construction helpers respectively.

Here are the main points of this new design:

1. All references/units that specify point origin in their definition (i.e., `si::kelvin`, `si::degree_Celsius`, and `usc::degree_Fahrenheit`) are excluded from the multiply syntax.
2. A new `delta` quantity construction helper is introduced:
   - `delta<m>(42)` results with a `quantity<si::metre, int>`,
   - `delta<deg_C>(5)` results with a `quantity<si::deg_C, int>`.
3. A new `point` quantity point construction helper is introduced:
   - `point<m>(42)` results with a `quantity_point<si::metre, zeroth_point_origin<kind_of<isq::length>>{}, int>`,
   - `point<deg_C>(5)` results with a `quantity<si::metre, si::ice_point, int>`.

Please note that `si::kelvin` is also excluded from the multiply syntax to prevent the following surprising issues:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Before</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Now</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity q(300 * K);
quantity_point qp(300 * K);
static_assert(q.in(deg_C) != qp.in(deg_C).quantity_from_zero());</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity q = delta&lt;K&gt;(300);
quantity_point qp = point&lt;K&gt;(300);
static_assert(q.in(deg_C) != qp.in(deg_C).quantity_from_zero());</code></pre></td>
</tr>
</table>

We believe that the code enforced with new utilities makes it much easier to understand what happens here.

With such changes to the interface design, the offending code will not compile as initially written. Users will be forced to think more about what they write. To enable the compilation, the users have to create explicitly:

- a `quantity_point` (the intended abstraction in this example) with any of the below syntaxes:

  ```cpp
  quantity_point Temperature = point<deg_C>(28.0);
  auto Temperature = point<deg_C>(28.0);
  quantity_point Temperature(delta<deg_C>(28.0));
  ```
- a `quantity` (an incorrect abstraction in this example) with:

  ```cpp
  quantity Temperature = delta<deg_C>(28.0);
  auto Temperature = delta<deg_C>(28.0);
  ```

Thanks to the new design, we can immediately see what happens here and why the result might be incorrect in the second case.

#### 20.13.2 `default_point_origin<Reference>`, `quantity_from_zero()`, and `natural_point_origin<QuantitySpec>`

`default_point_origin<Reference>`, `quantity_from_zero()`, and `natural_point_origin<QuantitySpec>` are introduced to simplify the usage of:

- temperature (and quantities with similar units) points where each unit has its own origin,
- quantity points for domains with one unquestionable “zero” origin and for which we do not have other predefined origins known at compile time.

In theory, those abstractions are not needed, and in this chapter, we will describe how the API and use cases would look like without it.

Let’s try to reimplement parts of our room AC temperature controller from the Temperature support chapter:

```cpp
constexpr struct room_reference_temp : relative_point_origin<si::zeroth_degree_Celsius + delta<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

room_temp room_ref{};

std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             room_ref.in(deg_C).quantity_from(si::zeroth_degree_Celsius),
             room_ref.in(deg_F).quantity_from(usc::zeroth_degree_Fahrenheit),
             room_ref.in(K).quantity_from(si::zeroth_kelvin));
```

Now let’s compare it to the implementation using the currently proposed design:

```cpp
constexpr struct room_reference_temp : relative_point_origin<point<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

room_temp room_ref{};

std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             room_ref.in(deg_C).quantity_from(default_point_origin(deg_C)),
             room_ref.in(deg_F).quantity_from(default_point_origin(deg_F)),
             room_ref.in(K).quantity_from(default_point_origin(K)));
```

First, removing those features also renders `point<deg_C>(21)` impossible to implement. Second, `default_point_origin(unit)` always gives the correct standard origin for the current unit, so conversions remain unit-agnostic: if someone changes the unit, no origin name needs updating.

For `quantity_point` objects already at their unit’s default origin (the common case for directly constructed temperature points), text output works directly and `quantity_from_zero()` returns the stored displacement:

```cpp
quantity_point temp = point<deg_C>(21.);  // PO = default_point_origin(deg_C) = ice_point

std::println("{} ({}) ({::N[.2f]})", temp, temp.in(deg_F), temp.in(K));
// prints: 21 ℃ (70.8 ℉) (294.15 K)

auto delta_C = temp.quantity_from_zero();        // 21 ℃ — from ice_point
auto delta_K = temp.in(K).quantity_from_zero();  // 294.15 K — from absolute_zero
```

`.quantity_from_zero()` is constrained to `PO == default_point_origin(R)`, matching `zero()`. For points at custom origins (such as `room_ref` above), use `quantity_from(default_point_origin(unit))` to obtain the displacement from the standard origin.

### 20.14 Interoperability with other libraries

It is easy to cooperate with similar entities of other libraries. No matter if we want to provide interoperability with a simple home-grown strongly typed wrapper type (e.g., `Meter`, `Timestamp`, …) or with a feature-rich quantities and units library, we have to provide specializations of:

- a `quantity_like_traits` for external `quantity`-like type,
- a `quantity_point_like_traits` for external `quantity_point`-like type.

#### 20.14.1 Specifying a conversion kind

Before we delve into the template specialization details, let’s first decide if we want the conversions to happen implicitly or if explicit ones would be a better choice. Or maybe the conversion should be implicit in one direction only (e.g., into abstractions in this library) while the explicit conversions in the other direction should be preferred?

There is no one unified answer to the above questions. Everything depends on the use case.

Typically, in the C++ language, the implicit conversions are allowed in cases where:

- both abstractions mean exactly the same, and interchanging them in the code should not change its logic,
- there is no significant runtime overhead introduced by such a conversion (e.g., no need for dynamic allocation or copying of huge internal buffers),
- the target type of the conversion provides the same or better safety to the users,
- we prefer the simplicity of implicit conversions over safety during the (hopefully short) transition period of refactoring our code base from the usage of one library to the other.

In all other scenarios, we should probably enforce explicit conversions.

The kinds of inter-library conversions can be easily configured in specializations of conversion traits in the **mp-units** library. Conversion traits should provide a static data member convertible to `bool`. If the value is `true`, then the conversion is `explicit`. Otherwise, if the value is `false`, implicit conversions will be allowed. The names of the flags are as follows:

- `explicit_import` to describe conversion from the external entity to the one in this library (import case),
- `explicit_export` to describe conversion from the entity in this library to the external one (export case).

#### 20.14.2 Quantities conversions

For example, let’s assume that some company has its own `Meter` strong-type wrapper:

```cpp
struct Meter {
  int value;
};
```

As every usage of `Meter` is at least as good and safe as the usage of `quantity<si::metre, int>`, and as there is no significant runtime performance penalty, we would like to allow the conversion to `std::quantity` to happen implicitly.

On the other hand, the `quantity` type is much safer than the `Meter`, and that is why we would prefer to see the opposite conversions stated explicitly in our code.

To enable such interoperability, we must define a specialization of the `quantity_like_traits<T>` type trait. Such specialization should provide:

- `reference` static data member that provides the quantity reference (e.g., unit),
- `rep` type that specifies the underlying storage type,
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a quantity’s raw value of `rep` type,
- `from_numerical_value(rep)` static member function returning `T`.

For example, for our `Meter` type, we could provide the following:

```cpp
template<>
struct std::quantity_like_traits<Meter> {
  static constexpr auto reference = si::metre;
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = decltype(Meter::value);
  static constexpr rep to_numerical_value(Meter m) { return m.value; }
  static constexpr Meter from_numerical_value(rep v) { return Meter{v}; }
};
```

After that, we can check that the `QuantityLike` concept is satisfied:

```cpp
static_assert(QuantityLike<Meter>);
```

and we can write the following:

```cpp
void print(Meter m) { std::cout << m.value << " m\n"; }

int main()
{
  using namespace std::si::unit_symbols;

  Meter height{42};

  // implicit conversions
  std::quantity h1 = height;
  std::quantity<isq::height[m], int> h2 = height;

  std::cout << h1 << "\n";
  std::cout << h2 << "\n";

  // explicit conversions
  print(Meter(h1));
  print(Meter(h2));
}
```

No matter if we decide to use implicit or explicit conversions, the library’s framework will not allow unsafe operations to happen.

If we extend the above example with unsafe conversions, the code will not compile, and we will have to fix the issues first before the conversion may be performed:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Unsafe</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Fixed</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity&lt;isq::height[m]&gt; h3 = height;
quantity&lt;isq::height[mm], int&gt; h4 = height;
quantity&lt;isq::height[km], int&gt; h5 = height;  // Error (1)
&#10;
std::cout &lt;&lt; h3 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h4 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h5 &lt;&lt; &quot;\n&quot;;
&#10;
print(Meter(h3));                            // Error (2)
print(Meter(h4));                            // Error (3)
print(Meter(h5));</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity&lt;isq::height[m]&gt; h3 = height;
quantity&lt;isq::height[mm], int&gt; h4 = height;
quantity&lt;isq::height[km], int&gt; h5 = quantity{height}.force_in(km);
&#10;
std::cout &lt;&lt; h3 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h4 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h5 &lt;&lt; &quot;\n&quot;;
&#10;
print(Meter(value_cast&lt;int&gt;(h3)));
print(Meter(h4.force_in(m)));
print(Meter(h5));</code></pre></td>
</tr>
</table>

`(1)` Truncation of value while converting from meters to kilometers.

`(2)` Conversion of `double` to `int` is not value-preserving.

`(3)` Truncation of value while converting from millimeters to meters.

#### 20.14.3 Quantity points conversions

To play with quantity point conversions, let’s assume that we have a `Timestamp` strong type in our codebase, and we would like to start using this library to work with this abstraction.

```cpp
struct Timestamp {
  int seconds;
};
```

As we described in The Affine Space chapter, timestamps should be modeled as quantity points rather than regular quantities.

To allow the conversion between our custom `Timestamp` type and the `quantity_point` class template we need to provide the following in the specialization of the `quantity_point_like_traits<T>` type trait:

- `reference` static data member that provides the quantity point reference (e.g., unit),
- `point_origin` static data member that specifies the absolute point, which is the beginning of our measurement scale for our points,
- `rep` type that specifies the underlying storage type,
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the `quantity` being the offset of the point from the origin,
- `from_numerical_value(rep)` static member function returning `T`.

For example, for our `Timestamp` type, we could provide the following:

```cpp
template<>
struct std::quantity_point_like_traits<Timestamp> {
  static constexpr auto reference = si::second;
  static constexpr auto point_origin = default_point_origin(reference);
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = decltype(Timestamp::seconds);
  static constexpr rep to_numerical_value(Timestamp ts) { return ts.seconds; }
  static constexpr Timestamp from_numerical_value(rep v) { return Timestamp(v); }
};
```

After that, we can check that the `QuantityPointLike` concept is satisfied:

```cpp
static_assert(std::QuantityPointLike<Timestamp>);
```

and we can write the following:

```cpp
void print(Timestamp ts) { std::cout << ts.seconds << " s\n"; }

int main()
{
  Timestamp ts{42};

  // implicit conversion
  std::quantity_point qp = ts;

  std::cout << qp << "\n";

  // explicit conversion
  print(Timestamp(qp));
}
```

#### 20.14.4 Interoperability with the `std::chrono` abstractions

In the C++ standard library, we have two types that handle quantities and model the affine space. Those are:

- [`std::chrono::duration`](https://en.cppreference.com/w/cpp/chrono/duration) - specifies quantities of time,
- [`std::chrono::time_point`](https://en.cppreference.com/w/cpp/chrono/time_point) - specifies quantity points of time.

This library comes with built-in interoperability with those types thanks to:

- specializations of `quantity_like_traits` and `quantity_point_like_traits` that provide support for implicit conversions between types in both directions,
- `chrono_point_origin<Clock>` point origin for `std` clocks,
- `to_chrono_duration` and `to_chrono_time_point` dedicated conversion functions that result in types exactly representing this library’s abstractions.

It is important to note here that only a `quantity_point` that uses `chrono_point_origin<Clock>` as its origin can be converted to the `std::chrono` abstractions:

```cpp
inline constexpr struct ts_origin : relative_point_origin<chrono_point_origin<system_clock> + 1 * h> {} ts_origin;
inline constexpr struct my_origin : absolute_point_origin<isq::time> {} my_origin;

quantity_point qp1 = sys_seconds{1s};
auto tp1 = to_chrono_time_point(qp1);  // OK

quantity_point qp2 = chrono_point_origin<system_clock> + 1 * s;
auto tp2 = to_chrono_time_point(qp2);  // OK

quantity_point qp3 = ts_origin + 1 * s;
auto tp3 = to_chrono_time_point(qp3);  // OK

quantity_point qp4 = my_origin + 1 * s;
auto tp4 = to_chrono_time_point(qp4);  // Compile-time Error (1)

quantity_point qp5{1 * s};
auto tp5 = to_chrono_time_point(qp5);  // Compile-time Error (2)
```

`(1)` `my_origin` is not defined in terms of `chrono_point_origin<Clock>`.

`(2)` `natural_point_origin` is not defined in terms of `chrono_point_origin<Clock>`.

Here is an example of how interoperability described in this chapter can be used in practice:

```cpp
using namespace std::chrono;

sys_seconds ts_now = floor<seconds>(system_clock::now());

quantity_point start_time = ts_now;
quantity speed = 925. * km / h;
quantity distance = 8111. * km;
quantity flight_time = distance / speed;
quantity_point exp_end_time = start_time + flight_time;

sys_seconds ts_end = value_cast<int>(exp_end_time.in(s));

auto curr_time = zoned_time(current_zone(), ts_now);
auto mst_time = zoned_time("America/Denver", ts_end);

std::cout << "Takeoff: " << curr_time << "\n";
std::cout << "Landing: " << mst_time << "\n";
```

The above may print the following output:

```cpp
Takeoff: 2023-11-18 13:20:54 UTC
Landing: 2023-11-18 15:07:01 MST
```

As mentioned above, conversions between entities in this and `std::chrono` libraries are implicit in both directions. This simplifies many scenarios. However, with such rules, `common_type_t<chrono::seconds, quantity<si::second, int>>;` and the ternary operator on such arguments will not work. If this concerns LEWG, we may consider implicit conversion in only one direction. However, it is not easy to decide which one to choose.

## 21 Teachability

Through the last years [[mp-units]](https://mpusz.github.io/mp-units) library proved to be very intuitive to both novices in the domain and non-C++ experts. Thanks to the user-friendly multiply syntax, support for CTAD, excellent readability of generated types in compiler error messages, and simplicity of systems definitions, this library makes it easy to do the first steps in the dimensional analysis domain.

### 21.1 Target audiences

Following the practice suggested in [[P1700R0]](https://wg21.link/p1700r0), we identify four distinct user populations for this library, each with different needs and interactions:

| Audience | Population | Roles and skills |
| --- | --- | --- |
| **Application Developers** | millions | Write application code using pre-defined quantities, units, and systems. Perform arithmetic with automatic dimensional analysis and compile-time unit safety. Use `quantity` for deltas and `quantity_point` for points and measurements (temperature, GPS, timestamps). Write generic interfaces constrained with `QuantityOf`. Interoperate with `std::chrono`. Modernise existing codebases by replacing raw numeric types with strongly-typed quantities. |
| **Unit Authors** | tens of thousands | Add named or scaled units to existing quantity types — standard-system extensions (imperial, binary prefixes) and derived combinations. Work entirely within the provided ISQ hierarchy; no new dimensions or quantity specifications required. |
| **Domain Modelers** | thousands | Properly model a new domain: define quantity systems (ISQ-like hierarchies), dimensions, quantity specifications, quantity kind hierarchies, and units. Design domain frameworks (physics engines, geodesy libraries, robotics toolkits) with correct ISQ-style structure. Require domain knowledge and familiarity with the quantity type system; deep C++ metaprogramming is not needed. |
| **Deep Integrators** | hundreds | Bridge custom or legacy types into the quantity system via `quantity_like_traits`. Implement custom representation types with specialised scaling behaviour. Require template metaprogramming expertise and understanding of library internals; domain-specific quantity modelling is not needed. |

This clear separation ensures that the vast majority of users (Application Developers) can be productive immediately with minimal learning, while still providing extensibility for expert users.

#### 21.1.1 Feature mapping by audience

The following table maps library features to their primary target audiences:

| Feature | Application Developers | Unit Authors | Domain Modelers | Deep Integrators |
| --- | --- | --- | --- | --- |
| Multiply syntax (`42 * m`) | ✓ | ✓ | ✓ | ✓ |
| CTAD for quantities | ✓ | ✓ | ✓ | ✓ |
| Arithmetic operations (`+`, `-`, `*`, `/`) | ✓ | ✓ | ✓ | ✓ |
| Unit conversions (`.in(unit)`) | ✓ | ✓ | ✓ | ✓ |
| Comparison operators | ✓ | ✓ | ✓ | ✓ |
| Standard unit symbols (`si::metre`, `usc::foot`) | ✓ | ✓ | ✓ | ✓ |
| Text formatting with `std::format` | ✓ | ✓ | ✓ | ✓ |
| Extracting numerical values (`.numerical_value_in()`) | ✓ | ✓ | ✓ | ✓ |
| `std::chrono` interop | ✓ | ✓ | ✓ | ✓ |
| `quantity` vs `quantity_point` (basic usage) | ✓ | ✓ | ✓ | ✓ |
| Generic interfaces (`QuantityOf<isq::length>`) | ✓ | ✓ | ✓ | ✓ |
| Defining custom units (`named_unit`) |  | ✓ | ✓ | ✓ |
| Unit prefixes (SI and binary) |  | ✓ | ✓ | ✓ |
| Scaled units (`mag<N> * unit`, `mag_constant`) |  | ✓ | ✓ | ✓ |
| Systems of quantities (ISQ-like hierarchies) |  |  | ✓ |  |
| Defining quantity types (`quantity_spec`) |  |  | ✓ |  |
| Custom dimensions (`derived_dimension`) |  |  | ✓ |  |
| Quantity kind hierarchies (`is_kind`) |  |  | ✓ |  |
| Custom point origins |  |  | ✓ |  |
| Representation type constraints (`RepresentationOf`) |  |  | ✓ | ✓ |
| Symbolic expression templates |  |  |  | ✓ |
| Magnitude framework (`mag_power`) |  |  |  | ✓ |
| Custom `quantity_like_traits` |  |  |  | ✓ |
| Custom representation types |  |  |  | ✓ |

Application Developers need only the first eleven rows — the core usage features. Unit Authors additionally define named and scaled units within the existing ISQ hierarchy. Domain Modelers and Deep Integrators are largely disjoint audiences: Domain Modelers bring domain expertise to define quantity systems, dimensions, and specifications, while Deep Integrators bring C++ metaprogramming expertise to extend the library’s type machinery. Both groups build on Unit Author skills, but neither needs the other’s specialisation.

### 21.2 Prerequisites and target audience

Students should have basic familiarity with:

- C++ fundamentals (variables, functions, basic templates)
- Basic physics concepts (*distance*, *time*, *speed*) for motivation

The library is suitable for:

- **Introductory programming courses** - teaches type safety early with intuitive physical examples
- **Scientific computing courses** - provides practical dimensional analysis tools
- **Software engineering courses** - demonstrates modern C++ library design and compile-time safety
- **Physics/engineering courses** - replaces error-prone raw numeric computations

No prior knowledge of template metaprogramming or dimensional analysis is required for basic usage.

### 21.3 Motivation through real-world disasters

Starting with compelling examples helps students understand *why* strong typing matters:

- [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) - Lost in 1999 because thruster software produced pound-force-seconds while the navigation system expected newton-seconds ($125M loss)
- [[Gimli Glider]](https://en.wikipedia.org/wiki/Gimli_Glider) - Air Canada Flight 143 ran out of fuel mid-flight in 1983 after the load was calculated in pounds instead of kilograms
- [[Columbus]](https://en.wikipedia.org/wiki/Christopher_Columbus) - Mixed up the Arabic mile and the Roman mile while preparing his voyage, badly underestimating the size of the equator and his expected travel distance
- [[Ariane flight V88]](https://en.wikipedia.org/wiki/Ariane_flight_V88) - Ariane 5 rocket destroyed in 1996 by an overflow when converting a 64-bit floating-point value to a 16-bit signed integer ($370M loss)

See Safety concerns for more examples and a deeper discussion of why these errors happen.

These examples demonstrate that unit and conversion errors are costly, hard to spot in code review, and can slip through testing. A quick demonstration of untyped vs. typed code makes the value proposition clear:

```cpp
// Unsafe - compiles but crashes spacecraft
double orbital_velocity(double radius, double period)
{
  return 2 * 3.14159 * radius / period;
}
auto v = orbital_velocity(400000, 5400);  // What units? Which one is length? Compiler can't tell!

// Safe - units enforced at compile time
quantity<si::metre / si::second> orbital_velocity(quantity<si::metre> radius, quantity<si::second> period)
{
  return 2 * pi * radius / period;
}
quantity v = orbital_velocity(400 * km, 90 * min);  // OK: 279 m/s
```

### 21.4 Learning path for beginners

#### 21.4.1 Step 1: Basic quantities

If someone is new to the domain, a concise introduction of Systems of units, the [[SI]](https://www.bipm.org/en/publications/si-brochure), and the US Customary System (and how it relates to SI) might be needed.

After that, every new user, even a C++ newbie, should have no problems with understanding the topics of the Quantity construction chapter and should be able to start using the library successfully. At least as long as they keep operating in the safety zone using floating-point representation types.

Start with the multiply syntax for creating quantities:

```cpp
import std;

int main()
{
  using namespace std::si::unit_symbols;

  quantity distance = 100.0 * m;
  quantity time = 9.58 * s;
  quantity speed = distance / time;

  std::println("Usain Bolt's speed: {::N[.2f]}", speed);  // 10.44 m/s
}
```

Key teaching points:

- Natural syntax: `100.0 * m` reads like physics notation
- Automatic unit propagation: `m / s` derived from division
- Type safety: Cannot accidentally add `distance + time`
- CTAD eliminates verbose type spelling

#### 21.4.2 Step 2: Unit conversions and safety

Eventually, the library will stand in the way, disallowing “unsafe” conversions. This would be a perfect place to mention the importance of providing safe interfaces at compile-time and describe why narrowing conversions are unwelcome and what the side effects of those might be. After that, forced conversions in the library should be presented.

Demonstrate safe conversions:

```cpp
quantity<m> race_distance = 100. * m;
quantity<km> trip_distance = race_distance.in(km);  // Safe: 0.1 km

quantity<m, int> d1 = 5 * m;          // OK
quantity<m, int> d2 = 5.5 * m;        // Error: narrowing conversion
quantity<m, int> d3 = (5.5 * m).force_in<int>();  // Explicit truncation

quantity<km, int> d4 = 1500 * m;      // Error: truncation in conversion
quantity<km, int> d5 = (1500 * m).force_in(km);   // Explicit: d5 == 1 km
```

This naturally introduces:

- The `.in(unit)` member function for safe conversions
- Why the library prevents narrowing (data loss, bugs)
- Explicit `.force_in()` for intentional lossy conversions
- Difference between representation narrowing and unit conversion narrowing

#### 21.4.3 Step 3: Interacting with legacy code

In case a target audience needs to interact with legacy interfaces that take raw numeric values, Safe quantity numerical value getters chapter should be introduced. In such a case, it is important to warn students of why this operation is unsafe and what are the potential maintainability issues.

```cpp
// Legacy API
void legacy_api(double distance_in_meters);

// Modern code
quantity dist = 5 * km;
legacy_api(dist.numerical_value_in(m));  // Explicit: I know this is in meters
```

Emphasize the dangers: the compiler cannot verify that `distance_in_meters` actually expects meters rather than feet or kilometers. You must manually ensure the unit in `.numerical_value_in()` matches the legacy API’s expectations, which may be undocumented or ambiguous.

#### 21.4.4 Step 4: Custom units and extensions

Next, we could show how easy extending the library with custom units is. A simple and funny example like the below could be a great exercise here:

```cpp
import std;

inline constexpr struct smoot : std::named_unit<"smoot", std::mag<67> * std::usc::inch> {} smoot;

int main()
{
  constexpr std::quantity dist = 364.4 * smoot;
  std::println("Harvard Bridge length = {::N[.5]} ({::N[.5]}, {::N[.5]}) ± 1 εar",
               dist, dist.in(std::usc::foot), dist.in(std::si::metre));
}
```

This demonstrates that the library is extensible and students can define domain-specific units (e.g., furlongs per fortnight for astronomy, pixels for graphics).

#### 21.4.5 Step 5: Temperature and affine spaces

After a while, we can also introduce students to The affine space abstractions and discuss the Temperature support.

This introduces the distinction between differences (`quantity`) and absolute points (`quantity_point`), using temperature as the most intuitive example:

```cpp
quantity temp_diff = 20 * delta<deg_C>;     // Temperature difference
quantity_point temp = 20 * point<deg_C>;    // Absolute temperature

quantity diff = temp - point<deg_C>(0);     // OK: difference between points
// auto sum = temp + point<deg_C>(10);      // Error: can't add points
```

With the above, we have learned enough for most users’ needs and do not need to delve into more details. The library is intuitive and will prevent all errors at compile time.

### 21.5 Advanced topics

For more advanced classes, groups, or use cases, we can introduce Generic Interfaces and Systems of quantities but we don’t have to describe every detail and corner cases of quantity types design and their convertibility. It is good to start here with Why do we need typed quantities?, followed by Quantities of the same kind and System of quantities is not only about kinds.

#### 21.5.1 Type system and quantity hierarchies

According to our experience, the most common pitfall in using quantity types might be related to the names chosen for them by the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (e.g., *length*). It might be good to describe what *length* means when we say “every *height* is a *length*” and what it means when we describe a box of *length*, *width*, and *height* dimensions. In the latter case, *length* will not restrict us to the horizontal dimension only. This is how the ISQ is defined, and we should accept this. However, we should present a way to define *horizontal length* as presented in the Comparing, adding, and subtracting quantities of the same kind and describe its rationale.

Advanced students can explore:

- Generic programming with quantity concepts (`QuantityOf<isq::length>`)
- Defining custom quantity types (e.g., `horizontal_length`, `gravitational_potential_energy`)
- Interoperability with `std::chrono::duration` and other libraries
- Vector and tensor quantities for mechanics and graphics

### 21.6 Compiler diagnostics and debugging

One of the library’s strongest teaching features is compiler error quality. When students make mistakes, they get readable messages:

```cpp
quantity d = 100 * m;
quantity t = 50 * s;
quantity wrong = d + t;  // Error
```

Type names in errors remain close to the source code: `quantity<si::metre, double>` rather than pages of template instantiation noise.

Debugging is similarly friendly: quantity objects display naturally in debuggers showing both value and unit. Print formatting with `std::print` produces human-readable output without custom formatters.

### 21.7 Exercises and assessment

Suggested exercises for different skill levels:

**Beginner:**

1. Convert recipe measurements between metric and imperial units
2. Calculate *speed* from *distance* and *time* (e.g., average speed for a road trip)
3. Compute area and volume (rectangle, box) with mixed units

**Intermediate:**

1. Implement projectile motion calculator (initial *velocity*, *angle*, *range*, max *height*)
2. Energy and power calculations (*kinetic energy*, *potential energy*, *power consumption* over *time*)
3. *Pressure*, *volume*, and *temperature* conversions (ideal gas law scenarios)

**Advanced:**

1. Implement generic numeric algorithms (linear interpolation, integration) that work with quantities
2. Design a domain-specific unit system (e.g., astronomical units, parsecs, light-years)
3. Integrate existing strongly-typed wrappers with the library using `quantity_like_traits`

### 21.8 Common mistakes and misconceptions

Based on teaching experience with [[mp-units]](https://mpusz.github.io/mp-units):

1. **Using integer representation types**: Leads to narrowing and overflow errors
   - Example: `quantity d = 1500 * m; quantity km_val = d.in(km);` fails (truncation)
   - Example: `quantity<nm, int> small = 5 * m;` fails (overflow on scaling factor)
   - Solution: Use floating-point for most cases, explicit `.force_in()` when integer truncation is intentional
2. **Operator precedence with unit literals**: Forgetting parentheses in expressions
   - Example: `quantity frequency = 1. / 2 * s;` gives `0.5 s`, not `0.5 Hz`
   - Correct: `quantity frequency = 1. / (2 * s);` or `quantity period = 2. * s; auto frequency = 1 / period;`
   - Solution: Use parentheses or intermediate variables for clarity
3. **Confusing `quantity` and `quantity_point`**: Attempting invalid affine space operations
   - Example: `auto result = 20 * deg_C + 30 * deg_C;` - multiply syntax disabled for offset units
   - Solution: Understand difference between intervals (quantities) and points (quantity_points)
4. **Forgetting namespace qualification**: Writing `42 * m` without importing unit symbols
   - Solution: Add `using namespace std::si::unit_symbols;` or use qualified names
5. **Overusing `.numerical_value_in()`**: Extracting raw values unnecessarily
   - Problem: Defeats type safety, makes refactoring harder
   - Solution: Keep quantities typed as long as possible, extract only at boundaries

### 21.9 Integration with curricula

This library fits naturally into existing courses:

**CS1/CS2 (Introductory Programming):**

- Introduce alongside basic types as motivation for type safety
- Use in physics-based programming exercises (projectile motion, etc.)
- Teaches good habits early: explicit units, compile-time verification

**Numerical Methods / Scientific Computing:**

- Replace raw `double` arrays with typed quantities
- Demonstrate that abstraction doesn’t hurt performance
- Real-world applications: simulation, data analysis

**Software Engineering:**

- Case study in modern C++ library design
- Example of zero-overhead abstractions
- Unit testing with dimensional analysis

**Physics / Engineering Computation:**

- Drop-in replacement for manual unit tracking
- Focus on problems, not bookkeeping
- Prevents entire categories of bugs

### 21.10 Teaching impact beyond C++

While the previous sections focus on teaching the library itself, this feature has broader pedagogical value: it transforms C++ into a teaching tool for units and quantities in general. A standardized quantities and units library extends C++’s educational reach beyond traditional computer science into physics, engineering, and even primary education.

#### 21.10.1 Enabling interdisciplinary education

The library provides non-CS educators with a robust computational tool for teaching their subject matter. Physics teachers can build hands-on computational exercises where students implement real physics equations (projectile motion, circuit analysis, thermodynamics) with compile-time verification that their dimensional analysis is correct. Engineering instructors can create laboratory exercises where sensor data is processed with proper unit handling from the start, mirroring professional practice. Chemistry educators can teach stoichiometry and gas laws with students writing code that enforces correct unit conversions between moles, grams, liters, and atmospheres.

This creates opportunities for integrated learning where domain knowledge and computational thinking develop together. A student learning physics doesn’t just memorize formulas—they implement them, and the compiler verifies their understanding of dimensional relationships. When a student writes `force = mass * acceleration` and the library confirms the result has units of force, they’ve demonstrated conceptual understanding in a way that traditional problem sets cannot assess.

#### 21.10.2 Supporting faculty with limited programming experience

Many science and engineering faculty have computational needs but limited software engineering expertise. The library’s intuitive multiply syntax (`distance = 50 * km`) requires minimal C++ knowledge while providing significant safety benefits. Faculty can create course materials using straightforward code that reads like mathematical notation, lowering the barrier to incorporating computation into their curriculum. The library’s compile-time error messages serve double duty: they catch programming mistakes *and* reveal dimensional analysis errors that indicate conceptual misunderstandings.

This is particularly valuable for disciplines where programming is auxiliary to the primary subject. An engineering professor teaching fluid mechanics doesn’t need to become a C++ expert—basic quantities and units operations are accessible with minimal training while still providing the benefits of type safety and dimensional analysis.

#### 21.10.3 Enriching K-12 and informal education

Computing education increasingly begins in primary and secondary schools. Robotics programs, often built around platforms like LEGO Mindstorms or Arduino, provide rich opportunities to introduce quantities and units naturally. A middle school robotics team programming their robot to navigate a course benefits from using `speed = 30 * cm / s` instead of raw numbers. The explicit units make the code self-documenting for young programmers still building intuition about physical quantities.

When students can write `if (distance < 50 * cm) { stop(); }` the connection between their physical robot and their code becomes clearer. The compiler preventing them from comparing distance to time reinforces dimensional understanding at an age when these concepts are still forming. This creates a richer learning environment where programming and physical intuition develop in parallel.

Similarly, informal education settings—science museums, summer camps, maker spaces—can leverage the library in interactive exhibits and workshops. The combination of physical computing (sensors, actuators) with properly-typed quantities provides immediate, tangible feedback about both programming and physics concepts.

#### 21.10.4 Preparing students for professional practice

Standardization ensures students learn an industry-relevant skill. Unlike toy educational languages or frameworks that must be unlearned later, proper units handling in C++ directly transfers to professional software development. Students who learn to write `quantity area = width * height;` where `width` and `height` are quantities develop habits that prevent real-world errors in safety-critical systems.

This is particularly important for students entering industries where C++ dominates: aerospace, automotive, embedded systems, robotics, quantitative finance, and game development. A graduate who has used quantities and units throughout their coursework arrives at their first job already familiar with dimensional analysis in code, ready to contribute safely to production systems.

The standardization aspect is crucial here—without it, each company uses incompatible internal libraries or ad-hoc approaches, forcing new graduates to relearn concepts they should already know. A standard library provides a stable foundation that educational institutions can confidently build curricula around, knowing their graduates will use these same tools professionally.

## 22 Acknowledgements

Special thanks and recognition goes to [The C++ Alliance](https://cppalliance.org) for supporting Mateusz’s membership in the ISO C++ Committee and the production of this proposal.

We would also like to thank:

- Peter Sommerlad for providing valuable feedback that helped us shape the final version of this document,
- Michael Hordijk for discovering typos and improving the flow of some confusing passages,
- Florian Tatzel and J.C. van Winkel (SG20 chairs) for the insightful suggestion to highlight the library’s broader impact on teaching units and quantities beyond C++ education and a need to assign the skills required for different target audiences.

## 23 References

[Ariane flight V88] Ariane flight V88.

https://en.wikipedia.org/wiki/Ariane_flight_V88

[Au] The Au Units library.

https://aurora-opensource.github.io/au

[Boost.Units] Matthias C. Schabel and Steven Watanabe. Boost.Units.

https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html

[CHEP’98] Walter E. Brown. Introduction to the SI Library of Unit-Based
Computation.

https://digital.library.unt.edu/ark:/67531/metadc668099

[Clarence] Steve Chawkins. Mismeasure for Measure.

https://www.latimes.com/archives/la-xpm-2001-feb-09-me-23253-story.html

[Columbus] Christopher Columbus.

https://en.wikipedia.org/wiki/Christopher_Columbus

[Disney] Cause of the Space Mountain Incident Determined at Tokyo
Disneyland Park.

https://web.archive.org/web/20040209033827/http://www.olc.co.jp/news/20040121_01en.html

[Flight 6316] Korean Air Flight 6316 MD-11, Shanghai, China - April 15,
1999.

https://web.archive.org/web/20210917190721/https://www.ntsb.gov/news/press-releases/Pages/Korean_Air_Flight_6316_MD-11_Shanghai_China_-_April_15_1999.aspx

[Gimli Glider] Gimli Glider.

https://en.wikipedia.org/wiki/Gimli_Glider

[Hochrheinbrücke] An embarrassing discovery during the construction of a
bridge.

https://www.normaalamsterdamspeil.nl/wp-content/uploads/2015/03/website_bridge.pdf

[ISO/IEC 80000] ISO/IEC 80000: Quantities and units.

https://www.iso.org/standard/76921.html

[ISO/IEC Guide 99] ISO/IEC Guide 99: International vocabulary of
metrology — Basic and general concepts and associated terms (VIM).

https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99

[JCGM 200:2012] International vocabulary of metrology - Basic and
general concepts and associated terms (VIM) (JCGM 200:2012, 3rd
edition).

https://jcgm.bipm.org/vim/en

[JSR 385] Units of Measurement.

https://unitsofmeasurement.github.io/indriya

[LK8000] LK8000 - Tactical Flight Computer.

http://lk8000.it

[Mars Orbiter] Mars Climate Orbiter.

https://en.wikipedia.org/wiki/Mars_Climate_Orbiter

[Measurement Data] William Kent, Stephanie Leichner Janowski, Bruce
Hamilton, and Dan Hepner. Measurement Data (Archive Report).

https://www.bkent.net/Doc/mdarchiv.pdf

[Medication dose errors] Alma Mulac, Ellen Hagesaether, and Anne Gerd
Granas. Medication dose calculation errors and other numeracy mishaps in
hospitals: Analysis of the nature and enablers of incident reports.

https://onlinelibrary.wiley.com/doi/10.1111/jan.15072

[MISRA C++] MISRA C++:2008 Guidelines for the use of the C++ language in
critical systems.

https://misra.org.uk/misra-c-plus-plus/

[mp-units] mp-units - A Physical Quantities and Units library for C++.

https://mpusz.github.io/mp-units

[nholthaus/units] UNITS - A compile-time, header-only, dimensional
analysis and unit conversion library built on c++14 with no
dependencies.

https://github.com/nholthaus/units

[P0870R5] Giuseppe D’Angelo. 2023-02-15. A proposal for a type trait to
detect narrowing conversions.

https://wg21.link/p0870r5

[P1045R1] David Stone. 2019-09-27. constexpr Function Parameters.

https://wg21.link/p1045r1

[P1700R0] Christopher Di Bella, JC van Winkel. 2019-06-17.
Target-audience tables.

https://wg21.link/p1700r0

[P1729R3] Elias Kosunen, Victor Zverovich. 2023-10-12. Text Parsing.

https://wg21.link/p1729r3

[P1930R0] Vincent Reverdy. 2019-10-07. Towards a standard unit systems
library.

https://wg21.link/p1930r0

[P1935R0] Mateusz Pusz. 2019-10-14. A C++ Approach to Physical Units.

https://wg21.link/p1935r0

[P1935R2] Mateusz Pusz. 2020-01-13. A C++ Approach to Physical Units.

https://wg21.link/p1935r2

[P1949R7] Steve Downey, Zach Laine, Tom Honermann, Peter Bindels, Jens
Maurer. 2021-04-15. C++ Identifier Syntax using Unicode Standard Annex
31.

https://wg21.link/p1949r7

[P2041R1] David Stone. 2021-03-10. template = delete.

https://wg21.link/p2041r1

[P2509R1] Giuseppe D’Angelo. 2025-05-19. A proposal for a type trait to
detect value-preserving conversions.

https://wg21.link/p2509r1

[P2822R2] Lewis Baker. 2024-08-08. Providing user control of associated
entities of class types.

https://wg21.link/p2822r2

[P2830R10] Gašper Ažman, Nathan Nichols. 2025-03-15. Standardized
Constexpr Type Ordering.

https://wg21.link/p2830r10

[P2980R1] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2023-11-28. A motivation, scope, and plan for a quantities and units
library.

https://wg21.link/p2980r1

[P2981R1] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña.
2023-11-09. Improving our safety with a physical quantities and units
library.

https://wg21.link/p2981r1

[P2982R1] Mateusz Pusz, Chip Hogg. 2023-11-09. `std::quantity` as a
numeric type.

https://wg21.link/p2982r1

[P2989R2] Corentin Jabot, Gašper Ažman. 2024-06-16. A Simple Approach to
Universal Template Parameters.

https://wg21.link/p2989r2

[P2993R0] Luke Valenty. 2024-03-21. Constrained Numbers.

https://wg21.link/p2993r0

[P3003R0] Johel Ernesto Guerrero Peña. 2023-10-14. The design of a
library of number concepts.

https://wg21.link/p3003r0

[P3045R0] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2024-02-15. Quantities and units library.

https://wg21.link/p3045r0

[P3045R1] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2024-05-22. Quantities and units library.

https://wg21.link/p3045r1

[P3045R2] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2024-10-09. Quantities and units library.

https://wg21.link/p3045r2

[P3045R3] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2024-10-15. Quantities and units library.

https://wg21.link/p3045r3

[P3045R4] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2024-11-15. Quantities and units library.

https://wg21.link/p3045r4

[P3045R5] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2025-01-13. Quantities and units library.

https://wg21.link/p3045r5

[P3045R6] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2025-06-19. Quantities and units library.

https://wg21.link/p3045r6

[P3045R7] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2026-02-23. Quantities and units library.

https://wg21.link/p3045r7

[P3045R8] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Peña,
Charles Hogg, Nicolas Holthaus, Roth Michaels, Vincent Reverdy.
2026-05-12. Quantities and units library.

https://wg21.link/p3045r8

[P3094R6] Mateusz Pusz. 2025-01-10. std::basic_fixed_string.

https://wg21.link/p3094r6

[P3133R0] Chip Hogg. 2024-02-14. Fast first-factor finding function.

https://wg21.link/p3133r0

[P3380R1] Barry Revzin. 2024-12-17. Extending support for class types as
non-type template parameters.

https://wg21.link/p3380r1

[P3679R0] Hana Dusíková. 2025-05-16. SFINAEable constexpr exceptions.

https://wg21.link/p3679r0

[Pint] Pint: makes units easy.

https://pint.readthedocs.io/en/stable/index.html

[SI] SI Brochure: The International System of Units (SI).

https://www.bipm.org/en/publications/si-brochure

[SI library] SI - Type safety for physical units”.

https://si.dominikberner.ch/doc

[Stonehenge] Tim Robey. Tiny stones, giant laughs: the story behind
Spinal Tap’s Stonehenge.

https://www.telegraph.co.uk/films/2020/05/01/tiny-stones-giant-laughs-story-behind-spinal-taps-stonehenge

[The Guardian] Charles Pensulo. Record Heat: Malawi swelters with
temperatures nearly 68F above average.

https://randomascii.wordpress.com/2023/10/17/localization-failure-temperature-is-hard

[Value Category Is Not Lifetime] Arthur O’Dwyer. Value Category Is Not
Lifetime.

https://quuxplusone.github.io/blog/2019/03/11/value-category-is-not-lifetime/

[Vasa] Rhitu Chatterjee and Lisa Mullins. New Clues Emerge in
Centuries-Old Swedish Shipwreck.

https://theworld.org/stories/2012-02-23/new-clues-emerge-centuries-old-swedish-shipwreck

[Wild Rice] Manufacturers, exporters think metric.

https://www.bizjournals.com/eastbay/stories/2001/07/09/focus3.html

---

1. Users should not select `unit_symbol_separator::half_high_dot` and `character_set::portable` at the same time. This symbol is valid only for UTF-8 encoding. Otherwise, we propose to throw an exception during the unit symbol string processing. We could also ignore the `unit_symbol_separator::half_high_dot` option and use space ” “, like this is the case for `character_set::portable`.↩︎
2. For integral reps, conversion factors are always integers. Non-integer factors already fail due to truncation, so overflow is moot.↩︎

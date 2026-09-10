---
title: "std::embed"
document: P1040R11
date: 2026-06-23
audience: LEWG, LWG, CWG
reply-to:
  - "JeanHeyd Meneide (https://thephd.dev) <phdofthehouse@gmail.com>"
---


## Abstract

A proposal for a function that allows pulling resources at compile-time into a program, and a preprocessor directive to make finding those resources feasible for compilers and build systems.


## 1. Revision History

### 1.1. Revision 11 - June 23<sup>rd</sup>, 2026

- Fix typos and finalization presentation found [here: https://thephd.dev/_presentations/standards/C++/2026%20June%20Brno/p1040/P1040%20-%20std%20embed.html](https://thephd.dev/_presentations/standards/C++/2026%20June%20Brno/p1040/P1040%20-%20std%20embed.html).
- Fix typo with `glob` and `glob_code` identifiers in the code example here.
- Prepend all `#depend` patterns with `^([\\/])?` (or equivalent) to prevent file prefixing (thanks, Dr. Lisa Lippincott), update Wording and Presentation to reflect this.
- Add and update wording to reflect and emphasize implementation-defined checks in the input dependency check and how it can be used VIA an example in the Recommended Practice.
- LEWG voted to use exceptions for error reporting. Added two new types to the wording and a short explanation in § 6.4.3 Exceptions.
- Explain the use of a Mandates (e.g. compile-time precondition) for the fixed-size embeds in § 6.4.3.1 What about an exception for when the span<T, Fixed> is too Small?.
- Update relevant polls from LEWG and EWG at § 2.1 2026 Brno: Library Evolution and Evolution Working Group.

### 1.2. Revision 10 - May 12<sup>th</sup>, 2026

- Prepare for an EWG presentation at the request of the CWG chair by changing a significant portion (particularly the Tony Table and later parapgraphs) of the § 3 Motivation.
- Once more point to existing implementation completed at ThePhD/embed GitHub repository and the existing patches for both GCC and Clang in § 5 Implementation Experience & Current Practice.
- Highlight that the recursive and similar bits of the proposal about their value have been talked about since 2019 in Belfast, shown in § 6.1 Primary Benefit: Recursive Processing and Composable String File Names.
- Mention that, as it always has been, it does not provide a unique address § 6.3.8 Non-Unique / Shared Data. Formalize this in the wording.
- Adjust wording to handle implementations which do partial preprocessing and do not fully honor the steps of a compiler such as Clang in § 6.4.1 Implementation Quirk: Clang and #depend and the Preprocessor.
- A presentation can (eventually, as the June 2026 meeting approaches) be found [here: https://thephd.dev/_presentations/standards/C++/2026%20June%20Brno/p1040/P1040%20-%20std%20embed.html](https://thephd.dev/_presentations/standards/C++/2026%20June%20Brno/p1040/P1040%20-%20std%20embed.html).

### 1.3. Revision 9 - March 25<sup>th</sup>, 2026

- Forward to CWG and LEWG from the Cryodon 2026 March meeting for C++29.
  - CWG to review the wording for core purposes.
  - LEWG to approve changes made to the function signature as mentioned in § 1.4 Revision 8 - June 23rd, 2025.
- Touch up some missing words in the § 7.1 Intent.
- Adjust and clean up wording, synopsis, and signatures in the § 7 Changes to the Standard for LEWG and CWG review.
- CWG:
  - Completely overhaul the § 7.3 Proposed Wording.
  - Rewrite the specification for `#depend` to work appropriately with macro expansion and match the current specification for `#include`/`#embed`.
  - *header-name* is mapped to a sequence of Unicode code points, and then used to do matching to make it somewhat resistant to internal encoding shenanigans. (QUESTION: sequence of characters is better?)
  - Introduce a *input dependency check* algorithm. Currently, it relies on ECMA 262 to describe what is effectively globbing and recursive-globbing behavior. (Maybe it would be better to use a POSIX reference and talk about globbing instead?)
  - Stop italicizing defined terms.
  - Add wording for the non-uniqueness of the data returned from a `std::embed` call § 7.3.1 Modify "§6.8.2 Object Model [intro.object]" one additional entry to the "... potentially non-unique object ..." list..
  - Remove "Postconditions" from the library wording and replace with a better "*Returns:*" clause.
  - More appropriately define the backing storage of the `std::embed` call in the library wording.
- EWG changes to evaluate:
  - Whether or not we want data deduplication for the backing array of `std::embed` call returns (implied and assumed but never explicitly stated during discussion).
- LEWG changes to evaluate:
  - Whether or not `noexcept` should be removed to have `std::embed` throw an exception on file-not-found § 6.4.2 Security: Globs and Otherwise.
  - Whether or not we want `(u8/w)string_view` for `std::embed` or just back to the SG16 recommendation of § 6.3.9 UTF-8 Only?.
- Further discussion of modules has been moved to a new paper, [p1130].

### 1.4. Revision 8 - June 23<sup>rd</sup>, 2025

- EWG settled on translation-unit specific dependencies; modules will be considered at a later date. See the vote § 2 Relevant Polls.
- Solidified wording for translation-unit based dependencies and removed relevant discussion in § 6.3.4 Modules.
- Some unfortunate implementation experience to accommodate the new `std::u8string_view`/`std::string_view`/`std::wstring_view` shenanigans in § 6.3.9 UTF-8 Only?.
- Added additional rationale for why `limit` and `offset` are present in § 6.3.6 Optional Limit and § 6.3.7 Offset.
- Clarified that we are waiting for `bit_cast<...>(...)` to be improved as a means of better "compile time `reinterpret_cast`" rather than frontloading what `TYPE` in `std::embed<TYPE>(...)` is meant for in § 6.3.5 Statically Polymorphic.

### 1.5. Revision 7 - December 12<sup>th</sup>, 2024

- Evaluate several different implementations and talk to several experts about the (now-closed) [p1130] with respect to `#depend`.
- Settle on `#depend` being exclusively based in translation units as this is both simple and easy to implement. Module export can be added on as a later paper, as described in § 6.3.4 Modules.
- Keep `#depend`’s glob syntax and reaffirm the speed of implementation is fine, and that "it’s slow on Windows" is more or less poor programming practices on behalf of folks not willing to use modern Windows/NTFS APIs.
- Choose a specific option for how module behavior works (it is entirely private and local to the module).
- Provide `limit` and `offset` overloads, with `N` exact-limit version as well.

### 1.6. Revision 6 - March 2<sup>nd</sup>, 2020

- Add new section § 2 Relevant Polls.
- Add new section § 6.4 Dependency-Scanning Friendly with #depend.
- Add new section § 8.1 Previous Design Discussion: Modules.
- Improve section § 6.3.5 Statically Polymorphic.
- Add new section § 6.3.6 Optional Limit.
- Add new section § 6.3.9 UTF-8 Only?.
- Add new section § 8.3 Previous Implementations.
- Improve wording and add static version (thanks, @lichray).

### 1.7. Revision 5 - January 13<sup>th</sup>, 2020

- Split `#embed` into a new paper.
- Add memory and time benchmarks from various implementation strategies in the new Current Practice section.
- Address concerns for a generic API and similar in the new Results Analysis section.
- Retarget to EWG and SG 7.

### 1.8. Revision 4 - November 26<sup>th</sup>, 2018

- Wording is now relative to [n4778].
- Minor typo and tweak fixes.

### 1.9. Revision 3 - November 26<sup>th</sup>, 2018

- Change to using `consteval`.
- Discuss potential issues with accessing resources after full semantic analysis is performed. Prepare to poll Evolution Working Group. Reference new paper, [p1130], about resource management.

### 1.10. Revision 2 - October 10<sup>th</sup>, 2018

- Destroy `embed_options` and `alignment` options: if the function is materialized only at compile-time through `constexpr` or the upcoming "immediate functions" (`constexpr!`), there is no reason to make this part of the function. Instead, the user can choose their own alignment when they pin this down into a std::array or some form of C array / C++ storage.

### 1.11. Revision 1 - June 10<sup>th</sup>, 2018

- Create future directions section, follow up on Library Evolution Working Group comments.
- Change `std::embed_options::null_terminated` to `std::embed_options::null_terminate`.
- Add more code demonstrating the old way and motivating examples.
- Incorporate LEWG feedback, particularly alignment requirements illuminated by Odin Holmes and Niall Douglass. Add a feature macro on top of having `__has_include( <embed> )`.

### 1.12. Revision 0 - May 11<sup>th</sup>, 2018

- Initial release. 🎉


## 2. Relevant Polls

The following polls are shaping the current design. Votes are in the form of SF (Strongly in Favor), F (in Favor), N (Neutral), A (Against), SA (Strongly Against).

### 2.1. 2026 Brno: Library Evolution and Evolution Working Group

EWG POLL D1040R11: EWG would prefer that the storage for the static storage duration array backing the data returned by a std::embed call is non-unique (e.g. prefix-dedeplucatible with different std::embed capable of having the same address just like string literals).

- `SF F N A SA`
- `3 8 2 1 0`
- Consensus. Interpretation: This should behave like string literals (optimizable but not required). Note that this is how it’s always been implemented.

EWG POLL D1040R11: Forward D1040R11 to CWG for inclusion in C++29.

- `SF F N A SA`
- `7 8 3 4 1`
- Consensus. Interpretation: Sending to CWG next meeting (after meeting with LEWG and getting their approval, subject to scheduling, etc. etc.).

NOTE: For those confused, the paper was unilaterally sent back to EWG after EWG already forwarded it in § 2.2 2026 Croydon: Evolution Working Group.

LEWG POLL D1040R11: Use (constexpr) exceptions for error reporting in std::embed (allowing for recovery)?

- `SF F N A SA`
- `8 9 1 1 0`
- Consensus. Interpretation: Swap to using new `dependency_error` and `file_not_found_error` types.

LEWG POLL D1040R11: LEWG prefers to use `size_t limit = numeric_limits<size_t>::max()`as a defaulted argument to `std::embed` to signal "read the whole file" as opposed to `optional<size_t> limit = nullopt`.

- `SF F N A SA`
- `2 5 6 7 2`
- No consensus. Interpretation: formalize on `optional<size_t> limit = nullopt`. Note that this is good because this is the difference between "never stop reading" (an error for infinity files) and "read up to this point" (an internal resource limitations problem); one could special case the value internally in the compiler but it is annoying to figure out the right maximum limit value for all targets/architectures and use it as the value, versus just simply not having a value there which is an easy cross-platform detectable condition. A higher quality of implementation can simply error on the `optional` being empty for files that are not seekable (character devices, block devices, certain kinds of pipes (`mkfifo`, etc.), stdin/stdout pipes, etc.) and exceed some kind of timeout or internally-applied limit. Users have already presented valid use cases for all of these.

LEWG POLL D1040R11: Change the 3 different `(u8/w)?string_view`overloads to require exactly one overload of just `char8_t`.

- `SF F N A SA`
- `0 0 3 8 4`
- No consensus. Interpretation: The status-quo of the paper for `u8`, `w`, and plain `string_view` types for the input is okay. This is good because of the issues with implementations needing to reach files.

LEWG POLL D1040R11: Apart from the [current] error handling behaviour we approve of the design direction of `std::embed`.

- `SF F N A SA`
- `10 8 2 0 0`
- Consensus. Interpretation: Come back to LEWG for another meeting to approve, then ask to go to LWG when available (subject to scheduling, time constraints, etc. etc.).

### 2.2. 2026 Croydon: Evolution Working Group

Forward P1040R8 (std::embed and #depend) to CWG and LEWG (to discuss the design of the interface+string types) for inclusion in C++29

- `SF F N A SA`
- `4 13 2 2 1`
- Consensus. Reaffirmed support for translation unit dependencies only. Do module-based dependencies and potential `#depend export ...` in another paper (p1130).

### 2.3. Sofia 2025: Evolution Working Group

P1040R7: EWG prefers using dependecies only from current translation unit meaning library wrapped std::embed in module won’t work on user provided dependencies.

- `SF F N A SA`
- `4 4 6 1 0`
- Consensus: translation unit dependencies only. Do module-based dependencies and potential `#depend export ...` in Primary Module Fragment in a different paper.

### 2.4. 2020-2022

`#depend` - We would like to have this feature in C++(Something) and spend time figuring out the details.

- `SF F N A SA`
- `14 13 2 0 0`
- Consensus: Do more work.

`#depend <foo/**>` - We want recursive globs (recursively searching through directories) for #depend.

- `SF F N A SA`
- `2 3 9 12 4`
- Consensus: Do not want.
- Vote Commentary:
  - A: Complexity?
  - SA: Windows is slow with recursive globs.

It should be mandatory that EVERY file for `std::embed` is specified by a `#depend`.

- `SF F N A SA`
- `4 12 5 6 3`
- Consensus: Split, no consensus. Add why/why not.
- Vote Commentary:
  - SF: This MUST exist. Both compiler and build system authors. (Implementers.)
  - SA: Can make user experience sad face for common case. Build system should scream at you for making the mistake instead.

`#depend` should form a Virtual File System / String Table State that constrains the search and should be passed to std::embed.

- `SF F N A SA`
- `3 11 7 2 2`
- Consensus: Do it.
- Vote Commentary:
  - SA: Hell to implement. (This was the author.)

### 2.5. 2018 Polls

Make std::embed ill-formed inside of a module interface (with a plan to revisit later).

- `SF F N A SA`
- `4 2 7 1 1`
- Consensus: Yes, but Meh.
- Vote Commentary:
  - SA: Modules are important we should make sure it interacts well with modules (figure it out now).
  - SF: How does this work with #depend ?
  - SF: std::embed is basically a #include -- why would we want it in interface? Just focus on getting feature working and doing it well.
  - A: Jumping the gun. Space needs more exploration.
  - N: We are highly undecided - need to answer more questions (especially about Modules).


## 3. Motivation

> I’m very keen on std::embed. I’ve been hand-embedding data in executables for NEARLY FORTY YEARS now. — Guy "Hatcat" Davidson, June 15, 2018

The primary motivation is to allow for not only accessing data at compile-time, but providing seamless, optimizable data loading that can access that information and respond to that information **while embedding data based on what is read at constant evaluation time**. In particular, given two Lua files:

`core/base.lua`:

```lua
base = {
  ["value"] = 30
}
```

`main.lua`:

```lua
require 'core/base.lua'

function main()
  return 1 + base.value
end
```

A C++ program would be capable of doing this:

```cpp
#include <span>
#include <phd/make_static.hpp>
#include <phd/embed.hpp>

int main(int, char*[]) {
  constexpr auto original_file_span = phd::embed<char>("resources/main.lua");

  std::printf("original file (\"%s\"):\n\n%s", "resources/main.lua", original_file.data());
  std::printf("\n\n=================================================================================\n");

  constexpr auto original_file = comptime_make_string_array<original_file_span.size()>(original_file_span);
  constexpr auto lua_code = recursive_parse_lua("resources/main.lua");
  std::printf("`consteval recursive_parse_lua` result:\n\n%s", lua_code.data());

  return 0;
}
```

Without needing any additional build tool-based concatenation or partial-embedded with `#embed` before having those data globs engineered together through string table manipulation or -- worse -- runtime-based coordination such as with GLSL’s `#include`-proxy system. Particularly, the output of the program would be:

```sh
original file ("resources/main.lua"):

require 'core/base.lua'

function main()
  return 1 + base.value
end


=================================================================================
`consteval recursive_parse_lua` result:

-- core/base.lua
base = {
  ["value"] = 30
}


function main()
  return 1 + base.value;
end
```

A very large amount of C and C++ programmer -- at some point -- attempts to `#include` large chunks of non-C++ data into their code. Of course, `#include` expects the format of the data to be source code, and thusly the program fails with spectacular lexer errors. Many different tools and practices were adapted to handle this, as far back as 1995 with the `xxd` tool. Many industries need such functionality, including (but hardly limited to):

- Financial Development
  - representing coefficients and numeric constants for performance-critical algorithms;
- Game Development
  - assets that do not change at runtime, such as icons, fixed textures and other data;
  - Shader and scripting code;
- Embedded Development
  - storing large chunks of binary, such as firmware, in a well-compressed format;
  - placing data in memory on chips and systems that do not have an operating system or file system;
- Application Development
  - compressed binary blobs representing data
  - non-C++ script code that is not changed at runtime;
- Server Development
  - configuration parameters which are known at build-time and are baked in to set limits and give compile-time information to tweak performance under certain loads;
  - SSL/TLS Certificates hard-coded into your executable (requiring a rebuild and potential authorization before deploying new certificates), and;
- Static Analyzers
  - Static analyzers suffer -- much like their binary code generating friends -- from having to parse extremely large array literals;
  - Reduces memory pressure and enables better information tracking and potential sanitization (file source is not lost in build system).

In the pursuit of this goal, these tools have proven to have inadequacies and contribute poorly to the C++ development cycle as it continues to scale up for larger and better low-end devices and high-performance machines, bogging developers down with menial build tasks and trying to cover-up disappointing differences between platforms. It also absolutely destroys state-of-the-art compilers due to the extremely high memory overhead of producing an Abstract Syntax Tree for a braced initializer list of several tens of thousands of integral constants with numeric values at 255 or less.

The request for some form of `#include_string` or similar dates back quite a long time, with one of the oldest stack overflow questions asked-and-answered about it dating back nearly 10 years. Predating even that is a plethora of mailing list posts and forum posts asking how to get script code and other things that are not likely to change into the binary.

A simpler, C-friendly, preprocessor-only version of this functionality was standardized in C++26 and C23 with `#embed <file> params...`, which solved the problem for C and C-adjacent use cases. However, many of the use cases above -- Application Development, Server Development, Embedded Development, and Game Development in particular -- rely on files that rely on other files and feature some form of file-awareness for use of packaging and re-packing reusable bits of code. Whether it is `require '...'` in Lua or `#include <>` in HLSL, many of these data files rely on other data files in order to be complete: in this way, `#embed` is only useful for the simplest and easiest data files which are wholly uncomplicated and feature-complete on their own. Many, many more data formats and their resulting files need to be parsed and stitched together in part or in whole to be usable without a pre-determined build system step.

Additionally, the ability to validate data files at compile-time or -- even more powerfully -- rely on C++26 reflection to generate pitch-perfect interoperation functionality for Python, Go, Java, Lua, and more can all be achieved fairly powerfully if the C++ code could understand such files. The possibility to fully and completely cover much of the value proposition of SWIG, sol2, cons_expr, C-Python, JNI, and many other interface-generation driven by manual labor is fully tied to the ability to be able to on a basic level parse and handle interface declarations at compile-time and hang that off to further `constexpr`, `consteval`, and `template` processing in C++.

This paper proposes `<embed>` to make this process much more efficient, portable, recursive, non-dependent on fixed preprocessor strings and streamlined.


## 4. Scope and Impact

`std::embed` is an extension to the language proposed entirely as a library construct. The goal is to have it implemented with compiler intrinsics, builtins, or other suitable mechanisms. It does not affect the language. The proposed header to expose this functionality is `<embed>`, making the feature entirely-opt-in by checking if either the proposed feature test macro exists.


## 5. Implementation Experience & Current Practice

There are a few cross-platform (and not-so-cross-platform) paths for getting data into an executable. We also scrutinized the performance, with numbers for both memory overhead and speed overhead available at the repository that houses the [current implementation](https://github.com/ThePhD/embed). For ease of access, the numbers as of January 2020 with the latest versions of the indicated compilers and tools are replicated below.

Finally, a proper implementation has been completed in LLVM/Clang trunk and in GCC trunk as of April 25th, 2026, though they are not integrated into main/trunk of either compiler yet. They can be viewed [here: https://github.com/ThePhD/embed/tree/main/patches](https://github.com/ThePhD/embed/tree/main/patches). It can be played with online on [Godbolt](https://compiler-explorer.com/z/WxdsEa9nj).

### 5.1. Speed Results

Below are timing results for a file of random bytes using a specific strategy. The file is of the size specified at the top of the column. Files are kept the same between strategies and tests.

- Intel Core i7-6700HQ @ 2.60 GHz
- 24.0 GB RAM 2952 MHz
- Debian Sid or Windows 10
- Method: Gather timings from `time` *nix program or `Measure-Command { ... }` PowerShell, compute mean

| Strategy | 4 bytes | 40 bytes | 400 bytes | 4 kilobytes |
| --- | --- | --- | --- | --- |
| `#embed` GCC | 0.201 s | 0.208 s | 0.207 s | 0.218 s |
| `phd::embed` GCC | 0.709 s | 0.724 s | 0.711 s | 0.715 s |
| `xxd`-generated GCC | 0.225 s | 0.215 s | 0.237 s | 0.247 s |
| `xxd`-generated Clang | 0.272 s | 0.275 s | 0.272 s | 0.272 s |
| `xxd`-generated MSVC | 0.204 s | 0.229 s | 0.209 s | 0.232 s |
| Circle `@array` | 0.353 s | 0.359 s | 0.361 s | 0.361 s |
| Circle `@embed` | 0.199 s | 0.208 s | 0.204 s | 0.368 s |
| `objcopy` (linker) | 0.501 s | 0.482 s | 0.519 s | 0.527 s |

| Strategy | 40 kilobytes | 400 kilobytes | 4 megabytes | 40 megabytes |
| --- | --- | --- | --- | --- |
| `#embed` GCC | 0.236 s | 0.231 s | 0.300 s | 1.069 s |
| `phd::embed` GCC | 0.705 s | 0.713 s | 0.772 s | 1.135 s |
| `xxd`-generated GCC | 0.406 s | 2.135 s | 23.567 s | 225.290 s |
| `xxd`-generated Clang | 0.366 s | 1.063 s | 8.309 s | 83.250 s |
| `xxd`-generated MSVC | 0.552 s | 3.806 s | 52.397 s | Out of Memory |
| Circle `@array` | 0.353 s | 0.363 s | 0.421 s | 0.585 s |
| Circle `@embed` | 0.238 s | 0.199 s | 0.219 s | 0.368 s |
| `objcopy` (linker) | 0.500 s | 0.497 s | 0.555 s | 2.183 s |

| Strategy | 400 megabytes | 1 gigabyte |
| --- | --- | --- |
| `#embed` GCC | 9.803 s | 26.383 s |
| `phd::embed` GCC | 4.170 s | 11.887 s |
| `xxd`-generated GCC | Out of Memory | Out of Memory |
| `xxd`-generated Clang | Out of Memory | Out of Memory |
| `xxd`-generated MSVC | Out of Memory | Out of Memory |
| Circle `@array` | 2.655 s | 6.023 s |
| Circle `@embed` | 1.886 s | 4.762 s |
| `objcopy` (linker) | 22.654 s | 58.204 s |

### 5.2. Memory Size Results

Below is the peak memory usage (heap usage) for a file of random bytes using a specific strategy. The file is of the size specified at the top of the column. Files are kept the same between strategies and tests.

- Intel Core i7-6700HQ @ 2.60 GHz
- 24.0 GB RAM 2952 MHz
- Debian Sid or Windows 10
- Method: `/usr/bin/time -v` or Execute command hundreds of times, stare at Task Manager

| Strategy | 4 bytes | 40 bytes | 400 bytes | 4 kilobytes |
| --- | --- | --- | --- | --- |
| `#embed` GCC | 17.26 MB | 17.26 MB | 17.26 MB | 17.27 MB |
| `phd::embed` GCC | 38.82 MB | 38.77 MB | 38.80 MB | 38.80 MB |
| `xxd`-generated GCC | 17.26 MB | 17.26 MB | 17.26 MB | 17.27 MB |
| `xxd`-generated Clang | 35.12 MB | 35.22 MB | 35.31 MB | 35.88 MB |
| `xxd`-generated MSVC | < 30.00 MB | < 30.00 MB | < 33.00 MB | < 38.00 MB |
| Circle `@array` | 53.56 MB | 53.60 MB | 53.53 MB | 53.88 MB |
| Circle `@embed` | 33.35 MB | 33.34 MB | 33.34 MB | 33.35 MB |
| `objcopy` (linker) | 17.32 MB | 17.31 MB | 17.31 MB | 17.31 MB |

| Strategy | 40 kilobytes | 400 kilobytes | 4 megabytes | 40 megabytes |
| --- | --- | --- | --- | --- |
| `#embed` GCC | 17.26 MB | 17.96 MB | 53.42 MB | 341.72 MB |
| `phd::embed` GCC | 38.80 MB | 40.10 MB | 59.06 MB | 208.52 MB |
| `xxd`-generated GCC | 24.85 MB | 134.34 MB | 1,347.00 MB | 12,622.00 MB |
| `xxd`-generated Clang | 41.83 MB | 103.76 MB | 718.00 MB | 7,116.00 MB |
| `xxd`-generated MSVC | ~48.60 MB | ~477.30 MB | ~5,280.00 MB | Out of Memory |
| Circle `@array` | 53.69 MB | 54.73 MB | 65.88 MB | 176.44 MB |
| Circle `@embed` | 33.34 MB | 33.34 MB | 39.41 MB | 113.12 MB |
| `objcopy` (linker) | 17.31 MB | 17.31 MB | 17.31 MB | 57.13 MB |

| Strategy | 400 megabytes | 1 gigabyte |
| --- | --- | --- |
| `#embed` GCC | 3,995.34 MB | 9,795.31 MB |
| `phd::embed` GCC | 1,494.66 MB | 5,279.37 MB |
| `xxd`-generated GCC | Out of Memory | Out of Memory |
| `xxd`-generated Clang | Out of Memory | Out of Memory |
| `xxd`-generated MSVC | Out of Memory | Out of Memory |
| Circle `@array` | 1,282.34 MB | 3,199.28 MB |
| Circle `@embed` | 850.40 MB | 2,128.36 MB |
| `objcopy` (linker) | 425.77 MB | 1,064.74 MB |

### 5.3. Results Analysis

The above clearly demonstrates the superiority of `std::embed` over latest optimized trunk builds of various compilers. It is also notable that originally the Circle language did not have an `@embed` keyword, but it was added in December 2019. When the compiler author was spoken to about Study Group 7’s aspirations for a more generic way of representing data from a file, the ultimate response was this:

> I’ll add a new @embed keyword that takes a type and a file path and loads the file and embeds it into an array prvalue of that type. This will cut out the interpreter and it’ll run at max speed. Feed back like this is good. This is super low-hanging fruit.
> 
> – Sean Baxter, December 12th, 2019

It was Circle’s conclusion that a generic API was unsuitable and suffered from the same performance pitfalls that currently plagued current-generation compilers today. And it was SG7’s insistence that a more generic API would be suitable, modeled on Circle’s principles. Given that thorough exploration of the design space in Circle led to the same conclusion this proposal is making, and given the wide variety of languages providing a similar interface (D, Nim, Rust, etc.), it is clear that a more generic API is not desirable for functionality as fundamental and simple as this. This does not preclude a more generic solution being created, but it does prioritize the "Bird in the Hand" approach that the Direction Group and Bjarne Stroustrup have advocated for many times.

Furthermore, inspecting compiler bug reports around this subject area reveal that this is not the first time GCC has suffered monumental memory blowup over unoptimized representation of data. In fact, this is a 16+ year old problem that GCC has been struggling with for a long time now (C++ version here). That the above numbers is nearing the best that can be afforded by some of the most passionate volunteers and experts curating an extremely large codebase should be testament to how hard the language is this area for compiler developers, and how painful it is for regular developers using their tools.

Clang, while having a better data representation and more optimized structures at its disposal, is similarly constrained. With significant implementation work, they are deeply constrained in what they can do:

> It might be possible to introduce some sort of optimized representation specifically for initializer lists. But it would be a big departure from existing AST handling. And it wouldn’t really open up new use cases, given that string literal handling is already reasonably efficient.
> 
> – Eli Friedman, December 29th 2019

Is this really the best use of compiler developer energy?

To provide a backdrop against which a big departure from current AST handling in can be compared, an implementation of the built-in necessary for this proposal is -- for an experienced developer -- at most a few day’s work in either GCC or Clang. Other compiler engineers have reported similar ease of implementation and integration. Should this really be delegated to Quality of Implementation that will be need to be solved N times over by every implementation in their own particularly special way? Chipping away at what is essentially a fundamental inefficiency required by C++'s inescapable tokenization model from the preprocessor plus the sheer cost of an ever-growing language that makes simple constructs like a brace initializer list of integer constants expensive is, in this paper’s demonstrated opinion, incredibly unwise.

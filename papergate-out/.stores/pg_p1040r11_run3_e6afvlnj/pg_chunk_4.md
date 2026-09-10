
### 6.2. Prior Art

There has been a lot of discussion over the years in many arenas, from Stack Overflow to mailing lists to meetings with the Committee itself. The latest advancements that had been brought to WG21’s attention was p0373r0 - File String Literals. It proposed the syntax `F"my_file.txt"` and `bF"my_file.txt"`, with a few other amenities, to load files at compilation time. The following is an analysis of the previous proposal. Additionally, some prior art and understanding comes from #embed.

#### 6.2.1. Literal-Based, constexpr

A user could reasonably assign (or want to assign) the resulting array to a `constexpr` variable as its expected to be handled like most other string literals. This allowed some degree of compile-time reflection. It is entirely helpful that such file contents be assigned to constexpr: e.g., string literals of JSON being loaded at compile time to be parsed by Ben Deane and Jason Turner in their CppCon 2017 talk, constexpr All The Things.

#### 6.2.2. Literal-Based, Null Terminated (?)

It is unclear whether the resulting array of characters or bytes was to be null terminated. The usage and expression imply that it will be, due to its string-like appearance. However, is adding an additional null terminator fitting for desired usage? From the existing tools and practice (e.g., `xxd -i` or linking a data-dumped object file), the answer is no: but the syntax `bF"hello.txt"` makes the answer seem like a "yes". This is confusing: either the user should be given an explicit choice or the feature should be entirely opt-in.

#### 6.2.3. Encoding

Because the proposal used a string literal, several questions came up as to the actual encoding of the returned information. The author gave both `bF"my_file.txt"` and `F"my_file.txt"` to separate binary versus string-based arrays of returns. Not only did this conflate issues with expectations in the previous section, it also became a heavily contested discussion on both the mailing list group discussion of the original proposal and in the paper itself. This is likely one of the biggest pitfalls between separating "binary" data from "string" data: imbuing an object with string-like properties at translation time provide for all the same hairy questions around source/execution character set and the contents of a literal.

### 6.3. Design Goals

Because of the aforementioned reasons, it seems more prudent to take a "compiler intrinsic"/"magic function" approach. The function overload takes the form:

```cpp
template <typename T = byte>
consteval span<const T> embed( 
  string_view resource_identifier,
  size_t offset = 0,
  optional<size_t> limit = std::nullopt
);

template <size_t N, typename T = byte>
consteval span<const T, N> embed( 
  string_view resource_identifier,
  size_t offset = 0
);

template <typename T = byte>
consteval span<const T> embed( 
  wstring_view resource_identifier,
  size_t offset = 0,
  optional<size_t> limit = std::nullopt
);

template <size_t N, typename T = byte>
consteval span<const T, N> embed( 
  wstring_view resource_identifier,
  size_t offset = 0
);

template <typename T = byte>
consteval span<const T> embed( 
  u8string_view resource_identifier,
  size_t offset = 0,
  optional<size_t> limit = std::nullopt
);

template <size_t N, typename T = byte>
consteval span<const T, N> embed( 
  u8string_view resource_identifier,
  size_t offset = 0
);
```

`resource_identifier` is a `string_view` processed in an implementation-defined manner to find and pull resources into C++ at constexpr time. `limit` is the maximum number of elements the function call can produce (but it may produce less). The most obvious source will be the file system, with the intention of having this evaluated as a core constant expression. We do not attempt to restrict the `string_view` to a specific subset: whatever the implementation accepts (typically expected to be a relative or absolute file path, but can be other identification scheme), the implementation should use. The `N` template parameter is for specifying that the returned span has *at least* `N` elements (to fit in the statically-sized `span`).

#### 6.3.1. Implementation Defined

Calls such as `std::embed( "my_file.txt" );`, `std::embed( "data.dll" );`, and `std::embed<vertex>( "vertices.bin" );` are meant to be evaluated in a `constexpr` context (with "core constant expressions" only), where the behavior is implementation-defined. The function has unspecified behavior when evaluated in a non-constexpr context (with the expectation that the implementation will provide a failing diagnostic in these cases). This is similar to how include paths work, albeit `#include` interacts with the programmer through the preprocessor.

There is precedent for specifying library features that are implemented only through compile-time compiler intrinsics (`type_traits`, `source_location`, and similar utilities). Core -- for other proposals such as p0466r1 - Layout-compatibility and Pointer-interconvertibility Traits -- indicated their preference in using a `constexpr` magic function implemented by intrinsic in the standard library over some form of `template <auto X> thing { /* implementation specified */ value; };` construct. However, it is important to note that [p0466r1] proposes type traits, where as this has entirely different functionality, and so its reception and opinions may be different.

Finally, we use "implementation defined" so that compilers can produce implementation-defined search path for their translation units and modules during compilation with flags. The current implementation uses `-fembed-path=some/path/here/` to indicate this, but when it is standardized there will probably be an `-RI` or `-resource-include` flag instead. It is up to the implementation to pick what works for their platform. We rely on the existing machinery from the recently-standardized `#embed` and the recently changed wording, such that `std::embed` uses a "quote resource search".

#### 6.3.2. Binary Only

Creating two separate forms or options for loading data that is meant to be a "string" always fuels controversy and debate about what the resulting contents should be. The problem is sidestepped entirely by demanding that the resource loaded by `std::embed` represents the bytes exactly as they come from the resource. This prevents encoding confusion, conversion issues, and other pitfalls related to trying to match the user’s idea of "string" data or non-binary formats. Data is received exactly as it is from the resource as defined by the implementation, whether it is a supposed text file or otherwise. `std::embed( "my_text_file.txt" )` and `std::embed( "my_binary_file.bin" )` behave exactly the same concerning their treatment of the resource.

#### 6.3.3. Constexpr Compatibility

The entire implementation must be usable in a `constexpr` context. It is not just for the purposes of processing the data at compile time, but because it matches existing implementations that store strings and huge array literals into a variable via `#include`. These variables can be `constexpr`: to not have a constexpr implementation is to leave many of the programmers who utilize this behavior without a proper standardized tool.

#### 6.3.4. Modules

Per the EWG vote for direction in the § 2 Relevant Polls section, modules need more care and consideration and would need further consideration. There were two options presented to EWG:

1. (CHOSEN) Use the dependencies of the current translation unit.
2. (NOT CHOSEN) Accumulate dependencies from the root function invocation in the constant evaluation context, creating a stack of accessible `#depend`s with each invoked function during constant evaluation.
3. (NOT CHOSEN) #2, but with the caveat that only `#depend export ...`s contribute to accessible depends and the others are "private" to the translation unit.

EWG chose to use the current translation unit. This is a simple, forwards-compatible choice while a separate paper will explore and nail down the semantics of use with modules. An early revision of [p1130r1] (revisions 0 and 1) tried to address this problem many, many years too early.

Now that modules have more well-defined semantics, the problem of dependency transfer can be more fully engaged with starting in Revision 2 and further versions of [p1130].

#### 6.3.5. Statically Polymorphic

We allow for 3 different kinds of values in the returned `std::span` to be used: `std::byte`, `char`, and `unsigned char`. The last two are for compatibility with existing code. The first is for forward-facing designs that rely on `std::byte`. The template type provided defaults to `std::byte` to keep this forward-facing aspect of the design.

In the future, we expect that a `std::bit_cast` that uses arrays will move things forward for a compile-time way to take blobs of data and turn them into (potentially) all sorts of types, particularly ones which satisfy `std::is_trivial_v<TYPE>`.

#### 6.3.6. Optional Limit

Consider some file-based resources that are otherwise un-sizeable and un-seek/tellable in various implementations such as `/dev/urandom`. Telling the compiler to go fetch data from this resource infinitely can result in compiler lockups or worse: therefore, the user can specify an additional parameter to the function call such as `std::embed("/dev/infinity", 0, 32);`. The `32` here is a `std::size_t limit` parameter in `std::embed`, and allows users to ask for up to but not more than `limit` elements in the returned `span`.

Note that as per § 6.3.5 Statically Polymorphic, the limit is specified in terms of `T`s, not bytes. This means `sizeof(T) * CHAR_BIT` bits are required, and the implementation is mandated to require up to but not more than that many.

Additionally, a user can provide a template argument `N` of type `std::size_t` to return a `span<T, N>`. This requires at _least_ `N` elements, but maybe more can exist. One can use both of these to request "exactly this many" elements, e.g. a call `std::embed<32>("/dev/infinity");` requires up to but not more than 32 elements (the `limit` parameter passed to the function) and that the returned span has at least 32 elements (the template parameter passed between the `<` and the `>`). Similarly, one could use `std::embed("/dev/infinity", 0, 32).first<32>();`. This fully covers the design space for what making a subset of the data is currently used for (e.g., prefixed data in a common model format that then has "back references" to the data contained in the first `n` elements).

#### 6.3.7. Offset

There is also an `offset` parameter. While this can be achieved by calling `subspan(...)` on the returned value, it does not aid in how MUCH storage is stored on the code-behind and would require optimization to know that the edge(s) of the static storage data array to trim off. Having both `offset` and `limit` allow for the compiler itself to know how much data to retain *without* the use of optimization. It also allows a compiler frontend to merge potentially different calls which pull data offsets from various locations.

#### 6.3.8. Non-Unique / Shared Data

The data that comes from `std::embed` is not unique. It is a matter of quality-of-implementation whether repeat calls with the exact same parameters produce the exact same data pointer. The data that comes from these types can point inside other static data. We make a small carve out in the wording, similar to that of String Literals, to allow for this.

#### 6.3.9. UTF-8 Only?

This is related to a serious problem for string literals, particularly those of Translation Phase 7. When a user types a string literal such as `"Fáuncy.softłer"`, that string literal -- at Phase 5 of compilation -- gets translated from an idealized internal compiler character set to the "Execution Source Character Set". What this means is that the compiler is allowed to perform an implementation-defined translation from the string literal’s ideal compiler representation to the execution character set (often, the presumed target execution character set). While this is not a problem for Clang -- which always uses UTF-8 -- and GCC -- which always uses UTF-8 unless someone specifically passes `-fexec-charset={something}` -- other compilers will take the string `"Fáuncy.softłer"` and mangle it. This mangling does not have to come with warnings: in fact, MSVC will often times replace characters it cannot translate to the execution character set with either Mojibake or `"?"`.

The solution that Study Group 16 recommended was to allow `std::u8string_view` and ONLY `std::u8string_view` as the parameter type. Others in SG-16 voiced concern that this would hamper general usability, but `u8` string literals and `char8_t` were put in the standard for reasons exactly such as this. The execution character set is an unknown and often lossy encoding on legacy systems: requiring UTF-8 with `std::u8string_view` matches most internal compiler representations of idealized text storage and provides a fairly representative way to work with the resource system.

Unfortunately, implementation experience attemping this found that there were a small subsection of files on all deployed operating systems (Windows, Linux-based, and MacOS (both normal and Linux through Asahi Linux)) that needed users to be precise about the byte sequence used to address storage on disk. As a backstop to the primary `std::u8string_view` template that we expect most users to employ with `u8""` string literals, we expect users to occasionally need to reach for `L""` (on fringe non-Windows and Windows machines) as well as `""` (to get an **exact** byte sequence to match specific platform peculiarities, like the absolute mess of file system issues that come from MacOS normalized vs. non-normalized file paths). We did not think this would be important in earlier revisions of the paper, but recently had to address the unfortunate reality of computing at the moment.

### 6.4. Dependency-Scanning Friendly with `#depend`

One of the biggest hurdles to generating consensus was the deep-seated issues with dependency scanning. The model with only dealing with `#include` as a way of adding extra code or data-as-code means that all dependencies -- at the time of compiler invocation -- can be completely and statically known by the end of Phase 4 of compilation. This greatly aided in speedy dependency pulling. `std::embed` throws a wrench in that model as it can affect the generation of code at Phase 7 time, which is when `constexpr` is evaluated. By taking a `std::(u8)string_view`, it makes it impossible to know all files which may be used by a translation or module unit.

For this purpose, a new `#depend` preprocessor directive was introduced. It is intended to inform the compiler which translation units it depends on in order to make it simpler to retrieve all necessary dependencies. An advanced implementation can also replace all `#depend` directives with magical compiler builtins which instruct the compiler to cache the file’s data as part of the translation unit. This makes it possible to send minimal compiler reproductions and test cases for bug vetting, as well as allow distributed systems to continue to use the `-fdirectives-only` or `-frewrite-includes` flags (or similar preprocessor flags).

The `#depend` directive works by allowing a user to specify a what are effectively globs that can be used later to filter out allowed calls to retrieve resources from `std::embed`:

```cpp
// single-dependency directives
#depend <config/graph.bin>
#depend <foo.txt>
// family-dependencies
// do not "recurse" into directories
#depend "art/*"
#depend "art/mocks/*.json"
// recursive-family-dependency
// recurse through directories and similar
#depend "assets/**"
// mixed: all resources starting with
// "translation/", with all files that end in ".po",
// that have at least one "/" (one directory)
// after the "translation/", found recursively
#depend "translation/**/*.po"
```

Some blame was placed on Windows by stating that recursive directory iteration was too slow, and thus that `**` should not be part of the feature set (see § 2 Relevant Polls). However, the manifest existence of CMake’s new `GLOB_RECURSE` in conjunction with `CONFIGURE_DEPENDS` very strongly nullifies the arguments brought up during the taking of that poll, which was that build systems could not do this fast enough on certain platforms (such as Windows). `GLOB_RECURSE` with `CONFIGURE_DEPENDS` was only allowed into CMake after benchmarks proved against conventional wisdom that this could be done swiftly. This was also backed up by the author of Boost’s Low-Level File I/O library. Therefore, we feel compelled to ask the Committee to reconsider this now that there is sufficient data in the positive for such behavior.

`#depend` uses both the chevron-delimited `<foo.txt>` and the quote-delimited `"foo.txt"` formats. This is because one is for resources that are found only on the system / implementation paths similar to `-I` and `-isystem`, and then one that uses local look up plus the aforementioned resource paths. This can be useful for e.g. files that get embedded from system SDKs, like icons from Windows or Android build-time graphical resources or similar.

NOTE: It is also imperative to note that the way Include Directories and Embed Resource Directories work in all implementations is such that they work as-if by recursive glob. That is, `-I/mnt/code/boost-1.56.0/include` provides access to `<boost/soped_ptr.hpp>`, not just the singular folder `<boost>`. That is, every resource and every include underneath boost is allowed, such that they are effectively doing the equivalent of `#depend <boost/**>` to allow, recursively, for any file to be used. `#depend` is modeled off of that same access.

#### 6.4.1. Implementation Quirk: Clang and `#depend` and the Preprocessor

As specified by the standard, a full translation unit is preprocessed before the later stages of compilation are reached. Therefore, this program:

```cpp
int main () {
  std::embed("foo.txt");
}

#depend "foo.txt"
```

is supposed to be fully legal. However, due to the quirks of how C and C++ work as well as the preprocessor, implementations do not actually have to preprocess input fully before moving on to parsing and type checking. Because there is currently no preprocessor directive which could possibly affect preceding preprocessing tokens or Phase 7+ elements, this program is supposed to be well-formed. Unfortunately, testing in Clang with large enough files triggered a failure if there was simply enough tokens before the `#depend` was encountered, resulting in spurious failures that were hard to track down where `std::embed("foo.txt")` would fail.

Therefore, the allowance of `#depend` that lexically follows its use from `std::embed` is conditionally supported. Separated preprocessors in the style of e.g. [eĿlipsis] or similar might work as expected, but implementations like Clang get to choose whether or not. The reason we do this is because it would be a serious change in Clang’s implementation to let this work, even if technically -- by the description of the standard -- it should.

#### 6.4.2. Security: Globs and Otherwise

It is important to note that, insofar as security is concerned, `#depend` that use glob-style syntax is **not** what triggers the full consumption of files from the file system, nor their transport to e.g. a CI server in order to make using `std::embed` on remote conglomerate build servers and similar work. `#depend` is a **whitelist** of files: it does not put any data into the program. You cannot "glob" files into the program, and there is no file system search capabilities built into this program: if a file is not found, the program is **ill-formed**, which is different from finding a file that is empty (in which case the returned `std::span<T>` is empty).

Additionally, security prospects are slightly improved by the fact that a failure to find a resource results in an ill-formed program. This means that a bad actor cannot continuously probe for a set of files until it finds one at build-time; any failed search stops compilation. This is not a fool-proof security or defense measure, but provides a slight check against code that would see to simply slurp up the contents of a file system. However, this does not stop an attacker from simply guessing all of the right files correctly, so it is only a small mitigation. This problem is better solved by build system sandboxing and proper data handling practices.

Finally, the additional security comes from the use of an anchoring `$` at the end of the "dependency pattern" that is used to perform the "input dependency check". This does not allow arbitrary paths that just "happen" to include the depended-on pattern: each `#depend` is anchored as being responsible for describing the tail end of a file. This in conjunction with the `--embed-dir=` resource-finding flags of existing implementations is enough to keep the directory use well-scoped.

NOTE: If an attacker has control of your build flags to make this a problem, you have MUCH bigger problems than the behavior of `std::embed`.

#### 6.4.3. Exceptions

After C++26 added `constexpr` exceptions and `std::meta::` added a `std::meta::exception` type for `consteval` reporting of errors, LEWG strongly voted to allow `std::embed` to provide `constexpr` errors. Two error types are now part of the wording synopsis -- `std::dependency_error` and `std::file_not_found_error`. The first one corresponds to a failed input dependency check. The second one corresponds to not finding the file. Both allow for recovering from a failed `std::embed` call; this is useful for e.g. processing a compile-time `require "foo"` call which checks for a file named `foo`, then a file named `foo.lua`, and then actually rethrowing the exception to just fail.

##### 6.4.3.1. What about an exception for when the `span<T, Fixed>` is too Small?

During discussion at the Brno 2026 meetings, some noted that it would be advantageous to have an exception tossed when an explicitly-provided `N` integral constant expression provided to `std::embed<N>(...)` was too large to be filled out by the file, that this should be an exception too. It was said they could programmatically work with the fact that an e.g. `constexpr auto x = std::embed<5000>(file);` could be worked around and so tossing an exception is better to allow for recovery of such a situation rather than a precondition / mandates violation.

We disagree. Ignoring the fact that throwing an exception here with require successive hard-coded guesses (or programmatically increasing some exact-sized limit with a recursive call or otherwise) in order to get `std::embed<N>` to compile, the same behavior could be achieved much more succinctly and safely by simply programming with a non-fixed-size span, and then using a fixed-size-one of the appropriate width after the programming is done.

Additionally, it is also not how `std::span<T, FixedExtent>(too_small_ptr, too_small_size)`’s constructor or similar works right now. Right now in [views.span], the way an incorrect size for `too_small_size` is handled is:

> Hardened preconditions: If `extent` is not equal to `dynamic_extent`, then `count` == `extent` is true.

It is simply a (hardened) precondition. The only reason we provide an additional mandate rather than a hardened precondition is:

- there is no reason to have undefined behavior at compile-time;
- there is no reason to let this explode inside of the `span` constructor or manifest as undefiend behavior with a pointer-too-far access at compile-time-but-much-later-than-the-`embed`-call;
- and, there is no reasonable recovery case that is any different than how hardened preconditions might handle this.

Therefore, we do not turn this mandates into a throws operation. We consider this to be a precondition and consider it a hard programmer error to do so, just like `std::span` would handle (and does handle it in debug / hardened implementations) during constant evaluation.

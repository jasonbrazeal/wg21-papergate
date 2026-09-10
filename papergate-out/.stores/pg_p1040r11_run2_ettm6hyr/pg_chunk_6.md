## 8. Appendix

### 8.1. Previous Design Discussion: Modules

Due to the vote taken in § 2 Relevant Polls at Revision 7 of this paper, the question posed by this section shown in this section was answered as "translation units only". The hope is to move on with translation units right now per EWG direction and then revisit this question in a separate paper, which will give these details and concerns the answers they deserve.

Modules front-load and bring front-and-center one of the largest problems not with `std::embed`, but with `#depend`. `#depend` is a Compilation Phase 4 entity: that is, it does not exist beyond the preprocessor. In the world of `#include`, preprocessor commands were resolved that would not exist in the traditional `#include` world, or at least would not have to need immediate answers. In particular, the fact that modules can "save" Phase 4 information before proceeding with the rest of compilation opens interesting questions for Module Interface Units (AKA, the public-facing portion of modules). Module implementation units and other module-related bits are, thankfully, entirely unaffected.

The problem is illustrated most powerfully by the following snippet:

`m0.c++m`:

```cpp
export module m0;

#depend "header.bin"

import <embed>;
import combine;

export consteval auto f0(std::string_view f) {
  const auto h = std::embed("header.bin");
  const auto t = std::embed(f);
  return combine(h, t);
}
```

`m1.c++m`:

```cpp
export module m1;

#depend "default.stuff"

import m0;

export consteval auto f1(std::string_view f = "default.stuff") {
  return f0(f);
}

export consteval auto getpath() {
  return "default.stuff";
}
```

`translation_unit0.c++`:

```cpp
import m1;
import print;
import <embed>

#depend "coolstuff.bin"

int main() {
  print(f1("coolstuff.bin"));  // [0] fails
  print(f1());                 // [1] fails
  std::embed("header.bin");    // [2] fails
  std::embed(getpath());       // [3] fails	
  std::embed("coolstuff.bin"); // [4] ok	
}
```

All of `[0]`, `[1]`, `[2]`, and `[3]` fail because each of them is trying to access dependencies that are part of translation units outside of the current translation unit. That is: modules do not transfer their dependencies outside of themselves. This seems unnecessarily cruel and hostile, but behaves in this manner to keep the specification simple and implementable. In the future or perhaps in another revision of this paper, additional work can be done to define the relationship in terms of translation units under a module accumulating all of their `#depend`s together. There is also some speculation on making such dependencies explicit with an additional form of `#depend` like:

`deps.c++m`:

```cpp
export module deps;

#depend <sdk/private/​**>
#depend export <sdk/everything/​**>
```

`main.cpp`:

```cpp
import deps;

int main () {
  std::embed("sdk/everything/meow.wav"); // ok
  std::embed("sdk/private/super_secret_sauce.mix"); // ill-formed
  return 0;
}
```

This would make the behavior opt-in and predictable. We do not include it in the most recent revision of this paper and plan to talk to SG15 and Modules Experts to craft this wording in a different version of this paper, after getting approval for the core feature and feedback from EWG. We also need to resolve the behavior for `cpp.import`-style header-unit importing. As of right now, no wording is provided for this section with respect to `std::embed` and resource dependencies, so as of right now importing a module versus importing a header unit does not change much insofar as our limited understanding is concerned.

### 8.2. Alternative

Other techniques used include pre-processing data, link-time based tooling, and assembly-time runtime loading. They are detailed below, for a complete picture of today’s sad landscape of options.

#### 8.2.1. Pre-Processing Tools Alternative

1. Run the tool over the data (`xxd -i xxd_data.bin > xxd_data.h`) to obtain the generated file (`xxd_data.h`):

```cpp
unsigned char xxd_data_bin[] = {
  0x48, 0x65, 0x6c, 0x6c, 0x6f, 0x2c, 0x20, 0x57, 0x6f, 0x72, 0x6c, 0x64,
  0x0a
};
unsigned int xxd_data_bin_len = 13;
```

1. Compile `main.cpp`:

```cpp
#include <iostream>
#include <string_view>

// prefix as constexpr,
// even if it generates some warnings in g++/clang++
constexpr
#include "xxd_data.h"
;

template <typename T, std::size_t N>
constexpr std::size_t array_size(const T (&)\[N]) {
  return N;
}

int main() {
  static_assert(xxd_data_bin[0] == 'H');
  static_assert(array_size(xxd_data_bin) == 13);

  std::string_view data_view(
    reinterpret_cast<const char*>(xxd_data_bin),
    array_size(xxd_data_bin));
  std::cout << data_view << std::endl; // Hello, World!
  return 0;
}
```

Others still use python or other small scripting languages as part of their build process, outputting data in the exact C++ format that they require.

There are problems with the `xxd -i` or similar tool-based approach. Lexing and Parsing data-as-source-code adds an enormous overhead to actually reading and making that data available.

Binary data as C(++) arrays provide the overhead of having to comma-delimit every single byte present, it also requires that the compiler verify every entry in that array is a valid literal or entry according to the C++ language.

This scales poorly with larger files, and build times suffer for any non-trivial binary file, especially when it scales into Megabytes in size (e.g., firmware and similar).

#### 8.2.2. `python` Alternative

Other companies are forced to create their own ad-hoc tools to embed data and files into their C++ code. MongoDB uses a [custom python script](https://github.com/mongodb/mongo/blob/master/site_scons/site_tools/jstoh.py), just to get their data into C++:

```python
import os
import sys

def jsToHeader(target, source):
  outFile = target
  h = [
    '#include "mongo/base/string_data.h"',
    '#include "mongo/scripting/engine.h"',
    'namespace mongo {',
    'namespace JSFiles{',
  ]
  def lineToChars(s):
    return ','.join(str(ord(c)) for c in (s.rstrip() + '\n')) + ','
  for s in source:
    filename = str(s)
    objname = os.path.split(filename)[1].split('.')[0]
    stringname = '_jscode_raw_' + objname

    h.append('constexpr char ' + stringname + "[] = {")

    with open(filename, 'r') as f:
      for line in f:
        h.append(lineToChars(line))

    h.append("0};")
    # symbols aren't exported w/o this
    h.append('extern const JSFile %s;' % objname)
    h.append('const JSFile %s = { "%s", StringData(%s, sizeof(%s) - 1) };' %
        (objname, filename.replace('\\', '/'), stringname, stringname))

  h.append("} // namespace JSFiles")
  h.append("} // namespace mongo")
  h.append("")

  text = '\n'.join(h)

  with open(outFile, 'wb') as out:
    try:
      out.write(text)
    finally:
      out.close()


  if __name__ == "__main__":
  if len(sys.argv) < 3:
    print "Must specify [target] [source] "
    sys.exit(1)
  jsToHeader(sys.argv[1], sys.argv[2:])
```

MongoDB were brave enough to share their code with me and make public the things they have to do: other companies have shared many similar concerns, but do not have the same bravery. We thank MongoDB for sharing.

#### 8.2.3. `ld` Alternative

A full, compilable example (except on Visual C++):

1. Have a file ld_data.bin with the contents `Hello, World!`.
2. Run `ld -r binary -o ld_data.o ld_data.bin`.
3. Compile the following `main.cpp` with `c++ -std=c++17 ld_data.o main.cpp`:

```cpp
#include <iostream>
#include <string_view>

#ifdef __APPLE__
#include <mach-o/getsect.h>

#define DECLARE_LD(NAME) extern const unsigned char _section$__DATA__##NAME[];
#define LD_NAME(NAME) _section$__DATA__##NAME
#define LD_SIZE(NAME) (getsectbyname("__DATA", "__" #NAME)->size)

#elif (defined __MINGW32__) /* mingw */

#define DECLARE_LD(NAME)                                 \
  extern const unsigned char binary_##NAME##_start[]; \
  extern const unsigned char binary_##NAME##_end[];
#define LD_NAME(NAME) binary_##NAME##_start
#define LD_SIZE(NAME) ((binary_##NAME##_end) - (binary_##NAME##_start))

#else /* gnu/linux ld */

#define DECLARE_LD(NAME)                                  \
  extern const unsigned char _binary_##NAME##_start[]; \
  extern const unsigned char _binary_##NAME##_end[];
#define LD_NAME(NAME) _binary_##NAME##_start
#define LD_SIZE(NAME) ((_binary_##NAME##_end) - (_binary_##NAME##_start))
#endif

DECLARE_LD(ld_data_bin);

int main() {
  // impossible
  //static_assert(xxd_data_bin[0] == 'H');
  std::string_view data_view(
    reinterpret_cast<const char*>(LD_NAME(ld_data_bin)), 
    LD_SIZE(ld_data_bin)
  );
  std::cout << data_view << std::endl; // Hello, World!
  return 0;
}
```

This scales a little bit better in terms of raw compilation time but is shockingly OS, vendor and platform specific in ways that novice developers would not be able to handle fully. The macros are required to erase differences, lest subtle differences in name will destroy one’s ability to use these macros effectively. We omitted the code for handling VC++ resource files because it is excessively verbose than what is present here.

N.B.: Because these declarations are `extern`, the values in the array cannot be accessed at compilation/translation-time.

#### 8.2.4. Manual Work

Many developers also hand-wrap their files in (raw) string literals, or similar to massage their data -- binary or not -- into a conforming representation that can be parsed at source code:

1. Have a file `data.json` with some data, for example:

```
{ "Hello": "World!" }
```

1. Mangle that file with raw string literals, and save it as `raw_include_data.h`:

```cpp
R"json({ "Hello": "World!" })json"
```

1. Include it into a variable, optionally made `constexpr`, and use it in the program:

```cpp
#include <iostream>
#include <string_view>

int main() {
  constexpr std::string_view json_view =
#include "raw_include_data.h"
    ;

  // { "Hello": "World!" }
  std::cout << json_view << std::endl;
  return 0;
}
```

This happens often in the case of people who have not yet taken the "add a build step" mantra to heart. The biggest problem is that the above C++-ready source file is no longer valid in as its original representation, meaning the file as-is cannot be passed to any validation tools, schema checkers, or otherwise. This hurts the portability and interop story of C++ with other tools and languages.

Furthermore, if the string literal is too big vendors such as VC++ will hard error the build (example from Nonius, benchmarking framework).

#### 8.2.5. The `incbin` tool

There is a tool called [incbin] which is a 3rd party attempt at pulling files in at "assembly time". Its approach is incredibly similar to `ld`, with the caveat that files must be shipped with their binary. It unfortunately falls prey to the same problems of cross-platform woes when dealing with VC++, requiring additional pre-processing to work out in full.

### 8.3. Previous Implementations

This section is primarily to address feedback from polls wherein different forms and implementation strategies were asked for by the Evolution Working Group and other implementers. A tour of the design and implementation these cases helps show what has been considered.

#### 8.3.1. `#depend` Soft Warnings, Hard Errors?

The current specification makes it a hard error if a file has not been identified previously by a `#depend` directive. This makes the simple case of including a single file a bit more annoying than it needs to be, but also makes the case of general development with a non-distributed build system a pain. To be perfectly transparent, the author of this paper and almost 100% of the author’s clients do not use distributed anything to build their code: errors at "file not found" are generally useful enough. Making the lack of matching `#depend` a hard error seems like pushing an important but nevertheless Committee-over-represented concern (i.e. distributed build tool users) onto all C++ users.

While the author feels a lot better about it being a soft warning that can be turned into a hard error by use of `-Werror-depend` for distributed build users, we leave the specification to strongly encourage implementations to hard error on an inability to not only find the resource but match it with a previous `#depend` declaration.

#### 8.3.2. String Table / Virtual File System

This implementation idea was floated twice, once during SG-7 discussion at the November 2019 Belfast meeting and again during the February 2020 Prague meeting. The crux of this version of `std::embed` is that it does not take resource identifiers related to e.g. the file system directly: a directive is used to build a "String Table" or "Translation Table" from system-specific paths to "friendly" names:

```cpp
// map "foo.txt" to file name "foo"
#depend_name "foo.txt" "foo"

#ifdef _WIN32
  // map Windows-specific resource
  // "win/bazunga.bin" to file name "baz"
  #depend_name "win/bazunga.bin" "baz"
#else
  // map Unix-specific resource
  // "nix/bazooka.bin" to file name "baz"
  #depend_name "nix/bazooka.bin" "baz"
#endif

#include <embed>

int main () {
  // pulls foo.txt
  constexpr std::span<std::byte> foo = std::embed("foo");
  // pulls either bazunga or bazooka
  constexpr std::span<std::byte> baz = std::embed("baz");
  return foo[0] == 'f' && baz[2] == '\x3';
}
```

On the tin, this seems to bring nice properties to the table. We get to "erase" platform-specific paths and give them common names, we have a static list of names that we always pull from, and more. However, there are several approaches to this problem. Consider one of the primary use cases for `std::embed` as a `constexpr` function: reading a resource and, based on its contents, `std::embed`-ing other resources.

This becomes a problem: if `foo.txt` has a `get: bar.doc` line of text in it, we read that line from `foo.txt`, and then attempt to `std::embed("bar.doc")`, we get an error because we did not give `bar.doc` a string table name. This means we need to go back and not only mark it as a dependency with `#depend`, but also give it a static string-table based name.

Even conquering that problem (with, e.g., glob-based `#depend` families of dependencies), we face another: resource files -- JSON, SPIR-V, Wavefront OBJ, HLSL/GLSL, python, Lua, HSAIL, whatever -- do not speak "C++ String Table" to name their identifiers. Generally, these speak "File System": we are adding a level of indirection that makes it difficult to keep working with the file system, especially when it comes to working with external resources. Most tools communicate and traffic interchange information VIA URIs or relative / local file paths. Forcing users to either adapt their code to play nice with this new C++ file system or maintaining a translation table to and from "C++ String Table" to "C++ File System" is an order of magnitude additional complexity.

There is absolutely room for a (potentially `constexpr`) Virtual File System in C++. This is not the feature that should bring us there. As the current implementation does, manipulating `--embed-dir=` similar to the way `#include` is handled alongside `-I` flags is a much better use of not only implementer time, but programmer time. It fits perfectly into the mental model ("include, but for resources") and lets users keep their file names as the unit of interchange as far as names go.

C++ does not need to make for itself a reputation of trying to be an extremely unique snowflake at the cost of usability and user friendliness.


## 9. Acknowledgements

Thank you to Hana Dusíková for helping jumpstart and kick off the final public Clang Implementation / Patches and the newer design ideas for C++29.

A big thank you to Andrew Tomazos for replying to the author’s e-mails about the prior art. Thank you to Arthur O’Dwyer for providing the author with incredible insight into the Committee’s previous process for how they interpreted the Prior Art.

A special thank you to Agustín Bergé for encouraging the author to talk to the creator of the Prior Art and getting started on this. Thank you to Tom Honermann for direction and insight on how to write a paper and apply for a proposal.

Thank you to Arvid Gerstmann for helping the author understand and use the link-time tools.

Thank you to Tony Van Eerd for valuable advice in improving the main text of this paper.

Thank you to Lilly (Cpplang Slack, @lillypad) for the valuable bikeshed and hole-poking in original designs, alongside Ben Craig who very thoroughly explained his woes when trying to embed large firmware images into a C++ program for deployment into production. Thank you to Elias Kounen and Gabriel Ravier for wording review.

For all this hard work, it is the author’s hope to carry this into C++. It would be the author’s distinct honor to make development cycles easier and better with the programming language we work in and love. ♥


## References

### Non-Normative References

**[CIRCLE-EMBED-TWEET]**
: Sean Baxter. [@embed added to Circle](https://twitter.com/seanbax/status/1205195567003045888). URL: [https://twitter.com/seanbax/status/1205195567003045888](https://twitter.com/seanbax/status/1205195567003045888)

**[CLANG-LARGE-INIT-BUG]**
: LLVM Foundation. [Memory Consumption Reduction for Large Array Initialization?](https://bugs.llvm.org/show_bug.cgi?id=44399). URL: [https://bugs.llvm.org/show_bug.cgi?id=44399](https://bugs.llvm.org/show_bug.cgi?id=44399)

**[CONSTEXPR-ALL-THE-THINGS]**
: Ben Deane; Jason Turner. [constexpr All The Things: CppCon 2017](https://www.youtube.com/watch?v=PJwd4JLYJJY). September 25th, 2017. URL: [https://www.youtube.com/watch?v=PJwd4JLYJJY](https://www.youtube.com/watch?v=PJwd4JLYJJY)

**[eĿlipsis]**
: Jens Gustedt. [eĿlipsis, a language independent preprocessor](https://gustedt.gitlabpages.inria.fr/ellipsis). April 28th, 2026. URL: [https://gustedt.gitlabpages.inria.fr/ellipsis](https://gustedt.gitlabpages.inria.fr/ellipsis)

**[GCC-LARGE-INIT-BUG-C]**
: GCC. [[8/9/10 regression] Uses lots of memory when compiling large initialized arrays](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=12245). URL: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=12245](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=12245)

**[GCC-LARGE-INIT-BUG-CPP]**
: GCC. [[8/9/10 regression] Uses lots of memory when compiling large initialized arrays](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=14179). URL: [https://gcc.gnu.org/bugzilla/show_bug.cgi?id=14179](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=14179)

**[INCBIN]**
: Dale Weiler (graphitemaster). [incbin: load files at 'assembly' time](https://github.com/graphitemaster/incbin). URL: [https://github.com/graphitemaster/incbin](https://github.com/graphitemaster/incbin)

**[N4778]**
: Richard Smith. [Working Draft, Standard for Programming Language C++](https://wg21.link/n4778). 8 October 2018. URL: [https://wg21.link/n4778](https://wg21.link/n4778)

**[NONIUS-VISUAL-C-ERROR]**
: R. Martinho Fernandes. [nonius generated HTML Reporter](https://github.com/libnonius/nonius/blob/devel/include/nonius/reporters/html_reporter.h%2B%2B#L42). September 1st, 2016. URL: [https://github.com/libnonius/nonius/blob/devel/include/nonius/reporters/html_reporter.h%2B%2B#L42](https://github.com/libnonius/nonius/blob/devel/include/nonius/reporters/html_reporter.h%2B%2B#L42)

**[P0373R0]**
: Andrew Tomazos. [Proposal of File Literals](https://wg21.link/p0373r0). 21 May 2016. URL: [https://wg21.link/p0373r0](https://wg21.link/p0373r0)

**[P0466R1]**
: Lisa Lippincott. [Layout-compatibility and Pointer-interconvertibility Traits](https://wg21.link/p0466r1). 12 February 2018. URL: [https://wg21.link/p0466r1](https://wg21.link/p0466r1)

**[P1130]**
: JeanHeyd Meneide. [Module Resource Requirement Propagation](https://thephd.dev/_vendor/future_cxx/papers/d1130.html). November 26th, 2018. URL: [https://thephd.dev/_vendor/future_cxx/papers/d1130.html](https://thephd.dev/_vendor/future_cxx/papers/d1130.html)

**[P1130R1]**
: JeanHeyd Meneide. [Module Resource Requirement Propagation](https://wg21.link/p1130r1). 21 January 2019. URL: [https://wg21.link/p1130r1](https://wg21.link/p1130r1)

**[P1130R2]**
: JeanHeyd Meneide. [Module Resource Requirement Propagation](https://wg21.link/p1130r2). 27 March 2026. URL: [https://wg21.link/p1130r2](https://wg21.link/p1130r2)

**[P1967]**
: JeanHeyd Meneide. [Module Resource Requirement Propagation](https://thephd.dev/_vendor/future_cxx/papers/d1967.html). February 14th, 2025. URL: [https://thephd.dev/_vendor/future_cxx/papers/d1967.html](https://thephd.dev/_vendor/future_cxx/papers/d1967.html)

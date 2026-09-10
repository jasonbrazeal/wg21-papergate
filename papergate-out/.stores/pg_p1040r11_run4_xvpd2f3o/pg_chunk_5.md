## 7. Changes to the Standard

Wording changes are relative to the latest working draft.

### 7.1. Intent

The intent of the wording is to provide a `consteval` function and a preprocessor directive that:

- whitelists a given file or a set of files for use with the `consteval` `std::embed` function (for a given translation unit only) by way of an input dependency check algorithm on all the input dependencies;
- handles the provided resource-identifying `string_view`/`u8string_view`/`wstring_view` in an implementation-defined manner;
- first finds the file (and if not throws a `file_not_found_error`), then checks if it matches an available `#depend` clause (and if not throws a `dependency_error`);
- retrieves the data as-if using `std::fgetc` in a loop on a file opened at constant expression time;
- fills the data in appropriately in a static, non-unique array, discarding `offset` elements and providing a view up to a the optional `limit`;
- and, returns the specified `constexpr span` representing either the bytes of the resource or the bytes view as the type `T`.

The wording also explicitly disallows the usage of the function outside of a core constant expression by marking it `consteval`, meaning it is ill-formed if it is attempted to be used at not-constexpr time (`std::embed` calls should not show up as a function in the final executable or in generated code). The program may pin the data returned by `std::embed` through the span into the executable if it is used outside a core constant expression.

For `#depend`, the purpose is to provide an implementation-defined set of search paths that get used only for `std::embed` later. This makes the specification lighter than generally anticipated. Because `#depend` is private to any given module, we simply do not touch the existing specification and thusly the preprocessor directive remains private in its effects. We explicitly do not add it to the wording around macro imports or *pp-imports*.

### 7.2. Proposed Feature Test Macro

The proposed feature test macros are `__cpp_lib_embed` for the library and `__cpp_pp_depend` for the preprocessor functionality.

### 7.3. Proposed Wording

#### 7.3.1. Modify "§6.8.2 Object Model [**intro.object**]" one additional entry to the "... potentially non-unique object ..." list.

> ...
> 
> An object is a potentially non-unique object if it is
> 
> - a string literal object (5.13.5 [[lex.string](https://eel.is/c++draft/lex.string)]),
> - the backing array of an initializer list (9.5.4 [[dcl.init.ref](https://eel.is/c++draft/dcl.init.ref)]), or
> - <ins>the backing array pointed to by the returned value from a `embed` call (17.✨.1 [support.res.embed]), or</ins>
> - a template parameter object of array type (21.4.3 [[meta.define.static](https://eel.is/c++draft/meta.define.static)]), or
> - a subobject thereof.
> 
> ...

#### 7.3.2. Modify "§15.1 Preamble [**cpp.pre**]" to add to the syntax

> ...
> 
> *control-line:*
> 
> : `# include` *pp-tokens* *new-line*
> : *pp-import*
> : `# embed` *pp-tokens* *new-line*
> : <ins>`# depend` *pp-tokens* *new-line*</ins>
> : `# define` *identifier* *replacement-list* *new-line*
> : `# define` *identifier* *lparen* *identifier-list*<sub>*opt*</sub> `)` *replacement-list* *new-line*
> : `# define` *identifier* *lparen* `...` `)` *replacement-list* *new-line*
> : `# define` *identifier* *lparen* *identifier-list* `,` `...` `)` *replacement-list* *new-line*
> : `# undef` *identifier* *new-line*
> : *line-directive*
> : `# error` *pp-tokens*<sub>*opt*</sub> *new-line*
> : `# warning` *pp-tokens*<sub>*opt*</sub> *new-line*
> : `# pragma` *pp-tokens*<sub>*opt*</sub> *new-line*
> : `#` *new-line*
> 
> ...

#### 7.3.3. Append to "§15.12 Predefined macro names [**cpp.predefined**]" one additional entry

> 
> #define __cpp_pp_depend     ????? /* 📝 NOTE: EDITOR VALUE HERE */
> 
> 

#### 7.3.4. Add a new section "§15.5 Dependency [**cpp.depend**]"

> **15.5 Dependency** [**cpp.depend**]
> 
> A `#depend` directive provides a dependency pattern to be used for performing input dependency checks. A *dependency patterns* is a sequence of Unicode code points. *Input depedencies* are the collection of dependency patterns accumulated by `#depend` directives throughout a translation unit.
> 
> A preprocessing directive of the form
> 
> : `#` `depend` *header-name* *new-line*
> 
> adds a dependency pattern to the input dependencies. After removal of the surrounding paired `"` (U+0022 QUOTATION MARK), or paired `<` (U+003C LESS-THAN SIGN) and `>` (U+003D GREATER-THAN SIGN), the mapping of the rest of a *header-name* to the sequence of Unicode code points representing the dependency pattern is implementation-defined.
> 
> A preprocessing directive of the form
> 
> : `# depend` *pp-tokens* *new-line*
> 
> (that does not match the previous form) is permitted. The preprocessing tokens after `depend` in the directive are processed just as in normal text (i.e., each identifier currently defined as a macro name is replaced by its replacement list of preprocessing tokens). The resulting sequence of preprocessing tokens shall be of the form
> 
> : *header-name-tokens*
> 
> An attempt is then made to form a header-name preprocessing token ([lex.header]) from the whitespace and the characters of the spellings of the header-name-tokens; the treatment of whitespace is implementation-defined. If the attempt succeeds, the directive with the so-formed header-name is processed as specified for the previous form. Otherwise, the program is ill-formed, no diagnostic required.
> 
> [*Note*: Adjacent *string-literals* are not concatenated into a single *string-literal* (see the translation phases in [[lex.phases](https://eel.is/c++draft/lex.phases)]); thus, an expansion that results in two *string-literals* is an invalid directive. — *end note*]
> 
> An *input dependency check* takes an input that is a sequence of Unicode code points and yields either success or failure according to the following. To start, an implementation may perform any implementation-defined checks and yield either success or failure. If the checks yield neither, then the following matching algorithm is used. For each dependency pattern, its sequence of Unicode code points is converted to an Standard Ecma 262 (called ECMA-262 in this clause) regular expression pattern (see ECMA-262 subclause 15.10) in the following way.
> 
> First, the ECMA-262 regular expression *CharacterClass* of `^(*path-separators-or-root*)?` (U+0053 CIRCUMFLEX ACCENTS, U+0028 LEFT PARENTHESIS, *path-separators-or-root*, U+0029 RIGHT PARENTHESIS, U+003F QUESTION MARK) is added to the front of the regular expression, where *path-separators-or-root* are the appropriate ECMA-262 regular expression *ClassAtoms* for a slash (U+002F SOLIDUS), a backslash (U+005C REVERSE SOLIDUS), and any other corresponding implementation-defined directory-separator or root-name ([[fs.path.generic](https://eel.is/c++draft/fs.path.generic)]).
> 
> Then, for each Unicode code point in the dependency pattern:
> 
> - If it is a `*` (U+002A ASTERISK) and:
>   - if it is followed by another `*` (U+002A ASTERISK), then the two asterisks are replaced by the ECMA-262 regular expression *Term* `.*` (U+002E FULL STOP, U+002A ASTERISK).
>   - Otherwise, if it not followed by another `*` (U+002A ASTERISK), then the single asterisk is replaced by the ECMA-262 regular expression *CharacterClass* of `[^*path-separators*]*` (U+005B LEFT SQUARE BRACKET, U+005E CIRCUMFLEX ACCENT, *path-separators*, U+005D RIGHT SQUARE BRACKET, U+002A ASTERISK), where *path-separators* are the appropriate ECMA-262 regular expression *ClassAtoms* for a slash (U+002F SOLIDUS), a backslash (U+005C REVERSE SOLIDUS), and any other corresponding implementation-defined directory-separator or root-name ([[fs.path.generic](https://eel.is/c++draft/fs.path.generic)]).
> - Otherwise, it is replaced by an appropriate ECMA-262 regular expression *Atom* representing the Unicode code point of the sequence.
> 
> Finally, the ECMA-262 regular expression *CharacterClass* `$` (U+0024 DOLLAR SIGN) is appended to the pattern.
> 
> [ *Note—* The *ClassAtom* and *Atom* placed into these regular expressions representing a plain Unicode code point appropriately escapes any Unicode code point that would otherwise be interpreted as non-*ClassAtom* or non-*Atom* in the overall regular expression. *— end Note* ]
> 
> The input is then matched against the constructed ECMA-262 regular expression representing the dependency pattern using the algorithm specified in ECMA-262 15.10. If the input matches the converted dependency pattern, then the input dependency check yields success. Otherwise, the input is checked against the next dependency pattern in the manner previously described. If all dependency patterns in the input dependencies are checked against the input and none yield success, the implementation may perform any additional implementation-defined checks against the input and if they succeed, then the input dependency check yields success. Otherwise, input dependency check yields failure.
> 
> *Recommended practice*: Implementations should use the input dependencies to inform the potential cache of state for the translation environment when it is beneficial, such as for proper replication of such an environment for translation of programs in a non-local enrivonment.
> 
> The implementation-defined checks in the input dependency check algorithm allows for culling inputs an implementation does not wish to provide to a program. Conversely, it also allows for implementation-defined inputs to be marked as successful where warranted or desired.

#### 7.3.5. Append to §17.1 General [**support.general**]'s **Table 38** one additional entry

> |  | Subclause | Header(s) |
> | --- | --- | --- |
> |  | ... | ... |
> | <ins>17.✨</ins> | <ins>Resources</ins> | <ins><embed></ins> |

#### 7.3.6. Append to §17.3.1 General [**support.limits.general**]'s one additional entry

> 
> #define __cpp_lib_embed     ????? /* 📝 NOTE: EDITOR VALUE HERE */
> 
> 

#### 7.3.7. Add a new section "§17.✨ Constant Evaluation Resources [**support.res**]" in "§17 Language support [**support**]"

> **17.✨ Constant Evaluation Resources** [**support.res**]
> 
> **17.✨.1** Header `<embed>` synopsis [**support.embed.syn**]
> 
> ```cpp
> #include <string_view>  // see [string_view.syn]
> 
> namespace std {
>   class file_not_found_error;
> 
>   class dependency_error;
> 
>   template<class T = byte>
>   consteval span<const T> embed(string_view resource_identifier,
>     size_t offset           = 0,
>     optional<size_t> limit  = nullopt) noexcept;
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(string_view resource_identifier,
>     size_t offset = 0) noexcept;
> 
>   template<class T = byte>
>   consteval span<const T> embed(wstring_view resource_identifier,
>     size_t offset           = 0,
>     optional<size_t> limit  = nullopt) noexcept;
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(wstring_view resource_identifier,
>     size_t offset = 0) noexcept;
> 
>   template<class T = byte>
>   consteval span<const T> embed(u8string_view resource_identifier,
>     size_t offset          = 0,
>     optional<size_t> limit = nullopt) noexcept;
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(u8string_view resource_identifier,
>     size_t offset = 0) noexcept;
> }
> ```
> 
> **17.✨.2** class `file_not_found_error` [**support.file_not_found_error**]
> 
> ```cpp
> class file_not_found_error : public std::exception
> {
> private:
>   optional<string> what_;   // exposition only
>   u8string u8what_;         // exposition only
>   source_location where_;   // exposition only
> 
> public:
>   consteval file_not_found_error(u8string_view what,
>     source_location where = source_location::current()) noexcept;
> 
>   consteval file_not_found_error(string_view what,
>     source_location where = source_location::current()) noexcept;
> 
>   file_not_found_error(const file_not_found_error&) = default;
>   file_not_found_error(file_not_found_error&&) = default;
> 
>   file_not_found_error& operator=(const file_not_found_error&) = default;
>   file_not_found_error& operator=(file_not_found_error&&) = default;
> 
>   constexpr const char* what() const noexcept override;
>   consteval u8string_view u8what() const noexcept;
>   consteval source_location where() const noexcept;
> };
> ```
> 
> The function template `embed` throw exceptions of type `file_not_found_error` to signal a failure to find a file. `file_not_found_error` is a consteval-only type.
> 
> ```cpp
> consteval file_not_found_error(u8string_view what) noexcept;
> ```
> 
> *Effects*: Initializes `u8what_` with `what`, `from_` with `from` and `where_` with `where`. If `what` can be represented in the ordinary literal encoding, initializes `what_` with `what`, transcoded from UTF-8 to the ordinary literal encoding. Otherwise, `what_` is value-initialized.
> 
> ```cpp
> consteval file_not_found_error(string_view what,
>   source_location where = source_location::current()) noexcept;
> ```
> 
> *Constant When*: `what` designates a sequence of characters that can be encoded in UTF-8.
> 
> *Effects*: Initializes `what_` with `what`, `u8what_` with `what` transcoded from the ordinary literal encoding to UTF-8, `from_` with `from` and `where_` with `where`.
> 
> ```cpp
> constexpr const char* what() const noexcept override;
> ```
> 
> Constant When: `what_.has_value()` is true.
> 
> *Returns*: `what_->c_str()`.
> 
> ```cpp
> consteval u8string_view u8what() const noexcept;
> ```
> 
> *Returns*: `u8what_`.
> 
> ```cpp
> consteval source_location where() const noexcept;
> ```
> 
> *Returns*: `where_`.
> 
> **17.✨.3** class `dependency_error` [**support.dependency_error**]
> 
> ```cpp
> class dependency_error : public std::exception
> {
> private:
>   optional<string> what_;   // exposition only
>   u8string u8what_;         // exposition only
>   source_location where_;   // exposition only
> 
> public:
>   consteval dependency_error(u8string_view what,
>     source_location where = source_location::current()) noexcept;
> 
>   consteval dependency_error(string_view what,
>     source_location where = source_location::current()) noexcept;
> 
>   dependency_error(const dependency_error&) = default;
>   dependency_error(dependency_error&&) = default;
> 
>   dependency_error& operator=(const dependency_error&) = default;
>   dependency_error& operator=(dependency_error&&) = default;
> 
>   constexpr const char* what() const noexcept override;
>   consteval u8string_view u8what() const noexcept;
>   consteval source_location where() const noexcept;
> };
> ```
> 
> The function template `embed` throw exceptions of type `dependency_error` to signal a failure to depend on a file, even if it a quote resource search. `dependency_error` is a consteval-only type.
> 
> ```cpp
> consteval dependency_error(u8string_view what) noexcept;
> ```
> 
> *Effects*: Initializes `u8what_` with `what`, `from_` with `from` and `where_` with `where`. If `what` can be represented in the ordinary literal encoding, initializes `what_` with `what`, transcoded from UTF-8 to the ordinary literal encoding. Otherwise, `what_` is value-initialized.
> 
> ```cpp
> consteval dependency_error(string_view what,
>   source_location where = source_location::current()) noexcept;
> ```
> 
> *Constant When*: `what` designates a sequence of characters that can be encoded in UTF-8.
> 
> *Effects*: Initializes `what_` with `what`, `u8what_` with `what` transcoded from the ordinary literal encoding to UTF-8, `from_` with `from` and `where_` with `where`.
> 
> ```cpp
> constexpr const char* what() const noexcept override;
> ```
> 
> Constant When: `what_.has_value()` is true.
> 
> *Returns*: `what_->c_str()`.
> 
> ```cpp
> consteval u8string_view u8what() const noexcept;
> ```
> 
> *Returns*: `u8what_`.
> 
> ```cpp
> consteval source_location where() const noexcept;
> ```
> 
> *Returns*: `where_`.
> 
> **17.✨.4** Function template `embed` [**support.embed**]
> 
> ```cpp
> namespace std {
>   template<class T = byte>
>   consteval span<const T> embed(string_view resource_identifier,
>     size_t offset          = 0,
>     optional<size_t> limit = nullopt);
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(string_view resource_identifier,
>     size_t offset = 0);
> 
>   template<class T = byte>
>   consteval span<const T> embed(wstring_view resource_identifier,
>     size_t offset          = 0,
>     optional<size_t> limit = nullopt);
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(wstring_view resource_identifier,
>     size_t offset = 0);
> 
>   template<class T = byte>
>   consteval span<const T> embed(u8string_view resource_identifier,
>     size_t offset          = 0,
>     optional<size_t> limit = nullopt);
> 
>   template<size_t N, class T = byte>
>   consteval span<const T, N> embed(u8string_view resource_identifier,
>     size_t offset = 0);
> }
> ```
> 
> The sequence of characters represented by `resource_identifier` is used to perform a quote resource search for a resource (15.4 [[cpp.embed](https://eel.is/c++draft/cpp.embed)]). The conversion of the sequence of characters represented by `resource_identifier` to an appropriate sequence of characters for a quote resource search is implementation-defined. The mapping of the sequence of characters represented by `resource_identifier` to an appropriate sequence of Unicode code points for use with the input dependency check is implementation-defined.
> 
> Let *implementation-resource-width* be the implementation-defined width of the resource. Let *implementation-resource-count* be `implementation-resource-width / CHAR_BIT`. Let *resource-offset* be min(offset,implementation-resource-count).
> 
> Let *resource-limit* be:
> 
> - `limit` if an overload with the `limit` parameter is used.
> - `N` if an overload with the template parameter `N` is used.
> - Otherwise, implementation-resource-count.
> 
> Let *resource-count* be max(0,min(implementation-resource−count − resource−offset,resource−limit)).
> 
> *Mandates:*
> 
> - `T` is one of `byte`, `char`, or `unsigned char`.
> - If an overload with the template parameter `N` is used, then resource-count is at least `N`.
> - Implementation-resource-width is an integral multiple of `CHAR_BIT`.
> 
> *Throws:*
> 
> - `file_not_found_error` with an implementation-defined set of arguments if the implementation cannot find the resource identified by the `resource_identifier` after a quote resource search.
> - Otherwise, `dependency_error` with an implementation-defined set of arguments if the implementation finds the resource specified but that same resource’s `resource_identifier` fails an input dependency check (15.5 [cpp.depend]).
> 
> *Returns:* A `span<const T, N>(p, s)` for overloads with the template parameter `N`, otherwise a `span<const T>(p, s)`, where
> 
> - `s` is resource-count.
> - `p` is a pointer to an element in an array of `const T` that has static storage duration and `p + s` points to either one past the end of said array or somewhere within said array.
> 
> *Effects:* Each object of type `const T` in the contiguous sequence represented by the returned value has a value as-if initialized by the reading of the resource in a manner similar to the `#embed` directive (15.4 [[cpp.embed](https://eel.is/c++draft/cpp.embed)]), except at constant evaluation time. The contiguous sequence is backed by an array of type "array of at least `resource-count` `const T`". [ *Note—* If `T` is `char` and `is_signed_v<char>` is true, then each `char`’s value, if any, is the unsigned value converted by a static cast to `char`. *— end Note* ]
> 
> *Remarks:* A `std::embed` call considers the input dependencies of the translation unit where the call lexically appears. If any `#depend` appears after where a `std::embed` call lexically appears, it is implementation-defined whether or not any of those `#depend` directives’s patterns contribute to the input dependencies.
> 
> *Recommended Practice*: Implementations should use the same search paths from `#embed` (15.4 [[cpp.embed](https://eel.is/c++draft/cpp.embed)]) for `std::embed`. The contiguous sequence of `const T` represented by the returned span should closely represent the bit stream of the *resource* unmodified. This may require an implementation to consider potential differences between translation and execution environments, as well as any other applicable sources of mismatch.
> 
> The implementation-defined conversion of the `resource_identifier` to an appropriate sequence of characters to both search for the resource and perform the input dependency check allows for robust checking of resource names identified by the quote research source. Consider a translation unit which contains a `#depend "cats/**"` directive and a `std::embed("cats/../../etc/uwu/private_secrets")` invocation. An implementation can use the implementation-defined checks built into the input dependency check to perform two checks intead of just one:
> 
> - first, check a straightforward interpretation of the `resource_identifier` representing `"cats/../../etc/uwu/private_secrets"` against the `^(/)?cats\/.*` ECMA-262 regular experession. (This check would succeed.)
> - Then, check the so-called "resolved path name" of the found resource -- i.e. `"/etc/uwu/private_secrets"` -- against the same `^(/)?cats\/.*`. (This check would fail.)
> 
> Such an implementation can address a wide variety of quote resource search-discovered files on a wide variety of program translation environments.
> 
> [*Example*: It is recommended that `#embed` and `std::embed` rely on the same implementation-defined search for their quote resource search.
> 
> ```cpp
> #include <embed>
> #include <algorithm>
> #include <span> // just for std::size
> 
> #depend "data.dat"
> 
> constexpr std::span<const unsigned char> x = std::embed<unsigned char>("data.dat");
> constexpr const unsigned char x2[] = {
> #embed "data.dat" // same data
> };
> 
> static_assert(x.size() == std::size(x2));
> static_assert(std::equal(x.data(), x.size(), &x2[0]));
> ```
> 
> — *end example*]
> 
> [*Example*: A `#depend` directive can come lexically after a `std::embed` call, as it is processed in an earlier phase of translation, but whether or not the `std::embed` call succeeds without throwing an error is conditionally supported.
> 
> ```cpp
> #include <embed>
> 
> constexpr const auto a = std::embed("sdk/jump.wav"); // conditionally supported
> #depend <sdk/​*>
> constexpr const auto b = std::embed("sdk/jump.wav"); // ok
> ```
> 
> — *end Example*]
> 
> [*Example*: All *resources* must be depended on first, irregardless of the implementation’s ability to find the identified *resource* without it:
> 
> ```cpp
> #include <embed>
> 
> constexpr auto data = std::embed("oh.no"); // ill-formed,
>                                            // fails the input dependency check
>                                            // (and throws a dependency_error)
> ```
> 
> — *end Example*]

## 3 Existing Standard UTF Interfaces in C and C++

### 3.1 C

C contains an alphabet soup of transcoding functions in `<stdlib.h>`, `<wchar.h>`, and `<uchar.h>`. [[Null-terminated multibyte strings]](https://en.cppreference.com/w/c/string/multibyte.html)

This paper doesn’t fully litigate these functions’ flaws (see WG14 [[N2902]](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n2902.htm) for a more detailed explanation). Some of the issues users encounter include reliance on an internal global conversion state, reliance on the current setting of the global C locale, optimization barriers in one-code-unit-at-a-time function calls, and inadequate error handling that does not support replacement of invalid subsequences with � as specified by Unicode.

[Example](https://godbolt.org/z/hrv78oKqo):

```c
setlocale(LC_ALL, "en_US.utf8");
char c[5] = {0};
const char16_t* w = u"\xd83d\xdd74";
mbstate_t state;
memset(&state, 0, sizeof(state));
c16rtomb(c, w[0], &state);
c16rtomb(c, w[1], &state);
const char* e = "\xf0\x9f\x95\xb4";
assert(strcmp(c, e) == 0);
```

### 3.2 C++

C++’s existing transcoding functionality, other than the aforementioned functions it inherits from C, consists of the set of `std::codecvt` facets provided in `<locale>` and `<codecvt>`.

[Example](https://godbolt.org/z/Yncfqeesa):

```cpp
std::wstring_convert<std::codecvt_utf8<char32_t>, char32_t> conv;
std::string c = conv.to_bytes(U"🙂");
assert(c == "\xf0\x9f\x99\x82");
```

All of the Unicode-specific functionality in this header was deprecated in C++17, and [[P2871R3]](https://wg21.link/p2871r3) and [[P2873R2]](https://wg21.link/p2873r2) finally remove most of it in C++26. There are many concerns about these interfaces, particularly with respect to safety.

These functions throw exceptions on encountering invalid UTF. Unicode functions that use exceptions for error handling are a well-known footgun because users consistently invoke them on untrusted user input without handling the exceptions properly, leading to denial-of-service vulnerabilities.

An example of this anti-pattern (although not involving these specific functions) can be found in [[CVE-2007-3917]](https://nvd.nist.gov/vuln/detail/CVE-2007-3917), where a multiplayer RPG server could be crashed by malicious users sending invalid UTF. Below is the patch: [[wesnoth]](https://github.com/wesnoth/wesnoth/commit/c5bc4e2a915ddf53b63f292f587526aaa39a96aa)

```cpp
- msg = font::word_wrap_text(msg,font::SIZE_SMALL,map_outside_area().w*3/4);
+ try {
+     // We've had a joker who send an invalid utf-8 message to crash clients
+     // so now catch the exception and ignore the message.
+     msg = font::word_wrap_text(msg,font::SIZE_SMALL,map_outside_area().w*3/4);
+ } catch (utils::invalid_utf8_exception&) {
+     LOG_STREAM(err, engine) << "Invalid utf-8 found, chat message is ignored.\n";
+     return;
+ }
```

Because it doesn’t use exceptions, the functionality proposed by this paper can serve as a safe, modern replacement for the deprecated and removed `codecvt` facets.


## 4 Replacing Ill-Formed Subsequences with “�”

When a transcoder encounters an invalid subsequence, the modern best practice is to replace it in the output with one or more � characters (`U+FFFD`, `REPLACEMENT CHARACTER`). The methodology for doing so is described in §3.9.6 of the Unicode Standard v17.0, Substitution of Maximal Subparts [[Substitution]](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G66453).

For UTF-32 and UTF-16, each invalid code unit is replaced by an individual � character.

For UTF-8, the same rule applies except if “a sequence of two or three bytes is a truncated version of a sequence which is otherwise well-formed to that point.” In the latter case, the full two-to-three byte subsequence is replaced by a single � character.

For example, UTF-8 encodes 🙂 as `0xF0` `0x9F` `0x99` `0x82`.

If that sequence of bytes is truncated to just `0xF0` `0x9F` `0x99`, it becomes a single � replacement character.

On the other hand, if the first byte of the four-byte sequence is changed from `0xF0` to `0xFF`, then it’s replaced by four replacement characters, ����, because no valid UTF-8 subsequence begins with `0xFF`.

More subtly, the subsequence `0xED` `0xA0` must be replaced with two replacement characters, ��, because any continuation of that subsequence can only result in a surrogate code point, so it can’t prefix any valid subsequence.

Each of the proposed `to_utfN_view` views adheres to this specification. The `to_utfN_as_error` views also use this scheme but produce `unexpected<utf_transcoding_error>` values instead of replacement characters.

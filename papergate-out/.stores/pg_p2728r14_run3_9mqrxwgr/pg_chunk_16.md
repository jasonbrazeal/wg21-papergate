
The `to_utf_view::*iterator*` is converting the string `Qϕ学𡪇` from UTF-8 to UTF-16. The user has iterated the view to the first UTF-16 code unit of the fourth character. `current_` points to the start of the fourth character in the input. `buf_` contains both UTF-16 code units of the fourth character; `buf_index_` keeps track of the fact that we’re currently pointing to the first one. If we invoke `operator++` on the `to_utf_view::*iterator*`, it will increment `buf_index_` to point to the second code unit. On the other hand, if we invoke `operator--`, it will notice that `buf_index_` is already at the beginning and move backward from the fourth character to the third character by invoking `*read-reverse*()`. The `*read*()` and `*read-reverse*()` functions contain most of the actual transcoding logic, updating `current_` and filling `buf_` up with the transcoded characters.

(The diagram depicts the minimal buffer, holding one character at a time. As described above, an implementation may instead fill `buf_` with the code units of several consecutive characters when the underlying range is multipass.)

Iterating a bidirectional transcoding view backwards produces, in reverse order, the exact same sequence of characters or `expected` values as are produced by iterating the view forwards.

#### 5.1.1 `utf_transcoding_error`

Each transcoding view, like `to_utf8_view`, which produces a range of `char8_t` and handles errors by substituting � replacement characters, has a corresponding `_or_error` equivalent, like `to_utf8_view_or_error`, which produces a range of `expected<char8_t, utf_transcoding_error>` and handles errors by substituting `unexpected<utf_transcoding_error>`s.

`utf_transcoding_error` is an enumeration whose enumerators are:

- `truncated_utf8_sequence`
  - An ill-formed subsequence that matches the beginning of some well-formed sequence.
  - Example invalid code unit sequence: UTF-8 `0xE1 0x80`.
- `unpaired_high_surrogate`
  - Example invalid code unit sequence: UTF-16 `0xD800`.
- `unpaired_low_surrogate`
  - Example invalid code unit sequence: UTF-16 `0xDC00`.
- `unexpected_utf8_continuation_byte`
  - Example invalid code unit sequence: UTF-8 `0x80`.
- `overlong`
  - An overlong UTF-8 encoding.
  - Example invalid code unit sequence: UTF-8 `0xE0 0x80`.
- `encoded_surrogate`
  - Applies to both UTF-8 and UTF-32.
  - Example invalid code unit sequence: UTF-8 `0xED 0xA0`, UTF-32 `0x0000D800`.
- `out_of_range`
  - Applies to both UTF-8 and UTF-32
  - In UTF-8, this applies to `0xF4` if it is followed by a continuation byte greater than `0x8F`
  - In UTF-32, this is any code unit greater than `0x10FFFF`
  - Example invalid code unit sequence: UTF-8 `0xF4 0x90`, UTF-32 `0x110000`.
- `invalid_utf8_leading_byte`
  - In UTF-8, this applies to `0xC0`-`0xC1` and `0xF5`-`0xFF`.
  - Example invalid code unit sequence: UTF-8 `0xC0`.

An alternative approach to minimize the number of enumerators could merge `truncated_utf8_sequence` with `unpaired_high_surrogate` and merge `unexpected_utf8_continuation_byte` with `unpaired_low_surrogate`, but based on feedback, splitting these up seems to be preferred.

The table below compares the error handling behavior of the `to_utf16` and `to_utf16_or_error` views on various sample UTF-8 inputs from the “Substitution of Maximal Subparts” section of the Unicode standard: [[SubstitutionExamples]](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G67519)

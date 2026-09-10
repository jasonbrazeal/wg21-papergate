## 6 Additional Examples

### 6.1 Transcoding a UTF-8 String Literal to a `std::u32string`

```cpp
std::u32string hello_world =
  u8"こんにちは世界"sv | std::views::to_utf32 | std::ranges::to<std::u32string>();
```

### 6.2 Sanitizing Potentially Invalid Unicode

Note that transcoding to and from the same encoding is not a no-op; it must maintain the invariant that the output of a transcoding view is always valid UTF.

```cpp
template <typename CharT>
std::basic_string<CharT> sanitize(CharT const* str) {
  return std::null_term(str) | std::views::to_utf<CharT> | std::ranges::to<std::basic_string<CharT>>();
}
```

### 6.3 Returning the Final Non-ASCII Code Point in a String, Transcoding Backwards Lazily

```cpp
std::optional<char32_t> last_nonascii(std::ranges::view auto str) {
  for (auto c : str | std::views::to_utf32 | std::views::reverse
                    | std::views::filter([](char32_t c) { return c > 0x7f; })) {
    return c;
  }
  return std::nullopt;
}
```

### 6.4 Transcoding Strings and Throwing a Descriptive Exception on Invalid UTF

(This assumes a reflection-based `enum_to_string` function.)

```cpp
template <typename FromChar, typename ToChar>
std::basic_string<ToChar> transcode_or_throw(std::basic_string_view<FromChar> input) {
  std::basic_string<ToChar> result;
  auto view = input | std::views::to_utf_or_error<ToChar>;
  for (auto it = view.begin(), end = view.end(); it != end; ++it) {
    if ((*it).has_value()) {
      result.push_back(**it);
    } else {
      throw std::runtime_error("error at position " +
                               std::to_string(it.base() - input.begin()) + ": " +
                               enum_to_string((*it).error()));
    }
  }
  return result;
}
```

```cpp
  // prints: "error at position 2: truncated_utf8_sequence"
  transcode_or_throw<char8_t, char16_t>(
    u8"hi🙂"sv | std::views::take(5) | std::ranges::to<std::u8string>());
```

### 6.5 Changing the Suits of Unicode Playing Card Characters

```cpp
enum class suit : std::uint8_t {
  spades = 0xA,
  hearts = 0xB,
  diamonds = 0xC,
  clubs = 0xD
};

// Unicode playing card characters are laid out such that changing the second least
// significant nibble changes the suit, e.g.
// U+1F0A1 PLAYING CARD ACE OF SPADES
// U+1F0B1 PLAYING CARD ACE OF HEARTS
constexpr char32_t change_playing_card_suit(char32_t card, suit s) {
  if (U'\N{PLAYING CARD ACE OF SPADES}' <= card && card <= U'\N{PLAYING CARD KING OF CLUBS}') {
    return (card & ~(0xF << 4)) | (static_cast<std::uint8_t>(s) << 4);
  }
  return card;
}

void change_playing_card_suits() {
  std::u8string_view const spades = u8"🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮";
  std::u8string const hearts =
    spades |
    to_utf32 |
    std::views::transform(std::bind_back(change_playing_card_suit, suit::hearts)) |
    to_utf8 |
    std::ranges::to<std::u8string>();
  assert(hearts == u8"🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾");
}
```

### 6.6 Handling Byte Offsets and Endianness

Say we want to handle a set of bytes in a message starting at offset N with length K that is UTF16BE text:

```cpp
std::u8string parse_message_subset(
    std::span<std::byte> message, std::size_t offset, std::size_t length) {
  return std::span{message.begin() + offset, message.begin() + offset + length}
         | std::views::chunk(2)
         | std::views::transform(
             [](const auto chunk) {
               std::array<std::byte, 2> a{};
               std::ranges::copy(chunk, a.begin());
               return std::bit_cast<std::uint16_t>(a);
             })
         | std::views::from_big_endian
         | std::views::as_char16_t
         | std::views::to_utf8
         | std::ranges::to<std::u8string>();
}
```

Note that this depends on P4030R0 “Endian Views” for `std::views::from_big_endian`.

### 6.7 Transcoding into a buffer of a fixed number of code units without truncating code points

```cpp
template <typename T>
constexpr bool is_continuation(T c) {
  if constexpr (std::is_same_v<decltype(c), char8_t>) {
    return (c & 0xC0) == 0x80;
  } else if constexpr (std::is_same_v<decltype(c), char16_t>) {
    return c >= 0xDC00 && c <= 0xDFFF;
  } else {
    return false;
  }
}

template <typename FromType, typename ToType, std::size_t N>
constexpr std::inplace_vector<ToType, N> transcode_truncating_correctly(
    std::basic_string_view<FromType> input) {
  std::inplace_vector<ToType, N> output;
  for (auto code_point_view : input
       | std::views::to_utf<ToType>
       | std::views::chunk_by([](auto, auto b) { return is_continuation(b); })) {
    if (std::ranges::distance(code_point_view)
        > static_cast<std::ptrdiff_t>(output.max_size() - output.size()))
      break;
    std::ranges::copy(code_point_view, std::back_insert_iterator{output});
  }
  return output;
}
```

### 6.8 Performing code unit substitutions on cuneiform strings

```cpp
// Adapted from an ICU unit test:
// https://github.com/unicode-org/icu/blob/649262a75ecddb15a0e58d71f637a8a32eaabd43/icu4c/source/test/intltest/utfiteratortest.cpp#L1205-L1228
std::u16string zamin = u"𒀭𒎏𒄈𒋢𒍠𒊩";
auto view = zamin | std::views::to_utf32;
auto it = view.begin();
++it;
auto ningirsuBegin = it.base();
std::advance(it, 3);
auto ningirsuEnd = it.base();
zamin.replace(ningirsuBegin, ningirsuEnd, u"𒊺𒉀");
assert(std::ranges::equal(zamin, u"𒀭𒊺𒉀𒍠𒊩"sv));
```


## 7 Dependencies

The code unit views depend on [[P3117R1]](https://wg21.link/p3117r1) “Extending Conditionally Borrowed”.


## 8 Implementation Experience

The most recent revision of this paper has a reference implementation called [beman.utf_view](https://github.com/bemanproject/utf_view) available on GitHub, which is a fork of Jonathan Wakely’s implementation of P2728R6 as an implementation detail for libstdc++. It is part of the Beman project.

Versions of the interfaces provided by previous revisions of this paper have also been implemented, and re-implemented, several times over the last 5 years or so, as part of a proposed (but not yet accepted!) Boost library, [Boost.Text](https://github.com/tzlaine/text). Boost.Text has hundreds of stars on GitHub.

Both libraries have comprehensive tests.

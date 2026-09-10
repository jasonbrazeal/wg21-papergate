## 9 Wording

### 9.1 Additional Helper Concepts

Add the following to 25.5.2 [[range.utility.helpers]](https://wg21.link/range.utility.helpers):

```cpp
  template<class T>
    concept code-unit =
      same_as<remove_cv_t<T>, char8_t> || same_as<remove_cv_t<T>, char16_t> || same_as<remove_cv_t<T>, char32_t>;
```

### 9.2 Header `<ranges>` synopsis

Add the following to 25.2 [[ranges.syn]](https://wg21.link/ranges.syn), after the `as_input_view` entries:

```cpp
  // [range.transcoding], transcoding views
  enum class utf_transcoding_error : unspecified;
  enum class to_utf_view_error_kind : unspecified;

  template<code-unit ToType>
  struct to_utf_tag_t;

  template<code-unit ToType>
  constexpr to_utf_tag_t<ToType> to_utf_tag{};

  using to_utf8_tag_t = to_utf_tag_t<char8_t>;
  constexpr to_utf8_tag_t to_utf8_tag{};

  using to_utf16_tag_t = to_utf_tag_t<char16_t>;
  constexpr to_utf16_tag_t to_utf16_tag{};

  using to_utf32_tag_t = to_utf_tag_t<char32_t>;
  constexpr to_utf32_tag_t to_utf32_tag{};

  template<input_range V, to_utf_view_error_kind E, code-unit ToType>
    requires view<V> && code-unit<range_value_t<V>>
  class to_utf_view;

  template<class V, to_utf_view_error_kind E, class ToType>
    constexpr bool enable_borrowed_range<to_utf_view<V, E, ToType>> =
      enable_borrowed_range<V>;

  namespace views {
    template<code-unit ToType> inline constexpr unspecified to_utf = unspecified;
    template<code-unit ToType> inline constexpr unspecified to_utf_or_error = unspecified;
    inline constexpr unspecified to_utf8 = unspecified;
    inline constexpr unspecified to_utf8_or_error = unspecified;
    inline constexpr unspecified to_utf16 = unspecified;
    inline constexpr unspecified to_utf16_or_error = unspecified;
    inline constexpr unspecified to_utf32 = unspecified;
    inline constexpr unspecified to_utf32_or_error = unspecified;
  }

  // [range.codeunitadaptor], code unit adaptors
  namespace views {
    inline constexpr unspecified as_char = unspecified;
    inline constexpr unspecified as_wchar_t = unspecified;
    inline constexpr unspecified as_char8_t = unspecified;
    inline constexpr unspecified as_char16_t = unspecified;
    inline constexpr unspecified as_char32_t = unspecified;
  }
```

### 9.3 Transcoding views

Add the following subclause to 25.7 [[range.adaptors]](https://wg21.link/range.adaptors):

#### 25.7.? Transcoding views [range.transcoding]

##### 25.7.?.1 Overview [range.transcoding.overview]

`to_utf_view` produces a view of the UTF code units transcoded from the elements of a `*utf-range*`. It transcodes from UTF-N to UTF-M, where N and M are each one of 8, 16, or 32. N may equal M. `to_utf_view`’s `ToType` template parameter is based on a mapping between character types and UTF encodings, which is that that `char8_t` corresponds to UTF-8, `char16_t` corresponds to UTF-16, and `char32_t` corresponds to UTF-32. If its `to_utf_view_error_kind` constant template parameter is `expected`, it produces a view of `expected<charN_t, utf_transcoding_error>` where invalid input subsequences result in errors.

The names `views::to_utf<ToType>`, `views::to_utf_or_error<ToType>`, `views::to_utf8`, `views::to_utf8_or_error`, `views::to_utf16`, `views::to_utf16_or_error`, `views::to_utf32`, and `views::to_utf32_or_error` denote range adaptor objects ([range.adaptor.object]).

`views::to_utf<ToType>` is equivalent to `views::to_utf8` if `ToType` is `char8_t`, `views::to_utf16` if `ToType` is `char16_t`, and `views::to_utf32` if `ToType` is `char32_t`, and similarly for `views::to_utf_or_error`.

Let `views::to_utfN` denote any of the aforementioned range adaptor objects, let `Char` be its corresponding character type, and let `Error` be its corresponding `to_utf_view_error_kind`. Let `E` be an expression and let `T` be `remove_cvref_t<decltype((E))>`. If `decltype((E))` does not model `*utf-range*`, or if `T` is an array of `char8_t`, `char16_t`, or `char32_t`, `to_utfN(E)` is ill-formed. Otherwise, the expression `to_utfN(E)` is expression-equivalent to:

- If `E` is a specialization of `empty_view` ([range.empty.view]):
  - If `Error` is `to_utf_view_error_kind::replacement`, then `empty_view<Char>{}`.
  - Otherwise, `empty_view<expected<Char, utf_trancoding_error>>{}`.
- Otherwise, if the type of `E` is a (possibly cv-qualified) specialization of `to_utf_view`, then `to_utf_view(E.base(), cw<Error>, to_utf_tag<Char>)`.
- Otherwise, if the type of `E` is *cv* `subrange<to_utf_view::*iterator*, to_utf_view::*iterator*, subrange_kind::unsized>` for some specialization of `to_utf_view`, then `to_utf_view(subrange(E.begin().base(), E.end().base()), cw<Error>, to_utf_tag<Char>)`.
- Otherwise, `to_utf_view(E, cw<Error>, to_utf_tag<Char>)`.

##### 25.7.?.2 Enumeration `utf_transcoding_error` [range.transcoding.error.transcoding]

```cpp
enum class utf_transcoding_error : unspecified {
  truncated_utf8_sequence,
  unpaired_high_surrogate,
  unpaired_low_surrogate,
  unexpected_utf8_continuation_byte,
  overlong,
  encoded_surrogate,
  out_of_range,
  invalid_utf8_leading_byte
};
```

##### 25.7.?.3 Enumeration `to_utf_view_error_kind` [range.transcoding.error.kind]

```cpp
enum class to_utf_view_error_kind : unspecified {
  replacement,
  expected
};
```

##### 25.7.?.4 UTF Tags [range.transcoding.tags]

```cpp
template<code-unit ToType>
struct to_utf_tag_t {
  explicit to_utf_tag_t() = default;
};

template<code-unit ToType>
constexpr to_utf_tag_t<ToType> to_utf_tag{};

using to_utf8_tag_t = to_utf_tag_t<char8_t>;

constexpr to_utf8_tag_t to_utf8_tag{};

using to_utf16_tag_t = to_utf_tag_t<char16_t>;

constexpr to_utf16_tag_t to_utf16_tag{};

using to_utf32_tag_t = to_utf_tag_t<char32_t>;

constexpr to_utf32_tag_t to_utf32_tag{};
```

##### 25.7.?.5 Class template `to_utf_view` [range.transcoding.view]

```cpp
template<input_range V, to_utf_view_error_kind E, code-unit ToType>
  requires view<V> && code-unit<range_value_t<V>>
class to_utf_view : public view_interface<to_utf_view<V, E, ToType>> {
private:
  template<bool>
  struct iterator; // exposition only
  template<bool>
  struct sentinel; // exposition only

  V base_ = V(); // exposition only

public:
  constexpr to_utf_view() requires default_initializable<V> = default;
  template <auto E2>
    constexpr explicit to_utf_view(V base, constant_wrapper<E2, to_utf_view_error_kind>, to_utf_tag_t<ToType>)
      requires (constant_wrapper<E2, to_utf_view_error_kind>::value == E);

  constexpr V base() const& requires copy_constructible<V> { return base_; }
  constexpr V base() && { return std::move(base_); }

  constexpr iterator<false> begin();
  constexpr iterator<true> begin() const requires range<const V> && ((same_as<range_value_t<V>, char32_t>) || (!forward_range<const V>))
  {
    if constexpr (bidirectional_range<const V>) {
      return iterator<true>(begin(base_), begin(base_), end(base_));
    } else {
      return iterator<true>(begin(base_), end(base_));
    }
  }

  constexpr sentinel<false> end() { return sentinel<false>(end(base_)); }
  constexpr iterator<false> end() requires common_range<V>
  {
    if constexpr (bidirectional_range<V>) {
      return iterator<false>(begin(base_), end(base_), end(base_));
    } else {
      return iterator<false>(end(base_), end(base_));
    }
  }
  constexpr sentinel<true> end() const requires range<const V>
  {
    return sentinel<true>(end(base_));
  }
  constexpr iterator<true> end() const requires common_range<const V>
  {
    if constexpr (bidirectional_range<const V>) {
      return iterator<true>(begin(base_), end(base_), end(base_));
    } else {
      return iterator<true>(end(base_), end(base_));
    }
  }

  constexpr bool empty() const { return empty(base_); }

  constexpr size_t size()
    requires sized_range<V> && same_as<char32_t, range_value_t<V>> && same_as<char32_t, ToType>
  {
    return size(base_);
  }

  constexpr auto reserve_hint() requires approximately_sized_range<V>;
  constexpr auto reserve_hint() const requires approximately_sized_range<const V>;
};

template<class R, auto E2, code-unit ToType>
  to_utf_view(R&&, constant_wrapper<E2, to_utf_view_error_kind>, to_utf_tag_t<ToType>)
    -> to_utf_view<views::all_t<R>, constant_wrapper<E2, to_utf_view_error_kind>::value, ToType>;

template <class V, to_utf_view_error_kind E, class ToType>
  inline constexpr bool enable_borrowed_range<to_utf_view<V, E, ToType>> = enable_borrowed_range<V>;
```

```cpp
template <auto E2>
  constexpr explicit to_utf_view(V base, constant_wrapper<E2, to_utf_view_error_kind>, to_utf_tag_t<ToType>)
    requires (constant_wrapper<E2, to_utf_view_error_kind>::value == E);
```

*Effects*: Initializes `*base_*` with `std::move(base)`.

```cpp
constexpr iterator begin();
```

*Returns:* `{*this, std::ranges::begin(*base_*)}`

```cpp
constexpr auto reserve_hint() requires approximately_sized_range<V>;
```

*Returns:* The result is implementation-defined.

```cpp
constexpr auto reserve_hint() const requires approximately_sized_range<const V>;
```

*Returns:* The result is implementation-defined.

> [ *Note:* The implementation of the `empty()` member function provided by the transcoding views is more efficient than the one provided by `view_interface`, since `view_interface`’s implementation will construct `to_utf_view::begin()` and `to_utf_view::end()` and compare them, whereas we can simply use the underlying range’s `empty()`, since a transcoding view is empty if and only if its underlying range is empty. — *end note* ]

##### 25.7.?.6 Class `to_utf_view::*iterator*` [range.transcoding.iterator]

```cpp
template<input_range V, to_utf_view_error_kind E, code-unit ToType>
  requires view<V> && code-unit<range_value_t<V>>
template<bool Const>
class to_utf_view<V, E, ToType>::iterator {
private:
  using Base = maybe-const<Const, V>; // exposition only

public:
  using iterator_concept = see below;
  using iterator_category = see below;  // not always present
  using value_type = conditional_t<E == to_utf_view_error_kind::expected, expected<ToType, utf_transcoding_error>, ToType>;
  using reference_type = value_type;
  using difference_type = ptrdiff_t;

private:
  iterator_t<Base> begin_{}; // exposition only, present only if
                                 //   bidirectional_range<Base> is true
  iterator_t<Base> current_{}; // exposition only
  sentinel_t<Base> end_; // exposition only

  inplace_vector<value_type, buffer-capacity> buf_{}; // exposition only

  ptrdiff_t buf_index_{}; // exposition only
  size_t to_increment_{}; // exposition only

  template<input_range V2, to_utf_view_error_kind E2, code-unit ToType2>
    requires view<V2> && code-unit<range_value_t<V2>>
  friend class to_utf_view; // exposition only

public:
  constexpr iterator() requires default_initializable<iterator_t<Base>> = default;

  constexpr iterator(iterator const&) requires copyable<iterator_t<Base>> = default;
  constexpr iterator& operator=(iterator const&) requires copyable<iterator_t<Base>> = default;
  constexpr iterator(iterator&&) = default;
  constexpr iterator& operator=(iterator&&) = default;

private:
  constexpr iterator(iterator_t<Base> begin, iterator_t<Base> current, sentinel_t<Base> end) // exposition only
    requires bidirectional_range<Base>
      : begin_(std::move(begin)), current_(std::move(current)), end_(end) {
    if (current_ != end())
      read();
  }

  constexpr iterator(iterator_t<Base> current, sentinel_t<Base> end) // exposition only
    requires (!bidirectional_range<Base>)
      : current_(std::move(current)), end_(end) {
    if (current_ != end())
      read();
    else if constexpr (!forward_range<Base>) {
      buf_index_ = -1;
    }
  }

public:
  constexpr iterator_t<Base> base() const
    requires forward_range<Base>;

  constexpr value_type operator*() const;

  constexpr iterator& operator++() requires (E == to_utf_view_error_kind::expected)
  {
    if (!success()) {
      if constexpr (is_same_v<ToType, char8_t>) {
        advance-one();
        advance-one();
      }
    }
    advance-one();
    return *this;
  }

  constexpr iterator& operator++() requires (E == to_utf_view_error_kind::replacement)
  {
    advance-one();
    return *this;
  }

  constexpr auto operator++(int) {
    if constexpr (is_same_v<iterator_concept, input_iterator_tag>) {
      ++*this;
    } else {
      auto retval = *this;
      ++*this;
      return retval;
    }
  }

  constexpr iterator& operator--() requires bidirectional_range<Base>
  {
    if (!buf_index_) {
      read-reverse();
    } else {
      --buf_index_;
      if constexpr (E == to_utf_view_error_kind::expected && is_same_v<ToType, char8_t>) {
        if (!success())
          buf_index_ -= 2;
      }
    }
    return *this;
  }

  constexpr iterator operator--(int) requires bidirectional_range<Base>
  {
    auto retval = *this;
    --*this;
    return retval;
  }

  friend constexpr bool operator==(const iterator& lhs, const iterator& rhs)
    requires equality_comparable<iterator_t<Base>>;

private:
  constexpr sentinel_t<Base> end() const { // exposition only
    return end_;
  }

  constexpr expected<void, utf_transcoding_error> success() const noexcept requires(E == to_utf_view_error_kind::expected); // exposition only

  constexpr void advance-one() // exposition only
  {
    ++buf_index_;
    if (buf_index_ == buf_.size()) {
      if constexpr (forward_range<Base>) {
        buf_index_ = 0;
        advance(current_, to_increment_);
      }
      if (current_ != end()) {
        read();
      } else if constexpr (!forward_range<Base>) {
        buf_index_ = -1;
      }
    }
  }

  constexpr void read(); // exposition only

  constexpr void read-reverse(); // exposition only
};
```

`*buffer-capacity*` is an unspecified constant that is at least `4 / sizeof(ToType)`. If `*Base*` does not model `forward_range`, `*buffer-capacity*` is `4 / sizeof(ToType)`.

> [ *Note:* A `*buffer-capacity*` greater than `4 / sizeof(ToType)` permits `*read*` to transcode several input subsequences per invocation, for example a chunk at a time using SIMD instructions. — *end note* ]

> [ *Note:* `to_utf_view::*iterator*` does its work by adapting an underlying range of code units. We use the term “input subsequence” to refer to a potentially ill-formed code unit subsequence which is to be transcoded into a code point `c`. Each input subsequence is decoded from the UTF encoding corresponding to `*from-type*`. If the underlying range contains ill-formed UTF, the code units are divided into input subsequences according to Substitution of Maximal Subparts, and each ill-formed input subsequence is transcoded into a `U+FFFD`. `c` is then encoded to `ToType`’s corresponding encoding, into an internal code unit buffer `buf_`. `buf_` may contain the transcoded code units of more than one input subsequence; the *current* input subsequence is the input subsequence whose transcoded code units include `buf_[buf_index_]`. — *end note* ]

> [ *Note:* `to_utf_view::*iterator*::base()` is only provided when the base range models `forward_range`. If `*this` is at the end of the range being adapted, then `base()` == `*end*()`. Otherwise, the position of `base()` is always at the beginning of the input subsequence corresponding to the current code point. — *end note* ]

`to_utf_view::*iterator*::iterator_concept` is defined as follows:

- If `V` models `bidirectional_range`, then `iterator_concept` is `bidirectional_iterator_tag`.
- Otherwise, if `V` models `forward_range`, then `iterator_concept` is `forward_iterator_tag`.
- Otherwise, `iterator_concept` is `input_iterator_tag`.

The member *typedef-name* `iterator_category` is defined if and only if `V` models `forward_range`.

In that case, `to_utf_view::*iterator*::iterator_category` is defined as follows:

- Let `C` denote the type `iterator_traits<iterator_t<V>>::iterator_category`.
- If `C` models `derived_from<bidirectional_iterator_tag>`, then `iterator_category` denotes `bidirectional_iterator_tag`.
- Otherwise, if `C` models `derived_from<forward_iterator_tag>`, then `iterator_category` denotes `forward_iterator_tag`.
- Otherwise, `iterator_category` denotes `C`.

```cpp
constexpr iterator_t<Base> base() const
  requires forward_range<Base>;
```

*Returns*: If `*this` is at the end of the range being adapted, an iterator equal to the end of the range being adapted. Otherwise, an iterator pointing to the first code unit of the current input subsequence.

> [ *Note:* An implementation whose `*read*` transcodes a single input subsequence per invocation can return `current_`. An implementation that transcodes several input subsequences per invocation can recompute this position from `current_` and `buf_index_`; the recomputation takes time bounded by `*buffer-capacity*`, a constant. — *end note* ]

```cpp
friend constexpr bool operator==(const iterator& lhs, const iterator& rhs)
  requires equality_comparable<iterator_t<Base>>;
```

*Returns*: If `*Base*` models `forward_range`, `true` if and only if either `lhs` and `rhs` are both at the end of the range being adapted, or the current input subsequences of `lhs` and `rhs` begin at the same position in the underlying range and `*lhs` and `*rhs` denote the code unit at the same offset within the transcoded code units of that input subsequence. Otherwise, `lhs.current_ == rhs.current_ && lhs.buf_index_ == rhs.buf_index_`.

> [ *Note:* For an implementation whose `*read*` and `*read-reverse*` transcode a single input subsequence per invocation, the first comparison is also equivalent to `lhs.current_ == rhs.current_ && lhs.buf_index_ == rhs.buf_index_`. For an implementation that transcodes several input subsequences per invocation, the stored members alone do not identify a position: two iterators denoting the same element can hold different `current_` values if their buffers were filled starting from different positions (for example, when one of them was filled moving forward by `*read*` and the other moving backward by `*read-reverse*`, or when their buffers were filled with chunks of different extents). — *end note* ]

```cpp
constexpr value_type operator*() const;
```

*Returns*: Either `buf_[buf_index_]`, or, if `E` is `to_utf_view_error_kind::expected` and `!*success*()`, then `unexpected{*success*().error()}`

```cpp
constexpr expected<void, utf_transcoding_error> success() const noexcept requires(E == to_utf_view_error_kind::expected); // exposition only
```

*Returns*:

- If `*from-type*` is `char8_t`:
  - If the current input subsequence is a code unit between 0x80 and 0xBF, returns `unexpected_utf8_continuation_byte`.
  - If the current input subsequence is a code unit between 0xC0 and 0xC2, or between 0xF5 and 0xFF, returns `invalid_utf8_leading_byte`.
  - If the current input subsequence is the code unit 0xE0, and the subsequent input subsequence is a code unit between 0x80 and 0x9F; or if the current input subsequence is the code unit 0xF0, and the subsequent input subsequence is a code unit between 0x80 and 0x8F; then returns `overlong`.
  - If the current input subsequence is the code unit 0xED, and the subsequent input subsequence is a code unit between 0xA0 and 0xBF, then returns `encoded_surrogate`.
  - If the the current input subsequence is the code unit 0xF4, and the subsequent input subsequence is a code unit between 0x90 and 0xBF, then returns `out_of_range`.
  - Otherwise, if the current input subsequence is invalid UTF-8, begins with a code unit between 0xC2 and 0xF4, and there exists some hypothetical sequence of code units which would make the current input subsequence well-formed if concatenated to the end of it, then returns `truncated_utf8_sequence`.
- If `*from-type*` is `char16_t`:
  - If the current input subsequence is a code unit between 0xD800 and 0xDBFF, returns `unpaired_high_surrogate`.
  - If the current input subsequence is a code unit between 0xDC00 and 0xDFFF, returns `unpaired_low_surrogate`.
- If `*from-type*` is `char32_t`:
  - If the current input subsequence is between 0xD800 and 0xDFFF, returns `encoded_surrogate`.
  - If the current input subsequence is between 0x110000 and 0xFFFFFFFF, returns `out_of_range`.

Otherwise, returns `expected<void, utf_transcoding_error>()`.

```cpp
constexpr void read(); // exposition only
```

*Effects*:

Let `n` be a number of consecutive input subsequences, chosen by the implementation, such that:

- `n >= 1`;
- `n` does not exceed the number of input subsequences remaining in the underlying range, starting at position `current_`;
- the total number of code units produced by transcoding those `n` input subsequences as described below is at most `*buffer-capacity*`; and
- if `forward_range<*Base*>` is not modeled, `n == 1`.

Clears `buf_`. Then, for each of the `n` consecutive input subsequences starting at position `current_`, in order: decodes the input subsequence into a code point `c`, using the UTF encoding corresponding to `*from-type*`, setting `c` to U+FFFD if the input subsequence is ill-formed; and appends the code units of `c`, encoded in the UTF encoding corresponding to `ToType`, to `buf_`. Sets `to_increment_` to the total number of code units comprising those `n` input subsequences, and sets `buf_index_` to `0`. If `forward_range<*Base*>` is modeled, `current_` is set to the position it had before `*read*` was called.

> [ *Note:* The choice of `n` is not observable: the division of the input into input subsequences does not depend on it, so the sequence of elements produced by the view is the same for every valid choice. `n` need not be the same on each invocation and can depend on the contents of the underlying range: an implementation typically transcodes a fixed-size window of code units, trimmed back to a whole number of input subsequences, so the number of input subsequences per chunk varies with how many code units each occupies. Choosing `n > 1` permits an implementation to transcode a chunk of input per invocation of `*read*`, for example using SIMD instructions. — *end note* ]

```cpp
constexpr void read-reverse(); // exposition only
```

*Effects*:

Let `n` be a number of consecutive input subsequences, chosen by the implementation, such that:

- `n >= 1`;
- `n` does not exceed the number of input subsequences in the underlying range preceding position `current_`; and
- the total number of code units produced by transcoding those `n` input subsequences as described below is at most `*buffer-capacity*`.

Clears `buf_`. Then, for each of the `n` consecutive input subsequences ending at position `current_`, in order: decodes the input subsequence into a code point `c`, using the UTF encoding corresponding to `*from-type*`, setting `c` to U+FFFD if the input subsequence is ill-formed; and appends the code units of `c`, encoded in the UTF encoding corresponding to `ToType`, to `buf_`. Sets `to_increment_` to the total number of code units comprising those `n` input subsequences, and sets `current_` to the position of the beginning of the first of those `n` input subsequences. Sets `buf_index_` to the index in `buf_` of the first code unit produced by transcoding the last of those `n` input subsequences if `E` is `to_utf_view_error_kind::expected` and that input subsequence is ill-formed, and to `buf_.size() - 1` otherwise.

> [ *Note:* The `n` consecutive input subsequences ending at position `current_` are well-defined: the division of the code units preceding `current_` into input subsequences under Substitution of Maximal Subparts does not depend on the code units at or after `current_`. As with `*read*`, the choice of `n` is not observable, and `n` need not be the same on each invocation: it can depend on the contents of the underlying range. In particular, an implementation need not decide on a number of input subsequences in advance. It can instead step backward over a fixed number of code units (chosen so that the transcoded result is guaranteed to fit in `buf_`), locate the first input subsequence boundary at or after that position by examining a bounded number of neighboring code units, and transcode forward from there to `current_`; `n` is then however many input subsequences that window happens to contain — fewer when the code points are encoded with more code units apiece. An implementation may also always choose `n == 1`, since backward iteration is typically used for short, local movements that would not amortize the cost of transcoding a large chunk. — *end note* ]

##### 25.7.?.7 Class `to_utf_view::*sentinel*` [range.transcoding.sentinel]

```cpp
template<input_range V, to_utf_view_error_kind E, code-unit ToType>
  requires view<V> && code-unit<range_value_t<V>>
template<bool Const>
struct to_utf_view<V, E, ToType>::sentinel {
private:
  using Base = maybe-const<Const, V>; // exposition only

  sentinel_t<Base> end_ = sentinel_t<Base>(); // exposition only

public:
  sentinel() = default;
  constexpr explicit sentinel(sentinel_t<Base> end) : end_{end} {}
  constexpr explicit sentinel(sentinel<!Const> i)
    requires Const && convertible_to<sentinel_t<V>, sentinel_t<Base>>
    : end_{i.end_} {}

  constexpr sentinel_t<Base> base() const { return end_; }

  template<bool OtherConst>
  requires sentinel_for<sentinel_t<Base>, iterator_t<maybe-const<OtherConst, V>>>
  friend constexpr bool operator==(const iterator<OtherConst>& x, const sentinel& y) {
    if constexpr (forward_range<Base>) {
      return x.current_ == y.end_;
    } else {
      return x.current_ == y.end_ && x.buf_index_ == -1;
    }
  }
};
```

### 9.4 Code unit adaptors

Add the following subclause to 25.7 [[range.adaptors]](https://wg21.link/range.adaptors):

#### 25.7.? Code unit adaptors [range.codeunitadaptor]

```cpp
template<class T>
struct implicit-cast-to { // exposition only/
  constexpr T operator()(auto x) const noexcept { return x; }
};
```

The names `as_char`, `as_wchar_t`, `as_char8_t`, `as_char16_t`, and `as_char32_t` denote range adaptor objects ([range.adaptor.object]). Let `as_charT` denote any one of `as_char`, `as_wchar_t`, `as_char8_t`, `as_char16_t`, and `as_char32_t`. Let `Char` be the corresponding character type for `as_charT`, let `E` be an expression and let `T` be `remove_cvref_t<decltype((E))>`. If `ranges::range_reference_t<T>` does not model `convertible_to<Char>`, or if `T` is an array, `as_charT(E)` is ill-formed. Otherwise, the expression `as_charT(E)` is expression-equivalent to:

- If `T` is a specialization of `empty_view` ([range.empty.view]), then `empty_view<Char>{}`.
- Otherwise, `ranges::transform_view(std::views::all(E), *implicit-cast-to*<Char>{})`.

[Example 1:

```cpp
std::vector<int> path_as_ints = {U'C', U':', U'\x00010000'};
std::filesystem::path path = path_as_ints | as_char32_t | std::ranges::to<std::u32string>();
const auto& native_path = path.native();
if (native_path != std::wstring{L'C', L':', L'\xD800', L'\xDC00'}) {
  return false;
}
```

— end example]

### 9.5 Feature test macro

Add the following macro definition to 17.3.2 [[version.syn]](https://wg21.link/version.syn), header `<version>` synopsis, with the value selected by the editor to reflect the date of adoption of this paper:

```cpp
#define __cpp_lib_unicode_transcoding 20XXXXL // also in <ranges>
```

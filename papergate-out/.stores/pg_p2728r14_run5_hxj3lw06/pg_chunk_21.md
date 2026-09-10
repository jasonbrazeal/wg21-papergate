## 10 Design Discussion and Alternatives

### 10.1 CPO Rejection of String Literals

String literals are arrays of char types that include a null terminator:

```cpp
static_assert(std::is_same_v<std::remove_reference_t<decltype("foo")>, const char[4]>);
static_assert(std::ranges::equal("foo", std::array{'f', 'o', 'o', '\0'}));
```

Because they are ranges, a naive implementation of the `to_utfN` CPO would result in null terminators in the output:

```cpp
u8"foo" | to_utf32 | std::ranges::to<u32string>()
// results in a std::u32string of length 4 containing U'f', U'o', U'o', U'\0'
```

To avoid this situation, the `to_utfN` CPOs reject all inputs that are arrays of `char`, as do the `as_charT` casting CPOs.

### 10.2 The `_or_error` Views Are Basis Operations for Other Error Handling Behaviors

You can use the `_or_error` view to implement the same behavior that the non-`std::expected`-based views have.

For example, `foo | std::views::to_utf8` has the same output as:

```cpp
foo
  | std::views::to_utf8_or_error
  | std::views::transform(
      [](std::expected<char8_t, std::utf_transcoding_error> c)
        -> std::inplace_vector<char8_t, 3>
      {
        if (c.has_value()) {
          return {c.value()};
        } else {
          // U+FFFD
          return {u8'\xEF', u8'\xBF', u8'\xBD'};
        }
      })
  | std::views::join
```

You can also substitute a different replacement character by changing the result of the `else` clause, or add exception-based error handling by throwing at that point.

### 10.3 Why We Don’t Cache `begin()`

When we invoke `begin()`, constructing the transcoding iterator may read a bounded number of elements from the underlying view — up to four if it’s transcoding from UTF-8 and buffering a single code point, or up to the (constant) capacity of its internal buffer if it transcodes a chunk of input at a time. A previous revision of this paper implemented `begin()` caching, based on the idea that iterating the underlying range could have unbounded complexity.

However, Tim Song pointed to the wording in `[iterator.requirements.general]` stating that “All the categories of iterators require only those functions that are realizable for a given category in constant time (amortized).” This means that we should be making the assumption that the underlying iterator operations used by `begin()` are “amortized constant time” (in a hand-wavey sense). Tim also pointed out that transcoding from UTF is equivalent to `views::adjacent<4>`, which doesn’t cache.

Based on this reasoning, the transcoding views don’t cache `begin()`.

### 10.4 Optimizing for Double-Transcoding

In generic code, it’s possible to introduce transcoding views that wrap other transcoding views:

```cpp
void foo(std::ranges::view auto v) {
#ifdef _MSC_VER
  windows_function(v | std::views::to_utf16);
#endif
  // ...
}

int main(int, char const* argv[]) {
  foo(std::null_term(argv[1]) | std::views::as_char8_t | std::views::to_utf32);
}
```

In the above example, naively, `foo` would create a `to_utf16_view` wrapping a `to_utf32_view`. However, the `to_utfN` CPOs detect this situation and elide the `to_utf32_view`, creating the `to_utf16_view` so that it directly wraps the view produced by `as_char8_t`.

There’s precedent for this kind of approach in the `views::reverse` CPO, which simply gives back the original underlying view if it detects that it’s reversing another `reverse_view`.

### 10.5 `.base_code_units()`

#### 10.5.1 Proposal

I received feedback that it could be useful to provide a `.base_code_units()` member function on the transcoding iterator which would give out a range of iterators from the underlying range delimiting the code units that make up the current code point.

Since we can’t give out iterators to the underlying range if it’s a (non-forward) input range, it’s also been suggested that in this case, `.base_code_units()` would still be available, but would give out iterators to a special cache that’s stored in the iterator.

To quote from a reflector email discussing this suggestion:

> I think it would be useful to differentiate access to the (complete) underlying range vs access to the input code unit sequence for the current character. Obviously, access to the complete underlying range isn’t possible for input iterators, but access to the current input code unit sequence is (with the caching approach described above is). The iterators could expose this interface:
> 
> ```cpp
>     // Forward+ iterators only; returns an iterator into the underlying range.
>     constexpr const iterator_t<Base>& base() const & noexcept requires forward_range<Base> { ... }
>     constexpr iterator_t<Base> base() && requires forward_range<Base> { ... }
> 
>     // Input+ iterators; returns a subrange containing the input code units for the current character.
>     // References the input code unit sequence cache for input iterators.
>     // References the underlying range otherwise.
>     constexpr subrange<...> base_code_units() const noexcept { ... }
> ```
> 
> Unlike `base()`, `base_code_units()` would not necessarily contain iterators for the underlying range (e.g., in the case of a caching input iterator).

Note that the choice to provide `.base_code_units()` for input ranges affects ABI since the size of the transcoding iterator depends on whether it contains the cache.

#### 10.5.2 Precedent

[[P0244R2]](https://wg21.link/p0244r2) provides transcoding iterators with a `.base_range()` member function that provide this range, although its input iterator functionality is implemented using special caching iterators that have shared ownership of a cache, instead of by storing the cached range in the iterator itself.

ICU provides multiple analogous APIs. The most directly comparable one is the `.stringView()` [member function](https://github.com/unicode-org/icu/blob/649262a75ecddb15a0e58d71f637a8a32eaabd43/icu4c/source/common/unicode/utfiterator.h#L416) on the `UnsafeCodeUnits` transcoding iterator, which provides a `std::basic_string_view` containing the underlying code units for the current code point. `UnsafeCodeUnits` also provides `.begin()` and `.end()` member functions which give out the same range. Unlike the proposed `.base_code_units()` member function, neither of these APIs provide support for input iterators; `.stringView()` is only enabled when the base range is contiguous, and `.begin()` and `.end()` are only enabled if it’s a forward range.

#### 10.5.3 Lifetime Issues

Here’s an example of a function where the use of `.base_code_units()` subtly introduces UB when the function is passed an input range.

This is a run-length-encoder that prints a count of the number of consecutive times it’s seen a code point, followed by the code units making up that code point:

```cpp
void print_runs(std::ranges::range auto text) {
  auto utf_view = text | std::views::to_utf32;
  auto it = utf_view.begin();
  while (it != utf_view.end()) {
    auto units = it.base_code_units();
    char32_t code_point = *it;
    int count = 1;
    ++it;
    while (it != utf_view.end() && *it == code_point) {
      ++count;
      ++it;
    }
    std::print(
      "{}x{::#x} ", count,
      units | std::views::transform([](char8_t c) { return (std::uint8_t)c; } ));
  }
  std::println("");
}
```

When invoked with `u8"ⒶⒶⒶⒷⒸ"sv`, it prints:

```cpp
3x[0xe2, 0x92, 0xb6] 1x[0xe2, 0x92, 0xb7] 1x[0xe2, 0x92, 0xb8]
```

When invoked with `u8"ⒶⒶⒶⒷⒸ"sv | std::views::as_input`, it invokes library undefined behavior and prints corrupted output. Worse, the UB here isn’t caught by AddressSanitizer or UndefinedBehaviorSanitizer because the invalidated `auto units` range points into the same, valid, transcoding iterator, whose cache simply contains the values for the subsequent code point, so the corrupted output is not automatically diagnosable.

With ICU’s APIs, on the other hand, this would fail to compile, because ICU only provides them for forward ranges.

I think this footgun would show up frequently.

In response, it was suggested that the above lifetime issue could be addressed by changing the return type of `.base_code_units()` to something like `std::inplace_vector<char8_t, 4>`.

That creates a different lifetime problem. Consider this example. The Unicode Tags block is intended for use in flag emojis but has been used for LLM prompt injections. Say a user writes the following function, which divides the stream of characters into Tags and non-Tags, and also imagine that they have a custom sink type that accepts iterator pairs rather than ranges:

```cpp
constexpr bool is_tag(char32_t c) { return (c & ~0x7F) == 0xE0000; }

void partition_tags(std::ranges::range auto text, sink non_tags, sink tags) {
  auto utf_view = text | std::views::to_utf32;
  for (auto it = utf_view.begin(); it != utf_view.end(); ++it) {
    (is_tag(*it) ? tags : non_tags).consume(
      it.base_code_units().begin(), it.base_code_units().end());
  }
}
```

Again, this works perfectly well when `partition_tags` is passed a forward range, but then when it’s passed an input range, because each call to `.base_code_units()` returns a separate temporary `std::inplace_vector`, `it.base_code_units().begin()` and `it.base_code_units().end()` now point to different objects, so the function invokes UB.

#### 10.5.4 Survey of Range Adaptors that Downgrade to Input

Some range adaptors downgrade forward ranges into input ranges: these are, to my understanding, `views::as_input`, `views::cache_latest`, `views::join`, and `views::join_with`.

`[range.as.input.overview]` states, “This is useful to avoid overhead that can be necessary to provide support for the operations needed for greater iterator strength.” This use case is potentially relevant for transcoding views, since the size of the iterator may be greater with a stronger iterator category. For example, bidirectional transcoding iterators need to store the begin iterator from the underlying range to avoid overrunning the beginning when transcoding backwards, but forward iterators don’t need it.

But implementing `.base_code_units()` for input views would actually cause `views::as_input` to *increase* the transcoding iterator’s overhead relative to its forward-iterator implementation, because the iterator would need to contain an additional code unit cache.

`views::as_input` was introduced by [[P3725R3]](https://wg21.link/p3725r3), “Filter View Extensions for Safer Use,” and, rather than avoiding overhead, its main motivation was composition with `std::views::filter` in order to avoid pitfalls related to mutating through a filter.

This is potentially relevant to transcoding, in that someone might write a filter-view pipeline on characters. Say a user wants to print the UTF-8 code units for all the non-ASCII code points in a range. That would look like this:

```cpp
void print_nonascii_code_points_and_code_units(std::ranges::range auto text) {
  auto print_code_point{
    [](char32_t code_point, auto code_unit_range) {
    std::println(
      "{:#x} = {::#x}", static_cast<std::uint32_t>(code_point),
      code_unit_range | std::views::transform([](char8_t c) { return (std::uint8_t)c; }));
    }};
  auto code_points = text
                     | std::views::filter([](char8_t c) { return c >= 0x80; })
                     | std::views::to_utf32;
  for (auto it = code_points.begin(); it != code_points.end(); ++it) {
    print_code_point(*it, it.base_code_units());
  }
}
```

A user following the [[P3725R3]](https://wg21.link/p3725r3) guidance might insert a `views::as_input` adaptor into the pipeline before `std::views::filter`, which would continue to compile and work if we provided `.base_code_units()` for input ranges, but which would cause `print_nonascii_code_points_and_code_units` to fail to compile if we didn’t.

But `views::as_input` isn’t strictly necessary here. And we already need to teach users that inserting `views::as_input` before `std::views::filter` will, in rare cases, cause some uses of `.base()` to fail to compile. To demonstrate why this isn’t a novelty, consider the following example:

```cpp
struct Task { int priority; };

bool submit_batch(std::ranges::range auto batch);

// Submit the high-priority tasks in batches; on a transient failure, hand the
// remaining high-priority tasks to the retry queue.
void submit_high_priority_tasks(std::vector<Task>& tasks) {
  auto high = tasks | std::views::filter([](Task const& t) { return t.priority > 100; });
  auto batches = high | std::views::chunk(BATCH_SIZE);
  for (auto it = batches.begin(); it != batches.end(); ++it) {
    if (!submit_batch(*it)) {
      requeue(std::ranges::subrange(it.base(), high.end()));
      return;
    }
  }
}
```

This works as written, but if `views::as_input` is inserted in front of `views::filter`, the call to `it.base()` fails to compile because `std::ranges::chunk_view`’s iterator doesn’t provide `.base()` for input views. But `views::as_input` is unnecessary here as well.

Furthermore, it’s worth noting that the list of plausible reasons to apply a filter_view on code *units* as opposed to code *points* is extremely short; ordinarily, doing so risks corrupting the output.

Moving on to `views::cache_latest`: that one is an adaptor with a niche use case and no special relevance to transcoding.

`views::join` is directly relevant, since it’s common for users to want to reassemble a text string that had previously been broken up into separate parts before transcoding it. `views::join_with` is also potentially relevant, since users may want to transcode text after having used `views::join_with` to add separators to it.

It’s important to note that in the common case, `views::join` and `views::join_with` do not downgrade from forward to input. They only do so if the range of ranges it’s given is a range of *prvalue* ranges.

For example, the `views::join` adaptor in the following example does not downgrade:

```cpp
void print_errors(std::ranges::range auto packets) {
  auto print_code_units =
    [](std::ranges::range auto code_unit) {
      std::println("{::#x}",
                   code_unit
                   | std::views::transform([](char8_t c) { return (std::uint8_t)c; }));
    };
  auto utf_view = packets
                | std::views::join
                | std::views::to_utf32_or_error;
  for (auto it = utf_view.begin(); it != utf_view.end(); ++it) {
    if (!(*it).has_value()) {
      print_code_units(it.base_code_units());
    }
  }
}
```

But, if the packets need to be decrypted before transcoding, and the user alters the pipeline like so:

```cpp
+ std::u8string decrypt(std::u8string_view packet) {
+   return packet
+          | std::views::transform(
+              [](char8_t c) {
+                return static_cast<char8_t>(c ^ 0x55);
+              })
+          | std::ranges::to<std::u8string>();
+ }

void print_errors(std::ranges::range auto packets) {
  auto print_code_units =
    [](std::ranges::range auto code_unit) {
      std::println("{::#x}",
                   code_unit
                   | std::views::transform([](char8_t c) { return (std::uint8_t)c; }));
    };
  auto utf_view = packets
+               | std::views::transform(decrypt)
                | std::views::join
                | std::views::to_utf32_or_error;
  for (auto it = utf_view.begin(); it != utf_view.end(); ++it) {
    if (!(*it).has_value()) {
      print_code_units(it.base_code_units());
    }
  }
}
```

Then it downgrades.

#### 10.5.5 Alternatives to `.base_code_units()` for Users

##### 10.5.5.1 Forward Ranges

For forward ranges, `it.base_code_units()` is equivalent to `std::ranges::subrange(it.base(), std::ranges::next(it).base())`.

The expression above raised concerns about the fact that its use in a loop would mean performing two `operator++` operations on every loop iteration, but that can be mitigated by simply caching the previous iterator while iterating forwards:

```cpp
auto prev_base = it.base();
++it;
auto code_units = std::ranges::subrange(prev_base, it.base());
```

##### 10.5.5.2 Input Ranges

For input ranges, since the transcoding view doesn’t provide `.base()`, the workaround involves making a copy of the input range in order to get a forward range.

###### 10.5.5.2.1 Copying the entire range

If it’s viable to copy the entire range, you can simply insert a `std::ranges::to<std::u8string>()` into the range pipeline.

```cpp
void print_utf8_code_points_and_code_units(std::ranges::range auto text) {
  auto print_code_point{
    [](char32_t code_point, auto code_unit_range) {
    std::println(
      "{:#x} = {::#x}", static_cast<std::uint32_t>(code_point),
      code_unit_range | std::views::transform([](char8_t c) { return (std::uint8_t)c; }));
    }};
  auto code_points = text
                     | std::ranges::to<std::u8string>()
                     | std::views::to_utf32;
  for (auto it = code_points.begin(); it != code_points.end(); ++it) {
    print_code_point(*it, std::ranges::subrange(it.base(), std::ranges::next(it).base()));
  }
}
```

When invoked with `u8"AΩ€😀b"sv | std::views::as_input`, this prints:

```cpp
0x41 = [0x41]
0x3a9 = [0xce, 0xa9]
0x20ac = [0xe2, 0x82, 0xac]
0x1f600 = [0xf0, 0x9f, 0x98, 0x80]
0x62 = [0x62]
```

###### 10.5.5.2.2 Avoiding copying

Although it requires rolling your own segmentation, it is possible to iterate over an input view’s code unit subsequences with additional refactoring:

```cpp
constexpr bool is_utf8_continuation(char8_t c) { return (c & 0xC0) == 0x80; }

void print_utf16_and_utf8_code_units_per_code_point(std::ranges::range auto text) {
  auto print_code_point{
    [](auto u16_view, auto u8_view) {
      std::println(
        "{::#x} = {::#x}",
        u16_view | std::views::transform([](char16_t c) { return (std::uint16_t)c; }),
        u8_view | std::views::transform([](char8_t c) { return (std::uint8_t)c; }));
    }};
  auto it = text.begin();
  std::u8string code_point;
  while (it != text.end()) {
    code_point.clear();
    code_point.push_back(*it);
    ++it;
    it = std::ranges::find_if(std::move(it), text.end(), [&](char8_t c) {
      if (!is_utf8_continuation(c)) return true;
      code_point.push_back(c);
      return false;
    });
    print_code_point(code_point | std::views::to_utf16, code_point);
  }
}
```

When invoked with `u8"AΩ€😀b"sv | std::views::as_input`, this prints:

```cpp
[0x41] = [0x41]
[0x3a9] = [0xce, 0xa9]
[0x20ac] = [0xe2, 0x82, 0xac]
[0xd83d, 0xde00] = [0xf0, 0x9f, 0x98, 0x80]
[0x62] = [0x62]
```

Clearly, this isn’t an ideal user experience, but it only applies to users who have an input range that is too large to copy, and also need to access the underlying code unit sequence for a code point. In my opinion, preserving the ergonomics of that use case is not worth the tradeoff of introducing the safety footgun demonstrated by the RLE example above.

#### 10.5.6 Implementation

An experimental implementation of `.base_code_units()` is available on the `enolan_basecodeunits2` branch of `beman.utf_view`.

### 10.6 SIMD support

The wording has been updated to allow implementations to read code points in chunks rather than one at a time, which enables support for SIMD.

To my knowledge, this would be the first view that reads its input in chunks for reasons of performance rather than correctness.

The transcoding iterator must be increased in size in order to fit a larger buffer which contains the output of the SIMD transcoding kernel. On the other hand, there is no need to store the input buffer in the iterator.

The decision of which output buffer size to select is left up to the implementation, but once chosen, an implementation can’t change it without breaking ABI. (This also implies that, as a process note, it’s not possible for us to standardize a version of this facility that *doesn’t* allow SIMD and then patch SIMD support onto it in a future paper.)

The invariant of `.base()` is that it points to the beginning of the code unit range for the current code point in the underlying view. Transcoding more than one code point at a time slightly complicates the implementation of `.base()` relative to the scalar implementation. For example, an implementation might want to store an iterator to the beginning of the current chunk in the underlying view and then, when `.base()` is invoked, iterate it forward from the beginning of the chunk to the start of the current code point. This means that, whereas the scalar implementation of `.base()` is a simple accessor to a data member, the chunked implementation may need to perform `CHUNK_SIZE` iterator increments internally (which is still O(1)).

Since it’s challenging to implement fully conformant Substitution of Maximal Subparts error handling in a SIMD transcoding kernel, we expect that implementers will add a validation step to their SIMD transcoding kernels and fall back to the serial implementation on invalid UTF. To fully benefit from the fast path, you need valid input.

SIMD support is enabled for forward ranges only. Here is an example of why the chunking behavior breaks input ranges. Say we have a video game that reads the player’s name but only allows space for five code points:

```cpp
std::u32string get_player_name() {
  std::ranges::subrange input_view(
      std::istreambuf_iterator<char>(std::cin),
      std::istreambuf_iterator<char>{});
  // get 5 code points of input
  return input_view
         | beman::utf_view::as_char8_t
         | beman::utf_view::to_utf32
         | std::views::take(5)
         | std::ranges::to<std::u32string>();
}
```

(This is actually somewhat more complicated to do than depicted here.)

With a chunked implementation, the user types “GAM3R” but then needs to keep typing until the chunk gets filled up, only for the rest of the chunk to get discarded.

The reference implementation’s benchmark transcodes the [unicode_lipsum](https://github.com/lemire/unicode_lipsum) corpora from UTF-16 to UTF-8. The SIMD implementation uses a prototype kernel written against C++26 `std::simd` and a buffer capacity of 64 code units. For comparison, the last column is a single bulk `simdutf` call over the whole corpus, with no view involved. Numbers are GiB/s of input consumed (GCC 16.1, `-O3 -march=native`, x86-64 AVX2, AMD Ryzen 9 5950X).

| Corpus | Scalar view | Prototype SIMD view | Bulk `simdutf` |
| --- | --- | --- | --- |
| Latin | 1.86 | 4.20 | 60.4 |
| Arabic | 0.81 | 0.96 | 10.9 |
| Chinese | 0.82 | 1.00 | 8.9 |
| Japanese | 0.77 | 0.85 | 8.7 |
| Korean | 0.89 | 0.86 | 8.0 |

In the current prototype, we see >2x speedup on the most favorable case, which is ASCII input, and either parity or small speedups on other corpuses. (Note that the prototype is currently in an incomplete state, and only implements the UTF16-UTF8 direction, so results with other directions may differ). 64 is the minimum buffer size at which we get favorable results, for this particular transcoding direction, in my prototype. `simdutf` smokes us, mainly due to benefiting from the bulk API, and we can’t approach its speed with a view; we would need to do an algorithm to achieve comparable performance.*

To put these numbers into perspective, the article text of English Wikipedia is roughly 40 GiB in UTF-8, or about 80 GiB in UTF-16, and so would take approximately 43 seconds to transcode on a single core with the scalar implementation and 19 seconds to transcode with SIMD, assuming its properties are roughly similar to the Latin corpus above.

* (This is because a view delivers its output one code unit at a time: every element costs an iterator increment, a dereference, and a buffer-index check, no matter how cheaply the buffer was filled. SIMD accelerates only the buffer refill; once that cost is amortized away, throughput is bounded by the per-element delivery loop — on the Latin row above, the SIMD view is already running at about two cycles per code unit, which is the cost of the loop itself rather than of transcoding. A bulk API has no per-element step at all: it reads and writes entire vectors. Closing the gap therefore requires an interface that writes directly to an output range, not a faster kernel inside the view.)

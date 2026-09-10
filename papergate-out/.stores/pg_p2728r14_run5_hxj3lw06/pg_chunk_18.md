
### 5.2 Code Unit Views

SG16 has a goal to ensure that C++ standard library functions that expect UTF-encoded input do not accept parameters of type `char` or `wchar_t`, whose encodings are implementation-defined, and instead use `char8_t`, `char16_t`, and `char32_t`. These views follow that pattern.

Because virtually all UTF-8 text processed by C++ is stored in `char` (and similarly for UTF-16 and `wchar_t`), this means that we need a terse way to smooth over the transition for users. To do so, this paper introduces views for casting between character types: `as_char`, `as_wchar_t`, `as_char8_t`, `as_char16_t`, and `as_char32_t`.

These are syntactic sugar for producing a `std::ranges::transform_view` with an exposition-only transformation functor that performs the needed cast.

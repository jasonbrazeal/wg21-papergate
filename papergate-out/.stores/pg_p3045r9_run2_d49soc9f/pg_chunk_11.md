```

`mp_units::is_integral_scaling` may be reused in a specialization to distinguish integral from fractional unit ratios. See Value conversions for details.

---

##### 12.3.2.5 `representation_values<Rep>`

A specializable class template that provides the special values used by `quantity::zero()`, `quantity::min()`, `quantity::max()`, mathematical rounding operations, and division-by-zero checks:

```cpp
template<typename Rep>
struct mp_units::representation_values {
  static constexpr Rep zero() noexcept;
  static constexpr Rep one() noexcept;
  static constexpr Rep min() noexcept;
  static constexpr Rep max() noexcept;
};
```

In hosted environments the primary specialization inherits `zero()`, `min()`, and `max()` from `std::chrono::duration_values<Rep>`; `one()` is always defined in the struct itself, constrained to `std::constructible_from<Rep, int>`. In freestanding environments all four methods are defined directly, each guarded by its own `requires` clause: `zero()` and `one()` require `std::constructible_from<Rep, int>`; `min()` requires `std::numeric_limits<Rep>::is_specialized` and that `std::numeric_limits<Rep>::lowest()` returns `Rep`; `max()` requires the same plus `std::numeric_limits<Rep>::max()` returning `Rep`. An explicit specialization is required for types that cannot satisfy those constraints or that need non-standard special values:

```cpp
template<typename T>
struct mp_units::representation_values<my_custom_type<T>> {
  static constexpr my_custom_type<T> zero() noexcept
  { return my_custom_type<T>{T{0}}; }

  static constexpr my_custom_type<T> one() noexcept
  { return my_custom_type<T>{T{1}}; }

  static constexpr my_custom_type<T> min() noexcept
  { return my_custom_type<T>{std::numeric_limits<T>::lowest()}; }

  static constexpr my_custom_type<T> max() noexcept
  { return my_custom_type<T>{std::numeric_limits<T>::max()}; }
};
```

### 12.4 How Scaling Works

Every representation type must be **unit-conversion scalable** — the library must be able to apply a unit magnitude ratio to it internally. This is captured by the `MagnitudeScalable` concept, which directly names the three built-in scaling paths:

```cpp
concept MagnitudeScalable =
  WeaklyRegular<T> && (UsesMagnitudeAwareScaling<T> || UsesFloatingPointScaling<T> || UsesIntegerScaling<T>);
```

`UsesMagnitudeAwareScaling` is satisfied by any type that provides `operator*(T, UnitMagnitude)` — checked first by the scaling engine, before the two built-in numeric paths. The full pattern is described in Magnitude-aware scaling:

```cpp
concept UsesMagnitudeAwareScaling = requires(const T& v) { v * mag<1>; };
```

`UsesFloatingPointScaling` matches any type — or container thereof — whose underlying type satisfies `treat_as_floating_point`, is constructible from `long double` (the precision at which magnitude constants are evaluated), and supports `operator*` and `operator/` with that underlying type, returning a weakly-regular result:

```cpp
concept UsesFloatingPointScaling =
  (treat_as_floating_point<T> || treat_as_floating_point<representation_underlying_type_t<T>>) &&
  std::constructible_from<representation_underlying_type_t<T>, long double> &&
  requires(T value, representation_underlying_type_t<T> f) {
    { value * f } -> WeaklyRegular;
    { value / f } -> WeaklyRegular;
  };
```

`UsesIntegerScaling` matches any type whose underlying type satisfies `detail::integral` (the scaling engine uses `get_value<wider_t>`, `wider_int_for<element_t>`, and `fixed_point<element_t>` internally, all of which require an integer element type). Scaling is routed through the type’s own `operator*` and `operator/`, so wrappers can check for overflow and containers can scale element-wise. The factor type is `wider_int_for<element_t>` — a wider integer of matching sign (e.g. `int64_t` for `int16_t`, `uint64_t` for `uint16_t`) — to prevent intermediate overflow in rational-magnitude conversions:

```cpp
concept UsesIntegerScaling =
  detail::integral<representation_underlying_type_t<T>> &&
  requires(T value, wider_int_for<representation_underlying_type_t<T>> wf) {
    { value * wf };
    { value / wf };
  };
```

> [ *Note:* `detail::integral` is used rather than `std::integral` because on GCC in strict mode (`-std=c++20`) `std::integral<__int128>` is `false` — the standard traits are not specialized for `__int128` outside GNU extensions. When the platform lacks `__SIZEOF_INT128__` entirely, `int128_t` and `uint128_t` are software-emulation types that also do not satisfy `std::integral`. `detail::integral` patches both gaps:
> 
> ```cpp
> template<typename T>
> concept detail::integral =
>   std::integral<T> ||
>   std::same_as<std::remove_cv_t<T>, int128_t> ||
>   std::same_as<std::remove_cv_t<T>, uint128_t>;
> ```
> 
> The scaling engine internals (`get_value`, `wider_int_for`, `fixed_point`) are all specialized for `int128_t` / `uint128_t`, ensuring the full integer scaling pipeline works correctly for 128-bit element types on all supported compilers. — *end note* ]

Most standard types satisfy `MagnitudeScalable` automatically. See Scaling operators for how to provide `operator*` and `operator/` for custom types.

#### 12.4.1 Built-in scaling algorithm

When two quantities of convertible units are combined or converted, the library applies the unit magnitude `M` to the representation value via `scale<To>(M, value)`. The built-in decision tree is:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIKICJodHRwOi8vd3d3LnczLm9yZy9HcmFwaGljcy9TVkcvMS4xL0RURC9zdmcxMS5kdGQiPgo8IS0tIEdlbmVyYXRlZCBieSBncmFwaHZpeiB2ZXJzaW9uIDIuNDIuNCAoMCkKIC0tPgo8IS0tIFRpdGxlOiBzY2FsaW5nIFBhZ2VzOiAxIC0tPgo8c3ZnIHdpZHRoPSIxMDAlIiAKIHZpZXdCb3g9IjAuMDAgMC4wMCA4NTYuNTAgNTM1LjAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIj4KPGcgaWQ9ImdyYXBoMCIgY2xhc3M9ImdyYXBoIiB0cmFuc2Zvcm09InNjYWxlKDEgMSkgcm90YXRlKDApIHRyYW5zbGF0ZSg0IDUzMSkiPgo8dGl0bGU+c2NhbGluZzwvdGl0bGU+Cjxwb2x5Z29uIGZpbGw9IndoaXRlIiBzdHJva2U9InRyYW5zcGFyZW50IiBwb2ludHM9Ii00LDQgLTQsLTUzMSA4NTIuNSwtNTMxIDg1Mi41LDQgLTQsNCIvPgo8IS0tIEEgLS0+CjxnIGlkPSJub2RlMSIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+QTwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xNzcuNSwtNTI3QzE3Ny41LC01MjcgMTAwLjUsLTUyNyAxMDAuNSwtNTI3IDk0LjUsLTUyNyA4OC41LC01MjEgODguNSwtNTE1IDg4LjUsLTUxNSA4OC41LC01MDMgODguNSwtNTAzIDg4LjUsLTQ5NyA5NC41LC00OTEgMTAwLjUsLTQ5MSAxMDAuNSwtNDkxIDE3Ny41LC00OTEgMTc3LjUsLTQ5MSAxODMuNSwtNDkxIDE4OS41LC00OTcgMTg5LjUsLTUwMyAxODkuNSwtNTAzIDE4OS41LC01MTUgMTg5LjUsLTUxNSAxODkuNSwtNTIxIDE4My41LC01MjcgMTc3LjUsLTUyNyIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxMzkiIHk9Ii01MDYuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPnNjYWxlKE0sIHZhbHVlKTwvdGV4dD4KPC9nPgo8IS0tIE1BIC0tPgo8ZyBpZD0ibm9kZTIiIGNsYXNzPSJub2RlIj4KPHRpdGxlPk1BPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEyNy4zMSwtNDQzLjMxQzEyNy4zMSwtNDQzLjMxIDExLjY5LC00MTYuNjkgMTEuNjksLTQxNi42OSA1Ljg1LC00MTUuMzUgNS44NSwtNDEyLjY1IDExLjY5LC00MTEuMzEgMTEuNjksLTQxMS4zMSAxMjcuMzEsLTM4NC42OSAxMjcuMzEsLTM4NC42OSAxMzMuMTUsLTM4My4zNSAxNDQuODUsLTM4My4zNSAxNTAuNjksLTM4NC42OSAxNTAuNjksLTM4NC42OSAyNjYuMzEsLTQxMS4zMSAyNjYuMzEsLTQxMS4zMSAyNzIuMTUsLTQxMi42NSAyNzIuMTUsLTQxNS4zNSAyNjYuMzEsLTQxNi42OSAyNjYuMzEsLTQxNi42OSAxNTAuNjksLTQ0My4zMSAxNTAuNjksLTQ0My4zMSAxNDQuODUsLTQ0NC42NSAxMzMuMTUsLTQ0NC42NSAxMjcuMzEsLTQ0My4zMSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIxMzkiIHk9Ii00MTcuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPm9wKihULCBVbml0TWFnbml0dWRlKTwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTM5IiB5PSItNDA1LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5wcm92aWRlZD88L3RleHQ+CjwvZz4KPCEtLSBBJiM0NTsmZ3Q7TUEgLS0+CjxnIGlkPSJlZGdlMSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+QSYjNDU7Jmd0O01BPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEzOSwtNDkwLjk0QzEzOSwtNDgxLjE5IDEzOSwtNDY4LjUxIDEzOSwtNDU2LjMxIi8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjE0Mi41LC00NTYuMjUgMTM5LC00NDYuMjUgMTM1LjUsLTQ1Ni4yNSAxNDIuNSwtNDU2LjI1Ii8+CjwvZz4KPCEtLSBNQVIgLS0+CjxnIGlkPSJub2RlMyIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+TUFSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTE4NSwtMzEzQzE4NSwtMzEzIDM1LC0zMTMgMzUsLTMxMyAyOSwtMzEzIDIzLC0zMDcgMjMsLTMwMSAyMywtMzAxIDIzLC0yODkgMjMsLTI4OSAyMywtMjgzIDI5LC0yNzcgMzUsLTI3NyAzNSwtMjc3IDE4NSwtMjc3IDE4NSwtMjc3IDE5MSwtMjc3IDE5NywtMjgzIDE5NywtMjg5IDE5NywtMjg5IDE5NywtMzAxIDE5NywtMzAxIDE5NywtMzA3IDE5MSwtMzEzIDE4NSwtMzEzIi8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjExMCIgeT0iLTI5OC4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+VXNlc01hZ25pdHVkZUF3YXJlU2NhbGluZzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMTEwIiB5PSItMjg2LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj52YWx1ZSAqIE17fTwvdGV4dD4KPC9nPgo8IS0tIE1BJiM0NTsmZ3Q7TUFSIC0tPgo8ZyBpZD0iZWRnZTIiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPk1BJiM0NTsmZ3Q7TUFSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTEzMS42OCwtMzgzLjQ4QzEyNy4wOCwtMzY0LjkxIDEyMS4xOSwtMzQxLjE1IDExNi43MSwtMzIzLjA3Ii8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjEyMC4wNiwtMzIyLjAzIDExNC4yNiwtMzEzLjE3IDExMy4yNiwtMzIzLjcyIDEyMC4wNiwtMzIyLjAzIi8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjEzNSIgeT0iLTM1MiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnllczwvdGV4dD4KPC9nPgo8IS0tIEIgLS0+CjxnIGlkPSJub2RlNCIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+QjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0zOTcuMTksLTMyNC44NUMzOTcuMTksLTMyNC44NSAyNDQuODEsLTI5Ny4xNSAyNDQuODEsLTI5Ny4xNSAyMzguOSwtMjk2LjA3IDIzOC45LC0yOTMuOTMgMjQ0LjgxLC0yOTIuODUgMjQ0LjgxLC0yOTIuODUgMzk3LjE5LC0yNjUuMTUgMzk3LjE5LC0yNjUuMTUgNDAzLjEsLTI2NC4wNyA0MTQuOSwtMjY0LjA3IDQyMC44MSwtMjY1LjE1IDQyMC44MSwtMjY1LjE1IDU3My4xOSwtMjkyLjg1IDU3My4xOSwtMjkyLjg1IDU3OS4xLC0yOTMuOTMgNTc5LjEsLTI5Ni4wNyA1NzMuMTksLTI5Ny4xNSA1NzMuMTksLTI5Ny4xNSA0MjAuODEsLTMyNC44NSA0MjAuODEsLTMyNC44NSA0MTQuOSwtMzI1LjkzIDQwMy4xLC0zMjUuOTMgMzk3LjE5LC0zMjQuODUiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDA5IiB5PSItMjk4LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj50cmVhdF9hc19mbG9hdGluZ19wb2ludDwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDA5IiB5PSItMjg2LjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj4mbHQ7VCZndDsgb3IgJmx0O3VuZGVybHlpbmdfdCZsdDtUJmd0OyZndDs/PC90ZXh0Pgo8L2c+CjwhLS0gTUEmIzQ1OyZndDtCIC0tPgo8ZyBpZD0iZWRnZTMiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPk1BJiM0NTsmZ3Q7QjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0xODUuNzIsLTM5Mi43NUMyMzAuOTUsLTM3My4xNSAyOTkuNzMsLTM0My4zNSAzNDguOTksLTMyMiIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIzNTAuNDgsLTMyNS4xNyAzNTguMjYsLTMxNy45OSAzNDcuNywtMzE4Ljc1IDM1MC40OCwtMzI1LjE3Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjI4OS41IiB5PSItMzUyIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+bm88L3RleHQ+CjwvZz4KPCEtLSBGUCAtLT4KPGcgaWQ9Im5vZGU1IiBjbGFzcz0ibm9kZSI+Cjx0aXRsZT5GUDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik00MzAsLTIwOEM0MzAsLTIwOCAyMjIsLTIwOCAyMjIsLTIwOCAyMTYsLTIwOCAyMTAsLTIwMiAyMTAsLTE5NiAyMTAsLTE5NiAyMTAsLTE4NCAyMTAsLTE4NCAyMTAsLTE3OCAyMTYsLTE3MiAyMjIsLTE3MiAyMjIsLTE3MiA0MzAsLTE3MiA0MzAsLTE3MiA0MzYsLTE3MiA0NDIsLTE3OCA0NDIsLTE4NCA0NDIsLTE4NCA0NDIsLTE5NiA0NDIsLTE5NiA0NDIsLTIwMiA0MzYsLTIwOCA0MzAsLTIwOCIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSIzMjYiIHk9Ii0xOTMuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPlVzZXNGbG9hdGluZ1BvaW50U2NhbGluZzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iMzI2IiB5PSItMTgxLjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5lLmcuIGRvdWJsZSwgY2FydGVzaWFuX3ZlY3RvciZsdDtkb3VibGUmZ3Q7PC90ZXh0Pgo8L2c+CjwhLS0gQiYjNDU7Jmd0O0ZQIC0tPgo8ZyBpZD0iZWRnZTQiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkImIzQ1OyZndDtGUDwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik0zODcuMTksLTI2Ni45NEMzNzQuNTUsLTI1MS4yNSAzNTguNzMsLTIzMS42MiAzNDYuMzQsLTIxNi4yNSIvPgo8cG9seWdvbiBmaWxsPSJibGFjayIgc3Ryb2tlPSJibGFjayIgcG9pbnRzPSIzNDguODYsLTIxMy43OSAzMzkuODYsLTIwOC4yIDM0My40MSwtMjE4LjE4IDM0OC44NiwtMjEzLjc5Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjM3NiIgeT0iLTIzMyIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnRydWU8L3RleHQ+CjwvZz4KPCEtLSBJTlQgLS0+CjxnIGlkPSJub2RlNiIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+SU5UPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTcwMy41LC0yMDhDNzAzLjUsLTIwOCA0OTAuNSwtMjA4IDQ5MC41LC0yMDggNDg0LjUsLTIwOCA0NzguNSwtMjAyIDQ3OC41LC0xOTYgNDc4LjUsLTE5NiA0NzguNSwtMTg0IDQ3OC41LC0xODQgNDc4LjUsLTE3OCA0ODQuNSwtMTcyIDQ5MC41LC0xNzIgNDkwLjUsLTE3MiA3MDMuNSwtMTcyIDcwMy41LC0xNzIgNzA5LjUsLTE3MiA3MTUuNSwtMTc4IDcxNS41LC0xODQgNzE1LjUsLTE4NCA3MTUuNSwtMTk2IDcxNS41LC0xOTYgNzE1LjUsLTIwMiA3MDkuNSwtMjA4IDcwMy41LC0yMDgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTk3IiB5PSItMTkzLjIiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjExLjAwIj5Vc2VzSW50ZWdlclNjYWxpbmc8L3RleHQ+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjU5NyIgeT0iLTE4MS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+ZS5nLiBpbnQsIHNhZmVfaW50LCBjYXJ0ZXNpYW5fdmVjdG9yJmx0O2ludCZndDs8L3RleHQ+CjwvZz4KPCEtLSBCJiM0NTsmZ3Q7SU5UIC0tPgo8ZyBpZD0iZWRnZTUiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPkImIzQ1OyZndDtJTlQ8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNDUxLjY2LC0yNzAuNjNDNDgzLjMxLC0yNTMuMjkgNTI2LjE3LC0yMjkuODEgNTU3LjEzLC0yMTIuODQiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNTU4Ljg0LC0yMTUuOSA1NjUuOTMsLTIwOC4wMiA1NTUuNDgsLTIwOS43NiA1NTguODQsLTIxNS45Ii8+Cjx0ZXh0IHRleHQtYW5jaG9yPSJtaWRkbGUiIHg9IjUzOC41IiB5PSItMjMzIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+ZmFsc2U8L3RleHQ+CjwvZz4KPCEtLSBHIC0tPgo8ZyBpZD0ibm9kZTciIGNsYXNzPSJub2RlIj4KPHRpdGxlPkc8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTg1LjM5LC0xMjMuOTZDNTg1LjM5LC0xMjMuOTYgNTM5Ljg0LC0xMTIuMDQgNTM5Ljg0LC0xMTIuMDQgNTM0LjA0LC0xMTAuNTIgNTM0LjA0LC0xMDcuNDggNTM5Ljg0LC0xMDUuOTYgNTM5Ljg0LC0xMDUuOTYgNTg1LjM5LC05NC4wNCA1ODUuMzksLTk0LjA0IDU5MS4yLC05Mi41MiA2MDIuOCwtOTIuNTIgNjA4LjYxLC05NC4wNCA2MDguNjEsLTk0LjA0IDY1NC4xNiwtMTA1Ljk2IDY1NC4xNiwtMTA1Ljk2IDY1OS45NiwtMTA3LjQ4IDY1OS45NiwtMTEwLjUyIDY1NC4xNiwtMTEyLjA0IDY1NC4xNiwtMTEyLjA0IDYwOC42MSwtMTIzLjk2IDYwOC42MSwtMTIzLjk2IDYwMi44LC0xMjUuNDggNTkxLjIsLTEyNS40OCA1ODUuMzksLTEyMy45NiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI1OTciIHk9Ii0xMDYuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPm1hZ25pdHVkZT88L3RleHQ+CjwvZz4KPCEtLSBJTlQmIzQ1OyZndDtHIC0tPgo8ZyBpZD0iZWRnZTYiIGNsYXNzPSJlZGdlIj4KPHRpdGxlPklOVCYjNDU7Jmd0O0c8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTk3LC0xNzEuODZDNTk3LC0xNjEuNzEgNTk3LC0xNDguNjMgNTk3LC0xMzcuMTIiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNjAwLjUsLTEzNy4xMSA1OTcsLTEyNy4xMSA1OTMuNSwtMTM3LjExIDYwMC41LC0xMzcuMTEiLz4KPC9nPgo8IS0tIEkgLS0+CjxnIGlkPSJub2RlOCIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+STwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik00NzksLTM2QzQ3OSwtMzYgMzY5LC0zNiAzNjksLTM2IDM2MywtMzYgMzU3LC0zMCAzNTcsLTI0IDM1NywtMjQgMzU3LC0xMiAzNTcsLTEyIDM1NywtNiAzNjMsMCAzNjksMCAzNjksMCA0NzksMCA0NzksMCA0ODUsMCA0OTEsLTYgNDkxLC0xMiA0OTEsLTEyIDQ5MSwtMjQgNDkxLC0yNCA0OTEsLTMwIDQ4NSwtMzYgNDc5LC0zNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI0MjQiIHk9Ii0yMS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+ZXhhY3QgaW50ZWdlciDDlzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNDI0IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGUuZy4gbeKGkm1tLCDDlzEwMDApPC90ZXh0Pgo8L2c+CjwhLS0gRyYjNDU7Jmd0O0kgLS0+CjxnIGlkPSJlZGdlNyIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+RyYjNDU7Jmd0O0k8L3RpdGxlPgo8cGF0aCBmaWxsPSJub25lIiBzdHJva2U9ImJsYWNrIiBkPSJNNTc1LjA5LC05Ni43M0M1NDcuOCwtODIuNjkgNTAwLjU3LC01OC4zOSA0NjYuMTcsLTQwLjY5Ii8+Cjxwb2x5Z29uIGZpbGw9ImJsYWNrIiBzdHJva2U9ImJsYWNrIiBwb2ludHM9IjQ2Ny43NywtMzcuNTggNDU3LjI4LC0zNi4xMiA0NjQuNTcsLTQzLjgxIDQ2Ny43NywtMzcuNTgiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTQwIiB5PSItNjEiIGZvbnQtZmFtaWx5PSJzYW5zLXNlcmlmIiBmb250LXNpemU9IjEwLjAwIj5pbnRlZ3JhbDwvdGV4dD4KPC9nPgo8IS0tIFIgLS0+CjxnIGlkPSJub2RlOSIgY2xhc3M9Im5vZGUiPgo8dGl0bGU+UjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik02NTUsLTM2QzY1NSwtMzYgNTM5LC0zNiA1MzksLTM2IDUzMywtMzYgNTI3LC0zMCA1MjcsLTI0IDUyNywtMjQgNTI3LC0xMiA1MjcsLTEyIDUyNywtNiA1MzMsMCA1MzksMCA1MzksMCA2NTUsMCA2NTUsMCA2NjEsMCA2NjcsLTYgNjY3LC0xMiA2NjcsLTEyIDY2NywtMjQgNjY3LC0yNCA2NjcsLTMwIDY2MSwtMzYgNjU1LC0zNiIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI1OTciIHk9Ii0yMS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+d2lkZW5lZCBpbnQgYXJpdGhtZXRpYzwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNTk3IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGludDY0X3QgLyAxMjgmIzQ1O2JpdCk8L3RleHQ+CjwvZz4KPCEtLSBHJiM0NTsmZ3Q7UiAtLT4KPGcgaWQ9ImVkZ2U4IiBjbGFzcz0iZWRnZSI+Cjx0aXRsZT5HJiM0NTsmZ3Q7UjwvdGl0bGU+CjxwYXRoIGZpbGw9Im5vbmUiIHN0cm9rZT0iYmxhY2siIGQ9Ik01OTcsLTkwLjg0QzU5NywtNzguMjggNTk3LC02MC45OCA1OTcsLTQ2LjUiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNjAwLjUsLTQ2LjExIDU5NywtMzYuMTEgNTkzLjUsLTQ2LjExIDYwMC41LC00Ni4xMSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI2MTYiIHk9Ii02MSIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTAuMDAiPnJhdGlvbmFsPC90ZXh0Pgo8L2c+CjwhLS0gSVIgLS0+CjxnIGlkPSJub2RlMTAiIGNsYXNzPSJub2RlIj4KPHRpdGxlPklSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTgzNi41LC0zNkM4MzYuNSwtMzYgNzE1LjUsLTM2IDcxNS41LC0zNiA3MDkuNSwtMzYgNzAzLjUsLTMwIDcwMy41LC0yNCA3MDMuNSwtMjQgNzAzLjUsLTEyIDcwMy41LC0xMiA3MDMuNSwtNiA3MDkuNSwwIDcxNS41LDAgNzE1LjUsMCA4MzYuNSwwIDgzNi41LDAgODQyLjUsMCA4NDguNSwtNiA4NDguNSwtMTIgODQ4LjUsLTEyIDg0OC41LC0yNCA4NDguNSwtMjQgODQ4LjUsLTMwIDg0Mi41LC0zNiA4MzYuNSwtMzYiLz4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNzc2IiB5PSItMjEuMiIgZm9udC1mYW1pbHk9InNhbnMtc2VyaWYiIGZvbnQtc2l6ZT0iMTEuMDAiPmxvbmcgZG91YmxlIGZpeGVkJiM0NTtwb2ludDwvdGV4dD4KPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeD0iNzc2IiB5PSItOS4yIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMS4wMCI+KGUuZy4gZGVn4oaScmFkLCDDl8+ALzE4MCk8L3RleHQ+CjwvZz4KPCEtLSBHJiM0NTsmZ3Q7SVIgLS0+CjxnIGlkPSJlZGdlOSIgY2xhc3M9ImVkZ2UiPgo8dGl0bGU+RyYjNDU7Jmd0O0lSPC90aXRsZT4KPHBhdGggZmlsbD0ibm9uZSIgc3Ryb2tlPSJibGFjayIgZD0iTTYxOS42NywtOTYuNzNDNjQ3LjkxLC04Mi42OSA2OTYuNzcsLTU4LjM5IDczMi4zNywtNDAuNjkiLz4KPHBvbHlnb24gZmlsbD0iYmxhY2siIHN0cm9rZT0iYmxhY2siIHBvaW50cz0iNzM0LjE3LC00My43MSA3NDEuNTcsLTM2LjEyIDczMS4wNiwtMzcuNDQgNzM0LjE3LC00My43MSIvPgo8dGV4dCB0ZXh0LWFuY2hvcj0ibWlkZGxlIiB4PSI3MTkuNSIgeT0iLTYxIiBmb250LWZhbWlseT0ic2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMC4wMCI+aXJyYXRpb25hbDwvdGV4dD4KPC9nPgo8L2c+Cjwvc3ZnPgo=)

The magnitude-aware path (`operator*(T, UnitMagnitude)`) is checked first — before any of the built-in paths. If a representation type provides this operator, it has full control over how scaling is performed and what type is returned. The built-in paths are only used as a fallback.

The integer path (`UsesIntegerScaling`) never promotes values to floating-point, even for the rational and irrational sub-paths. This is intentional: the user explicitly chose an integer representation type, opting out of floating-point arithmetic. The platform may lack FP hardware (embedded systems, DSPs), rely on software-emulated FP, or enforce a no-FP policy. The library respects that choice throughout unit conversion.

The design preference order is **exact integer > exact rational > approximate irrational**: integer multiplication keeps lossless conversions exact (`42 * m` → `42000 * mm` without floating-point rounding); rational factors are applied as numerator × value ÷ denominator entirely in integer arithmetic; and irrational factors (π/180, √2, …) fall back to a `long double` approximation rounded to the target integer type.

The rational path computes `value * numerator / denominator` entirely in integer arithmetic using widened types to prevent intermediate overflow — for example, converting feet to metres multiplies by 3048 before dividing by 10000, which would overflow a 64-bit integer for values above ~3×10¹⁵ without extra width:

| Source type | Widened to |
| --- | --- |
| Signed ≤ 32 bits (`int8_t`…`int32_t`) | `int64_t` |
| Unsigned ≤ 32 bits | `uint64_t` |
| `int64_t` | `__int128` or equivalent signed 128-bit |
| `uint64_t` | `unsigned __int128` or equivalent unsigned |

Using `long double` instead would violate the no-FP principle and introduce rounding (`0.3048` is not exactly representable in binary floating-point); on ARM / Apple Silicon `long double == double` anyway, giving no extra range.

Double-width arithmetic avoids most UB during intermediate scaling, but cannot prevent overflow in the final result when that result doesn’t fit in the target type. Runtime overflow detection requires a representation type that checks arithmetic operations — a checked-integer wrapper (e.g., `safe_int<T>` from mp-units) satisfies `UsesIntegerScaling` and will trap overflows in the final result.

Aggregate representation types that store multiple independently-scaled fields (e.g., `uncertainty<T>` holding a central value and an error bound) implement `operator*` and `operator/` to distribute scaling across all internal fields; the built-in integer and floating-point paths invoke those operators on the aggregate as a unit.

##### 12.4.1.1 Floating-point precision

For floating-point representation types (`UsesFloatingPointScaling`), the unit magnitude is reduced to a single `constexpr` scalar (a `double` or `long double` value representing the exact mathematical ratio) and applied as a single multiplication: `value * factor`. This matches what equivalent hand-written code would do. The library makes no stronger precision guarantee than the underlying floating-point operations provide — in particular, it does not mandate any specific ULP bound. This is consistent with the rest of the C++ standard library, including `std::chrono::duration`, which likewise leaves floating-point conversion precision to the quality of the implementation.

The concern raised that lazy evaluation could produce results differing from hand-written code by more than a few ULPs does not apply here: the magnitude is always a single compile-time constant representing the full unit ratio, never a chain of intermediate multiplications. Overflow to `+inf` would therefore only occur for values that would also overflow the equivalent hand-written multiplication, which is a property of the value, not the library.

For integer types, widened arithmetic (as described above) prevents intermediate overflow. For floating-point types, implementations are encouraged to choose a representation of the conversion factor that minimises precision loss, but this is a quality-of-implementation concern, not a normative requirement.

#### 12.4.2 Magnitude-aware scaling

A type satisfies `UsesMagnitudeAwareScaling` (see How Scaling Works) by providing `operator*(T, UnitMagnitude)` as a hidden friend. Unlike the built-in numeric paths, this operator receives the full compile-time unit magnitude and may return a **different type** — for example, a range-validated representation can adjust its bounds during conversion: constraining values to [-180, 180] in degrees should produce a type constrained to [-π, π] when converted to radians, otherwise the bounds would be meaningless in the target unit:

```cpp
// Example custom type (not provided by the library)
template<std::treat_as_floating_point T, auto Min, auto Max, typename Policy>
class bounded_value : /* ... */ {
public:
  template<std::UnitMagnitude M>
  [[nodiscard]] friend constexpr auto operator*(const bounded_value& val, M m)
  {
    constexpr T new_lo = std::scale<T>(M{}, T{Min});
    constexpr T new_hi = std::scale<T>(M{}, T{Max});

    const T scaled = std::scale<T>(m, val.value());

    if constexpr (new_lo <= new_hi)
      return bounded_value<T, new_lo, new_hi, Policy>(scaled);
    else
      return bounded_value<T, new_hi, new_lo, Policy>(scaled);
  }
};
```

The `scale` function handles precision optimization automatically — when the magnitude’s inverse is integral (e.g. degree-to-radian with π/180), it divides by the inverse instead of multiplying, avoiding FP rounding errors.

The library calls `value * M{}` in `scale()` before trying the built-in paths. Because the return type may differ from the input, `quantity::in(unit)` propagates the new representation type through `sudo_cast`, and the resulting `quantity` (or `quantity_point`) automatically uses the scaled-bounds representation.

### 12.5 Complex quantities and units

TODO

### 12.6 Vector and tensor quantities

TODO

### 12.7 Logarithmic quantities and units

TODO

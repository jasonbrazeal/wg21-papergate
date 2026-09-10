- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `character-set` token specifies the symbol text encoding:
  - `U` (default) uses the **UTF-8** symbols defined by [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (e.g., `LT⁻²`),
  - `P` forces non-standard **portable** output (e.g., `LT^-2`).

Dimension symbols of some quantities are specified to use Unicode signs by the ISQ (e.g., `Θ` symbol for the *thermodynamic temperature* dimension). The library follows this by default. From the engineering point of view, sometimes Unicode text might not be the best solution as terminals of many (especially embedded) devices can output only letters from the basic literal character set only. In such a case, the dimension symbol can be forced to be printed using such characters thanks to `character-set` token:

```cpp
std::println("{}", isq::dim_thermodynamic_temperature);   // Θ
std::println("{:P}", isq::dim_thermodynamic_temperature); // O
std::println("{}", isq::power.dimension);                 // L²MT⁻³
std::println("{:P}", isq::power.dimension);               // L^2MT^-3
```

#### 17.4.3 Unit formatting

```
unit-format-spec      = [fill-and-align], [width], [unit-spec];
unit-spec             = [character-set], [unit-symbol-solidus], [unit-symbol-separator], [L]
                      | [character-set], [unit-symbol-separator], [unit-symbol-solidus], [L]
                      | [unit-symbol-solidus], [character-set], [unit-symbol-separator], [L]
                      | [unit-symbol-solidus], [unit-symbol-separator], [character-set], [L]
                      | [unit-symbol-separator], [character-set], [unit-symbol-solidus], [L]
                      | [unit-symbol-separator], [unit-symbol-solidus], [character-set], [L];
unit-symbol-solidus   = '1' | 'a' | 'n';
unit-symbol-separator = 's' | 'd';
```

In the above grammar:

- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `unit-symbol-solidus` token specifies how the division of units should look like:
  - ‘1’ (default) outputs `/` only when there is only **one** unit in the denominator, otherwise negative exponents are printed (e.g., `m/s`, `kg m⁻¹ s⁻¹`)
  - ‘a’ **always** uses solidus (e.g., `m/s`, `kg/(m s)`)
  - ‘n’ **never** prints solidus, which means that negative exponents are always used (e.g., `m s⁻¹`, `kg m⁻¹ s⁻¹`)
- `unit-symbol-separator` token specifies how multiplied unit symbols should be separated:
  - ‘s’ (default) uses **space** as a separator (e.g., `kg m²/s²`)
  - ‘d’ uses half-high **dot** (`⋅`) as a separator (e.g., `kg⋅m²/s²`) (requires the UTF-8 encoding)
- ‘L’ is reserved for possible future localization use in case C++ standard library gets access to the ICU-like database.

*Note: The intent of the above grammar was that the elements of `unit-spec` can appear in any order as they have unique characters. Users shouldn’t have to remember the order of those tokens to control the formatting of a unit symbol.*

The above grammar for `unit-symbol-solidus` is consistent with the current state of [[mp-units]](https://mpusz.github.io/mp-units). However, a few aternatives are possible:

```
unit-symbol-solidus   = '1' | 'a' | 'n';
unit-symbol-solidus   = 'o' | 'a' | 'n';
unit-symbol-solidus   = '1' | '*' | '0';
unit-symbol-solidus   = '1' | '*' | '-';
unit-symbol-solidus   = '1' | '+' | '-';
```

Unit symbols of some quantities are specified to use Unicode signs by the [[SI]](https://www.bipm.org/en/publications/si-brochure) (e.g., `Ω` symbol for the *resistance* quantity). The library follows this by default. From the engineering point of view, sometimes Unicode text might not be the best solution as terminals of many (especially embedded) devices can output only letters from the basic literal character set only. In such a case, the unit symbol can be forced to be printed using such characters thanks to `character-set` token:

```cpp
std::println("{}", si::ohm);      // Ω
std::println("{:P}", si::ohm);    // ohm
std::println("{}", us);           // µs
std::println("{:P}", us);         // us
std::println("{}", m / s2);       // m/s²
std::println("{:P}", m / s2);     // m/s^2
```

Additionally, both [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) leave some freedom on how to print unit symbols. This is why two additional tokens were introduced.

`unit-symbol-solidus` specifies how the division of units should look like. By default, `/` will be used only when the denominator contains only one unit. However, with the ‘a’ or ‘n’ options, we can force the facility to print the `/` character always (even when there are more units in the denominator), or never, in which case a parenthesis will be added to enclose all denominator units.

```cpp
std::println("{}", m / s);          // m/s
std::println("{}", kg / m / s2);    // kg m⁻¹ s⁻²
std::println("{:a}", m / s);        // m/s
std::println("{:a}", kg / m / s2);  // kg/(m s²)
std::println("{:n}", m / s);        // m s⁻¹
std::println("{:n}", kg / m / s2);  // kg m⁻¹ s⁻²
```

The `unit-symbol-separator` token allows us to obtain the following outputs:

```cpp
std::println("{}", kg * m2 / s2);    // kg m²/s²
std::println("{:d}", kg * m2 / s2);  // kg⋅m²/s²
```

*Note: ‘d’ requires the UTF-8 encoding to be set.*

#### 17.4.4 Quantity formatting

```
quantity-format-spec        = [fill-and-align], [width], [quantity-specs], [defaults-specs];
quantity-specs              = conversion-spec;
                            | quantity-specs, conversion-spec;
                            | quantity-specs, literal-char;
literal-char                = ? any character other than '{', '}', or '%' ?;
conversion-spec             = '%', placement-type;
placement-type              = subentity-id | '?' | '%';
defaults-specs              = ':', default-spec-list;
default-spec-list           = default-spec;
                            | default-spec-list, default-spec;
default-spec                = subentity-id, '[' format-spec ']';
subentity-id                = 'N' | 'U' | 'D';
format-spec                 = ? as specified by the formatter for the argument type ?;
```

In the above grammar:

- `fill-and-align` and `width` tokens are defined in the 28.5.2.2 [[format.string.std]](https://wg21.link/format.string.std) chapter of the C++ standard specification,
- `placement-type` token specifies which entity should be put and where:
  - ‘N’ inserts a default-formatted numerical value of the quantity,
  - ‘U’ inserts a default-formatted unit of the quantity,
  - ‘D’ inserts a default-formatted dimension of the quantity,
  - ‘?’ inserts an optional separator between the number and a unit based on the value of `space_before_unit_symbol` for this unit,
  - ‘%’ just inserts ‘%’ character.
- `defaults-specs` token allows overwriting defaults for the underlying formatters with the custom format string. Each override starts with a subentity identifier (‘N’, ‘U’, or ‘D’) followed by the format string enclosed in square brackets.

##### 17.4.4.1 Two levels of format specification

The grammar above introduces a two-level design that may initially look unfamiliar, so it is worth describing in detail. A `quantity` is a wrapper over a numerical value tagged with a unit (and, indirectly, a dimension). When formatting it, there are two independent concerns, and each `:` delimiter opens the section that addresses one of them:

- The first `:` (as in any `std::format` replacement field) starts the **quantity-level** format specification. Here we provide `fill-and-align` and `width` that treat the entire quantity output as one contiguous piece of text, and `quantity-specs` — a small layout language built from the `%N`, `%U`, `%D`, `%?`, and `%%` placeholders — that decides *which* components (numerical value, unit, dimension) are printed and *how* they are arranged.
- The second `:` starts the **component-level** format specifications (`defaults-specs`). A `quantity` is only a numerical wrapper. It does not — and should not — assume any knowledge about the format-spec grammar of the representation type it stores. This is why the specs provided in `N[...]`, `U[...]`, and `D[...]` are not interpreted by the quantity formatter at all. They are forwarded verbatim to the formatters of the respective components and processed there.

We deliberately chose *not* to follow the `%Q`/`%q` convention that `std::chrono::duration` uses for its value and unit suffix. Those identifiers are easy to confuse with one another, do not hint at what they stand for, and — being lower/upper-case variants of the same letter — leave no room for a mnemonic third option. A `quantity` additionally exposes its *dimension*, which the `chrono` grammar has no concept of and therefore no placeholder for. We instead use the self-explanatory `%N` (numerical value), `%U` (unit), and `%D` (dimension), where each letter directly evokes the component it inserts.

Separating the two concerns means that overriding how a single component is formatted does not force us to respell the default quantity layout. For example, to round the number to two decimal places while keeping the default arrangement of the components intact, it is enough to leave the quantity-level spec empty and provide only the component-level override:

```cpp
std::println("{::N[.2f]}", 100. * km / (3 * h));  // 33.33 km/h
```

We did not have to write out the default `%N%?%U` layout just to attach a precision to the number. Had numerical-value modifiers been embedded directly in the quantity format-spec (as is the case for `std::chrono::duration`), every such customization would have required repeating the entire default format string verbatim.

This two-level `{::...}` shape is not novel. The C++ standard library already uses it to format the elements of a range. For a range, the first `:` opens the range’s own format spec, and the optional second `:` introduces a format spec that is forwarded to the formatter of each element:

```cpp
std::vector v{1.2345, 2.3456, 3.4567};
std::println("{}", v);        // [1.2345, 2.3456, 3.4567]
std::println("{::.2f}", v);   // [1.23, 2.35, 3.46]
std::println("{:n:.2f}", v);  // 1.23, 2.35, 3.46
```

Here `.2f` after the second `:` is not interpreted by the range formatter — it is handed unchanged to the `double` formatter used for every element. The `quantity` formatter follows exactly the same principle, so users already familiar with formatting the contents of a container should find the `quantity` grammar consistent with their expectations.

##### 17.4.4.2 Default formatting

To format `quantity` values, the formatting facility uses `quantity-format-spec`. If left empty, the default formatting is applied. The same default formatting is also applied to the output streams. This is why the following code lines produce the same output:

```cpp
std::cout << "Distance: " << 123 * km << "\n";
std::cout << std::format("Distance: {}\n", 123 * km);
std::cout << std::format("Distance: {:%N%?%U}\n", 123 * km);
```

Please note that for some quantities the `{:%N %U}` format may provide a different output than the default one, as some units have `space_before_unit_symbol` customization point explicitly set to `false` (e.g., `%` and `°`).

##### 17.4.4.3 Quantity numerical value, unit symbol, or both?

Thanks to the grammar provided above, the user can easily decide to either:

- print a whole quantity:

  ```cpp
  std::println("Speed: {}", 120 * km / h);
  ```

  ```
  Speed: 120 km/h
  ```
- provide custom quantity formatting:

  ```cpp
  std::println("Speed: {:%N in %U}", 120 * km / h);
  ```

  ```
  Speed: 120 in km/h
  ```
- provide custom formatting for components:

  ```cpp
  std::println("Speed: {::N[.2f]U[n]}", 100. * km / (3 * h));
  ```

  ```
  Speed: 33.33 km h⁻¹
  ```
- print only specific components (numerical value, unit, or dimension):

  ```cpp
  std::println("Speed:\n- number: {0:%N}\n- unit: {0:%U}\n- dimension: {0:%D}", 120 * km / h);
  ```

  ```
  Speed:
  - number: 120
  - unit: km/h
  - dimension: LT⁻¹
  ```

`placement-type` greatly simplify element access to the elements of the quantity. Without them the second case above would require the following:

```cpp
const quantity q = 120 * km / h;
std::println("Speed:\n- number: {}\n- unit: {}\n- dimension: {}",
             q.numerical_value_ref_in(q.unit), q.unit, q.dimension);
```

`default-spec` is crutial to provide formatting of user-defined representation types. Initially, [[mp-units]](https://mpusz.github.io/mp-units) library was providing numerical value modifiers inplace of its format specification similarly to `std::chrono::duration` formatter. However, it:

- worked only with fundamental arithmetic types and was not able to adjust to different format specifications of custom representation types,
- was quite hard to parse and format everything in a 100% compatible way with the formatting specified in the C++ standard and already implemented in the underlying standard library.

##### 17.4.4.4 Formatting of the quantity numerical value

The representation type used as a numerical value of a quantity must provide its own formatter specialization. It will be called by the quantity formatter with the format-spec provided by the user in the `N` defaults specification.

In case we use C++ fundamental arithmetic types with our quantities the standard formatter specified in [format.string.std](https://wg21.link/format.string.std) will be used. The rest of this chapter assumes that it is the case and provides some usage examples.

`sign` token allows us to specify how the value’s sign is being printed:

```cpp
std::println("{0},{0::N[+]},{0::N[-]},{0::N[ ]}", 1 * m);   // 1 m,+1 m,1 m, 1 m
std::println("{0},{0::N[+]},{0::N[-]},{0::N[ ]}", -1 * m);  // -1 m,-1 m,-1 m,-1 m
```

where:

- `+` indicates that a sign should be used for both non-negative and negative numbers,
- `-` indicates that a sign should be used for negative numbers and negative zero only (this is the default behavior),
- `<space>` indicates that a leading space should be used for non-negative numbers other than negative zero, and a minus sign for negative numbers and negative zero.

`precision` token is allowed only for floating-point representation types:

```cpp
std::println("{::N[.0]}", 1.2345 * m);   // 1 m
std::println("{::N[.1]}", 1.2345 * m);   // 1 m
std::println("{::N[.2]}", 1.2345 * m);   // 1.2 m
std::println("{::N[.3]}", 1.2345 * m);   // 1.23 m
std::println("{::N[.0f]}", 1.2345 * m);  // 1 m
std::println("{::N[.1f]}", 1.2345 * m);  // 1.2 m
std::println("{::N[.2f]}", 1.2345 * m);  // 1.23 m
```

`type` specifies how a value of the representation type is being printed. For integral types:

```cpp
std::println("{::N[b]}", 42 * m);    // 101010 m
std::println("{::N[B]}", 42 * m);    // 101010 m
std::println("{::N[d]}", 42 * m);    // 42 m
std::println("{::N[o]}", 42 * m);    // 52 m
std::println("{::N[x]}", 42 * m);    // 2a m
std::println("{::N[X]}", 42 * m);    // 2A m
```

The above can be printed in an alternate version thanks to the `#` token:

```cpp
std::println("{::N[#b]}", 42 * m);   // 0b101010 m
std::println("{::N[#B]}", 42 * m);   // 0B101010 m
std::println("{::N[#o]}", 42 * m);   // 052 m
std::println("{::N[#x]}", 42 * m);   // 0x2a m
std::println("{::N[#X]}", 42 * m);   // 0X2A m
```

For floating-point values, the `type` token works as follows:

```cpp
std::println("{::N[a]}",   1.2345678 * m);      // 1.3c0ca2a5b1d5dp+0 m
std::println("{::N[.3a]}", 1.2345678 * m);      // 1.3c1p+0 m
std::println("{::N[A]}",   1.2345678 * m);      // 1.3C0CA2A5B1D5DP+0 m
std::println("{::N[.3A]}", 1.2345678 * m);      // 1.3C1P+0 m
std::println("{::N[e]}",   1.2345678 * m);      // 1.234568e+00 m
std::println("{::N[.3e]}", 1.2345678 * m);      // 1.235e+00 m
std::println("{::N[E]}",   1.2345678 * m);      // 1.234568E+00 m
std::println("{::N[.3E]}", 1.2345678 * m);      // 1.235E+00 m
std::println("{::N[g]}",   1.2345678 * m);      // 1.23457 m
std::println("{::N[g]}",   1.2345678e8 * m);    // 1.23457e+08 m
std::println("{::N[.3g]}", 1.2345678 * m);      // 1.23 m
std::println("{::N[.3g]}", 1.2345678e8 * m);    // 1.23e+08 m
std::println("{::N[G]}",   1.2345678 * m);      // 1.23457 m
std::println("{::N[G]}",   1.2345678e8 * m);    // 1.23457E+08 m
std::println("{::N[.3G]}", 1.2345678 * m);      // 1.23 m
std::println("{::N[.3G]}", 1.2345678e8 * m);    // 1.23E+08 m
```

##### 17.4.4.5 Extensions to `std-format-spec`

Both [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) and [[SI]](https://www.bipm.org/en/publications/si-brochure) are recommending printing numbers into separated into groups of three:

> To facilitate the reading of numbers with many digits, these may be separated into groups of three, counting from the decimal sign towards the left and the right. In the case where there is no decimal part (and thus no decimal marker), the counting shall be from the right-most digit, towards the left. No group shall contain more than three digits, except that when there are only four digits before or after the decimal marker it is customary not to use a space to isolate a single digit. Where such separation into groups of three is used, the groups shall be separated by a small space and not by a point or a comma or by any other means.
> 
> EXAMPLE 1: 12 345
> 
> The practice of grouping digits in this way is a matter of choice. It is not always followed in certain specialized applications such as engineering drawings and scripts to be read by a computer. The separation into groups of three should not be used for ordinal numbers used as reference numbers. A year, when given by four digits, shall always be written without a space between the digits.

As of today, no flag in `std-format-spec` would force it. Similar output may be obtained thanks to localization, but international standards mentioned above recommend that for every user, no matter what localization option is being used.

##### 17.4.4.6 Inconsistencies with `std::chrono::duration`

This library prints the quantities and their units according to specific ISO specifications. Unfortunately, this is not the case for `std::chrono::duration`:

```cpp
using my_duration = std::chrono::duration<int, std::ratio<1, 4>>;

inline constexpr Unit auto my_unit = mag_ratio<1, 4> * si::second;

std::println("{}", std::chrono::seconds(42));
std::println("{}", 42 * s);
std::println("{}", my_duration(100));
std::println("{}", 100 * my_unit);
```

The above prints:

```
42s
42 s
100[1/4]s
100 (1/4 s)
```

We are unsure if that is a problem that we should be worried about. If so, we could consider adding ISO-compatible formatting to `std::chrono` abstractions, but it is not planned in the scope of this paper.

### 17.5 Quantity point text output

Text output is provided for `quantity_point` when its point origin equals `default_point_origin(R)` — the library-chosen default for the given reference:

- For references without an offset unit (e.g., `quantity_point<isq::length[m]>`), `default_point_origin` is `natural_point_origin<QuantitySpec>`, the mathematical zero. The stored quantity is unambiguous and can be printed directly:

  ```cpp
  quantity_point qp{42 * m};
  std::println("{}", qp);          // "42 m"
  ```
- For references whose unit carries a built-in origin (e.g., `quantity_point<deg_C>`), `default_point_origin` is the unit’s canonical reference point (`si::ice_point`). The output matches the conventional notation:

  ```cpp
  quantity_point temp = point<deg_C>(20.);
  std::println("{}", temp);        // "20 ℃"
  ```

Text output is **not** provided when a non-default origin is used. The stored value is a displacement from a domain-specific reference whose name the library cannot know. The same numeric value can describe entirely different physical locations depending on the origin — `42 m` above sea level, a mountain top, or the centre of Mars are all distinct points. For such cases the displacement should be extracted explicitly, with an application-defined label added to make the value unambiguous:

```cpp
std::cout << altitude.quantity_ref_from(sea_level) << " AMSL";  // "42 m AMSL"
```

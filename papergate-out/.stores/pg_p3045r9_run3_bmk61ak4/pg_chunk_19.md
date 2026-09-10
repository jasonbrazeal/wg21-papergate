## 17 Text output

A quantity value contains a numerical value and a unit. Both of them may have various text representations. Not only numbers but also units can be formatted in many different ways. Additionally, every dimension can be represented as a text as well.

This chapter will discuss the different options we have here.

*Note: For now, there is no standardized way to handle formatted text input in the C++ standard library, so this paper does not propose any approach to convert text to quantities. If [[P1729R3]](https://wg21.link/p1729r3) will be accepted by the LEWG, then we will add a proper “Text input” chapter as well.*

### 17.1 Symbols

The definitions of dimensions, units, prefixes, and constants require unique text symbols to be assigned for each entity. Those symbols can be composed to express dimensions and units of base and derived quantities.

#### 17.1.1 Symbol definition examples

*Note: The below code examples are based on the latest version of the [[mp-units]](https://mpusz.github.io/mp-units) library and might not be the final version proposed for standardization.*

Dimensions:

```cpp
inline constexpr struct dim_length : base_dimension<"L"> {} dim_length;
inline constexpr struct dim_mass : base_dimension<"M"> {} dim_mass;
inline constexpr struct dim_time : base_dimension<"T"> {} dim_time;
inline constexpr struct dim_electric_current : base_dimension<"I"> {} dim_electric_current;
inline constexpr struct dim_thermodynamic_temperature : base_dimension<{u8"Θ", "O"}> {} dim_thermodynamic_temperature;
inline constexpr struct dim_amount_of_substance : base_dimension<"N"> {} dim_amount_of_substance;
inline constexpr struct dim_luminous_intensity : base_dimension<"J"> {} dim_luminous_intensity;
```

Units:

```cpp
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct gram : named_unit<"g", kind_of<isq::mass>> {} gram;
inline constexpr auto kilogram = kilo<gram>;

inline constexpr struct newton : named_unit<"N", kilogram * metre / square(second)> {} newton;
inline constexpr struct joule : named_unit<"J", newton * metre> {} joule;
inline constexpr struct watt : named_unit<"W", joule / second> {} watt;
inline constexpr struct coulomb : named_unit<"C", ampere * second> {} coulomb;
inline constexpr struct volt : named_unit<"V", watt / ampere> {} volt;
inline constexpr struct farad : named_unit<"F", coulomb / volt> {} farad;
inline constexpr struct ohm : named_unit<{u8"Ω", "ohm"}, volt / ampere> {} ohm;
```

Prefixes:

```cpp
template<PrefixableUnit U> struct micro_ : prefixed_unit<{u8"µ", "u"}, mag_power<10, -6>, U{}> {};
template<PrefixableUnit U> struct milli_ : prefixed_unit<"m", mag_power<10, -3>, U{}> {};
template<PrefixableUnit U> struct centi_ : prefixed_unit<"c", mag_power<10, -2>, U{}> {};
template<PrefixableUnit U> struct deci_  : prefixed_unit<"d", mag_power<10, -1>, U{}> {};
template<PrefixableUnit U> struct deca_  : prefixed_unit<"da", mag_power<10, 1>, U{}> {};
template<PrefixableUnit U> struct hecto_ : prefixed_unit<"h", mag_power<10, 2>, U{}> {};
template<PrefixableUnit U> struct kilo_  : prefixed_unit<"k", mag_power<10, 3>, U{}> {};
template<PrefixableUnit U> struct mega_  : prefixed_unit<"M", mag_power<10, 6>, U{}> {};
```

Constants:

```cpp
inline constexpr struct hyperfine_structure_transition_frequency_of_cs :
  named_constant<{u8"Δν_Cs", "dv_Cs"}, mag<9'192'631'770> * hertz> {} hyperfine_structure_transition_frequency_of_cs;
inline constexpr struct speed_of_light_in_vacuum :
  named_constant<"c", mag<299'792'458> * metre / second> {} speed_of_light_in_vacuum;
inline constexpr struct planck_constant :
  named_constant<"h", mag_ratio<662'607'015, 100'000'000> * mag_power<10, -34> * joule * second> {} planck_constant;
inline constexpr struct elementary_charge :
  named_constant<"e", mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * coulomb> {} elementary_charge;
inline constexpr struct boltzmann_constant :
  named_constant<"k", mag_ratio<1'380'649, 1'000'000> * mag_power<10, -23> * joule / kelvin> {} boltzmann_constant;
inline constexpr struct avogadro_constant :
  named_constant<"N_A", mag_ratio<602'214'076, 100'000'000> * mag_power<10, 23> / mole> {} avogadro_constant;
inline constexpr struct luminous_efficacy :
  named_constant<"K_cd", mag<683> * lumen / watt> {} luminous_efficacy;
```

*Note: Two symbols always have to be provided if the primary symbol contains characters outside of the [basic literal character set](https://en.cppreference.com/w/cpp/language/charset). The first must be provided as a UTF-8 literal and may contain any Unicode characters. The second one must provide an alternative spelling and only use characters from within of [basic literal character set](https://en.cppreference.com/w/cpp/language/charset).*

#### 17.1.2 Lack of Unicode subscript characters

Unicode provides only a minimal set of characters available as subscripts, which are often used to differentiate various constants and quantities of the same kind. To workaround this issue, [[mp-units]](https://mpusz.github.io/mp-units) uses `'_'` character to specify that the following characters should be considered a subscript of the symbol.

#### 17.1.3 Symbols for quantity types

Although the ISQ defined in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides symbols for each quantity type, there is little use for them in the C++ code. In the [[mp-units]](https://mpusz.github.io/mp-units) project, we never had a request to provide such symbol definitions. Even though having them for completeness could be nice, they seem to not be required by the domain experts for their daily jobs. Also, it is worth noting that providing those raises some additional standardization and implementation challenges.

If we decide to provide symbols, the rest of this chapter provides the domain information to assess the complexity and potential issues with standardization and implementation of those.

All ISQ quantities have an official symbol assigned in their definitions, and how those should be printed is exactly specified. [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly states:

> The quantity symbols shall be written in italic (sloping) type, irrespective of the type used in the rest of the text.

Additionally, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) provides additional requirements for printing quantities of vector and tensor characters:

- vectors should be printed with a boldface type or have a right arrow above the letter symbol (e.g., ***a*** or \(\mathit{\overrightarrow{a}}\)),
- tensors should use either boldface sans serif type or have two arrows above the letter symbol (e.g., ***T*** or \(\overrightarrow{\overrightarrow{T}}\)).

*Note: In the above examples, the second symbol with arrows above should also use letters written in italics. The author could not find a way to format it properly in this document.*

There are also a few requirements for printing subscripts of quantity types. [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) states:

> The following principles for the printing of subscripts apply:
> 
> - A subscript that represents a physical quantity or a mathematical variable, such as a running number, is printed in italic (sloping) type.
> - Other subscripts, such as those representing words or fixed numbers, are printed in roman (upright) type.

It is worth noting that only a limited set of Unicode characters are available as subscripts. Those are often used to differentiate various quantities of the same kind.

For example, it is impossible to encode the symbols of the following quantities:

- *c*<sub>sat</sub> - *specific heat capacity at saturated vapour pressure*,
- *μ*<sub>JT</sub> - *Joule-Thomson coefficient*,
- *w*<sub>H<sub>2</sub>O</sub> - *mass fraction of water*,
- *σ*<sub>Ω,E</sub> - *direction and energy distribution of cross section*,
- *d*<sub>1/2</sub> - *half-value thickness*,
- *Φ*<sub>e,λ</sub> - *spectral radiant flux*.

It is important to state that the same issues are related to constant definitions. For them, in the Symbol definition examples chapter, we proposed to use the `'_'` character instead, as stated in Lack of Unicode subscript characters. We could use the same practice here.

Another challenge here might be related to the fact that [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) often provides more than one symbol for the same quantity. For example:

- *frequency* can use *f* or *ν*,
- *time constant* can use *τ* or *T* (*T* is also the only symbol provided for the *period duration* quantity),
- *thickness* can use *d* or *δ*,
- *diameter* can use *d* or *D* (which again conflicts with the *diameter* symbol).

Last but not least, it is worth noting that symbols of ISQ base quantities are not necessary the same as official dimension symbols of those quantities:

| Quantity type | Quantity type symbol | Dimension symbol |
| --- | --- | --- |
| *length* | *l*, *L* | L |
| *mass* | *m* | M |
| *time* | *t* | T |
| *electric current* | *I*, *i* | I |
| *thermodynamic temperature* | *T*, *Θ* | Θ |
| *amount of substance* | *n*(X) | N |
| *luminous intensity* | *I*<sub>v</sub>, (*I*) | J |

Founding a way to define, use, and print named quantity types is not enough. What should also be covered here is the text output of derived quantities. There are plenty of operations that one might do on scalar, vector, and tensor quantities, and all of them result in another quantity type, which should also be able to be printed in the console text output.

Taking all the challenges and issues mentioned above, we do not propose providing quantity type symbols in their definitions and any text input/output support for those.

#### 17.1.4 `fixed_string`

As shown above, symbols are provided as class NTTPs in the library. This means that the string type used for such a purpose has to satisfy the structural type requirements of the C++ language. One of such requirements is to expose all the data members publicly. So far, none of the existing string types in the C++ standard library satisfies such requirements. This is why we need to introduce a new type.

Such type should:

- satisfy structural type requirements,
- be equality comparable and potentially totally ordered,
- store and provide concatenation support for zero-ended strings,
- provide storage that, if set at compile time, would also be available for read-only access at runtime,
- provide at least read-only access to the contained storage.

Such a type does not need to expose a string-like interface. In case its interface is immutable, we can easily wrap it with `std::string_view` to get such an interface for free.

This type is being proposed separately in [[P3094R6]](https://wg21.link/p3094r6).

#### 17.1.5 `symbol_text`

Many symbols of units, prefixes, and constants require using a Unicode character set. For example:

- Θ - thermodynamic temperature dimension
- µ - micro
- Ω - ohm
- ℃ - degree Celsius
- ℉ - degree Fahrenheit
- ° - degree
- ′ - arcminute
- ″ - arcsecond
- ᵍ - gradian
- Å - angstrom
- M_☉ - solar mass
- Δν_Cs - hyperfine structure transition frequency of Cs
- g₀ - standard gravity
- μ₀ - magnetic constant
- c₀ - speed of light
- H₀ - hubble constant

The library should provide such Unicode output by default to be consistent with official systems’ specifications.

On the other hand, plenty of terminals do not support Unicode characters. Also, general engineering experience shows that people often prefer to work with a basic literal character set. This is why all such entities should provide an alternative spelling in their definitions.

This is where `symbol_text` comes into play. It is a simple wrapper over the two `fixed_string` objects:

```cpp
template<std::size_t N, std::size_t M>
class symbol_text {
public:
  fixed_u8string<N> utf8_;    // exposition only
  fixed_string<M> portable_;  // exposition only

  constexpr explicit(false) symbol_text(char ch);
  consteval explicit(false) symbol_text(const char (&txt)[N + 1]);
  constexpr explicit(false) symbol_text(const fixed_string<N>& txt);
  consteval symbol_text(const char8_t (&u)[N + 1], const char (&a)[M + 1]);
  constexpr symbol_text(const fixed_u8string<N>& u, const fixed_string<M>& a);

  constexpr const auto& utf8() const;
  constexpr const auto& portable() const;

  constexpr bool empty() const;

  template<std::size_t N2, std::size_t M2>
  constexpr friend symbol_text<N + N2, M + M2> operator+(const symbol_text& lhs, const symbol_text<N2, M2>& rhs);

  template<std::size_t N2, std::size_t M2>
  friend constexpr auto operator<=>(const symbol_text& lhs, const symbol_text<N2, M2>& rhs) noexcept;

  template<std::size_t N2, std::size_t M2>
  friend constexpr bool operator==(const symbol_text& lhs, const symbol_text<N2, M2>& rhs) noexcept;
};

symbol_text(char) -> symbol_text<1, 1>;

template<std::size_t N>
symbol_text(const char (&)[N]) -> symbol_text<N - 1, N - 1>;

template<std::size_t N>
symbol_text(const fixed_string<N>&) -> symbol_text<N, N>;

template<std::size_t N, std::size_t M>
symbol_text(const char8_t (&)[N], const char (&)[M]) -> symbol_text<N - 1, M - 1>;

template<std::size_t N, std::size_t M>
symbol_text(const fixed_u8string<N>&, const fixed_string<M>&) -> symbol_text<N, M>;
```

It is important to note that the `utf8_` text representation is used only when the output is of either:

- `char8_t` type,
- `char` and `std::text_encoding::literal().mib() == std::text_encoding::id::UTF8`.

Otherwise, `portable_` is used.

#### 17.1.6 Symbols for derived entities

##### 17.1.6.1 `character_set`

ISQ and [[SI]](https://www.bipm.org/en/publications/si-brochure) standards always specify symbols using Unicode encoding. This is why it is a default and primary target for text output. However, in some applications or environments, a standard portable text output using only the characters from the [basic literal character set](https://en.cppreference.com/w/cpp/language/charset) can be preferred by users.

This is why the library provides an option to change the default encoding to the portable one with:

```cpp
enum class character_set : std::int8_t {
  utf8,        // µs; m³;  L²MT⁻³
  portable,    // us; m^3; L^2MT^-3
  default_encoding = utf8
};
```

##### 17.1.6.2 Symbols of derived dimensions

###### 17.1.6.2.1 `dimension_symbol_formatting`

`dimension_symbol_formatting` is a data type describing the configuration of the symbol generation algorithm.

```cpp
struct dimension_symbol_formatting {
  character_set char_set = character_set::default_encoding;
};
```

###### 17.1.6.2.2 `dimension_symbol()`

Returns a `std::string_view` with the symbol of a dimension for the provided configuration:

```cpp
template<dimension_symbol_formatting fmt = dimension_symbol_formatting{}, typename CharT = char, Dimension D>
consteval std::string_view dimension_symbol(D);
```

*Note: It could be refactored to `dimension_symbol(D, fmt)` when [[P1045R1]](https://wg21.link/p1045r1) is available.*

For example:

```cpp
static_assert(dimension_symbol<{.char_set = character_set::portable}>(isq::power.dimension) == "L^2MT^-3");
```

###### 17.1.6.2.3 `dimension_symbol_to()`

Inserts the generated dimension symbol into the output text iterator at runtime.

```cpp
template<typename CharT = char, std::output_iterator<CharT> Out, Dimension D>
constexpr Out dimension_symbol_to(Out out, D d, dimension_symbol_formatting fmt = dimension_symbol_formatting{});
```

For example:

```cpp
std::string txt;
dimension_symbol_to(std::back_inserter(txt), isq::power.dimension, {.char_set = character_set::portable});
std::cout << txt << "\n";
```

The above prints:

```
L^2MT^-3
```

##### 17.1.6.3 Symbols of derived units

###### 17.1.6.3.1 `unit_symbol_formatting`

`unit_symbol_formatting` is a data type describing the configuration of the symbol generation algorithm. It contains three orthogonal fields, each with a default value.

```cpp
enum class unit_symbol_solidus : std::int8_t {
  one_denominator,  // m/s;   kg m⁻¹ s⁻¹
  always,           // m/s;   kg/(m s)
  never,            // m s⁻¹; kg m⁻¹ s⁻¹
  default_solidus = one_denominator
};

enum class unit_symbol_separator : std::int8_t {
  space,          // kg m²/s²
  half_high_dot,  // kg⋅m²/s²  (valid only for Unicode encoding)
  default_separator = space
};

struct unit_symbol_formatting {
  character_set char_set = character_set::default_encoding;
  unit_symbol_solidus solidus = unit_symbol_solidus::default_solidus;
  unit_symbol_separator separator = unit_symbol_separator::default_separator;
};
```

`unit_symbol_solidus` impacts how the division of unit symbols is being presented in the text output. By default, the ‘/’ will be printed if only one unit component is in the denominator. Otherwise, the exponent syntax will be used.

`unit_symbol_separator` specifies how multiple multiplied units should be separated from each other. By default, the space (’ ’) will be used as a separator.

###### 17.1.6.3.2 `unit_symbol()`

Returns a `std::string_view` with the symbol of a unit for the provided configuration:

```cpp
template<unit_symbol_formatting fmt = unit_symbol_formatting{}, typename CharT = char, Unit U>
consteval std::string_view unit_symbol(U);
```

*Note: It could be refactored to `unit_symbol(U, fmt)` when [[P1045R1]](https://wg21.link/p1045r1) is available.*

For example:

```cpp
static_assert(unit_symbol<{.solidus = unit_symbol_solidus::never,
                           .separator = unit_symbol_separator::half_high_dot}>(kg * m / s2) == "kg⋅m⋅s⁻²");
```

###### 17.1.6.3.3 `unit_symbol_to()`

Inserts the generated unit symbol into the output text iterator at runtime.

```cpp
template<typename CharT = char, std::output_iterator<CharT> Out, Unit U>
constexpr Out unit_symbol_to(Out out, U u, unit_symbol_formatting fmt = unit_symbol_formatting{});
```

For example:

```cpp
std::string txt;
unit_symbol_to(std::back_inserter(txt), kg * m / s2,
               {.solidus = unit_symbol_solidus::never, .separator = unit_symbol_separator::half_high_dot});
std::cout << txt << "\n";
```

The above prints:

```
kg⋅m⋅s⁻²
```

#### 17.1.7 Symbols of scaled units

Here are a few examples of scaled unit text output in action:

```cpp
inline constexpr Unit auto my_unit_1 = mag_ratio<1, 4> * si::second;
inline constexpr Unit auto my_unit_2 = mag_power<10, 4> * si::metre;
inline constexpr Unit auto my_unit_3 = mag<25> * mag_power<10, 4> * si::metre;

std::cout << 100 * my_unit_1 << "\n";
std::cout << 100 * my_unit_2 << "\n";
std::cout << 100 * my_unit_3 << "\n";
```

The above prints:

```
100 (1/4 s)
100 (10⁴ m)
100 (25 × 10⁴ m)
```

As we can see a scaled unit has a magnitude and a reference unit. To denote the scope of such a unit, we currently enclose it in `(...)`.

In most cases scaled units are hidden behind named units so the above outputs are a bit artifical. However, there are a few real-life where a user directly faces a scaled unit. For example:

```cpp
inline constexpr Unit auto L_per_100km = L / (mag<100> * km);
```

The above is a derived unit of litre divided by a scaled unit of `100` kilometers. For example, the following:

```cpp
std::cout << 6.7 * L_per_100km << "\n";
```

prints:

```
6.7 L/(100 km)
```

The current output of the fuel consumption unit is only one of the options here. It favors a derived unit over a scaled unit (i.e., the resulting type is `derived_unit<non_si::litre, per<scaled_unit<{some magnitude representing 100}, si::kilo<si::metre>>>>`). Another option would be to prefer a scaled unit so the result would be `scaled_unit<{some magnitude representing 1/100}, derived_unit<non_si::litre, per<si::kilo<si::metre>>>` and the output would look like:

```
6.7 (1/100 L/km)
```

The output could also look like this:

```
6.7 × 10⁻² L/km
```

but this, even though it is mathematically correct, is the poorest to express the intent here. The unit we use daily is the number of liters consumed for `100 km`, and not for a single `km`, which the last output suggests (i.e., “6.7 hundredths of a liter per kilometer”).

This is why we initially proposed the first version. However, on one of the meetings it was brought that this approach also leads to some issues in case of other quantities.

According to the current rules, the following code:

```cpp
std::cout << 10 * L_per_100km * (20 * km) << "\n";
```

prints the following output:

```
200 L km/(100 km)
```

At least for now, the units do not simplify which may look suprising.

Another thing worth noting here is that in case a value of a numerator or denumerator is greater or equal `1000` we use an exponential notation:

```cpp
inline constexpr Unit auto L_per_1000km = L / (mag<1000> * km);
std::cout << 10 * L_per_1000km << "\n";
```

prints:

```
10 L/(10³ km)
```

A motivation for that is that typically, for a value of `1000` or greater, a user could use a larger SI prefix (even though it would not make sense for kilometers).

All of the above are the inputs for a discussion and we are open to fine-tuning this behavior according to the LEWG guidelines.

#### 17.1.8 Symbols of common units

Some common units expressed with a specialization of the `common_unit` class template need special printing rules for their symbols. As they represent a minimum set of equivalent common units resulting from the addition or subtraction of multiple quantities, we print all of them as a scaled version of the source unit. For example, the following:

```cpp
std::cout << 1 * km + 1 * mi << "\n";
std::cout << 1 * nmi + 1 * mi << "\n";
std::cout << 1 * km / h + 1 * m / s << "\n";
std::cout << 1. * rad + 1. * deg << "\n";
```

prints:

```
40771 [(1/25146 mi), (1/15625 km)]
108167 [(1/50292 mi), (1/57875 nmi)]
23 [(1/5 km/h), (1/18 m/s)]
183.142 [(1/π°), (1/180 rad)]
```

Thanks to the above, it might be easier for the user to reason about the magnitude of the resulting unit and its impact on the value stored in the quantity.

It is important to note that this output is provided only for intermediate results of the equations, as shown above. A user usually knows which unit should be used, and explicit conversion can be made to achieve that. For example:

```cpp
std::cout << (1 * km + 1 * mi).in<double>(km) << "\n";
```

prints:

```
2.60934 km
```

#### 17.1.9 Unicode characters and their portable replacements

Library’s framework requires some Unicode characters for text output. The below table lists all of them together with the recommended portable replacements:

| Name | Symbol | C++ code | Portable alternative |
| --- | --- | --- | --- |
| SUPERSCRIPT ZERO | ⁰ | `u8"\u2070"` | `"0"` |
| SUPERSCRIPT ONE | ¹ | `u8"\u00b9"` | `"1"` |
| SUPERSCRIPT TWO | ² | `u8"\u00b2"` | `"2"` |
| SUPERSCRIPT THREE | ³ | `u8"\u00b3"` | `"3"` |
| SUPERSCRIPT FOUR | ⁴ | `u8"\u2074"` | `"4"` |
| SUPERSCRIPT FIVE | ⁵ | `u8"\u2075"` | `"5"` |
| SUPERSCRIPT SIX | ⁶ | `u8"\u2076"` | `"6"` |
| SUPERSCRIPT SEVEN | ⁷ | `u8"\u2077"` | `"7"` |
| SUPERSCRIPT EIGHT | ⁸ | `u8"\u2078"` | `"8"` |
| SUPERSCRIPT NINE | ⁹ | `u8"\u2079"` | `"9"` |
| SUPERSCRIPT MINUS | ⁻ | `u8"\u207b"` | `"-"` |
| MULTIPLICATION SIGN | × | `u8"\u00d7"` | `"x"` |
| GREEK SMALL LETTER PI | π | `u8"\u03c0"` | `"pi"` |
| DOT OPERATOR | ⋅ | `u8"\u22C5"` | `<none>`<sup>1</sup> |

Here is an example of how the above are being used in a code:

```cpp
static_assert(unit_symbol(kilogram * metre / square(second)) == "kg m/s²");
static_assert(unit_symbol<usf{.separator = half_high_dot}>(kilogram * metre / square(second)) == "kg⋅m/s²");
static_assert(unit_symbol<usf{.char_set = portable}>(kilogram * metre / square(second)) == "kg m/s^2");
static_assert(unit_symbol<usf{.solidus = never}>(kilogram * metre / square(second)) == "kg m s⁻²");
static_assert(unit_symbol<usf{.char_set = portable, .solidus = never}>(kilogram * metre / square(second)) == "kg m s^-2");

static_assert(unit_symbol(mag_ratio<1, 18000> * metre / second) == "[1/18 × 10⁻³ m]/s");
static_assert(unit_symbol<usf{.char_set = portable}>(mag_ratio<1, 18000> * metre / second) == "[1/18 x 10^-3 m]/s");

static_assert(unit_symbol(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[2⁻¹ π⁻¹ m]");
static_assert(unit_symbol<usf{.solidus = always}>(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[1/(2 π) m]");
static_assert(unit_symbol<usf{.char_set = portable, .solidus = always}>(mag<1> / (mag<2> * mag<pi_c>)*metre) == "[1/(2 pi) m]");
```

Additionally, if we decide to provide `per_mille` unit together with the framework (next to `one`, `percent`, and `parts_per_million`) we will need a symbol for it as well:

| Name | Symbol | C++ code | Portable alternative |
| --- | --- | --- | --- |
| PER MILLE SIGN | ‰ | u8”030” | ??? |

There is no good choice for a portable replacement here. We may try to be brief and use “%o” ([Wikipedia uses this symbol as a redirect for per mille](https://en.wikipedia.org/wiki/Per_mille)) or provide a longer textual string. The problem is that there is more than one option to chose from here ([names mentioned in Wikipedia](https://en.wikipedia.org/wiki/Per_mille)):

- “per mille” (even though it is consistent with the official name it is not a good option here as it looks like multiplication of two symbols),
- “per mil” and “per mill” (same as above),
- “permil”, “permill”, and “permille” (how to spell it correctly?).

### 17.2 `space_before_unit_symbol` customization point

The [[SI]](https://www.bipm.org/en/publications/si-brochure) says:

> The numerical value always precedes the unit and a space is always used to separate the unit from the number. … The only exceptions to this rule are for the unit symbols for degree, minute and second for plane angle, `°`, `′` and `″`, respectively, for which no space is left between the numerical value and the unit symbol.

There are more units with such properties. For example, per mille(`‰`).

To support the above, the library exposes `space_before_unit_symbol` customization point. By default, its value is `true` for all the units. This means that a number and a unit will be separated by the space in the output text. To change this behavior, a user should provide a explicit specialization for a specific unit:

```cpp
template<>
constexpr bool space_before_unit_symbol<non_si::degree> = false;
```

The above works only for the default formatting or for the format strings that use `%?` placement field (`std::format("{}", q)` is equivalent to `std::format("{:%N%?%U}", q)`).

In case a user provides custom format specification (e.g., `std::format("{:%N %U}", q)`), the library will always obey this specification for all the units (no matter what the actual value of the `space_before_unit_symbol` customization point is) and the separating space will always be used in this case.

### 17.3 Output streams

The easiest way to print a dimension, unit, or quantity is to provide its object to the output stream:

```cpp
const quantity v1 = avg_speed(220. * km, 2 * h);
const quantity v2 = avg_speed(140. * mi, 2 * h);
std::cout << v1 << '\n';            // 110 km/h
std::cout << v2 << '\n';            // 70 mi/h
std::cout << v2.unit << '\n';       // mi/h
std::cout << v2.dimension << '\n';  // LT⁻¹
```

The text output will always print the value using the default formatting for this entity.

#### 17.3.1 Output stream formatting

Only basic formatting can be applied for output streams. It includes control over width, fill, and alignment.

The numerical value of the quantity will be printed according to the current stream state and standard manipulators may be used to customize that (assuming that the underlying representation type respects them).

```cpp
std::cout << "|" << std::setw(10) << 123 * m << "|\n";                       // |     123 m|
std::cout << "|" << std::setw(10) << std::left << 123 * m << "|\n";          // |123 m     |
std::cout << "|" << std::setw(10) << std::setfill('*') << 123 * m << "|\n";  // |123 m*****|
```

Detailed formatting of any entity may be obtained with `std::format()` usage and then provided to the stream output if needed.

*Note: Custom stream manipulators may be provided to control a dimension and unit symbol output if requested by WG21.*

### 17.4 Text formatting

The library provides custom formatters for `std::format` facility, which allows fine-grained control over what and how it is being printed in the text output.

#### 17.4.1 Controlling width, fill, and alignment

Formatting grammar for all the entities provides control over width, fill, and alignment. The C++ standard grammar tokens `fill-and-align` and `width` are being used. They treat the entity as a contiguous text to be aligned. For example, here are a few examples of the quantity numerical value and symbol formatting:

```cpp
std::println("|{:0}|", 123 * m);     // |123 m|
std::println("|{:10}|", 123 * m);    // |     123 m|
std::println("|{:<10}|", 123 * m);   // |123 m     |
std::println("|{:>10}|", 123 * m);   // |     123 m|
std::println("|{:^10}|", 123 * m);   // |  123 m   |
std::println("|{:*<10}|", 123 * m);  // |123 m*****|
std::println("|{:*>10}|", 123 * m);  // |*****123 m|
std::println("|{:*^10}|", 123 * m);  // |**123 m***|
```

It is important to note that in the second line above, the quantity text is aligned to the right by default, which is consistent with the formatting of numeric types. Units and dimensions behave as text and, thus, are aligned to the left by default.

#### 17.4.2 Dimension formatting

```
dimension-format-spec = [fill-and-align], [width], [dimension-spec];
dimension-spec        = [character-set];
character-set         = 'U' | 'P';
```

In the above grammar:

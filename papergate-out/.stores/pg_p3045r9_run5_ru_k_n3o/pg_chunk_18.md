
Notice, that even though all of those quantities have the same dimension and can be expressed in the same units, they have different quantity equations used to create them implicitly:

- `energy` is the most generic one and thus can be created from base quantities of `mass`, `length`, and `time`. As those are also the roots of quantities of their kinds and all other quantities are implicitly convertible to them, it means that an `energy` can be implicitly constructed from any quantity having proper powers of *mass*, *length*, and *time*.

  ```cpp
  static_assert(implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::energy));
  static_assert(implicitly_convertible(isq::mass * pow<2>(isq::height) / pow<2>(isq::time), isq::energy));
  ```
- `mechanical_energy` is a more “specialized” quantity than `energy` (not every `energy` is a `mechanical_energy`). It is why an explicit cast is needed to convert from either `energy` or the results of its quantity equation.

  ```cpp
  static_assert(!implicitly_convertible(isq::energy, isq::mechanical_energy));
  static_assert(explicitly_convertible(isq::energy, isq::mechanical_energy));
  static_assert(!implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::mechanical_energy));
  static_assert(explicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), isq::mechanical_energy));
  ```
- `gravitational_potential_energy` is not only even more specialized one but additionally, it is special in a way that it provides its own “constrained” quantity equation. Maybe not every `mass * pow<2>(length) / pow<2>(time)` is a `gravitational_potential_energy`, but every `mass * acceleration_of_free_fall * height` is.

  ```cpp
  static_assert(!implicitly_convertible(isq::energy, gravitational_potential_energy));
  static_assert(explicitly_convertible(isq::energy, gravitational_potential_energy));
  static_assert(!implicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), gravitational_potential_energy));
  static_assert(explicitly_convertible(isq::mass * pow<2>(isq::length) / pow<2>(isq::time), gravitational_potential_energy));
  static_assert(implicitly_convertible(isq::mass * isq::acceleration_of_free_fall * isq::height, gravitational_potential_energy));
  ```

#### 16.1.6 Modeling a quantity kind

In the physical units library, we also need an abstraction describing an entire family of quantities of the same kind. Such quantities have not only the same dimension but also can be expressed in the same units.

To annotate a quantity to represent its kind (and not just a hierarchy tree’s root quantity), we introduced a `kind_of<>` specifier. For example, to express any quantity of *length*, we need to specify `kind_of<isq::length>`. That entity behaves as any quantity of its kind. This means that it is implicitly convertible to any quantity in a tree:

```cpp
static_assert(!implicitly_convertible(isq::length, isq::height));
static_assert(implicitly_convertible(kind_of<isq::length>, isq::height));
```

Additionally, the result of operations on quantity kinds is also a quantity kind:

```cpp
static_assert(same_type<kind_of<isq::length> / kind_of<isq::time>, kind_of<isq::length / isq::time>>);
```

However, if at least one equation’s operand is not a quantity kind, the result becomes a “strong” quantity where all the kinds are converted to the hierarchy tree’s root quantities:

```cpp
static_assert(!same_type<kind_of<isq::length> / isq::time, kind_of<isq::length / isq::time>>);
static_assert(same_type<kind_of<isq::length> / isq::time, isq::length / isq::time>);
```

Please note that only a root quantity from the hierarchy tree or the one marked with `is_kind` specifier in the `quantity_spec` definition can be put as a template parameter to the `kind_of` specifier. For example, `kind_of<isq::width>` will fail to compile. However, we can call `get_kind(q)` to obtain a kind of any quantity:

```cpp
static_assert(get_kind(isq::width) == kind_of<isq::length>);
```

#### 16.1.7 Creating distinct quantity kinds with `is_kind`

Dimension-based type safety prevents many errors, but quantities may share the same dimension while representing fundamentally incompatible physical concepts. The `is_kind` specifier creates distinct quantity types within a hierarchy that cannot be mixed despite sharing dimension and parent quantity properties.

##### 16.1.7.1 Design rationale

The `is_kind` specifier addresses cases where multiple incompatible concepts must share a parent quantity’s properties (unit, quantity type) while remaining isolated from each other. This is necessary when quantities cannot be meaningfully added or compared without explicit conversion, yet derive from the same physical basis.

The `is_kind` specifier creates subkinds within an existing quantity hierarchy tree, not independent trees. Subkinds inherit properties from their parent:

- Unit of measure: *fluid head* and *water head* inherit metre from *height*; *angular measure* inherits one from *dimensionless*
- Quantity type: Subkinds inherit their parent’s quantity type, essential when they appear in derived quantities (e.g., *sampling rate* and *tempo* can use Hz because they properly model a dimensionless component divided by *duration*)

For completely independent quantities with different dimension trees, separate root quantities should be defined instead (e.g., *frequency* and *activity* are independent roots, not subkinds).

Examples:

- *Angular measure* (rad), *solid angular measure* (sr), *storage capacity* (bit) — subkinds of *dimensionless*
- *Fluid head* and *water head* in hydraulic engineering — subkinds of *height* (dimension of *length*)

##### 16.1.7.2 Syntax

A distinct quantity kind is defined by adding `is_kind` to the `quantity_spec` definition:

```cpp
inline constexpr struct fluid_head : quantity_spec<isq::height, is_kind> {} fluid_head;
inline constexpr struct water_head : quantity_spec<isq::height, is_kind> {} water_head;
```

Both `fluid_head` and `water_head` are subkinds of *height* (inheriting dimension of *length* and unit of metre), but `is_kind` makes them distinct incompatible kinds requiring explicit conversion.

##### 16.1.7.3 Type safety properties

Quantities marked with `is_kind` enforce strict type boundaries:

1. No implicit or explicit conversion between different kinds:

   ```cpp
   static_assert(!implicitly_convertible(fluid_head, water_head));
   static_assert(!explicitly_convertible(fluid_head, water_head));
   static_assert(!castable(fluid_head, water_head));
   ```
2. No arithmetic operations or comparisons between different kinds:

   ```cpp
   quantity h_fluid = fluid_head(2 * m);
   quantity h_water = water_head(10 * m);
   
   // auto sum = h_fluid + h_water;  // Compile-time error
   // bool cmp = h_fluid < h_water;  // Compile-time error
   ```
3. Explicit conversion to base quantity required for generic operations:

   ```cpp
   quantity h1 = isq::height(h_fluid);
   quantity h2 = isq::height(h_water);
   quantity sum = h1 + h2;  // OK: both are isq::height
   ```

   Note: Implicit conversion from `is_kind` quantities to their base is not allowed:

   ```cpp
   quantity<isq::height[m]> h = h_fluid;  // Compile-time error
   ```
4. Compatible with `kind_of` introspection:

   ```cpp
   static_assert(get_kind(fluid_head) == kind_of<fluid_head>);
   static_assert(get_kind(water_head) == kind_of<water_head>);
   static_assert(get_kind(isq::height) == kind_of<isq::length>);
   
   static_assert(get_kind(fluid_head) != get_kind(water_head));
   static_assert(get_kind(fluid_head) != get_kind(isq::height));
   ```

### 16.2 Systems of units

Modeling a system of units is the most important feature and a selling point of every physical units library. Thanks to that, the library can protect users from performing invalid operations on quantities and provide automated conversion factors between various compatible units.

Probably all the libraries in the wild model the [[SI]](https://www.bipm.org/en/publications/si-brochure) or at least most of it (refer to SI units of quantities of the same dimension but different kinds for more details) and many of them provide support for additional units belonging to various other systems (e.g., imperial).

#### 16.2.1 Systems of units are based on systems of quantities

Systems of quantities specify a set of quantities and equations relating to those quantities. Those equations do not take any unit or a numerical representation into account at all. In order to create a quantity, we need to add those missing pieces of information. This is where a system of units kicks in.

The [[SI]](https://www.bipm.org/en/publications/si-brochure) is explicitly stated to be based on the ISQ. Among others, it defines seven base units, one for each base quantity. In the library, this is expressed by associating a quantity kind to a unit being defined:

```cpp
inline constexpr struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
```

The `kind_of<isq::length>` above states explicitly that this unit has an associated quantity kind. In other words, `si::metre` (and scaled units based on it) can be used to express the amount of any quantity of kind *length*.

#### 16.2.2 Units compose

One of the strongest points of the [[SI]](https://www.bipm.org/en/publications/si-brochure) system is that its units compose. This allows providing thousands of different units for hundreds of various quantities with a really small set of predefined units and prefixes. For example, one can write:

```cpp
quantity<si::metre / si::second> q;
```

to express a quantity of speed. The resulting quantity type is implicitly inferred from the unit equation by repeating exactly the same operations on the associated quantity kinds.

As units are regular values, we can easily provide a helper ad-hoc unit with:

```cpp
constexpr auto mps = si::metre / si::second;
quantity<mps> q;
```

#### 16.2.3 Many shades of the same unit

The [[SI]](https://www.bipm.org/en/publications/si-brochure) provides the names for 22 common coherent units of 22 derived quantities.

Each such named derived unit is a result of a specific predefined unit equation. For example, a unit of power quantity is defined as:

```cpp
inline constexpr struct watt : named_unit<"W", joule / second> {} watt;
```

However, a power quantity can be expressed in other units as well. For example, the following:

```cpp
auto q1 = 42 * W;
std::cout << q1 << "\n";
std::cout << q1.in(J / s) << "\n";
std::cout << q1.in(N * m / s) << "\n";
std::cout << q1.in(kg * m2 / s3) << "\n";
```

prints:

```
42 W
42 J/s
42 N m/s
42 kg m²/s³
```

All of the above quantities are equivalent and mean exactly the same.

#### 16.2.4 Constraining a derived unit to work only with a specific derived quantity

Some derived units are valid only for specific derived quantities. For example, [[SI]](https://www.bipm.org/en/publications/si-brochure) specifies both hertz and becquerel derived units with the same unit equation \(s^{-1}\). However, it also explicitly states:

> The hertz shall only be used for periodic phenomena and the becquerel shall only be used for stochastic processes in activity referred to a radionuclide.

This is why it is important for the library to allow constraining such units to be used only with a specific quantity kind:

```cpp
inline constexpr struct hertz : named_unit<"Hz", one / second, kind_of<isq::frequency>> {} hertz;
inline constexpr struct becquerel : named_unit<"Bq", one / second, kind_of<isq::activity>> {} becquerel;
```

With the above, `hertz` can only be used for *frequencies*, while `becquerel` should only be used for quantities of *activity*. This means that the following equation will not compile, improving the type-safety of the library:

```cpp
auto q = 1 * Hz + 1 * Bq;   // Fails to compile
```

#### 16.2.5 Prefixed units

Besides named units, the SI specifies also 24 prefixes (all being a power of `10`) that can be prepended to all named units to obtain various scaled versions of them.

Implementation of `std::ratio` provided by all major compilers is able to express only 16 of them. This is why, we had to find an alternative way to represent a unit’s magnitude in a more flexible way.

Each prefix is implemented as:

```cpp
template<PrefixableUnit U> struct quecto_ : prefixed_unit<"q", mag_power<10, -30>, U{}> {};
template<PrefixableUnit auto U> constexpr quecto_<decltype(U)> quecto;
```

and then a unit can be prefixed in the following way:

```cpp
inline constexpr auto qm = quecto<metre>;
```

The usage of `mag_power` not only enables providing support for SI prefixes, but it can also efficiently represent any rational magnitude. For example, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) prefixes used in the IT industry can be implemented as:

```cpp
template<PrefixableUnit U> struct yobi_ : prefixed_unit<"Yi", mag_power<2, 80>, U{}> {};
template<PrefixableUnit auto U> constexpr yobi_<decltype(U)> yobi;
```

*Please note that to improve the readability of generated types that are exposed in compiler errors and debugger, the variable template takes an NTTP and converts it to its type before passing the argument to the associated class template.*

#### 16.2.6 Scaled units

In the [[SI]](https://www.bipm.org/en/publications/si-brochure), all units are either base or derived units or prefixed versions of those. However, those are not the only options possible.

For example, there is a list of off-system units accepted for use with [[SI]](https://www.bipm.org/en/publications/si-brochure). All of those are scaled versions of the [[SI]](https://www.bipm.org/en/publications/si-brochure) units with ratios that can’t be explicitly expressed with predefined SI prefixes. Those include units like minute, hour, or electronvolt:

```cpp
inline constexpr struct minute : named_unit<"min", mag<60> * si::second> {} minute;
inline constexpr struct hour : named_unit<"h", mag<60> * minute> {} hour;
inline constexpr struct electronvolt : named_unit<"eV",
    mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * si::joule> {} electronvolt;
```

Also, units of other systems of units are often defined in terms of scaled versions of other (often SI) units. For example, the international yard is defined as:

```cpp
inline constexpr struct yard : named_unit<"yd", mag_ratio<9'144, 10'000> * si::metre> {} yard;
```

and then a `foot` can be defined as:

```cpp
inline constexpr struct foot : named_unit<"ft", mag_ratio<1, 3> * yard> {} foot;
```

For some units, a magnitude might also be irrational. The best example here is a `degree` which is defined using a floating-point magnitude having a factor of the number π (Pi):

```cpp
inline constexpr struct pi_c : mag_constant<{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, std::numbers::pi_v<long double>> {} pi_c;
inline constexpr struct pi : named_constant<symbol_text{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, mag<pi_c> * one> {} pi;
inline constexpr auto π /* U+03C0 GREEK SMALL LETTER PI */ = pi;
```

```cpp
inline constexpr struct degree : named_unit<{u8"°", "deg"}, mag_ratio<1, 180> * π * si::radian> {} degree;
```

#### 16.2.7 Common units

Adding, subtracting, or comparing two quantities of different units will force the library to find a common unit for those. This is to prevent data truncation. For the cases when one of the units is an integral multiple of the other, the resulting quantity will use a “smaller” one in its result. For example:

```cpp
static_assert((1 * kg + 1 * g).unit == g);
static_assert((1 * km + 1 * mm).unit == mm);
static_assert((1 * yd + 1 * mi).unit == yd);
```

However, in many cases an arithmetic operation on quantities of different units will result in a yet another unit. This happens when none of the source units is an integral multiple of another. In such cases, the library returns a special type that denotes that we are dealing with a common unit of such an equation:

```cpp
quantity q1 = 1 * km + 1 * mi; // quantity<common_unit<international::mile, si::kilo_<si::metre>>{}, int>
quantity q2 = 1. * rad + 1. * deg; // quantity<common_unit<si::degree, si::radian>{}, double>
```

The above is to not privilege any unit in the library:

- we shouldn’t introduce an unmentioned unit into computations (e.g., converting a `1 * mi + 1 * nmi` computation to `m` because `m` could be the privileged SI base unit),
- we shouldn’t go looking for specific units (e.g., converting a `1 * m + 1 * cm` computation to `m` because `m` is the privileged SI base unit).

Please note, that a user should never explicitly instantiate a `common_unit` class template. The library’s framework will do it based on the provided quantity equation.

#### 16.2.8 Unit symbols

Units are available via their full names or through their short symbols. To use a long version, it is enough to type:

```cpp
quantity q1 = 42 * si::metre / si::second;
quantity q2 = 42 * si::kilo<si::metre> / si::hour;
```

To simplify how we spell it a short, user-friendly symbols are provided in a dedicated subnamespace in systems definitions:

```cpp
namespace si::unit_symbols {

constexpr auto m = si::metre;
constexpr auto km = si::kilo<si::metre>;
constexpr auto s = si::second;
constexpr auto h = si::hour;

}
```

Unit symbols introduce a lot of short identifiers into the current namespace. This is why they are opt-in. A user has to explicitly “import” them from a dedicated `unit_symbols` namespace:

```cpp
using namespace si::unit_symbols;

quantity q1 = 42 * m / s;
quantity q2 = 42 * km / h;
```

or:

```cpp
using si::unit_symbols::m;
using si::unit_symbols::km;
using si::unit_symbols::s;
using si::unit_symbols::h;

quantity q1 = 42 * m / s;
quantity q2 = 42 * km / h;
```

Thanks to [[P1949R7]](https://wg21.link/p1949r7) we also provide alternative object identifiers using Unicode characters in their names for most unit symbols. The code using Unicode looks nicer, but it is harder to type on the keyboard. This is why we provide both versions of identifiers for such units.

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Portable only</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">With Unicode characters</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity resistance = 60 * kohm;
quantity capacitance = 100 * uF;</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity resistance = 60 * kΩ;
quantity capacitance = 100 * µF;</code></pre></td>
</tr>
</table>

It is worth noting that not all such units may get Unicode identifiers. Some of them do not have the XID_Start property. For example:

- ℃ (degree Celsius),
- ° (degree)
- ′ (minute)
- ″ (second)

template<typename Q1, typename U1, Unit U2>
consteval bool operator==(reference<Q1, U1>, U2 u2)
{
  return Q1{} == get_quantity_spec(u2) && U1{} == u2;
}
```

The second overload allows us to mix associated units and specializations of `reference` class template (both of them satisfy `Reference` concept). Thanks to this, we can check the following:

```cpp
static_assert(isq::time[second] != second);
static_assert(kind_of<isq::time>[second] == second);
```

Units may have many shades. This is why an equality check is not enough for them. In many cases, we don’t need to check against a concrete unit, but we want to ensure that the underlying numerical value will not change during a unit conversion. In such cases we check for equivalence. Watt (`W`) should be equivalent to `J/s` and `kg m²/s³`. Also, a litre (`l`) should be equivalent to a cubic decimetre (`dm³`).

To check for unit equivalence, currently we convert each unit to its canonical representation (scaled unit with magnitude expressed relative to some “blessed” implementation-specific reference unit) and then, we compare if the reference units and the magnitudes are the same:

```cpp
consteval bool equivalent(Unit auto lhs, Unit auto rhs)
{
  const auto lhs_canonical = get_canonical_unit(lhs);
  const auto rhs_canonical = get_canonical_unit(rhs);
  return lhs_canonical.mag == rhs_canonical.mag && lhs_canonical.reference_unit == rhs_canonical.reference_unit;
}
```

*Note: A `canonical_unit` is an implementation detail and is not exposed in public APIs for now.*

For example:

```cpp
static_assert(N != kg * m / s2);
static_assert(equivalent(N, kg * m / s2));
```

It is also worth noting that the above implementation makes the last line below pass, even though we can’t convert a quantity measured in `Hz` to the one in `Bq`:

```cpp
quantity q1 = (42 * Hz).in(one / s);
quantity q2 = (42 * Bq).in(one / s);
quantity q3 = (42 * one / s).in(Hz);
quantity q4 = (42 * one / s).in(Bq);
// quantity q5 = (42 * Hz).in(Bq);  // does not compile

quantity q6 = 1 * Hz + 1 * one / s;
quantity q7 = 1 * Bq + 1 * one / s;
// quantity q8 = 1 * Hz + 1 * Bq;   // does not compile

static_assert(Hz != Bq);
static_assert(Hz != one / s);
static_assert(Bq != one / s);
static_assert(equivalent(Hz, one / s));
static_assert(equivalent(Bq, one / s));
static_assert(equivalent(Hz, Bq));  // OK ???
```

Depending on the desired semanthics of `equivalent` function, we may want to make the last line to fail as well.

#### 20.6.2 Ordering

Ordering for dimensions and quantity types has no physical sense.

We could entertain adding ordering for units, but this would work only for quantities having the same reference unit, which would be inconsistent with how equality works.

Let’s see the following example:

```cpp
constexpr Unit auto my_unit = si::second;
if constexpr (my_unit == si::metre) {
 // ...
}
if constexpr (my_unit > si::metre) {
 // ...
}
if constexpr (my_unit > si::nano(si::second)) {
 // ...
}
```

In the above code, the first check could be useful for some use cases. However, the second one is impossible to implement and should not compile. The third one could be considered useful, but the current version of [[mp-units]](https://mpusz.github.io/mp-units) does not expose such an interface to limit potential confusion. Also, it is really hard to mathematically prove that the unit magnitude representation that we use in the library (based on primes factorization) is greater or smaller than the other one in some cases.

This is why we discourage providing ordering operations for any of those entities.

#### 20.6.3 Arithmetics

For consistency, we could also define arithmetic `operator+` and `operator-` for such entities to resemble the operations performed on quantities. For example:

```cpp
quantity q1 = isq::radius(1 * m) + isq::distance(1 * cm);
quantity q2 = isq::position_vector(1 * m) - isq::position_vector(1 * cm);
// quantity q3 = isq::position_vector(1 * m) + isq::position_vector(1 * cm);  // should not compile
```

returns:

- `quantity<isq::length[cm], int>` for `q1`,
- `quantity<isq::displacement[cm], int>` for `q2`.

Users may be interested to check what will be the result of performing such operations on ingredients of the quantity. As we say that “addition of a radius and a distance should yield a length” it would be good to model this arithmetics on our symbolic constants as well:

```cpp
static_assert(isq::radius + isq::distance == isq::length);
static_assert(isq::position_vector - isq::position_vector == isq::displacement);
// constexpr auto qs = isq::position_vector + isq::position_vector;  // should not compile
```

The operations that we expose must cover all of the operations we can do on quantities. This is why we not only have to overload operators but also expose other operations that can be performed on vector, tensor, and complex quantities:

```cpp
static_assert(implicitly_convertible(magnitude(isq::velocity), isq::speed));
static_assert(implicitly_convertible(scalar_product(isq::force, isq::displacement), isq::work));
static_assert(implicitly_convertible(vector_product(isq::position_vector, isq::force), isq::moment_of_force));
static_assert(implicitly_convertible(real(isq::complex_power), isq::active_power));
static_assert(implicitly_convertible(imag(isq::complex_power), isq::reactive_power));
static_assert(implicitly_convertible(modulus(isq::complex_power), isq::apparent_power));
```

Addition and subtractions on units is also possible, but it is more controverisal and less useful, so we do not propose them at this time:

```cpp
static_assert(m + cm == cm);
static_assert(km + mi == get_common_unit(km, mi));
```

### 20.7 Units

ISO specifies a measurement unit as a real scalar quantity, defined and adopted by convention, with which any other quantity of the same kind can be compared to express the ratio of the two quantities as a number.

In other words, a unit is a specific amount of a quantity. Such a definition is impractical from the programming language point of view. Let’s see the following hypothetical example (the below API is not a part of this proposal):

```cpp
namespace si {

constexpr auto metre = quantity<length>{1};
constexpr auto kilometre = 1000 * metre;

}

quantity<si::kilometre> distance = 42 * si::kilometre;
```

The above code would be consistent with the ISO definition however, it imposes several issues:

- creates a circular dependency for a `quantity` class,
- embeds a concrete representation type in the unit,
- loses all the benefits associated with our prime-factorized unit magnitudes (i.e., being able to express any ratio without the overflow of the underlying representation type),
- `quantity<length>{1}` may mean different things in namespaces of different systems which makes it much harder to provide interoperability between them,
- does not provide an opportunity to specify the unit symbol.

This is why decided to base unit definitions on tag types.

#### 20.7.1 `space_before_unit_symbol` alternatives

As described in the `space_before_unit_symbol` customization point chapter, some units should not be prepended with a space. We proposed the following customization point:

```cpp
template<Unit auto U>
constexpr bool space_before_unit_symbol = true;
```

It is important to note that the need for some customization is only for a small fraction of all units. It works but it has some disadvantages. First, it might be harder to reason about the units definitions because the spacialization of this variable template may be in a different location in the source code than the unit definition. Also, it breaks our assumption that we can define all the properties of the entity with a single line of a C++ code.

Maybe we should add an additional parameter (defaulted to `true`) to the `named_unit` class template to handle this?

#### 20.7.2 Prefixing units with prefixes

Initially [[mp-units]](https://mpusz.github.io/mp-units) library had one additional customization point for units:

```cpp
template<PrefixableUnit auto U>
constexpr bool unit_can_be_prefixed = true;
```

The above was used to disallow prefixes for some units, such as hours or degrees Celsius. However, after some time, we got [the issue on GitHub](https://github.com/mpusz/mp-units/issues/604) asking to allow prefixes for the latter.

It turns out that the certification organizations are not consistent here. ISO 80000-5 says:

> Prefixes are not allowed in combination with the unit °C.

However, [NIST states](https://www.nist.gov/pml/owm/writing-si-metric-system-units):

> Prefix symbols may be used with the unit symbol ºC, and prefix names may be used with the unit name “degree Celsius.” For example, 12 mºC (12 millidegrees Celsius) is acceptable. However, to avoid confusion, prefix symbols (and prefix names) are not used with the time-related unit symbols (names) min (minute), h (hour), d (day); nor with the angle-related symbols (names) º (degree), ’ (minute), and ” (second).

As a result of this issue and associated discussion, we decided to remove `unit_can_be_prefixed` support from the library, and we do not propose it here either.

### 20.8 Unit magnitudes

> [ *Note:* The word “magnitude” appears in this paper with three distinct meanings:
> 
> - **Quantity magnitude** (ISO 80000): the “magnitude of a quantity” is the quantity value itself — a number and a reference together expressing how large the quantity is.
> - **Vector magnitude**: the Euclidean norm of a vector, `|v|`, provided by the `norm()` CPO (also accessible as `magnitude(v)` for compatibility with physics terminology).
> - **Unit magnitude** (this section): a compile-time scaling factor relating a unit to other units of the same dimension.
> 
>  — *end note* ]

Each unit is associated with a magnitude representing its scaling factor relative to other units of the same dimension. However, absolute magnitude values have no physical meaning—only the *ratio* between magnitudes matters. For example, once we assign magnitude \(m_f\) to *foot*, we must assign \(3m_f\) to *yard* and \(m_f/12\) to *inch*.

We make magnitude interfaces mostly *implementation-defined*, exposing only minimal public APIs for interoperability while leaving freedom to implementers.

#### 20.8.1 Requirements beyond `std::ratio`

Magnitudes must support operations that units require: products and rational powers. Additionally, they must handle irrational ratios like \(\frac{\pi}{180}\) between degrees and radians.

`std::ratio` fails these requirements:

- Integral types too small for eight SI prefixes
- Not closed under rational powers (e.g., \(\sqrt{2}\))
- Cannot represent irrational factors like \(\pi\)
- Vulnerable to overflow when raised to powers

#### 20.8.2 Vector space representation with prime factorization

The solution uses prime factorization as a vector space basis. Each magnitude is a product of prime powers, with irrational constants (like \(\pi\)) added as additional basis elements when needed.

Examples using Astronomical Units (au), meters (m), degrees (deg), and radians (rad):

| Unit ratio | `std::ratio` | Vector space magnitude |
| --- | --- | --- |
| \(\left(\frac{\text{au}}{\text{m}}\right)\) | `std::ratio<149'597'870'700>` | `magnitude<power_v<2, 2>(), 3, power_v<5, 2>(), 73, 877, 7789>` |
| \(\left(\frac{\text{au}}{\text{m}}\right)^2\) | Overflow | `magnitude<power_v<2, 4>(), power_v<3, 2>(), power_v<5, 4>(), power_v<73, 2>(), power_v<877, 2>(), power_v<7789, 2>()>` |
| \(\sqrt{\frac{\text{au}}{\text{m}}}\) | Unrepresentable | `magnitude<2, power_v<3, 1, 2>(), 5, power_v<73, 1, 2>(), power_v<877, 1, 2>(), power_v<7789, 1, 2>()>` |
| \(\left(\frac{\text{rad}}{\text{deg}}\right)\) | Unrepresentable | `magnitude<power_v<2, 2>(), power_v<3, 2>(), power_v<pi_c{}, -1>(), 5>` |

Trade-offs: more verbose type names (mitigated by opaque types) and dependency on compile-time prime factorization.

#### 20.8.3 Compile-time factorization challenge

Users write `mag<149'597'870'700>`, which the library expands to its prime factorization. Large primes (e.g., 334,524,384,739 in the proton mass) cause compilers to assume infinite loops and terminate compilation when using trial division.

[[P3133R0]](https://wg21.link/p3133r0) explored `std::first_factor(uint64_t)` as a solution. Feedback showed a fast primality checker suffices for practical cases, though the function would still benefit the standard library and other domains.

#### 20.8.4 Common unit magnitude

Computing common magnitude: for each basis vector, take the minimum exponent across participating magnitudes (using implicit “0” for omitted vectors).

Example: \(\text{COM}[18, \frac{80}{3}] = \text{COM}[(2 \cdot 3^2), (2^4 \cdot 3^{-1} \cdot 5)] = 2^{\min[1,4]} \cdot 3^{\min[2,-1]} \cdot 5^{\min[0,1]} = \frac{2}{3}\)

### 20.9 Physical constants

#### 20.9.1 Constants as units

Physical constants are implemented as units rather than `constexpr` quantity values. Benefits:

- Constants in both numerator and denominator simplify at compile-time (like regular units)
- Expensive multiplication/division delayed until user selects output unit
- Enables simpler/faster representation types (e.g., integral instead of floating-point)

Example definitions:

```cpp
namespace si {

namespace si2019 {

inline constexpr struct speed_of_light_in_vacuum :
  named_constant<"c", mag<299'792'458> * metre / second> {} speed_of_light_in_vacuum;

}  // namespace si2019

inline constexpr struct magnetic_constant :
  named_constant<{u8"μ₀", "u_0"}, mag<4> * mag_power<10, -7> * π * henry / metre> {} magnetic_constant;

}  // namespace si
```

Usage example (vacuum permittivity):

```cpp
constexpr auto permeability_of_vacuum = 1. * si::magnetic_constant;
constexpr auto speed_of_light_in_vacuum = 1 * si::si2019::speed_of_light_in_vacuum;
QuantityOf<isq::permittivity_of_vacuum> auto q = 1 / (permeability_of_vacuum * pow<2>(speed_of_light_in_vacuum));
std::cout << q << " = " << q.in(F / m) << "\n";  // prints: 1  μ₀⁻¹ c⁻² = 8.85419e-12 F/m
```

#### 20.9.2 Negative constants

Named units may not be enough to model all of the constants out there. It turns out that there are many negative constants. Some of them can be found in [CODATA](https://physics.nist.gov/cuu/Constants). One such constant is [*helion g factor*](https://physics.nist.gov/cgi-bin/cuu/Value?ghn).

Trying to model this with `named_unit` fails to compile. The reason of the error is the fact that the conversion factors between units should be positive. This means that reusing `named_unit` to define constants may not be the best idea and we probably need to introduce a dedicated class.

This is why we need to introduce a new class template:

```cpp
inline constexpr struct helion_g_factor :
  named_constant<basic_symbol_text{"𝘨ₕ", "g_h"}, mag<-ratio{4'255'250'615, 1'000'000'000}> * one> {} helion_g_factor;
```

Additionally, such a solution does not allow the constant to be prefixed or associated with a `quantity_spec`.

### 20.10 Quantity specifications

Quantity specification provides all the data about the quantity type (i.e., kind, character, recipe, relation to other quantities in the hierarchy). It does not specify a unit, though.

#### 20.10.1 Bikeshedding `quantity_spec`

The “quantity specification” term is not provided in ISO or BIPM metrology dictonaries and was invented for the need of this library. This means that we should probably consider some other names for this abstraction:

- `quantity_specification`,
- `q_spec`,
- `q_specification`,
- `quantity_definition`,
- `quantity_def`,
- `quantity_data`,
- `q_data`.

### 20.11 Quantity references

*Note: We know that probably the term “reference” will not survive too long in the Committee, but we couldn’t find a better name for it in the [[mp-units]](https://mpusz.github.io/mp-units) library ([https://github.com/mpusz/mp-units/issues/486](https://github.com/mpusz/mp-units/issues/486)).*

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) says:

> **quantity** - property of a phenomenon, body, or substance, where the property has a magnitude that can be expressed as a number and a reference. … A reference can be a measurement unit, a measurement procedure, a reference material, or a combination of such.

In the library a quantity reference represents all the domain-specific meta-data about the quantity besides its representation type and its value. A `Reference` concept is satisfied by either of:

- an associated unit (e.g., `si::metre`),
- an instantiation of the `reference<QuantitySpec, Unit>` class template explicitly specifying the quantity type and its unit.

A reference type is implicitly created as a result of the following expression:

```cpp
constexpr Reference auto distance = isq::distance[m];
```

The above example defines a variable of type `reference<isq::distance, si::metre>`.

The `reference` class template also exposes an arithmetic interface similar to the one that we have already discussed in case of units and quantity types. It simply forwards the operation to its quantity type and unit members.

```cpp
constexpr ReferenceOf<isq::speed> auto speed = distance / si::second;
```

As a result we get a `reference<derived_quantity_spec<distance, per<time>>, derived_unit<metre, per<second>>>` type.

Similarly to the `Unit`, such a reference can be used to construct a quantity:

```cpp
QuantityOf<isq::speed> auto s = 60 * speed;
```

#### 20.11.1 Bikeshedding `reference`

The term `reference` is highly overloaded in the C++ domain. This is why we should probably rename the type that was successfully used in [[mp-units]](https://mpusz.github.io/mp-units). Here are a few proposals:

- `quantity_reference`
- `quantity_ref`
- `q_reference`
- `q_ref`

Please note that the longer the identifier we choose, the longer and harder it will be to grasp compiler error messages. A user never types this type identifier in the code (although a user might type an associated concept `Reference` or `ReferenceOf`).

### 20.12 Quantities

The `quantity` class template is a workhorse of the library. It can be considered a generalization of `std::chrono::duration`, but is not directly compatible with it.

Based on the ISO definition provided in the Quantity references chapter, the `quantity` class template has the following signature:

```cpp
template<Reference auto R, RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity;
```

It stores only one data member of `Rep` type. Unfortunately, this data member has to be publicly exposed to satisfy the C++ language requirements for [structural types](https://eel.is/c++draft/temp.param#def:type,structural). Hopefully, the language rules for structural types will improve with time before this library gets standardized.

#### 20.12.1 Multiply syntax commutativity

As of today, the multiply syntax that creates quantities is not commutative:

```cpp
quantity q1 = 1 * m;  // OK
quantity q2 = m * 1;  // Compile-time error
```

We decided to go this way to increase the readability of the code and limit possible confusion with this syntax. After a while, we extended it to support also the following:

```cpp
quantity q3 = 1 * m / s;    // OK
quantity q4 = 1 * m * m;    // OK
quantity q5 = 1 / s * m;    // OK
quantity q6 = s / 2;        // Compile-time error
quantity q7 = m * (1 / s);  // Compile-time error
quantity q8 = m * (1 * m);  // Compile-time error
```

However, [[mp-units]](https://mpusz.github.io/mp-units) users [requested the following use case](https://github.com/mpusz/mp-units/issues/621):

```cpp
if(num < Unit / 1'000'000'000'000) {
  quantity<si::femto<Unit>, double> n{num};
  out << n;
} else if(num < Unit / 1'000'000'000) {
  quantity<si::pico<Unit>, double> n{num};
  out << n;
} else // ...
```

Today, this does not compile. Should we extend the multiply syntax to support such use cases and with this have entire commutative property?

#### 20.12.2 Why don’t we use UDLs to create quantities?

Quantity construction chapter describes and explains why we introduced the multiply syntax as a construction helper for quantities. Many people ask why we chose this approach over battle-proven User Defined Literals (UDLs) that work well for the `std::chrono` library.

It turns out that many reasons make UDLs a poor choice for a physical units library:

1. UDLs work only with literals (compile-time known values). Our observation is that besides the unit tests, only a few compile-time known quantity values are used in the production code. Please note that for Physical constants, we recommend using units rather than compile-time constants.
2. Typical implementations of UDLs tend to always use the widest representation type available. In the case of `std::chrono::duration`, the following is true:

   ```cpp
   using namespace std::chrono_literals;
   auto d1 = 42s;
   auto d2 = 42.s;
   static_assert(std::is_same_v<decltype(d1)::rep, std::int64_t>);
   static_assert(std::is_same_v<decltype(d2)::rep, long double>);
   ```

   When such UDL is intermixed in arithmetics with any quantity type of a shorter representation type, it will always expand it to the longest one. In other words, such long type spreads until all types use it everywhere.
3. While increasing the coverage for the [[mp-units]](https://mpusz.github.io/mp-units) library, we learned that many unit symbols conflict with built-in types or numeric extensions. A few of those are: `F` (farad), `J` (joule), `W` (watt), `K` (kelvin), `d` (day), `l` or `L` (litre), `erg`, `ergps`. Using the `'_'` prefix would make it work for [[mp-units]](https://mpusz.github.io/mp-units), but if the library is standardized, those naming collisions would be a big issue. This is why we came up with the `_q_` prefix that would become `q_` after standardization (e.g., `42q_s`), which is not that nice anymore.
4. UDLs with the same identifiers defined in different namespace can’t be disambiguated in the C++ language. If both SI and CGS systems define `q_s` UDL for a second unit, then it would not be possible to specify which one to use in case both namespaces are “imported” with using directives.
5. Another bad property of UDLs is that they do not compose. A coherent unit of angular momentum would have a UDL specified as `q_kg_m2_per_s`. Now imagine that we want to make every possible user happy. How many variations of that unit would we predefine for differently scaled versions of all unit ingredients?
6. UDLs are also really expensive to define and specify. Typically, for each unit, we need two definitions. One for integral and another one for floating-point representation. In version 0.8.0 of the [[mp-units]](https://mpusz.github.io/mp-units) library, the coherent unit of angular momentum was defined as:

   ```cpp
   constexpr auto operator"" _q_kg_m2_per_s(unsigned long long l)
   {
     gsl_ExpectsAudit(std::in_range<std::int64_t>(l));
     return angular_momentum<kilogram_metre_sq_per_second, std::int64_t>(static_cast<std::int64_t>(l));
   }
   
   constexpr auto operator"" _q_kg_m2_per_s(long double l)
   {
     return angular_momentum<kilogram_metre_sq_per_second, long double>(l);
   }
   ```

The multiply syntax that we chose for this library does not have any of those issues.

#### 20.12.3 Special values of a quantity

`quantity` class template, similarly to `std::chrono::duration`, exposes some special values as `static` member functions:

- `min()`,
- `max()`,
- `zero()`.

Also, similarly to `std::chrono::duration` those functions are implemented in terms of a type trait:

```cpp
template<typename Rep>
struct representation_values : std::chrono::duration_values<Rep> {
  static constexpr Rep one() noexcept
    requires std::constructible_from<Rep, int>
 {
    return Rep(1);
 }
};
```

An additional the `one()` function in `representation_values` is provided for use with the multiply syntax when constructing quantities. Users can create a quantity with numerical value of one using: `representation_values<double>::one() * si::metre`. This function is not exposed as a static member of `quantity` because `one()` is not a true multiplicative identity for dimensional quantities—for example, `pow<2>(quantity<si::metre>::one())` would change the dimension from *length* to *area*.

Please also note that in C++26, `std::chrono::duration_values` is not a part of the freestanding library.

#### 20.12.4 Quantity arithmetics

##### 20.12.4.1 `quantity` is a numeric wrapper

If we think about it, the `quantity` class template is just a “smart” numeric wrapper. It exposes properly constrained set of arithmetic operations on one or two operands.

Every single arithmetic operator is exposed by the `quantity` class template only if the underlying representation type provides it as well and its implementation has proper semantics (e.g., returns a reasonable type).

For example, in the following code, `-a` will compile only if `MyInt` exposes such an operation as well:

```cpp
quantity a = MyInt{42} * m;
quantity b = -a;
```

Assuming that:

- `q` is our quantity,
- `qq` is a quantity implicitly convertible to `q`,
- `q2` is any other quantity,
- `kind` is a quantity of the same kind as `q`,
- `one` is a quantity of `dimension_one` with the unit `one`,
- `number` is a value of a type “compatible” with `q`’s representation type,

here is the list of all the supported operators:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Unary</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Compound assignment</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Binary</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;">Ordering &amp; comparison</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp"><span class="op">+</span>q</code><br/><code class="sourceCode cpp"><span class="op">-</span>q</code><br/><code class="sourceCode cpp"><span class="op">++</span>q</code><br/><code class="sourceCode cpp">q<span class="op">++</span></code><br/><code class="sourceCode cpp"><span class="op">--</span>q</code><br/><code class="sourceCode cpp">q<span class="op">--</span></code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">+=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">-=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">%=</span> qq</code><br/><code class="sourceCode cpp">q <span class="op">*=</span> number</code><br/><code class="sourceCode cpp">q <span class="op">*=</span> one</code><br/><code class="sourceCode cpp">q <span class="op">/=</span> number</code><br/><code class="sourceCode cpp">q <span class="op">/=</span> one</code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">+</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">-</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">%</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">*</span> q2</code><br/><code class="sourceCode cpp">q <span class="op">*</span> number</code><br/><code class="sourceCode cpp">number <span class="op">*</span> q</code><br/><code class="sourceCode cpp">q <span class="op">/</span> q2</code><br/><code class="sourceCode cpp">q <span class="op">/</span> number</code><br/><code class="sourceCode cpp">number <span class="op">/</span> q</code></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 25%;"><code class="sourceCode cpp">q <span class="op">==</span> kind</code><br/><code class="sourceCode cpp">q <span class="op">&lt;=&gt;</span> kind</code></td>
</tr>
</table>

As we can see, there are plenty of operations one can do on a value of a `quantity` type. As most of them are obvious, in the following chapters, we will discuss only the most important or non-trivial aspects of quantity arithmetics.

##### 20.12.4.2 Addition and subtraction

Quantities can easily be added or subtracted from each other:

```cpp
static_assert(1 * m + 1 * m == 2 * m);
static_assert(2 * m - 1 * m == 1 * m);
static_assert(isq::height(1 * m) + isq::height(1 * m) == isq::height(2 * m));
static_assert(isq::height(2 * m) - isq::height(1 * m) == isq::height(1 * m));
```

The above uses the same types for LHS, RHS, and the result, but in general, we can add, subtract, or compare the values of any quantity type as long as both quantities are of the same kind. The result of addition and subtraction will be the common type of the arguments:

```cpp
static_assert(1 * km + 1.5 * m == 1001.5 * m);
static_assert(isq::height(1 * m) + isq::width(1 * m) == isq::length(2 * m));
static_assert(isq::height(2 * m) - isq::distance(0.5 * m) == 1.5 * m);
static_assert(isq::radius(1 * m) - 0.5 * m == isq::radius(0.5 * m));
```

Please note that for the compound assignment operators, we always need to end up with the left-hand-side argument type:

```cpp
static_assert((1 * m += 1 * km) == 1001 * m);
static_assert((isq::length(1 * m) += isq::height(1 * m)) == isq::length(1 * m));
static_assert((isq::height(1.5 * m) -= 1 * m) == isq::height(0.5 * m));
```

If we break those rules, the code will not compile:

```cpp
quantity q1 = 1 * m -= 0.5 * m;                         // Compile-time error (1)
quantity q2 = 1 * km += 1 * m;                          // Compile-time error (2)
quantity q3 = isq::height(1 * m) += isq::length(1 * m); // Compile-time error (3)
```

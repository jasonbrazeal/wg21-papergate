`(1)` Convertions of the floating-point to integral representation type is considered narrowing.

`(2)` Conversion of quantity with integral representation type from a unit of a higher resolution to the one with a lower resolution is considered narrowing.

`(3)` Conversion from a more generic quantity type to a more specific one is considered unsafe.

Please note that all the above operations either preserved the input representation types or returned a common type if those were different for both arguments. This is not the case for irrational conversion factors. In such cases, the library will force the user to use at least one floating-point representation type to prevent truncation:

```cpp
template<typename... Ts>
consteval bool invalid_arithmetic(Ts... ts)
{
  return !requires { (... + ts); } && !requires { (... - ts); };
}

static_assert(invalid_arithmetic(1 * rad, 1 * deg));
static_assert(is_of_type<1. * rad + 1 * deg, quantity<deg, double>>);
static_assert(is_of_type<1 * rad + 1. * deg, quantity<deg, double>>);
static_assert(is_of_type<1. * rad + 1. * deg, quantity<deg, double>>);
```

##### 20.12.4.3 Multiplication and division

Multiplying or dividing a quantity by a number does not change its quantity type or unit. However, its representation type may change. For example:

```cpp
static_assert(isq::height(3 * m) * 0.5 == isq::height(1.5 * m));
```

Unless we use a compound assignment operator, in which case we always have to result with the type of the left-hand-side argument. This, together with the fact that this library tries to prevent truncation of a quantity value means, that the following does not compile:

```cpp
quantity q = isq::height(3 * m) *= 0.5; // Compile-time error
```

However, suppose we multiply or divide quantities of the same or different types, or we divide a raw number by a quantity. In that case, we most probably will end up in a quantity of yet another type:

```cpp
static_assert(120 * km / (2 * h) == 60 * km / h);
static_assert(isq::width(2 * m) * isq::length(2 * m) == isq::area(4 * m2));
static_assert(50 / isq::time(1 * s) == isq::frequency(50 * Hz));
```

An exception from the above rule happens when one of the arguments is a dimensionless quantity. If we multiply or divide by such a quantity, the quantity type will not change. If such a quantity has a unit `one`, also the unit of a quantity will not change:

```cpp
static_assert(120 * m / (2 * one) == 60 * m);
```

An interesting special case happens when we divide the same quantity kinds or multiply a quantity by its inverted type. In such a case, we end up with a dimensionless quantity.

```cpp
static_assert(isq::height(4 * m) / isq::width(2 * m) == 2 * one); // (1)
static_assert(5 * h / (120 * min) == 0 * one);                    // (2)
static_assert(5. * h / (120 * min) == 2.5 * one);
```

`(1)` The resulting quantity type of the LHS is `isq::height / isq::width`, which is a quantity of the dimensionless kind.

`(2)` The resulting quantity of the LHS is `0 * dimensionless[h / min]`. To be consistent with the division of different quantity types, we do not convert quantity values to a common unit before the division.

###### 20.12.4.3.1 Beware of integral division

The physical units library can’t do any runtime branching logic for the division operator. All logic has to be done at compile-time when the actual values are not known, and the quantity types can’t change at runtime.

If we expect `120 * km / (2 * h)` to return `60 km/h`, we have to agree with the fact that `5 * km / (24 * h)` returns `0 km/h`. We can’t do a range check at runtime to dynamically adjust scales and types based on the values of provided function arguments.

This is why we often prefer floating-point representation types when dealing with units. Some popular physical units libraries even [forbid integer division at all](https://aurora-opensource.github.io/au/main/troubleshooting/#integer-division-forbidden).

##### 20.12.4.4 Modulo

Now that we know how addition, subtraction, multiplication, and division work, it is time to talk about modulo. What would we expect to be returned from the following quantity equation?

```cpp
auto q = 5 * h % (120 * min);
```

Most of us would probably expect to see `1 h` or `60 min` as a result. And this is where the problems start.

The C++ language defines its `/` and `%` operators with the [quotient-remainder theorem](https://eel.is/c++draft/expr.mul#4):

```
q = a / b;
r = a % b;
q * b + r == a;
```

The important property of the modulo operator is that it only works for integral representation types (it is undefined what modulo for floating-point types means). However, as we saw in the previous chapter, integral types are tricky because they often truncate the value.

From the quotient-remainder theorem, the result of modulo operation is `r = a - q * b`. Let’s see what we get from such a quantity equation on integral representation types:

```cpp
quantity a = 5 * h;
quantity b = 120 * min;
quantity q = a / b;
quantity r = a - q * b;

std::cout << "reminder: " << r << "\n";
```

The above code outputs:

```
reminder: 5 h
```

And now, a tough question needs an answer. Do we really want modulo operator on physical units to be consistent with the quotient-remainder theorem and return `5 h` for `5 * h % (120 * min)`?

This is exactly why we decided not to follow this hugely surprising path in this library. The selected approach was also consistent with the feedback from C++ experts. For example, this is what Richard Smith said about this issue:

> I think the quotient-remainder property is a less important motivation here than other factors – the constraints on `%` and `/` are quite different, so they lack the inherent connection they have for integers. In particular, I would expect that `A / B` works for all quantities `A` and `B`, whereas `A % B` is only meaningful when `A` and `B` have the same dimension. It seems like a nice-to-have for the property to apply in the case where both `/` and `%` are defined, but internal consistency of `/` across all cases seems much more important to me.
> 
> I would expect `61 min % 1 h` to be `1 min`, and `1 h % 59 min` to also be `1 min`, so my intuition tells me that the result type of `A % B`, where `A` and `B` have the same dimension, should have the smaller unit of `A` and `B` (and if the smaller one doesn’t divide the larger one, we should either use the `gcd / std::common_type` of the units of `A` and `B` or perhaps just produce an error). I think any other behavior for `%` is hard to defend.
> 
> On the other hand, for division it seems to me that the choice of unit should probably not affect the result, and so if we want that `5 mm / 120 min = 0 mm/min`, then `5 h / 120 min == 0 hc` (where `hc` is a dimensionless “hexaconta”, or `60x`, unit). I don’t like the idea of taking SI base units into account; that seems arbitrary and like it would do the wrong thing as often as it does the right thing, especially when the units have a multiplier that is very large or small. We could special-case the situation of a dimensionless quantity, but that could lead to problematic overflow pretty easily: a calculation such as `10 s * 5 GHz * 2 uW` would overflow an `int` if it produces a dimensionless quantity for `10 s * 5 GHz`, but it could equally produce `50 G * 2 uW = 100 kW` without any overflow, and presumably would if the terms were merely reordered.
> 
> If people want to use integer-valued quantities, I think it’s fundamental that you need to know what the units of the result of an operation will be, and take that into account in how you express computations; the simplest rule for heterogeneous operators like `*` or `/` seems to be that the units of the result are determined by applying the operator to the units of the operands – and for homogeneous operators like `+` or `%`, it seems like the only reasonable option is that you get the `std::common_type` of the units of the operands.

To summarize, the modulo operator on physical units has more in common with addition and division operators than with the quotient-remainder theorem. To avoid surprising results, the operation uses a common unit to do the calculation and provide its result:

```cpp
static_assert(5 * h / (120 * min) == 0 * one);
static_assert(5 * h % (120 * min) == 60 * min);
static_assert(61 * min % (1 * h) == 1 * min);
static_assert(1 * h % (59 * min) == 1 * min);
```

##### 20.12.4.5 Comparison against zero

Zero is special. It is the only number that unambiguously defines the value of any kind of quantity, regardless of its units: zero inches and zero meters and zero miles are all identical. For this reason, it’s very common to compare the value of a quantity against zero. For example, when checking the sign of a quantity, or when making sure that it’s nonzero.

We could implement such checks in the following way:

```cpp
if(q1 / q2 != 0 * m / s)
  // ...
```

The above would work (assuming we are dealing with the quantity of *speed*), but it’s not ideal. If the result of `q1 / q2` is not expressed in `m / s`, we’ll incur an extra unit conversion. Even if it is in `m / s`, it’s cumbersome to repeat the unit in a context where it makes no difference.

We could avoid repeating the unit, and guarantee there won’t be an extra conversion, by writing:

```cpp
if(auto q = q1 / q2; q != q.zero())
  // ...
```

But that is a bit inconvenient, and inexperienced users could be unaware of this technique and its rationale.

For the above reasons, the library provides special support for comparisons against the literal `0`. Only this one value has elevated privileges and does not have to state the unit — the numerical value zero is common to all scaled units of any kind.

Thanks to that, to save typing and not pay for unneeded conversions, our check could be implemented as follows:

```cpp
if (q1 / q2 != 0)
  // ...
```

All six comparison operators support comparison against zero without specifying a unit. This works with any representation type `rep` for which `representation_values<rep>::zero()` is provided.

Only a compile-time zero is accepted: an integer or floating-point literal that is zero (e.g., `0`, `0.`, `0.f`, `0LL`). Passing another literal or a runtime variable — even one whose value happens to be zero — is rejected at compile time.

##### 20.12.4.6 Other maths

This chapter scoped only on the `quantity` type’s operators. However, there are many named math functions provided in the [[mp-units]](https://mpusz.github.io/mp-units) library. Among others, we can find there the following:

- `pow()`, `sqrt()`, `cbrt()`,
- `exp()`,
- `abs()`,
- `epsilon()`,
- `fma()`, `fmod()`, `remainder()`,
- `isfinite()`, `isinf()`, `isnan()`,
- `floor()`, `ceil()`, `round()`,
- `inverse()`,
- `hypot()`,
- `sin()`, `cos()`, `tan()`,
- `asin()`, `acos()`, `atan()`, `atan2()`.

In the library, we can also find the `<mp-units/random.h>` header file with all the pseudo-random number generators.

We plan to provide a separate paper on those in the future.

#### 20.12.5 Dimensionless quantities

The quantities we discussed so far always had some specific type and physical dimension. However, this is not always the case. While performing various computations, we sometimes end up with so-called “dimensionless” quantities, which [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) correctly defines as quantities of dimension one:

> - Quantity for which all the exponents of the factors corresponding to the base quantities in its quantity dimension are zero.
> - The measurement units and values of quantities of dimension one are numbers, but such quantities convey more information than a number.
> - Some quantities of dimension one are defined as the ratios of two quantities of the same kind.
> - Numbers of entities are quantities of dimension one.

##### 20.12.5.1 Dividing two quantities of the same kind

Dividing two quantities of the same kind always results in a quantity of dimension one. However, depending on what type of quantities we divide or what their units are, we may end up with slightly different types.

Dividing two quantities of the same dimension always results in a quantity with the dimension being `dimension_one`. This is often different for other physical units libraries, which may return a raw representation type for such cases. A raw value is also always returned from the division of two `std::chrono::duration` values.

In the initial design of the [[mp-units]](https://mpusz.github.io/mp-units) library, the resulting type of division of two quantities was their common representation type (just like `std::chrono::duration`):

```cpp
static_assert(std::is_same_v<decltype(10 * km / (5 * km)), int>);
```

The reasoning behind it was not providing a false impression of a strong `quantity` type for something that looks and feels like a regular number. Also, all of the mathematic and trigonometric functions were working fine out of the box with such representation types, so we did not have to rewrite `sin()`, `cos()`, `exp()`, and others.

However, the feedback we got from the production usage was that such an approach is really bad for generic programming. It is hard to handle the result of the two quantities’ division (or multiplication) as it might be either a quantity or a fundamental type. If we want to raise such a result to some power, we must use `units::pow` or `std::pow` depending on the resulting type (`units::pow` takes the power as template arguments). Those are only a few issues related to such an approach.

Moreover, suppose we divide quantities of the same dimension, but with units of significantly different magnitudes. In such case, we may end up with a really small or a huge floating-point value, which may result in losing lots of precision. Returning a dimensionless quantity from such cases allows us to benefit from all the properties of scaled units and is consistent with the rest of the library.

###### 20.12.5.1.1 Dividing quantities of the same type

First, let’s analyze what happens if we divide two quantities of the same type:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::height(200 * m) / isq::height(50 * m);
```

In such a case, we end up with a dimensionless quantity that has the following properties:

```cpp
static_assert(q.quantity_spec == dimensionless);
static_assert(q.dimension == dimension_one);
static_assert(q.unit == one);
```

In case we would like to print its value, we would see a raw value of `4` in the output with no unit being printed.

###### 20.12.5.1.2 Dividing quantities of different types

We can divide quantities of the same dimension and unit but of different quantity types:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::work(200 * J) / isq::heat(50 * J);
```

Again we end up with `dimension_one` and `one`, but this time:

```cpp
static_assert(q.quantity_spec == isq::work / isq::heat);
```

As shown above, the result is not of a `dimensionless` type anymore. Instead, we get a quantity type derived from the performed quantity equation. According to the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html), *work* divided by *heat* is the recipe for the *thermodynamic efficiency* quantity, thus:

```cpp
static_assert(implicitly_convertible(q.quantity_spec, isq::efficiency_thermodynamics));
```

Please note that the quantity of `isq::efficiency_thermodynamics` is of a kind `dimensionless`, so it is implicitly convertible to `dimensionless` and satisfies the `QuantityOf<dimensionless>` concept.

###### 20.12.5.1.3 Dividing quantities of different units

Now, let’s see what happens when we divide two quantities of the same type but different units:

```cpp
constexpr QuantityOf<dimensionless> auto q = isq::height(4 * km) / isq::height(2 * m);
```

This time we get a quantity of `dimensionless` type with a `dimension_one` as its dimension. However, the resulting unit is not `one` anymore:

```cpp
static_assert(q.unit == mag_power<10, 3> * one);
```

In case we would print the text output of this quantity, we would not see a raw value of `2000`, but `2 km/m`.

First, it may look surprising, but this is actually consistent with the division of quantities of different dimensions. For example, if we divide `4 * km / (2 * s)`, we do not expect `km` to be “expanded” to `m` before the division, right? We would expect the result of `2 * (km / s)`, which is exactly what we get when we divide quantities of the same kind.

This is a compelling feature that allows us to express huge or tiny ratios without the need for big and expensive representation types. With this, we can easily define things like a [Hubble’s constant](https://en.wikipedia.org/wiki/Hubble%27s_law#Dimensionless_Hubble_constant) that uses a unit that is proportional to the ratio of kilometers per megaparsecs, which are both units of length:

```cpp
inline constexpr struct hubble_constant :
    named_constant<{u8"H₀", "H_0"}, mag_ratio<701, 10> * si::kilo<si::metre> / si::second / si::mega<parsec>> {
} hubble_constant;
```

##### 20.12.5.2 Counts of things

Another important use case for dimensionless quantities is to provide strong types for counts of things. For example:

- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 3) provides a *rotation* quantity defined as the number of revolutions,
- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 6) provides a *number of turns in a winding* quantity,
- [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) provides a *Hamming distance* quantity defined as the number of digit positions in which the corresponding digits of two words of the same length are different.

Thanks to assigning strong names to such quantities, they can be used in the quantity equation of other quantities. For example, *rotational frequency* is defined by `rotation / duration`.

##### 20.12.5.3 Predefined units of the dimensionless quantity

As we observed above, the most common unit for dimensionless quantities is `one`. It has the ratio of `1` and does not output any textual symbol.

A unit `one` is special in the entire type system of units as it is considered to be an identity operand in the unit symbolic expressions. This means that, for example:

```cpp
static_assert(one * one == one);
static_assert(one * si::metre == si::metre);
static_assert(si::metre / si::metre == one);
```

The same is also true for `dimension_one` and `dimensionless` in the domains of dimensions and quantity specifications, respectively.

Besides the unit `one`, there are a few other scaled units predefined in the library for usage with dimensionless quantities:

```cpp
inline constexpr struct percent : named_unit<"%", mag_ratio<1, 100> * one> {} percent;
inline constexpr struct per_mille : named_unit<{u8"‰", "%o"}, mag_ratio<1, 1000> * one> {} per_mille;
inline constexpr struct parts_per_million : named_unit<"ppm", mag_ratio<1, 1'000'000> * one> {} parts_per_million;
inline constexpr auto ppm = parts_per_million;

inline constexpr struct pi : named_constant<symbol_text{u8"π" /* U+03C0 GREEK SMALL LETTER PI */, "pi"}, mag<pi_c> * one> {} pi;
inline constexpr auto π /* U+03C0 GREEK SMALL LETTER PI */ = pi;
```

###### 20.12.5.3.1 Superpowers of the unit `one`

Quantities implicitly convertible to `dimensionless` with the unit equivalent to `one` are the only ones that are:

- implicitly constructible from the raw value,
- explicitly convertible to a raw value,
- comparable to a raw value.

```cpp
quantity<one> inc(quantity<one> q) { return q + 1; }
void legacy(double) { /* ... */ }

if (auto q = inc(42); q != 0)
  legacy(static_cast<int>(q));
```

This property also expands to usual arithmetic operators.

Please note that those rules do not apply to all the dimensionless quantities. It would be unsafe and misleading to allow such operations on units with a magnitude different than `1` (e.g., `percent`) or for quantities that are not implicitly convertible to `dimensionless` (e.g., `angular_measure`).

##### 20.12.5.4 Angular quantities

Special, often controversial, examples of dimensionless quantities are the *angular measure* and *solid angular measure* quantities that are defined in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 3) to be the result of a division of `arc_length / radius` and `area / pow<2>(radius)` respectively. Moreover, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) also explicitly states that both can be expressed in the unit `one`. This means that both `isq::angular_measure` and `isq::solid_angular_measure` should be of a kind of `dimensionless`.

On the other hand, [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) also specifies that the unit `radian` can be used for *angular measure*, and the unit `steradian` can be used for *solid angular measure*. Those should not be mixed or used to express other types of dimensionless quantities. We should not be able to measure:

- basic dimensionless quantity in radians or steradians,
- *angular measure* in steradians,
- *solid angular measure* in radians.

This means that both `isq::angular_measure` and `isq::solid_angular_measure` should also be quantity kinds by themselves.

*Note: Many people claim that angle being a dimensionless quantity is a bad idea. There are proposals submitted to make an angle a base quantity and `rad` to become a base unit in both [[SI]](https://www.bipm.org/en/publications/si-brochure) and [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html).*

###### 20.12.5.4.1 Radians and degrees support

Thanks to the usage of magnitudes the library provides efficient strong types for all angular types. This means that with the built-in support for magnitudes of \(\pi\) we can provide accurate conversions between radians and degrees. The library also provides common trigonometric functions for angular quantities:

```cpp
quantity speed = 110 * km / h;
quantity rate_of_climb = -0.63657 * m / s;
quantity glide_ratio = speed / -rate_of_climb;
quantity glide_angle = angular::asin(1 / glide_ratio);

std::println("Glide ratio: {::N[.1f]}", glide_ratio.in(one));
std::println("Glide angle:");
std::println(" - {::N[.4f]}", glide_angle);
std::println(" - {::N[.2f]}", glide_angle.in(angular::degree));
std::println(" - {::N[.2f]}", glide_angle.in(angular::gradian));
```

The above program prints:

```
Glide ratio: 48.0
Glide angle:
 - 0.0208 rad
 - 1.19°
 - 1.33ᵍ
```

##### 20.12.5.5 Nested quantity kinds

Angular quantities are not the only ones with such a “strange” behavior. A similar case is the *storage capacity* quantity specified in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (part 13) that again allows expressing it in both `one` and `bit` units.

Those cases make dimensionless quantities an exceptional tree in the library. This quantity hierarchy contains more than one quantity kind and more than one unit in its tree:

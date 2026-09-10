
*Dotted lines denote `is_kind` relationships, where a child quantity forms a distinct kind incompatible with quantities of the same parent.*

To provide such support in the library, we provided an `is_kind` specifier that can be appended to the quantity specification:

```cpp
inline constexpr struct angular_measure : quantity_spec<dimensionless, arc_length / radius, is_kind> {} angular_measure;
inline constexpr struct solid_angular_measure : quantity_spec<dimensionless, area / pow<2>(radius), is_kind> {} solid_angular_measure;
inline constexpr struct storage_capacity : quantity_spec<dimensionless, is_kind> {} storage_capacity;
```

With the above, we can constrain `radian`, `steradian`, and `bit` to be allowed for usage with specific quantity kinds only:

```cpp
inline constexpr struct radian : named_unit<"rad", metre / metre, kind_of<isq::angular_measure>> {} radian;
inline constexpr struct steradian : named_unit<"sr", square(metre) / square(metre), kind_of<isq::solid_angular_measure>> {} steradian;
inline constexpr struct bit : named_unit<"bit", one, kind_of<storage_capacity>> {} bit;
```

This still allows the usage of `one` (possibly scaled) for such quantities which is exactly what we wanted to achieve.

It is worth mentioning here that converting up the hierarchy beyond a subkind requires an explicit conversion. For example:

```cpp
static_assert(implicitly_convertible(isq::rotation, dimensionless));
static_assert(!implicitly_convertible(isq::angular_measure, dimensionless));
static_assert(explicitly_convertible(isq::angular_measure, dimensionless));
```

This increases type safety and prevents accidental quantities with invalid units. For example, a result of a conversion from `isq::angular_measure[rad]` to `dimensionless` would be a reference of `dimensionless[rad]`, which contains an incorrect unit for a `dimensionless` quantity. Such a conversion must be explicit and be preceded by an explicit unit conversion:

```cpp
quantity q1 = isq::angular_measure(42. * rad);
quantity<dimensionless[one]> q2 = dimensionless(q1.in(one));
```

#### 20.12.6 Value conversions

Truncation prevention and Unit safety chapters describe the motivation, usage, and safety benefits of the `value_cast`, `in`, and `force_in` value conversion functions.

##### 20.12.6.1 `template` disambiguation concerns

Initially **mp-units** library allowed changing of the `quantity` representation type only via the `value_cast` non-member function. Introducing such a functionality to `in` and `force_in` member functions would mandate the usage of the `template` disambiguator in generic contexts that we encorage with Generic interfaces.

After bringing those concerns to LEWGI in St. Louis, the room agreed that we should provide this functionality for member functions as well. It is really useful and user-friendly in non-generic contexts and for the cases where we deal with a dependent name, we should leave `value_cast` even if it is an always conversion-forcing operation.

##### 20.12.6.2 Value conversions summary

The table below provides all the value conversions functions that may be run on `x` being the instance of either `quantity` or `quantity_point`:

| Forcing | Representation | Unit | Member function | Non-member function |
| --- | --- | --- | --- | --- |
| No | Same | `u` | `x.in(u)` |  |
| No | `T` | Same | `x.in<T>()` |  |
| No | `T` | `u` | `x.in<T>(u)` |  |
| Yes | Same | `u` | `x.force_in(u)` | `value_cast<u>(x)` |
| Yes | `T` | Same | `x.force_in<T>()` | `value_cast<T>(x)` |
| Yes | `T` | `u` | `x.force_in<T>(u)` | `value_cast<u, T>(x)` or `value_cast<T, u>(x)` |

##### 20.12.6.3 Bikeshedding `force_in(U)`

`force_in` is a bit ambiguous name for the conversion function in a quantities and units library. Writing `x.force_in(s)` may be misleading for a quantity of *time* rather than *force*. However, we do not have good alternatives here.

Before we provide some alternatives it is good to mention that we also heve a `x.force_numerical_value_in(u)` to force a truncation while obtaining a numerical value of the quantity.

[[Au]](https://aurora-opensource.github.io/au) library uses `x.coerce_in(u)` for this operation. We could also consider different names. Here are a few possbile alternatives:

- `x.force_in(u)`, `x.force_numerical_value_in(u)`,
- `x.forced_into(u)`, `x.forced_numerical_value_into(u)`,
- `x.unsafe_in(u)`, `x.unsafe_numerical_value_in(u)`,
- `x.lossy_in(u)`, `x.lossy_numerical_value_in(u)`,
- `x.unchecked_in(u)`, `x.unchecked_numerical_value_in(u)`,
- `x.coerce_in(u)`, `x.coerce_numerical_value_in(u)`,
- `x.cast_in(u)`, `x.cast_numerical_value_in(u)`,
- `x.cast_to(u)`, `x.cast_numerical_value_to(u)`.

In case we select `x.cast_to(u)` we probably should also rename `q.in(u)` to `q.to(u)`.

##### 20.12.6.4 Bikeshedding `quantity::rep`

[[mp-units]](https://mpusz.github.io/mp-units) initially tried to be compatible with `std::chrono::duration`. This is why we chose `rep` as the name for a public member type exposed from `quantity` to denote its representation type. This is consistent but may not be the best name.

First, we use `q.numerical_value_in()` to get the underlying value which is already inconsistent with `std::chrono::duration::count()`. Also, as we mentioned already, `quantity` is a numeric wrapper. To provide compatibility between different numeric types maybe we should set a policy that those should expose `value_type` or `element_type`? Both seem to be valid choices here as well.

#### 20.12.7 Binary operators

Binary operators for quantities (and quantity points) should take both arguments as template parameters. Implementing them in terms of implicit convertibility leads to invalid resulting types. Let’s see the following example:

```cpp
static_assert(std::convertible_to<quantity<isq::speed[m/s], int>,
                                  quantity<(isq::length / isq::time)[m/s], double>>);
static_assert(!std::convertible_to<quantity<(isq::length / isq::time)[m/s], double>,
                                   quantity<isq::speed[m/s], int>>);
```

As we see above, `quantity<isq::speed[m/s], int>` converts to `quantity<(isq::length / isq::time)[m/s], double>`, but this is not the case in the other direction. This is caused by the fact that conversion from `double` to `int` is considered truncating. If we would implement the operators in terms of the implicit conversion then we would end up with the quantity of `isq::length / isq::time` as a result, which is suboptimal. We prefer `isq::speed` in this case:

```cpp
quantity q1 = isq::speed(1 * m/s);
quantity q2 = isq::length(1. * m) / isq::time(1. * s);
static_assert(is_of_type<q1 + q2, quantity<isq::speed[m/s], double>>);
```

In the following example, we consistently use floating-point representation types and both quantities are interconvertible:

```cpp
static_assert(std::convertible_to<quantity<(isq::mass * pow<2>(isq::length / isq::time))[J], double>,
                                  quantity<isq::energy[kg*m2/s2], double>>);
static_assert(std::convertible_to<quantity<isq::energy[kg*m2/s2], double>,
                                  quantity<(isq::mass * pow<2>(isq::length / isq::time))[J], double>>);
```

We could think that the problem is gone, and we can use implicit conversions. However, depending on how we implement it, this might lead to an ambiguous overload resolution or lack of substitutability of addition. Even if we somehow solve those issues, none of the types would be perfect as a return type. While forming a resulting type `isq::energy` should have a priority over `isq::mass * pow<2>(isq::length / isq::time)` and `J` should have a priority over `kg*m2/s2`:

```cpp
quantity q1 = (isq::mass(1 * kg) * pow<2>(isq::length(1 * m) / isq::time(1 * s))).in(J);
quantity q2 = isq::energy(1 * kg*m2/s2);
static_assert(is_of_type<q1 + q2, quantity<isq::energy[J], int>>);
```

It is also worth noting that this approach is compatible with [binary operators for `std::chrono::duration`](https://eel.is/c++draft/time.duration.nonmember). As we can read in the Interoperability with the `std::chrono` abstractions chapter, `std::chrono::duration` is interconvertible with the quantity. Nevertheless, with the above, we always need to explicitly convert the argument to a proper entity before doing any arithmetic:

```cpp
static_assert(1 * s + 1s == 2 * s); // does not compile
static_assert(1 * s + quantity{1s} == 2 * s); // OK
```

This prevents ambiguity with `std::chrono::duration` operators and works the same for any user-defined `QuantityLike` type or any other type that is convertible to a `quantity`.

### 20.13 Quantity Points

#### 20.13.1 `delta` and `point` creation helpers

The features described in this chapter directly solve an issue raised on [std-proposals reflector](https://lists.isocpp.org/std-proposals/2024/06/10118.php). As it was reported, the code below may look correct, but it provides an invalid result:

```cpp
quantity Volume = 1.0 * m3;
quantity Temperature = 28.0 * deg_C;
quantity n_ = 0.04401 * kg / mol;
quantity R_boltzman = 8.314 * N * m / (K * mol);
quantity mass = 40.0 * kg;
quantity Pressure = R_boltzman * Temperature.in(K) * mass / n_ / Volume;
std::cout << Pressure << "\n";
```

The problem is related to the accidental usage of a `quantity` rather than `quantity_point` for `Temperature`. This means that after conversion to kelvins, we will get `28 K` instead of the expected `301.15 K`, corrupting all further calculations.

A correct code should use a `quantity_point`:

```cpp
quantity_point Temperature(28.0 * deg_C);
```

This might be an obvious thing for domain experts, but new users of the library may not be aware of the affine space abstractions and how they influence temperature handling.

After a lengthy discussion on handling such scenarios, we decided to:

- make the above code ill-formed,
- provide an alternative way to create `quantity` and `quantity_point` with the `delta` and `point` construction helpers respectively.

Here are the main points of this new design:

1. All references/units that specify point origin in their definition (i.e., `si::kelvin`, `si::degree_Celsius`, and `usc::degree_Fahrenheit`) are excluded from the multiply syntax.
2. A new `delta` quantity construction helper is introduced:
   - `delta<m>(42)` results with a `quantity<si::metre, int>`,
   - `delta<deg_C>(5)` results with a `quantity<si::deg_C, int>`.
3. A new `point` quantity point construction helper is introduced:
   - `point<m>(42)` results with a `quantity_point<si::metre, zeroth_point_origin<kind_of<isq::length>>{}, int>`,
   - `point<deg_C>(5)` results with a `quantity<si::metre, si::ice_point, int>`.

Please note that `si::kelvin` is also excluded from the multiply syntax to prevent the following surprising issues:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Before</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Now</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity q(300 * K);
quantity_point qp(300 * K);
static_assert(q.in(deg_C) != qp.in(deg_C).quantity_from_zero());</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity q = delta&lt;K&gt;(300);
quantity_point qp = point&lt;K&gt;(300);
static_assert(q.in(deg_C) != qp.in(deg_C).quantity_from_zero());</code></pre></td>
</tr>
</table>

We believe that the code enforced with new utilities makes it much easier to understand what happens here.

With such changes to the interface design, the offending code will not compile as initially written. Users will be forced to think more about what they write. To enable the compilation, the users have to create explicitly:

- a `quantity_point` (the intended abstraction in this example) with any of the below syntaxes:

  ```cpp
  quantity_point Temperature = point<deg_C>(28.0);
  auto Temperature = point<deg_C>(28.0);
  quantity_point Temperature(delta<deg_C>(28.0));
  ```
- a `quantity` (an incorrect abstraction in this example) with:

  ```cpp
  quantity Temperature = delta<deg_C>(28.0);
  auto Temperature = delta<deg_C>(28.0);
  ```

Thanks to the new design, we can immediately see what happens here and why the result might be incorrect in the second case.

#### 20.13.2 `default_point_origin<Reference>`, `quantity_from_zero()`, and `natural_point_origin<QuantitySpec>`

`default_point_origin<Reference>`, `quantity_from_zero()`, and `natural_point_origin<QuantitySpec>` are introduced to simplify the usage of:

- temperature (and quantities with similar units) points where each unit has its own origin,
- quantity points for domains with one unquestionable “zero” origin and for which we do not have other predefined origins known at compile time.

In theory, those abstractions are not needed, and in this chapter, we will describe how the API and use cases would look like without it.

Let’s try to reimplement parts of our room AC temperature controller from the Temperature support chapter:

```cpp
constexpr struct room_reference_temp : relative_point_origin<si::zeroth_degree_Celsius + delta<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

room_temp room_ref{};

std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             room_ref.in(deg_C).quantity_from(si::zeroth_degree_Celsius),
             room_ref.in(deg_F).quantity_from(usc::zeroth_degree_Fahrenheit),
             room_ref.in(K).quantity_from(si::zeroth_kelvin));
```

Now let’s compare it to the implementation using the currently proposed design:

```cpp
constexpr struct room_reference_temp : relative_point_origin<point<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

room_temp room_ref{};

std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             room_ref.in(deg_C).quantity_from(default_point_origin(deg_C)),
             room_ref.in(deg_F).quantity_from(default_point_origin(deg_F)),
             room_ref.in(K).quantity_from(default_point_origin(K)));
```

First, removing those features also renders `point<deg_C>(21)` impossible to implement. Second, `default_point_origin(unit)` always gives the correct standard origin for the current unit, so conversions remain unit-agnostic: if someone changes the unit, no origin name needs updating.

For `quantity_point` objects already at their unit’s default origin (the common case for directly constructed temperature points), text output works directly and `quantity_from_zero()` returns the stored displacement:

```cpp
quantity_point temp = point<deg_C>(21.);  // PO = default_point_origin(deg_C) = ice_point

std::println("{} ({}) ({::N[.2f]})", temp, temp.in(deg_F), temp.in(K));
// prints: 21 ℃ (70.8 ℉) (294.15 K)

auto delta_C = temp.quantity_from_zero();        // 21 ℃ — from ice_point
auto delta_K = temp.in(K).quantity_from_zero();  // 294.15 K — from absolute_zero
```

`.quantity_from_zero()` is constrained to `PO == default_point_origin(R)`, matching `zero()`. For points at custom origins (such as `room_ref` above), use `quantity_from(default_point_origin(unit))` to obtain the displacement from the standard origin.

### 20.14 Interoperability with other libraries

It is easy to cooperate with similar entities of other libraries. No matter if we want to provide interoperability with a simple home-grown strongly typed wrapper type (e.g., `Meter`, `Timestamp`, …) or with a feature-rich quantities and units library, we have to provide specializations of:

- a `quantity_like_traits` for external `quantity`-like type,
- a `quantity_point_like_traits` for external `quantity_point`-like type.

#### 20.14.1 Specifying a conversion kind

Before we delve into the template specialization details, let’s first decide if we want the conversions to happen implicitly or if explicit ones would be a better choice. Or maybe the conversion should be implicit in one direction only (e.g., into abstractions in this library) while the explicit conversions in the other direction should be preferred?

There is no one unified answer to the above questions. Everything depends on the use case.

Typically, in the C++ language, the implicit conversions are allowed in cases where:

- both abstractions mean exactly the same, and interchanging them in the code should not change its logic,
- there is no significant runtime overhead introduced by such a conversion (e.g., no need for dynamic allocation or copying of huge internal buffers),
- the target type of the conversion provides the same or better safety to the users,
- we prefer the simplicity of implicit conversions over safety during the (hopefully short) transition period of refactoring our code base from the usage of one library to the other.

In all other scenarios, we should probably enforce explicit conversions.

The kinds of inter-library conversions can be easily configured in specializations of conversion traits in the **mp-units** library. Conversion traits should provide a static data member convertible to `bool`. If the value is `true`, then the conversion is `explicit`. Otherwise, if the value is `false`, implicit conversions will be allowed. The names of the flags are as follows:

- `explicit_import` to describe conversion from the external entity to the one in this library (import case),
- `explicit_export` to describe conversion from the entity in this library to the external one (export case).

#### 20.14.2 Quantities conversions

For example, let’s assume that some company has its own `Meter` strong-type wrapper:

```cpp
struct Meter {
  int value;
};
```

As every usage of `Meter` is at least as good and safe as the usage of `quantity<si::metre, int>`, and as there is no significant runtime performance penalty, we would like to allow the conversion to `std::quantity` to happen implicitly.

On the other hand, the `quantity` type is much safer than the `Meter`, and that is why we would prefer to see the opposite conversions stated explicitly in our code.

To enable such interoperability, we must define a specialization of the `quantity_like_traits<T>` type trait. Such specialization should provide:

- `reference` static data member that provides the quantity reference (e.g., unit),
- `rep` type that specifies the underlying storage type,
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a quantity’s raw value of `rep` type,
- `from_numerical_value(rep)` static member function returning `T`.

For example, for our `Meter` type, we could provide the following:

```cpp
template<>
struct std::quantity_like_traits<Meter> {
  static constexpr auto reference = si::metre;
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = decltype(Meter::value);
  static constexpr rep to_numerical_value(Meter m) { return m.value; }
  static constexpr Meter from_numerical_value(rep v) { return Meter{v}; }
};
```

After that, we can check that the `QuantityLike` concept is satisfied:

```cpp
static_assert(QuantityLike<Meter>);
```

and we can write the following:

```cpp
void print(Meter m) { std::cout << m.value << " m\n"; }

int main()
{
  using namespace std::si::unit_symbols;

  Meter height{42};

  // implicit conversions
  std::quantity h1 = height;
  std::quantity<isq::height[m], int> h2 = height;

  std::cout << h1 << "\n";
  std::cout << h2 << "\n";

  // explicit conversions
  print(Meter(h1));
  print(Meter(h2));
}
```

No matter if we decide to use implicit or explicit conversions, the library’s framework will not allow unsafe operations to happen.

If we extend the above example with unsafe conversions, the code will not compile, and we will have to fix the issues first before the conversion may be performed:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Unsafe</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Fixed</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity&lt;isq::height[m]&gt; h3 = height;
quantity&lt;isq::height[mm], int&gt; h4 = height;
quantity&lt;isq::height[km], int&gt; h5 = height;  // Error (1)
&#10;
std::cout &lt;&lt; h3 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h4 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h5 &lt;&lt; &quot;\n&quot;;
&#10;
print(Meter(h3));                            // Error (2)
print(Meter(h4));                            // Error (3)
print(Meter(h5));</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>quantity&lt;isq::height[m]&gt; h3 = height;
quantity&lt;isq::height[mm], int&gt; h4 = height;
quantity&lt;isq::height[km], int&gt; h5 = quantity{height}.force_in(km);
&#10;
std::cout &lt;&lt; h3 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h4 &lt;&lt; &quot;\n&quot;;
std::cout &lt;&lt; h5 &lt;&lt; &quot;\n&quot;;
&#10;
print(Meter(value_cast&lt;int&gt;(h3)));
print(Meter(h4.force_in(m)));
print(Meter(h5));</code></pre></td>
</tr>
</table>

`(1)` Truncation of value while converting from meters to kilometers.

`(2)` Conversion of `double` to `int` is not value-preserving.

`(3)` Truncation of value while converting from millimeters to meters.

#### 20.14.3 Quantity points conversions

To play with quantity point conversions, let’s assume that we have a `Timestamp` strong type in our codebase, and we would like to start using this library to work with this abstraction.

```cpp
struct Timestamp {
  int seconds;
};
```

As we described in The Affine Space chapter, timestamps should be modeled as quantity points rather than regular quantities.

To allow the conversion between our custom `Timestamp` type and the `quantity_point` class template we need to provide the following in the specialization of the `quantity_point_like_traits<T>` type trait:

- `reference` static data member that provides the quantity point reference (e.g., unit),
- `point_origin` static data member that specifies the absolute point, which is the beginning of our measurement scale for our points,
- `rep` type that specifies the underlying storage type,
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the `quantity` being the offset of the point from the origin,
- `from_numerical_value(rep)` static member function returning `T`.

For example, for our `Timestamp` type, we could provide the following:

```cpp
template<>
struct std::quantity_point_like_traits<Timestamp> {
  static constexpr auto reference = si::second;
  static constexpr auto point_origin = default_point_origin(reference);
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = decltype(Timestamp::seconds);
  static constexpr rep to_numerical_value(Timestamp ts) { return ts.seconds; }
  static constexpr Timestamp from_numerical_value(rep v) { return Timestamp(v); }
};
```

After that, we can check that the `QuantityPointLike` concept is satisfied:

```cpp
static_assert(std::QuantityPointLike<Timestamp>);
```

and we can write the following:

```cpp
void print(Timestamp ts) { std::cout << ts.seconds << " s\n"; }

int main()
{
  Timestamp ts{42};

  // implicit conversion
  std::quantity_point qp = ts;

  std::cout << qp << "\n";

  // explicit conversion
  print(Timestamp(qp));
}
```

#### 20.14.4 Interoperability with the `std::chrono` abstractions

In the C++ standard library, we have two types that handle quantities and model the affine space. Those are:

- [`std::chrono::duration`](https://en.cppreference.com/w/cpp/chrono/duration) - specifies quantities of time,
- [`std::chrono::time_point`](https://en.cppreference.com/w/cpp/chrono/time_point) - specifies quantity points of time.

This library comes with built-in interoperability with those types thanks to:

- specializations of `quantity_like_traits` and `quantity_point_like_traits` that provide support for implicit conversions between types in both directions,
- `chrono_point_origin<Clock>` point origin for `std` clocks,
- `to_chrono_duration` and `to_chrono_time_point` dedicated conversion functions that result in types exactly representing this library’s abstractions.

It is important to note here that only a `quantity_point` that uses `chrono_point_origin<Clock>` as its origin can be converted to the `std::chrono` abstractions:

```cpp
inline constexpr struct ts_origin : relative_point_origin<chrono_point_origin<system_clock> + 1 * h> {} ts_origin;
inline constexpr struct my_origin : absolute_point_origin<isq::time> {} my_origin;

quantity_point qp1 = sys_seconds{1s};
auto tp1 = to_chrono_time_point(qp1);  // OK

quantity_point qp2 = chrono_point_origin<system_clock> + 1 * s;
auto tp2 = to_chrono_time_point(qp2);  // OK

quantity_point qp3 = ts_origin + 1 * s;
auto tp3 = to_chrono_time_point(qp3);  // OK

quantity_point qp4 = my_origin + 1 * s;
auto tp4 = to_chrono_time_point(qp4);  // Compile-time Error (1)

quantity_point qp5{1 * s};
auto tp5 = to_chrono_time_point(qp5);  // Compile-time Error (2)
```

`(1)` `my_origin` is not defined in terms of `chrono_point_origin<Clock>`.

`(2)` `natural_point_origin` is not defined in terms of `chrono_point_origin<Clock>`.

Here is an example of how interoperability described in this chapter can be used in practice:

```cpp
using namespace std::chrono;

sys_seconds ts_now = floor<seconds>(system_clock::now());

quantity_point start_time = ts_now;
quantity speed = 925. * km / h;
quantity distance = 8111. * km;
quantity flight_time = distance / speed;
quantity_point exp_end_time = start_time + flight_time;

sys_seconds ts_end = value_cast<int>(exp_end_time.in(s));

auto curr_time = zoned_time(current_zone(), ts_now);
auto mst_time = zoned_time("America/Denver", ts_end);

std::cout << "Takeoff: " << curr_time << "\n";
std::cout << "Landing: " << mst_time << "\n";
```

The above may print the following output:

```cpp
Takeoff: 2023-11-18 13:20:54 UTC
Landing: 2023-11-18 15:07:01 MST
```

As mentioned above, conversions between entities in this and `std::chrono` libraries are implicit in both directions. This simplifies many scenarios. However, with such rules, `common_type_t<chrono::seconds, quantity<si::second, int>>;` and the ternary operator on such arguments will not work. If this concerns LEWG, we may consider implicit conversion in only one direction. However, it is not easy to decide which one to choose.

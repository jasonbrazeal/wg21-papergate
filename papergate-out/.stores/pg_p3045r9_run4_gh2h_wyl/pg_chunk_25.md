`per<U>` (reciprocal unit), `delta<U>()` and `point<U>()` (affine space constructors) are intentionally terse to keep quantity equations and construction syntax readable. Their brevity could be problematic in the flat `std::` namespace. However, unlike the units and quantity specs above, these are helpers that form part of the core API and are arguably framework entities in the same sense as `quantity` itself.

##### 20.3.3.5 Summary

The placement of all of the above is an **open question for LEWG**. The three or four categories above may warrant different namespaces, or a single shared subnamespace (e.g., `std::units::` or `std::qty::`). The tradeoff is consistent with the broader framework discussion: a subnamespace reduces name-conflict risk but requires `using namespace` to keep equations readable.

### 20.4 Concepts

This chapter enumerates all the user-facing concepts in the library.

*Note: Initially, C++20 was meant to use `CamelCase` for all the concept identifiers. Frustratingly, `CamelCase` concepts got dropped from the C++ standard at the last moment before releasing C++20. Now, we are facing the predictable consequences of running out of names. As long as some concepts in the library could be easily named with a `standard_case` there are some that are hard to distinguish from the corresponding type names, such as `Quantity` or `QuantitySpec`. This is why we decided to use `CamelCase` consistently for all the concept identifiers to make it clear when we are talking about a type or concept identifier. However, we are aware that this might be a temporary solution. In case the library gets standardized, we can expect the LEWG to bikeshed/rename all of the concept identifiers to a `standard_case`, even if it will result in a harder to understand code. We propose some suggestions at the end of the chapter.*

#### 20.4.1 `Dimension<T> concept`

`Dimension` concept matches a dimension of either a base or derived quantity:

- Base dimensions are explicitly defined by the user by inheriting from the instantiation of a `base_dimension` class template. It should be instantiated with a unique symbol identifier describing this dimension in a specific system of quantities.
- Derived dimensions are implicitly created by the library’s framework based on the quantity equation provided in the quantity specification.

##### 20.4.1.1 `DimensionOf<T, V>` concept

`DimensionOf` concept is satisfied when both arguments satisfy a `Dimension` concept and when they compare equal.

#### 20.4.2 `QuantitySpec<T> concept`

`QuantitySpec` concept matches all the quantity specifications including:

- Base quantities defined by a user by inheriting from the `quantity_spec` class template instantiated with a base dimension argument.
- Derived named quantities defined by a user by inheriting from the `quantity_spec` class template instantiated with a result of a quantity equation passed as an argument.
- Other named quantities forming a hierarchy of quantities of the same kind defined by a user by inheriting from the `quantity_spec` class template instantiated with another “parent” quantity specification passed as an argument.
- Quantity kinds describing a family of mutually comparable quantities.
- Intermediate derived quantity specifications being a result of a quantity equations on other specifications.

##### 20.4.2.1 `QuantitySpecOf<T, V>` concept

`QuantitySpecOf` concept is satisfied when both arguments satisfy a `QuantitySpec` concept and when `T` is implicitly convertible to `V`.

#### 20.4.3 `UnitMagnitude<T>`

`UnitMagnitude` concept is satisfied by all types defining a unit magnitude.

*Note:* Unit magnitude implementation is a private implementation detail of the library.

#### 20.4.4 `Unit<T>` concept

`Unit` concept matches all the units in the library including:

- Base units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier describing this unit in a specific system of units.
- Named scaled units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier and a product of multiplying another unit with some magnitude.
- Prefixed units defined by a user by inheriting from the `prefixed_unit` class template instantiated with a prefix symbol, a magnitude, and a unit to be prefixed.
- Derived named units defined by a user by inheriting from the `named_unit` class template instantiated with a unique symbol identifier and a result of unit equation passed as an argument.
- Derived unnamed units being a result of a unit equations on other units.
- Physical constants defined by a user by inheriting from the `named_constant` class template instantiated with a unique symbol identifier and a product of multiplying another unit with some magnitude.

##### 20.4.4.1 `PrefixableUnit<T>`

`PrefixableUnit` concept is satisfied by all units derived from a `named_unit` class template. Such units can be passed as an argument to a `prefixed_unit` class template.

##### 20.4.4.2 `UnitOf<T, V>` concept

`UnitOf` concept is satisfied for all units `T` for which an associated quantity spec is implicitly convertible to the provided `QuantitySpec` value..

#### 20.4.5 `Reference<T>` concept

`Reference` concept is satisfied by all quantity reference types. Such types provide all the meta-information required to create a `Quantity`.

A `Reference` can either be:

- A `Unit`.
- The instantiation of a `reference` class template with a `QuantitySpec` passed as the first template argument and a `Unit` passed as the second one.

##### 20.4.5.1 `ReferenceOf<T, V>` concept

`ReferenceOf` concept is satisfied by references `T` which have a quantity specification that satisfies `QuantitySpecOf<V>` concept.

#### 20.4.6 `RepresentationOf<T, V>`

`RepresentationOf` concept constrains a type `T` of a number that stores the numerical value of a quantity.

Every representation type must satisfy a common baseline:

- **Weakly regular**: copyable and equality comparable (default-constructibility is not required).
- **`MagnitudeScalable`**: the library must be able to apply a unit magnitude ratio to it internally. Most standard types satisfy this automatically; see Representation Types for details.
- **Character-specific operations**: additional arithmetic operations required by the quantity character (e.g. total ordering for real scalars, `real()`/`imag()`/`modulus()` CPOs for complex scalars, `norm()`/`magnitude()` CPO for vectors).

The second template argument `V` further constrains which characters are accepted:

- if the type of `V` satisfies `QuantitySpec`:
  - by all representation types when `V` describes a quantity kind,
  - otherwise, by representation types that are of a quantity character associated with a provided quantity specification `V`.
- if `V` is of `quantity_character` type:
  - by representation types that are of a provided quantity character.

#### 20.4.7 `Quantity<T>` concept

`Quantity` concept matches every quantity in the library and is satisfied by all types being or deriving from an instantiation of a `quantity` class template.

##### 20.4.7.1 `QuantityOf<T, V>` concept

`QuantityOf` concept is satisfied by all the quantities for which a `ReferenceOf<V>` is `true`.

##### 20.4.7.2 `QuantityLike<T>` concept

`QuantityLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_like_traits` type trait yields a valid type that provides:

- `reference` static data member that matches the `Reference` concept,
- `rep` type that matches `RepresentationOf` concept with the character provided in `reference`.
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the quantity,
- `from_numerical_value(rep)` static member function returning `T`.

For example, this is how support for `std::chrono::seconds` can be provided:

```cpp
template<>
struct quantity_like_traits<std::chrono::seconds> {
  static constexpr auto reference = detail::time_unit_from_chrono_period<Period>();
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = Rep;
  using T = std::chrono::duration<Rep, Period>;

  [[nodiscard]] static constexpr rep to_numerical_value(const T& q) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return q.count();
  }

  [[nodiscard]] static constexpr T from_numerical_value(const rep& v) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return T(v);
  }
};

quantity q = 42s;
std::chrono::seconds dur = 42 * s;
```

#### 20.4.8 `PointOrigin<T>` concept

`PointOrigin` concept matches all quantity point origins in the library. It is satisfied by either:

- All types derived from an `absolute_point_origin` class template.
- All types derived from a `relative_point_origin` class template.

##### 20.4.8.1 `PointOriginFor<T, V>` concept

`PointOriginFor` concept is satisfied by all `PointOrigin` types that have quantity type implicitly convertible from quantity specification `V`, which means that `V` must satisfy `QuantitySpecOf<T::quantity_spec>`.

For example, `si::ice_point` can serve as a point origin for *points* of `isq::Celsius_temperature` because this quantity type implicitly converts to `isq::thermodynamic_temperature`.

However, if we define `mean_sea_level` in the following way:

```cpp
inline constexpr struct mean_sea_level : absolute_point_origin<isq::altitude> {} mean_sea_level;
```

then it can’t be used as a point origin for *points* of `isq::length` or `isq::width` as none of them is implicitly convertible to `isq::altitude`:

- not every *length* is an *altitude*,
- *width* is not compatible with *altitude*.

#### 20.4.9 `QuantityPoint<T>` concept

`QuantityPoint` concept is satisfied by all types being either a specialization or derived from `quantity_point` class template.

##### 20.4.9.1 `QuantityPointOf<T, V>` concept

`QuantityPointOf` concept is satisfied by all the quantity points `T` that match the following value `V`:

| `V` | Condition |
| --- | --- |
| `QuantitySpec` | The quantity point quantity specification satisfies `ReferenceOf<V>` concept. |
| `PointOrigin` | The *point* and `V` have the same absolute point origin. |

##### 20.4.9.2 `QuantityPointLike<T>` concept

`QuantityPointLike` concept provides interoperability with other libraries and is satisfied by a type `T` for which an instantiation of `quantity_point_like_traits` type trait yields a valid type that provides:

- `reference` static data member that matches the `Reference` concept.
- `point_origin` static data member that matches the `PointOrigin` concept.
- `rep` type that matches `RepresentationOf` concept with the character provided in `reference`.
- `explicit_import` static data member convertible to `bool` that specifies that the conversion from `T` to a `quantity_point` type should happen explicitly (if `true`),
- `explicit_export` static data member convertible to `bool` that specifies that the conversion from a `quantity_point` type to `T` should happen explicitly (if `true`),
- `to_numerical_value(T)` static member function returning a raw value of the quantity being the offset of the point from the origin,
- `from_numerical_value(rep)` static member function returning `T`.

For example, this is how support for a `std::chrono::time_point` of `std::chrono::seconds` can be provided:

```cpp
template<typename C>
struct quantity_point_like_traits<std::chrono::time_point<C, std::chrono::seconds>> {
  static constexpr auto reference = detail::time_unit_from_chrono_period<Period>();
  static constexpr auto point_origin = chrono_point_origin<C>;
  static constexpr bool explicit_import = false;
  static constexpr bool explicit_export = false;
  using rep = Rep;
  using T = std::chrono::time_point<C, std::chrono::duration<Rep, Period>>;

  [[nodiscard]] static constexpr rep to_numerical_value(const T& tp) noexcept(std::is_nothrow_copy_constructible_v<rep>)
  {
    return tp.time_since_epoch().count();
  }

  [[nodiscard]] static constexpr T from_numerical_value(const rep& v) noexcept(
    std::is_nothrow_copy_constructible_v<rep>)
  {
    return T(std::chrono::duration<Rep, Period>(v));
  }
};

quantity_point qp = time_point_cast<std::chrono::seconds>(std::chrono::system_clock::now());
std::chrono::sys_seconds q = qp + 42 * s;
```

#### 20.4.10 Bikeshedding concepts

This chapter provides some alternative names in `standard_case` for concepts.

| Before | After | Alternative | Comments |
| --- | --- | --- | --- |
| `Dimension` | `dimension` | `some_dimension` |  |
| `DimensionOf` | `dimension_of` |  | This concept is never used in the framework but might be useful to users. |
| `QuantitySpec` | `quantity_spec` | `some_quantity_spec` | “After” requires renaming `quantity_spec` to `named_quantity_spec` for a class template. |
| `QuantitySpecOf` | `quantity_spec_of` |  |  |
| `UnitMagnitude` | `unit_magnitude` | `some_unit_magnitude` |  |
| `Unit` | `unit` | `some_unit` | “Alternative” allows renaming named_unit class template to unit |
| `PrefixableUnit` | `prefixable_unit` |  |  |
| `UnitOf` | `unit_of` |  |  |
| `Reference` | `reference` | `some_reference` | Collides with `reference` class template, but we have some ideas how to remove the class template. |
| `ReferenceOf` | `reference_of` |  |  |
| `RepresentationOf` | `representation_of` |  |  |
| `Quantity` | `delta_quantity` | `some_quantity` | Collides with `quantity` class template. |
| `QuantityOf` | `delta_quantity_of` | `quantity_of` |  |
| `QuantityLike` | `delta_quantity_like` | `quantity_like` |  |
| `PointOrigin` | `point_origin` | `some_point_origin` |  |
| `PointOriginFor` | `point_origin_for` |  |  |
| `QuantityPoint` | `point_quantity` | `some_quantity_point` | Collides with `quantity_point` class template. |
| `QuantityPointOf` | `point_quantity_of` | `quantity_point_of` |  |
| `QuantityPointLike` | `point_quantity_like` | `quantity_point_like` |  |

How do we like `some_XXX` practice? It is already being used in some open source projects. It also reads nicely against `XXX_of`, which provides more restrictive constraints. If we are OK with it, should we apply it only in the conflicting cases or apply everywhere for consistency?

If we go for `some_XXX` then we can leave `quantity_spec` as the class template, and also we could rename `named_unit` class template to `unit` so the user can type less while defining their own system entities.

Here is a comparison of quantity specification and units definitions in both alternatives:

Today (inconsistent?):

```cpp
inline constexpr struct length : quantity_spec<dim_length> {} length;
inline constexpr struct time   : quantity_spec<dim_time> {} time;
inline constexpr struct speed  : quantity_spec<length / time> {} speed;

inline constexpr struct metre  : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
```

Option 1:

```cpp
inline constexpr struct length : named_quantity_spec<dim_length> {} length;
inline constexpr struct time   : named_quantity_spec<dim_time> {} time;
inline constexpr struct speed  : named_quantity_spec<length / time> {} speed;

inline constexpr struct metre  : named_unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
```

Option 2:

```cpp
inline constexpr struct length : quantity_spec<dim_length> {} length;
inline constexpr struct time   : quantity_spec<dim_time> {} time;
inline constexpr struct speed  : quantity_spec<length / time> {} speed;

inline constexpr struct metre  : unit<"m", kind_of<isq::length>> {} metre;
inline constexpr struct second : unit<"s", kind_of<isq::time>> {} second;
```

Please also note, that we’ve added `point_quantityXXX` alternatives as we consider replacing `quantity_point<..., Rep>` with `quantity<point<...>, Rep>`. In such a case, we could still need `some_quantity = delta_quantity || point_quantity`.

### 20.5 Symbolic expressions

Modern C++ physical quantities and units libraries use opaque types to improve the user experience while analyzing compile-time errors or inspecting types in a debugger. This is a huge usability improvement over the older libraries that use aliases to refer to long instantiations of class templates.

#### 20.5.1 Derived entities

Having such strong types for entities is not enough. While doing arithmetics on them, we get derived entities, and they also should be easy to understand and correlate with the code written by the user. This is where symbolic expressions come into play.

The library should use the same unified approach to represent the results of arithmetics on all kinds of entities. It is worth mentioning that a generic purpose symbolic expressions library is not a good solution for a physical quantities and units library.

Let’s assume that we want to represent the results of the following two unit equations:

- `metre / second * second`
- `metre * metre / metre`

Both of them should result in a type equivalent to `metre`. A general-purpose library will probably result with the types similar to the below:

- `mul<div<metre, second>, second>`
- `div<mul<metre, metre>, metre>`

Comparing such types for equivalence would not only be very expensive at compile-time but would also be really confusing to the users observing them in the compilation logs. This is why we need a dedicated solution here.

In a physical quantities and units library, we need symbolic expressions to express the results of

- dimension equations,
- quantity type equations,
- unit equations, and
- unit magnitude equations.

If the above equation results in a derived entity, we must create a type that clearly describes what we are dealing with. We need to pack a simplified expression template into some container for that. There are various possibilities here. The table below presents the types generated from unit expressions by two leading products on the market in this subject:

| Unit | [[mp-units]](https://mpusz.github.io/mp-units) | [[Au]](https://aurora-opensource.github.io/au) |
| --- | --- | --- |
| `N⋅m` | `derived_unit<metre, newton>` | `UnitProduct<Meters, Newtons>` |
| `1/s` | `derived_unit<one, per<second>>` | `Pow<Seconds, -1>` |
| `km/h` | `derived_unit<kilo_<metre>, per<hour>>` | `UnitProduct<Kilo<Meters>, Pow<Hours, -1>>` |
| `kg⋅m²/(s³⋅K)` | `derived_unit<kilogram, pow<metre, 2>, per<kelvin, power<second, 3>>>` | `UnitProduct<Pow<Meters, 2>, Kilo<Grams>, Pow<Seconds, -3>, Pow<Kelvins, -1>>` |
| `m²/m` | `metre` | `Meters` |
| `km/m` | `derived_unit<kilo_<metre>, per<metre>>` | `UnitProduct<Pow<Meters, -1>, Kilo<Meters>>` |
| `m/m` | `one` | `UnitProduct<>` |

It is a matter of taste which solution is better. While discussing the pros and cons here, we should remember that our users often do not have a scientific background. This is why we recommend to use syntax that is as similar to the correct English language as possible. It consistently uses the `derived_` prefix for types representing derived units, dimensions, and quantity specifications. Those are instantiated first with the contents of the numerator followed by the entities of the denominator (if present) enclosed in the `per<...>` symbolic expression.

#### 20.5.2 Identities

The arithmetics on units, dimensions, and quantity types require a special identity value. Such value can be returned as a result of the division of the same entities, or using it should not modify the symbolic expression on multiplication.

We chose the following names here:

- `one` in the domain of units,
- `dimension_one` in the domain of dimensions,
- `dimensionless` in the domain of quantity types.

The above names were selected based on the following quote from [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html):

> A quantity whose dimensional exponents are all equal to zero has the dimensional product denoted A<sup>0</sup>B<sup>0</sup>C<sup>0</sup>… = 1, where the symbol 1 denotes the corresponding dimension. There is no agreement on how to refer to such quantities. They have been called **dimensionless** quantities (although this term should now be avoided), quantities with **dimension one**, quantities with dimension number, or quantities with the **unit one**. Such quantities are dimensionally simply numbers. To avoid confusion, it is helpful to use explicit units with these quantities where possible, e.g., m/m, nmol/mol, rad, as specified in the SI Brochure.

#### 20.5.3 Supported operations and their results

The table below presents all the operations that can be done on units, dimensions, and quantity types in a quantities and units library. The right column presents corresponding expression templates being their results:

| Operation | Resulting template expression arguments |
| --- | --- |
| `A * B` | `A, B` |
| `B * A` | `A, B` |
| `A * A` | `power<A, 2>` |
| `{identity} * A` | `A` |
| `A * {identity}` | `A` |
| `A / B` | `A, per<B>` |
| `A / A` | `{identity}` |
| `A / {identity}` | `A` |
| `{identity} / A` | `{identity}, per<A>` |
| `pow<2>(A)` | `power<A, 2>` |
| `pow<2>({identity})` | `{identity}` |
| `sqrt(A)` or `pow<1, 2>(A)` | `power<A, 1, 2>` |
| `sqrt({identity})` or `pow<1, 2>({identity})` | `{identity}` |

#### 20.5.4 Simplifying the resulting symbolic expressions

To limit the length and improve the readability of generated types, there are many rules to simplify the resulting symbolic expression.

1. **Ordering**

   The resulting comma-separated arguments of multiplication are always sorted according to a specific predicate. This is why:

   ```cpp
   static_assert(A * B == B * A);
   static_assert(std::is_same_v<decltype(A * B), decltype(B * A)>);
   ```

   This is probably the most important of all the steps, as it allows comparing types and enables the rest of the simplification rules.

   User-provided symbols (when available) are not guaranteed to be unique in the project. For example, someone may use `"s"` as a symbol for a count of samples, which, when used in a unit expression with seconds, would cause fatal consequences (e.g., `sample * second` would yield `s²`, or `sample / second` would result in `one`).

   This is why the library chose to use type name identifiers in such cases. As of today, it could be implementation-defined of how a specific implementation orders the identifiers on a type list. If [[P2830R10]](https://wg21.link/p2830r10) gets standardized, then it will be possible for every implementation to guarantee the same ordering of types.
2. **Aggregation**

   In case two of the same type identifiers are found next to each other on the argument list, they will be aggregated in one entry:

   | Before | After |
   | --- | --- |
   | `A, A` | `power<A, 2>` |
   | `A, power<A, 2>` | `power<A, 3>` |
   | `power<A, 1, 2>, power<A, 2>` | `power<A, 5, 2>` |
   | `power<A, 1, 2>, power<A, 1, 2>` | `A` |
3. **Simplification**

   In case two of the same type identifiers are found in the numerator and denominator argument lists, they are being simplified into one entry:

   | Before | After |
   | --- | --- |
   | `A, per<A>` | `{identity}` |
   | `power<A, 2>, per<A>` | `A` |
   | `power<A, 3>, per<A>` | `power<A, 2>` |
   | `A, per<power<A, 2>>` | `{identity}, per<A>` |

   It is important to notice here that only the elements with exactly the same type are being simplified. This means that, for example, `m/m` results in `one`, but `km/m` will not be simplified. The resulting derived unit will preserve both symbols and their relative magnitude. This allows us to properly print symbols of some units or constants that require such behavior. For example, the Hubble constant is expressed in `km⋅s⁻¹⋅Mpc⁻¹`, where both `km` and `Mpc` are units of *length*.

   In [[mp-units]](https://mpusz.github.io/mp-units) library, we’ve tried to refine symbolic expressions simplification rules to preserve the information of the origin. However, we were not satisfied with the results. The generated types were much longer and harder to reason about, which decreased the compile-time errors user experience. We’ve also got issues with basic library operations (e.g., determining the best common unit). More details can be found in [Refining symbolic expressions simplification rules](https://github.com/mpusz/mp-units/discussions/582) discussion.
4. **Repacking**

   In case an expression uses two results of some other operations, the components of its arguments are repacked into one resulting type and simplified there.

   For example, assuming:

   ```cpp
   constexpr auto X = A / B;
   ```

   then:

   | Operation | Resulting template expression arguments |
   | --- | --- |
   | `X * B` | `A` |
   | `X * A` | `power<A, 2>, per<B>` |
   | `X * X` | `power<A, 2>, per<power<B, 2>>` |
   | `X / X` | `{identity}` |
   | `X / A` | `{identity}, per<B>` |
   | `X / B` | `A, per<power<B, 2>>` |

#### 20.5.5 Symbolic expressions in action

Thanks to all of the steps described above, a user may write the code like this one:

```cpp
using namespace si::unit_symbols;
quantity speed = isq::speed(60. * km / h);
quantity duration = 8 * s;
quantity acceleration1 = speed / duration;
quantity acceleration2 = isq::acceleration(acceleration1.in(m / s2));
std::cout << "acceleration: " << acceleration1 << " (" << acceleration2 << ")\n";
```

the text output provides:

```
acceleration: 7.5 km h⁻¹ s⁻¹ (2.08333 m/s²)
```

The above program will produce the following types for *acceleration* quantities:

- `acceleration1`

  ```
  quantity<reference<derived_quantity_spec<isq::speed, per<isq::time>>,
                     derived_unit<si::kilo_<si::metre>, per<non_si::hour, si::second>>>{},
           double>
  ```
- `acceleration2`

  ```
  quantity<reference<isq::acceleration,
                     derived_unit<si::metre, per<power<si::second, 2>>>>{},
           double>>
  ```

### 20.6 Operations on units, dimensions, quantity types, and references

Modern C++ physical quantities and units library should expose compile-time constants for units, dimensions, and quantity types. Each of such constants should be of a different type. Said otherwise, every unit, dimension, and quantity type has a unique type and a compile-time instance. This allows us to do regular algebra on such identifiers and get proper types as results of such operations.

The operations exposed by such a library should include at least:

- multiplication (e.g., `newton * metre`),
- division (e.g., `metre / second`),
- power (e.g., `pow<2>(metre)` or `pow<1, 2>(metre * metre)`).

To improve the usability of the library, we also recommend adding:

- square root (e.g., `sqrt(metre * metre)` as equivalent to `pow<1, 2>(metre * metre)`),
- cubic root (e.g., `cbrt(metre * metre * metre)` as equivalent to `pow<1, 3>(metre * metre * metre)`),
- inversion (e.g., `inverse(second)` as equivalent to `one / second`).

Additionally, for units only, to improve the readability of the code, it makes sense to expose the following:

- square power (e.g., `square(metre)` is equivalent to `pow<2>(metre)`),
- cubic power (e.g., `cubic(metre)` is equivalent to `pow<3>(metre)`).

The above two functions could also be considered for dimensions and quantity types. However, `cubic(length)` does not seem to make much sense, and probably `pow<3>(length)` should be preferred instead.

Please note that we want to keep most of the unit magnitude’s interface *implementation-defined*. This is why we provide only a minimal mandatory interface for them. For example, we have introduced a `mag_power<Basis, Num, Den = 1>` helper to get a power of a magnitude. With that, a user should probably never need to reach for an alternative `pow<Num, Den>(mag<Base>)` version. However, the latter could be considered more consistent with the same operation done on other abstractions. Let’s compare how a unit can be defined using both of those syntaxes:

- with `mag_power`:

```cpp
 inline constexpr struct electronvolt :
  named_unit<"eV", mag_ratio<1'602'176'634, 1'000'000'000> * mag_power<10, -19> * si::joule> {} electronvolt;
```

- with `pow<>(mag<>)`:

```cpp
 inline constexpr struct electronvolt :
   named_unit<"eV", mag_ratio<1'602'176'634, 1'000'000'000> * pow<-19>(mag<10>) * si::joule> {} electronvolt;
```

Even though it might be inconsistent with operations on other abstractions, we’ve decided to use the first one as it seems easier to read and better resembles what we write on paper. However, we are not married to it, and we can change it if the LEWG prefers consistency here. Please note, that in such a case, for consistency, we probably should also provide `sqrt()` and `cbrt()` operations. However, those are really rare operations for magnitudes (we have not found any use cases for those in [[mp-units]](https://mpusz.github.io/mp-units) so far).

#### 20.6.1 Equality and equivalence

Units, their magnitudes, dimensions, quantity types, and references can be checked for equality with `operator==`. Equality for all the tag types is a simple check if both arguments are of the same type. For example, for dimensions, we do the following:

```cpp
template<Dimension Lhs, Dimension Rhs>
consteval bool operator==(Lhs lhs, Rhs rhs)
{
  return is_same_v<Lhs, Rhs>;
}
```

Equality for references is a bit more complex:

```cpp
template<typename Q1, typename U1, typename Q2, typename U2>
consteval bool operator==(reference<Q1, U1>, reference<Q2, U2>)
{
  return is_same_v<reference<Q1, U1>, reference<Q2, U2>>;
}

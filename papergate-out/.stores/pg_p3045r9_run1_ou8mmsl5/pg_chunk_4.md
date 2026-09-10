## 11 API overview

This chapter presents the library’s core abstractions and design choices. The `quantity` class template represents displacement vectors in an affine space, while `quantity_point` represents points. Generic interfaces enable efficient, type-safe code without unit-specific functions.

*Note for readers: Most application developers need only understand Quantity construction and basic operations (arithmetic, conversions, formatting). Generic interfaces are primarily for library developers designing reusable libraries. More advanced topics like affine space and quantity specifications are covered later for domain specialists and framework developers.*

More details about the design, rationale for it, and alternative syntaxes discussions can be found in the Design details and rationale chapter.

### 11.1 Quantity construction

The `quantity` class template takes a reference and representation type:

```cpp
template<Reference auto R,
         RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity;
```

`quantity` is best understood as a **numerical strong type wrapper**: it takes any number-like representation type and enriches it with compile-time metadata — a quantity specification and a measurement unit — collectively called the **quantity reference** — that the type system uses to enforce correctness. The runtime cost is zero; all safety guarantees are resolved at compile time.

This design is not limited to physical computation. Any countable or measurable domain is a valid target: file sizes, pixel counts, angular positions, currency amounts, database row counts, audio sample offsets, and more. If a value can be added to another value of the same kind, multiplied by a dimensionless factor, or meaningfully converted to a different scale, `quantity` can model it. The library is a general-purpose compile-time safety layer for numeric domain modelling, of which SI units are simply the most prominent example.

If we want to set a value for a quantity, we always have to provide a number and a unit:

```cpp
quantity<si::metre, int> q{42, si::metre};
```

In case a quantity class template should use exactly the same unit and a representation type as provided in the initializer, it is recommended to use CTAD:

```cpp
quantity q{42, si::metre};
```

The [[SI]](https://www.bipm.org/en/publications/si-brochure) says:

> The value of the quantity is the product of the number and the unit. The space between the number and the unit is regarded as a multiplication sign (just as a space between units implies multiplication).

Following the above, the value of a quantity can also be created by multiplying a number with a predefined unit:

```cpp
quantity q = 42 * si::metre;
```

The above creates an instance of `quantity<si::metre(), int>`. It is worth noting here that the syntax with the reversed order of arguments is invalid and will not compile (e.g., we can’t write `si::metre * 42`).

The same can be obtained using an optional unit symbol:

```cpp
using namespace si::unit_symbols;

quantity q = 42 * m;
```

Unit symbols introduce a lot of short identifiers into the current scope, which is why they are opt-in. A user has to explicitly “import” them from a dedicated `unit_symbols` namespace.

[[SI]](https://www.bipm.org/en/publications/si-brochure) specifies 7 base and 22 coherent derived units with special names. Additionally, it specifies 24 prefixes. There are also non-SI units accepted for use with SI. Some of them are really popular, for example, minute, hour, day, degree, litre, hectare, tonne. All of those entities compose to allow the creation of a vast number of various derived units.

For example, we can create a quantity of speed with either:

```cpp
quantity speed1 = 60 * si::kilo<si::metre> / non_si::hour;
quantity speed2 = 60 * km / h;
```

The library is optimized to generate short and easy-to-understand types that highly improve the analysis of compile-time errors and debugging experience. All of the above definitions will create an instance of the type `quantity<derived_unit<si::kilo_<si::metre>, per<non_si::hour>>{}, int>>`. As we can see, the type generation is optimized to be easily understood even by non-experts in the domain. The library tries to keep the type’s readability as close to English as possible.

To find more discussion on a quantity creation syntax please refer to the following chapters:

- `explicit` is not explicit enough,
- Why don’t we use UDLs to create quantities?,
- Potential surprises during units composition.

### 11.2 Generic interfaces

#### 11.2.1 The issues with unit-specific interfaces

Unit-specific function interfaces introduce several problems:

```cpp
quantity<km / h> avg_speed(quantity<km> distance, quantity<h> duration)
{
  return distance / duration;
}
```

Using this function:

```cpp
quantity<km / h> s1 = avg_speed(220 * km, 2 * h);
quantity<mi / h> s2 = avg_speed(140 * mi, 2 * h);
quantity<m / s> s3 = avg_speed(20 * m, 2 * s);
```

Problems:

1. Expensive unit conversions at each call and return.
2. Additional conversions to use results in caller’s preferred units.
3. Potential data truncation during conversions.
4. Forces floating-point types; integral types fail to compile without explicit `value_cast` or `force_in`, which can produce incorrect results (e.g., division by zero).

#### 11.2.2 Constraining function parameters with concepts

Generic code using quantity concepts eliminates these issues:

```cpp
auto avg_speed(QuantityOf<isq::length> auto distance,
               QuantityOf<isq::time> auto duration)
{
  return isq::speed(distance / duration);
}
```

This ensures arguments are implicitly convertible to the required quantity types while allowing the compiler to generate optimal code without conversions. Integral types can be safely used, improving performance.

#### 11.2.3 Constraining the function return type

Constraining return types provides documentation and verification:

```cpp
QuantityOf<isq::speed> auto avg_speed(QuantityOf<isq::length> auto distance,
                                      QuantityOf<isq::time> auto duration)
{
  return isq::speed(distance / duration);
}
```

Benefits:

1. Documents expected results for users.
2. Acts as a compile-time test verifying the quantity equation is correct.

#### 11.2.4 Constraining a variable on the stack

When using generic interfaces, constrain variables with concepts to document intent and verify correctness:

```cpp
QuantityOf<isq::speed> auto s1 = avg_speed(220 * km, 2 * h);
QuantityOf<isq::speed> auto s2 = avg_speed(140 * mi, 2 * h);
QuantityOf<isq::speed> auto s3 = avg_speed(20 * m, 2 * s);
```

This serves as documentation and a unit test for the returned type.

### 11.3 The affine space

The affine space distinguishes between:

- ***point*** - a position (*location*, *timestamp*, *altitude*, *temperature reading*, etc.)
- ***displacement vector*** - the difference between two points (*distance*, *duration*, *offset*, etc.)

The *displacement vector* described here is specific to the affine space theory and is not the same thing as the quantity of a vector character that we discuss later (although, in some cases, those terms may overlap).

In the following subchapters, we will often refer to *displacement vectors* simply as *vectors* for brevity.

#### 11.3.1 Operations in the affine space

Valid operations:

- *vector* ± *vector* → *vector*
- -*vector* → *vector*
- *vector* × scalar → *vector*
- scalar × *vector* → *vector*
- *vector* / scalar → *vector*
- *point* - *point* → *vector*
- *point* ± *vector* → *point*
- *vector* + *point* → *point*

It is not possible to:

- add two *points*,
- subtract a *point* from a *vector*,
- multiply nor divide *points* with anything else.

#### 11.3.2 *Displacement vector* is modeled by `quantity`

The `quantity` type models displacement vectors. Construction options include:

- Multiply syntax: `42 * m`, `100 * km / h`
- `delta<Reference>` constructor: `delta<deg_C>(3)`, `delta<isq::height[m]>(42)`
- Two-parameter constructor: `quantity{42, si::metre}`

The multiply syntax is disabled for units with inherent point origins (temperature units). Rationale is in `delta` and `point` creation helpers.

#### 11.3.3 *Point* is modeled by `quantity_point` and `PointOrigin`

The `quantity_point` class template represents points:

```cpp
template<Reference auto R,
         PointOriginFor<get_quantity_spec(R)> auto PO = default_point_origin(R),
         RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity_point;
```

The `PO` parameter specifies the measurement origin. By default, `default_point_origin(R)` provides:

- The unit’s defined origin (e.g., for °C, °F), or
- `natural_point_origin<QuantitySpec>` for other quantities.

Construction requires explicit conversion or the `point` helper:

```cpp
quantity_point qp1(42 * m);              // explicit conversion
quantity_point qp2 = point<m>(42);       // construction helper
quantity_point qp3 = point<deg_C>(21);   // temperature point
```

Multiply syntax is disabled to prevent confusion between vectors and points.

##### 11.3.3.1 `natural_point_origin<QuantitySpec>`

`natural_point_origin<QuantitySpec>` provides a default origin for domains with a well-established, unique zeroth point, eliminating boilerplate:

![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjwhLS0gQ3JlYXRlZCB3aXRoIElua3NjYXBlIChodHRwOi8vd3d3Lmlua3NjYXBlLm9yZy8pIC0tPgoKPHN2ZwogICB3aWR0aD0iOTYuNTE5NDQ3bW0iCiAgIGhlaWdodD0iMTguOTc3NTA3bW0iCiAgIHZpZXdCb3g9IjAgMCA5Ni41MTk0NDcgMTguOTc3NTA3IgogICB2ZXJzaW9uPSIxLjEiCiAgIGlkPSJzdmcxIgogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxkZWZzCiAgICAgaWQ9ImRlZnMxIj4KICAgIDxtYXJrZXIKICAgICAgIHN0eWxlPSJvdmVyZmxvdzp2aXNpYmxlIgogICAgICAgaWQ9IkRhcnRBcnJvdy03IgogICAgICAgcmVmWD0iMCIKICAgICAgIHJlZlk9IjAiCiAgICAgICBvcmllbnQ9ImF1dG8tc3RhcnQtcmV2ZXJzZSIKICAgICAgIG1hcmtlcldpZHRoPSIxIgogICAgICAgbWFya2VySGVpZ2h0PSIxIgogICAgICAgdmlld0JveD0iMCAwIDEgMSIKICAgICAgIHByZXNlcnZlQXNwZWN0UmF0aW89InhNaWRZTWlkIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImZpbGw6Y29udGV4dC1zdHJva2U7ZmlsbC1ydWxlOmV2ZW5vZGQ7c3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Ik0gMCwwIDUsLTUgLTEyLjUsMCA1LDUgWiIKICAgICAgICAgdHJhbnNmb3JtPSJzY2FsZSgtMC41KSIKICAgICAgICAgaWQ9InBhdGg2LTQiIC8+CiAgICA8L21hcmtlcj4KICA8L2RlZnM+CiAgPGcKICAgICBpZD0ibGF5ZXIxIgogICAgIHRyYW5zZm9ybT0idHJhbnNsYXRlKC0yNS42ODgwMzEsLTUuMTM3ODg0NSkiPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuNTtzdHJva2UtZGFzaGFycmF5Om5vbmU7bWFya2VyLWVuZDp1cmwoI0RhcnRBcnJvdy03KSIKICAgICAgIGQ9Ik0gMjUuNjg4MDMxLDIwLjE5MDgwNCBIIDExOC42ODU0OCIKICAgICAgIGlkPSJwYXRoNC0xIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gMzguOTcyNTgyLDE5LjE1MDc0NiB2IDIuMDgwMTE2IgogICAgICAgaWQ9InBhdGg3LTYiIC8+CiAgICA8cGF0aAogICAgICAgc3R5bGU9ImZpbGw6IzAwMDAwMDtzdHJva2U6I2E0YTRhNDtzdHJva2Utd2lkdGg6MC4yOTc4MjM7c3Ryb2tlLWRhc2hhcnJheToxLjE5MTI5LCAwLjI5NzgyMztzdHJva2UtZGFzaG9mZnNldDowO3N0cm9rZS1vcGFjaXR5OjEiCiAgICAgICBkPSJNIDM4Ljk3MjU4Miw2LjQ3NzA0OTIgViAxOC45NDA1OTQiCiAgICAgICBpZD0icGF0aDItMi0yIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gMTA2LjcwMDI0LDYuNDc3MDQ5IFYgMTguOTQwNTk0IgogICAgICAgaWQ9InBhdGgyLTItMS0wIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiNhNGE0YTQ7c3Ryb2tlLXdpZHRoOjAuMjk4O3N0cm9rZS1kYXNoYXJyYXk6MS4xOTIsIDAuMjk4O3N0cm9rZS1kYXNob2Zmc2V0OjA7c3Ryb2tlLW9wYWNpdHk6MSIKICAgICAgIGQ9Ik0gOTQuNDkzMDI2LDYuNDc3MDQ4OSBWIDE4Ljk0MDU5NCIKICAgICAgIGlkPSJwYXRoMi0yLTEtMC0wIiAvPgogICAgPHBhdGgKICAgICAgIHN0eWxlPSJmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAuMzgxMjk4O3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIGQ9Im0gOTQuNDkzMDI2LDE5LjE1MDc0NiB2IDIuMDgwMTE2IgogICAgICAgaWQ9InBhdGgyLTUtMiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0iZmlsbDojMDAwMDAwO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowLjM4MTI5ODtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICBkPSJtIDEwNi43MDAyNCwxOS4xNTA3NDYgdiAyLjA4MDExNiIKICAgICAgIGlkPSJwYXRoMi01LTctOCIgLz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iMzguMjk0OTMzIgogICAgICAgeT0iMjMuNjA1NTE1IgogICAgICAgaWQ9InRleHQyLTEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4yLTQiCiAgICAgICAgIHN0eWxlPSJmb250LXNpemU6Mi40Njk0NHB4O3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iMzguMjk0OTMzIgogICAgICAgICB5PSIyMy42MDU1MTUiPjA8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuNDY5NDRweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgeD0iOTIuNDQzODAyIgogICAgICAgeT0iMjMuNjI4MjU0IgogICAgICAgaWQ9InRleHQyLTItOSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS05IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuNDY5NDRweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI5Mi40NDM4MDIiCiAgICAgICAgIHk9IjIzLjYyODI1NCI+cXAxPC90c3Bhbj48L3RleHQ+CiAgICA8dGV4dAogICAgICAgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIKICAgICAgIHN0eWxlPSJmb250LXdlaWdodDpib2xkO2ZvbnQtc2l6ZToyLjExNjY3cHg7Zm9udC1mYW1pbHk6QXJpYWw7LWlua3NjYXBlLWZvbnQtc3BlY2lmaWNhdGlvbjonQXJpYWwgQm9sZCc7ZmlsbDojZDQwMDAwO2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjY1LjcyNDEyOSIKICAgICAgIHk9IjE1LjkwMzc4IgogICAgICAgaWQ9InRleHQyLTItNy00OSI+PHRzcGFuCiAgICAgICAgIGlkPSJ0c3BhbjItOS0wLTk2IgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNkNDAwMDA7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI2NS43MjQxMjkiCiAgICAgICAgIHk9IjE1LjkwMzc4Ij5xMTwvdHNwYW4+PC90ZXh0PgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi40Njk0NHB4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSIxMDQuNTEyMzMiCiAgICAgICB5PSIyMy42MjgyNTQiCiAgICAgICBpZD0idGV4dDItMi0yLTMxIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjQ2OTQ0cHg7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iMTA0LjUxMjMzIgogICAgICAgICB5PSIyMy42MjgyNTQiPnFwMjwvdHNwYW4+PC90ZXh0PgogICAgPGcKICAgICAgIGlkPSJwYXRoOC0wIj4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC44NTkwMjUsMTYuOTU4NjI1IEggOTMuODgzMjEzIgogICAgICAgICBpZD0icGF0aDE5IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljg1OTM3NSwxNi44MzM5ODQgdiAwLjI1IGggNTUuMDIzNDM3IHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgyMCIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImcxOCI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNkNDAwMDA7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gOTIuNTg3ODkxLDE2LjA1MDc4MSAtMC4xNTgyMDQsMC4zMTY0MDYgMS4xODM1OTQsMC41OTE3OTcgLTEuMTgzNTk0LDAuNTkxNzk3IDAuMTU4MjA0LDAuMzE2NDA2IDEuODE2NDA2LC0wLjkwODIwMyB6IgogICAgICAgICAgIGlkPSJwYXRoMTgiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzttaXgtYmxlbmQtbW9kZTpub3JtYWw7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9Ijk2LjAzMDU0OCIKICAgICAgIHk9IjYuNjgzMDEyIgogICAgICAgaWQ9InRleHQyLTItNy00OS01Ij48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNCIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iOTYuMDMwNTQ4IgogICAgICAgICB5PSI2LjY4MzAxMiI+cXAyIC0gcXAxPC90c3Bhbj48L3RleHQ+CiAgICA8ZwogICAgICAgaWQ9InBhdGg4LTAtOSI+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJNIDk0LjY2ODYwNSw4LjEzNDcyNTkgSCAxMDYuMTUyNyIKICAgICAgICAgaWQ9InBhdGgxMyIgLz4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eTowLjk2MDc4NDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgIGQ9Im0gOTQuNjY3OTY5LDguMDA5NzY1NiB2IDAuMjUgaCAxMS40ODQzNzEgdiAtMC4yNSB6IgogICAgICAgICBpZD0icGF0aDE0IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzEyIj4KICAgICAgICA8cGF0aAogICAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDstaW5rc2NhcGUtc3Ryb2tlOm5vbmUiCiAgICAgICAgICAgZD0ibSAxMDQuODU3NDIsNy4yMjY1NjI1IC0wLjE1ODIsMC4zMTY0MDYyIDEuMTgzNTksMC41OTE3OTY5IC0xLjE4MzU5LDAuNTkxNzk2OSAwLjE1ODIsMC4zMTY0MDYzIDEuODE2NDEsLTAuOTA4MjAzMiB6IgogICAgICAgICAgIGlkPSJwYXRoMTIiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICAgIDxnCiAgICAgICBpZD0icGF0aDMtMi02Ij4KICAgICAgPHBhdGgKICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojMDAwMGRkOy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOC45NDczNDcsMTIuNjM5MjMzIEggMTA2LjA4NTYyIgogICAgICAgICBpZD0icGF0aDE2IiAvPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM4Ljk0NzI2NiwxMi41MTM2NzIgdiAwLjI1IGggNjcuMTM4Njc0IHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGgxNyIgLz4KICAgICAgPGcKICAgICAgICAgaWQ9ImcxNSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiMwMDAwZGQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICAgIGQ9Im0gMTA0Ljc4OTA2LDExLjczMDQ2OSAtMC4xNTgyLDAuMzE2NDA2IDEuMTgzNTksMC41OTE3OTcgLTEuMTgzNTksMC41OTE3OTcgMC4xNTgyLDAuMzE2NDA2IDEuODE2NDEsLTAuOTA4MjAzIHoiCiAgICAgICAgICAgaWQ9InBhdGgxNSIgLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPHRleHQKICAgICAgIHhtbDpzcGFjZT0icHJlc2VydmUiCiAgICAgICBzdHlsZT0iZm9udC13ZWlnaHQ6Ym9sZDtmb250LXNpemU6Mi4xMTY2N3B4O2ZvbnQtZmFtaWx5OkFyaWFsOy1pbmtzY2FwZS1mb250LXNwZWNpZmljYXRpb246J0FyaWFsIEJvbGQnO2ZpbGw6IzAwMDBkZDtmaWxsLW9wYWNpdHk6MTtzdHJva2U6IzAwMDAwMDtzdHJva2Utd2lkdGg6MDtzdHJva2UtZGFzaGFycmF5Om5vbmUiCiAgICAgICB4PSI3MS42ODQ0OTQiCiAgICAgICB5PSIxMS42NTU3NyIKICAgICAgIGlkPSJ0ZXh0Mi0yLTItNS0xIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTYtMi04NSIKICAgICAgICAgc3R5bGU9ImZvbnQtc2l6ZToyLjExNjY3cHg7ZmlsbDojMDAwMGRkO2ZpbGwtb3BhY2l0eToxO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgICAgeD0iNzEuNjg0NDk0IgogICAgICAgICB5PSIxMS42NTU3NyI+cTI8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuODIyMjJweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJztmaWxsOiMwMDAwMDA7c3Ryb2tlOiMwMDAwMDA7c3Ryb2tlLXdpZHRoOjAiCiAgICAgICB4PSIxMjAuMDQ5NDgiCiAgICAgICB5PSIyMy45MTA0MDgiCiAgICAgICBpZD0idGV4dDEiPjx0c3BhbgogICAgICAgICBpZD0idHNwYW4xIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuODIyMjJweDtzdHJva2Utd2lkdGg6MCIKICAgICAgICAgeD0iMTIwLjA0OTQ4IgogICAgICAgICB5PSIyMy45MTA0MDgiPlE8L3RzcGFuPjwvdGV4dD4KICAgIDx0ZXh0CiAgICAgICB4bWw6c3BhY2U9InByZXNlcnZlIgogICAgICAgc3R5bGU9ImZvbnQtd2VpZ2h0OmJvbGQ7Zm9udC1zaXplOjIuMTE2NjdweDtmb250LWZhbWlseTpBcmlhbDstaW5rc2NhcGUtZm9udC1zcGVjaWZpY2F0aW9uOidBcmlhbCBCb2xkJzttaXgtYmxlbmQtbW9kZTpub3JtYWw7ZmlsbDojYTRhNGE0O2ZpbGwtb3BhY2l0eToxO3N0cm9rZTojMDAwMDAwO3N0cm9rZS13aWR0aDowO3N0cm9rZS1kYXNoYXJyYXk6bm9uZSIKICAgICAgIHg9IjU0LjAzNTQ5MiIKICAgICAgIHk9IjYuNjc4ODc3OCIKICAgICAgIGlkPSJ0ZXh0Mi0yLTctNDktNS0zLTItNi0yIj48dHNwYW4KICAgICAgICAgaWQ9InRzcGFuMi05LTAtOTYtNC0xLTgtOC0xIgogICAgICAgICBzdHlsZT0iZm9udC1zaXplOjIuMTE2NjdweDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjE7c3Ryb2tlLXdpZHRoOjA7c3Ryb2tlLWRhc2hhcnJheTpub25lIgogICAgICAgICB4PSI1NC4wMzU0OTIiCiAgICAgICAgIHk9IjYuNjc4ODc3OCI+cXAxLnF1YW50aXR5X2Zyb21fdW5pdF96ZXJvKCk8L3RzcGFuPjwvdGV4dD4KICAgIDxnCiAgICAgICBpZD0icGF0aDgtMC05LTgtMC0wLTAiCiAgICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMC4yMTM2NzIzMSwtOTAuOTM3NSkiPgogICAgICA8cGF0aAogICAgICAgICBzdHlsZT0iY29sb3I6IzAwMDAwMDtmaWxsOiNhNGE0YTQ7ZmlsbC1vcGFjaXR5OjAuOTYwNzg0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgZD0iTSAzOS4xMDc3MTksOTkuMDcxODI2IEggOTQuMTE1NzcyIgogICAgICAgICBpZD0icGF0aDU2LTAiIC8+CiAgICAgIDxwYXRoCiAgICAgICAgIHN0eWxlPSJjb2xvcjojMDAwMDAwO2ZpbGw6I2E0YTRhNDtmaWxsLW9wYWNpdHk6MC45NjA3ODQ7LWlua3NjYXBlLXN0cm9rZTpub25lIgogICAgICAgICBkPSJtIDM5LjEwNzQyMiw5OC45NDcyNjYgdiAwLjI1IGggNTUuMDA3ODEyIHYgLTAuMjUgeiIKICAgICAgICAgaWQ9InBhdGg1Ny04IiAvPgogICAgICA8ZwogICAgICAgICBpZD0iZzU1LTQiPgogICAgICAgIDxwYXRoCiAgICAgICAgICAgc3R5bGU9ImNvbG9yOiMwMDAwMDA7ZmlsbDojYTRhNGE0Oy1pbmtzY2FwZS1zdHJva2U6bm9uZSIKICAgICAgICAgICBkPSJtIDkyLjgyMDMxMiw5OC4xNjQwNjIgLTAuMTU4MjAzLDAuMzE2NDA3IDEuMTgzNTk0LDAuNTkxNzk3IC0xLjE4MzU5NCwwLjU5MTc5NiAwLjE1ODIwMywwLjMxNjQwNyAxLjgxNjQwNywtMC45MDgyMDMgeiIKICAgICAgICAgICBpZD0icGF0aDU1LTkiIC8+CiAgICAgIDwvZz4KICAgIDwvZz4KICA8L2c+Cjwvc3ZnPgo=)

```cpp
quantity_point<isq::distance[si::metre]> qp1(100 * m);
quantity_point<isq::distance[si::metre]> qp2 = point<m>(120);

assert(qp2 - qp1 == 20 * m);
assert(qp1.quantity_from_zero() == 100 * m);
// auto res = qp1 + qp2;   // Compile-time error
```

Key design considerations:

- Points can be explicitly constructed from quantities when using `zeroth_point_origin`.
- A point has no inherent value—it’s a position expressible with different displacement vectors from different origins.
- **Safety trade-off**: `natural_point_origin` makes quantity points compatible when their quantity types are compatible (e.g., `isq::distance` and `isq::height` points can be subtracted), which may be surprising but enables ergonomic usage for common cases.

##### 11.3.3.2 Absolute *point* origin

Absolute point origins establish isolated, independent spaces where points are incompatible even with the same quantity type:

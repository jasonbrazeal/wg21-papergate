## 19 Safety

Physical quantities and units libraries prevent errors at compile time through multiple safety layers. All safety features described here have **zero runtime overhead**—they’re enforced entirely at compile time, providing safety without performance cost.

### 19.1 Overview of safety levels

This library provides six distinct safety levels:

1. **Dimension Safety** - Prevents mixing incompatible dimensions (e.g., adding *length* to *time*)
2. **Unit Safety** - Prevents unit mismatches and eliminates manual scaling factors
3. **Representation Safety** - Protects against overflows and precision loss
4. **Quantity Kind Safety** - Prevents arithmetic on quantities of different kinds (e.g., `Hz` vs `Bq`)
5. **Quantity Safety** - Enforces correct quantity relationships and equation ingredients
6. **Mathematical Space Safety** - Distinguishes points (absolute positions) from vectors (differences)

All major C++ units libraries provide dimension safety (level 1) and unit safety (level 2). Some provide representation safety (level 3) and mathematical space safety (level 6). However, [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.

### 19.2 Dimension safety

Dimension safety prevents mixing quantities with incompatible dimensions through automatic dimensional analysis:

```cpp
quantity<si::metre / si::second> speed = 100 * km / h;  // OK: km/h is speed (same as m/s)
quantity<si::second> time = 2 * h;                      // OK: hour is time (same as second)
quantity<si::metre> distance = speed * time;            // OK: length
// quantity<si::metre> distance = 2 * h;                // Error: incompatible dimensions!
// quantity<si::metre> distance = speed / time;         // Error: wrong dimension!
// auto result = distance + time;                       // Error: cannot add length and time!
```

All major C++ units libraries provide this foundational feature enabling dimensional analysis.

### 19.3 Unit safety

Unit safety ensures compatible units at interface boundaries (function arguments, return types, component integration).

```cpp
// Function accepts any length and time units
quantity<si::metre / si::second> avg_speed(quantity<si::metre> d, quantity<si::second> t)
{
  return d / t;
}

quantity distance = 220 * km;
quantity time = 2 * h;
quantity<km / h> speed = avg_speed(distance, time);  // 110 km/h - automatic conversion
```

Unit conversions are automated and checked at compile-time:

```cpp
auto q1 = 5 * km;
std::cout << q1.in(m) << '\n';           // prints: 5000 m
quantity<si::metre, int> q2 = q1;        // OK: km → m
```

Unlike `std::chrono::duration` which uses `std::ratio`, this library supports arbitrary conversion factors including irrational numbers (π for radians/degrees) and extreme ratios (electronvolt: 1 eV = 1.602176634×10⁻¹⁹ J).

#### 19.3.1 Safe quantity numerical value getters

Legacy APIs often require raw numerical values. Always specify the unit explicitly:

```cpp
void legacy_func(std::int64_t seconds);
```

**Bad** (like `std::chrono::duration::count()` - doesn’t specify unit):

```cpp
struct X {
  std::vector<std::chrono::milliseconds> vec;
};

X x;
x.vec.emplace_back(42s);
legacy_func(x.vec[0].count());  // Wrong if storage does not match seconds!
```

**Good** (explicit unit specification):

```cpp
struct X {
  std::vector<quantity<si::milli<si::second>>> vec;
};

X x;
x.vec.emplace_back(42 * s);
legacy_func(x.vec[0].numerical_value_in(si::second));        // Safe
legacy_func(x.vec[0].force_numerical_value_in(si::second));  // If truncation OK
```

The member function `numerical_value_ref_in(Unit)` enables direct access without conversion or copying:

```cpp
void legacy_func(const int& joules);

quantity q1 = 42 * J;
quantity q2 = 42 * N * (2 * m);
quantity q3 = 42 * kJ;

legacy_func(q1.numerical_value_ref_in(si::joule));  // OK
legacy_func(q2.numerical_value_ref_in(si::joule));  // OK (equivalent unit)
legacy_func(q3.numerical_value_ref_in(si::joule));  // Compile-time error (different magnitude)
legacy_func((4 * J + 2 * J).numerical_value_ref_in(si::joule));  // Compile-time error (rvalue)
```

This prevents most dangling references while acknowledging the value category ≠ lifetime limitation (see [[Value Category Is Not Lifetime]](https://quuxplusone.github.io/blog/2019/03/11/value-category-is-not-lifetime/)).

### 19.4 Representation safety

Representation safety protects against numerical issues like overflow, underflow, and precision loss during conversions and arithmetic operations.

#### 19.4.1 Truncation prevention

Conversions that would lose precision with integral types are prevented at compile-time:

```cpp
quantity q1 = 5 * m;
std::cout << q1.in(km) << '\n';              // Compile-time error
quantity<si::kilo<si::metre>, int> q2 = q1;  // Compile-time error
```

Converting 5 meters to kilometers with `int` would truncate to 0. To allow such conversions, use floating-point types or explicit casts:

```cpp
quantity q1 = 5. * m;                        // double representation
std::cout << q1.in(km) << '\n';              // OK: prints 0.005 km
```

```cpp
quantity q1 = 5 * m;                         // int representation  
std::cout << q1.in<double>(km) << '\n';      // OK: explicit conversion to double
std::cout << q1.force_in(km) << '\n';        // OK: explicit truncation (prints 0 km)
quantity<si::kilo<si::metre>, int> q2 = value_cast<km>(q1);  // OK: explicit cast
```

The same protection applies to representation type conversions:

```cpp
quantity q1 = 2.5 * m;
quantity<si::metre, int> q2 = q1;                   // Compile-time error
quantity<si::metre, int> q3 = value_cast<int>(q1);  // OK: explicit truncation
```

Combined conversions (unit + representation) are supported to prevent intermediate overflow:

```cpp
value_cast<Unit, Representation>(Quantity);
value_cast<Representation, Unit>(Quantity);
value_cast<Unit, Representation>(QuantityPoint);
value_cast<Representation, Unit>(QuantityPoint);
q.force_in<Representation>(Unit);
qp.force_in<Representation>(Unit);
```

#### 19.4.2 Scaling overflow prevention

Converting small integral types between units can overflow even for non-zero values:

```cpp
quantity q1 = std::int8_t(1) * km;
quantity q2 = q1.force_in(m);   // Compile-time error (factor 1'000 > max int8_t)
if(q1 != 1 * m) { /* ... */ }   // Compile-time error
```

The conversion factor (1000) exceeds `std::int8_t` range, so the library prevents the conversion even though `0 * km` would technically work. See Integer overflow for details.

*Note: No library can prevent runtime arithmetic overflow at compile time (e.g., `quantity * 2`), nor can they prevent floating-point overflow/underflow. For such cases, use custom representation types with runtime checks.*

#### 19.4.3 `explicit` is not explicit enough

Consider:

```cpp
struct X {
  std::vector<std::chrono::milliseconds> vec;
};
X x;
x.vec.emplace_back(42);  // Compiles but fragile!
```

If someone changes `milliseconds` to `microseconds`, the code still compiles but calculations are wrong by 1000×. The solution: require both number and unit:

```cpp
struct X {
  std::vector<quantity<si::milli<si::second>>> vec;
};
X x;
x.vec.emplace_back(42);       // Compile-time error
x.vec.emplace_back(42 * ms);  // OK
```

Similarly, `quantity_point` requires explicit origin association (unlike `std::chrono::time_point`):

```cpp
quantity_point qp1 = mean_sea_level + 42 * m;
quantity_point qp2 = default_ac_temperature + 2 * delta<deg_C>;
```

### 19.5 Quantity kind safety

Quantity kind safety distinguishes between quantities sharing the same dimension but representing different physical concepts.

What should `1 * Hz + 1 * Bq + 1 * Bd` equal? Several leading libraries disagree:

- [[Boost.Units]](https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html) claims the answer to be 2 Hz (bauds not supported),
- [[nholthaus/units]](https://github.com/nholthaus/units) claims it is 2 s<sup>-1</sup> (bauds not supported),
- [[Pint]](https://pint.readthedocs.io/en/stable/index.html) library in Python claims the result is 3.0 Hz,
- [[JSR 385]](https://unitsofmeasurement.github.io/indriya) library in Java throws an exception—**the only correct answer**.

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) states:

- Quantities may be grouped into categories that are **mutually comparable**
- Mutually comparable quantities are **quantities of the same kind**
- Quantities **cannot be added or subtracted unless they belong to the same category**
- Quantities of the **same kind** have the **same dimension**
- Quantities of the **same dimension are not necessarily of the same kind**

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly notes:

> Measurement units of quantities of the same quantity dimension may be designated by the same name and symbol even when the quantities are not of the same kind. For example, joule per kelvin and J/K are respectively the name and symbol of both a measurement unit of heat capacity and a measurement unit of entropy, which are generally not considered to be quantities of the same kind. **However, in some cases special measurement unit names are restricted to be used with quantities of specific kind only**. For example, the measurement unit ‘second to the power minus one’ (1/s) is called hertz (Hz) when used for frequencies and becquerel (Bq) when used for activities of radionuclides.

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) explicitly states that *frequency* (Hz) and *activity* (Bq) are different kinds—they should not be comparable, added, or subtracted. Allowing such operations leads to safety issues when unrelated quantities of the same dimension are accidentally added or assigned:

```cpp
quantity absorbed_dose = 1.5 * Gy;
quantity dose_equivalent = 2.0 * Sv;

// auto result = absorbed_dose + dose_equivalent;           // Compile-time error!
// Error: cannot add absorbed dose and dose equivalent (both L²T⁻², but different kinds)

// QuantityOf<isq::absorbed_dose> auto d = 2.5 * Sv;        // Compile-time error!
// Error: cannot initialize absorbed dose with dose equivalent
```

*[[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety, fully distinguishing all SI quantity kinds including Gy/Sv, Hz/Bq, and rad/sr.*

### 19.6 Quantity safety

Quantity safety is the highest level, ensuring semantic correctness through:

1. **Quantity Type Correctness** - Hierarchies, conversions, and quantity equation ingredient validation
2. **Quantity Character Correctness** - Representation types and character-specific operations

#### 19.6.1 Quantity hierarchies

Dimension-only libraries can’t distinguish between different quantities of the same kind:

```cpp
class Box {
  quantity<isq::area[m2]> base_;
  quantity<isq::length[m]> height_;  // Can't distinguish length, width, height!
public:
  Box(quantity<isq::length[m]> l, quantity<isq::length[m]> w, quantity<isq::length[m]> h)
    : base_(l * w), height_(h) {}
};
```

[[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) defines hierarchies: *width*, *height*, *radius* are distinct but all are *lengths*. This library models these hierarchies to prevent errors:

```cpp
// Quantity Type: Hierarchy prevents mixing energy types
void process_kinetic(quantity<isq::kinetic_energy[J]> ke) { /* ... */ }

quantity pe = isq::potential_energy(100 * J);
// process_kinetic(pe);                                                   // Compile-time error!
// Error: cannot pass potential_energy where kinetic_energy is required

// Quantity Type: Ingredient validation requires specific quantity types
quantity<isq::height[m]> h = 5 * m;
quantity<isq::gravitational_potential_energy[J]> Ep = mass * g * height;  
// quantity<isq::gravitational_potential_energy[J]> wrong = mass * g * width;  // Compile-time error!
// Error: cannot form gravitational potential energy from width
```

See Systems of quantities for details.

#### 19.6.2 Safe operations of vector and tensor quantities

While talking about quantities and units libraries, everyone expects that the library will protect (preferably at compile-time) from accidentally replacing multiplication with division operations or vice versa. Everyone knows and expects that the multiplication of *length* and *time* should not result in *speed*. It does not mean that such a quantity equation is invalid. It just results in a quantity of a different type.

If we expect the above protection for scalar quantities, we should also strive to provide similar guarantees for vector and tensor quantities. First, the multiplication or division of two vectors or tensors is not even mathematically defined. Such operations should be impossible on quantities using vector or tensor representation types.

What multiplication and division are for scalars, the dot and cross products are for vector quantities. The result of the first one is a scalar. The second one results in a vector perpendicular to both vectors passed as arguments. A good quantities and units library should protect the user from making such an error of accidentally replacing those operations.

Vector and tensor quantities can be implemented in two ways:

1. Encapsulating multiple quantities into a homogeneous vector or tensor representation type

   This solution is the most common in the C++ market. It requires the quantities library to provide only basic arithmetic operations (addition, subtraction, multiplication, and division) which are being used to calculate the result of linear algebra math. However, this solution can’t provide any compile-time safety described above, and will also crash when someone passes a proper vector and tensor representation type to a quantity, expecting it to work.
2. Encapsulating a vector or tensor as a representation type of a quantity

   This provides all the required type safety, but requires the library to implement more operations on quantities and properly constrain them so they are selectively enabled when needed. Besides [[mp-units]](https://mpusz.github.io/mp-units), the only library that supports such an approach is [[Pint]](https://pint.readthedocs.io/en/stable/index.html). Such a solution requires the following operations to be exposed for quantity types (note that character refers to the algebraic structure of either scalar, vector and tensor):
   - `a + b` - addition where both arguments should be of the same quantity kind and character
   - `a - b` - subtraction where both arguments should be of the same quantity kind and character
   - `a % b` - modulo where both arguments should be of the same quantity kind and character
   - `a * b` - multiplication where one of the arguments has to be a scalar
   - `a / b` - division where the divisor has to be scalar
   - `a ⋅ b` - dot product of two vectors
   - `a × b` - cross product of two vectors
   - `|a|` - magnitude (norm) of a vector, i.e., `norm(a)`
   - `a ⊗ b` - tensor product of two vectors or tensors
   - `a ⋅ b` - inner product of two tensors
   - `a ⋅ b` - inner product of tensor and vector
   - `a : b` - scalar product of two tensors

Additionally, the library knows the expected quantity character, which is provided (implicitly or explicitly) in the definition of each quantity type. Thanks to that, it prevents the user, for example, from providing a vector representation type for *speed*.

```cpp
quantity q1 = isq::speed(60 * km / h);                       // OK
quantity q2 = isq::speed(la_vector{0, 0, -60} * km / h);     // Compile-time error
quantity q3 = isq::velocity(60 * km / h);                    // OK
quantity q4 = isq::velocity(la_vector{0, 0, -60} * km / h);  // OK
```

As we can see above, such features additionally improves the compile-time safety of the library by ensuring that quantities are created with proper quantity equations and are using correct representation types.

#### 19.6.3 Complex quantities

Complex quantities enforce domain-specific construction rules. Example: *complex power* requires *active power* and *reactive power* in correct order:

```cpp
quantity<isq::complex_power[V * A], std::complex<double>> complex = get_power();
quantity<isq::active_power[W]> active = complex.real();
quantity<isq::reactive_power[var]> reactive = complex.imag();
quantity<isq::apparent_power[V * A]> apparent = complex.modulus();
```

### 19.7 Mathematical space safety

Mathematical space safety distinguishes between **quantity points** (absolute positions) and **quantity vectors** (differences/displacements). `quantity` represents vectors; `quantity_point` represents points. This prevents nonsensical operations:

**Forbidden operations:**

- Adding two points: `home + airport` (what is “Boston + New York”?)
- Subtracting vector from point: `distance - airport`
- Scaling points: `2 * airport`
- Mixing incompatible point origins

**Allowed operations:**

- Subtracting points yields vector: `airport - home` → distance
- Adding vector to point: `home + distance` → new location
- Scaling vectors: `2 * distance`

Example with temperature: *Temperatures* are points on a scale with an origin; *temperature changes* are vectors. You can add *temperature changes*, but adding two *temperatures* is meaningless:

```cpp
// Points: Positions on a scale with an origin
quantity_point room_temp = point<deg_C>(20.);
quantity_point outside_temp = point<deg_C>(5.);

quantity temp_diff = room_temp - outside_temp;      // OK: 15 K (vector)
// auto temp_sum = room_temp + outside_temp;        // Compile-time error!
// Error: cannot add points (meaningless: what is 20 °C + 5 °C?)

// Vectors: Differences between values
quantity temp_change = delta<K>(10);
quantity_point new_temp = room_temp + temp_change;  // OK: point + vector = 30 °C
quantity total_change = temp_change + temp_change;  // OK: vector + vector = 20 K

// auto wrong = temp_change - room_temp;            // Compile-time error!
// Error: cannot subtract point from vector (meaningless: what is 10 K - 20 °C?)
```

Examples where mathematical space safety prevents errors: *temperature* (cannot add 20 °C + 10 °C, but can compute difference), *time* (cannot add two *timestamps*, but can subtract them), *position* (cannot add GPS coordinates, but can compute *displacement*), *altitude* (cannot add two *elevations*, but can compute *height* difference).

### 19.8 Safety pitfalls

#### 19.8.1 Integer division

If we expect `120 * km / (2 * h)` to return `60 km / h`, we have to agree with the fact that `5 * km / (24 * h)` returns `0 km/h`. We can’t do a range check at runtime to dynamically adjust scales and types based on the values of provided function arguments.

The same applies to:

```cpp
static_assert(5 * h / (120 * min) == 0 * one);
```

We may consider adding a special mode to detect the above cases at compile-time and try to bring the unit to a common unit before doing the operation. However, it will make it inconsistent with the following code:

```cpp
static_assert(2 * m * (5 * h) / (120 * min) == 0 * m);
```

If we decide to change the current behavior, it would:

- make generic programming harder,
- should be enabled only for integers (inconsistent resulting units with floating-point mode),
- would make it harder to express ratios of hugely different units of the same dimension (e.g., Hubble constant is expressed in `km/s/Mpc`).

This is why floating-point representation types are recommended as a default to store the numerical value of a quantity. Some popular physical units libraries even [forbid integer division at all](https://aurora-opensource.github.io/au/main/troubleshooting/#integer-division-forbidden).

#### 19.8.2 Integer overflow

**The problem**: Unit conversions multiply by hidden factors. Comparing `11 * m > 12 * yd` converts both to a common unit (800 μm), multiplying by ~1000× under the hood—easy to overflow small integer types.

**Mitigation strategies:** in fact, at the time of writing, new strategies are still being developed and tested. Here are the main strategies we have seen.

##### 19.8.2.1 Do nothing

This is the simplest approach, and probably also the most popular: make the users responsible for avoiding overflow. The documentation may simply warn them to check their values ahead of time, as in this [example from the bernedom/SI library](https://github.com/bernedom/SI/blob/main/doc/implementation-details.md#implicit-ratio-conversion--possible-loss-of-precision). This valid approach places substantial responsibility on users, many unaware of the risk. Since unit conversions are hard to spot, this likely leads to the highest incidence of overflow bugs.

##### 19.8.2.2 Curate user-facing types

[`std::chrono`](https://en.cppreference.com/w/cpp/chrono/duration) crafts user-facing types with generous ranges: all named durations shorter than a day (hours to nanoseconds) represent ±292 years. Users within this range who stick to these primary types avoid overflow.

This works well for time-only libraries but doesn’t scale to multi-dimensional units libraries where quantity types proliferate and users can create arbitrary combinations on the fly.

##### 19.8.2.3 Adapt to risk

Overflow risk depends on: (1) conversion factor size (bigger = more risk)<sup>2</sup>, and (2) maximum representable value (larger = less risk).

An adaptive policy can forbid conversions where the “smallest overflowing value” is “small enough to be scary”. [[Au]](https://aurora-opensource.github.io/au) uses threshold 2,147: if this value converts without overflow, permit the operation. This prevents operations failing on values under 1,000 while allowing common patterns like `500 * mega<hertz>` in `int32_t`. Production experience confirms this provides good default protection.

This paper is more conservative: we fail conversion if the representation can’t handle value `1` converted to the destination unit (see Scaling overflow prevention), pessimizing only the `0` case.

##### 19.8.2.4 Check every conversion at runtime

Runtime checks guarantee perfect safety. While unit conversions rarely appear in hot loops, making runtime cost worthwhile, the main challenge is error handling (exceptions, `optional`, `expected`, contracts, etc.).

A promising approach separates error detection and response: the library provides boolean checkers for overflow/truncation, then each project uses these with their preferred error handling mechanism.

##### 19.8.2.5 Delegate to rep

Perhaps the most appealing approach to overflow in units libraries is to delegate the problem to another library entirely. Quantity types can work with any underlying numeric type (called the “rep”, as in the `chrono` library) that satisfies certain concepts related to basic arithmetic. If that rep comes from a library that is dedicated to providing overflow-safe numeric types, then the problem is solved without any additional effort on the units library side.

This approach currently suffers from at least two significant downsides. First, it is less thoroughly tested in production usage, so we don’t know what the practical pitfalls are. Second, raw numeric types are likely to be overwhelmingly common in practice, and using this approach alone would leave this group of users unprotected—a group where less-experienced users are likely to be over-represented. Therefore, this can’t be the *only* solution to overflow.

#### 19.8.3 Lack of safe numeric types

Integers overflow on arithmetic (causing expensive failures [[Ariane flight V88]](https://en.wikipedia.org/wiki/Ariane_flight_V88)) and truncate on narrowing assignment. Floating-point types lose precision on narrowing, and `int64_t` to `double` conversion also loses precision.

Safe numeric types in the standard library would address these concerns as `quantity` reps. A type trait indicating value-preserving conversions would also help.

#### 19.8.4 Potential surprises during units composition

Units compose to create derived units (`constexpr Unit auto kmph = km / h;`), an industry standard in [[Boost.Units]](https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html) and [[Pint]](https://pint.readthedocs.io/en/stable/index.html).

However, order of operations can surprise users:

```cpp
quantity q = 60 * km / 2 * h;  // Results in 30 km⋅h, not 30 km/h
quantity q = 60 * km / (2 * h); // Requires parentheses for 30 km/h
```

Generic code can also produce unexpected types:

```cpp
template<typename T>
auto make_length(T v) { return v * si::metre; }

quantity v = 42 * m;
quantity q = make_length(v);  // Returns area (m²), not length!
```

[[mp-units]](https://mpusz.github.io/mp-units) initially disallowed multiplying/dividing quantities by units to prevent this, but requiring `60 * (km / h)` proved too verbose and confusing.

These issues always surface as compile-time errors when assigning to explicitly-typed quantities:

```cpp
quantity<si::kilo<si::metre> / non_si::hour, int> q1 = 60 * km / 2 * h;  // Error
QuantityOf<isq::speed> auto q3 = 60 * km / 2 * h;                        // Error
quantity<si::metre, int> q1 = make_length(42 * m);                       // Error
QuantityOf<isq::length> auto make_length(T v) { return v * si::metre; }  // Constrains return type
```

#### 19.8.5 Limitations of systems of quantities

Modeling systems of quantities improves safety but has pitfalls in corner cases.

##### 19.8.5.1 Allowing irrational quantity combinations

While `length * length → area` makes sense bidirectionally, `width * height → area` is unidirectional—not all areas are width×height products:

```cpp
static_assert(implicitly_convertible(isq::width * isq::height, isq::area));
static_assert(!implicitly_convertible(isq::area, isq::width * isq::height));
```

Surprisingly, `height * height → area` behaves similarly. While hard to imagine physically, the library cannot prevent such operations.

##### 19.8.5.2 Arithmetic and compatibility of quantities of dimension one

Dividing quantities of the same kind yields dimension-one quantities with different meanings (*slope of ramp*, *clock accuracy*), yet they’re mutually comparable per dimensional analysis.

The above means that the following code is valid:

```cpp
quantity q1 = isq::length(1. * m) / isq::length(10. * m) + isq::time(1. * us) / isq::time(1 * h);
quantity q2 = isq::height(1. * m) / isq::length(10. * m) + isq::time(1. * us) / isq::time(1 * h);
```

Both produce `dimensionless` (root of hierarchy). Converting `q2` and `q3` to specific dimension-one quantities works for general forms but requires explicit conversion for specific combinations:

```cpp
quantity<(isq::length / isq::length)[m / m]> ok1 = q1;     // OK (same quantity)
quantity<(isq::length / isq::length)[m / m]> ok2 = q2;     // OK (same quantity)
quantity<(isq::height / isq::length)[m / m]> bad1 = q1;    // Error (not every dimensionless is height/length)
quantity<(isq::height / isq::length)[m / m]> bad2 = q2;    // Error (not every dimensionless is height/length)
```

#### 19.8.6 Structural types

The `quantity` and `quantity_point` class templates are structural types to allow them to be passed as template arguments. For example, we can write the following:

```cpp
constexpr struct amsterdam_sea_level : absolute_point_origin<isq::altitude> {
} amsterdam_sea_level;

constexpr struct mediterranean_sea_level : relative_point_origin<amsterdam_sea_level + isq::altitude(-27 * cm)> {
} mediterranean_sea_level;

using altitude_DE = quantity_point<isq::altitude[m], amsterdam_sea_level>;
using altitude_CH = quantity_point<isq::altitude[m], mediterranean_sea_level>;
```

Unfortunately, current language rules require that all member data of a structural type are public. This could be considered a safety issue. We try really hard to provide unit-safe interfaces, but at the same time expose the public “naked” data member that can be freely read or manipulated by anyone.

Hopefully, this requirement on structural types will be relaxed before the library gets standardized.

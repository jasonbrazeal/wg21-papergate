## 21 Teachability

Through the last years [[mp-units]](https://mpusz.github.io/mp-units) library proved to be very intuitive to both novices in the domain and non-C++ experts. Thanks to the user-friendly multiply syntax, support for CTAD, excellent readability of generated types in compiler error messages, and simplicity of systems definitions, this library makes it easy to do the first steps in the dimensional analysis domain.

### 21.1 Target audiences

Following the practice suggested in [[P1700R0]](https://wg21.link/p1700r0), we identify four distinct user populations for this library, each with different needs and interactions:

| Audience | Population | Roles and skills |
| --- | --- | --- |
| **Application Developers** | millions | Write application code using pre-defined quantities, units, and systems. Perform arithmetic with automatic dimensional analysis and compile-time unit safety. Use `quantity` for deltas and `quantity_point` for points and measurements (temperature, GPS, timestamps). Write generic interfaces constrained with `QuantityOf`. Interoperate with `std::chrono`. Modernise existing codebases by replacing raw numeric types with strongly-typed quantities. |
| **Unit Authors** | tens of thousands | Add named or scaled units to existing quantity types — standard-system extensions (imperial, binary prefixes) and derived combinations. Work entirely within the provided ISQ hierarchy; no new dimensions or quantity specifications required. |
| **Domain Modelers** | thousands | Properly model a new domain: define quantity systems (ISQ-like hierarchies), dimensions, quantity specifications, quantity kind hierarchies, and units. Design domain frameworks (physics engines, geodesy libraries, robotics toolkits) with correct ISQ-style structure. Require domain knowledge and familiarity with the quantity type system; deep C++ metaprogramming is not needed. |
| **Deep Integrators** | hundreds | Bridge custom or legacy types into the quantity system via `quantity_like_traits`. Implement custom representation types with specialised scaling behaviour. Require template metaprogramming expertise and understanding of library internals; domain-specific quantity modelling is not needed. |

This clear separation ensures that the vast majority of users (Application Developers) can be productive immediately with minimal learning, while still providing extensibility for expert users.

#### 21.1.1 Feature mapping by audience

The following table maps library features to their primary target audiences:

| Feature | Application Developers | Unit Authors | Domain Modelers | Deep Integrators |
| --- | --- | --- | --- | --- |
| Multiply syntax (`42 * m`) | ✓ | ✓ | ✓ | ✓ |
| CTAD for quantities | ✓ | ✓ | ✓ | ✓ |
| Arithmetic operations (`+`, `-`, `*`, `/`) | ✓ | ✓ | ✓ | ✓ |
| Unit conversions (`.in(unit)`) | ✓ | ✓ | ✓ | ✓ |
| Comparison operators | ✓ | ✓ | ✓ | ✓ |
| Standard unit symbols (`si::metre`, `usc::foot`) | ✓ | ✓ | ✓ | ✓ |
| Text formatting with `std::format` | ✓ | ✓ | ✓ | ✓ |
| Extracting numerical values (`.numerical_value_in()`) | ✓ | ✓ | ✓ | ✓ |
| `std::chrono` interop | ✓ | ✓ | ✓ | ✓ |
| `quantity` vs `quantity_point` (basic usage) | ✓ | ✓ | ✓ | ✓ |
| Generic interfaces (`QuantityOf<isq::length>`) | ✓ | ✓ | ✓ | ✓ |
| Defining custom units (`named_unit`) |  | ✓ | ✓ | ✓ |
| Unit prefixes (SI and binary) |  | ✓ | ✓ | ✓ |
| Scaled units (`mag<N> * unit`, `mag_constant`) |  | ✓ | ✓ | ✓ |
| Systems of quantities (ISQ-like hierarchies) |  |  | ✓ |  |
| Defining quantity types (`quantity_spec`) |  |  | ✓ |  |
| Custom dimensions (`derived_dimension`) |  |  | ✓ |  |
| Quantity kind hierarchies (`is_kind`) |  |  | ✓ |  |
| Custom point origins |  |  | ✓ |  |
| Representation type constraints (`RepresentationOf`) |  |  | ✓ | ✓ |
| Symbolic expression templates |  |  |  | ✓ |
| Magnitude framework (`mag_power`) |  |  |  | ✓ |
| Custom `quantity_like_traits` |  |  |  | ✓ |
| Custom representation types |  |  |  | ✓ |

Application Developers need only the first eleven rows — the core usage features. Unit Authors additionally define named and scaled units within the existing ISQ hierarchy. Domain Modelers and Deep Integrators are largely disjoint audiences: Domain Modelers bring domain expertise to define quantity systems, dimensions, and specifications, while Deep Integrators bring C++ metaprogramming expertise to extend the library’s type machinery. Both groups build on Unit Author skills, but neither needs the other’s specialisation.

### 21.2 Prerequisites and target audience

Students should have basic familiarity with:

- C++ fundamentals (variables, functions, basic templates)
- Basic physics concepts (*distance*, *time*, *speed*) for motivation

The library is suitable for:

- **Introductory programming courses** - teaches type safety early with intuitive physical examples
- **Scientific computing courses** - provides practical dimensional analysis tools
- **Software engineering courses** - demonstrates modern C++ library design and compile-time safety
- **Physics/engineering courses** - replaces error-prone raw numeric computations

No prior knowledge of template metaprogramming or dimensional analysis is required for basic usage.

### 21.3 Motivation through real-world disasters

Starting with compelling examples helps students understand *why* strong typing matters:

- [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) - Lost in 1999 because thruster software produced pound-force-seconds while the navigation system expected newton-seconds ($125M loss)
- [[Gimli Glider]](https://en.wikipedia.org/wiki/Gimli_Glider) - Air Canada Flight 143 ran out of fuel mid-flight in 1983 after the load was calculated in pounds instead of kilograms
- [[Columbus]](https://en.wikipedia.org/wiki/Christopher_Columbus) - Mixed up the Arabic mile and the Roman mile while preparing his voyage, badly underestimating the size of the equator and his expected travel distance
- [[Ariane flight V88]](https://en.wikipedia.org/wiki/Ariane_flight_V88) - Ariane 5 rocket destroyed in 1996 by an overflow when converting a 64-bit floating-point value to a 16-bit signed integer ($370M loss)

See Safety concerns for more examples and a deeper discussion of why these errors happen.

These examples demonstrate that unit and conversion errors are costly, hard to spot in code review, and can slip through testing. A quick demonstration of untyped vs. typed code makes the value proposition clear:

```cpp
// Unsafe - compiles but crashes spacecraft
double orbital_velocity(double radius, double period)
{
  return 2 * 3.14159 * radius / period;
}
auto v = orbital_velocity(400000, 5400);  // What units? Which one is length? Compiler can't tell!

// Safe - units enforced at compile time
quantity<si::metre / si::second> orbital_velocity(quantity<si::metre> radius, quantity<si::second> period)
{
  return 2 * pi * radius / period;
}
quantity v = orbital_velocity(400 * km, 90 * min);  // OK: 279 m/s
```

### 21.4 Learning path for beginners

#### 21.4.1 Step 1: Basic quantities

If someone is new to the domain, a concise introduction of Systems of units, the [[SI]](https://www.bipm.org/en/publications/si-brochure), and the US Customary System (and how it relates to SI) might be needed.

After that, every new user, even a C++ newbie, should have no problems with understanding the topics of the Quantity construction chapter and should be able to start using the library successfully. At least as long as they keep operating in the safety zone using floating-point representation types.

Start with the multiply syntax for creating quantities:

```cpp
import std;

int main()
{
  using namespace std::si::unit_symbols;

  quantity distance = 100.0 * m;
  quantity time = 9.58 * s;
  quantity speed = distance / time;

  std::println("Usain Bolt's speed: {::N[.2f]}", speed);  // 10.44 m/s
}
```

Key teaching points:

- Natural syntax: `100.0 * m` reads like physics notation
- Automatic unit propagation: `m / s` derived from division
- Type safety: Cannot accidentally add `distance + time`
- CTAD eliminates verbose type spelling

#### 21.4.2 Step 2: Unit conversions and safety

Eventually, the library will stand in the way, disallowing “unsafe” conversions. This would be a perfect place to mention the importance of providing safe interfaces at compile-time and describe why narrowing conversions are unwelcome and what the side effects of those might be. After that, forced conversions in the library should be presented.

Demonstrate safe conversions:

```cpp
quantity<m> race_distance = 100. * m;
quantity<km> trip_distance = race_distance.in(km);  // Safe: 0.1 km

quantity<m, int> d1 = 5 * m;          // OK
quantity<m, int> d2 = 5.5 * m;        // Error: narrowing conversion
quantity<m, int> d3 = (5.5 * m).force_in<int>();  // Explicit truncation

quantity<km, int> d4 = 1500 * m;      // Error: truncation in conversion
quantity<km, int> d5 = (1500 * m).force_in(km);   // Explicit: d5 == 1 km
```

This naturally introduces:

- The `.in(unit)` member function for safe conversions
- Why the library prevents narrowing (data loss, bugs)
- Explicit `.force_in()` for intentional lossy conversions
- Difference between representation narrowing and unit conversion narrowing

#### 21.4.3 Step 3: Interacting with legacy code

In case a target audience needs to interact with legacy interfaces that take raw numeric values, Safe quantity numerical value getters chapter should be introduced. In such a case, it is important to warn students of why this operation is unsafe and what are the potential maintainability issues.

```cpp
// Legacy API
void legacy_api(double distance_in_meters);

// Modern code
quantity dist = 5 * km;
legacy_api(dist.numerical_value_in(m));  // Explicit: I know this is in meters
```

Emphasize the dangers: the compiler cannot verify that `distance_in_meters` actually expects meters rather than feet or kilometers. You must manually ensure the unit in `.numerical_value_in()` matches the legacy API’s expectations, which may be undocumented or ambiguous.

#### 21.4.4 Step 4: Custom units and extensions

Next, we could show how easy extending the library with custom units is. A simple and funny example like the below could be a great exercise here:

```cpp
import std;

inline constexpr struct smoot : std::named_unit<"smoot", std::mag<67> * std::usc::inch> {} smoot;

int main()
{
  constexpr std::quantity dist = 364.4 * smoot;
  std::println("Harvard Bridge length = {::N[.5]} ({::N[.5]}, {::N[.5]}) ± 1 εar",
               dist, dist.in(std::usc::foot), dist.in(std::si::metre));
}
```

This demonstrates that the library is extensible and students can define domain-specific units (e.g., furlongs per fortnight for astronomy, pixels for graphics).

#### 21.4.5 Step 5: Temperature and affine spaces

After a while, we can also introduce students to The affine space abstractions and discuss the Temperature support.

This introduces the distinction between differences (`quantity`) and absolute points (`quantity_point`), using temperature as the most intuitive example:

```cpp
quantity temp_diff = 20 * delta<deg_C>;     // Temperature difference
quantity_point temp = 20 * point<deg_C>;    // Absolute temperature

quantity diff = temp - point<deg_C>(0);     // OK: difference between points
// auto sum = temp + point<deg_C>(10);      // Error: can't add points
```

With the above, we have learned enough for most users’ needs and do not need to delve into more details. The library is intuitive and will prevent all errors at compile time.

### 21.5 Advanced topics

For more advanced classes, groups, or use cases, we can introduce Generic Interfaces and Systems of quantities but we don’t have to describe every detail and corner cases of quantity types design and their convertibility. It is good to start here with Why do we need typed quantities?, followed by Quantities of the same kind and System of quantities is not only about kinds.

#### 21.5.1 Type system and quantity hierarchies

According to our experience, the most common pitfall in using quantity types might be related to the names chosen for them by the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) (e.g., *length*). It might be good to describe what *length* means when we say “every *height* is a *length*” and what it means when we describe a box of *length*, *width*, and *height* dimensions. In the latter case, *length* will not restrict us to the horizontal dimension only. This is how the ISQ is defined, and we should accept this. However, we should present a way to define *horizontal length* as presented in the Comparing, adding, and subtracting quantities of the same kind and describe its rationale.

Advanced students can explore:

- Generic programming with quantity concepts (`QuantityOf<isq::length>`)
- Defining custom quantity types (e.g., `horizontal_length`, `gravitational_potential_energy`)
- Interoperability with `std::chrono::duration` and other libraries
- Vector and tensor quantities for mechanics and graphics

### 21.6 Compiler diagnostics and debugging

One of the library’s strongest teaching features is compiler error quality. When students make mistakes, they get readable messages:

```cpp
quantity d = 100 * m;
quantity t = 50 * s;
quantity wrong = d + t;  // Error
```

Type names in errors remain close to the source code: `quantity<si::metre, double>` rather than pages of template instantiation noise.

Debugging is similarly friendly: quantity objects display naturally in debuggers showing both value and unit. Print formatting with `std::print` produces human-readable output without custom formatters.

### 21.7 Exercises and assessment

Suggested exercises for different skill levels:

**Beginner:**

1. Convert recipe measurements between metric and imperial units
2. Calculate *speed* from *distance* and *time* (e.g., average speed for a road trip)
3. Compute area and volume (rectangle, box) with mixed units

**Intermediate:**

1. Implement projectile motion calculator (initial *velocity*, *angle*, *range*, max *height*)
2. Energy and power calculations (*kinetic energy*, *potential energy*, *power consumption* over *time*)
3. *Pressure*, *volume*, and *temperature* conversions (ideal gas law scenarios)

**Advanced:**

1. Implement generic numeric algorithms (linear interpolation, integration) that work with quantities
2. Design a domain-specific unit system (e.g., astronomical units, parsecs, light-years)
3. Integrate existing strongly-typed wrappers with the library using `quantity_like_traits`

### 21.8 Common mistakes and misconceptions

Based on teaching experience with [[mp-units]](https://mpusz.github.io/mp-units):

1. **Using integer representation types**: Leads to narrowing and overflow errors
   - Example: `quantity d = 1500 * m; quantity km_val = d.in(km);` fails (truncation)
   - Example: `quantity<nm, int> small = 5 * m;` fails (overflow on scaling factor)
   - Solution: Use floating-point for most cases, explicit `.force_in()` when integer truncation is intentional
2. **Operator precedence with unit literals**: Forgetting parentheses in expressions
   - Example: `quantity frequency = 1. / 2 * s;` gives `0.5 s`, not `0.5 Hz`
   - Correct: `quantity frequency = 1. / (2 * s);` or `quantity period = 2. * s; auto frequency = 1 / period;`
   - Solution: Use parentheses or intermediate variables for clarity
3. **Confusing `quantity` and `quantity_point`**: Attempting invalid affine space operations
   - Example: `auto result = 20 * deg_C + 30 * deg_C;` - multiply syntax disabled for offset units
   - Solution: Understand difference between intervals (quantities) and points (quantity_points)
4. **Forgetting namespace qualification**: Writing `42 * m` without importing unit symbols
   - Solution: Add `using namespace std::si::unit_symbols;` or use qualified names
5. **Overusing `.numerical_value_in()`**: Extracting raw values unnecessarily
   - Problem: Defeats type safety, makes refactoring harder
   - Solution: Keep quantities typed as long as possible, extract only at boundaries

### 21.9 Integration with curricula

This library fits naturally into existing courses:

**CS1/CS2 (Introductory Programming):**

- Introduce alongside basic types as motivation for type safety
- Use in physics-based programming exercises (projectile motion, etc.)
- Teaches good habits early: explicit units, compile-time verification

**Numerical Methods / Scientific Computing:**

- Replace raw `double` arrays with typed quantities
- Demonstrate that abstraction doesn’t hurt performance
- Real-world applications: simulation, data analysis

**Software Engineering:**

- Case study in modern C++ library design
- Example of zero-overhead abstractions
- Unit testing with dimensional analysis

**Physics / Engineering Computation:**

- Drop-in replacement for manual unit tracking
- Focus on problems, not bookkeeping
- Prevents entire categories of bugs

### 21.10 Teaching impact beyond C++

While the previous sections focus on teaching the library itself, this feature has broader pedagogical value: it transforms C++ into a teaching tool for units and quantities in general. A standardized quantities and units library extends C++’s educational reach beyond traditional computer science into physics, engineering, and even primary education.

#### 21.10.1 Enabling interdisciplinary education

The library provides non-CS educators with a robust computational tool for teaching their subject matter. Physics teachers can build hands-on computational exercises where students implement real physics equations (projectile motion, circuit analysis, thermodynamics) with compile-time verification that their dimensional analysis is correct. Engineering instructors can create laboratory exercises where sensor data is processed with proper unit handling from the start, mirroring professional practice. Chemistry educators can teach stoichiometry and gas laws with students writing code that enforces correct unit conversions between moles, grams, liters, and atmospheres.

This creates opportunities for integrated learning where domain knowledge and computational thinking develop together. A student learning physics doesn’t just memorize formulas—they implement them, and the compiler verifies their understanding of dimensional relationships. When a student writes `force = mass * acceleration` and the library confirms the result has units of force, they’ve demonstrated conceptual understanding in a way that traditional problem sets cannot assess.

#### 21.10.2 Supporting faculty with limited programming experience

Many science and engineering faculty have computational needs but limited software engineering expertise. The library’s intuitive multiply syntax (`distance = 50 * km`) requires minimal C++ knowledge while providing significant safety benefits. Faculty can create course materials using straightforward code that reads like mathematical notation, lowering the barrier to incorporating computation into their curriculum. The library’s compile-time error messages serve double duty: they catch programming mistakes *and* reveal dimensional analysis errors that indicate conceptual misunderstandings.

This is particularly valuable for disciplines where programming is auxiliary to the primary subject. An engineering professor teaching fluid mechanics doesn’t need to become a C++ expert—basic quantities and units operations are accessible with minimal training while still providing the benefits of type safety and dimensional analysis.

#### 21.10.3 Enriching K-12 and informal education

Computing education increasingly begins in primary and secondary schools. Robotics programs, often built around platforms like LEGO Mindstorms or Arduino, provide rich opportunities to introduce quantities and units naturally. A middle school robotics team programming their robot to navigate a course benefits from using `speed = 30 * cm / s` instead of raw numbers. The explicit units make the code self-documenting for young programmers still building intuition about physical quantities.

When students can write `if (distance < 50 * cm) { stop(); }` the connection between their physical robot and their code becomes clearer. The compiler preventing them from comparing distance to time reinforces dimensional understanding at an age when these concepts are still forming. This creates a richer learning environment where programming and physical intuition develop in parallel.

Similarly, informal education settings—science museums, summer camps, maker spaces—can leverage the library in interactive exhibits and workshops. The combination of physical computing (sensors, actuators) with properly-typed quantities provides immediate, tangible feedback about both programming and physics concepts.

#### 21.10.4 Preparing students for professional practice

Standardization ensures students learn an industry-relevant skill. Unlike toy educational languages or frameworks that must be unlearned later, proper units handling in C++ directly transfers to professional software development. Students who learn to write `quantity area = width * height;` where `width` and `height` are quantities develop habits that prevent real-world errors in safety-critical systems.

This is particularly important for students entering industries where C++ dominates: aerospace, automotive, embedded systems, robotics, quantitative finance, and game development. A graduate who has used quantities and units throughout their coursework arrives at their first job already familiar with dimensional analysis in code, ready to contribute safely to production systems.

The standardization aspect is crucial here—without it, each company uses incompatible internal libraries or ad-hoc approaches, forcing new graduates to relearn concepts they should already know. A standard library provides a stable foundation that educational institutions can confidently build curricula around, knowing their graduates will use these same tools professionally.


## 22 Acknowledgements

Special thanks and recognition goes to [The C++ Alliance](https://cppalliance.org) for supporting Mateusz’s membership in the ISO C++ Committee and the production of this proposal.

We would also like to thank:

- Peter Sommerlad for providing valuable feedback that helped us shape the final version of this document,
- Michael Hordijk for discovering typos and improving the flow of some confusing passages,
- Florian Tatzel and J.C. van Winkel (SG20 chairs) for the insightful suggestion to highlight the library’s broader impact on teaching units and quantities beyond C++ education and a need to assign the skills required for different target audiences.

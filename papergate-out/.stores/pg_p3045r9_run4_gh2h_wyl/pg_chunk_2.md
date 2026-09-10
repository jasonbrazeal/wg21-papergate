## 7 Motivation

This chapter describes why we believe that physical quantities and units should be part of a C++ Standard Library.

### 7.1 Safety concerns

It is no longer only the space industry or experienced pilots that benefit from the autonomous operations of some machines. We live in a world where more and more ordinary people trust machines with their lives daily. In the near future, we will be allowed to sleep while our car autonomously drives us home from a late party. As a result, many more C++ engineers are expected to write life-critical software today than it was a few years ago. However, writing safety-critical code requires extensive training and experience, both of which are in short demand. While there exists some standards and guidelines such as MISRA C++ [[MISRA C++]](https://misra.org.uk/misra-c-plus-plus/) with the aim of enforcing the creation of safe code in C++, they are cumbersome to use and tend to shift the burden on the discipline of the programmers to enforce these. At the time of writing, the C++ language does not change fast enough to enforce safe-by-construction code.

One of the ways C++ can significantly improve the safety of applications being written by thousands of developers is by introducing a type-safe, well-tested, standardized way to handle physical quantities and their units. The rationale is that people tend to have problems communicating or using proper units in code and daily life. Numerous expensive failures and accidents happened due to using an invalid unit or a quantity type.

The most famous and probably the most expensive example in the software engineering domain is the Mars Climate Orbiter that in 1999 failed to enter Mars’ orbit and crashed while entering its atmosphere [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter). This is one of many examples here. People tend to confuse units quite often. We see similar errors occurring in various domains over the years:

- On October 12, 1492, Christopher Columbus unintentionally discovered the sea route from Europe to America because, during his travel preparations, he mixed the Arabic mile with a Roman mile, which led to the wrong estimation of the equator and his expected travel distance [[Columbus]](https://en.wikipedia.org/wiki/Christopher_Columbus).
- In 1628, a new warship, Vasa, accidentally had an asymmetrical hull (being thicker on the port side than the starboard side), which was one of the reasons for her sinking less than a mile into her maiden voyage, resulting in the death of 30 people on board. This asymmetry could have been caused by the use of different systems of measurement, as archaeologists have found four rulers used by the workers who built the ship. Two were calibrated in Swedish feet, which had 12 inches, while the other two measured Amsterdam feet, which had 11 inches [[Vasa]](https://theworld.org/stories/2012-02-23/new-clues-emerge-centuries-old-swedish-shipwreck).
- Air Canada Flight 143 ran out of fuel on July 23, 1983, at an altitude of 41 000 feet (12 000 metres), midway through the flight because the fuel had been calculated in pounds instead of kilograms by the ground crew [[Gimli Glider]](https://en.wikipedia.org/wiki/Gimli_Glider).
- The British rock band Black Sabbath, during its Born Again tour in 1983, ordered a replica of Stonehenge as props for the scene. Unfortunately, they had to leave them in the storage area because, while submitting the order, their manager wrote dimensions down in meters when he meant feet, and so the stones didn’t fit the scene. “It cost a fortune to make, but there was not a building on Earth that you could fit it into” [[Stonehenge]](https://www.telegraph.co.uk/films/2020/05/01/tiny-stones-giant-laughs-story-behind-spinal-taps-stonehenge).
- On April 15, 1999, Korean Air Cargo Flight 6316 crashed due to a miscommunication between pilots about the desired flight altitude [[Flight 6316]](https://web.archive.org/web/20210917190721/https://www.ntsb.gov/news/press-releases/Pages/Korean_Air_Flight_6316_MD-11_Shanghai_China_-_April_15_1999.aspx).
- In February 2001, the crew of the Moorpark College Zoo built an enclosure for Clarence the Tortoise with a weight of 250 pounds instead of 250 kilograms [[Clarence]](https://www.latimes.com/archives/la-xpm-2001-feb-09-me-23253-story.html).
- In December 2003, one of the roller coaster’s cars at Tokyo Disneyland’s Space Mountain attraction suddenly derailed due to a broken axle caused by confusion after upgrading the specification from imperial to metric units [[Disney]](https://web.archive.org/web/20040209033827/http://www.olc.co.jp/news/20040121_01en.html).
- During the construction of the Hochrheinbrücke bridge to connect the small German town of Laufenburg with Swiss Laufenburg, the construction team made a sign error that resulted in a discrepancy of 54 cm between the two outer ends of the bridge [[Hochrheinbrücke]](https://www.normaalamsterdamspeil.nl/wp-content/uploads/2015/03/website_bridge.pdf).
- An American company sold a shipment of wild rice to a Japanese customer, quoting a price of 39 cents per pound, but the customer thought the quote was for 39 cents per kilogram [[Wild Rice]](https://www.bizjournals.com/eastbay/stories/2001/07/09/focus3.html).
- On October 17, 2023, The Guardian published an article titled “Record Heat: Malawi swelters with temperatures nearly 68F above average” with many issues related to the affine space types and temperature units. Due to incorrect logic, probably during the translation of the article to the U.S. market, `20 °C` above the average temperature was converted to `68 °F`. The actual temperature increase was `32 °F`, not `68 °F` [[The Guardian]](https://randomascii.wordpress.com/2023/10/17/localization-failure-temperature-is-hard).
- A whole set of [[Medication dose errors]](https://onlinelibrary.wiley.com/doi/10.1111/jan.15072)…

The safety subject is so vast and essential by itself that we dedicated an entire [Safety features] chapter of this paper that discusses all the nuances in detail.

### 7.2 Vocabulary types

We standardized many library features mostly used in the implementation details (fmt, ranges, random-number generators, etc.). However, we believe that the most important role of the C++ Standard is to provide a standardized way of communication between different vendors.

Let’s imagine a world without `std::string` or `std::vector`. Every vendor has their version of it, and of course, they are highly incompatible with each other. As a result, when someone needs to integrate software from different vendors, it turns out to be an unnecessarily arduous task.

Introducing `std::chrono::duration` and `std::chrono::time_point` improved the interfaces a lot, but time is only one of many quantities that we deal with in our software on a daily basis. We desperately need to be able to express more quantities and units in a standardized way so different libraries get means to communicate with each other.

If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds, and the [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) would not have crashed during the Mars orbital insertion maneuver.

### 7.3 Certification

Mission and life-critical projects, or those for embedded devices, often have to obey the safety norms that care about software for safety-critical systems (e.g., ISO 61508 is a basic functional safety standard applicable to all industries, and ISO 26262 for automotive). As a result, their company policy often forbid third-party tooling that lacks official certification. Such certification requires a specification to be certified against, and those tools often do not have one. The risk and cost of self-certifying an Open Source project is too high for many as well.

Companies often have a policy that the software they use must obey all the rules MISRA provides. This is a common misconception, as many of those rules are intended to be deviated from. However, those deviations require rationale and documentation, which is also considered to be risky and expensive by many.

All of those reasons often prevent the usage of an Open Source product in a company, which is a huge issue, as those companies typically are natural users of physical quantities and units libraries.

Having the physical quantities and units library standardized would solve those issues for many customers, and would allow them to produce safer code for projects on which human life depends every single day.

### 7.4 Complex and complicated

Suppose vendors can’t use an Open Source library in a production project for the above reasons. They are forced to write their own abstractions by themselves. Besides being costly and time-consuming, it also happens that writing a physical quantities and units library by yourself is far from easy. Doing this is complex and complicated, especially for engineers who are not experts in the domain. There are many exceptional corner cases to cover that most developers do not even realize before falling into a trap in production. On the other hand, domain experts might find it difficult to put their knowledge into code and create a correct implementation in C++. As a result, companies either use really simple and unsafe numeric wrappers, or abandon the effort entirely and just use built-in types, such as `float` or `int`, to express quantity values, thus losing all semantic categorization. This often leads to safety issues caused by accidentally using values representing the wrong quantity or having an incorrect unit.

### 7.5 Extensibility

Many applications of a quantity and units library may need to operate on a combination of standard (e.g., SI) and domain-specific quantities and units. The complexity of developing domain-specific solutions highlights the value in being able to define new quantities and units that have all the expressivity and safety as those provided by the library.

Experience with writing ad hoc typed quantities without library support that can be combined with or converted to `std::chrono::duration` has shown the downside of bespoke solutions: If not all operations or conversions are handled, users will need to leave the safety of typed quantities to operate on primitive types.

The interfaces of the this library were designed with ease of extensibility in mind. Each definition of a dimension, quantity type, or unit typically takes only a single line of code. This is possible thanks to the extensive usage of C++20 class types as Non-Type Template Parameters (NTTP). For example, the following code presents how second (a unit of time in the [[SI]](https://www.bipm.org/en/publications/si-brochure)) and hertz (a unit of frequency in the [[SI]](https://www.bipm.org/en/publications/si-brochure)) can be defined:

```cpp
inline constexpr struct second : named_unit<"s", kind_of<isq::time>> {} second;
inline constexpr struct hertz : named_unit<"Hz", 1 / second, kind_of<isq::frequency>> {} hertz;
```

### 7.6 Broad industry value

When people think about industries that could use physical quantities and unit libraries, they think of a few companies related to aerospace, autonomous cars, or embedded industries. That is all true, but there are many other potential users for such a library.

Here is a list of some less obvious candidates:

- Manufacturing and production systems,
- energy sector (power generation, electrical grids, renewable energy),
- maritime industry,
- freight transport and logistics,
- chemical and process engineering,
- oil and gas (drilling, pipelines, refineries),
- HVAC and environmental control,
- telecommunications and signal processing,
- military,
- astronomy,
- civil engineering and construction,
- 3D design and CAD,
- robotics,
- audio and music production,
- medical devices and pharmaceutical dosing,
- gaming and physics simulation,
- national laboratories,
- scientific institutions and universities,
- all kinds of navigation and charting,
- GUI frameworks and computer graphics,
- finance (including HFT).

As we can see, the range of domains for such a library is vast and not limited to applications involving specifically physical units. Any software that involves measurements, or operations on counts of some standard or domain-specific quantities, could benefit from a zero-cost abstraction for operating on quantity values and their units. The library also provides affine space abstractions, which may prove useful in many applications.

### 7.7 Standardizing existing practice

Plenty of physical units libraries have been available to the public for many years. In 1998 Walter Brown provided an “Introduction to the SI Library of Unit-Based Computation” paper for the International Conference on Computing in High Energy Physics [[CHEP’98]](https://digital.library.unt.edu/ark:/67531/metadc668099). It emphasizes the importance of strong types and static type-checking. After that, it describes a library modeling the [[SI]](https://www.bipm.org/en/publications/si-brochure) to provide “strict compile-time type-checking without run-time overhead”.

It also states that at this time, “in numeric programming, programmers make heavy, near-exclusive, use of a language’s native numeric types (e.g., `double`)”. Today, twenty-five years later, plenty of “Modern C++” production code bases still use `double` to represent various quantities and units. It is high time to change this.

Throughout the years, we have learned the best practices for handling specific cases in the domain. Various products may have different scopes and support different C++ versions. Still, taking that aside, they use really similar concepts, types, and operations under the hood. We know how to do those things already.

The authors of this paper developed and delivered multiple successful C++ libraries for this domain. Libraries developed by them [have more than 90% of all the stars on GitHub in the field of physical units libraries for C++](https://github.com/topics/dimensional-analysis?l=c%2B%2B). The [[mp-units]](https://mpusz.github.io/mp-units) library, which is the base of this proposal, has the most number of stars in this list, making it the most popular project in the C++ industry.

The authors joined forces and are working together to propose the best quantities and units library we can get with the latest version of the C++ language. They spend their private time and efforts hoping that the ISO C++ Committee will be willing to include such a feature in the C++ standard library.

### 7.8 WG21 wants it

In Belfast 2019 the following polls were taken for [[P1935R0]](https://wg21.link/p1935r0) in LEWG:

**POLL:** *We should promise more committee time to pursuing adding common units (such as SI, customary, etc) to the standard library, knowing that our time is scarce and this will leave less time for other work.*

| SF | WF | N | WA | SA |
| --- | --- | --- | --- | --- |
| 11 | 7 | 4 | 2 | 0 |

**POLL:** *We should promise more committee time to pursuing a standard library framework for user defined units and unit systems, knowing that our time is scarce and this will leave less time for other work.*

| SF | WF | N | WA | SA |
| --- | --- | --- | --- | --- |
| 10 | 8 | 4 | 1 | 1 |

As a result of the above polls, Mateusz approached authors of all other popular actively maintained libraries. We formed a working group of experts and worked on a common unified proposal for a few years. This paper and the current implementation of the [[mp-units]](https://mpusz.github.io/mp-units) library is the result of those actions.

In Croydon 2026, this paper was reviewed by both SG18 (LEWG Incubator) and LEWG. LEWG took the following polls:

**POLL:** *We acknowledge the complexity inherent to the domain of quantities and units and think this is a problem worth solving thoroughly in the standard library, following the direction presented in P3045R7.*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 22 | 13 | 1 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We support the direction presented as a technical solution (instantiating quantities with units, creating the hierarchy of kinds).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 16 | 22 | 0 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value in covering use cases in fine granularity (different quantities of the same kind, such as width and height, or difference between kinetic and potential energy).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 22 | 12 | 3 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value of standardizing these parts of the framework: Core library (quantity, symbolic expressions, dimensions, units, references and concepts), Quantity kinds (support quantities of the same dimension), Quantities of the same kind (width, height, etc.).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 27 | 9 | 0 | 0 | 0 |

**Outcome: Strong consensus in favour**

**POLL:** *We see the value of standardizing Affine space (quantity_point, point origin, and concepts for them).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 24 | 8 | 1 | 0 | 0 |

**Outcome: Strong consensus in favor**

**POLL:** *We see the value of standardizing Text output (for quantity, units, and dimensions).*

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 15 | 14 | 5 | 0 | 0 |

**Outcome: Strong consensus in favour**

These results demonstrate strong committee support for the comprehensive approach to quantities and units presented in this paper, including the more advanced features like affine space abstractions and fine-grained quantity specifications.


## 8 Common smells when there is no library for quantities and units

In this chapter, we are going to review typical safety issues related to physical quantities and units in the C++ code when a proper library is not used. Even though all the examples come from the Open Source projects, expensive revenue-generating production source code often is similar.

### 8.1 The proliferation of `double`

It turns out that in the C++ software, most of our calculations in the physical quantities and units domain are handled with fundamental types like `double`. Code like below is a typical example here:

```cpp
double GlidePolar::MacCreadyAltitude(double MCREADY,
                                     double Distance,
                                     const double Bearing,
                                     const double WindSpeed,
                                     const double WindBearing,
                                     double *BestCruiseTrack,
                                     double *VMacCready,
                                     const bool isFinalGlide,
                                     double *TimeToGo,
                                     const double AltitudeAboveTarget=1.0e6,
                                     const double cruise_efficiency=1.0,
                                     const double TaskAltDiff=-1.0e6);
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Header/McReady.h#L7-L21).

There are several problems with such an approach: The abundance of `double` parameters makes it easy to accidentally switch values and there is no way of noticing such a mistake at compile-time. The code is not self-documenting in what units the parameters are expected. Is `Distance` in meters or kilometers? Is `WindSpeed` in meters per second or knots? Different code bases choose different ways to encode this information, which may be internally inconsistent. A strong type system would help answer these questions at the time the interface is written, and the compiler would verify it at compile-time.

### 8.2 The proliferation of magic numbers

There are a lot of constants and conversion factors involved in the quantity equations. Source code responsible for such computations is often trashed with magic numbers:

```cpp
double AirDensity(double hr, double temp, double abs_press)
{
  return (1/(287.06*(temp+273.15)))*(abs_press - 230.617 * hr * exp((17.5043*temp)/(241.2+temp)));
}
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Source/Library/PressureFunctions.cpp#L134-L136).

Apart from the obvious readability issues, such code is hard to maintain, and it needs a lot of domain knowledge on the developer’s side. While it would be easy to replace these numbers with named constants, the question of which unit the constant is in remains. Is `287.06` in pounds per square inch (psi) or millibars (mbar)?

### 8.3 The proliferation of conversion macros

The lack of automated unit conversions often results in handwritten conversion functions or macros that are spread everywhere among the code base:

```cpp
#ifndef PI
static const double PI = (4*atan(1));
#endif
#define EARTH_DIAMETER    12733426.0    // Diameter of earth in meters
#define SQUARED_EARTH_DIAMETER  162140137697476.0 // Diameter of earth in meters (EARTH_DIAMETER*EARTH_DIAMETER)
#ifndef DEG_TO_RAD
#define DEG_TO_RAD  (PI / 180)
#define RAD_TO_DEG  (180 / PI)
#endif

#define NAUTICALMILESTOMETRES (double)1851.96
#define KNOTSTOMETRESSECONDS (double)0.5144

#define TOKNOTS (double)1.944
#define TOFEETPERMINUTE (double)196.9
#define TOMPH   (double)2.237
#define TOKPH   (double)3.6

// meters to.. conversion
#define TONAUTICALMILES (1.0 / 1852.0)
#define TOMILES         (1.0 / 1609.344)
#define TOKILOMETER     (0.001)
#define TOFEET          (1.0 / 0.3048)
#define TOMETER         (1.0)
```

[Original code here](https://github.com/LK8000/LK8000/blob/052bbc20a106fda4db41874e788e39020fb86512/Common/Header/Defines.h#L901-L924).

Again, the question of which unit the constant is in remains. Without looking at the code, it is impossible to tell from which unit `TOMETER` converts. Also, macros have the problem that they are not scoped to a namespace and thus can easily clash with other macros or functions, especially if they have such common names like `PI` or `RAD_TO_DEG`. A quick search through open source C++ code bases reveals that, for example, the `RAD_TO_DEG` macro is defined in a multitude of different ways – sometimes even within the same repository:

```cpp
#define RAD_TO_DEG (180 / PI)
#define RAD_TO_DEG 57.2957795131
#define RAD_TO_DEG ( radians ) ((radians ) * 180.0 / M_PI)
#define RAD_TO_DEG 57.2957805f
...
```

[Example search across multiple repositories](https://github.com/search?q=lang%3AC%2B%2B++%22%23define+RAD_TO_DEG%22&type=code)

[Multiple redefinitions in the same repository](https://github.com/search?q=repo%3ALK8000%2FLK8000%20rad_to_deg&type=code)

Another safety issue occurring here is the fact that macro values can be deliberately tainted by compiler settings at built time and can acquire values that are not present in the source code. Human reviews won’t catch such issues.

Also, most of the macros do not follow best practices. Often, necessary parentheses are missing, processing in a preprocessor ends up with redundant casts, or some compile-time constants use too many digits for a value to be exact for a specific type (e.g., `float`).

### 8.4 Lack of consistency

If we not only lack strong types to isolate the abstractions from each other, but also lack discipline to keep our code consistent, we end up in an awful place:

```cpp
void DistanceBearing(double lat1, double lon1,
                     double lat2, double lon2,
                     double *Distance, double *Bearing);

double DoubleDistance(double lat1, double lon1,
                      double lat2, double lon2,
                      double lat3, double lon3);

void FindLatitudeLongitude(double Lat, double Lon,
                           double Bearing, double Distance,
                           double *lat_out, double *lon_out);

double CrossTrackError(double lon1, double lat1,
                       double lon2, double lat2,
                       double lon3, double lat3,
                       double *lon4, double *lat4);

double ProjectedDistance(double lon1, double lat1,
                         double lon2, double lat2,
                         double lon3, double lat3,
                         double *xtd, double *crs);
```

[Original code here](https://github.com/LK8000/LK8000/blob/af404168ff5f92b03ab0c5db336ed8f01a792cda/Common/Header/NavFunctions.h#L7C1-L27).

Users can easily make errors if the interface designers are not consistent in ordering parameters. It is really hard to remember which function takes latitude or `Bearing` first and when a latitude or `Distance` is in the front.

### 8.5 Lack of a conceptual framework

The previous points mean that the fundamental types can’t be leveraged to model the different concepts of quantities and units frameworks. There is no shared vocabulary between different libraries. User-facing APIs use ad-hoc conventions. Even internal interfaces are inconsistent between themselves.

Arithmetic types such as `int` and `double` are used to model different concepts. They are used to represent any abstraction (be it a magnitude, difference, point, or kind) of any quantity type of any unit. These are weak types that make up weakly-typed interfaces. The resulting interfaces and implementations built with these types easily allow mixing up parameters and using operations that are not part of the represented quantity.


## 9 Design goals

The library facilities that we plan to propose in the upcoming papers is designed with the following goals in mind.

### 9.1 Compile-time safety

The most important property of any such a library is the safety it brings to C++ projects. The correct handling of physical quantities, units, and numerical values should be verifiable both by the compiler and by humans with manual inspection of each individual line.

In some cases, we are even eager to prioritize safe interfaces over the general usability experience (e.g., getters of the underlying raw numerical value will always require a unit in which the value should be returned in, which results in more typing and is sometimes redundant).

More information on this subject can be found in [Safety features].

### 9.2 Performance

The library should be as fast or even faster than working with fundamental types. There should be no runtime overhead, and no space size overhead should be needed to implement higher-level abstractions. In practice, the [[mp-units]](https://mpusz.github.io/mp-units) implementation compiles to identical or faster assembly as equivalent code using raw `double` arithmetic — this can be verified via the Compiler Explorer links provided in the Usage examples chapter.

### 9.3 Great user experience

The primary purpose of the library is to generate compile-time errors. If users did not introduce any bugs in the manual handling of quantities and units, the library would be of little use. This is why the library is optimized for readable compilation errors and great debugging experience.

The library is easy to use and flexible. The interfaces are straight-forward and safe by default. Users should be able to easily express any quantity and unit, which requires them to compose.

The above constraints imply the usage of special implementation techniques. The library will not only provide types, but also compile-time known values that will enable users to write easy to understand and efficient equations on quantities and units.

### 9.4 Scope

There are plenty of expectations from different parties regarding such a library. It should support at least:

- Any unit’s magnitude (huge, small, floating-point).
- Systems of Quantities.
- Systems of Units.
- The affine space.
- Highly adjustable text-output formatting.

Additionally, it would be good to also support the following features:

- Scalar, vector, and tensor quantities.
- Natural units systems.

### 9.5 Easy to extend

The library’s core framework does not assume the usage of any systems of quantities or units. It is fully generic and allow defining any system abstraction on top of it.

Most entities in the library can be defined with a single line of code without preprocessor macros. Users can easily extend provided systems with custom dimensions, quantities, and units.

### 9.6 Low standardization cost

The set of entities required for standardization should be limited to the bare minimum.

Most of the entities in systems definitions should be possible to implement with a single line of code.

Derived units do not need separate library types. Instead, they can be obtained through the composition of predefined named units. Units should not be associated with User-Defined Literals (UDLs), as it is the case with `std::chrono::duration`. UDLs do not compose, have very limited scope and functionality, and are expensive to standardize.

The user interface should have no preprocessor macros.

It should be possible for most proposed features (besides the text output) to be freestanding.

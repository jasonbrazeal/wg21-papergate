## 13 Hello units

This chapter traces a complete, minimal example from user-facing code down through the library’s layers, showing how each piece fits together. The goal is to build an intuition for the design before reading the detailed specifications that follow.

### 13.1 The example

A *smoot* is a unit of length equal to the height of Oliver Smoot (five feet and seven inches), famously used to measure the Harvard Bridge in 1958. Adding it to the library takes exactly one line:

```cpp
import std;

inline constexpr struct smoot : std::named_unit<"smoot", std::mag<67> * std::usc::inch> {} smoot;

int main()
{
  constexpr std::quantity dist = 364.4 * smoot;
  std::println("Harvard Bridge length = {::N[.1f]} ({::N[.1f]}, {::N[.2f]}) ± 1 εar",
               dist, dist.in(std::usc::foot), dist.in(std::si::metre));
}
```

Output:

```
Harvard Bridge length = 364.4 smoot (2034.6 ft, 620.14 m) ± 1 εar
```

Three things happen here: a unit is defined, a quantity is created, and the quantity is converted. Each layer is examined below.

### 13.2 Layer 1: Units — a chain to a base

Every unit ultimately traces back to a *base unit* — a unit associated directly with a quantity kind rather than being defined relative to another unit. The `named_unit<Symbol, kind_of<QS>>` form is used for these coherent base units:

```cpp
// base unit — anchored to the length quantity kind
struct metre : named_unit<"m", kind_of<isq::length>> {} metre;
```

From there, US customary units are defined as a chain of scaled aliases using the `named_unit<Symbol, Scale>` form, each expressed in terms of the one above:

```cpp
struct yard : named_unit<"yd", mag_ratio<9144, 10000> * si::metre> {} yard;  // 0.9144 m
struct foot : named_unit<"ft", mag_ratio<1, 3>        * yard>      {} foot;  // 1/3 yd
struct inch : named_unit<"in", mag_ratio<1, 12>       * foot>      {} inch;  // 1/12 ft
```

Both forms assign a name and symbol to the unit and automatically propagate the quantity kind down the chain — `inch` is a unit of *length* with no extra annotation.

### 13.3 Layer 2: Magnitudes — exact compile-time rationals

The scaling factors `mag_ratio<N, D>` and `mag<N>` are compile-time rational numbers stored as products of prime powers. No floating-point arithmetic occurs in the type system. When the library traverses the chain from `inch` to `metre`, it multiplies the accumulated factors:

```
1 inch = (1/12) × (1/3) × (9144/10000) m  =  127/5000 m  =  0.0254 m  (exact)
```

The conversion factor from `smoot` to `metre` is therefore:

```
1 smoot = 67 × (127/5000) m  =  8509/5000 m  (exact rational)
```

This ratio is available entirely at compile time and applied to the stored value only at the point of an explicit conversion.

### 13.4 Layer 3: Naming a unit — `named_unit<"smoot", mag<67> * usc::inch>`

The expression `mag<67> * usc::inch` produces a `scaled_unit<mag<67>, inch>`. Wrapping it in `named_unit`:

```cpp
struct smoot : named_unit<"smoot", mag<67> * usc::inch> {} smoot;
```

does three things simultaneously:

1. Records the symbol `"smoot"` for use in text output.
2. Inherits the `_base_type_` of the scaled unit, making `smoot` a unit of *length*.
3. Records the scaling so that `get_canonical_unit(smoot)` can recover the exact magnitude relative to `metre` without any additional bookkeeping.

### 13.5 Layer 4: The `quantity` type

The central type of the library is:

```cpp
template<Reference auto R, RepresentationOf<get_quantity_spec(R)> Rep = double>
class quantity {
public:
  Rep numerical_value_is_an_implementation_detail_;  // the only runtime datum

  static constexpr Reference auto reference        = R;
  static constexpr QuantitySpec auto quantity_spec = get_quantity_spec(R);    // isq::length
  static constexpr Dimension auto dimension        = quantity_spec.dimension; // dim_length
  static constexpr Unit auto unit                  = get_unit(R);             // smoot
  using rep = Rep;
};
```

The unit, quantity specification, and dimension are part of the **type** — they consume no storage and carry zero runtime overhead. Only the numerical value is stored.

A bare unit such as `smoot` also satisfies the `Reference` concept (since the quantity specification can be recovered from it via `get_quantity_spec`), so it can serve directly as the reference template argument.

### 13.6 Layer 5: Creating a quantity — `364.4 * smoot`

The expression `364.4 * smoot` invokes:

```cpp
template<typename FwdRep, Reference R, ...>
  requires(!OffsetUnit<get_unit(R{})>)
constexpr quantity<R{}, Rep> operator*(FwdRep&& lhs, R) { return quantity{std::forward<FwdRep>(lhs), R{}}; }
```

The result is `quantity<smoot{}, double>` — a type that encodes `smoot` and `double` as compile-time template arguments and stores only `364.4` at runtime.

### 13.7 Layer 6: Unit conversion — `dist.in(si::metre)`

`.in(ToU)` checks at compile time that `ToU` is a valid unit for the same quantity specification, then applies the conversion:

```cpp
template<UnitOf<quantity_spec> ToU>
  requires ImplicitScaling<unit, ToU{}, rep>
constexpr QuantityOf<quantity_spec> auto in(ToU) const;
```

Internally, the conversion ratio is computed entirely at compile time:

```cpp
constexpr UnitMagnitude auto c_mag = get_canonical_unit(From::unit).mag / get_canonical_unit(To::unit).mag;
```

The exact rational `8509/5000` is then applied to the stored value at runtime. The fraction is converted to a `long double` constant **at compile time**, so the actual runtime operation for a `double` representation is a single multiplication:

```
364.4 × 1.7018L ≈ 620.14
```

Scaling behaviour for other representation types (integers, fixed-point, custom types) is discussed in How Scaling Works.

The return type is `quantity<si::metre{}, double>` holding `620.14`. Attempting to convert to an incompatible unit — for example `si::second` — is a compile-time error because `si::second` does not satisfy `UnitOf<isq::length>`.

### 13.8 Layer 7: Formatting — `{::N[.1f]}`

The library provides a `std::formatter` specialization for `quantity`. The format-specification grammar (described fully in Text output) gives independent control over the numerical part and the unit symbol. For `dist.in(si::metre)` formatted with `{::N[.2f]}`, the `N[.2f]` sub-spec is forwarded to the `Rep` formatter (producing `"620.14"`), after which the formatter appends the unit symbol `"m"` — yielding `"620.14 m"`.

---

That is the full path from user code to bits: one stored `double`, with the unit, quantity kind, dimension, and conversion factor living entirely in the C++ type system.

This is intentionally a minimal example. Many library features — quantity convertibility, generic interfaces and concepts, the affine space, representation type constraints, mixed-unit arithmetic, value casts, and more — are not used here and therefore not described. They are covered in the chapters that follow.


## 14 Usage examples

This chapter demonstrates key safety features through minimal compile-time examples.

### 14.1 Basic quantity equations

Let’s start with a really simple example presenting basic operations that every physical quantities and units library should provide:

```cpp
import std;

using namespace std::si::unit_symbols;

// simple numeric operations
static_assert(10 * km / 2 == 5 * km);

// conversions to common units
static_assert(1 * h == 3600 * s);
static_assert(1 * km + 1 * m == 1001 * m);

// derived quantities
static_assert(1 * km / (1 * s) == 1000 * m / s);
static_assert(2 * km / h * (2 * h) == 4 * km);
static_assert(2 * km / (2 * km / h) == 1 * h);

static_assert(2 * m * (3 * m) == 6 * m2);

static_assert(10 * km / (5 * km) == 2);

static_assert(1000 / (1 * s) == 1 * kHz);
```

Try it in [the Compiler Explorer](https://godbolt.org/z/xKE7b81Yb).

### 14.2 mp-units showcase

The next example serves as a showcase of various features available in the [[mp-units]](https://mpusz.github.io/mp-units) library.

```cpp
import std;

constexpr std::QuantityOf<std::isq::speed> auto avg_speed(std::QuantityOf<std::isq::length> auto d,
                                                          std::QuantityOf<std::isq::time> auto t)
{
  return d / t;
}

int main()
{
  using namespace std::si::unit_symbols;
  using namespace std::yard_pound::unit_symbols;

  constexpr std::quantity v1 = 110 * km / h;
  constexpr std::quantity v2 = 70 * mph;
  constexpr std::quantity v3 = avg_speed(220. * std::isq::distance[km], 2 * h);
  constexpr std::quantity v4 = avg_speed(std::isq::distance(140. * mi), 2 * h);
  constexpr std::quantity v5 = v3.in(m / s);
  constexpr std::quantity v6 = value_cast<m / s>(v4);
  constexpr std::quantity v7 = value_cast<int>(v6);

  std::cout << v1 << '\n';                                        // 110 km/h
  std::cout << std::setw(10) << std::setfill('*') << v2 << '\n';  // ***70 mi/h
  std::cout << std::format("{:*^10}\n", v3);                      // *110 km/h*
  std::println("{:%N in %U of %D}", v4);                          // 70 in mi/h of LT⁻¹
  std::println("{::N[.2f]}", v5);                                 // 30.56 m/s
  std::println("{::N[.2f]U[dn]}", v6);                            // 31.29 m⋅s⁻¹
  std::println("{:%N}", v7);                                      // 31
}
```

Try it in [the Compiler Explorer](https://godbolt.org/z/1YfYxer7v).

### 14.3 Storage tank

This example estimates the process of filling a storage tank with some contents. It presents:

- [The importance of supporting more than one distinct quantity of the same kind](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/systems_of_quantities/#system-of-quantities-is-not-only-about-kinds),
- [faster-than-lightspeed constants](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/faster_than_lightspeed_constants/),
- how easy it is to [add custom quantity types](https://mpusz.github.io/mp-units/2.0/users_guide/framework_basics/systems_of_quantities/#defining-quantities) when needed, and
- [interoperability with `std::chrono::duration`](https://mpusz.github.io/mp-units/2.1/users_guide/framework_basics/concepts/#QuantityLike).

```cpp
import std;

namespace {

using namespace std::si::unit_symbols;

// add a custom quantity type of kind isq::length
inline constexpr struct horizontal_length : std::quantity_spec<std::isq::length> {} horizontal_length;

// add a custom derived quantity type of kind isq::area
// with a constrained quantity equation
inline constexpr struct horizontal_area : std::quantity_spec<horizontal_length * std::isq::width> {} horizontal_area;

inline constexpr auto g = 1 * std::si::standard_gravity;
inline constexpr auto air_density = std::isq::mass_density(1.225 * kg / m3);

class StorageTank {
  std::quantity<horizontal_area[m2]> base_;
  std::quantity<std::isq::height[m]> height_;
  std::quantity<std::isq::mass_density[kg / m3]> density_ = air_density;
public:
  constexpr StorageTank(const std::quantity<horizontal_area[m2]>& base, const std::quantity<isq::height[m]>& height) :
      base_(base), height_(height)
  {
  }

  constexpr void set_contents_density(const std::quantity<std::isq::mass_density[kg / m3]>& density)
  {
    assert(density > air_density);
    density_ = density;
  }

  [[nodiscard]] constexpr std::QuantityOf<isq::weight> auto filled_weight() const
  {
    std::quantity volume = std::isq::volume(base_ * height_);
    const std::QuantityOf<std::isq::mass> auto mass = density_ * volume;
    return std::isq::weight(mass * g);
  }

  [[nodiscard]] constexpr std::quantity<std::isq::height[m]> fill_level(const std::quantity<std::isq::mass[kg]>& measured_mass) const
  {
    return height_ * measured_mass * g / filled_weight();
  }

  [[nodiscard]] constexpr std::quantity<std::isq::volume[m3]> spare_capacity(const std::quantity<std::isq::mass[kg]>& measured_mass) const
  {
    return (height_ - fill_level(measured_mass)) * base_;
  }
};


class CylindricalStorageTank : public StorageTank {
public:
  constexpr CylindricalStorageTank(const std::quantity<std::isq::radius[m]>& radius, const std::quantity<std::isq::height[m]>& height) :
      StorageTank(std::quantity_cast<horizontal_area>(std::numbers::pi * pow<2>(radius)), height)
  {
  }
};

class RectangularStorageTank : public StorageTank {
public:
  constexpr RectangularStorageTank(const std::quantity<horizontal_length[m]>& length, const std::quantity<isq::width[m]>& width,
                                   const std::quantity<isq::height[m]>& height) :
      StorageTank(length * width, height)
  {
  }
};

}  // namespace


int main()
{
  const std::quantity height = std::isq::height(200 * mm);
  auto tank = RectangularStorageTank(horizontal_length(1'000 * mm), std::isq::width(500 * mm), height);
  tank.set_contents_density(1'000 * kg / m3);

  const auto duration = std::chrono::seconds{200};
  const std::quantity fill_time = std::value_cast<int>(std::quantity{duration});  // time since starting fill
  const std::quantity measured_mass = 20. * kg;                                   // measured mass at fill_time

  const std::quantity fill_level = tank.fill_level(measured_mass);
  const std::quantity spare_capacity = tank.spare_capacity(measured_mass);
  const std::quantity filled_weight = tank.filled_weight();

  const std::QuantityOf<std::isq::mass_change_rate> auto input_flow_rate = measured_mass / fill_time;
  const std::QuantityOf<std::isq::speed> auto float_rise_rate = fill_level / fill_time;
  const std::QuantityOf<std::isq::time> auto fill_time_left = (height / fill_level - 1 * one) * fill_time;

  const std::quantity fill_ratio = fill_level / height;

  std::println("fill height at {} = {} ({} full)", fill_time, fill_level, fill_ratio.in(percent));
  std::println("fill weight at {} = {} ({})", fill_time, filled_weight, filled_weight.in(N));
  std::println("spare capacity at {} = {}", fill_time, spare_capacity);
  std::println("input flow rate = {}", input_flow_rate);
  std::println("float rise rate = {}", float_rise_rate);
  std::println("tank full E.T.A. at current flow rate = {}", fill_time_left.in(s));
}
```

The above code outputs:

```
fill height at 200 s = 0.04 m (20% full)
fill weight at 200 s = 100 g₀ kg (980.665 N)
spare capacity at 200 s = 0.08 m³
input flow rate = 0.1 kg/s
float rise rate = 2e-04 m/s
tank full E.T.A. at current flow rate = 800 s
```

Try it in [the Compiler Explorer](https://godbolt.org/z/Yzax3c3vs).

### 14.4 Bridge across the Rhine

The following example codifies the history of a famous issue during the construction of a bridge across the Rhine River between the German and Swiss parts of the town Laufenburg [[Hochrheinbrücke]](https://www.normaalamsterdamspeil.nl/wp-content/uploads/2015/03/website_bridge.pdf). It also nicely presents how [the Affine Space is being modeled in the library](https://mpusz.github.io/mp-units/latest/users_guide/framework_basics/the_affine_space/).

```cpp
import std;

using namespace std::si::unit_symbols;

inline constexpr struct amsterdam_sea_level : std::absolute_point_origin<isq::altitude> {
} amsterdam_sea_level;

inline constexpr struct mediterranean_sea_level : std::relative_point_origin<amsterdam_sea_level - 27 * cm> {
} mediterranean_sea_level;

using altitude_DE = std::quantity_point<std::isq::altitude[m], amsterdam_sea_level>;
using altitude_CH = std::quantity_point<std::isq::altitude[m], mediterranean_sea_level>;

template<auto R, typename Rep>
std::ostream& operator<<(std::ostream& os, std::quantity_point<R, altitude_DE::point_origin, Rep> alt)
{
  return os << alt.quantity_ref_from(altitude_DE::point_origin) << " AMSL(DE)";
}

template<auto R, typename Rep>
std::ostream& operator<<(std::ostream& os, std::quantity_point<R, altitude_CH::point_origin, Rep> alt)
{
  return os << alt.quantity_ref_from(altitude_CH::point_origin) << " AMSL(CH)";
}

template<auto R, typename Rep>
struct std::formatter<std::quantity_point<R, altitude_DE::point_origin, Rep>> : std::formatter<std::quantity<R, Rep>> {
  template<typename FormatContext>
  auto format(const std::quantity_point<R, altitude_DE::point_origin, Rep>& alt, FormatContext& ctx) const
  {
    std::formatter<std::quantity<R, Rep>>::format(alt.quantity_ref_from(altitude_DE::point_origin), ctx);
    return std::format_to(ctx.out(), " AMSL(DE)");
  }
};

template<auto R, typename Rep>
struct std::formatter<std::quantity_point<R, altitude_CH::point_origin, Rep>> : std::formatter<std::quantity<R, Rep>> {
  template<typename FormatContext>
  auto format(const std::quantity_point<R, altitude_CH::point_origin, Rep>& alt, FormatContext& ctx) const
  {
    std::formatter<std::quantity<R, Rep>>::format(alt.quantity_ref_from(altitude_CH::point_origin), ctx);
    return std::format_to(ctx.out(), " AMSL(CH)");
  }
};

int main()
{
  // expected bridge altitude in a specific reference system
  std::quantity_point expected_bridge_alt = amsterdam_sea_level + 330 * m;

  // some nearest landmark altitudes on both sides of the river
  // equal but not equal ;-)
  altitude_DE landmark_alt_DE = altitude_DE::point_origin + 300 * m;
  altitude_CH landmark_alt_CH = altitude_CH::point_origin + 300 * m;

  // artifical deltas from landmarks of the bridge base on both sides of the river
  std::quantity delta_DE = std::isq::height(3 * m);
  std::quantity delta_CH = std::isq::height(-2 * m);

  // artificial altitude of the bridge base on both sides of the river
  std::quantity_point bridge_base_alt_DE = landmark_alt_DE + delta_DE;
  std::quantity_point bridge_base_alt_CH = landmark_alt_CH + delta_CH;

  // artificial height of the required bridge pilar height on both sides of the river
  std::quantity bridge_pilar_height_DE = expected_bridge_alt - bridge_base_alt_DE;
  std::quantity bridge_pilar_height_CH = expected_bridge_alt - bridge_base_alt_CH;

  std::println("Bridge pillars height:");
  std::println("- Germany:     {}", bridge_pilar_height_DE);
  std::println("- Switzerland: {}", bridge_pilar_height_CH);

  // artificial bridge altitude on both sides of the river in both systems
  std::quantity_point bridge_road_alt_DE = bridge_base_alt_DE + bridge_pilar_height_DE;
  std::quantity_point bridge_road_alt_CH = bridge_base_alt_CH + bridge_pilar_height_CH;

  std::println("Bridge road altitude:");
  std::println("- Germany:     {}", bridge_road_alt_DE);
  std::println("- Switzerland: {}", bridge_road_alt_CH);

  std::println("Bridge road altitude relative to the Amsterdam Sea Level:");
  std::println("- Germany:     {}", bridge_road_alt_DE.quantity_from(amsterdam_sea_level));
  std::println("- Switzerland: {}", bridge_road_alt_CH.quantity_from(amsterdam_sea_level));
}
```

The above provides the following text output:

```
Bridge pillars height:
- Germany:     27 m
- Switzerland: 3227 cm
Bridge road altitude:
- Germany:     330 m AMSL(DE)
- Switzerland: 33027 cm AMSL(CH)
Bridge road altitude relative to the Amsterdam Sea Level:
- Germany:     330 m
- Switzerland: 33000 cm
```

Try it in [the Compiler Explorer](https://godbolt.org/z/sG8K6Y4Tv).

### 14.5 Hardware voltage measurement readout

Every measurement can (and probably should) be modelled as a `quantity_point` and this is a perfect example of such a use case.

This example implements a simplified scenario of measuring voltage read from hardware through a mapped 16-bits register. The actual voltage range of [-10 V, 10 V] is mapped to [0, 65534] on hardware and the value 65535 is used for error reporting. Translation of the value requires not only scaling of the value but also applying of an offset.

```cpp
import std;

// real voltage range
inline constexpr int min_voltage = -10;
inline constexpr int max_voltage = 10;
inline constexpr int voltage_range = max_voltage - min_voltage;

// hardware encoding of voltage
using voltage_hw_t = std::uint16_t;
inline constexpr voltage_hw_t voltage_hw_error = std::numeric_limits<voltage_hw_t>::max();
inline constexpr voltage_hw_t voltage_hw_min = 0;
inline constexpr voltage_hw_t voltage_hw_max = voltage_hw_error - 1;
inline constexpr voltage_hw_t voltage_hw_range = voltage_hw_max - voltage_hw_min;
inline constexpr voltage_hw_t voltage_hw_zero = voltage_hw_range / 2;

inline constexpr struct hw_voltage_origin :
  std::relative_point_origin<std::point<std::si::volt>(min_voltage)> {} hw_voltage_origin;

inline constexpr struct hw_voltage_unit :
  std::named_unit<"hwV", std::mag_ratio<voltage_range, voltage_hw_range> * std::si::volt, hw_voltage_origin> {} hw_voltage_unit;

using hw_voltage_quantity_point = std::quantity_point<hw_voltage_unit, hw_voltage_origin, voltage_hw_t>;

// mapped HW register
volatile voltage_hw_t hw_voltage_value;

std::optional<hw_voltage_quantity_point> read_hw_voltage()
{
  voltage_hw_t local_copy = hw_voltage_value;
  if (local_copy == voltage_hw_error) return std::nullopt;
  return std::point<hw_voltage_unit>(local_copy);
}

void print(std::QuantityPoint auto qp)
{
  std::println("{:10} ({:5})", qp,
               std::value_cast<double, si::volt>(qp));
}

int main()
{
  // simulate reading of 3 values from the hardware
  hw_voltage_value = voltage_hw_min;
  std::quantity_point qp1 = read_hw_voltage().value();
  hw_voltage_value = voltage_hw_zero;
  std::quantity_point qp2 = read_hw_voltage().value();
  hw_voltage_value = voltage_hw_max;
  std::quantity_point qp3 = read_hw_voltage().value();

  print(qp1);
  print(qp2);
  print(qp3);
}
```

The above prints:

```
     0 hwV (-10 V)
 32767 hwV (  0 V)
 65534 hwV ( 10 V)
```

Try it in [the Compiler Explorer](https://godbolt.org/z/ME8xrGq8d).

### 14.6 User defined quantities and units

Users can easily define new quantities and units for domain-specific use-cases. This example from digital signal processing domain will show how to define custom strongly typed dimensionless quantities, units for them, and how they can be converted to time measured in milliseconds:

```cpp
import std;

namespace ni {

// quantities
inline constexpr struct SampleCount : std::quantity_spec<std::dimensionless, std::is_kind> {} SampleCount;
inline constexpr struct SampleDuration : std::quantity_spec<std::isq::period_duration> {} SampleDuration;
inline constexpr struct SamplingRate : std::quantity_spec<std::isq::frequency, SampleCount / SampleDuration> {} SamplingRate;

inline constexpr struct UnitSampleAmount : std::quantity_spec<std::dimensionless, std::is_kind> {} UnitSampleAmount;
inline constexpr auto Amplitude = UnitSampleAmount;
inline constexpr auto Level = UnitSampleAmount;
inline constexpr struct Power : std::quantity_spec<Level * Level> {} Power;

inline constexpr struct MIDIClock : std::quantity_spec<std::dimensionless, std::is_kind> {} MIDIClock;

inline constexpr struct BeatCount : std::quantity_spec<std::dimensionless, std::is_kind> {} BeatCount;
inline constexpr struct BeatDuration : std::quantity_spec<std::isq::period_duration> {} BeatDuration;
inline constexpr struct Tempo : std::quantity_spec<std::isq::frequency, BeatCount / BeatDuration> {} Tempo;

// units
inline constexpr struct Sample : std::named_unit<"Smpl", std::one, std::kind_of<SampleCount>> {} Sample;
inline constexpr struct SampleValue : std::named_unit<"PCM", std::one, std::kind_of<UnitSampleAmount>> {} SampleValue;
inline constexpr struct MIDIPulse : std::named_unit<"p", std::one, std::kind_of<MIDIClock>> {} MIDIPulse;

inline constexpr struct QuarterNote : std::named_unit<"q", std::one, std::kind_of<BeatCount>> {} QuarterNote;
inline constexpr struct HalfNote : std::named_unit<"h", std::mag<2> * QuarterNote> {} HalfNote;
inline constexpr struct DottedHalfNote : std::named_unit<"h.", std::mag<3> * QuarterNote> {} DottedHalfNote;
inline constexpr struct WholeNote : std::named_unit<"w", std::mag<4> * QuarterNote> {} WholeNote;
inline constexpr struct EighthNote : std::named_unit<"8th", std::mag_ratio<1, 2> * QuarterNote> {} EighthNote;
inline constexpr struct DottedQuarterNote : std::named_unit<"q.", std::mag<3> * EighthNote> {} DottedQuarterNote;
inline constexpr struct QuarterNoteTriplet : std::named_unit<"qt", std::mag_ratio<1, 3> * HalfNote> {} QuarterNoteTriplet;
inline constexpr struct SixteenthNote : std::named_unit<"16th", std::mag_ratio<1, 2> * EighthNote> {} SixteenthNote;
inline constexpr struct DottedEighthNote : std::named_unit<"q.", std::mag<3> * SixteenthNote> {} DottedEighthNote;

inline constexpr auto Beat = QuarterNote;

inline constexpr struct BeatsPerMinute : std::named_unit<"bpm", Beat / std::si::minute> {} BeatsPerMinute;
inline constexpr struct MIDIPulsePerQuarter : std::named_unit<"ppqn", MIDIPulse / QuarterNote> {} MIDIPulsePerQuarter;

namespace unit_symbols {

inline constexpr auto Smpl = Sample;
inline constexpr auto pcm = SampleValue;
inline constexpr auto p = MIDIPulse;

inline constexpr auto n_wd = 3 * HalfNote;
inline constexpr auto n_w = WholeNote;
inline constexpr auto n_hd = DottedHalfNote;
inline constexpr auto n_h = HalfNote;
inline constexpr auto n_qd = DottedQuarterNote;
inline constexpr auto n_q = QuarterNote;
inline constexpr auto n_qt = QuarterNoteTriplet;
inline constexpr auto n_8thd = DottedEighthNote;
inline constexpr auto n_8th = EighthNote;
inline constexpr auto n_16th = SixteenthNote;

}

std::quantity<BeatsPerMinute, float> GetTempo()
{
  return 110 * BeatsPerMinute;
}

std::quantity<MIDIPulsePerQuarter, unsigned> GetPPQN()
{
  return 960 * MIDIPulse / QuarterNote;
}

std::quantity<MIDIPulse, unsigned> GetTransportPos()
{
  return 15'836 * MIDIPulse;
}

std::quantity<SamplingRate[std::si::hertz], float> GetSampleRate()
{
  return 44'100.f * std::si::hertz;
}

}

int main()
{
  using namespace ni::unit_symbols;
  using namespace std::si::unit_symbols;

  const std::quantity sr1 = ni::GetSampleRate();
  const std::quantity sr2 = 48'000.f * Smpl / s;

  const std::quantity samples = 512 * Smpl;

  const std::quantity sampleTime1 = (samples.in<float>() / sr1).in(s);
  const std::quantity sampleTime2 = (samples.in<float>() / sr2).in(ms);

  const std::quantity sampleDuration1 = std::inverse<ms>(sr1);
  const std::quantity sampleDuration2 = std::inverse<ms>(sr2);

  const std::quantity rampTime = 35.f * ms;
  const std::quantity rampSamples1 = ni::SampleCount((rampTime * sr1).in(one)).force_in<int>(Smpl);
  const std::quantity rampSamples2 = (rampTime * sr2).force_in<int>(Smpl);

  std::println("Sample rate 1 is: {}", sr1);
  std::println("Sample rate 2 is: {}", sr2);

  std::println("{} @ {} is {::N[.5f]}", samples, sr1, sampleTime1);
  std::println("{} @ {} is {::N[.5f]}", samples, sr2, sampleTime2);

  std::println("One sample @ {} is {::N[.5f]}", sr1, sampleDuration1);
  std::println("One sample @ {} is {::N[.5f]}", sr2, sampleDuration2);

  std::println("{} is {} @ {}", rampTime, rampSamples1, sr1);
  std::println("{} is {} @ {}", rampTime, rampSamples2, sr2);

  const std::quantity sampleValue = -0.4f * pcm;
  const std::quantity power1 = sampleValue * sampleValue;
  const std::quantity power2 = -0.2 * pow<2>(pcm);

  const std::quantity tempo = ni::GetTempo();
  const std::quantity reverbBeats = 1 * n_qd;
  const std::quantity reverbTime = reverbBeats / tempo;

  const std::quantity pulsePerQuarter = std::value_cast<float>(ni::GetPPQN());
  const std::quantity transportPosition = ni::GetTransportPos();
  const std::quantity transportBeats = (transportPosition / pulsePerQuarter).in(n_q);
  const std::quantity transportTime = (transportBeats / tempo).in(s);

  std::println("SampleValue is: {}", sampleValue);
  std::println("Power 1 is: {}", power1);
  std::println("Power 2 is: {}", power2);

  std::println("Tempo is: {}", tempo);
  std::println("Reverb Beats is: {}", reverbBeats);
  std::println("Reverb Time is: {}", reverbTime.in(s));
  std::println("Pulse Per Quarter is: {}", pulsePerQuarter);
  std::println("Transport Position is: {}", transportPosition);
  std::println("Transport Beats is: {}", transportBeats);
  std::println("Transport Time is: {}", transportTime);

  // auto error = 1 * Smpl + 1 * pcm + 1 * p + 1 * Beat;  // Compile-time error
}
```

The above code outputs:

```
Sample rate 1 is: 44100 Hz
Sample rate 2 is: 48000 Smpl/s
512 Smpl @ 44100 Hz is 0.01161 s
512 Smpl @ 48000 Smpl/s is 10.66667 ms
One sample @ 44100 Hz is 0.02268 ms
One sample @ 48000 Smpl/s is 0.02083 ms
35 ms is 1543 Smpl @ 44100 Hz
35 ms is 1680 Smpl @ 48000 Smpl/s
SampleValue is: -0.4 PCM
Power 1 is: 0.16000001 PCM²
Power 2 is: -0.2 PCM²
Tempo is: 110 bpm
Reverb Beats is: 1 q.
Reverb Time is: 0.8181818 s
Pulse Per Quarter is: 960 ppqn
Transport Position is: 15836 p
Transport Beats is: 16.495832 q
Transport Time is: 8.997726 s
```

Try it in [the Compiler Explorer](https://godbolt.org/z/eYx79sxzz).

*Note: More about this example can be found in [“Exploration of Strongly-typed Units in C++: A Case Study from Digital Audio”](https://www.youtube.com/watch?v=oxnCdIfC4Z4) CppCon 2023 talk by Roth Michaels.*

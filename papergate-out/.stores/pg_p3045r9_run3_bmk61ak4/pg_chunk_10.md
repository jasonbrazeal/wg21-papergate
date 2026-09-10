## 12 Representation Types

Every `quantity` has a **representation type** that stores the numerical value. The library works seamlessly with fundamental arithmetic types (except `bool`) and `std::complex`, but custom representation types can also be used to model domain-specific requirements—such as range-validated values, vectors, or specialized numeric types.

The representation type determines what mathematical operations are available and how the quantity behaves in calculations. The library verifies at compile time that the representation type has the capabilities required for the quantity’s character.

### 12.1 Representation Requirements

To be used as a representation type, a type must satisfy the `RepresentationOf` concept. The library supports different types of representations corresponding to different quantity characters.

**Why verify representation capabilities?** The same unit can represent fundamentally different physical concepts requiring different mathematical operations. For example:

- *speed* (scalar, magnitude only) vs. *velocity* (vector, magnitude and direction) both use m/s,
- *mass* (scalar) uses kg while *weight force* (vector, pointing downward) uses N.

The library tracks **character in the quantity specification** (what the quantity represents) and verifies that the **representation type provides the required capabilities**. This dual approach provides **compile-time type safety** for the mathematical nature of physical quantities—preventing, for example, using a scalar type where vector operations like cross product are needed.

The following table summarizes the requirements for different representation characters:

| Requirement | Real Scalar | Complex Scalar | Vector | Tensor |
| --- | --- | --- | --- | --- |
| Copyable | ✅ | ✅ | ✅ | ✅ |
| Addition/subtraction (`+`, `-`, unary `-`) | ✅ | ✅ | ✅ | ✅ |
| `MagnitudeScalable` (unit-conversion) | ✅ | ✅ | ✅ | ✅ |
| Self-scalable (`T * T`, `T / T`) | ✅ | ✅ | - | - |
| Equality comparable (`==`) | ✅ | ✅ | ✅ | ✅ |
| Totally ordered (`<`, `>`, `<=`, `>=`) | ✅ | - | - | - |
| Not a quantity type itself | ✅ | ✅ | ✅ | ✅ |
| **Construction** | - | `T{real, imag}` | - | - |
| **Required CPOs** | - | `mp_units::real()`, `mp_units::imag()`, `mp_units::modulus()` | `mp_units::magnitude()` | `mp_units::magnitude()` |
| **Opt-out mechanism** | `disable_real<T>` | - | `disable_vector<T>` | - |
| **Examples** | `int`, `double`, `long double` | `std::complex<double>` | `Eigen::Vector3d`, `cartesian_vector<double>`, `int`, `double` | `Eigen::Matrix3d`, `int`, `double` (for scalar measures) |

All representation types must be **weakly regular**, which means they satisfy the `std::regular` concept except for the default-constructibility requirement. Specifically, they must be:

- **Copyable** (`std::copyable`)
- **Equality comparable** (`std::equality_comparable`)

This ensures that representation types have value semantics suitable for use in quantities. Default construction is not required, allowing types like range-validated representations that may not have a meaningful default value.

**Construction**

Complex scalars **must** be constructible from real and imaginary parts: `T{real_value, imag_value}`. This is essential for operations that combine real-valued quantities into complex results. For example, combining *active power* and *reactive power* into *complex power*:

```cpp
quantity active = isq::active_power(100.0 * W);
quantity reactive = isq::reactive_power(50.0 * W);
// Library needs to construct: std::complex<double>{active.numerical_value(),
//                                                  reactive.numerical_value()}
```

**Total Ordering**

Well-designed complex-like types do not provide total ordering (`operator<`, etc.) since there is no natural ordering for complex numbers. If a complex-like type does provide ordering operators (e.g., for use in containers), use the `disable_real` opt-out mechanism:

```cpp
template<>
constexpr bool mp_units::disable_real<my_complex_type> = true;
```

Alternatively, the library could explicitly check for the absence of `mp_units::real()` and `mp_units::imag()` to distinguish real from complex scalars — a design choice that may be refined based on standardization discussions.

The different names reflect domain conventions: `modulus()` is traditional complex analysis terminology, while `magnitude()` follows physics and engineering conventions for vectors. Naming the vector CPO `norm` was considered but rejected: `std::norm` already exists in `<complex>` with a different meaning — it returns |z|² (the squared modulus), not |z|. Introducing a standard CPO named `norm` that returns |v| would create a semantic collision within the same namespace. The library therefore uses `magnitude` as the primary name and additionally accepts `norm`-named member functions and free functions as fallbacks, so that types from linear algebra libraries integrate without adaptation.

Arithmetic types like `int` and `double` intentionally satisfy requirements for multiple characters — real scalar (primary use), 1-dimensional vector, and scalar tensor measures like von Mises stress. Type safety comes from `quantity_character` matching in the quantity specification, not from mutually exclusive representation concepts:

```cpp
// All valid uses of double:
quantity m = isq::mass(5.0 * kg);           // Scalar
quantity v = isq::velocity(10.0 * m/s);     // 1D vector
quantity sigma = isq::stress(100.0 * Pa);   // Scalar tensor measure
```

Most engineering extracts scalar measures from tensor fields rather than working with full 3×3 matrix representations — von Mises stress, principal stresses, shear components, hydrostatic stress — which is why arithmetic types cover the tensor character in practice.

### 12.2 Concept Hierarchy

Most of the concepts described below are *exposition-only*: they capture how the library classifies representation types internally and are not part of its public interface. The only public concept in this chapter is `RepresentationOf` — the building-block and character concepts (`Addable`, `ScalableWith`, `RealScalar`, `Vector`, and the rest) exist to define it and to explain how a representation type is recognized.

These concepts are **syntactic**: they constrain which operations are available and that results have a common type with `T` (`std::common_with`). They deliberately do **not** — and a C++ concept fundamentally cannot — enforce the algebraic *laws* (associativity, commutativity, distributivity, existence of identities, compatibility of an order with the arithmetic) that the corresponding mathematical structures require. This is the same limitation `std::regular` and `std::totally_ordered` already accept. For this reason the concepts are named for the *role* a type plays rather than for the structure it resembles; Relationship to algebraic structures below maps each one to the structure it approximates and lists the laws left unchecked.

The requirements summarized in the table above map directly to a hierarchy of C++ concepts. The lowest-level building blocks are:

```cpp
template<typename T>
concept WeaklyRegular = std::copyable<T> && std::equality_comparable<T>;

template<typename T>
concept Addable = requires(const T a, const T b) {
  { -a } -> std::common_with<T>;
  { a + b } -> std::common_with<T>;
  { a - b } -> std::common_with<T>;
};

template<typename T, typename S>
concept ScalableWith = requires(const T v, const S s) {
  { v * s / s } -> std::common_with<T>;
  { s * v / s } -> std::common_with<T>;
  { v / s * s } -> std::common_with<T>;
};
```

`WeaklyRegular` is `std::regular` without default-initialization. Default construction is intentionally not required: some representation types cannot provide a meaningful default-constructed value (see, e.g., [[P2993R0]](https://wg21.link/p2993r0)) yet are otherwise well-behaved as quantity representations. Requiring only copyability and equality comparison keeps such types in scope.

`Addable` requires unary negation (`-a`) alongside `+` and `-`, so it models an additive *group* rather than a mere monoid. Inverses are required because the library forms differences (between quantities, and between quantity points); types that support only accumulation are intentionally out of scope.

`ScalableWith<T, S>` deliberately constrains the *round-trip* `v * s / s` rather than the intermediate `v * s`. Leaving the intermediate unconstrained is intentional: it lets types whose `operator*`/`operator/` change the type — quantities being the canonical example — still satisfy the concept, as long as scaling by `s` and back lands on a type with a common type with `T`. The round-trip requirement simultaneously rejects irreversible silent type promotion, where `operator*` decays to a different type than `T` and never recovers it (e.g. a checked-integer wrapper whose `operator*` returns a raw arithmetic type). The constraint is on the result *type*, not its value: over integer representations `v * s / s` need not equal `v` (integer division truncates). `ScalableWith` certifies that the scalar action is **type-stable**, not that scaling is exactly invertible. Because the round-trip divides by `s`, the scalar type `S` must itself be division-capable (field-like); scaling by ring-only scalars that lack division is not expressible through this concept.

The result types of `+`, `-`, and the scaling round-trip are guarded with `std::common_with<T>` rather than left unconstrained or pinned to a stronger concept, and the choice is a deliberate compromise:

- A bare requirement (`{ a + b };`) is satisfied even by an `operator+` returning `void`, so some return check is needed.
- The natural ideal — requiring the result to be a scalar/vector *again* (true closure, `{ a + b } -> Scalar`) — is **ill-formed**, not merely expensive: those character concepts are defined transitively through `Addable`/`ScalableWith`, so constraining their own results by them would make a concept depend on itself, which 13.5.2.3 [[temp.constr.atomic]](https://wg21.link/temp.constr.atomic) forbids (and which would otherwise recurse without termination).
- Requiring `std::same_as<T>` is well-formed but too strong: it forbids the type-changing arithmetic the round-trip is designed to permit (expression templates, quantities).

`std::common_with<T>` is the non-recursive middle ground: it rejects `void` and unrelated return types while admitting any result that shares a common type with `T`. The standard’s cross-type comparison concepts (`std::equality_comparable_with`, `std::three_way_comparable_with`) constrain with the related `std::common_reference_with`, because they relate operands that may be lvalues or proxy references. Here the constrained expressions yield prvalues, so a common *value* type is the meaningful requirement — and `std::common_with` is the stronger relation anyway, entailing `common_reference_with` for the corresponding `const` lvalue references ([concept.common]).

These compose into the character-specific concepts:

```cpp
template<typename T>
concept RegularAddable = Addable<T> && WeaklyRegular<T>;

// Scalars: self-scalable — T * T and T / T stay in the same type
template<typename T>
concept BaseScalar = RegularAddable<T> && ScalableWith<T, T>;

// Real scalar: totally ordered, opt-out via disable_real<T>
template<typename T>
concept RealScalar = !disable_real<T> && BaseScalar<T> && std::totally_ordered<T>;

// Complex scalar: constructible from real/imag parts; provides real, imag, modulus
template<typename T>
concept ComplexScalar =
  BaseScalar<T> &&
  requires(const T v, const T& ref) {
    requires std::constructible_from<T,
      decltype(mp_units::real(ref)), decltype(mp_units::imag(ref))>;
    mp_units::real(v);
    mp_units::imag(v);
    mp_units::modulus(v);
    requires ScalableWith<T, decltype(mp_units::modulus(v))>;
  };

// Vector: scalable by its magnitude type (a scalar); magnitude need not equal T
template<typename T>
concept Vector =
  !disable_vector<T> &&
  RegularAddable<T> &&
  requires(const T v) {
    mp_units::magnitude(v);
    requires ScalableWith<T, decltype(mp_units::magnitude(v))>;
  };
```

The key structural difference between `BaseScalar` and `Vector` reflects the underlying mathematics. A scalar type must satisfy `ScalableWith<T, T>` — multiplying two scalars yields another scalar of the same kind. A vector type is only required to satisfy `ScalableWith<T, decltype(magnitude(v))>` — it can be scaled by its magnitude (a scalar), but vector × vector is not required and is typically not defined at all.

The concept is named `Vector` to match the `quantity_character::vector` it identifies, not to assert that it models an arbitrary vector space. In the [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) sense a vector quantity is characterized by a magnitude and a direction, so the `magnitude(v)` requirement is intrinsic to that character rather than an extra restriction: the representation of a vector quantity is, precisely, an element of a normed space.

`ComplexScalar` takes `modulus(v)` to be the Euclidean modulus \(|z| = \sqrt{\operatorname{re}(z)^2 + \operatorname{im}(z)^2}\) — the same quantity `magnitude` computes for vectors — and *not* the algebraic field norm \(|z|^2\) (see Relationship to algebraic structures).

The character concepts combine with `MagnitudeScalable` (described in How Scaling Works) to form the representation concepts the library checks internally:

```cpp
template<typename T>
concept RealScalarRepresentation = !is_quantity<value_type_t<T>> && RealScalar<T> && MagnitudeScalable<T>;

template<typename T>
concept ComplexScalarRepresentation = !is_quantity<value_type_t<T>> && ComplexScalar<T> && MagnitudeScalable<T>;

template<typename T>
concept VectorRepresentation = !is_quantity<value_type_t<T>> && Vector<T> && MagnitudeScalable<T>;
```

The `!is_quantity<value_type_t<T>>` guard applies to the **element type** of `T`, not to `T` itself. For a plain type like `double`, `value_type_t<double>` is `double` — not a quantity, so the guard is satisfied. For a container-style representation like `cartesian_vector<double>`, `value_type_t<cartesian_vector<double>>` is `double` — also fine. The guard rejects `cartesian_vector<quantity<si::metre, double>>` because its element type is itself a quantity, preventing inadvertent nesting of quantities.

The top-level public concept is `RepresentationOf<T, V>`, where `V` is either a `quantity_spec` or a `quantity_character` value:

```cpp
template<typename T, auto V>
concept RepresentationOf =
  (QuantitySpec<decltype(V)> &&
   ((QuantityKindSpec<decltype(V)> && SomeRepresentation<T>) ||
    IsOfCharacter<T, V.character>)) ||
  (std::same_as<quantity_character, decltype(V)> && IsOfCharacter<T, V>);
```

When `V` is a `quantity_spec`, the concept checks whether `T` matches the character embedded in that spec. For a *kind* spec — one that represents an entire kind without pinning a specific character, such as `kind_of<isq::length>` — any valid representation type is accepted. When `V` is a bare `quantity_character` value (e.g., `quantity_character::vector`), `T` must directly satisfy that character’s requirements.

#### 12.2.1 Relationship to algebraic structures

Each concept above approximates a classical algebraic structure but is named for the role it plays in the library rather than for that structure. We avoid the structural names (`Field`, `OrderedField`, `VectorSpace`, …) on purpose:

- A concept can only check that operations exist and that result types are stable; it cannot verify the defining laws. A concept named `Field` would promise associativity, distributivity, and inverses that the compiler never enforces.
- The library deliberately admits types that are *weaker* than the named structure. `int` is not a field (it has no multiplicative inverses) yet must satisfy `BaseScalar`; `int` and `double` are accepted as one-dimensional vectors although they are not, in the usual sense, elements of a vector space. Role-oriented names (“scalar”, “vector”) communicate the intended use without making algebraic claims the type does not honor.

| Concept | Structure approximated | Principal laws left unchecked |
| --- | --- | --- |
| `Addable` | additive group | associativity & commutativity of `+`, existence of `0` |
| `WeaklyRegular` | a set with value semantics (copy + equality) | — |
| `RegularAddable` | a (regular) abelian group under addition | the group axioms above |
| `ScalableWith<T,S>` | a scalar action of `S` on `T` (module / vector-space multiplication) | distributivity and associativity of the action; closure is approximated by round-trip type stability, not `v*s/s == v` |
| `BaseScalar` | a field (commutative division ring) | commutativity/associativity of `×`, distributivity, existence of `0` and `1` |
| `RealScalar` | an ordered field | compatibility of the order with `+` and `×` (`std::totally_ordered` is only a set order) |
| `ComplexScalar` | the complex field `ℂ` (a 2-D real division algebra with modulus) | field axioms; that `real`/`imag` genuinely coordinatize `ℂ` |
| `Vector` | an element of a normed vector space | the vector-space axioms and the norm axioms (homogeneity, triangle inequality) |

A note on the magnitude vocabulary, where the mathematics is most easily miscommunicated. The word “norm” is overloaded across mathematics:

- the **algebraic (field) norm** \(N(z) = z\bar{z} = |z|^2\) — a multiplicative, quadratic form; and
- the **Euclidean (\(L^2\)) norm** \(\lVert v\rVert = \sqrt{N(z)} = |z|\) — the analytic norm satisfying the triangle inequality.

`std::norm(std::complex)` already exists and computes the *field* norm \(|z|^2\), not \(|z|\). A new customization point named `norm` returning \(\lVert v\rVert\) would therefore both collide with `std::norm` and reuse a word that already carries a different, legitimate meaning in the same namespace. The library avoids the ambiguity by using:

- `modulus(z)` for the complex absolute value \(|z|\) (the standard complex-analysis term), and
- `magnitude(v)` for the vector Euclidean norm \(\lVert v\rVert\),

and by exposing no customization point for the field norm.

Complex types are kept out of the vector character by the `!Scalar` guard on the `norm` fallback (described above) together with `disable_vector<std::complex>`: without those, `std::norm(z)` would supply the real value \(|z|^2\) and make a complex number satisfy `Vector` with a spurious “magnitude”.

### 12.3 Customization Points

The library provides several customization mechanisms for representation types. These fall into two categories: **Character determination** (what kind of representation type you have) and **Behavior and values** (how the library interacts with your type).

#### 12.3.1 Character Determination

##### 12.3.1.1 Customization Point Objects (CPOs)

The library uses several CPOs to support different representation types. Providing these CPOs determines the **character** of the representation type. Each CPO checks for implementations in the following priority order:

**`mp_units::real(c)`** - Returns the real part of a complex number:

1. `c.real()` member function
2. `real(c)` free function found via ADL

**`mp_units::imag(c)`** - Returns the imaginary part of a complex number:

1. `c.imag()` member function
2. `imag(c)` free function found via ADL

**`mp_units::modulus(c)`** - Returns the magnitude of a complex number:

1. `c.modulus()` member function
2. `modulus(c)` free function found via ADL
3. `c.abs()` member function
4. `abs(c)` free function found via ADL

**`mp_units::magnitude(v)`** - Returns the magnitude of a vector or tensor as a scalar:

1. `v.magnitude()` member function
2. `magnitude(v)` free function found via ADL
3. `v.norm()` member function
4. `norm(v)` free function found via ADL
5. For arithmetic types: `std::abs(v)`
6. For real scalar types: `v.abs()` member function
7. For real scalar types: `abs(v)` free function found via ADL

Steps 3–4 are provided so that types from linear algebra libraries that follow the `norm()` naming convention work without adaptation. They are guarded to only apply when `T` is not a `Scalar` (i.e., neither a real nor a complex scalar): `std::norm` is overloaded both for arithmetic types and for `std::complex`, returning |x|² rather than |x| in either case, so scalar types are explicitly directed to the `abs` fallback below instead.

For `modulus()`, `abs()` is accepted as a fallback for compatibility with `std::complex` and similar types that use that name. For `magnitude()`, `abs()` enables arithmetic types to serve as 1-dimensional vectors and scalar tensor measures, which accurately reflects engineering practice where most calculations use scalar values rather than full vector/tensor representations. —

##### 12.3.1.2 `disable_real<T>`

A specializable variable template to opt out a type from being treated as a real scalar:

```cpp
template<typename T>
constexpr bool mp_units::disable_real = false;
```

Specializing to `true` prevents a type from being classified as real scalar character even if it satisfies all syntactic requirements. The library uses this internally to exclude `bool`, which is totally ordered and arithmetic but meaningless as a quantity:

```cpp
template<>
constexpr bool mp_units::disable_real<my_type> = true;
```

> [ *Note:* The `disable_real` and `disable_vector` opt-outs exist for the same underlying reason: both guard against syntactic satisfaction of a concept where the **semantics are wrong**.
> 
> - `disable_real<T>`: `std::totally_ordered` is a ubiquitous, incidental property. Many types support `operator<` purely for container use with no physical meaning as a real scalar. `bool` is the canonical example.
> - `disable_vector<T>`: the `magnitude()` CPO accepts `norm()` as a fallback (for linear algebra library interoperability), but `std::norm` for complex types returns |z|² rather than |z|. `std::complex<T>` is therefore opted out by default.
> 
> There is no `disable_complex<T>`. The `ComplexScalar` contract — `real()`, `imag()`, and `modulus()` by those names, plus `T{re, im}` construction — is too specific to be satisfied accidentally by any standard type or mixin. No opt-out is needed. — *end note* ]

---

##### 12.3.1.3 `disable_vector<T>`

A specializable variable template to opt out a type from being treated as a vector:

```cpp
template<typename T>
constexpr bool mp_units::disable_vector = false;
```

Specializing to `true` prevents a type from satisfying `Vector` even if it provides all required operations. The library uses this internally to exclude `std::complex<T>`: `std::complex<T>` satisfies the syntactic requirements for `Vector` because the non-member `std::norm` (found via ADL) is accepted as a fallback for `mp_units::magnitude()`. However, `std::norm(z)` returns |z|² — the **squared** modulus — not |z|, so the semantics are wrong for a vector magnitude. Opting out prevents this accidental satisfaction:

```cpp
// built-in specialization — do not specialize further for std::complex
template<typename T>
constexpr bool mp_units::disable_vector<std::complex<T>> = true;
```

User-defined complex-like types that provide `real()`, `imag()`, and `norm()` should follow the same pattern:

```cpp
template<>
constexpr bool mp_units::disable_vector<my_complex_type> = true;
```

> [ *Note:* The `disable_real` / `disable_vector` pair share the same rationale: both opt-out mechanisms guard against accidental syntactic satisfaction of a concept where the semantics are wrong. `disable_complex` is not needed because the `ComplexScalar` contract — `real()`, `imag()`, `modulus()` by those names, plus `T{re, im}` construction — is too specific to be satisfied accidentally. — *end note* ]

---

#### 12.3.2 Behavior and Values

##### 12.3.2.1 `representation_underlying_type<T>`

`representation_underlying_type<T>` is the extension point for exposing the underlying arithmetic or element type of a representation to the library. It drives the scaling factor type and the `treat_as_floating_point` check:

```cpp
template<typename T>
struct mp_units::representation_underlying_type;  // primary — empty

template<typename T>
using mp_units::representation_underlying_type_t = representation_underlying_type<T>::type;
```

The library provides partial specializations that detect the underlying type in order:

1. `T::value_type` or `T::element_type` member type (cv-qualification stripped)
2. `std::underlying_type_t<T>` for scoped enumerations (unscoped enumerations are excluded — they already implicitly convert to their underlying type)
3. `T` itself as a fallback

If both `value_type` and `element_type` are present with differing underlying types, the trait is empty and the library treats `T` as a leaf — provide only `value_type` unless there is a specific reason to expose both (e.g., satisfying iterator concepts), in which case ensure they name the same underlying type.

A `value_type` member is the preferred form for types under the user’s control:

```cpp
template<typename T>
class my_wrapper {
public:
  using value_type = T;
  // ...
};
```

When the source of a type cannot be modified, the trait may be specialized directly:

```cpp
// MyFloat wraps long double internally
template<>
struct mp_units::representation_underlying_type<MyFloat> {
  using type = long double;
};
```

> [ *Note:* `std::indirectly_readable_traits` was intentionally not reused: that standard trait answers “what does `*t` yield?” and is the extension point for iterators and smart pointers — specializing it for a non-iterator type is a semantic misuse. — *end note* ]

---

##### 12.3.2.2 Scaling operators

The library scales a representation value by calling `value * factor` and `value / factor`, where `factor` is of type `representation_underlying_type_t<T>` (or a wider integer type for the rational integer path — see How Scaling Works for details). A type may additionally provide `operator*(T, UnitMagnitude)` to receive the full compile-time unit magnitude; when present, this operator is called **first** and the factor-based operators serve as a fallback. The magnitude-aware operator may return a **different type** — see Magnitude-aware scaling for the full pattern.

These operators are found via ADL. Hidden friends are the preferred form for types under the user’s control; non-member operators placed in the type’s namespace serve the same role for third-party types:

```cpp
template<typename T>
class my_wrapper {
  T value_;
public:
  using value_type = T;

  friend constexpr my_wrapper operator*(my_wrapper v, T factor) { return my_wrapper{v.value_ * factor}; }
  friend constexpr my_wrapper operator/(my_wrapper v, T factor) { return my_wrapper{v.value_ / factor}; }

  // Optional: magnitude-aware scaling (return type may differ from my_wrapper)
  // template<mp_units::UnitMagnitude M>
  // friend constexpr auto operator*(const my_wrapper& v, M m) { /* ... */ }
};
```

---

##### 12.3.2.3 `treat_as_floating_point<Rep>`

A specializable variable template that tells the library whether a type should be treated as floating-point for the purpose of allowing implicit conversions:

```cpp
template<typename Rep>
constexpr bool mp_units::treat_as_floating_point = /* implementation-defined */;
```

By default, the value is determined by applying `std::chrono::treat_as_floating_point_v` (hosted) or `std::is_floating_point_v` (freestanding) to the recursively-unwrapped underlying type of `Rep`. When `true`, implicit conversions are enabled; otherwise an explicit `value_cast` is required (see Value conversions). A specialization is needed when automatic detection yields an incorrect result:

```cpp
template<>
constexpr bool mp_units::treat_as_floating_point<my_fixed_point_type> = true;
```

---

##### 12.3.2.4 `implicitly_scalable<FromUnit, FromRep, ToUnit, ToRep>`

A specializable variable template that controls **whether** a conversion from `quantity<FromUnit, FromRep>` to `quantity<ToUnit, ToRep>` is implicit or requires an explicit cast via `value_cast`/`force_in`. It is the policy layer built on top of `treat_as_floating_point`: the default formula derives the implicit-conversion decision from it, and a specialization overrides that decision for types where the derived rule is incorrect:

```cpp
template<auto FromUnit, typename FromRep, auto ToUnit, typename ToRep>
constexpr bool mp_units::implicitly_scalable =
  treat_as_floating_point<ToRep> ||
  (!treat_as_floating_point<FromRep> && is_integral_scaling(FromUnit, ToUnit));
```

`mp_units::is_integral_scaling(from, to)` is a `consteval` predicate that can also be used in user specializations to distinguish the integral-factor case (e.g. `m → mm` (×1000)) from fractional ones (e.g. `mm → m` (÷1000), `ft → m`, `deg → rad`).

The default follows the precedent of `std::chrono::duration`: conversions to a floating-point representation are always implicit, conversions between integer representations are implicit only when the unit ratio is an integer multiplier (exact, no truncation), and all other cases require an explicit cast.

For example, a decimal fixed-point type that represents fractional ratios exactly can permit all unit conversions implicitly:

```cpp
template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, safe_decimal, ToUnit, safe_decimal> = true;
```

When precision is asymmetric between two types, the specialization can be directional:

```cpp
template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, double, ToUnit, my_decimal> = true;

template<auto FromUnit, auto ToUnit>
constexpr bool mp_units::implicitly_scalable<FromUnit, my_decimal, ToUnit, double> = false;
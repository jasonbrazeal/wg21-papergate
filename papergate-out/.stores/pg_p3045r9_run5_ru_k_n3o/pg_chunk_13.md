## 15 Why do we need typed quantities?

### 15.1 Limitations of units-only solutions

Units-only is not a good design for a quantities and units library. It works to some extent, but plenty of use cases can’t be addressed, and for those that somehow work, we miss important safety improvements provided by additional abstractions in this chapter. But before we talk about those extensions, let’s first discuss some limitations of the units-only solution.

*Note: The issues described below do not apply to the proposed library, because with the proposed interfaces, even if we decide to only use units, they are still backed up by quantity kinds under the framework’s hood.*

#### 15.1.1 No way to specify a quantity type in generic interfaces

A common requirement in the domain is to write unit-agnostic generic interfaces. For example, let’s try to implement a generic `avg_speed` function template that takes a quantity of any unit and produces the result. So if we call it with *distance* in `km` and *time* in `h`, we will get `km / h` as a result, but if we call it with `mi` and `h`, we expect `mi / h` to be returned.

```cpp
template<Unit auto U1, typename Rep1, Unit auto U2, typename Rep2>
auto avg_speed(quantity<U1, Rep1> distance, quantity<U2, Rep2> time)
{
  return distance / time;
}

quantity speed = avg_speed(120 * km, 2 * h);
```

This function works but does not provide any type safety to the users. The function arguments can be easily reordered on the call site. Also, we do not get any information about the return type of the function and any safety to ensure that the function logic actually returns a quantity of *speed*.

To improve safety, with a units-only library, we have to write the function in the following way:

```cpp
template<typename Rep1, typename Rep2>
quantity<si::metre / si::second, decltype(Rep1{} / Rep2{})> avg_speed(quantity<si::metre, Rep1> distance,
                                                                      quantity<si::second, Rep2> time)
{
  return distance / time;
}

avg_speed(120 * km, 2 * h).in(km / h);
```

Despite being safer, the above code decreased the performance because we always pay for the conversion at the function’s input and output.

Moreover, in a good library, the above code should not compile. The reason for this is that even though the conversion from `km` to `m` and from `h` to `s` is considered value-preserving, it is not true in the opposite direction. When we will try to convert the result stored in an integral type from the unit of `m/s` to `km/h` we will inevitably lose some data.

We could try to provide concepts like `ScaledUnitOf<si::metre>` that would take a set of units while trying to constrain them somehow, but it leads to even more problems with the unit definitions. For example, are `Hz` and `Bq` just scaled versions of `1/s`? If we constrain the interface to just prefixed units, then litre and a cubic metre or kilometre and mile will be incompatible. What about radian and steradian or a litre per 100 kilometre (popular unit of a fuel consumption) and a squared metre? Should those be compatible?

#### 15.1.2 Disjoint units of the same quantity type do not work

Sometimes, we need to define several units describing the same quantity but which should not convert to each other in the library’s framework. A typical example here is currency. A user may want to define EURO and USD as units of currency, so both of them can be used for such quantities. However, it is impossible to predefine one fixed conversion factor for those, as a currency exchange rate varies over time, and the library’s framework can’t provide such an information as an input to the built-in conversion function. User’s application may have more information in this domain and handle such a conversion at runtime with custom logic (e.g., using an additional time point function argument). If we would like to model that in a unit-only solution, how can we specify that EURO and USD are units of quantities of currency, but are not convertible to each other?

### 15.2 Dimensions to the rescue?

To prevent the above issues, most of the libraries on the market introduce dimension abstraction. Thanks to that, we could solve the first issue of the previous chapter with:

```cpp
QuantityOf<dim_speed> auto avg_speed(QuantityOf<dim_length> auto distance,
                                     QuantityOf<dim_time> auto time)
{
  return distance / time;
}
```

and the second one by specifying that both EURO and USD are units of `dim_currency`. This is a significant improvement but still has some issues.

#### 15.2.1 Limitations of dimensions

Let’s first look again at the above solution. A domain expert seeing this code will immediately say there is no such thing as a speed dimension. The ISQ specifies only 7 dimensions with unique symbols assigned, and the dimensions of all the ISQ quantities are created as a vector product of those. For example, a quantity of *speed* has a dimension of \(L^1T^{-1}\). So, to be physically correct, the above code should be rewritten as:

```cpp
QuantityOf<dim_length / dim_time> auto avg_speed(QuantityOf<dim_length> auto distance,
                                                 QuantityOf<dim_time> auto time)
{
  return distance / time;
}
```

Most of the libraries on the market ignore this fact and try to model distinct quantities through their dimensions, giving a false sense of safety. A dimension is not enough to describe a quantity. This has been known for a long time now. The [[Measurement Data]](https://www.bkent.net/Doc/mdarchiv.pdf) report from 1996 says explicitly, “Dimensional analysis does not adequately model the semantics of measurement data”.

In the following chapters, we will see a few use cases that can’t be solved with an approach that only relies on units or dimensions.

#### 15.2.2 SI units of quantities of the same dimension but different kinds

The [[SI]](https://www.bipm.org/en/publications/si-brochure) provides several units for distinct quantities of the same dimension but different kinds. For example:

- hertz (Hz) is a unit of *frequency* and becquerel (Bq) is a unit of *activity*. Both are defined as \(s^{-1}\), and have the same dimension of \(T^{-1}\).
- gray (Gy) is a unit of *absorbed dose* and sievert (Sv) is a unit of *dose equivalent*. Both are defined as \(m^2 s^{-2}\), and have the same dimension of \(L^2T^{-2}\)
- radian (rad) is a unit of *plane angle* defined as \(m/m\), and steradian (sr) is a unit of *solid angle* defined as \(m^2/m^2\). Both are quantities of dimension one, which also has its own units like one (1) and percent (%).

There are many more similar examples in [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html). For example, *storage capacity* quantity can be measured in units of one, bit, octet, and byte.

The above conflicts can’t be solved with dimensions, and they yield many safety issues. For example, we can ask ourselves what should be the result of the following:

1. `quantity q = 1 * Hz + 1 * Bq;`
2. `quantity<Gy> q = 42 * Sv;`
3. `bool b = (1 * rad + 1 * bit) == 2 * sr;`

None of the above code should compile, but most of the libraries on the market happily accept it and provide meaningless results. Some of them decide not to define one or more of the above units at all to avoid potential safety issues. For example, [the [Au] library does not define `Sv` to avoid mixing it up with Gy](https://github.com/aurora-opensource/au/pull/157).

#### 15.2.3 Derived quantities of the same dimension but different kinds

Even if some quantities do not have a specially assigned unit, they may still have a totally different physical meaning even if they share the same dimension:

- *work* vs. *moment of force* both of the same dimension \(L^2MT^{-2}\)
- *fuel consumption* expressed in \(\frac{l}{100\;km}\) vs. *area* expressed in \(m^2\) both of the same dimension \(L^2\)

Again, we don’t want to accidentally mix those.

#### 15.2.4 Various quantities of the same dimension and kinds

Even if we somehow address all the above, there are plenty of use cases that still can’t be safely implemented with such abstractions.

Let’s consider that we want to implement a freight transport application to position cargo in the container. In majority of the products on the market we will end up with something like:

```cpp
class Box {
  length length_;
  length width_;
  length height_;
public:
  Box(length l, length w, length h): length_(l), width_(w), height_(h) {}
  area floor() const { return length_ * width_; }
  // ...
};
```

```cpp
Box my_box(2 * m, 3 * m, 1 * m);
```

Such interfaces are not much safer than just using plain fundamental types (e.g., `double`). One of the main reasons of using a quantities and units library was to introduce strong-type interfaces to prevent such issues. In this scenario, we need to be able to discriminate between *length*, *width*, and *height* of the package.

A similar but also really important use case is in aviation. The current *altitude* is a totally different quantity than the *distance* to the destination. The same is true for *forward speed* and *sink rate*. We do not want to accidentally mix those.

When we deal with *energy*, we should be able to implicitly construct it from a proper product of any *mass*, *length*, and *time*. However, when we want to calculate *gravitational potential energy*, we may not want it to be implicitly initialized from any expression of matching dimensions. Such an implicit construction should be allowed only if we multiply a *mass* with *acceleration of free fall* and *height*. All other conversions should have an explicit annotation to make it clear that something potentially unsafe is being done in the code. Also, we should not be able to assign a *potential energy* to a quantity of *kinetic energy*. However, both of them (possibly accumulated with each other) should be convertible to a *mechanical energy* quantity.

```cpp
mass m = 1 * kg;
length l = 1 * m;
time t = 1 * s;
acceleration_of_free_fall g = 9.81 * m / s2;
height h = 1 * m;
speed v = 1 * m / s;
energy e = m * pow<2>(l) / pow<2>(t);                     // OK
potential_energy ep1 = e;                                 // should not compile
potential_energy ep2 = static_cast<potential_energy>(e);  // OK
potential_energy ep3 = m * g * h;                         // OK
kinetic_energy ek1 = m * pow<2>(v) / 2;                   // OK
kinetic_energy ek2 = ep3 + ek1;                           // should not compile
mechanical_energy me = ep3 + ek1;                         // OK
```

Yet another example comes from the audio industry. In the audio software, we want to treat specific counts (e.g., *beats*, *samples*) as separate quantities. We could assign dedicated base dimensions to them. However, if we divide them by *duration*, we should obtain a quantity convertible to *frequency* and even be able to express the result in a unit of `Hz`. With the dedicated dimensions approach, this wouldn’t work as the dimension of frequency is just \(T^{-1}\), which would not match the results of our dimensional equations. This is why we can’t assign dedicated dimensions to such counts.

The last example that we want to mention here comes from finance. This time, we need to model *currency volume* as a special quantity of *currency*. *currency volume* can be obtained by multiplying *currency* by the dimensionless *market quantity*. Of course, both *currency* and *currency volume* should be expressed in the same units (e.g., USD).

None of the above scenarios can be addressed with just units and dimensions. We need a better abstraction to safely implement them.

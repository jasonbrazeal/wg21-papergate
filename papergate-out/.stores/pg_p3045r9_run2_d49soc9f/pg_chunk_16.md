Please note that some quantities may be specified by [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html) as vector or tensor quantities (e.g., `displacement`).

#### 16.1.3 Converting between quantities of the same kind

Quantity conversion rules can be defined based on the same hierarchy of quantities of kind length.

1. **Implicit conversions**
   - Every *width* is a *length*.
   - Every *radius* is a *width*.

   ```cpp
   static_assert(implicitly_convertible(isq::width, isq::length));
   static_assert(implicitly_convertible(isq::radius, isq::length));
   static_assert(implicitly_convertible(isq::radius, isq::width));
   ```

   Implicit conversions are allowed on copy-initialization:

   ```cpp
   void foo(quantity<isq::length[m]> q);
   ```

   ```cpp
   quantity<isq::width[m]> q1 = 42 * m;
   quantity<isq::length[m]> q2 = q1;  // implicit quantity conversion
   foo(q1);                           // implicit quantity conversion
   ```
2. **Explicit conversions**
   - Not every *length* is a *width*.
   - Not every *width* is a *radius*.

   ```cpp
   static_assert(!implicitly_convertible(isq::length, isq::width));
   static_assert(!implicitly_convertible(isq::length, isq::radius));
   static_assert(!implicitly_convertible(isq::width, isq::radius));
   static_assert(explicitly_convertible(isq::length, isq::width));
   static_assert(explicitly_convertible(isq::length, isq::radius));
   static_assert(explicitly_convertible(isq::width, isq::radius));
   ```

   Explicit conversions are forced by passing the quantity to a call operator of a `quantity_spec` type or by calling `quantity`’s explicit constructor::

   ```cpp
   void foo(quantity<isq::height[m]> q);
   ```

   ```cpp
   quantity<isq::length[m]> q1 = 42 * m;
   quantity<isq::height[m]> q2 = isq::height(q1);  // explicit quantity conversion
   quantity<isq::height[m]> q3(q1);                // direct initialization
   foo(isq::height(q1));                           // explicit quantity conversion
   ```
3. **Explicit casts**
   - *height* is never a *width*, and vice versa.
   - Both *height* and *width* are quantities of kind *length*.

   ```cpp
   static_assert(!implicitly_convertible(isq::height, isq::width));
   static_assert(!explicitly_convertible(isq::height, isq::width));
   static_assert(castable(isq::height, isq::width));
   ```

   Explicit casts are forced with a dedicated `quantity_cast` function:

   ```cpp
   void foo(quantity<isq::height[m]> q);
   ```

   ```cpp
   quantity<isq::width[m]> q1 = 42 * m;
   quantity<isq::height[m]> q2 = quantity_cast<isq::height>(q1);  // explicit quantity cast
   foo(quantity_cast<isq::height>(q1));                           // explicit quantity cast
   ```
4. **No conversion**
   - *time* has nothing in common with *length*.

   ```cpp
   static_assert(!implicitly_convertible(isq::time, isq::length));
   static_assert(!explicitly_convertible(isq::time, isq::length));
   static_assert(!castable(isq::time, isq::length));
   ```

   Even the explicit casts will not force such a conversion:

   ```cpp
   void foo(quantity<isq::length[m]>);
   ```

   ```cpp
   quantity<isq::length[m]> q1 = 42 * s;    // Compile-time error
   foo(quantity_cast<isq::length>(42 * s)); // Compile-time error
   ```

#### 16.1.4 Comparing, adding, and subtracting quantities of the same kind

[[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) explicitly states that *width* and *height* are quantities of the same kind and as such they:

- are mutually comparable, and
- can be added and subtracted.

If we take the above for granted, the only reasonable result of `1 * width + 1 * height` is `2 * length`, where the result of `length` is known as a common quantity type. A result of such an equation is always the first common node in a hierarchy tree of the same kind. For example:

```cpp
static_assert((isq::width(1 * m) + isq::height(1 * m)).quantity_spec == isq::length);
static_assert((isq::thickness(1 * m) + isq::radius(1 * m)).quantity_spec == isq::width);
static_assert((isq::distance(1 * m) + isq::path_length(1 * m)).quantity_spec == isq::path_length);
```

One could argue that allowing to add or compare quantities of *height* and *width* might be a safety issue, but we need to be consistent with the requirements of [[ISO/IEC 80000]](https://www.iso.org/standard/76921.html). Moreover, from our experience, disallowing such operations and requiring an explicit cast to a common quantity in every single place makes the code so cluttered with casts that it nearly renders the library unusable.

Fortunately, the above-mentioned conversion rules make the code safe by construction anyway. Let’s analyze the following example:

```cpp
inline constexpr struct horizontal_length : quantity_spec<isq::length> {} horizontal_length;

namespace christmas {

struct gift {
  quantity<horizontal_length[m]> length;
  quantity<isq::width[m]> width;
  quantity<isq::height[m]> height;
};

std::array<quantity<isq::length[m]>, 2> gift_wrapping_paper_size(const gift& g)
{
  quantity dim1 = 2 * g.width + 2 * g.height + 0.5 * g.width;
  quantity dim2 = g.length + 2 * 0.75 * g.height;
  return { dim1, dim2 };
}

}  // namespace christmas

int main()
{
  const christmas::gift lego = { horizontal_length(40 * cm), isq::width(30 * cm), isq::height(15 * cm) };
  auto paper = christmas::gift_wrapping_paper_size(lego);

  std::cout << "Paper needed to pack a lego box:\n";
  std::cout << "- " << paper[0] << " X " << paper[1] << "\n";  // - 1.05 m X 0.625 m
  std::cout << "- area = " << paper[0] * paper[1] << "\n";     // - area = 0.65625 m²
}
```

In the beginning, we introduce a custom quantity `horizontal_length` of a kind *length*, which then, together with `isq::width` and `isq::height`, are used to define the dimensions of a Christmas gift. Next, we provide a function that calculates the dimensions of a gift wrapping paper with some wraparound. The result of both those expressions is a quantity of `isq::length`, as this is the closest common quantity for the arguments used in this quantity equation.

Regarding safety, it is important to mention here, that thanks to the conversion rules provided above, it would be impossible to accidentally do the following:

```cpp
void foo(quantity<horizontal_length[m]> q);

quantity<isq::width[m]> q1 = dim1;  // Compile-time error
quantity<isq::height[m]> q2{dim1};  // Compile-time error
foo(dim1);                          // Compile-time error
```

The reason of compilation errors above is the fact that `isq::length` is not implicitly convertible to the quantities defined based on it. To make the above code compile, an explicit conversion of a quantity type is needed:

```cpp
void foo(quantity<horizontal_length[m]> q);

quantity<isq::width[m]> q1 = isq::width(dim1);
quantity<isq::height[m]> q2{isq::height(dim1)};
foo(horizontal_length(dim1));
```

To summarize, rules for addition, subtraction, and comparison of quantities improve the library usability, while the conversion rules enhance the safety of the library compared to the libraries that do not model quantity kinds.

#### 16.1.5 Hierarchies of derived quantities

The same rules propagate to derived quantities. For example, we can define strongly typed horizontal length and area:

```cpp
inline constexpr struct horizontal_length : quantity_spec<isq::length> {} horizontal_length;
inline constexpr struct horizontal_area : quantity_spec<isq::area, horizontal_length * isq::width> {} horizontal_area;
```

The first definition says that a `horizontal_length` is a more specialized quantity than `isq::length` and belongs to the same quantity kind. The second line defines a `horizontal_area`, which is a more specialized quantity than `isq::area`, so it has a more constrained recipe as well. Thanks to that:

```cpp
static_assert(implicitly_convertible(horizontal_length, isq::length));
static_assert(!implicitly_convertible(isq::length, horizontal_length));
static_assert(explicitly_convertible(isq::length, horizontal_length));

static_assert(implicitly_convertible(horizontal_area, isq::area));
static_assert(!implicitly_convertible(isq::area, horizontal_area));
static_assert(explicitly_convertible(isq::area, horizontal_area));

static_assert(implicitly_convertible(isq::length * isq::length, isq::area));
static_assert(!implicitly_convertible(isq::length * isq::length, horizontal_area));
static_assert(explicitly_convertible(isq::length * isq::length, horizontal_area));

static_assert(implicitly_convertible(horizontal_length * isq::width, isq::area));
static_assert(implicitly_convertible(horizontal_length * isq::width, horizontal_area));
```

Unfortunately, derived quantity equations often do not automatically form a hierarchy tree. This is why sometimes it is not obvious what such a tree should look like. Also, the [[ISO/IEC Guide 99]](https://www.iso.org/obp/ui#iso:std:iso-iec:guide:99) explicitly states:

> The division of ‘quantity’ according to ‘kind of quantity’ is, to some extent, arbitrary.

The below presents some arbitrary hierarchy of derived quantities of kind *energy*:

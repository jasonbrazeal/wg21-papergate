
```cpp
constexpr struct room_reference_temp : relative_point_origin<point<deg_C>(21)> {} room_reference_temp;
using room_temp = quantity_point<isq::Celsius_temperature[deg_C], room_reference_temp>;

constexpr auto step_delta = delta<isq::Celsius_temperature[deg_C]>(0.5);
constexpr int number_of_steps = 6;

room_temp room_ref{};
room_temp room_low = room_ref - number_of_steps * step_delta;
room_temp room_high = room_ref + number_of_steps * step_delta;

auto std_ref = room_ref.point_for(si::ice_point);
std::println("Room reference temperature: {} ({}, {::N[.2f]})\n",
             std_ref, std_ref.in(deg_F), std_ref.in(K));

std::println("| {:<18} | {:^18} | {:^18} | {:^18} |",
             "Temperature delta", "Room reference", "Ice point", "Absolute zero");
std::println("|{0:=^20}|{0:=^20}|{0:=^20}|{0:=^20}|", "");

auto print_temp = [&](std::string_view label, auto v) {
  std::println("| {:<18} | {:^18} | {:^18} | {:^18:N[.2f]} |", label,
               v - room_reference_temp, (v - si::ice_point).in(deg_C), (v - si::absolute_zero).in(deg_C));
};

print_temp("Lowest", room_low);
print_temp("Default", room_ref);
print_temp("Highest", room_high);
```

The above prints:

```
Room reference temperature: 21 ℃ (69.8 ℉, 294.15 K)

| Temperature delta  |   Room reference   |     Ice point      |   Absolute zero    |
|====================|====================|====================|====================|
| Lowest             |       -3 ℃        |       18 ℃        |     291.15 ℃      |
| Default            |        0 ℃        |       21 ℃        |     294.15 ℃      |
| Highest            |        3 ℃        |       24 ℃        |     297.15 ℃      |
```

More about temperatures can be found in the [Potential surprises while working with temperatures] chapter.

### 11.4 User-defined representation types

The library should work with any representation type for:

- Improved safety (overflow prevention, range restrictions).
- Additional information (measurement uncertainty).
- Linear algebra support.

By default, floating-point and integral types (except `bool`) are treated as real scalars.

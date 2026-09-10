# What the paper offers

## why it matters: supported with specifics
> Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

## who is affected: supported with specifics
> The Teachability chapter includes audience tables (following [[P1700R0]](https://wg21.link/p1700r0)) that map library features to four distinct user populations: Application Developers (millions), Unit Authors (tens of thousands), Domain Modelers (thousands), and Deep Integrators (hundreds).

## prior art and alternatives: supported with specifics
> [[Boost.Units]](https://www.boost.org/doc/libs/1_83_0/doc/html/boost_units.html) claims the answer to be 2 Hz (bauds not supported), [[nholthaus/units]](https://github.com/nholthaus/units) claims it is 2 s<sup>-1</sup> (bauds not supported), [[Pint]](https://pint.readthedocs.io/en/stable/index.html) library in Python claims the result is 3.0 Hz, [[JSR 385]](https://unitsofmeasurement.github.io/indriya) library in Java throws an exception

## why the standard: supported with specifics
> However, [[mp-units]](https://mpusz.github.io/mp-units) is the only C++ library implementing quantity kind safety (level 4) and quantity safety (level 5), making it uniquely comprehensive in its safety guarantees.

## coordination and interoperability: supported with specifics
> If Lockheed Martin and NASA could have used standardized vocabulary types in their interfaces, maybe they would not interpret pound-force seconds as newton seconds, and the [[Mars Orbiter]](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) would not have crashed during the Mars orbital insertion maneuver.

## why a library will not do: supported with specifics
> `std::ratio` fails these requirements: - Integral types too small for eight SI prefixes - Not closed under rational powers (e.g., \(\sqrt{2}\)) - Cannot represent irrational factors like \(\pi\) - Vulnerable to overflow when raised to powers

## implementation experience: supported with specifics
> Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

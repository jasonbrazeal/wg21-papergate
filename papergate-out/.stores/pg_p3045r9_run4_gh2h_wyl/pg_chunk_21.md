## 18 Core Library Framework scope

After a rough introduction of most of the features and abstractions in the library, it might be good to discuss the scope for the Core Library Framework.

We have several significant features to consider here:

- **Core library**: `quantity`, symbolic expressions, dimensions, units, references, and concepts for them,
- **Quantity kinds**: support quantities of the same dimension that should be distinct, e.g., *frequency*, *activity*, and *modulation_rate*, or *energy* and *moment_of_force*
- **Various quantities of the same kind**: support quantities of the same kind that should be distinct, e.g., *width*, *height*, *wavelength* (all of the kind *length*),
- **The affine space**: `quantity_point`, point origins, and concepts for them,
- **Text output**: for `quantity`, units, and dimensions,

Please note that the above only lists the features present in this proposal. Additional features, like definitions of specific systems of quantities and units, math utilities, and other extensions, may be provided in the follow-up papers. We chose not to include those features here because they can be separately added later. This also means that we believe that all of the features listed above should be provided in the first release of the library.

To prove that, let’s try to identify possible problems if a specific feature is excluded from the MVP scope:

1. **Core library**

   It just has to be there with all of the components listed. Otherwise, nothing works.
2. **Quantity kinds**

   If we remove this feature, we would not be able to make a distinction between `Hz`, `Bq`, and `Bd`, or `rad`, `sr` and `bit`, or `Gy` and `Sv` as the quantities associated with those units have the same dimensions. It is not only about units. It also means that we will be able to pass a quantity of *solid angular measure* to a function that takes `angular measure`. Users will also not be able to model their own distinct abstractions like we showed in the case of the audio example (samples, beats, etc.). We also need to note that we need that feature to be able to model the International System of Quantities (ISQ). Skipping it is a serious usability and safety issue that we should prevent.

   Deciding to postpone this feature will block us from providing proper SI definitions, as the units of this system should be properly constrained for specific quantity kinds (possibly of the same dimension).
3. **Various quantities of the same kind**

   Production feedback confirms this is a groundbreaking feature preventing critical bugs: warehouse robots misinterpreting box dimensions, flight computers passing *forward velocity* to *sink rate* parameters, or *kinetic energy* substituting for *potential energy*.

   Beyond convertibility, hierarchies validate derived quantity construction: *kinetic energy* cannot implicitly convert from `m g h` (recipe for *gravitational potential energy*). This validates correct ingredients in quantity equations.

   Without hierarchies, we cannot:
   - Distinguish specific *lengths* (*width*, *height*, *radius*), *energies* (*kinetic*, *potential*, *thermal*, *enthalpy*), or custom dimensions
   - Validate specific *energy* ingredients (e.g., *height* for *gravitational potential energy*)
   - Separate *plane angle* (radian) from *solid angle* (steradian) in dimensionless hierarchy
   - Discriminate between ratios, storage capacities, or algorithmic complexities
   - Support quantity characters (scalar vs. vector operations, character-specific operations)
   - Enforce correct units for different *power* types (`W` vs `VA` vs `var` in AC circuits)
   - Model physical systems like *water head*, *mass density* specializations, or audio examples (samples, beats, sounds)
   - Provide strongly-typed counts extending the dimensionless tree without custom dimension overhead

   **Removing quantity hierarchies eliminates quantity-safety entirely**, reducing the library to basic dimensional analysis. Postponing affects SI system modeling irreversibly—SI units provided without quantity specifications cannot be improved later. ISQ modeling becomes impossible.
4. **The affine space**

   This looks like a feature that can be added later, and it is partially true. However, the lack of this feature will prevent us from modeling temperatures correctly, which means that we will have big problems defining SI units as the degree Celsius unit needs an offset to kelvin. If we postpone and release SI first, then we will not be able to improve the degree Celsius definition later on.

   Skipping this feature also means that we will lack very important building block in modeling many problems in engineering. Those abstractions are considered so important that the BSI (British Standards Institution) already voted that they would strongly oppose a library not having this feature.

   Also, without it, we will not be able to provide proper `std::chrono` compatibility.
5. **Text output**

   Again, this looks like a purely additive feature, but if we never decide to standardize it, then all the symbols provided in unit and dimension definitions will be useless. If we do not intend to have text output, we should remove symbol text from the core framework class templates. This is why we should take that decision now.

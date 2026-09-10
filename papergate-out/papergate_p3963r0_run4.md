Verdict: Strong (10/14)

The paper offers a mixed case for standardization, with concrete grounding in the technical obstacle posed by `movable-box` and some vendor engagement, but it leaves key parts of the argument—especially the claimed necessity of a language change and the expected implementation burden—largely asserted rather than demonstrated.

- The strongest support comes from the specific identification of `movable-box` and its non-trivial copy/move assignment as the library-level blocker for trivially copyable views.
- The paper also benefits from reported conversations with NVIDIA and compiler implementors, indicating some external awareness and preliminary confidence in feasibility.
- The thinnest support is the claim that this “defeats the whole purpose of lambda expressions,” which is presented as self-evident without connecting the ergonomic complaint to a standards-level requirement.
- Most glaringly, the implementation experience section admits no implementation exists yet, leaving the practical risk and design validation entirely unsubstantiated.

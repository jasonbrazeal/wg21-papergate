Verdict: Strong (8/14)

The paper offers a reasonably clear account of the mismatch between the standardized partial ordering rule and widespread implementation behavior, but it leans heavily on a small set of observations that are not developed into full evidence. The thinnest parts concern why standardization is the only viable remedy, what library or non-normative alternatives were considered, and whether the claimed existing practice is stable enough to codify.

- The strongest support is the concrete documentation of CWG 1395 and the divergence among EDG, GCC, Clang, and MSVC, which makes the current specification’s impracticality credible.
- The paper also gives useful prior art by identifying the specific issue resolution it proposes to revisit and the direction of the intended change.
- What remains most underdeveloped is the justification that this requires a core language change rather than guidance, defect-report refinement, or some other response.
- The implementation experience is asserted rather than demonstrated, with no sustained evidence about bug frequency, user impact, or real-world code patterns beyond a passing reference.

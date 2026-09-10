# What the paper offers

## why it matters: supported with specifics
> Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.

## who is affected: not addressed

## prior art and alternatives: supported with specifics
> The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”.

## why the standard: not addressed
> While not sufficient in itself to make C++ safer, the change proposed in this paper is a necessary building block for technology such as the above which can greatly improve the security of C++ applications.

## coordination and interoperability: not addressed

## why a library will not do: supported with specifics
> However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.

## implementation experience: asserted, with nothing supporting it
> Based on implementation experience

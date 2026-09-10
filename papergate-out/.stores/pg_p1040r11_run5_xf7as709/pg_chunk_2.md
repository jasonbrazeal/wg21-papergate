## 6. Design Decisions

`<embed>` avoids using the preprocessor or defining new string literal syntax like its predecessors, preferring the use of a free function in the `std` namespace. This gives `std::embed` a greater degree of power and advantage over `#embed`’s design is derived heavily from community feedback plus the rejection of the prior art up to this point, as well as the community needs demonstrated by existing practice and their pit falls.

### 6.1. Primary Benefit: Recursive Processing and Composable String File Names

One of the biggest benefits of `std::embed` is that it’s a normal, regular `consteval` function call. This means that when processing data, it can be called recursively after reading the data from inside of the embedded file. This allows someone much greater degrees of freedom and power than is capable with either `#embed` or `_Pragma("embed ...")`, as it allows someone to use other constant expression parsing facilities along the introduction of file-based data. Among the primary use cases for this are:

- the ability to embed data recursively, such as processing sister language’s that have their own `#include` or `import` statements like CG, HLSL, GLSL, etc.
- and, the ability to respond to the contents of the data and perform other compile-time data processing, such as search for certain records or performing deserialization or serialization.

Such behaviors can also be combined with the approach `meta` and Reflection facilities that are coming to C++, which would also allow for generative reflection in a set of files determined at constant evaluation time (rather than a fixed set at preprocessing time). This would enable to do things such as enable the generation of C++ code from data files or other languages, such as automatic binding layers to Lua tables/functions, Python objects/scripts/modules, and other robust integrations (such as Rust, JavaScsript, etc.). Many of these languages have `require`, `include`, `import`, or other things which require multi-file coordination that `#embed` cannot handle.

This benefit has been discussed since the [November 2019 Belfast C++ Meeting](https://thephd.dev/_presentations/standards/C++/2019%20November%20Belfast/p1040/P1040%20-%20std%20embed.html) and at no point was it ever unambiguous what the fully-intentional reason for this proposal was:

## 2 UTF Primer

If you’re already familiar with Unicode, you can skip this section.

The Unicode standard maps *abstract characters* to *code points* in the *Unicode codespace* from `0` to `0x10FFFF`. Unicode text forms a *coded character sequence*, “an ordered sequence of one or more code points.” [[Definitions]](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G2212)

The simplest way of encoding code points is UTF-32, which encodes code points as a sequence of 32-bit unsigned integers. The building blocks of an encoding are *code units*, and UTF-32 has the most direct mapping between code points and code units.

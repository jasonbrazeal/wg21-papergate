
Any values greater than `0x10FFFF` are rejected by validators for being outside the range of valid Unicode.

Next is UTF-16, which exists for the historical reason that the Unicode codespace used to top out at `0xFFFF`. Code points outside this range are represented using *surrogates*, a reserved area in codespace which allows combining the low 10 bits of two code units to form a single code point.

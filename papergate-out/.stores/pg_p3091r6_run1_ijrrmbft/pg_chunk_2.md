## 8 Wording

This wording is relative to the July 2025 working draft, [[N5014]](https://wg21.link/n5014).

### 8.1 Feature-Test Macros

To the list in 17.3.2 [[version.syn]](https://wg21.link/N5014#version.syn)<sup>1</sup>, add:

> `#define __cpp_lib_map_lookup yyyymmL // also in <map>, <unordered_map>, <flat_map>`

### 8.2 `std::map` Changes

In 23.4.3.1 [[map.overview]](https://wg21.link/N5014#map.overview)/2, insert the `lookup` element-access members:

> //
> 
> 23.4.3.3
> [[map.access]](https://wg21.link/N5014#map.access),
> element access
> 
> constexpr mapped_type& operator[](const key_type& x);
> 
> constexpr mapped_type& operator[](key_type&& x);
> 
> template<class K> constexpr mapped_type& operator[](K&& x);
> 
> constexpr mapped_type&       at(const key_type& x);
> 
> const constexpr mapped_type& at(const key_type& x) const;
> 
> template<class K> constexpr mapped_type&       at(const K& x);
> 
> template<class K> const constexpr mapped_type& at(const K& x) const;
> 
> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

At the end of 23.4.3.3 [[map.access]](https://wg21.link/N5014#map.access), add these descriptions:

> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

> > *Constraints*: For the third and fourth overloads, the *qualified-id* `Compare::is_transparent` is valid and denotes a type.

> > *Preconditions*: The expression `find(x)` is well-formed and has well-defined behavior.

> > *Returns*: `find(x)->second` if `contains(x)` is `true` , otherwise `nullopt` .

> > *Complexity*: Logarithmic.

### 8.3 `std::unordered_map` Changes

In 23.5.3.1 [[unord.map.overview]](https://wg21.link/N5014#unord.map.overview)/3, insert the `lookup` element-access members:

> //
> 
> 23.5.3.3
> [[unord.map.elem]](https://wg21.link/N5014#unord.map.elem),
> element access
> 
> constexpr mapped_type& operator[](const key_type& x);
> 
> constexpr mapped_type& operator[](key_type&& x);
> 
> template<class K> constexpr mapped_type& operator[](K&& x);
> 
> constexpr mapped_type&       at(const key_type& x);
> 
> const constexpr mapped_type& at(const key_type& x) const;
> 
> template<class K> constexpr mapped_type&       at(const K& x);
> 
> template<class K> const constexpr mapped_type& at(const K& x) const;
> 
> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

At the end of 23.5.3.3 [[unord.map.elem]](https://wg21.link/N5014#unord.map.elem), add these descriptions:

> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

> > *Constraints*: For the third and fourth overloads, the *qualified-id*s `Hash::is_transparent` and `Pred::is_transparent` are valid and denote types.

> > *Preconditions*: The expression `find(x)` is well-formed and has well-defined behavior.

> > *Returns*: `find(x)->second` if `contains(x)` is `true` , otherwise `nullopt` .

> > *Complexity*: Average case constant, worst case linear in `size()` .

> > > **Editorial Note to LWG**: The *Complexity* clause is technically redundant because the return value is specified in terms of `find` . I added it here to match the format of `map::lookup` , which in turn matches the format of `map::at` . However, *Complexity* is currently missing for two of the overloads of `unordered_map::at` that are *not* specified in terms if `find` . Should that be an LWG issue?

### 8.4 `std::flat_map` Changes

In 23.6.8.2 [[flat.map.defn]](https://wg21.link/N5014#flat.map.defn), insert the `lookup` element-access members:

> //
> 
> 23.6.8.6
> [[flat.map.access]](https://wg21.link/N5014#flat.map.access)
> 
> ,
> element access
> 
> constexpr mapped_type& operator[](const key_type& x);
> 
> constexpr mapped_type& operator[](key_type&& x);
> 
> template<class K> constexpr mapped_type& operator[](K&& x);
> 
> constexpr mapped_type& at(const key_type& x);
> 
> constexpr const mapped_type& at(const key_type& x) const;
> 
> template<class K> constexpr mapped_type& at(const K& x);
> 
> template<class K> constexpr const mapped_type& at(const K& x) const;
> 
> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

At the end of 23.6.8.6 [[flat.map.access]](https://wg21.link/N5014#flat.map.access), add these descriptions:

**Editorial Note to LWG**: The following description is character-for-character identical to that of `map::lookup` . The same is true for the existing descriptions of `operator[]` and `at` . Consider moving all of these descriptions into 23.2.7.1 [[associative.reqmts.general]](https://wg21.link/N5014#associative.reqmts.general) and, for consistency, move the `unordered_map` versions into 23.2.8.1 [[unord.req.general]](https://wg21.link/N5014#unord.req.general). **Resolution**: LWG agrees, but there should be a separate paper, as there is a sizable set of similar functions for which this change should be made.

> constexpr optional<mapped_type&>       lookup(const key_type& x);
> 
> constexpr optional<const mapped_type&> lookup(const key_type& x) const;
> 
> template<class K> constexpr optional<mapped_type&>       lookup(const K& x);
> 
> template<class K> constexpr optional<const mapped_type&> lookup(const K& x) const;

> > *Constraints*: For the third and fourth overloads, the *qualified-id* `Compare::is_transparent` is valid and denotes a type.

> > *Preconditions*: The expression `find(x)` is well-formed and has well-defined behavior.

> > *Returns*: `find(x)->second` if `contains(x)` is `true` , otherwise `nullopt` .

> > *Complexity*: Logarithmic.


## 9 Acknowledgments

Thanks to Tomasz Kamiński for pushing me on the `optional<T&>` approach.

Thanks to Steve Downey for working with me to harmonize P2988 and P1255 with this paper.

Thanks to Lori Hughes for editing support.


## 10 References

[Folly] Meta. folly/folly/MapUtil.h.

https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71

[N5008] Thomas Köppe. 2025-03-15. Working Draft, Programming Languages —
C++.

https://wg21.link/n5008

[N5014] Thomas Köppe. 2025-08-05. Working Draft, Standard for
Programming Language C++.

https://wg21.link/n5014

[P1255] Steve Downey. A view of 0 or 1 elements:

views::nullable

And a concept to constrain

maybe

s.

http://wg21.link/P1255

[P2988R12] Steve Downey, Peter Sommerlad. 2025-04-04.
std::optional<T&>.

https://wg21.link/p2988r12

[P2988R4] Steve Downey, Peter Sommerlad. 2024-04-16.
std::optional<T&>.

https://wg21.link/p2988r4

[P2988R7] Steve Downey, Peter Sommerlad. 2024-09-10.
std::optional<T&>.

https://wg21.link/p2988r7

[P3091R0] Pablo Halpern. 2024-02-06. Better lookups for `map` and
`unordered_map`.

https://wg21.link/p3091r0

[P3091R2] Pablo Halpern. 2024-05-22. Better lookups for `map` and
`unordered_map`.

https://wg21.link/p3091r2

[P4139R2] Nathan Myers, Pablo Halpern. 2026-05-09. Better Name for
Better Lookups in P3091.

https://wg21.link/p4139r2

[P4139R3] Nathan Myers, Pablo Halpern. Better Name for Better Lookups in
P3091.

http://wg21.link/P4139R3

---

1. All citations to the Standard are to working draft N5014 unless otherwise specified.↩︎

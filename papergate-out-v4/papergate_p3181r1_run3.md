Verdict: Adequate (6/14)

The paper gives solid support for the motivating memory-model problem and for ruling out some alternative fixes, but it leaves several practical arguments as assertions rather than demonstrations. The thinnest areas are the lack of concrete evidence about affected hardware or users and the absence of implementation experience beyond a reference to Itanium.

- The strongest established point is the concrete happens-before failure in the relaxed-atomic-plus-fence pattern, which gives the paper a clear technical reason to exist.
- The discussion of alternatives is also well supported, particularly the rejection of changing happens-before itself and the acknowledgment that upgrading relaxed stores would be unacceptable.
- The paper claims, but does not establish, that real synchronization primitives create the interoperability and destruction-safety hazards it describes.
- The most glaring omission is implementation experience: the only named architecture said to require stronger relaxed-store ordering is Itanium, with no substantial evidence of current or realistic implementations affected by the proposed change.

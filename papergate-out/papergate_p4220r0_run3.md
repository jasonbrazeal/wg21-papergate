Verdict: Adequate (5/14)

The paper offers only a narrow slice of the evidence needed to justify standardization, resting almost entirely on one implementation’s retreat from the idea while leaving the core questions of purpose, need, and standard-library fit unanswered. The thinnest parts are the complete absence of any argument for why the standard should act, why a library solution is insufficient, or how the feature would coordinate with existing string and view facilities.

- The strongest support is the specific, cited observation that Microsoft’s GSL deprecated its dedicated C-string enforcement types after version 4.0.0, leaving only `zstring`.
- The paper gives no reason why the feature matters or what problem it would solve for users of the standard.
- It never addresses why the standard, rather than a library, is the right vehicle, and it skips coordination and interoperability considerations entirely.

Verdict: Strong (9/14)

The paper grounds its case in concrete design details and prior work, but it leaves several parts of the standardization argument unstated, particularly around affected users and implementation experience. The strongest support appears where the proposal ties its behavior to existing scheduler queries and acknowledges the limits of a library-only solution, while the thinnest support concerns who would benefit and whether the design has been tried in practice.

- The paper gives specific reasoning for why the standard library is the right home, noting that current scheduling operations may throw and that a library-only approach would struggle with that permission.
- It supports its design choices with references to the original `task` proposal and the use of `continues_on`, showing awareness of prior art.
- It explains the coordination requirement clearly by tying the affinity scheduler to the `get_scheduler` query on the receiver’s environment.
- It does not address who is affected by the proposal or provide any implementation experience, leaving the practical motivation and feasibility largely unsubstantiated.

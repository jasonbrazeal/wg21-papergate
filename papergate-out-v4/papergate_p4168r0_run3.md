Verdict: Strong (10/14)

The paper gives a reasonably solid account of the implementation landscape and the prior work, but it is thinner when it comes to showing who is concretely harmed and why the problem cannot be handled outside the standard. The strongest material concerns interoperability and existing practice, while the weakest concerns the affected audience and the impossibility of a library solution.

- The clearest support comes from the documented divergence among implementations and the fact that the proposed behavior is already shipping in two major standard libraries.
- The paper also does well to tie itself to prior LWG issues and earlier proposals, showing that this is an active and recognized defect area.
- The case for who is affected is asserted rather than demonstrated, with no real evidence of user impact beyond the existence of the inconsistency.
- The most glaring omission is the lack of an established argument for why a library cannot address the problem, since the cited Boost facility is presented as a working library alternative but not ruled out as a sufficient remedy.

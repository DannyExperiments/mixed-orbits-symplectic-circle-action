# Q1921: symplectic locally free circle action with mixed orbit contractibility

**Status:** affirmative for the dimension-unrestricted question as stated. In fact an example exists in every even dimension at least eight, with exceptional orbits of any prescribed finite order in the fundamental group. This proof does not decide the six-dimensional refinement mentioned in the source.

## Exact question and source

Rei Henigman and Yael Karshon, *Symplectic torus actions with non-contractible orbits*, [arXiv:2607.21159v1, Question 8.2, §8.1, printed and PDF p. 27](https://arxiv.org/pdf/2607.21159v1#page=27), ask for a non-Hamiltonian symplectic locally free circle action on a closed connected symplectic manifold “such that some but not all of its orbits are contractible?” Contractibility refers to the inclusion of the orbit, not the potentially many-to-one orbit map, as explained on p. 3 and in §3. The question imposes no dimension: the later sentence and Table 1 highlight the separate dimension-six case.

## Construction and proof

Fix m≥2 and let ζ = exp(2πi/m). By [Kotschick, Theorem 2](https://arxiv.org/pdf/math/0410243#page=1), there is a closed connected symplectic six-manifold (P,ω) with a free symplectic S¹-action all of whose circles are null-homotopic in P. Write R for rotation of the standard area sphere S² by angle 2π/m about the polar axis.

Form the quotient M = (P × S²)/C_m by the cyclic deck generator g(p,s)=(ζ·p,R(s)). The action of C_m on the product is free: its nonidentity powers act without fixed points on the P factor. It is symplectic for the sum of the two factor forms. Consequently the product form descends through the covering q:P×S²→M to a closed nondegenerate form, and M is closed, connected and eight-dimensional.

The first-factor circle action commutes with g, so it descends as t·q(p,s)=q(t·p,s). Its stabilizer at q(p,s) is exactly {ζ^j:R^j(s)=s}: the equality in the quotient requires t·p=ζ^j·p, which forces t=ζ^j by freeness upstairs. Off the two poles this is the trivial group; at either pole it is all of C_m. Thus the descended circle action is faithful, symplectic and locally free. A Hamiltonian of a circle action on a closed manifold must attain a maximum, at which the infinitesimal generator vanishes by nondegeneracy of the form. There are no fixed points here, so the action is not Hamiltonian.

For a nonpolar s, one circuit around the actual orbit downstairs is the projection of the full upstairs loop t↦(exp(2πit)·p,s), 0≤t≤1. This upstairs loop bounds a disk map in P×{s}, so the downstream orbit inclusion is null-homotopic.

For a pole s, instead one circuit around the actual orbit downstairs lifts from (p,s) to (ζ·p,s), along the path t↦(exp(2πit/m)·p,s). The endpoints differ. A null-homotopic loop would lift to a loop, so this orbit inclusion is not null-homotopic. In fact a power of the loop can only lift closed if its exponent is divisible by m, while its mth power lifts to the original full contractible loop. Its fundamental-group class therefore has order exactly m. This explains why all full S¹-parametrized orbit maps can be null-homotopic even when some actual orbit inclusions are not.

This gives the requested mixed contractibility. Taking the product with any number of symplectic spheres with trivial action raises the dimension by any even number; the cohomological and covering-space checks remain valid, or project to M to see that exceptional loops stay noncontractible.

## Source and prior-art audit (November 27, 2026 UTC)

- The [arXiv record](https://arxiv.org/abs/2607.21159) lists only v1. [Henigman's publications page](https://reihenigman.github.io/) identifies it as submitted and links that version; exact title/DOI searches did not locate a later version.
- Kotschick provides the free upstairs action, not mixed orbit types. Its products with trivial action still have only contractible orbits. The nontrivial diagonal *finite* quotient creates finite stabilizers while preserving a smooth symplectic total space; the distinct endpoints of the primitive orbit lift are the additional ingredient.
- Henigman–Karshon Lemma 3.1 only compares parametrized orbit maps and free orbits. Their Example 3.3 uses a smooth equivariant connected sum with fixed points, and Remark 3.6 explicitly observes that that example is not symplectic. Their Lemma 3.5 ensures Hamiltonian torus orbits are all contractible, not the present non-Hamiltonian case.
- Tested likely corollaries from finite quotients, Hamiltonian sphere rotations and known free actions: reparametrizing a known action or taking a direct product does not produce the required noncontractible inclusion, and taking a finite quotient along P alone makes the induced original circle action nonfaithful; quotienting the effective circle then leaves no mixture. The sphere rotation coupled to the deck action avoids both problems.
- Exact-phrase and synonym searches (mixed orbit contractibility, some but not all orbits, locally free symplectic circle action with finite stabilizers, diagonal quotient Kotschick sphere, Question 8.2 and arXiv ID) located no prior matching symplectic construction in checked sources. Not a certification of priority or peer review. Dimension six remains unanswered by this packet.


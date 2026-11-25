# From Proof Production to Knowledge Assimilation

### A Paradigm of Hierarchical Proofs and Cumulative Verification for Mathematics in the Age of AI

**Chunming LAI (赖俊铭)** · Independent Researcher  
[ORCID: 0009-0002-7594-4535](https://orcid.org/0009-0002-7594-4535) · [Contact](mailto:jimmybus0610@outlook.com)

## The challenge

AI may dramatically expand the production of mathematical proofs. Mathematical progress, however, requires more than correct conclusions: it requires the human understanding, verification, communication and reuse of mathematical knowledge.

This research initiative advocates a shift in research and publication practices, from the complete paper as the predominant unit of acceptance toward a network of locally examinable, independently reusable proof contributions.

## The proposed paradigm

Given a target theorem $T$, organize its new proof contributions into a finite directed acyclic dependency graph. For each node $v$, let $D(v)$ be its direct new dependencies relative to an existing theorem library.

$$
\ell(v)=\begin{cases}
0,& D(v)=\varnothing,\\
1+\max_{u\in D(v)}\ell(u),& D(v)\ne\varnothing.
\end{cases}
$$

The target's level is $r=\ell(T)$. Dependencies may cross levels; branches need not have equal depths, and several results may reuse the same lemma.

Human mathematicians can examine and verify local proofs from foundational results upward, add established contributions to shared theorem libraries, and reuse them in later proofs and research. The objective is individually manageable arguments, not an arbitrary limit on proof length.

The framework distinguishes formal correctness, semantic fidelity and mathematical understanding. It establishes logical properties of the dependency and accumulation model, while treating practical improvements in review efficiency as conditional and subject to investigation.

## A call to the mathematical community

We invite mathematicians, research institutions, journals, formalization communities and AI research groups to explore how existing tools and institutions can support hierarchical proof organization, local human understanding and cumulative acceptance of mathematical knowledge. The aim is not to replace mathematical papers or claim to invent existing theorem libraries or proof assistants.

The English position paper and its Chinese counterpart are being prepared for this repository's first public release.

## Research status and disclosure

This is a research and publication paradigm proposal, not a claim of independent peer review, formal verification of the manuscript, or established historical priority. The central concept and choice of bottom-up dependency height were supplied or confirmed by the author; ChatGPT assisted with formalization, analysis, literature research, examples, drafting and revision, as disclosed in the manuscript.

The manuscript is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

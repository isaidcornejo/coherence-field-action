# Fisher–Geometric Action — Computational Support

This directory contains the **computational components** used to support and illustrate the Fisher–geometric variational theory introduced in:

> **A Fisher–Geometric Action for the Isotropic Empirical Alignment Field**
> I. Cornejo (2025)

Unlike the earlier experimental suite dedicated to empirical diagnostics, this module focuses on the **geometric action**, the associated **Poisson equation on statistical manifolds**, and the generation of figures illustrating intrinsic Fisher–geometric relaxation.

---

## Geometric Setting

The theory promotes the isotropic empirical alignment diagnostic

**A(θ; q) = Tr(G⁻¹ C) − D**

to an auxiliary scalar field **φ(θ)** defined intrinsically on the statistical manifold Θ.

The minimal Fisher–geometric action yields the field equation:

**−Δ_G φ(θ) = −γ A(θ; q)**

where Δ_G denotes the Laplace–Beltrami operator associated with the Fisher–Rao metric **G**.

All code in this directory is organized around this geometric structure.

---

## Contents

### `figures/`

Code for generating the figures appearing in the paper, including:

* Schematic spectra of the alignment operator
* Solutions of the Fisher–geometric Poisson equation
* Visualization of geometric relaxation on canonical statistical manifolds (e.g. Gaussian family)

Figure generation is deterministic and fully reproducible.

---

### `utils/`

Reusable geometric utilities implementing:

* Fisher–Rao metric components
* Laplace–Beltrami operators on statistical manifolds
* Poisson solvers for scalar fields on curved parameter spaces
* Auxiliary normalization and consistency checks

These components are geometry-first and intentionally independent of any learning or optimization dynamics.

---

## Running the Figure Generation

All figures are generated via the top-level runner using module execution:

```bash
python -m src.run_figures
```

Outputs are written to:

```
paper/revtext/figures/
```

No empirical datasets, training loops, or stochastic optimization procedures are used in this module.

---

## Design Principles

* **Reparametrization invariance** is enforced throughout.
* **No geometric structure beyond Fisher–Rao** is introduced.
* The implementation is intentionally restricted to the **scalar (spin-0) sector**.
* The code reflects **static geometric relaxation**, not temporal or learning dynamics.

Extensions to anisotropic sectors or genuine alignment dynamics are intentionally left outside the scope of this directory.

---

## Relation to Other Repositories

This module complements the earlier **Coherence Field — Experimental Suite**, which focuses on empirical diagnostics and spectral alignment measurements.

Together, the two codebases form a conceptual pair:

* **Diagnostic** → empirical measurement of alignment
* **Action** → geometric regularization and variational completion

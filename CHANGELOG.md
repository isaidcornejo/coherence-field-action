# Changelog

All notable changes to this repository will be documented in this file.
The format follows *Keep a Changelog*, adapted for scientific research code
and reproducible geometric workflows.

---

## [1.0.0] – 2025-12-15

### Added

* **Initial public release** of the Fisher–geometric action framework for
  isotropic empirical alignment on statistical manifolds.

* **Complete variational formulation** of the alignment field:

  * Definition of the auxiliary scalar field φ(θ) on the statistical manifold.
  * Fisher–geometric action constructed solely from the Fisher–Rao metric.
  * Euler–Lagrange equation yielding a Poisson equation on the manifold.
  * Explicit treatment of zero modes, normalization, and global consistency.

* **Programmatic figure-generation pipeline** illustrating the theory:

  * Alignment-field screening and relaxation behavior.
  * Spectral structure of the alignment operator.
  * Explicit solutions on canonical statistical manifolds
    (e.g. univariate Gaussian family).

* **Geometry-focused computational utilities**:

  * Fisher–Rao metric handling.
  * Laplace–Beltrami operator construction.
  * Poisson solvers for scalar fields on curved parameter spaces.
  * Path and plotting helpers for reproducible figure generation.

* **Reproducible execution interface**:

  * Module-based execution via:
    ```bash
    python -m src.run_figures
    ```
  * Deterministic regeneration of all manuscript figures.

* **Structured RevTeX manuscript source**:

  * Sectioned LaTeX architecture under `paper/revtex/`.
  * Local bibliography and figure handling.
  * Versioned PDF archive under `paper_versions/v1/`.

* **Testing infrastructure**:

  * Pytest-based validation of figure generation and geometric utilities.
  * Ensures numerical stability and reproducibility.

* **Unified Makefile** enabling a full reproducible workflow:

  * `make test` — run test suite.
  * `make figures` — regenerate figures.
  * `make paper` — compile the manuscript.
  * `make all` — clean, test, generate figures, and compile.

* **Project metadata and reproducibility support**:

  * `environment.yml` for environment recreation.
  * `CITATION.cff` with concept DOI and citation metadata.
  * Repository-level README documenting scope, structure, and usage.

### Notes

* This release establishes the **static, scalar (spin-0) sector** of the
  Fisher–geometric alignment theory.
* No learning dynamics, temporal evolution, or anisotropic tensor sectors
  are implemented in this repository.
* The codebase is intended as a **foundational geometric layer**, enabling
  future work on alignment dynamics and higher-rank extensions.

---

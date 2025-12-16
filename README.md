# Fisher–Geometric Action for the Isotropic Empirical Alignment Field

This repository provides the full implementation, figure-generation pipeline, and manuscript for

**A Fisher–Geometric Action for the Isotropic Empirical Alignment Field**

which develops a **minimal variational formulation** for empirical alignment on statistical manifolds, grounded entirely in Fisher–Rao geometry.

It is designed as a **conceptual and technical continuation** of the earlier scalar diagnostic work, shifting the focus from pointwise measurement to **intrinsic geometric regularization via an action principle**.

The repository includes:

* A complete Fisher–geometric formulation of the alignment field.
* Programmatic generation of all figures appearing in the manuscript.
* A structured LaTeX manuscript (RevTeX) with versioned outputs.
* Geometry-focused utility modules (metrics, Laplace–Beltrami operators, Poisson solvers).
* A unified Makefile for reproducible testing, figure generation, and paper compilation.

---

## 📐 Core Idea

Empirical data generically deform the intrinsic Fisher–Rao geometry of statistical models. While such deformation can be quantified locally by invariant diagnostics, a static measure does not by itself provide a **global or variational mechanism** for geometric regularization.

This work promotes the isotropic component of empirical alignment to an auxiliary scalar field **φ(θ)** defined intrinsically on the statistical manifold Θ.

### Empirical source

```
A(θ; q) = Tr(G⁻¹ C) − D
```

### Fisher–geometric field equation

```
−Δ_G φ(θ) = −γ A(θ; q)
```

Where:

* **G** — Fisher–Rao metric
* **C** — empirical score covariance under data distribution *q*
* **Δ_G** — Laplace–Beltrami operator induced by *G*
* **D** — dimension of the statistical manifold

The resulting Poisson equation describes **intrinsic geometric relaxation** of empirical deformation, fully determined by Fisher geometry and reparametrization invariance.

---

## 📂 Repository Structure

```
coherence-action/
│
├─ paper/
│   └─ revtex/
│
├─ paper_versions/
│   └─ v1/
│
├─ src/
│   ├─ figures/
│   ├─ utils/
│   └─ run_figures.py
│
├─ tests/
│   ├─ figures/
│   ├─ utils/
│   └─ test_run_all_figures.py
│
├─ Makefile
├─ environment.yml
├─ pytest.ini
└─ README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/isaidcornejo/coherence-action.git
cd coherence-action
```

### 2. Create the environment

```bash
conda env create -f environment.yml
conda activate coherence-action
```

---

## 📊 Figure Generation

All figures appearing in the manuscript are generated programmatically from the Fisher–geometric construction.

Run:

```bash
python -m src.run_figures
```

Generated figures are written to:

```
paper/revtext/figures
```

The figure scripts illustrate:

* Screening and relaxation of empirical alignment fields
* Spectral structure of the alignment operator
* Explicit solutions on canonical statistical manifolds (e.g. univariate Gaussian family)

---

## 🧪 Testing

A pytest-based test suite validates:

* Figure generation stability
* Core geometric utilities
* Path and plotting consistency

Run tests with:

```bash
python -m pytest -q
```

---

## 📝 Paper Compilation

The main LaTeX entry point is:

```
paper/revtex/fisher-geometric-action.tex
```

To compile manually:

```bash
cd paper/revtex
latexmk -pdf fisher-geometric-action.tex
```

---

## 🛠️ Using the Makefile (Recommended)

Run the full reproducible pipeline:

```bash
make all
```

Available targets include:

* `make test` — run tests
* `make figures` — regenerate all figures
* `make paper` — compile the manuscript
* `make clean` — remove caches and temporary files

---

## 🔖 Citation

If you use this repository or build upon this framework, please cite:

```
Isaid Cornejo,
"A Fisher–Geometric Action for the Isotropic Empirical Alignment Field",
Information Physics Institute, 2025.
```

A Zenodo DOI is provided with the corresponding release.

---

## 📄 License

MIT License.

---

## 🔭 Outlook

This repository is intentionally restricted to the **static scalar (spin-0) sector** of empirical geometric deformation. The variational structure developed here provides a natural foundation for future work on:

* Alignment flows and geometric dynamics
* Diffusion-type processes on statistical manifolds
* Tensorial (anisotropic) extensions of empirical alignment

These directions are not implemented here but are conceptually enabled by the present construction.

---

## 📬 Contact

**Isaid Cornejo**
Information Physics Institute

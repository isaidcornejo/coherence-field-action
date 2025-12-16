# ============================================================
# Fisher–Geometric Action — Makefile
# Testing, figure generation, and paper compilation.
# ============================================================

PYTHON   = python
PYTEST   = python -m pytest -q
LATEXMK  = latexmk -pdf

# ------------------------------------------------------------
# Paper main file (RevTeX)
# ------------------------------------------------------------
REVTEX_MAIN = fisher-geometric-action.tex


# ------------------------------------------------------------
# Testing
# ------------------------------------------------------------
test:
	$(PYTEST)

test-verbose:
	python -m pytest


# ------------------------------------------------------------
# Figures
# ------------------------------------------------------------
figures:
	$(PYTHON) -m src.run_figures


# ------------------------------------------------------------
# Paper compilation
# ------------------------------------------------------------
paper:
	cd paper/revtex && $(LATEXMK) $(REVTEX_MAIN)


# ------------------------------------------------------------
# Cleanup LaTeX auxiliary files
# ------------------------------------------------------------
paper-clean:
	cd paper/revtex && $(LATEXMK) -C


# ------------------------------------------------------------
# Cleanup utilities (cross-platform, Python-based)
# ------------------------------------------------------------
clean:
	$(PYTHON) -c "import os, shutil; \
	[shutil.rmtree(os.path.join(r, d), ignore_errors=True) \
	for r, ds, _ in os.walk('.', topdown=False) for d in ds if d=='__pycache__']"

clean-figures:
	$(PYTHON) -c "import shutil; \
	shutil.rmtree('src/figures', ignore_errors=True)"


deep-clean: clean clean-figures paper-clean
	$(PYTHON) -c "import shutil; \
	shutil.rmtree('.pytest_cache', ignore_errors=True); \
	shutil.rmtree('.hypothesis', ignore_errors=True)"


# ------------------------------------------------------------
# Full reproducible pipeline
# ------------------------------------------------------------
all: clean test figures paper
	@echo "============================================================"
	@echo "   Fisher–Geometric Action — Full pipeline completed"
	@echo "============================================================"

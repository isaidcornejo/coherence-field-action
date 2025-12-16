"""
Spectrum of the Fisher-normalized alignment operator H = G^{-1} C.

This module generates a publication-quality figure illustrating the
eigenvalue spectrum of the Fisher-normalized alignment operator

    H = G^{-1} C,

where G is the Fisher–Rao metric and C is the empirical score covariance.
The eigenvalues λ_i quantify direction-wise empirical reinforcement
(λ_i > 1) or suppression (λ_i < 1) relative to Fisher geometry.

The figure shown here uses a synthetic representative spectrum intended
for conceptual and editorial illustration rather than empirical analysis.
"""

import numpy as np
import matplotlib.pyplot as plt

from src.utils.plotting import (
    setup_figure,
    finalize_figure,
    add_fisher_equilibrium_line,
)
from src.utils.paths import figure_paths_all_formats


def generate(formats=("revtext",)):
    """
    Generate the alignment-operator spectrum figure.

    The figure displays a discrete set of eigenvalues λ_i of the
    Fisher-normalized alignment operator H = G^{-1} C, together with
    a horizontal reference line at λ = 1 corresponding to Fisher
    equilibrium.

    Parameters
    ----------
    formats : tuple of str, optional
        Paper formats for which the figure should be generated.
        Each format corresponds to a subdirectory under ``paper/``.

    Notes
    -----
    - The spectrum shown is synthetic and representative.
    - The purpose of this figure is conceptual illustration, not
      quantitative inference.
    - Output is generated with standardized editorial settings and
      saved consistently across all requested formats.
    """

    # --- synthetic representative spectrum (editorial figure) ---
    lambdas = np.array([0.5, 1.0, 5.0])

    setup_figure()
    plt.plot(lambdas, "o")
    add_fisher_equilibrium_line(1.0)

    plt.xlabel("Mode index")
    plt.ylabel(r"Eigenvalue $\lambda_i$")

    for path in figure_paths_all_formats(
        "fig_alignment_operator_spectrum",
        formats=formats,
    ):
        finalize_figure(path, close=False)

    plt.close()

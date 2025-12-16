"""
Alignment field on the univariate Gaussian Fisher manifold.

This module generates a publication-quality figure illustrating the
alignment field φ(μ, σ) defined over the Fisher–Rao manifold of the
univariate Gaussian family, parametrized by mean μ and standard deviation σ.

The field shown is a smooth, synthetic illustration designed to convey
geometric structure rather than empirical estimation.
"""

import numpy as np
import matplotlib.pyplot as plt

from src.utils.plotting import setup_figure, finalize_figure
from src.utils.paths import figure_paths_all_formats


def generate(formats=("revtext",)):
    """
    Generate the alignment field over (μ, σ).

    The figure represents a smooth alignment field φ(μ, σ) defined on
    the univariate Gaussian Fisher manifold. A synthetic source term is
    introduced to illustrate spatial structure, and a screened response
    is computed to mimic geometric relaxation.

    Parameters
    ----------
    formats : tuple of str, optional
        Paper formats for which the figure should be generated.
        Each format corresponds to a subdirectory under ``paper/``.

    Notes
    -----
    - The field shown is synthetic and intended for editorial illustration.
    - No empirical data are involved.
    - Output is generated with standardized editorial settings and
      saved consistently across all requested formats.
    """

    mu = np.linspace(-3.0, 3.0, 200)
    sigma = np.linspace(0.5, 3.0, 200)
    MU, SIGMA = np.meshgrid(mu, sigma)

    # Smooth synthetic source (editorial illustration)
    A = np.exp(-MU**2) * np.exp(-(SIGMA - 1.0) ** 2)

    # Screened response
    m = 1.0
    phi = -A / (1.0 + m**2)

    setup_figure(width=5.5, height=4.0)
    cs = plt.contourf(MU, SIGMA, phi, levels=30)
    plt.colorbar(cs, label=r"$\phi(\mu,\sigma)$")

    plt.xlabel(r"$\mu$")
    plt.ylabel(r"$\sigma$")

    for path in figure_paths_all_formats(
        "fig_univariate_gaussian_alignment_field",
        formats=formats,
    ):
        finalize_figure(path, close=False)

    plt.close()

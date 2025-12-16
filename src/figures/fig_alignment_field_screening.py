"""
Geometric screening of the alignment field as a function of Fisher distance.

This module generates a publication-quality figure illustrating the
exponential screening behavior of the alignment field φ(d_G) as a function
of Fisher distance. The screening strength is controlled by a mass-like
parameter m.

The resulting figure is saved consistently across multiple paper formats
using the centralized path and plotting utilities.
"""

import numpy as np
import matplotlib.pyplot as plt

from src.utils.plotting import setup_figure, finalize_figure
from src.utils.paths import figure_paths_all_formats


def generate(formats=("revtext",)):
    """
    Generate the alignment-field screening figure.

    The figure displays exponential screening profiles of the form

        φ(d_G) = exp(-m d_G)

    for multiple values of the screening parameter m. The Fisher distance
    d_G is shown on the horizontal axis, and the alignment field amplitude
    φ on the vertical axis.

    Parameters
    ----------
    formats : tuple of str, optional
        Paper formats for which the figure should be generated.
        Each format corresponds to a subdirectory under ``paper/``.

    Notes
    -----
    - The figure is created using standardized editorial defaults.
    - Output is vector-safe (PDF) and resolution-enforced.
    - The same figure is saved into all requested paper formats.
    """
    d = np.linspace(0.0, 4.0, 300)
    m_values = [0.5, 1.0, 2.0]

    setup_figure()

    for m in m_values:
        phi = np.exp(-m * d)
        plt.plot(d, phi, label=rf"$m={m}$")

    plt.xlabel(r"Fisher distance $d_G$")
    plt.ylabel(r"Alignment field $\phi$")
    plt.legend(frameon=False)

    for path in figure_paths_all_formats(
        "fig_alignment_field_screening",
        formats=formats,
    ):
        finalize_figure(path, close=False)

    plt.close()

"""
Centralized figure-generation entry point for the paper.

This module provides a single orchestration function that generates
all publication figures in a consistent and reproducible manner across
supported paper formats.

It is intended to be used both programmatically (e.g. from CI or tests)
and as a standalone script.
"""

from src.figures.fig_alignment_operator_spectrum import generate as fig_spectrum
from src.figures.fig_alignment_field_screening import generate as fig_screening
from src.figures.fig_univariate_gaussian_alignment_field import generate as fig_gaussian

from src.utils.paths import SUPPORTED_FORMATS


def run_all(formats=None):
    """
    Generate all figures for the selected paper formats.

    Parameters
    ----------
    formats : iterable of str or None, optional
        Paper formats for which figures should be generated.
        If ``None``, all supported formats are used.

    Notes
    -----
    - This function acts as the canonical entry point for figure generation.
    - Each figure is generated using standardized plotting and path utilities.
    - Side effects are limited to filesystem output under ``paper/``.
    """
    if formats is None:
        formats = SUPPORTED_FORMATS

    fig_spectrum(formats=formats)
    fig_screening(formats=formats)
    fig_gaussian(formats=formats)


if __name__ == "__main__":
    run_all()

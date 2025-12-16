"""
Publication-quality Matplotlib utilities.

All figures are guaranteed to satisfy:
- minimum DPI: 300
- minimum linear resolution: 1200 px
- vector-safe output (PDF)
"""

import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# Editorial quality constraints
# ---------------------------------------------------------------------
MIN_DPI = 300
MIN_PIXELS = 1200


# ---------------------------------------------------------------------
# Figure creation
# ---------------------------------------------------------------------
def setup_figure(
    width: float = 5.5,
    height: float = 3.5,
    dpi: int = MIN_DPI,
):
    """
    Create a Matplotlib figure with editorial defaults.

    Parameters
    ----------
    width : float
        Figure width in inches.
    height : float
        Figure height in inches.
    dpi : int
        Dots per inch (minimum enforced).

    Returns
    -------
    matplotlib.figure.Figure
    """
    dpi = max(dpi, MIN_DPI)
    fig = plt.figure(figsize=(width, height), dpi=dpi)
    return fig


# ---------------------------------------------------------------------
# Resolution enforcement
# ---------------------------------------------------------------------
def ensure_min_resolution(fig, min_pixels: int = MIN_PIXELS):
    """
    Ensure that the figure has at least `min_pixels` on its longest side.

    This rescales the figure uniformly if needed.
    """
    width_px = fig.get_figwidth() * fig.get_dpi()
    height_px = fig.get_figheight() * fig.get_dpi()
    max_px = max(width_px, height_px)

    if max_px < min_pixels:
        scale = min_pixels / max_px
        fig.set_size_inches(
            fig.get_figwidth() * scale,
            fig.get_figheight() * scale,
        )


# ---------------------------------------------------------------------
# Saving
# ---------------------------------------------------------------------
def finalize_figure(
    path,
    fig=None,
    dpi: int = MIN_DPI,
    tight: bool = True,
    close: bool = True,
):
    """
    Finalize and save a figure with guaranteed editorial quality.

    Parameters
    ----------
    path : Path
        Output file path.
    fig : matplotlib.figure.Figure, optional
        Figure object (defaults to current figure).
    dpi : int
        Output DPI (minimum enforced).
    tight : bool
        Apply tight_layout before saving.
    close : bool
        Close figure after saving.
    """
    if fig is None:
        fig = plt.gcf()

    dpi = max(dpi, MIN_DPI)

    ensure_min_resolution(fig)

    if tight:
        fig.tight_layout()

    fig.savefig(
        path,
        dpi=dpi,
        bbox_inches="tight",
    )

    if close:
        plt.close(fig)


# ---------------------------------------------------------------------
# Small helpers (semantic, not stylistic)
# ---------------------------------------------------------------------
def add_fisher_equilibrium_line(y: float = 1.0):
    """
    Add a reference line corresponding to Fisher equilibrium.
    """
    plt.axhline(y, linestyle="--", linewidth=1.0)


def set_axis_labels(xlabel: str, ylabel: str):
    """
    Standardized axis labeling.
    """
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

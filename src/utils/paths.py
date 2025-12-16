"""
Filesystem utilities for canonical paper and figure paths.

This module defines a centralized, format-aware interface for resolving
paths to papers and generated figures within the repository. It is designed
to support multiple publication formats (e.g. RevTeX, MDPI) from a single
figure-generation pipeline.

All paths are resolved relative to the repository root and created lazily
when accessed.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Iterator


# ---------------------------------------------------------------------
# Repository root
# ---------------------------------------------------------------------
ROOT_DIR: Path = Path(__file__).resolve().parents[2]
"""
Absolute path to the repository root.

This is inferred dynamically from the location of this file, assuming
the standard repository layout:

    repo/
      ├─ src/
      │   └─ ...
      ├─ paper/
      └─ ...
"""


# ---------------------------------------------------------------------
# Paper root
# ---------------------------------------------------------------------
PAPER_DIR: Path = ROOT_DIR / "paper"
"""
Root directory containing all paper formats.
"""


# ---------------------------------------------------------------------
# Supported paper formats
# ---------------------------------------------------------------------
SUPPORTED_FORMATS: set[str] = {
    "revtext",
}
"""
Set of supported paper formats.

Each format corresponds to a subdirectory under `PAPER_DIR`.
"""


# ---------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------
def _paper_dir(format: str) -> Path:
    """
    Resolve the root directory for a given paper format.

    Parameters
    ----------
    format : str
        Paper format identifier (e.g. ``"revtext"``).

    Returns
    -------
    Path
        Path to the paper directory for the given format.

    Raises
    ------
    ValueError
        If the requested format is not supported.
    """
    if format not in SUPPORTED_FORMATS:
        raise ValueError(
            f"Unknown paper format '{format}'. "
            f"Supported formats: {sorted(SUPPORTED_FORMATS)}"
        )
    return PAPER_DIR / format


def figures_dir(format: str) -> Path:
    """
    Return (and create if necessary) the figures directory
    for a given paper format.

    Parameters
    ----------
    format : str
        Paper format identifier.

    Returns
    -------
    Path
        Path to the figures directory for the given format.

    Notes
    -----
    The directory is created with ``parents=True`` and
    ``exist_ok=True`` to ensure idempotent behavior.
    """
    path = _paper_dir(format) / "figures"
    path.mkdir(parents=True, exist_ok=True)
    return path


# ---------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------
def figure_path(
    name: str,
    *,
    format: str,
    ext: str = "pdf",
) -> Path:
    """
    Construct the canonical path for a figure file.

    Parameters
    ----------
    name : str
        Base figure name. Must start with ``"fig_"``.
    format : str
        Paper format identifier.
    ext : str, optional
        File extension (default: ``"pdf"``).

    Returns
    -------
    Path
        Full filesystem path to the figure file.

    Raises
    ------
    ValueError
        If the figure name does not start with ``"fig_"``.
    """
    if not name.startswith("fig_"):
        raise ValueError(
            "Figure names must start with 'fig_' "
            "(e.g. 'fig_alignment_operator_spectrum')"
        )

    return figures_dir(format) / f"{name}.{ext}"


def figure_paths_all_formats(
    name: str,
    *,
    ext: str = "pdf",
    formats: Iterable[str] | None = None,
) -> Iterator[Path]:
    """
    Yield figure paths for all or a selected subset of paper formats.

    This is useful when the same figure must be generated and saved
    consistently across multiple publication formats.

    Parameters
    ----------
    name : str
        Base figure name (must start with ``"fig_"``).
    ext : str, optional
        File extension (default: ``"pdf"``).
    formats : iterable of str or None, optional
        Iterable of format identifiers. If ``None``, all supported
        formats are used.

    Yields
    ------
    Path
        Canonical path for the figure in each format.
    """
    if formats is None:
        formats = SUPPORTED_FORMATS

    for fmt in formats:
        yield figure_path(name, format=fmt, ext=ext)

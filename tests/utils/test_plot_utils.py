"""
Tests for publication-quality Matplotlib utilities.

These tests verify DPI enforcement, resolution guarantees, saving behavior,
and basic semantic helpers without relying on visual inspection.
"""

import matplotlib
import matplotlib.pyplot as plt
import pytest
from pathlib import Path

from src.utils.plotting import (
    MIN_DPI,
    MIN_PIXELS,
    setup_figure,
    ensure_min_resolution,
    finalize_figure,
    add_fisher_equilibrium_line,
    set_axis_labels,
)


# ---------------------------------------------------------------------
# Global test configuration
# ---------------------------------------------------------------------
@pytest.fixture(autouse=True)
def use_headless_backend():
    """
    Force a non-interactive Matplotlib backend for tests.
    """
    matplotlib.use("Agg")


# ---------------------------------------------------------------------
# Figure creation
# ---------------------------------------------------------------------
def test_setup_figure_enforces_min_dpi():
    """
    setup_figure must enforce MIN_DPI even if a lower value is requested.
    """
    fig = setup_figure(dpi=72)

    assert fig.get_dpi() >= MIN_DPI
    plt.close(fig)


def test_setup_figure_dimensions():
    """
    setup_figure must respect requested physical dimensions.
    """
    fig = setup_figure(width=6.0, height=4.0)

    assert fig.get_figwidth() == pytest.approx(6.0)
    assert fig.get_figheight() == pytest.approx(4.0)
    plt.close(fig)


# ---------------------------------------------------------------------
# Resolution enforcement
# ---------------------------------------------------------------------
def test_ensure_min_resolution_scales_up_if_needed():
    """
    ensure_min_resolution must increase figure size if pixel resolution
    is below MIN_PIXELS.
    """
    fig = setup_figure(width=2.0, height=2.0, dpi=MIN_DPI)

    before = max(
        fig.get_figwidth() * fig.get_dpi(),
        fig.get_figheight() * fig.get_dpi(),
    )

    ensure_min_resolution(fig, min_pixels=MIN_PIXELS)

    after = max(
        fig.get_figwidth() * fig.get_dpi(),
        fig.get_figheight() * fig.get_dpi(),
    )

    assert after >= MIN_PIXELS
    assert after >= before
    plt.close(fig)


def test_ensure_min_resolution_no_change_if_sufficient():
    """
    ensure_min_resolution must not shrink figures already above threshold.
    """
    fig = setup_figure(width=6.0, height=6.0, dpi=MIN_DPI)

    before = fig.get_size_inches().copy()
    ensure_min_resolution(fig)
    after = fig.get_size_inches()

    assert after[0] == pytest.approx(before[0])
    assert after[1] == pytest.approx(before[1])
    plt.close(fig)


# ---------------------------------------------------------------------
# Saving and finalization
# ---------------------------------------------------------------------
def test_finalize_figure_saves_file(tmp_path):
    """
    finalize_figure must save the figure to disk.
    """
    fig = setup_figure()
    path = tmp_path / "test_figure.pdf"

    finalize_figure(path, fig=fig, close=True)

    assert path.exists()
    assert path.stat().st_size > 0


def test_finalize_figure_uses_current_figure(tmp_path):
    """
    finalize_figure must default to the current figure if none is provided.
    """
    setup_figure()
    path = tmp_path / "test_current.pdf"

    finalize_figure(path)

    assert path.exists()
    assert path.stat().st_size > 0


# ---------------------------------------------------------------------
# Semantic helpers
# ---------------------------------------------------------------------
def test_add_fisher_equilibrium_line_adds_line():
    """
    add_fisher_equilibrium_line must add a horizontal line to the axes.
    """
    fig, ax = plt.subplots()
    initial_lines = len(ax.lines)

    add_fisher_equilibrium_line()

    assert len(ax.lines) == initial_lines + 1
    plt.close(fig)


def test_set_axis_labels_sets_labels():
    """
    set_axis_labels must correctly set x and y axis labels.
    """
    fig, ax = plt.subplots()

    set_axis_labels("x-label", "y-label")

    assert ax.get_xlabel() == "x-label"
    assert ax.get_ylabel() == "y-label"
    plt.close(fig)

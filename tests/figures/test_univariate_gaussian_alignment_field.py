"""
Tests for the univariate Gaussian alignment field figure generator.

These tests verify that the figure generation pipeline executes correctly
and produces output files for the requested paper formats.
"""

import matplotlib
import pytest

from src.figures.fig_univariate_gaussian_alignment_field import generate


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
# Tests
# ---------------------------------------------------------------------
def test_generate_creates_alignment_field_figure(tmp_path, monkeypatch):
    """
    generate must create the univariate Gaussian alignment field figure.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    generate(formats=("revtext",))

    output = (
        tmp_path
        / "paper"
        / "revtext"
        / "figures"
        / "fig_univariate_gaussian_alignment_field.pdf"
    )

    assert output.exists()
    assert output.stat().st_size > 0


def test_generate_supports_multiple_formats(tmp_path, monkeypatch):
    """
    generate must support saving the figure for multiple formats.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    formats = ("revtext", "revtext")  # intentional duplication
    generate(formats=formats)

    output = (
        tmp_path
        / "paper"
        / "revtext"
        / "figures"
        / "fig_univariate_gaussian_alignment_field.pdf"
    )

    assert output.exists()

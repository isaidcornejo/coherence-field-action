"""
Tests for the alignment operator spectrum figure generator.

These tests verify that the spectrum figure generation pipeline executes
successfully and produces output files for the requested paper formats.
"""

import matplotlib
import pytest

from src.figures.fig_alignment_operator_spectrum import generate


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
def test_generate_creates_spectrum_figure(tmp_path, monkeypatch):
    """
    generate must create the alignment-operator spectrum figure.
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
        / "fig_alignment_operator_spectrum.pdf"
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
        / "fig_alignment_operator_spectrum.pdf"
    )

    assert output.exists()

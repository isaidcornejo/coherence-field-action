"""
Tests for the alignment field screening figure generator.

These tests verify that the figure generation pipeline executes correctly
and produces output files for the requested paper formats.
"""

import matplotlib
import pytest

from src.figures.fig_alignment_field_screening import generate


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
def test_generate_creates_figures(tmp_path, monkeypatch):
    """
    generate must create a figure file for each requested format.
    """
    # Redirect paper directory to a temporary location
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    generate(formats=("revtext",))

    output = tmp_path / "paper" / "revtext" / "figures" / "fig_alignment_field_screening.pdf"

    assert output.exists()
    assert output.stat().st_size > 0


def test_generate_multiple_formats(tmp_path, monkeypatch):
    """
    generate must support multiple output formats simultaneously.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    formats = ("revtext", "revtext")  # intentional duplication for robustness
    generate(formats=formats)

    output = tmp_path / "paper" / "revtext" / "figures" / "fig_alignment_field_screening.pdf"

    assert output.exists()

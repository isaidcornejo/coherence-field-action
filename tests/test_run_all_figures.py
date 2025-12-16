"""
Tests for the centralized figure-generation entry point.
"""

import matplotlib
import pytest

from src.run_figures import run_all


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
def test_run_all_generates_all_figures(tmp_path, monkeypatch):
    """
    run_all must generate all figures for the given paper format.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    run_all(formats=("revtext",))

    figures_dir = tmp_path / "paper" / "revtext" / "figures"

    expected = {
        "fig_alignment_operator_spectrum.pdf",
        "fig_alignment_field_screening.pdf",
        "fig_univariate_gaussian_alignment_field.pdf",
    }

    produced = {p.name for p in figures_dir.iterdir()}

    assert expected.issubset(produced)


def test_run_all_defaults_to_supported_formats(tmp_path, monkeypatch):
    """
    run_all must default to all supported formats when formats is None.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    run_all()

    figures_dir = tmp_path / "paper" / "revtext" / "figures"

    assert figures_dir.exists()
    assert any(figures_dir.iterdir())

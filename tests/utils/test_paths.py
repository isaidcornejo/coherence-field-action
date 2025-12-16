"""
Tests for canonical paper and figure path utilities.

These tests validate correctness, error handling, filesystem behavior,
and fundamental functional properties of the path-construction API used
for publication figures.
"""

from pathlib import Path

import pytest
from hypothesis import given, strategies as st

from src.utils.paths import (
    SUPPORTED_FORMATS,
    figures_dir,
    figure_path,
    figure_paths_all_formats,
)


# ---------------------------------------------------------------------
# Basic behavior
# ---------------------------------------------------------------------
def test_figures_dir_is_created(tmp_path, monkeypatch):
    """
    figures_dir must create the figures directory if it does not exist.

    The directory should be created under the appropriate paper format
    root and be idempotent across repeated calls.
    """
    monkeypatch.setattr(
        "src.utils.paths.PAPER_DIR",
        tmp_path / "paper",
    )

    fmt = next(iter(SUPPORTED_FORMATS))
    path = figures_dir(fmt)

    assert path.exists()
    assert path.is_dir()
    assert path.name == "figures"


def test_figure_path_has_correct_name_and_extension():
    """
    figure_path must correctly construct the figure filename
    and append the requested extension.
    """
    fmt = next(iter(SUPPORTED_FORMATS))
    path = figure_path("fig_test_example", format=fmt, ext="png")

    assert path.name == "fig_test_example.png"
    assert isinstance(path, Path)


def test_figure_paths_all_formats_yields_all_supported_formats():
    """
    figure_paths_all_formats must yield exactly one path per
    supported paper format.
    """
    paths = list(figure_paths_all_formats("fig_test"))

    assert len(paths) == len(SUPPORTED_FORMATS)

    for path in paths:
        assert path.name == "fig_test.pdf"


# ---------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------
def test_invalid_figure_name_raises():
    """
    Figure names not starting with the required 'fig_' prefix
    must raise a ValueError.
    """
    fmt = next(iter(SUPPORTED_FORMATS))

    with pytest.raises(ValueError):
        figure_path("invalid_name", format=fmt)


def test_unknown_format_raises():
    """
    Requesting an unsupported paper format must raise a ValueError.
    """
    with pytest.raises(ValueError):
        figure_path("fig_test", format="unknown_format")


# ---------------------------------------------------------------------
# Determinism and functional properties
# ---------------------------------------------------------------------
@given(
    name=st.text(min_size=1).map(lambda s: "fig_" + s.replace("/", "_")),
    ext=st.sampled_from(["pdf", "png", "svg"]),
)
def test_figure_path_is_deterministic(name, ext):
    """
    figure_path must be deterministic for identical inputs.

    Repeated calls with the same arguments must produce identical paths.
    """
    fmt = next(iter(SUPPORTED_FORMATS))

    p1 = figure_path(name, format=fmt, ext=ext)
    p2 = figure_path(name, format=fmt, ext=ext)

    assert p1 == p2


@given(
    name=st.text(min_size=1).map(lambda s: "fig_" + s.replace("/", "_")),
)
def test_figure_paths_all_formats_consistency(name):
    """
    figure_paths_all_formats must be consistent with figure_path
    for all supported paper formats.
    """
    paths = list(figure_paths_all_formats(name))

    assert len(paths) == len(SUPPORTED_FORMATS)

    for fmt, path in zip(SUPPORTED_FORMATS, paths):
        assert path == figure_path(name, format=fmt)

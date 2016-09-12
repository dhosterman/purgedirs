from functools import partial
import os
import shutil
from unittest.mock import MagicMock, patch

from click.testing import CliRunner
import pytest

from purgedirs import cli, empty_directories


@pytest.fixture
def mock_os_walk(monkeypatch):
    def mock_values(*args, **kwargs):
        return [("dir1", ["dir2", "dir3", "dir4"], ["file1"]),
                ("dir5", ["dir6", "dir7", "dir8"], []), ]

    monkeypatch.setattr("os.walk", mock_values)


@pytest.fixture
def cli_runner():
    runner = CliRunner()
    return partial(CliRunner().invoke, cli)


def test_empty_directories(mock_os_walk):
    """Should return the absolute path for directories without files"""
    assert empty_directories(".") == [os.getcwd() + "/dir5"]


@pytest.mark.parametrize("test_input", [(["--help"]), (["-h"])])
def test_help_option(test_input):
    result = cli_runner()(test_input)
    assert "Show this message and exit" in result.output


@pytest.mark.parametrize("test_input", [(["--dry-run", "."]), (["-d", "."])])
def test_dry_run_option(test_input, mock_os_walk):
    result = cli_runner()(test_input)
    assert "dir5" in result.output


@pytest.mark.parametrize("test_input", [(["."]), ])
def test_cli(test_input, mock_os_walk, monkeypatch):
    with patch("shutil.rmtree") as mock:
        result = cli_runner()(test_input)
        mock.assert_called_once_with(os.getcwd() + "/dir5")
        assert "dir5" in result.output

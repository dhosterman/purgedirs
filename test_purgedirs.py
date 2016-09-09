import os
import pytest

from purgedirs import empty_directories


@pytest.fixture
def os_walk_mock(*args, **kwargs):
    return [
        ("dir1", ["dir2", "dir3", "dir4"], ["file1"]),
        ("dir5", ["dir6", "dir7", "dir8"], []),
    ]


def test_empty_directories(monkeypatch):
    """Should return the absolute path for directories without files"""
    monkeypatch.setattr("os.walk", os_walk_mock)
    assert empty_directories(".") == [os.getcwd() + "/dir5"]

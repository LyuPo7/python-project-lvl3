# -*- coding:utf-8 -*-

"""Tests for page-loader."""
import pytest
from page_loader import path
import os.path
import json

FILE_HTML_PATHS = 'tests/fixtures/data/html_paths.json'
FILE_SOURCES_PATHS = 'tests/fixtures/data/sources_paths.json'
FILE_SRCS = 'tests/fixtures/data/src.json'

def extract(file):
    """Extract data from json file.
    Args:
        file(str): json file,

    Returns:
        : dictionary with {link: expected_html}
    """
    return json.loads(open(file).read()).items()

@pytest.mark.parametrize("link,html_expected_file",
    extract(FILE_HTML_PATHS),
)
def test_path_create_file(link, html_expected_file):
    """Check path.create function.
    Check if created path is correct.
    """
    downloaded_file, dir_sources = path.create(link)

    assert downloaded_file == html_expected_file


@pytest.mark.parametrize("link,expected_dir",
    extract(FILE_SOURCES_PATHS),
)
def test_path_create_dir(link, expected_dir):
    """Check path.create function.
    Check if created dir for srcs is correct.
    """
    downloaded_file, dir_sources = path.create(link)

    assert dir_sources == expected_dir


@pytest.mark.parametrize("link,expected_src",
    extract(FILE_SRCS),
)
def test_path_src(link, expected_src):
    """Check path.create function.
    Check if relink for src works correctly.
    """
    src = path.relink(link)

    assert src == expected_src
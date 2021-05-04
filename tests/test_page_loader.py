# -*- coding:utf-8 -*-

"""Tests for page-loader."""
import os
import pytest
import requests
import tempfile
import requests_mock
from page_loader import page
from page_loader import path
from bs4 import BeautifulSoup as bs


LINK = 'https://pythonjobs.github.io'
HTML = './tests/fixtures/source/pythonjobs-github-io.html'
DIR_TMP = tempfile.mkdtemp()
HTML_EXPECTED = './tests/fixtures/expected/pythonjobs-github-io.html'
DIR_EXPECTED = './tests/fixtures/expected/pythonjobs-github-io_files/'


def extract(link):
    """Extract data from file.
    Args:
        link(str): file,

    Returns:
        : string with content of the file
    """
    with open(link) as file:
        return file.read()


def download(link, html, folder):
    """Run download function with mock."""
    with requests_mock.mock() as m:
         m.get(link, text=extract(html))
    page.download(link, folder) 


def test_content():
    """Compare expected and source html content."""
    # Expected file content
    file_exp = open(HTML_EXPECTED, 'rb')
    content_exp = bs(file_exp.read(), 'html.parser')
    # Downloaded file content
    download(LINK, HTML, DIR_TMP)
    html_down = path.create(LINK)[0]
    file_down = open(os.path.join(DIR_TMP, html_down))
    content_down = bs(file_down, 'html.parser')

    assert content_exp.decode() == content_down.decode()


def test_srcs():
    """Compare expected and downloaded srcs lists."""
    # Expected srcs list
    files_exp = os.listdir(DIR_EXPECTED)
    # Downloaded srcs list
    dir_down = path.create(LINK)[1]
    files_down = os.listdir(os.path.join(DIR_TMP, dir_down))
    assert files_exp == files_down
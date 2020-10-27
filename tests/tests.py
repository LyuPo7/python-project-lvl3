# -*- coding:utf-8 -*-

"""Tests for page-loader."""
import pytest
import tempfile
import requests
from page_loader import path
from page_loader import page
import os.path
from lxml import html, etree

@pytest.mark.parametrize("link,html_file,dir_name", [
    ('https://hexlet.io/courses', 'hexlet-io-courses.html', 'hexlet-io-courses_files'),
    ('https://pythonjobs.github.io', 'pythonjobs-github-io.html', 'pythonjobs-github-io_files'),
 ])
def test_path_create(link, html_file, dir_name):
    """Check path.create function."""
    created_name = path.create(link)
    true_names = (html_file, dir_name)

    assert created_name == true_names


@pytest.mark.parametrize("link,html_file", [
    ('https://hexlet.io/courses', 'hexlet-io-courses.html'),
    ('https://pythonjobs.github.io', 'pythonjobs-github-io.html'),
 ])
def test_page_download(link, html_file):
    """Check page.download function"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path2check = os.path.join(tmpdir, html_file)
        page.download(link, tmpdir)
        exist_file2check = os.path.exists(path2check)
        assert  exist_file2check == True


@pytest.mark.parametrize("link,dir_name", [
    ('https://hexlet.io/courses', 'hexlet-io-courses_files'),
    ('https://pythonjobs.github.io', 'pythonjobs-github-io_files'),
 ])
def test_src_download(link, dir_name):
    """Check src.download function"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path2check = os.path.join(tmpdir, dir_name)
        page.download(link, tmpdir)
        srcs2check = os.listdir(path2check)
    
        res = requests.get(link)
        extracted_html = html.fromstring(res.content)
        srcs = extracted_html.xpath("//image/@src")
        srcs.extend(extracted_html.xpath("//script/@src"))
        srcs.extend(extracted_html.xpath("//link/@href"))
        srcs_valid = [src for src in srcs if not '//' in src and '/' in src]
        assert  len(srcs_valid) == len(srcs2check)
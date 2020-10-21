# -*- coding:utf-8 -*-

"""Tests for page-loader."""
import pytest
import tempfile
import requests
from page_loader import path
from page_loader import page
import os.path

def test_path_create():
    """Check path.create function."""
    created_name = path.create('https://hexlet.io/courses', '/var/tmp')
    true_name = '/var/tmp/hexlet-io-courses.html'

    assert created_name == true_name


'''def test_page_download():
    """Check page.download function"""
    with tempfile.TemporaryDirectory() as tmpdir:
        path2check = os.path.join(tmpdir, 'hexlet-io-courses.html')
        page.download('https://hexlet.io/courses',path2check)
        file2check = open(path2check)
        data2check = file2check.read()
        res = requests.get('https://hexlet.io/courses')
        correct = res.text
        assert  correct == data2check
'''

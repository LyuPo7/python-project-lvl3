# -*- coding:utf-8 -*-

"""Tests for page-loader."""
import pytest
import tempfile
from page_loader import path
from page_loader import page
from page_loader import error
from page_loader import text
import os
import stat
import os.path
from lxml import html

TEST_LINK = 'test'


@pytest.mark.parametrize("link", TEST_LINK)
def test_perm_error(link):
    """Test error.Error exception."""
    with pytest.raises(error.Error):
        with tempfile.TemporaryDirectory() as tmpdir:
            os.chmod(tmpdir, stat.S_IREAD)
            page.download(link, tmpdir)
# This Python file uses the following encoding: utf-8

"""Paths module."""
import re
import os.path
from urllib.parse import urlparse

# Constants
CHANGE_SYMBOL = '-'
MAX_LEN = 100


def change(path):
    """Change char if itsn't valid.
    Args:
        path(str): path to check,

    Returns:
        char(str): valid path.
    """
    path_valid = ''
    char_regx = re.compile(r'[a-zA-Z0-9]')
    for i in range(len(path)):
        if char_regx.search(path[i]):
            path_valid += path[i]
        else:
            path_valid += CHANGE_SYMBOL
    return path_valid


def create(page):
    """Create name for html page and name for directory of sources of html page.
    Args:
        page(str): html page,

    Returns:
        path_page(str): path for save page,
        path_dir(str): path of directory for save sources of the page.
    """
    page_wo_schema = urlparse(page)
    path_path, path_ext = os.path.splitext(page_wo_schema.path)
    path_valid = change("{}{}".format(
            page_wo_schema.netloc,
            path_path,
        ),
    )
    path_page = '{}.html'.format(path_valid)
    path_dir = '{}_files'.format(path_valid)
    return (path_page, path_dir)


def relink(src):
    """Relink source with valid chars.
    Args:
        page(str): html page,

    Returns:
        src(str): relinked source,
    """
    path, ext = os.path.splitext(src)
    path_valid = change(path)
    if len(path_valid) > MAX_LEN:
        path_valid = path_valid[:MAX_LEN]
    return path_valid + ext

# This Python file uses the following encoding: utf-8

"""Paths module."""
import os.path
import re

# Constants
CHANGE_SYMBOL = '-'


def change(path):
    """Change char if itsn't valid.
    Args:
        char(str): char to check,

    Returns:
        char(str): valid char.
    """
    path_valid = ''
    char_regx = re.compile(r'[a-zA-Z0-9]')
    for i in range(len(path)):
        if char_regx.search(path[i]):
            path_valid += path[i]
        else:
            path_valid += CHANGE_SYMBOL
    return path_valid


def cut(link):
    """Cut schema from the link.
    Args:
        link(str): link,

    Returns:
        link(str): link without schema.
    """
    domain_regx = re.compile(r'(https:\/\/)(\S*)')
    domain = domain_regx.search(link)
    if domain:
        return domain.group(2)
    return link


def create(page):
    """Create name for html page and name for directory of sources of html page.
    Args:
        page(str): html page,

    Returns:
        path_page(str): path for save page,
        path_dir(str): path of directory for save sources of the page.
    """
    path = cut(page)
    path_valid = change(path)
    path_page = '{}.html'.format(path_valid)
    path_dir = '{}_files'.format(path_valid)
    return (path_page, path_dir)


def relink(src):
    """Relink source with valid chars.
    Args:
        page(str): html page,

    Returns:
        src(str): name of source,
        path_dir(str): path of directory for save sources of the page.
    """
    path, ext = os.path.splitext(src)
    path_valid = change(path)
    if len(path_valid) > 100:
        path_valid = path_valid[:100]
    return path_valid + ext

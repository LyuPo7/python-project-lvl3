# This Python file uses the following encoding: utf-8

"""Paths module."""
import os.path
import re

# Constants
CHANGE_SYMBOL = '-'


def change(char):
    char_regx = re.compile(r'[a-zA-Z0-9]')
    if char_regx.search(char):
        return char
    return CHANGE_SYMBOL


def cut(link):
    domain_regx = re.compile(r'(https:\/\/)(\S*)')
    domain = domain_regx.search(link)
    if domain:
        return domain.group(2)
    return link


def create(page):
    path = list(cut(page))
    for i in range(len(path)):
        path[i] = change(path[i])
    path_page = '{}.html'.format(''.join(path))
    path_dir = '{}_files'.format(''.join(path))
    return (path_page, path_dir)


def relink(src):
    path, ext = os.path.splitext(src)
    path = list(path)
    for i in range(len(path)):
        path[i] = change(path[i])
    if len(path) > 100:
        path = path[:100]
    return ''.join(path[1:]) + ext

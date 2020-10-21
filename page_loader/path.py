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


def create(page, output):
    path = list(page.split('://')[1])
    for i in range(len(path)):
        path[i] = change(path[i])
    path = '{}.html'.format(''.join(path))
    return os.path.join(output, path)

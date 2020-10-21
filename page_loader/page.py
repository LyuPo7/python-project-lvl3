# This Python file uses the following encoding: utf-8

"""Page module."""
import requests


def download(page, path_out):
    """Download HTML page."""
    res = requests.get(page)
    if res.status_code == 200:
        text = res.text
        with open(path_out, 'w') as html_file:
            html_file.write(text)

# This Python file uses the following encoding: utf-8

"""Html module."""
import requests
from lxml import html
import logging
import os.path
from page_loader import error
from page_loader import src


def get(page):
    """Get request of page.
    Args:
        page(str): page to download,

    Returns:
        : request of the page.
    """
    try:
        res = requests.get(page)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        logging.error(e.__doc__)
        raise error.Error() from e
    else:
        return res


def extract(page):
    """Get HTML text of page.
    Args:
        page(str): page to download,

    Returns:
        : text of html page,
        : extracted html page.
    """
    res = get(page)
    return (res.text, html.fromstring(res.content))


def save(page, html_text, path_html):
    """Save HTML text of page to local HTML file.
    Args:
        page(str): page to download,

    Returns:
        html_text(str): text of html page,
        path_html(str): path for saving html page.
    """
    logging.info('Starting download html text.')
    with open(path_html, 'w') as html_file:
        logging.info('Saving %s to %s', page, path_html)
        html_file.write(html_text)
    logging.info('Finishing download html text.')


def relink(page, srcs_downloaded, text_html, srcs_dir, dir_out, html_name):
    """Relink every src in HTML file.
    Args:
        page(str): page to download,
        srcs_downloaded(list): all downloaded srcs,
        text_html(str): text of html page,
        srcs_dir(str): directory of downloaded srcs,
        dir_out(str): directory for html downloading,
        html_name(str): name for html file,

    Returns:
        html_text(str): text of html page,
        path_html(str): path for saving html page.
    """
    path_html = os.path.join(dir_out, html_name)
    text_relinked = src.relink(srcs_downloaded, text_html, srcs_dir)
    save(page, text_relinked, path_html)
    logging.info('Name of HTML file: %s', html_name)
    logging.debug('Path to HTML file: %s', path_html)

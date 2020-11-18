# This Python file uses the following encoding: utf-8

"""Page module."""
from lxml import html
from page_loader import path
from page_loader import error
from page_loader import text
from page_loader import src
import os
import shutil
import logging


def download(page, dir_out):
    """Download HTML page."""
    # Create paths for HTML page and directory for resources from HTML page
    base_name_out, base_dir_out = path.create(page)
    path_html = os.path.join(dir_out, base_name_out)
    path_dir_out = os.path.join(dir_out, base_dir_out)
    # Remove directory for resources from HTML page if already exists
    if os.path.exists(path_dir_out):
        logging.debug('Directory %s already exists.', path_dir_out)
        logging.debug('Removing %s.', path_dir_out)
        shutil.rmtree(path_dir_out)
    try:  # Check if dir entered by user exists
        os.mkdir(path_dir_out)
        logging.info('Creating %s', path_dir_out)
    except IOError as e:  # If not exists raise exception
        logging.error("No such directory: {}".format(dir_out))
        raise error.PathError() from e
    logging.info('Name of HTML file: %s', base_name_out)
    logging.debug('Name of directory for sources saving: %s', path_dir_out)
    logging.debug('Path to HTML file: %s', path_html)
    logging.debug('Path to source directory: %s', path_dir_out)
    # Make request
    res = text.download(page)
    text_html = res.text
    # Save src anf href to list
    extracted_html = html.fromstring(res.content)
    srcs = extracted_html.xpath("//image/@src")
    srcs.extend(extracted_html.xpath("//script/@src"))
    srcs.extend(extracted_html.xpath("//link/@href"))
    srcs_valid = [src for src in srcs if '//' not in src and '/' in src]
    text_relinked = src.download(page, srcs_valid, text_html, path_dir_out, base_dir_out)
    with open(path_html, 'w') as html_file:
        logging.info('Saving %s to %s', page, path_html)
        html_file.write(text_relinked)

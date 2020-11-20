# This Python file uses the following encoding: utf-8

"""Sources module."""
import os
import requests
import requests.status_codes as rsc
import logging
from page_loader import path
from progress.bar import Bar


def relink(srcs, text_html, dir_out):
    """Relink sources in HTML text.
    Args:
        srcs(list): sources to be relinked,
        text_html(str): html text contained sources,
        base_dir_out(str): directory to which relink sources.
    """
    logging.info('Starting relink of sources of the page.')
    for link in srcs:
        file_name = path.relink(link)
        full_name = os.path.join(dir_out, file_name)
        text_html = text_html.replace(link, full_name)
        logging.info('Changing %s to %s', link, full_name)
    logging.info('Finishing relink of sources of the page.')
    return text_html


def download(page, srcs, path_dir_out):
    """Download sources from HTML page.
    Args:
        page(str): HTML page,
        srcs(list): sources to be downloaded,
        path_dir_out(str): directory to which download sources.
    """
    logging.info('Starting download of sources of the page.')
    logging.debug('All sources from page to download: {}'.format(srcs))
    bar = Bar('Downloading resources', max=len(srcs), suffix='%(percent).1f%% - Remaining time: %(eta).1f sec')
    for link in srcs:
        file_name = path.relink(link)
        path_link = os.path.join(path_dir_out, file_name)
        full_link = page + link
        logging.info('Downloading %s to %s', full_link, path_link)
        with open(path_link, 'wb') as fd:
            src_res = requests.get(full_link)
            response = src_res.status_code
            if response == rsc.codes.OK:
                for chunk in src_res.iter_content(100000):
                    fd.write(chunk)
            elif response == rsc.codes.NOT_FOUND:  # 404
                logging.warning('Server not found. Check your internet connection.')
            elif response == rsc.codes.TIMEOUT:  # 408
                logging.warning("The request wan't within the time that the server was prepared to wait.")
            elif response == rsc.codes.BAD:  # 400
                logging.warning("The request could not be understood by the server due to malformed syntax.")
            elif response == rsc.codes.GATEWAY_TIMEOUT:  # 504
                logging.warning("The server could have problems.")
            else:
                logging.warning('Problem with request to %s', full_link)
        bar.next()
    bar.finish()
    logging.info('Finishing download of sources of the page.')

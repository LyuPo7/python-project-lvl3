# This Python file uses the following encoding: utf-8

"""Sources module."""
import os
import shutil
import requests
import logging
from page_loader import error
from page_loader import path
from progress.bar import Bar


def relink(srcs, text_html, dir_out):
    """Relink sources in HTML text.
    Args:
        srcs(list): sources to be relinked,
        text_html(str): html text contained sources,
        dir_out(str): directory to which relink sources.
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
    bar = Bar(
        'Downloading resources',
        max=len(srcs),
        suffix='%(percent).1f%% - Remaining time: %(eta).1f sec',
    )
    for link in srcs:
        file_name = path.relink(link)
        path_link = os.path.join(path_dir_out, file_name)
        full_link = page + link
        logging.info('Downloading %s to %s', full_link, path_link)
        with open(path_link, 'wb') as fd:
            try:
                src_res = requests.get(full_link)
                src_res.raise_for_status()
            except requests.exceptions.HTTPError as e:
                logging.error(e.__doc__)
                raise error.Error() from e
            else:
                for chunk in src_res.iter_content(100000):
                    fd.write(chunk)
        bar.next()
    bar.finish()
    logging.info('Finishing download of sources of the page.')


def create_dir(abs_path_2_src_dir, dir_out):
    """Create directory for downloading srcs.
    Args:
        abs_path_2_src_dir(str): name of directory for saving html,
        dir_out(str): directory to which download page.
    """
    # Remove directory for resources from HTML page if already exists
    if os.path.exists(abs_path_2_src_dir):
        logging.debug('Directory %s already exists.', abs_path_2_src_dir)
        logging.debug('Removing %s.', abs_path_2_src_dir)
        shutil.rmtree(abs_path_2_src_dir)
    try:  # Check if dir entered by user exists
        os.mkdir(abs_path_2_src_dir)
        logging.info('Creating directory: %s', abs_path_2_src_dir)
    except IOError as e:  # If not exists raise exception
        logging.error("No such directory: {}".format(dir_out))
        raise error.Error() from e
    except PermissionError as e:  # If not enough permissions
        logging.error(
            """No enough permissions for create directory
            in: {}""".format(dir_out)
        )
        raise error.Error() from e
    logging.debug(
        'Name of directory for sources saving: %s',
        abs_path_2_src_dir,
    )
    logging.debug('Path to source directory: %s', abs_path_2_src_dir)

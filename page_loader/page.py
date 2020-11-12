# This Python file uses the following encoding: utf-8

"""Page module."""
import requests
import requests.status_codes as rsc
from lxml import html
from page_loader import path
import os
import shutil
import logging
from page_loader import error


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
    try:
        res = requests.get(page)
        res_response = res.status_code
    except requests.exceptions.ConnectionError as e:
        logging.error("Name or service not known: {}.".format(page))
        raise error.RequestError() from e
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
        logging.error("Invalid URL: {}.".format(page))
        raise error.RequestError() from e
    if res_response == rsc.codes.OK:
        text = res.text
    elif res_response == rsc.codes.NOT_FOUND:  # 404
        logging.error('Server not found. Check your request: {}.'.format(page))
        raise error.RequestError()
    elif res_response == rsc.codes.TIMEOUT:  # 408
        logging.warning("The request wan't within the time that the server was prepared to wait.")
    elif res_response == rsc.codes.BAD:  # 400
        logging.warning("The request could not be understood by the server due to malformed syntax.")
    elif res_response == rsc.codes.GATEWAY_TIMEOUT:  # 504
        logging.warning("The server could have problems.")
    else:
        logging.warning('Problem with request to %s', page)
    # Save src anf href to list
    extracted_html = html.fromstring(res.content)
    srcs = extracted_html.xpath("//image/@src")
    srcs.extend(extracted_html.xpath("//script/@src"))
    srcs.extend(extracted_html.xpath("//link/@href"))
    srcs_valid = [src for src in srcs if '//' not in src and '/' in src]
    logging.debug('All sources from page to download: {}'.format(srcs_valid))
    for link in srcs_valid:
        file_name = path.relink(link)
        path_link = os.path.join(path_dir_out, file_name)
        full_name = os.path.join(base_dir_out, file_name)
        full_link = page + link
        logging.info('Downloading %s to %s', full_link, path_link)
        with open(path_link, 'wb') as fd:
            src_res = requests.get(full_link)
            response = src_res.status_code
            if response == rsc.codes.OK:
                for chunk in src_res.iter_content(100000):
                    fd.write(chunk)
                text = text.replace(link, full_name)
                logging.info('Changing %s to %s', link, full_name)
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
    with open(path_html, 'w') as html_file:
        logging.info('Saving %s to %s', page, path_html)
        html_file.write(text)

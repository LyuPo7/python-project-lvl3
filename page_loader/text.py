# This Python file uses the following encoding: utf-8

"""Html module."""
import requests
import requests.status_codes as rsc
import logging
from page_loader import error


def download(page):
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
        return res
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


def save(page, html_text, path_html):
    logging.info('Starting download html text.')
    with open(path_html, 'w') as html_file:
        logging.info('Saving %s to %s', page, path_html)
        html_file.write(html_text)
    logging.info('Finishing download html text.')
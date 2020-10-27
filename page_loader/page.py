# This Python file uses the following encoding: utf-8

"""Page module."""
import requests
import bs4
from page_loader import path
import os
import shutil
import logging


def download(page, dir_out):
    """Download HTML page."""
    # Create paths for HTML page and directory for resources from HTML page
    base_name_out, base_dir_out = path.create(page)
    path_dir_out = os.path.join(dir_out, base_dir_out)
    path_html = os.path.join(dir_out, base_name_out)
    # Remove directory for resources from HTML page if already exists
    if os.path.exists(path_dir_out):
        shutil.rmtree(path_dir_out)
    os.makedirs(path_dir_out)
    # Make request
    res = requests.get(page)
    text = res.text
    res.raise_for_status()
    soup = bs4.BeautifulSoup(text, "html.parser")
    # Save src anf href to list
    links4save = []
    scripts = soup.select('script[src]')
    imgs = soup.select('img[src]')
    links = soup.select('link[href]')
    for script in scripts:
        src = script.get('src')
        if '//' not in src:
            links4save.append(src)
    for img in imgs:
        src = script.get('src')
        if '//' not in src:
            links4save.append(src)
    for link in links:
        href = link.get('href')
        if '//' not in href and '/' in href:
            links4save.append(href)
    print(links4save)
    for link in links4save:
        file_name = path.relink(link)
        path_link = os.path.join(path_dir_out, file_name)
        full_name = os.path.join(base_dir_out, file_name)
        full_link = page + link
        logging.info('Downloading %s to %s', full_link, path_link)
        with open(path_link, 'wb') as fd:
            try:
                src_res = requests.get(full_link)
                for chunk in src_res.iter_content(100000):
                    fd.write(chunk)
                text = text.replace(link, full_name)
                logging.info('Changing %s to %s', link, full_name)
            except:
                logging.info('Failed to download %s', link)
    with open(path_html, 'w') as html_file:
        logging.info('Saving %s to %s', page, path_html)
        html_file.write(text)

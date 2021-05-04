# This Python file uses the following encoding: utf-8

"""Page module."""
import os
from page_loader import path
from page_loader import text
from page_loader import src


def find_srcs(page, extracted_html, abs_path_2_src_dir):
    """Download srcs from the page to srcs dir.
    Args:
        page(str): page with src to download,
        extracted_html(srt): extracted html page,
        abs_path_2_src_dir(str): name of directory for saving html,

    Returns:
        srcs_downloaded(list): list of downloaded srcs.
    """
    srcs = extracted_html.xpath("//image/@src")
    srcs.extend(extracted_html.xpath("//script/@src"))
    srcs.extend(extracted_html.xpath("//link/@href"))
    srcs_downloaded = [src for src in srcs if '//' not in src and '/' in src]
    src.download(page, srcs_downloaded, abs_path_2_src_dir)
    return srcs_downloaded


def download(page, dir_out):
    """Download HTML page.
    Args:
        page(str): page to download,
        dir_out(str): directory to which download page.
    """
    # Paths and names for html file and directory for srcs
    html_name, srcs_dir = path.create(page)
    abs_path_2_src_dir = os.path.join(dir_out, srcs_dir)
    # Create srcs dir
    src.create_dir(abs_path_2_src_dir, dir_out)
    # Get html text
    text_html, extracted_html = text.extract(page)
    # Download srcs
    srcs_downloaded = find_srcs(page, extracted_html, abs_path_2_src_dir)
    # Relink and download html text
    text.relink(
        page,
        srcs_downloaded,
        text_html,
        srcs_dir,
        dir_out,
        html_name,
    )

# This Python file uses the following encoding: utf-8

"""Main file of project."""
from page_loader import page
from page_loader.parser import create_parser
import logging


def main():
    """Run project."""
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
    logging.info('Started')
    parser = create_parser()
    namespace = parser.parse_args()
    page.download(namespace.page, namespace.output)
    logging.info('Finished')


if __name__ == '__main__':
    main()

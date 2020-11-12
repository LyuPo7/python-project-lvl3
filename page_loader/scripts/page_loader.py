# This Python file uses the following encoding: utf-8

"""Main file of project."""
from page_loader import page
from page_loader import VERBOSITY
from page_loader.parser import create_parser
import logging
import sys
from page_loader import error
import traceback


def main():
    """Run project."""
    parser = create_parser()
    namespace = parser.parse_args()
    logging.basicConfig(
        level=VERBOSITY[namespace.verbosity],
        format=' %(asctime)s - %(levelname)s - %(message)s',
    )
    logging.info('Started')
    try:
        page.download(namespace.page, namespace.output)
    except error.ConnectionError:
        traceback.print_exc(file=open('./page_loader.log', 'a'))
        sys.exit(1)
    except error.PathError:
        traceback.print_exc(file=open('./page_loader.log', 'a'))
        sys.exit(1)
    except error.RequestError:
        traceback.print_exc(file=open('./page_loader.log', 'a'))
        sys.exit(1)

    logging.info('Finished')


if __name__ == '__main__':
    main()

# This Python file uses the following encoding: utf-8

"""Main file of project."""
import sys
import logging
import traceback
from page_loader import page
from page_loader import error
from page_loader import VERBOSITY
from page_loader.parser import create_parser


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
    except error.Error:
        traceback.print_exc()
        sys.exit(1)

    logging.info('Finished')


if __name__ == '__main__':
    main()

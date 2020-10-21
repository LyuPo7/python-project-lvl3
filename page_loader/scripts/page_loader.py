# This Python file uses the following encoding: utf-8

"""Main file of project."""
from page_loader import path
from page_loader import page
from page_loader.parser import create_parser


def main():
    """Run project."""
    parser = create_parser()
    namespace = parser.parse_args()
    file_name = path.create(namespace.page, namespace.output)
    page.download(namespace.page, file_name)


if __name__ == '__main__':
    main()

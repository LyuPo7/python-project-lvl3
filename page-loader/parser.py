# This Python file uses the following encoding: utf-8

"""Parser of project."""
import argparse


def create_parser():
    """Create parser.

    Returns:
        parser - parser.
    """
    parser = argparse.ArgumentParser(
        prog='page-loader',
		description="""Description:
            The program loads HTML pages.""",
		epilog="""(c) October 2020.
            The developer isn't responsible for any problems
            which might result from work of this program.
            """,
    )
    parser.add_argument(
        'page',
        metavar='page',
        type=str,
        help='page for download',
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='./',
        help='output directory',
        metavar='OUTPUT',
    )

    return parser

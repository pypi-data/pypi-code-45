from __future__ import unicode_literals

import argparse
import logging

from .base import append_doc_link
from .base import CmdBaseNoRepo
from dvc.exceptions import DvcException


logger = logging.getLogger(__name__)


class CmdGetUrl(CmdBaseNoRepo):
    def run(self):
        from dvc.repo import Repo

        try:
            Repo.get_url(self.args.url, out=self.args.out)
            return 0
        except DvcException:
            logger.exception("failed to get '{}'".format(self.args.url))
            return 1


def add_parser(subparsers, parent_parser):
    GET_HELP = "Download or copy files from URL."
    get_parser = subparsers.add_parser(
        "get-url",
        parents=[parent_parser],
        description=append_doc_link(GET_HELP, "get-url"),
        help=GET_HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    get_parser.add_argument(
        "url", help="See `dvc import-url -h` for full list of supported URLs."
    )
    get_parser.add_argument(
        "out", nargs="?", help="Destination path to put data to."
    )
    get_parser.set_defaults(func=CmdGetUrl)

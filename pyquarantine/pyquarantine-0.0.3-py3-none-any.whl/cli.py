#!/usr/bin/env python
#
# PyQuarantine-Milter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyQuarantine-Milter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyQuarantineMilter.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import logging
import logging.handlers
import sys
import time

import pyquarantine

from pyquarantine.version import __version__ as version

def _get_quarantine_obj(config, quarantine):
    try:
        quarantine_obj = next((q["quarantine_obj"]
                               for q in config if q["name"] == quarantine))
    except StopIteration:
        raise RuntimeError("invalid quarantine '{}'".format(quarantine))
    return quarantine_obj


def _get_whitelist_obj(config, quarantine):
    try:
        whitelist_obj = next((q["whitelist_obj"]
                              for q in config if q["name"] == quarantine))
    except StopIteration:
        raise RuntimeError("invalid quarantine '{}'".format(quarantine))
    return whitelist_obj


def print_table(columns, rows):
    if not rows:
        return

    column_lengths = []
    column_formats = []

    # iterate columns to display
    for header, key in columns:
        # get the length of the header string
        lengths = [len(header)]
        # get the length of the longest value
        lengths.append(
            len(str(max(rows, key=lambda x: len(str(x[key])))[key])))
        # use the the longer one
        length = max(lengths)
        column_lengths.append(length)
        column_formats.append("{{:<{}}}".format(length))

    # define row format
    row_format = " | ".join(column_formats)

    # define header/body separator
    separators = []
    for length in column_lengths:
        separators.append("-" * length)
    separator = "-+-".join(separators)

    # print header and separator
    print(row_format.format(*[column[0] for column in columns]))
    print(separator)

    keys = [entry[1] for entry in columns]
    # print rows
    for entry in rows:
        row = []
        for key in keys:
            row.append(entry[key])
        print(row_format.format(*row))


def list_quarantines(config, args):
    if args.batch:
        print("\n".join([quarantine["name"] for quarantine in config]))
    else:
        print_table(
            [("Name", "name"), ("Quarantine", "quarantine_type"),
             ("Notification", "notification_type"), ("Action", "action")],
            config
        )


def list_quarantine_emails(config, args):
    logger = logging.getLogger(__name__)

    # get quarantine object
    quarantine = _get_quarantine_obj(config, args.quarantine)
    if quarantine is None:
        raise RuntimeError(
            "quarantine type is set to None, unable to list emails")

    # find emails and transform some metadata values to strings
    rows = []
    emails = quarantine.find(
        mailfrom=args.mailfrom,
        recipients=args.recipients,
        older_than=args.older_than)
    for quarantine_id, metadata in emails.items():
        row = emails[quarantine_id]
        row["quarantine_id"] = quarantine_id
        row["date"] = time.strftime(
            '%Y-%m-%d %H:%M:%S',
            time.localtime(
                metadata["date"]))
        row["mailfrom"] = metadata["mailfrom"]
        row["recipient"] = metadata["recipients"].pop(0)
        row["subject"] = emails[quarantine_id]["headers"]["subject"][:60]
        rows.append(row)

        if metadata["recipients"]:
            row = {
                "quarantine_id": "",
                "date": "",
                "mailfrom": "",
                "recipient": metadata["recipients"].pop(0),
                "subject": ""
            }
            rows.append(row)

    if args.batch:
        # batch mode, print quarantine IDs, each on a new line
        print("\n".join(emails.keys()))
        return

    if not emails:
        logger.info("quarantine '{}' is empty".format(args.quarantine))
    print_table(
        [("Quarantine-ID", "quarantine_id"), ("Date", "date"),
         ("From", "mailfrom"), ("Recipient(s)", "recipient"),
         ("Subject", "subject")],
        rows
    )


def list_whitelist(config, args):
    logger = logging.getLogger(__name__)

    # get whitelist object
    whitelist = _get_whitelist_obj(config, args.quarantine)
    if whitelist is None:
        raise RuntimeError(
            "whitelist type is set to None, unable to list entries")

    # find whitelist entries
    entries = whitelist.find(
        mailfrom=args.mailfrom,
        recipients=args.recipients,
        older_than=args.older_than)
    if not entries:
        logger.info(
            "whitelist of quarantine '{}' is empty".format(
                args.quarantine))
        return

    # transform some values to strings
    for entry_id, entry in entries.items():
        entries[entry_id]["permanent_str"] = str(entry["permanent"])
        entries[entry_id]["created_str"] = entry["created"].strftime(
            '%Y-%m-%d %H:%M:%S')
        entries[entry_id]["last_used_str"] = entry["last_used"].strftime(
            '%Y-%m-%d %H:%M:%S')

    print_table(
        [
            ("ID", "id"), ("From", "mailfrom"), ("To", "recipient"),
            ("Created", "created_str"), ("Last used", "last_used_str"),
            ("Comment", "comment"), ("Permanent", "permanent_str")
        ],
        entries.values()
    )


def add_whitelist_entry(config, args):
    logger = logging.getLogger(__name__)

    # get whitelist object
    whitelist = _get_whitelist_obj(config, args.quarantine)
    if whitelist is None:
        raise RuntimeError(
            "whitelist type is set to None, unable to add entries")

    # check existing entries
    entries = whitelist.check(args.mailfrom, args.recipient)
    if entries:
        # check if the exact entry exists already
        for entry in entries.values():
            if entry["mailfrom"] == args.mailfrom and \
                    entry["recipient"] == args.recipient:
                raise RuntimeError(
                    "an entry with this from/to combination already exists")

        if not args.force:
            # the entry is already covered by others
            for entry_id, entry in entries.items():
                entries[entry_id]["permanent_str"] = str(entry["permanent"])
                entries[entry_id]["created_str"] = entry["created"].strftime(
                    '%Y-%m-%d %H:%M:%S')
                entries[entry_id]["last_used_str"] = entry["last_used"].strftime(
                    '%Y-%m-%d %H:%M:%S')
            print_table(
                [
                    ("ID", "id"), ("From", "mailfrom"), ("To", "recipient"),
                    ("Created", "created_str"), ("Last used", "last_used_str"),
                    ("Comment", "comment"), ("Permanent", "permanent_str")
                ],
                entries.values()
            )
            print("")
            raise RuntimeError(
                "from/to combination is already covered by the entries above, "
                "use --force to override.")

    # add entry to whitelist
    whitelist.add(args.mailfrom, args.recipient, args.comment, args.permanent)
    logger.info("whitelist entry added successfully")


def delete_whitelist_entry(config, args):
    logger = logging.getLogger(__name__)

    whitelist = _get_whitelist_obj(config, args.quarantine)
    if whitelist is None:
        raise RuntimeError(
            "whitelist type is set to None, unable to delete entries")

    whitelist.delete(args.whitelist_id)
    logger.info("whitelist entry deleted successfully")


def notify_email(config, args):
    logger = logging.getLogger(__name__)

    quarantine = _get_quarantine_obj(config, args.quarantine)
    if quarantine is None:
        raise RuntimeError(
            "quarantine type is set to None, unable to send notification")
    quarantine.notify(args.quarantine_id, args.recipient)
    logger.info("sent notification successfully")


def release_email(config, args):
    logger = logging.getLogger(__name__)

    quarantine = _get_quarantine_obj(config, args.quarantine)
    if quarantine is None:
        raise RuntimeError(
            "quarantine type is set to None, unable to release email")

    quarantine.release(args.quarantine_id, args.recipient)
    logger.info("quarantined email released successfully")


def delete_email(config, args):
    logger = logging.getLogger(__name__)

    quarantine = _get_quarantine_obj(config, args.quarantine)
    if quarantine is None:
        raise RuntimeError(
            "quarantine type is set to None, unable to delete email")

    quarantine.delete(args.quarantine_id, args.recipient)
    logger.info("quarantined email deleted successfully")


class StdErrFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.ERROR, logging.WARNING)


class StdOutFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno in (logging.DEBUG, logging.INFO)


def main():
    "PyQuarantine command-line interface."
    # parse command line
    def formatter_class(prog): return argparse.HelpFormatter(
        prog, max_help_position=50, width=140)
    parser = argparse.ArgumentParser(
        description="PyQuarantine CLI",
        formatter_class=formatter_class)
    parser.add_argument(
        "-c", "--config",
        help="Config files to read.",
        nargs="+", metavar="CFG",
        default=pyquarantine.QuarantineMilter.get_configfiles())
    parser.add_argument(
        "-d", "--debug",
        help="Log debugging messages.",
        action="store_true")
    parser.add_argument(
        "-v", "--version",
        help="Print version.",
        action="version",
        version="%(prog)s ({})".format(version))
    parser.set_defaults(syslog=False)
    subparsers = parser.add_subparsers(
        dest="command",
        title="Commands")
    subparsers.required = True

    # list command
    list_parser = subparsers.add_parser(
        "list",
        help="List available quarantines.",
        formatter_class=formatter_class)
    list_parser.add_argument(
        "-b", "--batch",
        help="Print results using only quarantine names, each on a new line.",
        action="store_true")
    list_parser.set_defaults(func=list_quarantines)

    # quarantine command group
    quarantine_parser = subparsers.add_parser(
        "quarantine",
        description="Manage quarantines.",
        help="Manage quarantines.",
        formatter_class=formatter_class)
    quarantine_parser.add_argument(
        "quarantine",
        metavar="QUARANTINE",
        help="Quarantine name.")
    quarantine_subparsers = quarantine_parser.add_subparsers(
        dest="command",
        title="Quarantine commands")
    quarantine_subparsers.required = True
    # quarantine list command
    quarantine_list_parser = quarantine_subparsers.add_parser(
        "list",
        description="List emails in quarantines.",
        help="List emails in quarantine.",
        formatter_class=formatter_class)
    quarantine_list_parser.add_argument(
        "-f", "--from",
        dest="mailfrom",
        help="Filter emails by from address.",
        default=None,
        nargs="+")
    quarantine_list_parser.add_argument(
        "-t", "--to",
        dest="recipients",
        help="Filter emails by recipient address.",
        default=None,
        nargs="+")
    quarantine_list_parser.add_argument(
        "-o", "--older-than",
        dest="older_than",
        help="Filter emails by age (days).",
        default=None,
        type=float)
    quarantine_list_parser.add_argument(
        "-b", "--batch",
        help="Print results using only email quarantine IDs, each on a new line.",
        action="store_true")
    quarantine_list_parser.set_defaults(func=list_quarantine_emails)
    # quarantine notify command
    quarantine_notify_parser = quarantine_subparsers.add_parser(
        "notify",
        description="Notify recipient about email in quarantine.",
        help="Notify recipient about email in quarantine.",
        formatter_class=formatter_class)
    quarantine_notify_parser.add_argument(
        "quarantine_id",
        metavar="ID",
        help="Quarantine ID.")
    quarantine_notify_parser_group = quarantine_notify_parser.add_mutually_exclusive_group(
        required=True)
    quarantine_notify_parser_group.add_argument(
        "-t", "--to",
        dest="recipient",
        help="Release email for one recipient address.")
    quarantine_notify_parser_group.add_argument(
        "-a", "--all",
        help="Release email for all recipients.",
        action="store_true")
    quarantine_notify_parser.set_defaults(func=notify_email)
    # quarantine release command
    quarantine_release_parser = quarantine_subparsers.add_parser(
        "release",
        description="Release email from quarantine.",
        help="Release email from quarantine.",
        formatter_class=formatter_class)
    quarantine_release_parser.add_argument(
        "quarantine_id",
        metavar="ID",
        help="Quarantine ID.")
    quarantine_release_parser.add_argument(
        "-n",
        "--disable-syslog",
        dest="syslog",
        help="Disable syslog messages.",
        action="store_false")
    quarantine_release_parser_group = quarantine_release_parser.add_mutually_exclusive_group(
        required=True)
    quarantine_release_parser_group.add_argument(
        "-t", "--to",
        dest="recipient",
        help="Release email for one recipient address.")
    quarantine_release_parser_group.add_argument(
        "-a", "--all",
        help="Release email for all recipients.",
        action="store_true")
    quarantine_release_parser.set_defaults(func=release_email)
    # quarantine delete command
    quarantine_delete_parser = quarantine_subparsers.add_parser(
        "delete",
        description="Delete email from quarantine.",
        help="Delete email from quarantine.",
        formatter_class=formatter_class)
    quarantine_delete_parser.add_argument(
        "quarantine_id",
        metavar="ID",
        help="Quarantine ID.")
    quarantine_delete_parser.add_argument(
        "-n", "--disable-syslog",
        dest="syslog",
        help="Disable syslog messages.",
        action="store_false")
    quarantine_delete_parser_group = quarantine_delete_parser.add_mutually_exclusive_group(
        required=True)
    quarantine_delete_parser_group.add_argument(
        "-t", "--to",
        dest="recipient",
        help="Delete email for one recipient address.")
    quarantine_delete_parser_group.add_argument(
        "-a", "--all",
        help="Delete email for all recipients.",
        action="store_true")
    quarantine_delete_parser.set_defaults(func=delete_email)

    # whitelist command group
    whitelist_parser = subparsers.add_parser(
        "whitelist",
        description="Manage whitelists.",
        help="Manage whitelists.",
        formatter_class=formatter_class)
    whitelist_parser.add_argument(
        "quarantine",
        metavar="QUARANTINE",
        help="Quarantine name.")
    whitelist_subparsers = whitelist_parser.add_subparsers(
        dest="command",
        title="Whitelist commands")
    whitelist_subparsers.required = True
    # whitelist list command
    whitelist_list_parser = whitelist_subparsers.add_parser(
        "list",
        description="List whitelist entries.",
        help="List whitelist entries.",
        formatter_class=formatter_class)
    whitelist_list_parser.add_argument(
        "-f", "--from",
        dest="mailfrom",
        help="Filter entries by from address.",
        default=None,
        nargs="+")
    whitelist_list_parser.add_argument(
        "-t", "--to",
        dest="recipients",
        help="Filter entries by recipient address.",
        default=None,
        nargs="+")
    whitelist_list_parser.add_argument(
        "-o", "--older-than",
        dest="older_than",
        help="Filter emails by last used date (days).",
        default=None,
        type=float)
    whitelist_list_parser.set_defaults(func=list_whitelist)
    # whitelist add command
    whitelist_add_parser = whitelist_subparsers.add_parser(
        "add",
        description="Add whitelist entry.",
        help="Add whitelist entry.",
        formatter_class=formatter_class)
    whitelist_add_parser.add_argument(
        "-f", "--from",
        dest="mailfrom",
        help="From address.",
        required=True)
    whitelist_add_parser.add_argument(
        "-t", "--to",
        dest="recipient",
        help="Recipient address.",
        required=True)
    whitelist_add_parser.add_argument(
        "-c", "--comment",
        help="Comment.",
        default="added by CLI")
    whitelist_add_parser.add_argument(
        "-p", "--permanent",
        help="Add a permanent entry.",
        action="store_true")
    whitelist_add_parser.add_argument(
        "--force",
        help="Force adding an entry, even if already covered by another entry.",
        action="store_true")
    whitelist_add_parser.set_defaults(func=add_whitelist_entry)
    # whitelist delete command
    whitelist_delete_parser = whitelist_subparsers.add_parser(
        "delete",
        description="Delete whitelist entry.",
        help="Delete whitelist entry.",
        formatter_class=formatter_class)
    whitelist_delete_parser.add_argument(
        "whitelist_id",
        metavar="ID",
        help="Whitelist ID.")
    whitelist_delete_parser.set_defaults(func=delete_whitelist_entry)

    args = parser.parse_args()

    # setup logging
    loglevel = logging.INFO
    root_logger = logging.getLogger()
    root_logger.setLevel(loglevel)

    # setup console log
    if args.debug:
        formatter = logging.Formatter(
            "%(levelname)s: [%(name)s] - %(message)s")
    else:
        formatter = logging.Formatter("%(levelname)s: %(message)s")
    # stdout
    stdouthandler = logging.StreamHandler(sys.stdout)
    stdouthandler.setLevel(logging.DEBUG)
    stdouthandler.setFormatter(formatter)
    stdouthandler.addFilter(StdOutFilter())
    root_logger.addHandler(stdouthandler)
    # stderr
    stderrhandler = logging.StreamHandler(sys.stderr)
    stderrhandler.setLevel(logging.WARNING)
    stderrhandler.setFormatter(formatter)
    stderrhandler.addFilter(StdErrFilter())
    root_logger.addHandler(stderrhandler)
    logger = logging.getLogger(__name__)

    # try to generate milter configs
    try:
        global_config, config = pyquarantine.generate_milter_config(
            config_files=args.config, configtest=True)
    except RuntimeError as e:
        logger.error(e)
        sys.exit(255)

    if args.syslog:
        # setup syslog
        sysloghandler = logging.handlers.SysLogHandler(
            address="/dev/log",
            facility=logging.handlers.SysLogHandler.LOG_MAIL)
        sysloghandler.setLevel(loglevel)
        if args.debug:
            formatter = logging.Formatter(
                "pyquarantine: [%(name)s] [%(levelname)s] %(message)s")
        else:
            formatter = logging.Formatter("pyquarantine: %(message)s")
        sysloghandler.setFormatter(formatter)
        root_logger.addHandler(sysloghandler)

    # call the commands function
    try:
        args.func(config, args)
    except RuntimeError as e:
        logger.error(e)
        sys.exit(1)


if __name__ == "__main__":
    main()

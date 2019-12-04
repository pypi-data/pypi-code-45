"""
Sesh is a tool for managing music classes from the command line.
Copyright (C) 2019  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com

The examples given for the functions below are shown in the context of CLI
commands. However this module is intended to provide an API that may be
used by other interfaces in the future.

The args parameter that is passed into each of these functions is expected
to be a Namepace object, similar to that created by the argparse module in the
Standard Library. For more information on this, please see:

https://docs.python.org/3/library/argparse.html#the-namespace-object
"""

import sys

from sesh import core
from sesh.config.base_config import SESH_COOKIE_FILE
from sesh.enum import UserRole
from sesh.error import ExitCode
from sesh.init_db import _init_db, _load_sample_data

__all__ = ['admin', 'delete', 'login', 'logout', 'new', 'show', 'update']


def check_for_session(args):
    return core._get_active_session(args)


def admin(args, kwargs=None):
    """Administer the Sesh database.

    Args:
        --init-db: Initialize a new database with default values. Any
        existing database for Sesh will be deleted!

        --load-sample-data: Add a reasonably-sized data set of example data,
        for use in testing, or for exploring Sesh without needing to set up
        a whole lot from the start. The only table that will not be populated
        is the login_session table. See the _load_sample_data() function in
        the init_db module for the data set that is loaded.

    Examples:
        sesh admin --init-db
        sesh admin --load-sample-data
        sesh admin --init-db --load-sample-data

    NOTE:
        You must be logged in as a user in a 'Staff' role in order to issue
        these commands.
    """
    username = kwargs.get('username')
    user_role = core._check_user(username)

    if user_role != UserRole.STAFF.value:
        print(
            f"\nYou must be logged-in as a Staff member in order to run "
            f"'admin' commands.\n\n"
        )
        sys.exit(ExitCode.EX_NOPERM)

    if args.init_db:
        _init_db()
        if SESH_COOKIE_FILE.exists():
            SESH_COOKIE_FILE.unlink()

    if args.load_sample_data:
        _load_sample_data()


def delete(args, kwargs=None):
    pass


def set_last_command(cmd):
    core._set_last_command(cmd)


def login(args, kwargs=None):
    """Login to Sesh.

    The user must already have a login account. New accounts must be created
    by a user in a 'Staff' role.

    Once logged-in, the user will remain logged-in until they logout, or until
    five minutes have passed since they last issued a command.

    Only one user may be logged in at a time. Multiple users may be supported
    in a future release.

    Args:
        username: The email address of the user to logout.

    Examples:
        sesh login admin@example.com
    """
    core._login(args.username)


def renew_session(args, kwargs):
    core._renew_session(args, kwargs)


def logout(args, kwargs=None):
    """Logout of Sesh.

    Args:
        username: The email address of the user to logout.

    Examples:
        sesh logout admin@example.com
    """
    core._logout(kwargs)


def new(args, kwargs=None):
    logged_in_user = kwargs.get('username')
    print(
        f"\n{logged_in_user} is creating new target: {args.target}\n\n"
    )
    pass


def rent():
    pass


def show(args, kwargs=None):
    print(f"\nARGS: {args}\n\n")
    pass


def update(args, kwargs=None):
    pass

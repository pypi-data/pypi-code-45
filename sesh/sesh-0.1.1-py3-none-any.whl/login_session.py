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
"""

from datetime import datetime
import shelve
import sqlite3
from uuid import uuid4

from sesh.config.base_config import SESH_DB_PATH, SESH_COOKIE_FILE
from sesh.log import get_logger

logger = get_logger(__name__)


class LoginSession(object):
    """A LoginSession object represents a Sesh user's session.
    An active login session is required in order to run any of the Sesh
    commands. When a session is active, a cookie is placed on the user's
    machine, storing the username, and a unique session token used to
    identify the session. This cookie is deleted when the user logs out.
    """

    def __init__(self, email_addr, kwargs=dict(new_session=False)):
        self._email_addr = email_addr
        self._user_id = None
        self._token = None
        self._time_login = None
        self._last_cmd = None
        self._time_last_cmd = None
        self._time_logout = None

        self._conn = sqlite3.connect(
            SESH_DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES
        )
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

        new_session = kwargs.get('new_session')

        if not new_session:
            self._reconstitute_login_session(kwargs)

    @property
    def email_addr(self):
        return self._email_addr

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        logger.info(f"Setting active session id: {value}")
        self._id = value

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        logger.info(f"Setting active session user_id: {value}")
        self._user_id = value

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        logger.info(f"Setting active session token: {value}")
        self._token = value

    @property
    def time_login(self):
        return self._time_login

    @time_login.setter
    def time_login(self, value):
        logger.info(f"Setting active session time of login: {value}")
        self._time_login = value

    @property
    def last_cmd(self):
        return self._last_cmd

    @last_cmd.setter
    def last_cmd(self, value):
        logger.info(f"Setting active session last command: {value}")
        self._last_cmd = value

    @property
    def time_last_cmd(self):
        return self._time_last_cmd

    @time_last_cmd.setter
    def time_last_cmd(self, value):
        logger.info(f"Setting active session time of last command: {value}")
        self._time_last_cmd = value

    @property
    def time_logout(self):
        return self._time_logout

    @time_logout.setter
    def time_logout(self, value):
        logger.info(f"Setting active session time of logout: {value}")
        self._time_logout = value

    def _reconstitute_login_session(self, kwargs):
        self.token = kwargs.get('token')
        self._cursor.execute(
            """
            SELECT *
            FROM "login_session"
            WHERE "token"=?
            """, (self.token,)
        )
        session = self._cursor.fetchone()

        self.id = session['id']
        self.user_id = session['user_id']
        self.time_login = session['time_login']
        self.last_cmd = session['last_cmd']
        self.time_last_cmd = session['time_last_cmd']

    def login(self):
        # Get id from user table
        self._cursor.execute(
            """
            SELECT "id"
            FROM "user"
            WHERE "email_addr"=?
            """, (self.email_addr,)
        )
        self.user_id = self._cursor.fetchone()[0]
        token = uuid4()
        self.token = str(token)
        self.time_login = datetime.now().timestamp()
        self.last_cmd = f"login user {self.email_addr}"
        self.time_last_cmd = datetime.now().timestamp()

        self._cursor.execute(
            """
            INSERT INTO "login_session"
                (
                    "user_id",
                    "token",
                    "time_login",
                    "last_cmd",
                    "time_last_cmd"
                )
            VALUES (?, ?, ?, ?, ?)
            """, (
                self.user_id,
                self.token,
                self.time_login,
                self.last_cmd,
                self.time_last_cmd
            )
        )
        self._conn.commit()

        with shelve.open(str(SESH_COOKIE_FILE)) as cookie:
            cookie['user'] = self.email_addr
            cookie['token'] = self.token

    def renew_session(self, token, cmd, target):
        if target:
            self.last_cmd = f"{cmd} {target}"
        else:
            self.last_cmd = cmd
        self.time_last_cmd = datetime.now().timestamp()
        self._cursor.execute(
            """
            UPDATE login_session
            SET last_cmd = ?, time_last_cmd = ?
            WHERE token = ?
            """, (self.last_cmd, self.time_last_cmd, self.token)
        )
        self._conn.commit()

    def logout(self):
        cmd = f"logout user {self.email_addr}"
        self.time_logout = datetime.now().timestamp()
        self._cursor.execute(
            """
            UPDATE login_session
            SET last_cmd = ?, time_last_cmd = ?, time_logout = ?
            WHERE token = ?
            """, (cmd, self.time_logout, self.time_logout, self.token)
        )
        self._conn.commit()

        if SESH_COOKIE_FILE.exists():
            SESH_COOKIE_FILE.unlink()

    def set_last_command(self, cmd):
        """
        Update the current session in the database to reflect
        the last command and the time of the last command
        """
        now = datetime.now().timestamp()
        self._cursor.execute(
            """
            UPDATE "login_session"
            SET "last_cmd"=?, "time_last_cmd"=?
            WHERE "token"=?
            """, (cmd, now, self.token)
        )
        self._conn.commit()
        self.last_cmd = cmd

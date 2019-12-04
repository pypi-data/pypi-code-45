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

import sqlite3

from sesh.config.base_config import SESH_DB_PATH
from sesh.log import get_logger
from sesh.login_session import LoginSession

logger = get_logger(__name__)


class User(object):
    """The base User object.

    No Sesh users are actually instantiated from this class directly. Instead,
    this class is subclassed by the Instructor, Staff, and Student classes
    in this module.

    This class holds all of the common attributes and methods of those other
    users.
    """

    def __init__(self, email_addr, kwargs):
        self._email_addr = email_addr
        self._id = None
        self._role_id = kwargs.get('role_id')
        self._name_first = kwargs.get('name_first')
        self._name_last = kwargs.get('name_last')
        self._addr1 = kwargs.get('addr1')
        self._addr2 = kwargs.get('addr2')
        self._addr_city = kwargs.get('addr_city')
        self._addr_state = kwargs.get('addr_state')
        self._addr_zip = kwargs.get('addr_zip')
        self._phone_number = kwargs.get('phone')
        self._datetime_added = kwargs.get('datetime_added')
        self._login_session = None

        new = kwargs.get('new')

        self._conn = sqlite3.connect(
            SESH_DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES
        )
        self._conn.row_factory = sqlite3.Row
        self._cursor = self._conn.cursor()

        if new:
            self.id = None
            self.role_id = kwargs.get('role_id')
            self.name_first = kwargs.get('name_first')
            self.name_last = kwargs.get('name_last')
            self.addr1 = kwargs.get('addr1')
            self.addr2 = kwargs.get('addr2')
            self.addr_city = kwargs.get('addr_city')
            self.addr_state = kwargs.get('addr_state')
            self.addr_zip = kwargs.get('addr_zip')
            self.phone_number = kwargs.get('phone')
            self.datetime_added = kwargs.get('datetime_added')
            self.login_session = None
        else:
            self._reconstitute_user()

        self._init_login_session(kwargs)

    @property
    def id(self):
        """int: The user id. Auto-incremented and assigned by the database."""
        return self._id

    @id.setter
    def id(self, value):
        if self._id is None:
            self._id = value
        else:
            logger.error(
                f"This user already has an id of {self.id}. "
                f"Once set, id cannot be changed. Discarding id {value}."
            )

    @property
    def role_id(self):
        """int: The role id. Maps to the UserRole enum class in the
        sesh.enum module and the enum_role table in the database.
        """
        return self._role_id

    @role_id.setter
    def role_id(self, value):
        logger.info(f"Setting role_id for user {self.id} to {value}")
        self._role_id = value

    @property
    def name_first(self):
        """str: The given name of the user."""
        return self._name_first

    @name_first.setter
    def name_first(self, value):
        logger.info(f"Setting first name for user {self.id} to {value}")
        self._name_first = value

    @property
    def name_last(self):
        """str: The surname of the user."""
        return self._name_last

    @name_last.setter
    def name_last(self, value):
        logger.info(f"Setting last name for user {self.id} to {value}")
        self._name_last = value

    @property
    def addr1(self):
        """str: The first line of the user's address. Typically, this is
        the Street Number and Street Name"""
        return self._addr1

    @addr1.setter
    def addr1(self, value):
        logger.info(f"Setting address line 1 for user {self.id} to {value}")
        self._addr1 = value

    @property
    def addr2(self):
        """str: The second line of the user's address. Typically, this is
        optional and is used to identify an Appartment or Suite number."""
        return self._addr2

    @addr2.setter
    def addr2(self, value):
        if value is not None or value != '':
            logger.info(
                f"Setting address line 2 for user {self.id} to {value}"
            )
            self._addr2 = value

    @property
    def addr_city(self):
        """str: The city of the user's address."""
        return self._addr_city

    @addr_city.setter
    def addr_city(self, value):
        logger.info(f"Setting city for user {self.id} to {value}")
        self._addr_city = value

    @property
    def addr_state(self):
        """str: The state of the user's address."""
        return self._addr_state

    @addr_state.setter
    def addr_state(self, value):
        logger.info(f"Setting state for user {self.id} to {value}")
        self._addr_state = value

    @property
    def addr_zip(self):
        """str: The zipcode of the user's address. This may be represented in
        either the 5-digit or the 9-digit format."""
        return self._addr_zip

    @addr_zip.setter
    def addr_zip(self, value):
        logger.info(f"Setting zip code for user {self.id} to {value}")
        self._addr_zip = value

    @property
    def email_addr(self):
        """str: The user's email address. This also serves as the username for
        their login."""
        return self._email_addr

    @email_addr.setter
    def email_addr(self, value):
        logger.info(f"Setting email address for user {self.id} to {value}")
        self._email_addr = value

    @property
    def phone_number(self):
        """str: A phone number for the user. Currently, any format is
        supported, but that may change in a future release. The preferred
        format is aaa-ppp-nnnn where 'aaa' is the Area Code, 'ppp' is the
        prefix, and 'nnnn' is the remainder of the number."""
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        logger.info(f"Setting phone number for user {self.id} to {value}")
        self._phone_number = value

    @property
    def datetime_added(self):
        """datetime: The date and time when the user was created."""
        return self._datetime_added

    @datetime_added.setter
    def datetime_added(self, value):
        if self._datetime_added is None:
            self._datetime_added = value
        else:
            logger.error(
                f"This user was already added at {self.datetime_added}. "
                f"Once set, datetime_added cannot be changed. "
                f"Discarding id {value}."
            )

    @property
    def login_session(self):
        """:obj: `LoginSession`: An instance of the LoginSession class, from
        the `login_session` module, representing a Sesh user's session. An
        active login session is required in order to run any of the Sesh
        commands. When a session is active, a cookie is placed on the user's
        machine, storing the username, and a unique session token used to
        identify the session. This cookie is deleted when the user logs out."""
        return self._login_session

    def _reconstitute_user(self):
        self._cursor.execute(
            """
            SELECT *
            FROM "User"
            WHERE "email_addr"=?
            """, (self.email_addr,)
        )
        user = self._cursor.fetchone()

        self.id = user['id']
        self.role_id = user['role_id']
        self.name_first = user['name_first']
        self.name_last = user['name_last']
        self.addr1 = user['addr1']
        self.addr2 = user['addr2']
        self.addr_city = user['addr_city']
        self.addr_state = user['addr_state']
        self.addr_zip = user['addr_zip']
        self.phone_number = user['phone_number']
        self.datetime_added = user['datetime_added']

    def _init_login_session(self, kwargs):
        self._login_session = LoginSession(self.email_addr, kwargs)

    def _login(self):
        self.login_session.login()

    def _renew_session(self, token, cmd, target):
        self.login_session.renew_session(token, cmd, target)

    def _logout(self):
        self.login_session.logout()


class Instructor(User):
    """Represents an Instructor User

    TODO:
        These attributes are not yet read from or written to the database.
        The sample data set contains values for these attributes, but they
        are not yet mapped to this object.
    """

    def __init__(self, email_addr, kwargs=dict()):
        super(Instructor, self).__init__(email_addr, kwargs)
        self._specialties = kwargs.get('specialties')
        self._availability = kwargs.get('availability')


class Staff(User):
    """Represents a Staff User

    A Staff user is anyone working in an administrative capacity at the
    Music Center - they are not Intructors. Currently, there is no way for
    a user to hold multiple roles. Multi-role capabilities may be added in
    a future release.

    TODO:
        These attributes are not yet read from or written to the database.
        The sample data set contains values for these attributes, but they
        are not yet mapped to this object.
    """

    def __init__(self, email_addr, kwargs=dict()):
        super(Staff, self).__init__(email_addr, kwargs)
        self._title = kwargs.get('title')


class Student(User):
    """Represents an Student User

    TODO:
        These attributes are not yet read from or written to the database.
        The sample data set contains values for these attributes, but they
        are not yet mapped to this object.
    """

    def __init__(self, email_addr, kwargs=dict()):
        super(Student, self).__init__(email_addr, kwargs)
        self._account_balance = kwargs.get('account_balance')
        self._instruments = kwargs.get('instruments')

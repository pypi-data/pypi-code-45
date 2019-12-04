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

This module is used to initialize a new instance of the Sesh database. During
the initialization process, any previous Sesh database will be DELETED.

This module also holds sample data and the functions to load that data into
the database, if desired.
"""

from datetime import datetime, date, time
from hashlib import sha256
import random
import sqlite3
import string
from textwrap import dedent

from sesh.config.base_config import SESH_DB_PATH, SESH_ADMIN_FILE
from sesh.error import ExitCode


def adapt_time(time):
    return time.isoformat('minutes')


sqlite3.register_adapter(time, adapt_time)


def _get_conn_cursor():
    conn = sqlite3.connect(SESH_DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    return conn, cursor


def _init_db():
    # If there is an existing database, delete it.
    if SESH_DB_PATH.exists():
        SESH_DB_PATH.unlink()

    conn, cursor = _get_conn_cursor()
    _create_tables(conn, cursor)
    _load_default_data(conn, cursor)

    conn.close()

    return ExitCode.EX_SUCCESS


def _create_tables(conn, cursor):
    cursor.executescript(
        """
        CREATE TABLE "class_session"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "instructor_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "student_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "classroom_id" INTEGER NOT NULL
                REFERENCES "classroom" ("id") DEFERRABLE INITIALLY DEFERRED,
            "session_start" DATETIME NOT NULL,
            "session_stop" DATETIME NOT NULL,
            "instrument_id" INTEGER NOT NULL
                REFERENCES "enum_instrument" ("id")
                DEFERRABLE INITIALLY DEFERRED,
            "recording" BOOLEAN NOT NULL DEFAULT 0,
            "canceled" BOOLEAN NOT NULL DEFAULT 0,
            "amt_billed" DOUBLE NOT NULL DEFAULT 0.00,
            "amt_paid" DOUBLE NOT NULL DEFAULT 0.00
        );

        CREATE TABLE "classroom"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "location" VARCHAR(32) UNIQUE,
            "piano" BOOLEAN NOT NULL DEFAULT 0,
            "recording_capable" BOOLEAN NOT NULL DEFAULT 0
        );

        CREATE TABLE "classroom_avail"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "classroom_id" INTEGER NOT NULL
                REFERENCES "classroom" ("id") DEFERRABLE INITIALLY DEFERRED,
            "day_id" INTEGER NOT NULL
                REFERENCES "enum_day" ("id") DEFERRABLE INITIALLY DEFERRED,
            "time_start" DATETIME,
            "time_end" DATETIME,
            "active" BOOLEAN NOT NULL DEFAULT 1
        );

        CREATE TABLE "enum_day"(
            "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "day" VARCHAR(9) NOT NULL
        );

        CREATE TABLE "enum_instrument"(
            "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "instrument" VARCHAR(32) NOT NULL
        );

        CREATE TABLE "enum_role"(
            "id" INTEGER NOT NULL PRIMARY KEY UNIQUE,
            "name" VARCHAR(32) NOT NULL,
            "description" VARCHAR(300) NOT NULL
        );

        CREATE TABLE "instructor_avail"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "day_id" INTEGER NOT NULL
                REFERENCES "enum_day" ("id") DEFERRABLE INITIALLY DEFERRED,
            "time_start" DATETIME,
            "time_end" DATETIME,
            "active" BOOLEAN NOT NULL DEFAULT 1
        );

        CREATE TABLE "instructor_spec"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "specialty" INTEGER NOT NULL
                REFERENCES "inst_enum" ("id") DEFERRABLE INITIALLY DEFERRED
        );

        CREATE TABLE "login_session"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "token" VARCHAR(128) NOT NULL UNIQUE,
            "time_login" REAL NOT NULL,
            "last_cmd" VARCHAR(64),
            "time_last_cmd" REAL,
            "time_logout" REAL
        );

        CREATE TABLE "rental"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "inv_tag" VARCHAR(64) NOT NULL
                REFERENCES "rental_inventory" ("inv_tag")
                DEFERRABLE INITIALLY DEFERRED,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "date_start" DATE NOT NULL,
            "date_end" DATE
        );

        CREATE TABLE "rental_inventory"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "instrument_id" VARCHAR(32) NOT NULL
                REFERENCES "enum_instrument" ("id")
                DEFERRABLE INITIALLY DEFERRED,
            "model" VARCHAR(128) NOT NULL,
            "inv_tag" VARCHAR(64) NOT NULL UNIQUE,
            "rental_fee" DOUBLE NOT NULL
        );

        CREATE TABLE "staff"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "title" VARCHAR(32)
        );

        CREATE TABLE "student"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "user_id" INTEGER NOT NULL
                REFERENCES "user" ("id") DEFERRABLE INITIALLY DEFERRED,
            "account_balance" DOUBLE NOT NULL DEFAULT 0.0
        );

        CREATE TABLE "user"(
            "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            "datetime_added" DATETIME NOT NULL,
            "role_id" INTEGER NOT NULL
                REFERENCES "enum_role" ("id") DEFERRABLE INITIALLY DEFERRED,
            "name_first" VARCHAR(30) NOT NULL,
            "name_last" VARCHAR(60),
            "addr1" VARCHAR(250),
            "addr2" VARCHAR(250),
            "addr_city" VARCHAR(64),
            "addr_state" VARCHAR(2),
            "addr_zip" VARCHAR(20),
            "email_addr" VARCHAR(250) NOT NULL,
            "phone_number" VARCHAR(12),
            "password" VARCHAR(128) NOT NULL
        );
        """
    )
    conn.commit()


def _load_default_data(conn, cursor):
    _load_enum_day(conn, cursor)
    _load_enum_instrument(conn, cursor)
    _load_enum_roles(conn, cursor)
    _load_default_user(conn, cursor)


def _load_enum_day(conn, cursor):
    enum_day = [
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    ]
    cursor.executemany(
        """
        INSERT INTO "enum_day" ("id", "day")
        VALUES (?, ?)
        """, enum_day)
    conn.commit()


def _load_enum_instrument(conn, cursor):
    enum_instrument = [
        (1, "Cello"),
        (2, "Clarinet"),
        (3, "Didgeridoo"),
        (4, "Guitar"),
        (5, "Drum Kit"),
        (6, "Piano"),
        (7, "Saxophone"),
        (8, "Trumpet"),
        (9, "Violin"),
        (10, "Voice")
    ]
    cursor.executemany(
        """
        INSERT INTO "enum_instrument" ("id", "instrument")
        VALUES (?, ?)
        """, enum_instrument
    )
    conn.commit()


def _load_enum_roles(conn, cursor):
    default_roles = [
        (1, "Staff", "Music Center Administrative Staff"),
        (2, "Instructor", "Music Center Instructor"),
        (3, "Student", "Music Center Student")
    ]
    cursor.executemany(
        """
        INSERT INTO "enum_role" ("id", "name", "description")
        VALUES (?, ?, ?)
        """, default_roles
    )
    conn.commit()


def _load_default_user(conn, cursor):
    datetime_added = datetime.now().replace(second=0, microsecond=0)
    role_id = 1
    name_first = "Admin"
    name_last = "ChangeMe"
    email_addr = "admin@example.com"
    pw_length = 12
    pw = ''.join(
        random.choices(
            string.ascii_letters +
            string.digits +
            string.punctuation,
            k=pw_length
        ))
    pw_hash = sha256(pw.encode('utf-8')).hexdigest()

    with open(SESH_ADMIN_FILE, 'w') as f:
        f.write(pw)

    cursor.execute(
        """
        INSERT INTO "user"
            (
                "datetime_added",
                "role_id",
                "name_first",
                "name_last",
                "email_addr",
                "password"
            )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            datetime_added,
            role_id,
            name_first,
            name_last,
            email_addr,
            pw_hash
        ))

    cursor.execute(
        """
        INSERT INTO "staff" ("user_id", "title")
        VALUES (?, ?)
        """, (cursor.lastrowid, "Staff Administrator")
    )
    conn.commit()

    print(dedent(
        f"""

        An admin user has been created in the database.
        The initial password for this user can be found in the file
        located at {SESH_ADMIN_FILE}.

        The login name is {email_addr}

        Please login now and update that user with your information and
        change the password!!!


        """
    ))


def _load_sample_data():
    conn, cursor = _get_conn_cursor()

    _load_sample_classrooms(conn, cursor)
    _load_sample_staff(conn, cursor)
    _load_sample_instructors(conn, cursor)
    _load_sample_students(conn, cursor)
    _load_sample_instruments(conn, cursor)
    _load_sample_rentals(conn, cursor)
    _load_sample_class_sessions(conn, cursor)

    conn.close()


def _load_classroom(conn, cursor, classroom):
    cursor.execute(
        """
        INSERT INTO "classroom"(
            "location",
            "piano",
            "recording_capable"
        )
        VALUES (?, ?, ?)
        """,
        classroom
    )
    conn.commit()

    return cursor.lastrowid


def _load_sample_classrooms(conn, cursor):
    classrooms = [
        ("N1", True, True),
        ("S1", False, True),
        ("E1", False, False),
        ("W1", False, False),
        ("W2", False, False)
    ]

    availability = [
        {
            0: {"time_start": time(9), "time_end": time(21)},
            1: {"time_start": time(9), "time_end": time(21)},
            2: {"time_start": time(9), "time_end": time(21)},
            3: {"time_start": time(9), "time_end": time(21)},
            4: {"time_start": time(9), "time_end": time(21)},
            5: {"time_start": time(9), "time_end": time(21)},
            6: {"time_start": time(9), "time_end": time(21)},
        },
        {
            0: {"time_start": time(9), "time_end": time(21)},
            1: {"time_start": time(9), "time_end": time(21)},
            2: {"time_start": time(9), "time_end": time(21)},
            3: {"time_start": time(9), "time_end": time(21)},
            4: {"time_start": time(9), "time_end": time(21)},
            5: {"time_start": time(9), "time_end": time(21)},
            6: {"time_start": time(9), "time_end": time(21)},
        },
        {
            0: {"time_start": time(9), "time_end": time(21)},
            1: {"time_start": time(9), "time_end": time(21)},
            2: {"time_start": time(9), "time_end": time(21)},
            3: {"time_start": time(9), "time_end": time(21)},
            4: {"time_start": time(9), "time_end": time(21)},
            5: {"time_start": time(9), "time_end": time(21)},
            6: {"time_start": time(9), "time_end": time(21)},
        },
        {
            0: {"time_start": time(9), "time_end": time(21)},
            1: {"time_start": time(9), "time_end": time(21)},
            2: {"time_start": time(9), "time_end": time(21)},
            3: {"time_start": time(9), "time_end": time(21)},
            4: {"time_start": time(9), "time_end": time(21)},
            5: {"time_start": time(9), "time_end": time(21)},
            6: {"time_start": time(9), "time_end": time(21)},
        },
        {
            0: {"time_start": time(9), "time_end": time(21)},
            1: {"time_start": time(9), "time_end": time(21)},
            2: {"time_start": time(9), "time_end": time(21)},
            3: {"time_start": time(9), "time_end": time(21)},
            4: {"time_start": time(9), "time_end": time(21)},
            5: {"time_start": time(9), "time_end": time(21)},
            6: {"time_start": time(9), "time_end": time(21)}
        }
    ]

    for i, classroom in enumerate(classrooms):
        # Populate the "classroom" table, listing each classroom's
        # location, whether or not it has a piano, and
        # whether or not it has recording capabiliites.
        classroom_id = _load_classroom(conn, cursor, classroom)

        # Populate the "classroom_avail" table, listing each classroom's
        # availability.
        for day, avail in availability[i].items():
            cursor.execute(
                """
                INSERT INTO "classroom_avail"
                    (
                        "classroom_id",
                        "day_id",
                        "time_start",
                        "time_end",
                        "active"
                    )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    classroom_id, day, avail['time_start'], avail['time_end'],
                    True
                )
            )
            conn.commit()


def _load_sample_user(conn, cursor, user):
    cursor.execute(
        """
        INSERT INTO "user"(
            "datetime_added",
            "role_id",
            "name_first",
            "name_last",
            "addr1",
            "addr2",
            "addr_city",
            "addr_state",
            "addr_zip",
            "email_addr",
            "phone_number",
            "password"
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        user
    )
    conn.commit()

    return cursor.lastrowid


def _load_sample_staff(conn, cursor):
    # Sample user password is mUs1caL*
    sample_staff_users = [
        (
            datetime(2019, 7, 2, 12).replace(second=0, microsecond=0),
            1,
            "Jeffrey",
            "Lebowski",
            "1642 Sunset Boulevard",
            None,
            "Los Angeles",
            "CA",
            "90210",
            "one.chillindude@live.com",
            "310-848-9325‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 7, 2, 12).replace(second=0, microsecond=0),
            1,
            "Kurt",
            "Gödel",
            "1 Einstein Drive",
            None,
            "Princeton",
            "NJ",
            "08540",
            "kgodel@live.com",
            "703-821-9316‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 7, 2, 12).replace(second=0, microsecond=0),
            1,
            "Margot",
            "Tenenbaum",
            "Central Park West at 79th Street",
            None,
            "New York",
            "NY",
            "10024",
            "margot.frolics@outlook.com",
            "703-506-9102",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        )
    ]

    sample_titles = [
        "Owner",
        "Accountant",
        "Head Instructor"
    ]

    for i, user in enumerate(sample_staff_users):
        user_id = _load_sample_user(conn, cursor, user)
        cursor.execute(
            """
            INSERT INTO "staff" ("user_id", "title")
            VALUES (?, ?)
            """,
            (user_id, sample_titles[i])
        )
        conn.commit()


def _load_sample_instructors(conn, cursor):
    # Sample user password is mUs1caL*
    sample_instructor_users = [
        (
            datetime(2019, 7, 2, 12).replace(second=0, microsecond=0),
            2,
            "Nathan",
            "Muir",
            "8200 Georgetown Pike",
            None,
            "McLean",
            "VA",
            "22102",
            "old.scotch@outlook.com",
            "703-656-6916‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 7, 5, 10).replace(second=0, microsecond=0),
            2,
            "Tom",
            "Bishop",
            "11110 Georgetown Pike",
            None,
            "Great Falls",
            "VA",
            "22066",
            "smugglebishop@yahoo.com",
            "‭703-255-1001",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 7, 31, 14).replace(second=0, microsecond=0),
            2,
            "Ziva",
            "David",
            "1051 Waverly Way",
            None,
            "McLean",
            "VA",
            "22101",
            "ziva.sings@yahoo.com",
            "‭703-821-0022‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 6, 10).replace(second=0, microsecond=0),
            2,
            "Edward",
            "Lewis",
            "1912 37th St NW",
            None,
            "Washington",
            "DC",
            "20007",
            "edward.lewis@trove.fm",
            "202-382-2242",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 6, 10).replace(second=0, microsecond=0),
            2,
            "Etheline",
            "Tenenbaum",
            "3030 K St NW",
            "Ph 217",
            "Washington",
            "DC",
            "20007",
            "etheline@trove.fm",
            "202-382-1234",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 10, 11, 10).replace(second=0, microsecond=0),
            2,
            "Jules",
            "Winnfield",
            "1000 Wilhelm Dr",
            None,
            "Great Falls",
            "VA",
            "22066",
            "jules@trove.fm",
            "703-448-6232",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        )
    ]

    specialties = [
        [6, 4],
        [3, 5],
        [1, 4, 10],
        [1, 9],
        [2, 6],
        [7, 8]
    ]

    availability = [
        {
            0: {"time_start": time(9), "time_end": time(18)},
            1: {"time_start": time(9), "time_end": time(18)},
            2: {"time_start": time(9), "time_end": time(18)},
            3: {"time_start": time(9), "time_end": time(18)},
            4: {"time_start": time(9), "time_end": time(18)},
        },
        {
            0: {"time_start": time(10), "time_end": time(19)},
            1: {"time_start": time(13), "time_end": time(21)},
            2: {"time_start": time(13), "time_end": time(17)},
            3: {"time_start": time(9), "time_end": time(18)},
            5: {"time_start": time(10), "time_end": time(19)},
        },
        {
            1: {"time_start": time(9), "time_end": time(18)},
            2: {"time_start": time(9), "time_end": time(14)},
            3: {"time_start": time(9), "time_end": time(15)},
            4: {"time_start": time(9), "time_end": time(18)},
            6: {"time_start": time(12), "time_end": time(18)}
        },
        {
            0: {"time_start": time(9), "time_end": time(18)},
            1: {"time_start": time(9), "time_end": time(18)},
            2: {"time_start": time(9), "time_end": time(18)},
            3: {"time_start": time(9), "time_end": time(18)},
            4: {"time_start": time(9), "time_end": time(18)},
        },
        {
            0: {"time_start": time(10), "time_end": time(19)},
            1: {"time_start": time(13), "time_end": time(21)},
            2: {"time_start": time(13), "time_end": time(17)},
            3: {"time_start": time(9), "time_end": time(18)},
            5: {"time_start": time(10), "time_end": time(19)},
        },
        {
            1: {"time_start": time(9), "time_end": time(18)},
            2: {"time_start": time(9), "time_end": time(14)},
            3: {"time_start": time(9), "time_end": time(15)},
            4: {"time_start": time(9), "time_end": time(18)},
            6: {"time_start": time(12), "time_end": time(18)}
        }
    ]

    for i, user in enumerate(sample_instructor_users):
        # Populate the "instrcutor_spec" table, listing each instructor's
        # musical specialties.
        user_id = _load_sample_user(conn, cursor, user)
        for spec_id in specialties[i]:
            cursor.execute(
                """
                INSERT INTO "instructor_spec" ("user_id", "specialty")
                VALUES (?, ?)
                """,
                (user_id, spec_id)
            )
            conn.commit()

        # Populate the "instrcutor_avail" table, listing each instructor's
        # availability.
        for day, avail in availability[i].items():
            cursor.execute(
                """
                INSERT INTO "instructor_avail"
                    ("user_id", "day_id", "time_start", "time_end", "active")
                VALUES (?, ?, ?, ?, ?)
                """,
                (user_id, day, avail['time_start'], avail['time_end'], True)
            )
            conn.commit()


def _load_sample_students(conn, cursor):
    # Sample user password is mUs1caL*
    sample_student_users = [
        (
            datetime(2019, 8, 1, 10, 1).replace(second=0, microsecond=0),
            3,
            "Robert",
            "Angier",
            "420 Live Oak Drive",
            None,
            "McLean",
            "VA",
            "22101",
            "amazing.angier@outlook.com",
            "703-356-4567",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 8, 1, 12, 30).replace(second=0, microsecond=0),
            3,
            "Rick",
            "Blaine",
            "1800 Old Meadow Drive",
            "Apt. 933",
            "McLean",
            "VA",
            "22102",
            "richard.blaine57@yahoo.com",
            "571-236-0981‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 8, 2, 9, 42).replace(second=0, microsecond=0),
            3,
            "Jason",
            "Bourne",
            "793 Stephanie Circle",
            None,
            "Great Falls",
            "VA",
            "22066",
            "jb@trove.fm",
            "‭571-236-1150‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 8, 2, 9, 58).replace(second=0, microsecond=0),
            3,
            "Holly",
            "Golightly",
            "3053 P Street NW",
            "Apt. 5",
            "Washington",
            "DC",
            "20007",
            "boughsof.holly@outlook.com",
            "‭202-426-6592‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 8, 9, 10, 10).replace(second=0, microsecond=0),
            3,
            "Dana",
            "Scully",
            "2027 N Dinwiddie St",
            None,
            "Arlington",
            "VA",
            "22207",
            "doc.scully@trove.fm",
            "‭703-821-9317‬",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 5, 16, 20).replace(second=0, microsecond=0),
            3,
            "Penny",
            "Lane",
            "102 Kingsley Rd SE",
            None,
            "Vienna",
            "VA",
            "22180",
            "penny.lane@trove.fm",
            "703-587-9234",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 5, 16, 42).replace(second=0, microsecond=0),
            3,
            "William",
            "Miller",
            "8220 Crestwood Heights Dr",
            "#618",
            "McLean",
            "VA",
            "22102",
            "william.miller@trove.fm",
            "571-236-8456",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 10, 14, 14).replace(second=0, microsecond=0),
            3,
            "Lester",
            "Bangs",
            "4831 Little Falls Rd",
            None,
            "Arlington",
            "VA",
            "22207",
            "lester.bangs@trove.fm",
            "571-236-4875",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 9, 20, 10, 5).replace(second=0, microsecond=0),
            3,
            "Frank",
            "Abagnale, Jr.",
            "3525 Winfield Ln NW",
            None,
            "Washington",
            "DC",
            "20007",
            "frank.abagnale@trove.fm",
            "202-382-1270",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 10, 4, 9, 38).replace(second=0, microsecond=0),
            3,
            "Caroline",
            "Clairmont",
            "3020 Dent Pl NW",
            "Unit 32W",
            "Washington",
            "DC",
            "20007",
            "caroline.clairmont@trove.fm",
            "202-382-9998",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 10, 4, 10, 8).replace(second=0, microsecond=0),
            3,
            "Violet",
            "Sanford",
            "3601 Wisconsin Ave NW",
            "#501",
            "Washington",
            "DC",
            "20016",
            "violet.sanford@trove.fm",
            "202-512-4422",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 10, 8, 10, 32).replace(second=0, microsecond=0),
            3,
            "Claire",
            "Kuchever",
            "3618 Connecticut Ave NW",
            "#405",
            "Washington",
            "DC",
            "20008",
            "claire.kuchever@trove.fm",
            "202-512-0008",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 10, 24, 15, 50).replace(second=0, microsecond=0),
            3,
            "Doug",
            "Carlin",
            "3651 Winfield Ln NW",
            None,
            "Washington",
            "DC",
            "20007",
            "doug.carlin@trove.fm",
            "202-382-9127",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 11, 1, 9, 15).replace(second=0, microsecond=0),
            3,
            "Korben",
            "Dallas",
            "1200 N Nash St",
            "#551",
            "Arlington",
            "VA",
            "22209",
            "korben.dallas@trove.fm",
            "703-338-5979",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 11, 5, 14).replace(second=0, microsecond=0),
            3,
            "Leeloo",
            None,
            "2001 15th St N",
            "#1506",
            "Arlington",
            "VA",
            "22201",
            "leeloo@trove.fm",
            "571-236-3234",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 11, 7, 14, 22).replace(second=0, microsecond=0),
            3,
            "Craig",
            "Jones",
            "1746 Great Falls St",
            None,
            "McLean",
            "VA",
            "22101",
            "craig.jones@trove.fm",
            "571-236-5515",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        ),
        (
            datetime(2019, 11, 7, 16, 20).replace(second=0, microsecond=0),
            3,
            "Smokey",
            None,
            "7887 Jones Branch Dr",
            "#1602",
            "McLean",
            "VA",
            "22102",
            "smokey@trove.fm",
            "571-236-6677",
            "f8691f96be6422505f3a0078c8071b1b0e0201356b20168804436bd26431ae39"
        )
    ]

    sample_account_balance = [
        0.0,
        -80.0,
        0.0,
        200.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        200.0,
        0.0,
        0.0,
        0.0,
        0.0,
        -40.0
    ]

    for i, user in enumerate(sample_student_users):
        user_id = _load_sample_user(conn, cursor, user)
        cursor.execute(
            """
            INSERT INTO "student" ("user_id", "account_balance")
            VALUES (?, ?)
            """,
            (user_id, sample_account_balance[i])
        )
        conn.commit()


def _load_sample_instruments(conn, cursor):
    sample_instruments = [
        (1, "Cecilio CCO-500", "TRV-INS-001", 30.0),
        (1, "Merano CL500-MP", "TRV-INS-002", 30.0),
        (1, "D Z Strad Model 150", "TRV-INS-003", 40.0),
        (1, "Andreas Eastman VC305", "TRV-INS-004", 40.0),
        (2, "Jean Paul USA CL-300", "TRV-INS-005", 30.0),
        (2, "Cecilio MCT-30", "TRV-INS-006", 30.0),
        (2, "Cecilio CT-480", "TRV-INS-007", 40.0),
        (2, "Selmer CL211", "TRV-INS-008", 40.0),
        (3, "Large Earl Clements 5494", "TRV-INS-009", 20.0),
        (3, "Arnhemland Buwathay Munyarryun Yidaki 5269", "TRV-INS-010", 40.0),
        (4, "Blueridge BR-70", "TRV-INS-011", 20.0),
        (4, "Blueridge BR-70", "TRV-INS-012", 20.0),
        (4, "Fender CF-60", "TRV-INS-013", 20.0),
        (4, "Yamaha AC3R", "TRV-INS-014", 30.0),
        (4, "Martin DCPA4 Rosewood", "TRV-INS-015", 40.0),
        (5, "Pearl Roadshow RS525WFC", "TRV-INS-016", 30.0),
        (5, "Mendini Junior Drum Set", "TRV-INS-017", 10.0),
        (5, "Gammon Percussion Full Size", "TRV-INS-018", 30.0),
        (7, "Yamaha YAS-280", "TRV-INS-019", 30.0),
        (7, "Kaizer ASAX-1000LQ", "TRV-INS-020", 30.0),
        (7, "Jupiter JAS1100SG", "TRV-INS-021", 40.0),
        (8, "Yamaha YTR-2330S", "TRV-INS-022", 30.0),
        (8, "Yamaha YTR-2330S", "TRV-INS-023", 30.0),
        (8, "Getzen 590S-S", "TRV-INS-024", 30.0),
        (8, "Bach Stradivarius 180S37", "TRV-INS-025", 40.0),
        (9, "Kennedy Bunnel Pupil", "TRV-INS-026", 30.0),
        (9, "Fiddlerman Artist", "TRV-INS-027", 30.0),
        (9, "Franz Hoffmann Amadeus", "TRV-INS-028", 30.0)
    ]

    cursor.executemany(
        """
        INSERT INTO "rental_inventory"(
            "instrument_id",
            "model",
            "inv_tag",
            "rental_fee"
        )
        VALUES (?, ?, ?, ?)
        """,
        sample_instruments
    )
    conn.commit()


def _load_sample_rentals(conn, cursor):
    rentals = [
        ("TRV-INS-004", 8, date(2019, 8, 1)),
        ("TRV-INS-009", 10, date(2019, 8, 5)),
        ("TRV-INS-012", 12, date(2019, 8, 9)),
        ("TRV-INS-015", 17, date(2019, 9, 5)),
        ("TRV-INS-016", 19, date(2019, 9, 20)),
        ("TRV-INS-026", 20, date(2019, 10, 4)),
        ("TRV-INS-005", 22, date(2019, 10, 8)),
        ("TRV-INS-025", 23, date(2019, 10, 24)),
        ("TRV-INS-014", 24, date(2019, 11, 1)),
        ("TRV-INS-010", 25, date(2019, 11, 5)),
        ("TRV-INS-018", 26, date(2019, 11, 7)),
        ("TRV-INS-019", 27, date(2019, 11, 7))
    ]
    cursor.executemany(
        """
        INSERT INTO "rental" ("inv_tag", "user_id", "date_start")
        VALUES (?, ?, ?)
        """,
        rentals
    )
    conn.commit()


def _load_sample_class_sessions(conn, cursor):
    class_sessions = [
        (7, 8, 3, datetime(2019, 8, 1, 14), datetime(2019, 8, 1, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 8, 2, 16), datetime(2019, 8, 2, 17),
            6, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 8, 5, 10), datetime(2019, 8, 5, 11),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 8, 8, 14), datetime(2019, 8, 8, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 8, 9, 14), datetime(2019, 8, 9, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 8, 9, 14), datetime(2019, 8, 9, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 8, 12, 14), datetime(2019, 8, 12, 15),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 8, 15, 14), datetime(2019, 8, 15, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 8, 16, 14), datetime(2019, 8, 16, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 8, 16, 14), datetime(2019, 8, 16, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 8, 19, 14), datetime(2019, 8, 19, 15),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 8, 22, 14), datetime(2019, 8, 22, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 8, 23, 14), datetime(2019, 8, 23, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 8, 23, 14), datetime(2019, 8, 23, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 8, 26, 14), datetime(2019, 8, 26, 15),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 8, 29, 14), datetime(2019, 8, 29, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 8, 30, 14), datetime(2019, 8, 30, 15),
            6, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 8, 30, 14), datetime(2019, 8, 30, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 9, 3, 14), datetime(2019, 9, 3, 15),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 9, 5, 14), datetime(2019, 9, 5, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 9, 6, 10), datetime(2019, 9, 6, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 9, 6, 9), datetime(2019, 9, 6, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 9, 6, 14), datetime(2019, 9, 6, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 9, 6, 14), datetime(2019, 9, 6, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 9, 10, 14), datetime(2019, 9, 10, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 9, 11, 11), datetime(2019, 9, 11, 12),
            3, 0, 1, 0.0, 0.0),
        (7, 8, 3, datetime(2019, 9, 12, 14), datetime(2019, 9, 12, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 9, 13, 10), datetime(2019, 9, 13, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 9, 13, 9), datetime(2019, 9, 13, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 9, 13, 14), datetime(2019, 9, 13, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 9, 13, 14), datetime(2019, 9, 13, 15),
            6, 0, 1, 40.0, 0.0),
        (6, 10, 5, datetime(2019, 9, 17, 14), datetime(2019, 9, 17, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 9, 18, 11), datetime(2019, 9, 18, 12),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 9, 19, 14), datetime(2019, 9, 19, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 9, 20, 10), datetime(2019, 9, 20, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 9, 20, 9), datetime(2019, 9, 20, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 9, 20, 14), datetime(2019, 9, 20, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 9, 20, 14), datetime(2019, 9, 20, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 9, 21, 14), datetime(2019, 9, 21, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 9, 24, 14), datetime(2019, 9, 24, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 9, 25, 11), datetime(2019, 9, 25, 12),
            3, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 9, 26, 14), datetime(2019, 9, 26, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 9, 27, 10), datetime(2019, 9, 27, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 9, 27, 9), datetime(2019, 9, 27, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 9, 27, 14), datetime(2019, 9, 27, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 9, 27, 14), datetime(2019, 9, 27, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 9, 28, 14), datetime(2019, 9, 28, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 10, 1, 14), datetime(2019, 10, 1, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 10, 2, 11), datetime(2019, 10, 2, 12),
            6, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 10, 3, 14), datetime(2019, 10, 3, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 10, 4, 9), datetime(2019, 10, 4, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 10, 4, 10), datetime(2019, 10, 4, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 10, 4, 14), datetime(2019, 10, 4, 15),
            6, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 10, 4, 14), datetime(2019, 10, 4, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 10, 5, 14), datetime(2019, 10, 5, 15),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 10, 6, 12), datetime(2019, 10, 6, 13),
            1, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 10, 7, 11), datetime(2019, 10, 7, 12),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 10, 8, 14), datetime(2019, 10, 8, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 10, 9, 11), datetime(2019, 10, 9, 12),
            6, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 10, 10, 10), datetime(2019, 10, 10, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 10, 10, 14), datetime(2019, 10, 10, 15),
            1, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 10, 11, 10), datetime(2019, 10, 11, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 10, 11, 9), datetime(2019, 10, 11, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 10, 11, 14), datetime(2019, 10, 11, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 10, 11, 14), datetime(2019, 10, 11, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 10, 12, 14), datetime(2019, 10, 12, 15),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 10, 13, 12), datetime(2019, 10, 13, 13),
            1, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 10, 14, 11), datetime(2019, 10, 14, 12),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 10, 15, 14), datetime(2019, 10, 15, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 10, 16, 11), datetime(2019, 10, 16, 12),
            6, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 10, 17, 10), datetime(2019, 10, 17, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 10, 17, 14), datetime(2019, 10, 17, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 10, 18, 9), datetime(2019, 10, 18, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 10, 18, 10), datetime(2019, 10, 18, 11),
            10, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 10, 18, 14), datetime(2019, 10, 18, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 10, 18, 14), datetime(2019, 10, 18, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 10, 19, 14), datetime(2019, 10, 19, 15),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 10, 20, 12), datetime(2019, 10, 20, 13),
            1, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 10, 21, 11), datetime(2019, 10, 21, 12),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 10, 22, 14), datetime(2019, 10, 22, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 10, 23, 11), datetime(2019, 10, 23, 12),
            6, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 10, 24, 10), datetime(2019, 10, 24, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 10, 24, 14), datetime(2019, 10, 24, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 10, 25, 9), datetime(2019, 10, 25, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 10, 25, 10), datetime(2019, 10, 25, 11),
            10, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 10, 25, 14), datetime(2019, 10, 25, 15),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 10, 25, 14), datetime(2019, 10, 25, 15),
            6, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 10, 26, 14), datetime(2019, 10, 26, 15),
            4, 0, 0, 40.0, 40.0),
        (10, 23, 4, datetime(2019, 10, 27, 16), datetime(2019, 10, 27, 17),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 10, 27, 12), datetime(2019, 10, 27, 13),
            1, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 10, 28, 11), datetime(2019, 10, 28, 12),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 10, 29, 14), datetime(2019, 10, 29, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 10, 30, 11), datetime(2019, 10, 30, 12),
            6, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 10, 31, 10), datetime(2019, 10, 31, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 10, 31, 14), datetime(2019, 10, 31, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 11, 1, 9), datetime(2019, 11, 1, 10),
            4, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 11, 1, 10), datetime(2019, 11, 1, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 11, 1, 14), datetime(2019, 11, 1, 15),
            6, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 11, 1, 14), datetime(2019, 11, 1, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 11, 2, 14), datetime(2019, 11, 2, 15),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 11, 3, 12), datetime(2019, 11, 3, 13),
            1, 0, 0, 40.0, 40.0),
        (10, 23, 4, datetime(2019, 11, 3, 16), datetime(2019, 11, 3, 17),
            4, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 11, 4, 11), datetime(2019, 11, 4, 12),
            3, 0, 0, 40.0, 40.0),
        (5, 24, 1, datetime(2019, 11, 5, 10), datetime(2019, 11, 5, 11),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 11, 5, 14), datetime(2019, 11, 5, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 11, 6, 11), datetime(2019, 11, 6, 12),
            6, 0, 1, 40.0, 0.0),
        (6, 25, 5, datetime(2019, 11, 6, 14), datetime(2019, 11, 6, 15),
            3, 0, 0, 40.0, 40.0),
        (6, 26, 5, datetime(2019, 11, 7, 10), datetime(2019, 11, 7, 11),
            3, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 11, 7, 10), datetime(2019, 11, 7, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 11, 7, 14), datetime(2019, 11, 7, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 11, 8, 9), datetime(2019, 11, 8, 10),
            4, 0, 1, 0.0, 0.0),
        (7, 16, 5, datetime(2019, 11, 8, 10), datetime(2019, 11, 8, 11),
            10, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 11, 8, 14), datetime(2019, 11, 8, 15),
            6, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 11, 8, 14), datetime(2019, 11, 8, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 11, 9, 14), datetime(2019, 11, 9, 15),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 11, 10, 12), datetime(2019, 11, 10, 13),
            1, 0, 0, 40.0, 40.0),
        (10, 27, 4, datetime(2019, 11, 10, 14), datetime(2019, 11, 10, 15),
            7, 0, 0, 40.0, 40.0),
        (10, 23, 4, datetime(2019, 11, 10, 16), datetime(2019, 11, 10, 17),
            4, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 11, 11, 11), datetime(2019, 11, 11, 12),
            3, 0, 0, 40.0, 40.0),
        (5, 24, 1, datetime(2019, 11, 12, 10), datetime(2019, 11, 12, 11),
            3, 0, 0, 40.0, 40.0),
        (6, 10, 5, datetime(2019, 11, 12, 14), datetime(2019, 11, 12, 15),
            3, 0, 0, 40.0, 40.0),
        (9, 18, 1, datetime(2019, 11, 13, 11), datetime(2019, 11, 13, 12),
            6, 0, 0, 40.0, 40.0),
        (6, 25, 5, datetime(2019, 11, 13, 14), datetime(2019, 11, 13, 15),
            3, 0, 0, 40.0, 40.0),
        (6, 26, 5, datetime(2019, 11, 14, 10), datetime(2019, 11, 14, 11),
            3, 0, 0, 40.0, 40.0),
        (9, 22, 1, datetime(2019, 11, 14, 10), datetime(2019, 11, 14, 11),
            2, 0, 0, 40.0, 40.0),
        (7, 8, 3, datetime(2019, 11, 14, 14), datetime(2019, 11, 14, 15),
            1, 0, 0, 40.0, 40.0),
        (5, 17, 4, datetime(2019, 11, 15, 9), datetime(2019, 11, 15, 10),
            4, 0, 0, 40.0, 40.0),
        (5, 9, 1, datetime(2019, 11, 15, 14), datetime(2019, 11, 15, 15),
            6, 0, 0, 40.0, 40.0),
        (7, 16, 5, datetime(2019, 11, 15, 10), datetime(2019, 11, 15, 11),
            10, 0, 0, 40.0, 40.0),
        (7, 12, 4, datetime(2019, 11, 15, 14), datetime(2019, 11, 15, 15),
            4, 0, 0, 40.0, 40.0),
        (6, 19, 4, datetime(2019, 11, 16, 14), datetime(2019, 11, 16, 15),
            4, 0, 0, 40.0, 40.0),
        (10, 27, 4, datetime(2019, 11, 17, 14), datetime(2019, 11, 17, 15),
            7, 0, 0, 40.0, 40.0),
        (10, 23, 4, datetime(2019, 11, 17, 16), datetime(2019, 11, 17, 17),
            4, 0, 0, 40.0, 40.0),
        (7, 21, 2, datetime(2019, 11, 17, 12), datetime(2019, 11, 17, 13),
            1, 0, 0, 40.0, 40.0),
        (8, 20, 2, datetime(2019, 11, 18, 11), datetime(2019, 11, 18, 12),
            3, 0, 0, 40.0, 0.0),
        (5, 24, 1, datetime(2019, 11, 19, 10), datetime(2019, 11, 19, 11),
            3, 0, 0, 40.0, 0.0),
        (6, 10, 5, datetime(2019, 11, 19, 14), datetime(2019, 11, 19, 15),
            3, 0, 0, 40.0, 0.0),
        (9, 18, 1, datetime(2019, 11, 20, 11), datetime(2019, 11, 20, 12),
            6, 0, 0, 40.0, 0.0),
        (6, 25, 5, datetime(2019, 11, 20, 14), datetime(2019, 11, 20, 15),
            3, 0, 0, 40.0, 0.0),
        (6, 26, 5, datetime(2019, 11, 21, 10), datetime(2019, 11, 21, 11),
            3, 0, 0, 40.0, 0.0),
        (9, 22, 1, datetime(2019, 11, 21, 10), datetime(2019, 11, 21, 11),
            2, 0, 0, 40.0, 0.0),
        (7, 8, 3, datetime(2019, 11, 21, 14), datetime(2019, 11, 21, 15),
            1, 0, 0, 40.0, 0.0),
        (5, 17, 4, datetime(2019, 11, 22, 9), datetime(2019, 11, 22, 10),
            4, 0, 0, 40.0, 0.0),
        (7, 16, 5, datetime(2019, 11, 22, 10), datetime(2019, 11, 22, 11),
            10, 0, 0, 40.0, 0.0),
        (5, 9, 1, datetime(2019, 11, 22, 14), datetime(2019, 11, 22, 15),
            6, 0, 0, 40.0, 0.0),
        (7, 12, 4, datetime(2019, 11, 22, 14), datetime(2019, 11, 22, 15),
            4, 0, 0, 40.0, 0.0),
        (6, 19, 4, datetime(2019, 11, 23, 14), datetime(2019, 11, 23, 15),
            4, 0, 0, 40.0, 0.0),
        (10, 27, 4, datetime(2019, 11, 24, 14), datetime(2019, 11, 24, 15),
            7, 0, 0, 40.0, 0.0),
        (7, 21, 2, datetime(2019, 11, 24, 12), datetime(2019, 11, 24, 13),
            1, 0, 0, 40.0, 0.0),
        (10, 23, 4, datetime(2019, 11, 24, 16), datetime(2019, 11, 24, 17),
            4, 0, 0, 40.0, 0.0),
        (8, 20, 2, datetime(2019, 11, 25, 11), datetime(2019, 11, 25, 12),
            3, 0, 0, 40.0, 0.0),
        (5, 24, 1, datetime(2019, 11, 26, 10), datetime(2019, 11, 26, 11),
            3, 0, 0, 40.0, 0.0),
        (6, 10, 5, datetime(2019, 11, 26, 14), datetime(2019, 11, 26, 15),
            3, 0, 0, 40.0, 0.0),
        (9, 18, 1, datetime(2019, 11, 27, 11), datetime(2019, 11, 27, 12),
            6, 0, 0, 40.0, 0.0),
        (6, 25, 5, datetime(2019, 11, 27, 14), datetime(2019, 11, 27, 15),
            3, 0, 0, 40.0, 0.0)
    ]
    cursor.executemany(
        """
        INSERT INTO "class_session" (
            "instructor_id",
            "student_id",
            "classroom_id",
            "session_start",
            "session_stop",
            "instrument_id",
            "recording",
            "canceled",
            "amt_billed",
            "amt_paid"
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        class_sessions
    )
    conn.commit()

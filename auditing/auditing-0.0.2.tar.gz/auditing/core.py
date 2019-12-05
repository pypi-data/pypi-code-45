import datetime
import logging

from flask import request, session

_driver = {}  # dict for storing driver state


def setup(driver, *args, **kwargs):
    """
    The setup method must be called prior to any calls to the audit method.
    :param driver: string to identify one of the default drivers
    :param args: args to the drivers setup function
    :param kwargs: kwargs to the drivers setup function
    :return: None
    """
    if isinstance(driver, str):
        if driver not in _default_drivers.keys():
            raise ValueError("No default driver available with name {}".format(driver))
        _driver["name"] = {"name": driver}
        _default_drivers[driver](*args, **kwargs)
        return
    default_drivers = ",".join(_default_drivers.keys())
    raise ValueError("Driver must be provided as string identifying one of default drivers ({}). "
                     "To inject custom drivers, use the 'inject_driver' method.".format(default_drivers))


def inject_driver(**kwargs):
    """
    Inject a custom driver.
    :param kwargs: kwargs should include a "name" (string), an "audit" function, and optionally a "teardown" function.
    :return: None
    """
    teardown()
    for key in kwargs:
        _driver[key] = kwargs[key]


def teardown():
    """
    The teardown method can be called to release resources allocated for the driver on the setup call.
    :return: None
    """
    if _driver:
        if "teardown" not in _driver:
            logging.INFO("No teardown method was supplied for driver audit driver")
        _driver["teardown"]()
        for key in _driver:
            del _driver[key]


def audit(tag, dt=None, **kwargs):
    """
    When the audit method is called, an event is transmitted via the driver (initialized vis the setup method), e.g.
    to a postgres database.
    :param tag: a tag by which audit event are grouped by default. For the postgres driver, this tag translates into
    the column name in the database
    :param dt: datetime, must be a datetime object. If not provided, it is set to datetime.now()
    :param kwargs: data to be written in the audit event
    :return: None
    """
    # Check if driver has been set, default to console logging.
    if not _driver:
        logging.INFO("Audit driver has not been set, falling back to console.")
        _driver["name"] = "console"
        _driver["audit"] = _console_audit
    # Skip requests prior to user login. TODO: Make these checks configurable
    if "user" not in session:
        return
    # Try to detect client ip. This is NOT bulletproof, http://esd.io/blog/flask-apps-heroku-real-ip-spoofing.html
    if not request.headers.getlist("X-Forwarded-For"):
        ip = request.remote_addr
    else:
        ip = ",".join(request.headers.getlist("X-Forwarded-For"))
    # Default metrics desired metrics. TODO: Make these properties configurable
    default_args = dict(
        ip=ip,
        host=request.host.split(':', 1)[0],
        path=request.path,
        username=session["user"]['preferred_username'],
        datetime=datetime.datetime.now() if dt is None else dt
    )
    # Do the audit.
    _driver["audit"](tag, **default_args, **kwargs)


# region Default drivers

def _console_audit(tag, **kwargs):
    print("{}: {}".format(tag, kwargs))


def _elasticsearch_setup(**kwargs):
    """
    Simple driver that connects to an elasticsearch database.
    :param kwargs: arguments for establishing elasticsearch database connection (see '_elasticsearch_audit')
    :return: None
    """
    _driver["audit"] = _elasticsearch_audit
    for key in kwargs:
        _driver[key] = kwargs[key]


def _elasticsearch_audit(tag, **kwargs):
    from elasticsearch import Elasticsearch
    es = Elasticsearch([_driver["args"]])
    es.index(index=_driver["db_name"], body={**{"tag": tag}, **kwargs})


def _postgres_setup(**kwargs):
    """
    Driver for connecting to postgres database using a thread safe connection pool.
    :param kwargs: arguments for establishing postgres database connection
    :return: None
    """
    from psycopg2.pool import ThreadedConnectionPool
    _driver["audit"] = _postgres_audit
    _driver["pool"] = ThreadedConnectionPool(1, 100, **kwargs["args"])


def _postgres_audit(tag, **kwargs):
    connection = _driver["pool"].getconn()
    cursor = connection.cursor()
    # Convert data.
    keys = list(kwargs.keys())
    values = [kwargs[key] for key in keys]
    formatters = ["%s"] * len(values)
    # Do magic.
    command = "INSERT INTO {} ({}) VALUES({});".format(tag, ",".join(keys), ",".join(formatters))
    cursor.execute(command, values)
    connection.commit()
    cursor.close()
    _driver["pool"].putconn(connection)


def _postgres_auto_setup(**kwargs):
    """
    Like the postgres driver, but with databases and tables automatically created and extended.
    :param kwargs: arguments for establishing postgres database connection
    :return: None
    """
    from .psycopg2auto import AutoThreadedConnectionPool
    _driver["audit"] = _postgres_audit
    _driver["pool"] = AutoThreadedConnectionPool(1, 100, **kwargs["args"])


_default_drivers = {
    "postgres": _postgres_setup,
    "postgres_auto": _postgres_auto_setup,
    "elasticsearch": _elasticsearch_setup
}

# endregion

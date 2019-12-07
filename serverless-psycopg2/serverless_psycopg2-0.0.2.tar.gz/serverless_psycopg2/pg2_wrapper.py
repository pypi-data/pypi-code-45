import time
import random
import logging
import functools
from datetime import timedelta
import psycopg2
import psycopg2.errors
from .event import Event

logger = logging.getLogger('serverless_psycopg2')
logger.setLevel(logging.WARN)

def auto_reconnect(f):
    """helper function supposed to be used as decorator for
    :cls:`CursorProxy`'s member methods.
    """
    @functools.wraps(f)
    def inner(self, *args, **kwargs):
        try:
            f(self, *args, **kwargs)
        except (psycopg2.errors.AdminShutdown, psycopg2.InterfaceError): # pylint: disable=no-member
            self._reconnect()
            f(self, *args, **kwargs)
    return inner

class CursorProxy(object):
    """A proxy class of psycopg2 `conn.cursor` object"""

    def __init__(self, connection_proxy, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self._connection_proxy = connection_proxy
        try:
            self._cursor = self._connection_proxy._conn.cursor(*args, **kwargs)
        except (psycopg2.errors.AdminShutdown, psycopg2.InterfaceError): # pylint: disable=no-member
            #: TooManyConnection error belongs to `psycopg2.OperationalError`
            #: so still be raised upon hitting the `max_retries` limit.
            #: This is an intended behavior and without this, this block may
            #: fall into an infinite loop.
            self._reconnect()

    def _reconnect(self):
        pg2 = self._connection_proxy._pg2
        pg2._reset_conn()
        pg2._reset_counter()

        new_conn = pg2.get_connection()
        self._connection_proxy._replace_conn(new_conn)
        del pg2

        self._cursor = self._connection_proxy._conn.cursor(*self.args, **self.kwargs)

    @auto_reconnect
    def execute(self, *args, **kwargs):
        logger.info(*args)
        self._cursor.execute(*args, **kwargs)

    @auto_reconnect
    def mogrify(self, *args, **kwargs):
        return self._cursor.mogrify(*args, **kwargs)

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def close(self):
        self._cursor.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        self.close()

    def __del__(self):
        self.close()

class ConnectionProxy(object):
    def __init__(self, conn, pg2):
        self._conn = conn #: pg2 connection object
        self._pg2  = pg2 #: ServerlessPsycopg2 object

    @property
    def pg_config(self):
        return self._pg2._cfg

    def cursor(self, *args, **kwargs):
        return CursorProxy(self, *args, **kwargs)

    def close(self):
        pg2 = self._pg2
        if pg2.conn is None or not pg2.manage_conns:
            return

        pg2.counter += 1

        max_conn = self._get_max_connections()
        used_conns = self._get_total_connections()

        min_timeout = timedelta(seconds=pg2.zombie_min_timeout)
        max_timeout = timedelta(seconds=pg2.zombie_max_timeout)

        #: if over utilization threshold, try and clean up zombies
        cur_conn_util = used_conns['total'] / max_conn['total']
        logger.info(cur_conn_util)
        if cur_conn_util > pg2.conn_utilization:
            #: Calculate the zombie timeout

            timeout = min(
                max(
                    used_conns['max_age'],
                    min_timeout
                ),
                max_timeout
            )
            #: kill zombies if they are within the timeout
            killed_zombies = self.kill_zombie_connections(timeout) if \
                                timeout <= used_conns['max_age'] else 0
            logger.info('zombie connections killed %d' % killed_zombies)
            #: if no zombies were cleaned up, close this connection
            if killed_zombies == 0:
                logger.info('connection killed itself')
                self.quit()
                return

        elif used_conns['max_age'] > max_timeout:
            self.kill_zombie_connections(max_timeout)

        self.commit()

    def quit(self):
        """explicitly closes the pg connection"""
        pg2 = self._pg2
        if pg2.conn is not None:
            self._conn.close()
            pg2._reset_conn()
            pg2._reset_counter()
            pg2.on_close()

    def rollback(self):
        self._conn.rollback()

    def commit(self):
        self._conn.commit()

    def _replace_conn(self, conn):
        self.quit()
        self._conn = conn

    def _get_max_connections(self):
        if time.time() - self._pg2._max_conns['updated'] > self._pg2.max_conns_freq:
            c = self.cursor()
            c.execute(
                """
                SELECT CASE
                    WHEN rol.rolconnlimit > 0
                    THEN LEAST(
                        rol.rolconnlimit,
                        CAST(max_conn.current_setting AS INTEGER)
                    )
                    ELSE CAST(max_conn.current_setting AS INTEGER)
                END AS total,
                CASE
                    WHEN rol.rolconnlimit > 0
                    THEN true
                    ELSE false
                END AS user_limit
                FROM (
                    SELECT rolconnlimit FROM pg_roles WHERE rolname = %s
                ) AS rol, (
                    SELECT CURRENT_SETTING('max_connections')
                ) AS max_conn;
                """,
                (self.pg_config['user'],)
            )
            result = c.fetchone()
            self._pg2._max_conns.update({
                'total': result[0],
                'user_limit': result[1],
                'updated': time.time()
            })
            c.close()

        return self._pg2._max_conns

    def _get_total_connections(self):
        #: if cache is expired
        if time.time() - self._pg2._used_conns['updated'] > self._pg2.used_conns_freq:
            c = self.cursor()
            c.execute(
                """
                SELECT
                    COUNT(pid),
                    MAX(NOW() - state_change)
                FROM pg_stat_activity
                WHERE
                    usename = %s AND
                    state != ''
                """,
                (self.pg_config['user'],)
            )
            result = c.fetchone()
            self._pg2._used_conns.update({
                'total': result[0],
                'max_age': result[1],
                'updated': time.time()
            })
            c.close()

        return self._pg2._used_conns

    def kill_zombie_connections(self, timeout=timedelta(seconds=900)):
        #: hunt for zombies (just the sleeping ones that this user owns)
        killed_zombies = 0
        c = self.cursor()
        try:
            c.execute(
                """
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE
                    usename = %s AND
                    (state='idle' OR state='idle in transaction') AND
                    now() - state_change >= %s
                """,
                (
                    self.pg_config['user'], #: datname
                    timeout  #: interval in seconds
                )
            )
        except BaseException as e:
            self._pg2.on_kill_error(e)
        else:
            killed_zombies = len(c.fetchall())
            c.close()

        return killed_zombies

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is not None: self.rollback()
        else: self.commit()

    def __del__(self):
        self.quit()
        self._pg2._reset_conn()

class ServerlessPsycopg2(object):
    #: event handlers
    on_connect = Event()
    on_connect_error = Event()
    on_retry = Event()
    on_close = Event()
    on_error = Event()
    on_kill = Event()
    on_kill_error = Event()

    def __init__(
        self,
        manage_conns=True,
        cap=100,
        base=2,
        max_retries=50,
        backoff='full',         #: default to full Jitter
        conn_utilization=0.8,
        zombie_min_timeout=3,   #: default to 3 seconds
        zombie_max_timeout=900, #: default to 15 minutes
        max_conns_freq=15000,   #: default to 15 seconds
        used_conns_freq=0,      #: default to 0 ms
        pg_config=None,
    ):
        #: config
        self.manage_conns       = manage_conns
        self.cap                = cap
        self.base               = base
        self.max_retries        = max_retries
        self.backoff            = backoff
        self.conn_utilization   = conn_utilization
        self.zombie_min_timeout = zombie_min_timeout
        self.zombie_max_timeout = zombie_max_timeout
        self.max_conns_freq     = max_conns_freq
        self.used_conns_freq    = used_conns_freq

        #: variables
        self.conn    = None #: init client as None
        self.cur     = None
        self.counter = 0    #: total reuse count
        self.error   = 0    #: error count
        self.retries = 0    #: retry count
        self._cfg    = {
            'dbname'  : None,
            'user'    : None,
            'password': None,
            'host'    : None,
            'port'    : None,
        }
        self._cfg.update(pg_config if isinstance(pg_config, dict) else {})  #: postgresql config globals
        self._max_conns  = {'updated': 0}
        self._used_conns = {'updated': 0}

        self._conn_args = []
        self._conn_kwargs = {}

    def connect(self, *args, **kwargs):
        if args is not None:
            self._conn_args = args
        if kwargs is not None:
            self._conn_kwargs = kwargs

        conn = self.get_connection()
        return ConnectionProxy(conn, self)

    def get_connection(self, wait=0):
        #: for compatibility
        try:
            conn = self._get_connection()
        except psycopg2.OperationalError as e:
            if ('too many clients' in str(e) or \
                    e.pgcode == psycopg2.errorcodes.TOO_MANY_CONNECTIONS) and \
                    self.retries < self.max_retries:
                self.retries += 1
                wait = wait if isinstance(wait, int) else 0
                #: delay in ms
                sleep = self.full_jitter() if self.backoff != 'decorrelated' else \
                        self.decorrelated_jitter(wait)

                self.on_retry() #: emit on_retry event
                time.sleep(sleep / 1000)
                return self.get_connection(wait=sleep)
            else:
                self.on_connect_error()
                raise e
            
        return conn

    def _get_connection(self):
        self._reset_counter()
        try:
            conn = psycopg2.connect(
            #    dbname=kwargs['dbname'],
            #    user=kwargs['user'],
            #    password=kwargs['password'],
            #    host=kwargs['host'],
            #    port=kwargs['port'],
                 **self._cfg, **self._conn_kwargs
            )
        except Exception as e:
            self._reset_conn() #: TODO: really need this??;;
            self._reset_counter()
            self.error += 1
            self.on_error() #: emit on_error event
            raise e
        else:
            self._reset_retries()
            self.on_connect() #: emit on_connect event
            self.conn = True
            return conn

    def full_jitter(self):
        return random.randint(0, min(self.cap, self.base * 2 ** self.retries))

    def decorrelated_jitter(self, sleep=0):
        return min(self.cap, random.randint(self.base, sleep * 3))

    def _reset_conn(self):
        self.conn = None

    def _reset_retries(self):
        self.retries = 0
    
    def _reset_counter(self):
        self.counter = 0

    def get_error_count(self):
        return self.error
    
    def get_config(self):
        return self._cfg

    def get_counter(self):
        return self.counter

    def config(self, cfg):
        self._cfg.update(cfg)
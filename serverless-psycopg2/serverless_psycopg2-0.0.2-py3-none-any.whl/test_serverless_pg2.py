import pytest

import time
import math
import functools
import psycopg2
import psycopg2.errorcodes
from .pg2_wrapper import ServerlessPsycopg2

def spy(f):
    called = 0
    @functools.wraps(f)
    def inner(*args, **kwargs):
        nonlocal called
        called += 1
        return f(*args, **kwargs)
    
    inner.iscalled = lambda: True if called > 0 else False
    inner.get_called_number = lambda: called
    return inner

@pytest.fixture
def pg_config():
    return {
        'user': 'dev',
        'dbname': 'saeshin_dmc',
        'password': 'dev',
        'host': '127.0.0.1',
        'port': '5432'
    }

def test_execute(pg_config):
    sl_pg2 = ServerlessPsycopg2(pg_config=pg_config)
    conn = sl_pg2.connect()
    with conn:
        with conn.cursor() as c:
            c.execute('SELECT * FROM package ORDER BY id DESC')
            res = c.fetchall()
    
    conn.quit()

    import psycopg2 as pg2
    conn = pg2.connect(
        user='dev',
        dbname='saeshin_dmc',
        password='dev',
        host='127.0.0.1',
        port='5432'
    )
    with conn:
        with conn.cursor() as c:
            c.execute('SELECT * FROM package ORDER BY id DESC')
            res_2 = c.fetchall()

    conn.close()
    assert res == res_2

def test_conn_ctx(pg_config):
    pg2 = ServerlessPsycopg2(pg_config=pg_config)
    conn = pg2.connect()

    #: spy on the original connection object's rollback method
    conn.rollback = spy(conn.rollback)

    assert conn.rollback.iscalled() == False
    assert conn.rollback.get_called_number() == 0

    try:
        with conn:
            with conn.cursor() as c:
                #: intentionally raise a sql syntax error
                c.execute('SELECT * FROM hello')
    except:
        pass

    assert conn.rollback.iscalled() == True
    assert conn.rollback.get_called_number() == 1

    conn.commit = spy(conn.commit)

    assert conn.commit.iscalled() == False
    assert conn.commit.get_called_number() == 0

    with conn:
        with conn.cursor() as c:
            c.execute('SELECT pid FROM pg_stat_activity')

    assert conn.commit.iscalled() == True
    assert conn.commit.get_called_number() == 1

    conn.quit()

def test_cursor_ctx(pg_config):
    pg2 = ServerlessPsycopg2(pg_config=pg_config)
    conn = pg2.connect()

    with conn:
        c = conn.cursor()
        c.close = spy(c.close)
        with c:
            c.execute('SELECT pid FROM pg_stat_activity')

        assert c.close.iscalled() == True
        assert c.close.get_called_number() == 1

    conn.quit()

def test_multiconn(pg_config):
    """test :meth:`close` of an `ServerlessPsycopg2` instacne.
    Calling `sl_pg2.close()` closes an established connections
    until the total connections by a user drop below the
    `conn_utilization` limit.

    From this point on, a further calling of `close()` doesn't
    close a connection so the connection can be reused.

    To explicitly close the current connection, one can use the
    :meth:`quit()`.
    """
    conn_refs = {}
    bg_conns = 0
    cur_conns = 0
    max_conns = 0
    conn_util = 0.1
    pg2 = ServerlessPsycopg2(pg_config=pg_config)

    #: get `max_conns` and `bg_conns`
    conn = pg2.connect()
    with conn:
        max_conns = conn._get_max_connections()['total']
        bg_conns = conn._get_total_connections()['total'] - 1
    
    conn.quit()
    del conn

    for i in range(math.ceil(max_conns * conn_util) - bg_conns + 3):
        pg2 = ServerlessPsycopg2(pg_config=pg_config, conn_utilization=conn_util)
        conn_refs[i] = pg2.connect()

    with conn_refs[0] as conn:
        cur_conns = conn._get_total_connections()['total']

    assert cur_conns == math.ceil(max_conns * conn_util) + 3
    
    i = 0
    while cur_conns - i > math.ceil(max_conns * conn_util):
        i += 1
        #: spy on `kill_zombie_connections` method
        conn_refs[i - 1].kill_zombie_connections = \
            spy(conn_refs[i - 1].kill_zombie_connections)

        conn_refs[i - 1].close()
        next_conns = conn_refs[i]._get_total_connections()['total']

        #: check if `close()` call triggered `kill_zombie_connections()`
        assert not conn_refs[i - 1].kill_zombie_connections.iscalled()
        assert next_conns == cur_conns - i

        #: After implementing `auto-reconnect` upon failure, the following
        #: assertion checks are no longer valid.
        # with pytest.raises(psycopg2.InterfaceError) as e:
        #     conn_refs[i - 1].cursor()
        # assert 'connection already closed' in str(e.value)

    cur_conns = next_conns

    #: once the total used connections
    conn_refs[i + 1].close()
    with conn_refs[i + 2] as conn:
        next_conns = conn._get_total_connections()['total']

    assert cur_conns == next_conns

    err = None
    try:
        c = conn_refs[i + 1].cursor()
        c.close()
    except psycopg2.InterfaceError as e:
        err = e
    assert err is None

    #: explicitly close a connection by calling `quit()`
    conn_refs[i + 1].quit()
    with conn_refs[i + 2] as conn:
        next_conns = conn._get_total_connections()['total']

    assert cur_conns - 1 == next_conns

    #: cleanup
    for v in conn_refs.values():
        v.quit()

def test_retries(pg_config):
    pg2 = ServerlessPsycopg2(pg_config=pg_config)
    conn = pg2.connect()
    c    = conn.cursor()
    c.execute("SELECT COUNT(pid) FROM pg_stat_activity WHERE usename= %s AND state != ''", (pg_config['user'],))

    max_conns = conn._get_max_connections()['total']
    used_conns = c.fetchone()[0]

    c.close()

    conn_refs = {}
    for i in range(max_conns - used_conns):
        _pg2 = ServerlessPsycopg2(pg_config=pg_config)
        _conn = _pg2.connect()
        conn_refs[i] = (_pg2, _conn)

    new_pg2 = ServerlessPsycopg2(pg_config=pg_config, max_retries=5)
    new_conn = None
    with pytest.raises(psycopg2.OperationalError) as e:
        new_conn = new_pg2.connect()

    #: clean up for further test codes
    conn.quit()
    for v in conn_refs.values():
        v[1].quit()

    assert e.value.pgcode == psycopg2.errorcodes.TOO_MANY_CONNECTIONS or 'too many clients' in str(e.value)
    assert new_pg2.retries == 5
    assert new_conn is None

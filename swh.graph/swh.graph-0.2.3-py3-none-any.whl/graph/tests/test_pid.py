# Copyright (C) 2019  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import os
import shutil
import tempfile
import unittest

from itertools import islice

from swh.graph.pid import str_to_bytes, bytes_to_str
from swh.graph.pid import PidToNodeMap, NodeToPidMap
from swh.model.identifiers import PID_TYPES


class TestPidSerialization(unittest.TestCase):

    pairs = [
        ('swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2',
         bytes.fromhex('01' + '00' +
                       '94a9ed024d3859793618152ea559a168bbcbb5e2')),
        ('swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505',
         bytes.fromhex('01' + '01' +
                       'd198bc9d7a6bcf6db04f476d29314f157507d505')),
        ('swh:1:ori:b63a575fe3faab7692c9f38fb09d4bb45651bb0f',
         bytes.fromhex('01' + '02' +
                       'b63a575fe3faab7692c9f38fb09d4bb45651bb0f')),
        ('swh:1:rel:22ece559cc7cc2364edc5e5593d63ae8bd229f9f',
         bytes.fromhex('01' + '03' +
                       '22ece559cc7cc2364edc5e5593d63ae8bd229f9f')),
        ('swh:1:rev:309cf2674ee7a0749978cf8265ab91a60aea0f7d',
         bytes.fromhex('01' + '04' +
                       '309cf2674ee7a0749978cf8265ab91a60aea0f7d')),
        ('swh:1:snp:c7c108084bc0bf3d81436bf980b46e98bd338453',
         bytes.fromhex('01' + '05' +
                       'c7c108084bc0bf3d81436bf980b46e98bd338453')),
    ]

    def test_str_to_bytes(self):
        for (pid_str, pid_bytes) in self.pairs:
            self.assertEqual(str_to_bytes(pid_str), pid_bytes)

    def test_bytes_to_str(self):
        for (pid_str, pid_bytes) in self.pairs:
            self.assertEqual(bytes_to_str(pid_bytes), pid_str)

    def test_round_trip(self):
        for (pid_str, pid_bytes) in self.pairs:
            self.assertEqual(pid_str, bytes_to_str(str_to_bytes(pid_str)))
            self.assertEqual(pid_bytes, str_to_bytes(bytes_to_str(pid_bytes)))


def gen_records(types=['cnt', 'dir', 'ori', 'rel', 'rev', 'snp'],
                length=10000):
    """generate sequential PID/int records, suitable for filling int<->pid maps for
    testing swh-graph on-disk binary databases

    Args:
        types (list): list of PID types to be generated, specified as the
            corresponding 3-letter component in PIDs
        length (int): number of PIDs to generate *per type*

    Yields:
        pairs (pid, int) where pid is a textual PID and int its sequential
        integer identifier

    """
    pos = 0
    for t in sorted(types):
        for i in range(0, length):
            seq = format(pos, 'x')  # current position as hex string
            pid = 'swh:1:{}:{}{}'.format(t, '0' * (40 - len(seq)), seq)
            yield (pid, pos)
            pos += 1


# pairs PID/position in the sequence generated by :func:`gen_records` above
MAP_PAIRS = [
    ('swh:1:cnt:0000000000000000000000000000000000000000', 0),
    ('swh:1:cnt:000000000000000000000000000000000000002a', 42),
    ('swh:1:dir:0000000000000000000000000000000000002afc', 11004),
    ('swh:1:ori:00000000000000000000000000000000000056ce', 22222),
    ('swh:1:rel:0000000000000000000000000000000000008235', 33333),
    ('swh:1:rev:000000000000000000000000000000000000ad9c', 44444),
    ('swh:1:snp:000000000000000000000000000000000000ea5f', 59999),
]


class TestPidToNodeMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """create reasonably sized (~2 MB) PID->int map to test on-disk DB

        """
        cls.tmpdir = tempfile.mkdtemp(prefix='swh.graph.test.')
        cls.fname = os.path.join(cls.tmpdir, 'pid2int.bin')
        with open(cls.fname, 'wb') as f:
            for (pid, i) in gen_records(length=10000):
                PidToNodeMap.write_record(f, pid, i)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmpdir)

    def setUp(self):
        self.map = PidToNodeMap(self.fname)

    def tearDown(self):
        self.map.close()

    def test_lookup(self):
        for (pid, pos) in MAP_PAIRS:
            self.assertEqual(self.map[pid], pos)

    def test_missing(self):
        with self.assertRaises(KeyError):
            self.map['swh:1:ori:0101010100000000000000000000000000000000'],
        with self.assertRaises(KeyError):
            self.map['swh:1:cnt:0101010100000000000000000000000000000000'],

    def test_type_error(self):
        with self.assertRaises(TypeError):
            self.map[42]
        with self.assertRaises(TypeError):
            self.map[1.2]

    def test_update(self):
        fname2 = self.fname + '.update'
        shutil.copy(self.fname, fname2)  # fresh map copy
        map2 = PidToNodeMap(fname2, mode='rb+')
        for (pid, int) in islice(map2, 11):  # update the first N items
            new_int = int + 42
            map2[pid] = new_int
            self.assertEqual(map2[pid], new_int)  # check updated value

        os.unlink(fname2)  # tmpdir will be cleaned even if we don't reach this

    def test_iter_type(self):
        for t in PID_TYPES:
            first_20 = list(islice(self.map.iter_type(t), 20))
            k = first_20[0][1]
            expected = [('swh:1:{}:{:040x}'.format(t, i), i)
                        for i in range(k, k + 20)]
            assert first_20 == expected

    def test_iter_prefix(self):
        for t in PID_TYPES:
            prefix = self.map.iter_prefix('swh:1:{}:00'.format(t))
            first_20 = list(islice(prefix, 20))
            k = first_20[0][1]
            expected = [('swh:1:{}:{:040x}'.format(t, i), i)
                        for i in range(k, k + 20)]
            assert first_20 == expected


class TestNodeToPidMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """create reasonably sized (~1 MB) int->PID map to test on-disk DB

        """
        cls.tmpdir = tempfile.mkdtemp(prefix='swh.graph.test.')
        cls.fname = os.path.join(cls.tmpdir, 'int2pid.bin')
        with open(cls.fname, 'wb') as f:
            for (pid, _i) in gen_records(length=10000):
                NodeToPidMap.write_record(f, pid)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmpdir)

    def setUp(self):
        self.map = NodeToPidMap(self.fname)

    def tearDown(self):
        self.map.close()

    def test_lookup(self):
        for (pid, pos) in MAP_PAIRS:
            self.assertEqual(self.map[pos], pid)

    def test_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.map[1000000]
        with self.assertRaises(IndexError):
            self.map[-1000000]

    def test_update(self):
        fname2 = self.fname + '.update'
        shutil.copy(self.fname, fname2)  # fresh map copy
        map2 = NodeToPidMap(fname2, mode='rb+')
        for (int, pid) in islice(map2, 11):  # update the first N items
            new_pid = pid.replace(':0', ':f')  # mangle first hex digit
            map2[int] = new_pid
            self.assertEqual(map2[int], new_pid)  # check updated value

        os.unlink(fname2)  # tmpdir will be cleaned even if we don't reach this

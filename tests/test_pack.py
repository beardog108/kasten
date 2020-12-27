import unittest
import os
from time import time
from math import floor
from msgpack import unpackb

from kasten.generator import pack
from kasten import exceptions


class TestPack(unittest.TestCase):

    def test_pack(self):
        data = os.urandom(10)
        t = floor(time())
        packed = pack.pack(data, 'bin', timestamp=t)
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertAlmostEqual(unpacked[1], t)
        self.assertEqual(len(unpacked), 3)

    def test_with_meta(self):
        data = os.urandom(10)
        t = floor(time())
        packed = pack.pack(data, 'bin', app_metadata={"meme": "doge"})
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertAlmostEqual(unpacked[1], t)
        self.assertEqual(unpacked[2], {"meme": "doge"})
        self.assertEqual(len(unpacked), 3)

    def test_linebreak_data(self):
        data = os.urandom(10) + b'\n'
        t = floor(time())
        packed = pack.pack(data, 'bin', 0)
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertAlmostEqual(unpacked[1], t)
        self.assertEqual(len(unpacked[0]), 3)

    def test_invalid_data_type(self):
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, '', 1)
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, 'aaaaa', 1)



unittest.main()
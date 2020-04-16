import unittest
import os
from time import time
from math import floor
from msgpack import unpackb

from kasten.generator import pack
from kasten import exceptions


class TestPack(unittest.TestCase):

    def test_unsigned_pack(self):
        data = os.urandom(10)
        t = floor(time())
        packed = pack.pack(data, 'bin', 0)
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertEqual(unpacked[1], 0)
        self.assertAlmostEqual(unpacked[2], t)
        self.assertEqual(len(unpacked), 3)

    def test_unsigned_with_meta(self):
        data = os.urandom(10)
        t = floor(time())
        packed = pack.pack(data, 'bin', 0, app_metadata={"meme": "doge"})
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertEqual(unpacked[1], 0)
        self.assertAlmostEqual(unpacked[2], t)
        self.assertEqual(unpacked[3], {"meme": "doge"})
        self.assertEqual(len(unpacked), 4)

    def test_linebreak_data(self):
        data = os.urandom(10) + b'\n'
        t = floor(time())
        packed = pack.pack(data, 'bin', 0)
        parts = packed.split(b'\n', 1)
        unpacked = unpackb(parts[0])
        self.assertEqual(unpacked[0], 'bin')
        self.assertEqual(unpacked[1], 0)
        self.assertAlmostEqual(unpacked[2], t)
        self.assertEqual(len(unpacked[0]), 3)

    def test_invalid_data_type(self):
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, '', 1)
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, 'aaaaa', 1)

    def test_invalid_enc_mode(self):
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', None)
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', "100")
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', 100)
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', -1)
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', -5)
        self.assertRaises(exceptions.InvalidEncryptionMode, pack.pack, data, 'txt', "test")



unittest.main()
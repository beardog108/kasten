import unittest
import os

from kasten import pack
from kasten import exceptions


class TestPack(unittest.TestCase):

    def test_unsigned_pack(self):
        data = os.urandom(10)
        packed = pack.pack(data, 'bin', 0)
        parts = packed.split(b'\n', 1)
        self.assertEqual(parts[0], b'\x92\xa3bin\x00\xc4\x01')
        self.assertEqual(parts[1], data)

    def test_linebreak_data(self):
        data = os.urandom(9) + b'\n' + b"okay"
        packed = pack.pack(data, 'bin', 0)
        parts = packed.split(b'\n', 1)
        self.assertEqual(parts[0], b'\x92\xa3bin\x00\xc4\x01')
        self.assertEqual(parts[1], data)

    def test_invalid_data_type(self):
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, '', 1)
        data = os.urandom(10)
        self.assertRaises(exceptions.InvalidKastenTypeLength, pack.pack, data, 'aaaaa', 1)



unittest.main()
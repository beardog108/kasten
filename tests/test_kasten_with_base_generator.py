import unittest
from hashlib import sha3_384

from kasten import Kasten
from kasten import exceptions
from kasten.generator import KastenBaseGenerator


class TestKastenBaseGenerator(unittest.TestCase):
    def test_kasten(self):
        k = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntest'
        K = Kasten(sha3_384(k).digest(), k, KastenBaseGenerator)

    def test_kasten_invalid(self):
        k = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntest'
        self.assertRaises(exceptions.InvalidID, Kasten, sha3_384(k + b'invalid').digest(), k, KastenBaseGenerator)


unittest.main()

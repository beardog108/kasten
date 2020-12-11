import unittest
from hashlib import sha3_384

from kasten import Kasten
from kasten import exceptions
from kasten.generator import KastenBaseGenerator, pack


class TestKastenBaseGenerator(unittest.TestCase):
    def test_kasten(self):
        k = b'\x95\xa3tst\x00\x00\x92\xc4\x00\xc4\x00\xc0\ntest data'
        K = Kasten(sha3_384(k).digest(), k, KastenBaseGenerator)

    def test_kasten_invalid(self):
        k = b'\x95\xa3tst\x00\x00\x92\xc4\x00\xc4\x00\xc0\ntest data'
        self.assertRaises(
            exceptions.InvalidID,
            Kasten, sha3_384(k + b'invalid').digest(), k, KastenBaseGenerator)

    def test_kasten_get_metadata(self):
        metadata = {"name": "john", "raw": b"are we having fun yet?"}
        packed = pack.pack(b"test msg", "tst", 0, app_metadata=metadata)
        K = Kasten(sha3_384(packed).digest(), packed, KastenBaseGenerator)
        self.assertEqual(K.get_metadata(), metadata)

    def test_kasten_unsafe_deserialize(self):
        class Person:
            def __init__(self, n):
                self.name = n
        kevin = Person("kevin")
        metadata = {
            "name": "john", "raw": b"are we having fun yet?", "person": kevin}
        try:
            packed = pack.pack(b"test msg", "tst", 0, app_metadata=metadata)
            K = Kasten(sha3_384(packed).digest(), packed, KastenBaseGenerator)
        except TypeError:
            pass
        else:
            raise Exception("Serialized custom type in packer")



unittest.main()

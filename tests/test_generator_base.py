import unittest
from hashlib import sha3_384

from kasten import exceptions
from kasten.generator import KastenBaseGenerator


class TestBaseGenerator(unittest.TestCase):
    def test_base_generator(self):
        k = b'\x92\xa3bin\x00\xc4\x01\n(\x86!\xd7\xb5\x8ar\xae\x97z'
        K = KastenBaseGenerator.generate(k)
        h = sha3_384(k).digest()
        self.assertTrue(len(K.packed_bytes) > 0)
        KastenBaseGenerator.validate_id(h, k)
        self.assertRaises(exceptions.InvalidID, KastenBaseGenerator.validate_id, h, b"\x92\xa3txt\x00\xc4\x01\n(\x86!\xd7\xb5\x8ar\xae\x97z")


unittest.main()

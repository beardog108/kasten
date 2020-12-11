import unittest
from hashlib import sha3_384

from kasten import exceptions
from kasten.generator import KastenBaseGenerator


class TestBaseGenerator(unittest.TestCase):
    def test_base_generator(self):

        k = b'\x95\xa3tst\x00\x00\xc0\xc0\ntest data'
        invalid = b'\x95\xa3tst\x00\x00\xc0\xc0\ntest datb'

        correct_K = KastenBaseGenerator.generate(k)
        hash_test = sha3_384(k).digest()

        self.assertTrue(len(correct_K.get_packed()) > 0)

        # k = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntest'
        # invalid = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntes2'
        # K = KastenBaseGenerator.generate(k)
        # h = sha3_384(k).digest()
        # self.assertTrue(len(K.get_packed()) > 0)
        # KastenBaseGenerator.validate_id(h, k)
        # self.assertRaises(exceptions.InvalidID, KastenBaseGenerator.validate_id, h, invalid)
        # self.assertEqual(K.get_packed(), k)


unittest.main()

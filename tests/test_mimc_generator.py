import unittest

import mimcvdf

from kasten import exceptions
from kasten.generator import KastenMimcGenerator


class TestMimcGenerator(unittest.TestCase):
    def test_mimc_generator(self):
        k = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntest'
        invalid = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntes2'
        K = KastenMimcGenerator.generate(k)
        #h = sha3_384(k).digest()
        h = mimcvdf.vdf_create(k, 5000, dec=True)
        self.assertTrue(len(K.get_packed()) > 0)
        KastenMimcGenerator.validate_id(h, k)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, invalid)
        self.assertEqual(K.get_packed(), k)

    def test_mimc_generator_wrong_rounds(self):
        k = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntest'
        invalid = b'\x93\xa3txt\x01\xce^\x97\xe3\xdc\ntes2'
        K = KastenMimcGenerator.generate(k)
        #h = sha3_384(k).digest()
        h = mimcvdf.vdf_create(k, 1000, dec=True)
        self.assertTrue(len(K.get_packed()) > 0)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, k)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, invalid)
        self.assertEqual(K.get_packed(), k)

unittest.main()

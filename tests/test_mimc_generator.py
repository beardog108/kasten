import unittest

import mimcvdf

from kasten import exceptions
from kasten.generator import KastenMimcGenerator
from kasten import Kasten


class TestMimcGenerator(unittest.TestCase):
    def test_mimc_generator(self):
        k = b'\x93\xa3tst\xce_\xe7\xfb\xfb\xc0\nTest'
        invalid = b'\x93\xa3tst\xce_\xe7\xfb\xfb\xc0\nTes2'
        K = KastenMimcGenerator.generate(k)
        #h = sha3_384(k).digest()
        h = mimcvdf.vdf_create(k, 5000, dec=True)
        self.assertTrue(len(K.get_packed()) > 0)
        KastenMimcGenerator.validate_id(h, k)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, invalid)
        self.assertEqual(K.get_packed(), k)

    def test_mimc_generator_wrong_rounds(self):
        k = b'\x93\xa3tst\xce_\xe7\xfb\xfb\xc0\nTest'
        invalid = b'\x93\xa3tst\xce_\xe7\xfb\xfb\xc0\nTes2'
        K = KastenMimcGenerator.generate(k)
        #h = sha3_384(k).digest()
        h = mimcvdf.vdf_create(k, 1000, dec=True)
        self.assertTrue(len(K.get_packed()) > 0)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, k)
        self.assertRaises(exceptions.InvalidID, KastenMimcGenerator.validate_id, h, invalid)
        self.assertEqual(K.get_packed(), k)

    def test_mimc_generator_kasten_auto_validate(self):
        k = b'\x93\xa3tst\xce_\xe7\xfb\xfb\xc0\nTest'
        K = KastenMimcGenerator.generate(k, 1000)

        Kasten(int.from_bytes(K.id, byteorder="big"), K.get_packed(), KastenMimcGenerator, *[1000])
        self.assertRaises(
            exceptions.InvalidID,
            Kasten,
            int.from_bytes(K.id, byteorder="big"), K.get_packed(), KastenMimcGenerator, *[100]
        )

unittest.main()

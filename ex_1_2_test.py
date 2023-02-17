import unittest
import codecs
from ex_2 import fixed_xor

class FixedXorTestCase(unittest.TestCase):

    def test_fixed_xor(self):
        result = fixed_xor(codecs.decode('1c0111001f010100061a024b53535009181c','hex'),codecs.decode('686974207468652062756c6c277320657965','hex'))
        self.assertEqual(codecs.encode(result,'hex'), b'746865206b696420646f6e277420706c6179')

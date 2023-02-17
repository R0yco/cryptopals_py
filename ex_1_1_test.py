import unittest
from ex_1 import hex_to_base64

class ConvertionTestCase(unittest.TestCase):

    def test_hex_to_base64(self):
        result = hex_to_base64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
        self.assertEqual(result, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")



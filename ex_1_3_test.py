import unittest

from ex_1_3 import find_best_key

class TestXorDecrypter(unittest.TestCase):
    
    def test_xor_decrypter(self):
        text1 = "The quick brown fox jumps over the lazy dog"
        text_xored = bytes([c ^ 45 for c in text1.encode('ascii')])
        self.assertEqual(find_best_key(text_xored), 45)

if __name__ == "__main__":
    unittest.main()


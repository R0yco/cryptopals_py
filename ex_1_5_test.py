from ex_1_5 import reapeating_xor_encrypt
import unittest
import codecs
class TestRepeatingXorEncrypt(unittest.TestCase):
        def test_repeating_xor(self):
            plaintext = b"Burning 'em, if you ain't quick and nimble\n"\
            b"I go crazy when I hear a cymbal"
            expected_ciphertext = b"0b3637272a2b2e63622c2e69692a23693"\
            b"a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a"\
            b"652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
            key = b"ICE"
            ciphertext_hex = codecs.encode(reapeating_xor_encrypt(plaintext, key), 'hex')
            self.assertEqual(expected_ciphertext, ciphertext_hex)

if __name__ == "__main__":
    unittest.main()

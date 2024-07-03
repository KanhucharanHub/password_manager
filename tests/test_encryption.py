import unittest
from src.encryption import EncryptionManager

class TestEncryptionManager(unittest.TestCase):
    def setUp(self):
        self.key = EncryptionManager.generate_key()
        self.encryption_manager = EncryptionManager(self.key)

    def test_encrypt_decrypt(self):
        original_text = "HelloWorld"
        encrypted_text = self.encryption_manager.encrypt(original_text)
        decrypted_text = self.encryption_manager.decrypt(encrypted_text)
        self.assertEqual(original_text, decrypted_text)

        
if __name__ == '__main__':
    unittest.main()

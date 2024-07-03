import unittest
from src.authentication import AuthenticationManager

class TestAuthenticationManager(unittest.TestCase):
    def setUp(self):
        self.auth_manager = AuthenticationManager()
        self.password = "SuperSecret"
        self.auth_manager.set_master_password(self.password)

    def test_verify_master_password(self):
        self.assertTrue(self.auth_manager.verify_master_password(self.password))
        self.assertFalse(self.auth_manager.verify_master_password("WrongPassword"))

if __name__ == '__main__':
    unittest.main()

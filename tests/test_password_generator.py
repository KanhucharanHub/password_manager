import unittest
from src.password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        password = generate_password(16)
        self.assertEqual(len(password), 16)

    def test_generate_password_characters(self):
        password = generate_password(12)
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in '!@#$%^&*()_+' for char in password))

if __name__ == '__main__':
    unittest.main()

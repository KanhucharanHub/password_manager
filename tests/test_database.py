import unittest
from src.database import DatabaseManager

class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db_manager = DatabaseManager(':memory:')  # Use in-memory database for testing

    def test_add_and_get_password(self):
        self.db_manager.add_password('example', 'user1', 'password123')
        result = self.db_manager.get_password('example')
        self.assertEqual(result, ('user1', 'password123'))

if __name__ == '__main__':
    unittest.main()

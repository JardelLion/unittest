import unittest
from fixtures.main import UserManager


class TestUserManager(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.User = UserManager()

    def test_add_user(self):
        self.assertTrue(self.User.add_user('jardel', 'iamjardelprogrammer@gmail.com'))

    def test_get_user(self):
        user = self.User.get_user('Jardel')
        self.assertIsNone(self.User.get_user('jardel'), None)

    def test_add_duplicate_user(self):
        self.User.add_user("john doe", 'john@example.com')
        with self.assertRaises(ValueError):
            self.User.add_user('john doe', 'john@example.com')

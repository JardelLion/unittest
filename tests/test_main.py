from basic.main import get_weather, divide, add

import unittest

class TestMain(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.temperature = 21

    def test_get_weather(self):
        self.assertEqual(get_weather(self.temperature), 'hot')
        self.assertEqual(get_weather(self.temperature -20), 'cold')

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        with self.assertRaises(ValueError):
            divide(2, 0)


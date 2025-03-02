import unittest
from app import get_greeting

class TestApp(unittest.TestCase):
    def text_get_greeting(self):
        self.assertEqual(get_greeting(), "Hello, WorldssssssssS!")


if __name__ == '__main__':
    unittest.main()
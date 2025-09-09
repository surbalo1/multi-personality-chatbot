import unittest
from src.main import awesome_function

class TestMain(unittest.TestCase):

    def test_awesome_function(self):
        self.assertEqual(awesome_function(), "Hello from awesome_function!")

if __name__ == '__main__':
    unittest.main()

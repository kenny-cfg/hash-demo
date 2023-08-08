import unittest

from my_set import MySet


class TestMySet(unittest.TestCase):
    def test_can_put_something_in(self):
        set = MySet()
        set.put('Hello')

        result = set.has('Hello')

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

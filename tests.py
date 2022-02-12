import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        input = 'asDf1122~'
        self.assertTrue(check_pwd(input))

    def test2(self):
        input ='11111111'
        self.assertFalse(check_pwd(input))

    def test3(self):
        input = 'aaaaaaaa'
        self.assertFalse(check_pwd(input))

if __name__ == '__main__':
    unittest.main()

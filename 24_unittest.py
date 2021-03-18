import unittest
from nose.tools import ok_, eq_, raises, timed


class TestStringMethods(unittest.TestCase):

    # def setUp(self):
    #     print('This is setup before Test')
    #
    # def tearDown(self):
    #     print('This is tearDown after Test')

    def test_upper(self):
        eq_('foo'.upper(), 'FOO')
        # expected = 'FOO'
        # actual   = 'foo'.upper()
        # self.assertEqual(actual, expected)

    def test_isupper(self):
        ok_('FOO'.isupper())
        ok_(not 'Foo'.isupper())

    #   self.assertTrue('FOO'.isupper())
    #   self.assertFalse('foo'.isupper())

    def test_split(self):
        eq_('hello world'.split(), ["hello", "world"])

    #     string = 'hello world'
    #     self.assertEqual(string.split(), ["hello", "world"])

    @raises(TypeError)
    def test_exception(self):
        'hello world'.split(2)

        # string = 'hello world'
        # with self.assertRaises(TypeError):
        #     string.split(2)

    @timed(0.01)
    def test_time(self):
        for i in range(10000):
            'hello world'.split()


def main():
    unittest.main()

    return

if __name__ == '__main__':
    main()
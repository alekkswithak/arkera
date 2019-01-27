import unittest


def increment_dictionary_values(d, i):
    return {k: v+i for k, v in d.items()}


class TestIncrementDictionaryValues(unittest.TestCase):

    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d, 1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


if __name__ == '__main__':
    unittest.main()
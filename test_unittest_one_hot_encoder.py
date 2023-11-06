import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):

    def test_empty_input(self):
        with self.assertRaises(TypeError):
            fit_transform()

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            fit_transform(0)

    def test_artem_sukhov_me(self):
        result = fit_transform('artem', 'sukhov', 'me')
        expected = [
            ('artem', [0, 0, 1]),
            ('sukhov', [0, 1, 0]),
            ('me', [1, 0, 0])
        ]
        self.assertEqual(result, expected)

    def test_list_artem_sukhov_me(self):
        result = fit_transform(['artem', 'sukhov', 'me'])
        self.assertIn(('artem', [0, 0, 1]), result)

    def test_artem_sukhov_artem(self):
        result = fit_transform('artem', 'sukhov', 'artem')
        expected = [
            ('artem', [0, 1]),
            ('sukhov', [1, 0]),
            ('artem', [0, 1])
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

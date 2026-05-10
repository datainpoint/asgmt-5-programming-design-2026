import unittest
import importlib
import numpy as np

class TestAssignmentFive(unittest.TestCase):
    def test_01(self):
        square_sqrt_args = asgmt.SquareSqrtArgs()
        self.assertEqual(square_sqrt_args.square_args(0, 1, 2), [0, 1, 4])
        self.assertEqual(square_sqrt_args.sqrt_args(0, 1, 4), [0.0, 1.0, 2.0])
        self.assertEqual(square_sqrt_args.square_args(3, 4, 5), [9, 16, 25])
        self.assertEqual(square_sqrt_args.sqrt_args(9, 16, 25), [3.0, 4.0, 5.0])
        self.assertEqual(square_sqrt_args.square_args(6, 7), [36, 49])
        self.assertEqual(square_sqrt_args.sqrt_args(36, 49), [6.0, 7.0])
    def test_02(self):
        reverse_kwargs = asgmt.ReverseKwargs(one=1, two=2, three=3)
        self.assertEqual(reverse_kwargs.fetch_key_value(), {'key': ('one', 'two', 'three'), 'value': (1, 2, 3)})
        self.assertEqual(reverse_kwargs.reverse_key_value(), {1: 'one', 2: 'two', 3: 'three'})
        reverse_kwargs = asgmt.ReverseKwargs(four=4, five=5)
        self.assertEqual(reverse_kwargs.fetch_key_value(), {'key': ('four', 'five'), 'value': (4, 5)})
        self.assertEqual(reverse_kwargs.reverse_key_value(), {4: 'four', 5: 'five'})
    def test_03(self):
        cd = asgmt.CommonDivisors(3, 6)
        self.assertEqual(len(cd.x_divisors), 2)
        self.assertEqual(len(cd.y_divisors), 4)
        self.assertEqual(len(cd.get_common_divisors()), 2)
        cd = asgmt.CommonDivisors(4, 8)
        self.assertEqual(len(cd.x_divisors), 3)
        self.assertEqual(len(cd.y_divisors), 4)
        self.assertEqual(len(cd.get_common_divisors()), 3)
        cd = asgmt.CommonDivisors(5, 10)
        self.assertEqual(len(cd.x_divisors), 2)
        self.assertEqual(len(cd.y_divisors), 4)
        self.assertEqual(len(cd.get_common_divisors()), 2)
    def test_04(self):
        pj = asgmt.PrimeJudger(1)
        self.assertEqual(len(pj.get_divisors()), 1)
        self.assertFalse(pj.is_prime())
        pj = asgmt.PrimeJudger(2)
        self.assertEqual(len(pj.get_divisors()), 2)
        self.assertTrue(pj.is_prime())
        pj = asgmt.PrimeJudger(4)
        self.assertEqual(len(pj.get_divisors()), 3)
        self.assertFalse(pj.is_prime())
        pj = asgmt.PrimeJudger(5)
        self.assertEqual(len(pj.get_divisors()), 2)
        self.assertTrue(pj.is_prime())
    def test_05(self):
        countries_json = asgmt.import_countries_json()
        self.assertIsInstance(countries_json, list)
        self.assertEqual(len(countries_json), 249)
    def test_06(self):
        self.assertEqual(asgmt.lookup_country_iso_codes("Taiwan"), ('TW', 'TWN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Japan"), ('JP', 'JPN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Lithuania"),  ('LT', 'LTU'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Slovenia"), ('SI', 'SVN'))
        self.assertEqual(asgmt.lookup_country_iso_codes("Czechia"),  ('CZ', 'CZE'))
        self.assertEqual(asgmt.lookup_country_iso_codes("United States of America (the)"), ('US', 'USA'))
    def test_07(self):
        arr = np.array([5, 5, 6, 6])
        aga = asgmt.ArrayGetAttrs(arr)
        self.assertEqual(aga.get_ndim(), 1)
        self.assertEqual(aga.get_shape(), (4,))
        self.assertEqual(aga.get_size(), 4)
        arr = np.array([[5, 5],
                        [6, 6]])
        aga = asgmt.ArrayGetAttrs(arr)
        self.assertEqual(aga.get_ndim(), 2)
        self.assertEqual(aga.get_shape(), (2, 2))
        self.assertEqual(aga.get_size(), 4)
    def test_08(self):
        A = np.array([5, 5, 6, 6]).reshape(-1, 1)
        np.testing.assert_array_equal(asgmt.add_intercepts(A),
        np.array([[1, 5],
                  [1, 5],
                  [1, 6],
                  [1, 6]]))
        B = np.arange(10).reshape(5, 2)
        np.testing.assert_array_equal(asgmt.add_intercepts(B),
        np.array([[1, 0, 1],
                  [1, 2, 3],
                  [1, 4, 5],
                  [1, 6, 7],
                  [1, 8, 9]]))
        C = np.array([5, 6, 7, 8]).reshape(-1, 1)
        np.testing.assert_array_equal(asgmt.add_intercepts(C),
        np.array([[1, 5],
                  [1, 6],
                  [1, 7],
                  [1, 8]]))
    def test_09(self):
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(2, 5566),
        np.array([[   0, 5566],
                  [5566,    0]]))
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(3, 55),
        np.array([[ 0, 55, 55],
                  [55,  0, 55],
                  [55, 55,  0]]))
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(4, 66),
        np.array([[ 0, 66, 66, 66],
                  [66,  0, 66, 66],
                  [66, 66,  0, 66],
                  [66, 66, 66,  0]]))
    def test_10(self):
        np.testing.assert_array_equal(asgmt.create_square_matrix(3),
        np.array([[1, 2, 3],
                  [2, 4, 6],
                  [3, 6, 9]]))
        np.testing.assert_array_equal(asgmt.create_square_matrix(4),
        np.array([[ 1,  2,  3,  4],
                  [ 2,  4,  6,  8],
                  [ 3,  6,  9, 12],
                  [ 4,  8, 12, 16]]))
        np.testing.assert_array_equal(asgmt.create_square_matrix(5),
        np.array([[ 1,  2,  3,  4,  5],
                  [ 2,  4,  6,  8, 10],
                  [ 3,  6,  9, 12, 15],
                  [ 4,  8, 12, 16, 20],
                  [ 5, 10, 15, 20, 25]]))

asgmt = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFive)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))
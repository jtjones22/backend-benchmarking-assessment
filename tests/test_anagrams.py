""" Test Suite for anagrams module. """
import unittest
from timeit import Timer
from anagrams import find_anagrams


class TestAnagrams(unittest.TestCase):
    """
        Benchmarking test case. We test actual functionality of find_anagrams
        with doctests, which is why this test case excludes those unit tests.
    """

    def run_find_anagrams(self, word_list, benchmark):
        my_time = Timer(lambda: find_anagrams(word_list)).timeit(number=1)
        my_time = round(my_time, 3)
        failure_text = (
            'find_anagrams took {} seconds, which exceeds the '
            'benchmark of {} seconds'.format(my_time, benchmark)
            )
        self.assertTrue(my_time <= benchmark, failure_text)

    def test_short(self):
        """ Test find_anagrams with short word list. """
        with open("words/short.txt") as f:
            short_list = f.read().split()
        self.run_find_anagrams(short_list, 0.005)

    def test_long(self):
        """ Test find_anagrams with long word list. """
        with open("words/long.txt") as f:
            long_list = f.read().split()
        self.run_find_anagrams(long_list, 0.10)


if __name__ == '__main__':
    unittest.main()

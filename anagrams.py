#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" anagrams
    Command line interface that accepts a word file and returns a dictionary of
    anagrams for that file.

    Module provides a function find_anagrams which can be used to do the same
    for an arbitrary list of strings.

"""
__author__ = "Jonathan Jones"

import sys
import cProfile
from collections import defaultdict


def alphabetized(string):
    """ alphabetize
        Given a string, return a string that includes the same letters in
        alphabetical order.
        Example:
        >>> print(alphabetize('cab'))
        abc
    """
    return "".join(sorted(string.lower()))


def find_anagrams(words):
    """ find_anagrams

        Return a dictionary with keys that are alphabetized words and values
        that are all words that, when alphabetized, match the key.

        Example:

        >>> print find_anagrams(['cat', 'dog', 'act'])
        {'dgo': ['dog'], 'act': ['cat', 'act']}

    """
    anagram_dict = defaultdict(list)
    for word in words:
        anagram_dict[alphabetized(word)].append(word)
    return dict(anagram_dict)


if __name__ == "__main__":
    # run find anagrams of first argument
    if len(sys.argv) < 2:
        print("Please specify a word file!")
        sys.exit(1)
    else:
        with open(sys.argv[1], 'r') as handle:
            words = handle.read().split()
            cProfile.run('find_anagrams(words)', sort='cumtime')
            print(find_anagrams(words))
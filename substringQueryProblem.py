#import ahocorasick

# -*- coding: utf-8 -*-
"""
    Aho-Corasick string search algorithm.
    Author    : Wojciech Muła, wojciech_mula@poczta.onet.pl
    WWW       : http://0x80.pl
    License   : public domain
"""

from collections import deque

nil = object()    # used to distinguish from None

class TrieNode(object):
    """
    Node of trie/Aho-Corasick automaton
    """

    __slots__ = ['char', 'output', 'fail', 'children']

    def __init__(self, char):
        """
        Constructs an empty node
        """

        self.char = char        # character
        self.output = nil        # an output function for this node
        self.fail = nil            # fail link used by Aho-Corasick automaton
        self.children = {}        # children


class Trie(object):
    """
    Trie/Aho-Corasick automaton.
    """

    def __init__(self):
        """
        Construct an empty trie
        """

        self.root = TrieNode('')


    def add_word(self, word, value):
        """
        Adds word and associated value.
        If word already exists, its value is replaced.
        """
        if not word:
            return

        node = self.root
        for c in word:
            try:
                node = node.children[c]
            except KeyError:
                n = TrieNode(c)
                node.children[c] = n
                node = n

        node.output = value


    def make_automaton(self):
        """
        Converts trie to Aho-Corasick automaton.
        """

        queue = deque()

        # 1.
        for i in range(256):
            c = chr(i)
            if c in self.root.children:
                node = self.root.children[c]
                node.fail = self.root    # f(s) = 0
                queue.append(node)
            else:
                self.root.children[c] = self.root

        # 2.
        while queue:
            r = queue.popleft()
            for node in r.children.values():
                queue.append(node)
                state = r.fail
                while node.char not in state.children:
                        state = state.fail

                node.fail = state.children.get(node.char, self.root)


    def iter(self, string):
        """
        Generator performs Aho-Corasick search string algorithm, yielding
        tuples containing two values:
        - position in string
        - outputs associated with matched strings
        """
        state = self.root
        for index, c in enumerate(string):
            while c not in state.children:
                state = state.fail

            state = state.children.get(c, self.root)

            tmp = state
            output = []
            while tmp is not nil:
                if tmp.output is not nil:
                    output.append(tmp.output)

                tmp = tmp.fail

            if output:
                yield (index, output)

#my code from here
A = Trie()
haystack = input()

want = []
d = {}
#put the words we want into the Trie
for idx in range(int(input())):
    key, pos = input().split()
    want.append((key, int(pos)))
    d[key] = []
    A.add_word(key, (idx, key))

A.make_automaton()

#look for the words in the automaton and store all their positions in a dictionary
for end_index, ListGiven in A.iter(haystack):
    for tup in ListGiven:
        insert_order, original_value = tup[0], tup[1]
        start_index = end_index - len(original_value) + 1
        d[original_value].append(start_index)

#print the values that we want
for (string, pos) in want:
    try:
        print(d[string][pos-1] + 1)
    except IndexError:
        print(-1)
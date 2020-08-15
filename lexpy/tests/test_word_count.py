import unittest
import os

from lexpy.trie import Trie
from lexpy.dawg import DAWG
from lexpy.utils import build_trie_from_file
from lexpy.exceptions import InvalidWildCardExpressionError


HERE = os.path.dirname(__file__)


class TestTrieWordCount(unittest.TestCase):

    def test_with_count(self):
        trie = Trie()
        trie.add_all(['ash', 'ashley', 'ashes', 'ashes'])
        expected = [('ash', 1), ('ashley', 1), ('ashes', 2)]
        self.assertListEqual(expected, trie.search('a*', with_count=True))

    def test_without_count(self):
        trie = Trie()
        trie.add_all(['ash', 'ashley', 'ashes', 'ashes'])
        expected = ['ash', 'ashley', 'ashes']
        self.assertListEqual(expected, trie.search('a*'))


class TestDAWGWordCount(unittest.TestCase):

    def test_with_count(self):
        d = DAWG()
        d.add_all(['ash', 'ashes', 'ashes', 'ashley'])
        d.reduce()
        expected = [('ash', 1), ('ashes', 2), ('ashley', 1)]
        self.assertListEqual(expected, d.search('a*', with_count=True))

    def test_without_count(self):
        d = DAWG()
        d.add_all(['ash', 'ashes', 'ashes', 'ashley'])
        d.reduce()
        expected = ['ash', 'ashes', 'ashley']
        self.assertListEqual(expected, d.search('a*'))
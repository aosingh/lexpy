import unittest
import os

from lexpy.trie import Trie
from lexpy.utils import build_trie_from_file
from lexpy.exceptions import InvalidWildCardExpressionError


HERE = os.path.dirname(__file__)

large_dataset = os.path.join(HERE, 'data/words.txt')
small_dataset = os.path.join(HERE, 'data/words2.txt')


class TestWordCount(unittest.TestCase):

    def test_word_count_greater_than_zero(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley', 'ashes'])
        self.assertGreater(self.trie.get_word_count(), 0, "The number of words should be greater than 0")
        self.assertEqual(3, self.trie.get_word_count(), "Word count not equal")

    def test_word_count_zero(self):
        self.trie = Trie()
        self.trie.add_all([])
        self.assertEqual(0, self.trie.get_word_count(), "Word count not equal")


class TestTrieExactWordSearch(unittest.TestCase):

    def test_word_in_trie(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertTrue('ash' in self.trie, "Word should be in trie")

    def test_word_not_int_trie1(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertFalse('salary' in self.trie, "Word should not be in trie")

    def test_word_not_int_trie2(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertFalse('mash lolley' in self.trie, "Word should not be in trie")


class TesTrieWordInsert(unittest.TestCase):

    def test_word_add(self):
        self.trie = Trie()
        self.trie.add('axe')
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('axe' in self.trie, "Word should be in trie")


    def test_word_add_all_list(self):
        self.trie = Trie()
        self.trie.add_all(['axe', 'kick']) #list
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('axe' in self.trie, "Word should be in trie")
        self.assertTrue('kick' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")

    def test_word_add_all_set(self):
        self.trie = Trie()
        self.trie.add_all({'axe', 'kick'}) #set
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('axe' in self.trie, "Word should be in trie")
        self.assertTrue('kick' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")

    def test_word_add_all_tuple(self):
        self.trie = Trie()
        self.trie.add_all(('axe', 'kick')) #tuple
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('axe' in self.trie, "Word should be in trie")
        self.assertTrue('kick' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")

    def test_word_add_all_with_number(self):
        self.trie = Trie()
        self.trie.add_all(('axe', 'kick', 3)) #tuple with one integer.
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('axe' in self.trie, "Word should be in trie")
        self.assertTrue('kick' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")

    def test_word_add_all_gen(self):
        def gen_words():
            a = ['ash', 'ashley', 'simpson']
            for word in a:
                yield word
        self.trie = Trie()
        self.trie.add_all(gen_words()) # generator
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertTrue('simpson' in self.trie, "Word should be in trie")
        self.assertEqual(3, self.trie.get_word_count(), "Word count not equal")

    def test_word_add_all_file_path(self):
        self.trie = Trie()
        self.trie.add_all(small_dataset) # From a file
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertTrue('simpson' in self.trie, "Word should be in trie")
        self.assertEqual(8, self.trie.get_word_count(), "Word count not equal")


class TestTrieNodeCount(unittest.TestCase):

    def test_trie_node_count(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")
        self.assertEqual(7, len(self.trie), "Number of nodes")


class TestTriePrefixExists(unittest.TestCase):

    def test_trie_node_prefix_exists(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")

        self.assertTrue(self.trie.contains_prefix('ash'), "Prefix should be present in Trie")
        self.assertTrue(self.trie.contains_prefix('as'), "Prefix should be present in Trie")
        self.assertTrue(self.trie.contains_prefix('a'), "Prefix should be present in Trie")

    def test_trie_node_prefix_not_exists(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(2, self.trie.get_word_count(), "Word count not equal")
        self.assertFalse(self.trie.contains_prefix('xmas'), "Prefix should be present in Trie")
        self.assertFalse(self.trie.contains_prefix('xor'), "Prefix should be present in Trie")
        self.assertFalse(self.trie.contains_prefix('sh'), "Prefix should be present in Trie")


class TestTriePrefixSearch(unittest.TestCase):

    def test_trie_prefix_search(self):
        self.trie = Trie()
        self.trie.add_all(['ashlame', 'ashley', 'askoiu', 'ashlo'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertFalse('ash' in self.trie, "Word should not be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(4, self.trie.get_word_count(), "Word count not equal")
        self.assertTrue(self.trie.contains_prefix('ash'), "Prefix should be present in Trie")
        self.assertEqual(sorted(self.trie.search_with_prefix('ash')), sorted(['ashlame', 'ashley', 'ashlo']), 'The lists should be equal')


class TestWildCardSearch(unittest.TestCase):

    def test_trie_asterisk_search(self):
        self.trie = Trie()
        self.trie.add_all(['ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(sorted(self.trie.search('a*')), sorted(['ash', 'ashley']), 'The lists should be equal')

    def test_trie_question_search(self):
        self.trie = Trie()
        self.trie.add_all(['ab', 'as', 'ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(sorted(self.trie.search('a?')), sorted(['ab', 'as']), 'The lists should be equal')

    def test_trie_wildcard_search(self):
        self.trie = Trie()
        self.trie.add_all(['ab', 'as', 'ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertEqual(sorted(self.trie.search('*a******?')), sorted(['ab', 'as', 'ash', 'ashley']), 'The lists should be equal')

    def test_trie_wildcard_exception(self):
        self.trie = Trie()
        self.trie.add_all(['ab', 'as', 'ash', 'ashley'])
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertRaises(InvalidWildCardExpressionError, self.trie.search, '#$%^a')


class TestBuildFromFile(unittest.TestCase):

    def test_trie_build_from_file_path(self):
        self.trie = build_trie_from_file(small_dataset)
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertTrue('simpson' in self.trie, "Word should be in trie")
        self.assertEqual(8, self.trie.get_word_count(), "Word count not equal")

    def test_trie_build_from_file_object(self):
        with open(small_dataset, 'r') as input_file:
            self.trie = build_trie_from_file(input_file)
        self.assertIsInstance(self.trie, Trie, "Object should be of type `lexpy.trie.Trie`")
        self.assertTrue('ash' in self.trie, "Word should be in trie")
        self.assertTrue('ashley' in self.trie, "Word should be in trie")
        self.assertTrue('simpson' in self.trie, "Word should be in trie")
        self.assertEqual(8, self.trie.get_word_count(), "Word count not equal")


if __name__ == '__main__':
    unittest.main()
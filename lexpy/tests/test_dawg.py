import os
import unittest

from lexpy.dawg import DAWG
from lexpy.utils import build_dawg_from_file
from lexpy.exceptions import InvalidWildCardExpressionError

HERE = os.path.dirname(__file__)

large_dataset = os.path.join(HERE, 'data/ridyhew_master.txt')
small_dataset = os.path.join(HERE, 'data/TWL06.txt')


class TestWordCount(unittest.TestCase):

    def test_word_count_greater_than_zero(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashes', 'ashley'])
        self.dawg.reduce()
        self.assertGreater(self.dawg.get_word_count(), 0, "The number of words should be greater than 0")
        self.assertEqual(3, self.dawg.get_word_count(), "Word count not equal")

    def test_word_count_zero(self):
        self.dawg = DAWG()
        self.dawg.add_all([])
        self.dawg.reduce()
        self.assertEqual(0, self.dawg.get_word_count(), "Word count not equal")


class TestDAWGExactWordSearch(unittest.TestCase):

    def test_word_in_dawg(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")

    def test_word_not_int_dawg1(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertFalse('salary' in self.dawg, "Word should not be in dawg")
    
    def test_word_not_int_dawg2(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertFalse('mash lolley' in self.dawg, "Word should not be in dawg")

class TesDAWGWordInsert(unittest.TestCase):

    def test_word_add(self):
        self.dawg = DAWG()
        self.dawg.add('axe')
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('axe' in self.dawg, "Word should be in dawg")


    def test_word_add_all_list(self):
        self.dawg = DAWG()
        self.dawg.add_all(['axe', 'kick']) #list
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('axe' in self.dawg, "Word should be in dawg")
        self.assertTrue('kick' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")

    def test_word_add_all_set(self):
        self.dawg = DAWG()
        self.dawg.add_all({'axe', 'kick'}) #set
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('axe' in self.dawg, "Word should be in dawg")
        self.assertTrue('kick' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")

    def test_word_add_all_tuple(self):
        self.dawg = DAWG()
        self.dawg.add_all(('axe', 'kick')) #tuple
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('axe' in self.dawg, "Word should be in dawg")
        self.assertTrue('kick' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")

    def test_word_add_all_with_number(self):
        self.dawg = DAWG()
        self.dawg.add_all(('axe', 'kick')) #tuple with one integer.
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('axe' in self.dawg, "Word should be in dawg")
        self.assertTrue('kick' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")

    def test_word_add_all_gen(self):
        def gen_words():
            a = ['ash', 'ashley', 'simpson']
            for word in a:
                yield word
        self.dawg = DAWG()
        self.dawg.add_all(gen_words()) # generator
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertTrue('simpson' in self.dawg, "Word should be in dawg")
        self.assertEqual(3, self.dawg.get_word_count(), "Word count not equal")

    def test_word_add_all_file_path(self):
        self.dawg = DAWG()
        self.dawg.add_all(small_dataset) # From a file
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('AARGH' in self.dawg, "Word should be in dawg")
        self.assertTrue('AARRGHH' in self.dawg, "Word should be in dawg")
        self.assertTrue('AAS' in self.dawg, "Word should be in dawg")
        self.assertEqual(178691, self.dawg.get_word_count(), "Word count not equal")


class TestDAWGNodeCount(unittest.TestCase):

    def test_dawg_node_count(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")
        self.assertEqual(6, len(self.dawg), "Number of nodes")

    def test_dawg_reduced_node_count(self):
        self.dawg = DAWG()
        self.dawg.add_all(["tap", "taps", "top", "tops"])
        self.dawg.reduce()
        self.assertEqual(6, len(self.dawg), "Number of nodes")


class TestDAWGPrefixExists(unittest.TestCase):
    def test_dawg_node_prefix_exists(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")

        self.assertTrue(self.dawg.contains_prefix('ash'), "Prefix should be present in DAWG")
        self.assertTrue(self.dawg.contains_prefix('as'), "Prefix should be present in DAWG")
        self.assertTrue(self.dawg.contains_prefix('a'), "Prefix should be present in DAWG")

    def test_dawg_node_prefix_not_exists(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(2, self.dawg.get_word_count(), "Word count not equal")
        self.assertFalse(self.dawg.contains_prefix('xmas'), "Prefix should be present in DAWG")
        self.assertFalse(self.dawg.contains_prefix('xor'), "Prefix should be present in DAWG")
        self.assertFalse(self.dawg.contains_prefix('sh'), "Prefix should be present in DAWG")


class TestDAWGPrefixSearch(unittest.TestCase):
    def test_dawg_prefix_search(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ashlame', 'ashley', 'ashlo', 'askoiu'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertFalse('ash' in self.dawg, "Word should not be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(4, self.dawg.get_word_count(), "Word count not equal")
        self.assertTrue(self.dawg.contains_prefix('ash'), "Prefix should be present in DAWG")
        self.assertEqual(sorted(self.dawg.search_with_prefix('ash')), sorted(['ashlame', 'ashley', 'ashlo']),
                              'The lists should be equal')


class TestWildCardSearch(unittest.TestCase):
    def test_dawg_asterisk_search(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(sorted(self.dawg.search('a*')), sorted(['ash', 'ashley']), 'The lists should be equal')

    def test_dawg_question_search(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ab', 'as', 'ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(sorted(self.dawg.search('a?')), sorted(['ab', 'as']), 'The lists should be equal')

    def test_dawg_wildcard_search(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ab', 'as', 'ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertEqual(sorted(self.dawg.search('*a******?')), sorted(['ab', 'as', 'ash', 'ashley']),
                              'The lists should be equal')

    def test_dawg_wildcard_exception(self):
        self.dawg = DAWG()
        self.dawg.add_all(['ab', 'as', 'ash', 'ashley'])
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ash' in self.dawg, "Word should be in dawg")
        self.assertTrue('ashley' in self.dawg, "Word should be in dawg")
        self.assertRaises(InvalidWildCardExpressionError, self.dawg.search, '#$%^a')


class TestBuildFromFile(unittest.TestCase):
    def test_dawg_build_from_file_path(self):
        self.dawg = build_dawg_from_file(small_dataset)
        self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ZYGOMORPHIES' in self.dawg, "Word should be in dawg")
        self.assertTrue('ZYGOMATA' in self.dawg, "Word should be in dawg")
        self.assertTrue('ZYGOMORPHY' in self.dawg, "Word should be in dawg")
        self.assertEqual(178691, self.dawg.get_word_count(), "Word count not equal")

    def test_dawg_build_from_file_object(self):
        with open(small_dataset, 'r') as input_file:
            self.dawg = build_dawg_from_file(input_file)
            self.dawg.reduce()
        self.assertIsInstance(self.dawg, DAWG, "Object should be of type `lexpy.dawg.DAWG`")
        self.assertTrue('ZYGOMORPHIES' in self.dawg, "Word should be in dawg")
        self.assertTrue('ZYGOMATA' in self.dawg, "Word should be in dawg")
        self.assertTrue('ZYGOMORPHY' in self.dawg, "Word should be in dawg")
        self.assertEqual(178691, self.dawg.get_word_count(), "Word count not equal")


class TestSearchWithinDistance(unittest.TestCase):

    def test_edit_distance_search(self):
        self.dawg = DAWG()
        input_words = ['abhor', 'abuzz', 'accept', 'acorn', 'agony', 'albay', 'albin', 'algin', 'alisa', 'almug',
                       'altai', 'amato', 'ampyx', 'aneto', 'arbil', 'arrow', 'artha', 'aruba', 'athie', 'auric',
                       'aurum', 'cap', 'common', 'dime', 'eyes', 'foot', 'likeablelanguage', 'lonely', 'look',
                       'nasty', 'pet', 'psychotic', 'quilt', 'shock', 'smalldusty', 'sore', 'steel', 'suit',
                       'tank', 'thrill']
        self.dawg.add_all(input_words)
        self.dawg.reduce()
        self.assertListEqual(self.dawg.search_within_distance('arie', dist=2), ['arbil', 'athie', 'auric'])



if __name__ == '__main__':
    unittest.main()
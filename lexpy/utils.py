from lexpy.trie import Trie
from lexpy.dawg import DAWG


def _build_from_file(input_file, clazz):
    fsa = clazz()
    fsa.add_all(input_file)
    return fsa


def build_dawg_from_file(input_file):
    return _build_from_file(input_file, clazz=DAWG)


def build_trie_from_file(input_file):
    return _build_from_file(input_file, clazz=Trie)
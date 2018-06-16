from __future__ import unicode_literals
from __future__ import absolute_import


from lexpy.trie import Trie
from lexpy.dawg import DAWG


def _build_from_file(infile=None, _type='Trie'):
    if infile is None:
        raise ValueError("Please provide the file path")
    fsa = None
    if _type == 'Trie':
        fsa = Trie()
        fsa.add_all(infile)
    elif _type == 'DAWG':
        fsa = DAWG()
        fsa.add_all(infile)
    return fsa


def build_dawg_from_file(infile=None):
    return _build_from_file(infile, _type='DAWG')


def build_trie_from_file(infile=None):
    return _build_from_file(infile)
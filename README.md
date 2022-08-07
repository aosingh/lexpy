# Lexpy

[![lexpy](https://github.com/aosingh/lexpy/actions/workflows/lexpy_build.yaml/badge.svg)](https://github.com/aosingh/lexpy/actions)
[![Downloads](https://pepy.tech/badge/lexpy)](https://pepy.tech/project/lexpy)
[![PyPI version](https://badge.fury.io/py/lexpy.svg)](https://pypi.python.org/pypi/lexpy)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![PyPy3.7](https://img.shields.io/badge/python-PyPy3.7-blue.svg)](https://www.pypy.org/download.html)
[![PyPy3.8](https://img.shields.io/badge/python-PyPy3.8-blue.svg)](https://www.pypy.org/download.html)
[![PyPy3.9](https://img.shields.io/badge/python-PyPy3.9-blue.svg)](https://www.pypy.org/download.html)



- A lexicon is a data-structure which stores a set of words. The difference between 
a dictionary and a lexicon is that in a lexicon there are **no values** associated with the words. 

- A lexicon is similar to a list of words or a set, but the internal representation is different and optimized
for faster searches of words, prefixes and wildcard patterns. 

- Given a word, precisely the search time is O(W) where W is the length of the word. 

- 2 important lexicon data-structures are:

    - Trie.
    - Directed Acyclic Word Graph (DAWG).

Both Trie and DAWG are Finite State Automaton (FSA)


# Install
```commandline
pip install lexpy
```

# Interface

| **Interface Description**                                                                                                     	| **Trie** method                           	| **DAWG** method                           	|
|-------------------------------------------------------------------------------------------------------------------------------	|-------------------------------------------	|-------------------------------------------	|
| Add a single word                                                                                                             	| `add('apple', count=2)`                            	| `add('apple', count=2)`                            	|
| Add multiple words                                                                                                            	| `add_all(['advantage', 'courage'])`       	| `add_all(['advantage', 'courage'])`       	|
| Check if exists?                                                                                                              	| `in` operator                             	| `in` operator                             	|
| Search using wildcard expression                                                                                              	| `search('a?b*', with_count=True)`             | `search('a?b*, with_count=True)`              |
| Search for prefix matches                                                                                                     	| `search_with_prefix('bar', with_count=True)`  | `search_with_prefix('bar')`               	|
| Search for similar words within  given edit distance. Here, the notion of edit distance  is same as Levenshtein distance 	| `search_within_distance('apble', dist=1, with_count=True)` 	| `search_within_distance('apble', dist=1, with_count=True)` 	|
| Get the number of nodes in the automaton 	| `len(trie)` 	| `len(dawg)` 	|


# Examples

## Trie

### Build from an input list, set, or tuple of words.

```python
from lexpy.trie import Trie

trie = Trie()

input_words = ['ampyx', 'abuzz', 'athie', 'athie', 'athie', 'amato', 'amato', 'aneto', 'aneto', 'aruba', 
               'arrow', 'agony', 'altai', 'alisa', 'acorn', 'abhor', 'aurum', 'albay', 'arbil', 'albin', 
               'almug', 'artha', 'algin', 'auric', 'sore', 'quilt', 'psychotic', 'eyes', 'cap', 'suit', 
               'tank', 'common', 'lonely', 'likeable' 'language', 'shock', 'look', 'pet', 'dime', 'small' 
               'dusty', 'accept', 'nasty', 'thrill', 'foot', 'steel', 'steel', 'steel', 'steel', 'abuzz']

trie.add_all(input_words) # You can pass any sequence types of a file like object here

print(trie.get_word_count())

>>> 48
```

### Build from a file or file path.

In the file, words should be newline separated.

```python

from lexpy.trie import Trie

# Either
trie = Trie()
trie.add_all('/path/to/file.txt')

# Or
with open('/path/to/file.txt', 'r') as infile:
     trie.add_all(infile)

```

### Check if exists using the `in` operator

```python
print('ampyx' in trie)

>>> True
```

### Prefix search

```python
print(trie.search_with_prefix('ab'))

>>> ['abhor', 'abuzz']
```

```python

print(trie.search_with_prefix('ab', with_count=True))

>>> [('abuzz', 2), ('abhor', 1)]

```

### Wildcard search using `?` and `*`

- `?` = 0 or 1 occurrence of any character

- `*` = 0 or more occurrence of any character

```python
print(trie.search('a*o*'))

>>> ['amato', 'abhor', 'aneto', 'arrow', 'agony', 'acorn']

print(trie.search('a*o*', with_count=True))

>>> [('amato', 2), ('abhor', 1), ('aneto', 2), ('arrow', 1), ('agony', 1), ('acorn', 1)]

print(trie.search('su?t'))

>>> ['suit']

print(trie.search('su?t', with_count=True))

>>> [('suit', 1)]

```

### Search for similar words using the notion of Levenshtein distance

```python
print(trie.search_within_distance('arie', dist=2))

>>> ['athie', 'arbil', 'auric']

print(trie.search_within_distance('arie', dist=2, with_count=True))

>>> [('athie', 3), ('arbil', 1), ('auric', 1)]

```

### Increment word count

- You can either add a new word or increment the counter for an existing word.

```python

trie.add('athie', count=1000)

print(trie.search_within_distance('arie', dist=2, with_count=True))

>>> [('athie', 1003), ('arbil', 1), ('auric', 1)]
```

# Directed Acyclic Word Graph (DAWG)

- DAWG supports the same set of operations as a Trie. The difference is the number of nodes in a DAWG is always
less than or equal to the number of nodes in Trie. 

- They both are Deterministic Finite State Automata. However, DAWG is a minimized version of the Trie DFA.

- In a Trie, prefix redundancy is removed. In a DAWG, both prefix and suffix redundancies are removed.

- In the current implementation of DAWG, the insertion order of the words should be **alphabetical**.

- The implementation idea of DAWG is borrowed from http://stevehanov.ca/blog/?id=115


```python
from lexpy.trie import Trie
from lexpy.dawg import DAWG

trie = Trie()
trie.add_all(['advantageous', 'courageous'])

dawg = DAWG()
dawg.add_all(['advantageous', 'courageous'])

len(trie) # Number of Nodes in Trie
23

dawg.reduce() # Perform DFA minimization. Call this every time a chunk of words are uploaded in DAWG.

len(dawg) # Number of nodes in DAWG
21

```

## DAWG

The APIs are exactly same as the Trie APIs

### Build a DAWG

```python
from lexpy.dawg import DAWG
dawg = DAWG()

input_words = ['ampyx', 'abuzz', 'athie', 'athie', 'athie', 'amato', 'amato', 'aneto', 'aneto', 'aruba', 
               'arrow', 'agony', 'altai', 'alisa', 'acorn', 'abhor', 'aurum', 'albay', 'arbil', 'albin', 
               'almug', 'artha', 'algin', 'auric', 'sore', 'quilt', 'psychotic', 'eyes', 'cap', 'suit', 
               'tank', 'common', 'lonely', 'likeable' 'language', 'shock', 'look', 'pet', 'dime', 'small' 
               'dusty', 'accept', 'nasty', 'thrill', 'foot', 'steel', 'steel', 'steel', 'steel', 'abuzz']


dawg.add_all(input_words)
dawg.reduce()

dawg.get_word_count()

>>> 48

```

### Check if exists using the `in` operator

```python
print('ampyx' in dawg)

>>> True
```

### Prefix search

```python
print(dawg.search_with_prefix('ab'))

>>> ['abhor', 'abuzz']
```

```python

print(dawg.search_with_prefix('ab', with_count=True))

>>> [('abuzz', 2), ('abhor', 1)]

```

### Wildcard search using `?` and `*`

`?` = 0 or 1 occurance of any character

`*` = 0 or more occurance of any character

```python
print(dawg.search('a*o*'))

>>> ['amato', 'abhor', 'aneto', 'arrow', 'agony', 'acorn']

print(dawg.search('a*o*', with_count=True))

>>> [('amato', 2), ('abhor', 1), ('aneto', 2), ('arrow', 1), ('agony', 1), ('acorn', 1)]

print(dawg.search('su?t'))

>>> ['suit']

print(dawg.search('su?t', with_count=True))

>>> [('suit', 1)]

```

### Search for similar words using the notion of Levenshtein distance

```python
print(dawg.search_within_distance('arie', dist=2))

>>> ['athie', 'arbil', 'auric']

print(dawg.search_within_distance('arie', dist=2, with_count=True))

>>> [('athie', 3), ('arbil', 1), ('auric', 1)]

```

### Alphabetical order insertion

If you insert a word which is lexicographically out-of-order, ``ValueError`` will be raised.
```python
dawg.add('athie', count=1000)
```
ValueError

```text
ValueError: Words should be inserted in Alphabetical order. <Previous word - thrill>, <Current word - athie>
```

### Increment the word count

- You can either add an alphabetically greater word with a specific count or increment the count of the previous added word.

```python


dawg.add_all(['thrill']*20000) # or dawg.add('thrill', count=20000)

print(dawg.search('thrill', with_count=True))

>> [('thrill', 20001)]

```

## Trie vs DAWG


![Number of nodes comparison](https://github.com/aosingh/lexpy/blob/master/lexpy_trie_dawg_nodes.png)

![Build time comparison](https://github.com/aosingh/lexpy/blob/master/lexpy_trie_dawg_time.png)



# Future Work

These are some ideas which I would love to work on next in that order. Pull requests or discussions are invited.

- Merge trie and DAWG features in one data structure
  -  Support all functionalities and still be as compressed as possible.
- Serialization / Deserialization
    - Pickle is definitely an option. 
- Server (TCP or HTTP) to serve queries over the network.


# Fun Facts
1. The 45-letter word pneumonoultramicroscopicsilicovolcanoconiosis is the longest English word that appears in a major dictionary.
So for all english words, the search time is bounded by O(45). 
2. The longest technical word(not in dictionary) is the name of a protein called as [titin](https://en.wikipedia.org/wiki/Titin). It has 189,819
letters and it is disputed whether it is a word.




![Logo](https://github.com/aosingh/lexpy/blob/master/images/lexpylogo.png)

[![PyPI version](https://badge.fury.io/py/lexpy.svg)](https://pypi.python.org/pypi/lexpy)
[![Travis](https://travis-ci.org/aosingh/lexpy.svg?branch=master)](https://travis-ci.org/aosingh/lexpy)
[![Build status](https://ci.appveyor.com/api/projects/status/hib5wm4qo2oop3ui?svg=true)](https://ci.appveyor.com/project/aosingh/lexpy)
[![Coverage Status](https://coveralls.io/repos/github/aosingh/lexpy/badge.svg?branch=master)](https://coveralls.io/github/aosingh/lexpy?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/60626f81c0db0c5d8dcd/maintainability)](https://codeclimate.com/github/aosingh/lexpy/maintainability)

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.3](https://img.shields.io/badge/python-3.3-blue.svg)](https://www.python.org/downloads/release/python-330/)
[![Python 3.4](https://img.shields.io/badge/python-3.4-blue.svg)](https://www.python.org/downloads/release/python-340/)
[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


>A lexicon is a data-structure which stores a set of words. The difference between 
a dictionary and a lexicon is that in a lexicon there are no values associated with the words. A lexicon is similar to a list of words or a set, but the internal representation is different and optimized
for faster searches(of words, prefixes and wildcard patterns). Precisely the search time is O(W) where W is the length of the word. 

2 important Lexicon data-structures are:
1. Trie.
3. Directed Acyclic Word Graph(DAWG).

Both Trie and DAWG are Finite State Automaton(FSA)

# Install
```commandline
pip install lexpy
```

# Interface

| **Interface Description**                                                                                                     	| **Trie** method                           	| **DAWG** method                           	| Notes                                                                                                                                                                                                                                                                   	|
|-------------------------------------------------------------------------------------------------------------------------------	|-------------------------------------------	|-------------------------------------------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Add a single word                                                                                                             	| `add('apple')`                            	| `add('apple')`                            	|                                                                                                                                                                                                                                                                         	|
| Add multiple words                                                                                                            	| `add_all(['advantage', 'courage'])`       	| `add_all(['advantage', 'courage'])`       	| Supports Python `sequence` types  or `file` like objects which provide the `read()` method.   When dealing with files, you can pass the path to the file.  For e.g. `add_all('path/to/bigfile.txt')`  In the current implementation,  each word should be on a newline. 	|
| Check if exists?                                                                                                              	| `in` operator                             	| `in` operator                             	|                                                                                                                                                                                                                                                                         	|
| Search using wildcard  expression                                                                                             	| `search('a?b*')`                          	| `search('a?b*)`                           	|                                                                                                                                                                                                                                                                         	|
| Search for prefix matches                                                                                                     	| `search_with_prefix('bar')`               	| `search_with_prefix('bar')`               	|                                                                                                                                                                                                                                                                         	|
| Search for similar words within  given edit distance. Here, the notion of edit distance  is same as Levenshtein distance (LD) 	| `search_within_distance('apble', dist=1)` 	| `search_within_distance('apble', dist=1)` 	|                                                                                                                                                                                                                                                                         	|



## Trie
```python
from lexpy.trie import Trie
trie = Trie()
trie.add_all(['abc', 'abcc', 'abcd']) # You can pass a set, list, generator or an input file or words
trie.get_word_count()
3

# Wildcard Pattern
trie.search('a*')
['abc', 'abcc', 'abcd']

trie.search('*d')
['abcd']

trie.add('axe') # Add a single word

trie.get_word_count()
4


trie.search_with_prefix('ax')
['axe']

```

## Directed Acyclic Word Graph (DAWG)

>DAWG supports the same set of operations as a Trie. The difference is the number of nodes in a DAWG is always
less than or equal to the number of nodes in Trie. They both are Deterministic Finite State Automata. 
However DAWG is a minimized version of the Trie DFA. (More stats coming in documentation). 
In Trie, prefix redundancy is removed.
In DAWG, both prefix and suffix redundancies are removed.

In the current implementation of DAWG, the insertion order of the words should be alphabetical. 


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
13

```



*Fun Facts* :
1. The 45-letter word pneumonoultramicroscopicsilicovolcanoconiosis is the longest English word that appears in a major dictionary.
So for all english words, the search time is bounded by O(45). 
2. The longest technical word(not in dictionary) is the name of a protein called as [titin](https://en.wikipedia.org/wiki/Titin). It has 189,819
letters and it is disputed whether it is a word.








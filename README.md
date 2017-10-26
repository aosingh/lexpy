![Logo](https://github.com/aosingh/lexpy/blob/master/images/lexpylogo.png)

[![Travis](https://img.shields.io/travis/aosingh/lexpy.svg)]()
[![Test Coverage](https://codeclimate.com/github/aosingh/lexpy/badges/coverage.svg)](https://codeclimate.com/github/aosingh/lexpy/badges/coverage.svg)

>A lexicon is a data-structure which stores a set of words. The difference between 
a dictionary and a lexicon is that in a lexicon there are no values associated with the words. A lexicon is similar to a list of words or a set, but the internal representation is different and optimized
for faster searches(of words, prefixes and wildcard patterns). Precisely the search time is O(W) where W is the length of the word. 


2 important Lexicon datastructures are:
1. Trie.
3. Directed Acyclic Word Graph(DAWG).

Both Trie and DAWG are Finite State Automaton(FSA)

*Fun Facts* :
1. The 45-letter word pneumonoultramicroscopicsilicovolcanoconiosis is the longest English word that appears in a major dictionary.
So for all english words, the search time is bounded by O(45). 
2. The longest technical word(not in dictionary) is the name of a protein called as [titin](https://en.wikipedia.org/wiki/Titin). It has 189,819
letters and it is disputed whether it is a word.






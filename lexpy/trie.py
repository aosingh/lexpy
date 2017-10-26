from collections import deque
from lexpy._utils import validate_expression, gen_source
from lexpy.exceptions import InvalidWildCardExpressionError

import os
import types



def build_trie_from_file(infile=None):
    """
        Description:
            This method can be used to create a Trie from an input file of words.
            Each word is expected to be on a new line.

        Args:
            :arg infile (str or File-like object): Either absolute file path or a File object

        Returns:
            :returns trie (`lexpy.trie.Trie`) : An instance of Trie class created after inserting all the words.

        Raises:
            :raises `ValueError` : If the input file is `None`
        """
    if infile is None:
        raise ValueError("Please provide the file path")
    trie = Trie()
    trie.add_all(infile)
    return trie


class _Node:
    """
    Description:
        A Trie Node

    Attributes:
        id (int) : Unique numerical ID assigned to this node
        val (str) : Label for the node. e.g. a letter from alphabet.
        children (dict) : Children Edges.
        eow (bool) : End of word(EOW) flag

    """
    def __init__(self, _id, val):
        """
        Description:
            Initialize a Trie Node.

        Args:
            :arg id (int) Unique numerical ID assigned to this node.
            :arg val (str) The Letter from alphabet.
        """
        self.id = _id
        self.val = val
        self.children = {}
        self.eow = False

    def add_child(self, letter, _id=None):
        """
        Description:
            To add a child edge to the current Node.

        Args:
            :arg letter (str) The character label that the child node will have.
            :arg id (int) Unique numerical ID assigned to this node.

        """
        self.children[letter] = _Node(_id, letter)

    def __getitem__(self, letter):
        """
        Description:
            Returns the child node. To use this method first check if the key is present in the dictionary of children
            edges.

        Args:
            :arg (str) The letter(or label) corresponding to the child node

        Returns:
            :return (_Node) The child Node
        """
        return self.children[letter]

    def __eq__(self, other):
        """
        Description:
            Currently, if the IDs are equal then the nodes are equal.

        Args:
            :arg (_Node)
        :return:
        """
        if self.id == other.id:
            return True
        return False

    def __iter__(self):
        """
        Description:
            Iterate over a Trie node in a Breadth First Search(BFS) manner.

        Args:
            :arg (_Node)

        Returns:
            :returns : A generator expression which can be used to iterate over the children of this node

        :return:
        """
        queue = deque()
        queue.append(self)
        while queue:
            current_node = queue.popleft()
            yield current_node
            queue.extend([child for _, child in current_node.children.iteritems()])

    def __repr__(self):
        return "{0}(id={1}, label={2}, EOW={3})".format(_Node, self.id, self.val, self.eow)


class Trie:

    """
    Description:
        To create a Trie instance, create an object of this class.

    Attributes:
        root: (_Node) The Top level node which is created every time you create a Trie instance

    """
    def __init__(self):
        """
        Description:
            This method initializes the Trie instance by creating the root node.
            By default, the id of the root node is 1 and number of words in the Trie is also 1.
            The label of the root node is an empty string ''.
        """
        self.__id = 1
        self.__num_of_words = 1
        self.root = _Node(self.__id, '')

    def __contains__(self, word):
        """
        Description:
            To enable the use of 'in' keyword on trie. Returns true if the word is present in trie else false

        Args:
            :arg word (str) The word to be searched

        Returns:
            :returns contains (boolean) True or False
        """
        if word == '':
            return True # The root is an empty string. So it is always present
        if word is None:
            return False
        node = self.root
        for i in range(0, len(word)):
            letter = word[i]
            if letter in node.children:
                node = node[letter]
                if node.eow and i == len(word)-1:
                    return True
        return False

    def __len__(self):
        """
        Description:
            Returns the number of nodes in the Trie Data Structure

        Returns:
            :returns (int) Number of Nodes in the trie data structure
        :return:
        """
        return self.__id

    def __contains_prefix(self, prefix):
        """
        Description:
            Checks whether the prefix is present in the Trie. If yes, returns (True, node) where the prefix ends else
            returns (False, None)

        Arguments:
            :arg (str) prefix: The Prefix string

        Returns:
            :returns (tuple)(exists, node):  If yes, returns (True, node) where the prefix ends else
            returns (False, None)

        """
        if prefix == '':
            return True, self.root
        if prefix is None:
            return False, None
        node = self.root
        for i in range(0, len(prefix)):
            letter = prefix[i]
            if letter in node.children:
                node = node[letter]
            else:
                return False, None
        return True, node

    def contains_prefix(self, prefix):
        """
        Description:
            Returns a boolean indicating the presence of prefix in the Trie data-structure

        Arguments:
            :arg (str) prefix: The Prefix string

        Returns:
            :returns (boolean) True, if present, else False.

        """
        contains, _ = self.__contains_prefix(prefix)
        return contains

    @staticmethod
    def __words_with_wildcard(node, wildcard, index, currentWord):
        """
        Description:
            Returns all the words where the wildcard pattern matches.
            This method uses backtracking to recursively traverse nodes in the Trie for wildcard characters '?' and '*'

        Args:
            :arg node(lexpy.trie.Trie): Current Node in the Trie
            :arg wildcard (str) : The wildcard pattern as input
            :arg index (int): The current index in the wildcard pattern
            :arg currentWord (str): Word formed till now

        Returns:
            :returns words(list): Returns the list of words where the wildcard pattern matches.

        """
        if node is None or wildcard is None or wildcard == '' or index < 0:
            return None

        if node.eow \
            and index >= len(wildcard) \
            and currentWord is not None \
            and len(currentWord) != 0 :
            return [currentWord]

        if index >= len(wildcard):
            return None

        if currentWord is None:
            currentWord = ""

        words = []

        letter = wildcard[index]

        if letter == '?':
            for child in node.children:
                childnode = node[child]
                new_word = currentWord+child
                childwords = Trie.__words_with_wildcard(childnode, wildcard, index+1, new_word)
                if childwords is not None and len(childwords) > 0:
                    words.extend(childwords)
        elif letter == '*':
            words_at_current_level = Trie.__words_with_wildcard(node, wildcard, index+1, currentWord)
            if words_at_current_level is not None and len(words_at_current_level) > 0:
                words.extend(words_at_current_level)
            if node.children:
                for child in node.children:
                    childnode = node[child]
                    new_word = currentWord+child
                    childwords = Trie.__words_with_wildcard(childnode, wildcard, index, new_word)
                    if childwords is not None and len(childwords) > 0:
                        words.extend(childwords)
            elif node.eow and index==len(wildcard)-1:
                return [currentWord]
        else:
            if letter in node.children:
                childnode = node[letter]
                new_word = currentWord+childnode.val
                childwords = Trie.__words_with_wildcard(childnode, wildcard, index+1, new_word)
                if childwords is not None and len(childwords) > 0:
                    words.extend(childwords)
        return words

    def search(self, wildcard):
        """
        Description:
            Returns all the words where the wildcard pattern matches.

        Args:
            :arg wildcard(str) : The wildcard pattern as input

        Returns:
            :returns words(list): Returns the list of words where the wildcard pattern matches.

        """
        words = []
        assert wildcard is not None, "Search word cannot be None"
        if wildcard == '':
            return words
        try:
            wildcard = validate_expression(wildcard)
        except InvalidWildCardExpressionError as e:
            raise e
        if wildcard.isalpha():
            if self.__contains__(wildcard):
                words.append(wildcard)
            return words
        result = Trie.__words_with_wildcard(self.root, wildcard, 0, None)
        return result

    def search_with_prefix(self, prefix):
        """
        Description:
            Returns a list of words which share the same prefix as passed in input. The words are by default sorted
            in the increasing order of length.

        Arguments:
            :arg (str) prefix: The Prefix string

        Returns:
            :returns (list) words: which share the same prefix as passed in input

        """
        words = []
        if prefix == '' or prefix is None:
            return None
        _, node = self.__contains_prefix(prefix)
        if node is None:
            return None
        return self.__words_with_wildcard(node, '*', 0, prefix)

    def add(self, word):
        """
        Description:
            Adds a word in the trie data structure.

        Args:
            :arg word (str) : The word that you want to insert in the trie.

        Raises:
            :raises: ``AssertionError`` if the word is None

        """
        assert word is not None, "Input word cannot be None"

        node = self.root
        for i in range(0, len(word)):
            letter = word[i]
            if letter not in node.children:
                self.__id += 1
                node.add_child(letter, _id=self.__id)
            node = node[letter]
            if i == len(word)-1:
                node.eow = True
                self.__num_of_words += 1

    def add_all(self, source):
        """
        Description:
            Add a collection of words from any of the following passed in input
                1. File (complete path to the file) or a `File` type
                2. Generator
                3. List
                4. Set
                5. Tuple
            Words which are not of type string are not inserted in the Trie

        Args:
            :arg source (list, set, tuple, Generator, File)

        Returns:
            None

        """
        if type(source) not in [list, set, tuple, types.GeneratorType, str, file]:
            raise ValueError("Source type {0} not supported ".format(type(source)))

        if type(source) in [str, file]:
            if type(source) == str and not os.path.exists(source):
                raise IOError("File does not exists")
            source = gen_source(source)

        for word in source:
            if type(word) == str:
                self.add(word)

    def get_word_count(self):
        """
        Description:
            Returns the number of words in Trie Data structure

        Returns:
            :returns (int) Number of words
        """
        return max(0, self.__num_of_words-1)
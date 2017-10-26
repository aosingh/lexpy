import os
import types

from collections import deque
from lexpy._utils import validate_expression, gen_source
from lexpy.exceptions import InvalidWildCardExpressionError


class FSANode:
    """
    Class for Finite State Automaton(FSA) Node. Both Trie and Directed-Acyclic-Word-Graph(DAWG) nodes inherit from
    this class.
    """
    def __init__(self, _id, val):
        """
        Description:
            Initialize a Finite State Automaton(FSA) Node.

        Args:
            :arg _id (int) Unique numerical ID assigned to this node.
            :arg val (str) The Letter from alphabet.
        """
        self.id = _id
        self.val = val
        self.children = {}
        self.eow = False

    def __getitem__(self, letter):
        """
        Description:
            Returns the child node. To use this method first check if the key is present in the dictionary of children
            edges or use default as None

        Args:
            :arg (str) The letter(or label) corresponding to the child node

        Returns:
            :return (FSANode) The child Node
        """
        return self.children[letter]

    def __iter__(self):
        """
        Description:
            Iterate over a node in a Breadth First Search(BFS) manner.

        Args:
            :arg (FSANode)

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

    def __str__(self):
        """
        Description:
            Outputs a string representation of the FSA node. This is invoked when str(`FSANode`) is called.

        :return:
        """
        strarr = []
        if self.eow:
            strarr.append("1")
        else:
            strarr.append("0")

        for letter, node in self.children.iteritems():
            strarr.append(letter)
            strarr.append(str(node.id))

        return ",".join(strarr)

    def __eq__(self, other):
        """
        Description:
            Equal only if string representations are same.

        :param other:
        :return: bool
        """
        return self.__str__() == other.__str__()

    def __hash__(self):
        """
        Description:
            Call the __hash__() method on the string representation.

        :return:
        """
        return self.__str__().__hash__()

    def __repr__(self):
        """
        Description:
            Returns a nicely formatted string of the FSA node. This is invoked when `print()` is called.
        :return:
        """
        return "{0}(id={1}, label={2}, EOW={3})".format(self.__class__.__name__, self.id, self.val, self.eow)


class FSA:

    def __init__(self, root):
        """
        Description:
            This method initializes the Trie instance by creating the root node.
            By default, the id of the root node is 1 and number of words in the Trie is also 1.
            The label of the root node is an empty string ''.
        """
        self._id = 1
        self._num_of_words = 1
        self.root = root

    def __contains__(self, word):
        """
        Description:
            To enable the use of 'in' keyword on dawg. Returns true if the word is present in dawg else false

        Args:
            :arg word (str) The word to be searched

        Returns:
            :returns contains (boolean) True or False
        """
        if word == '':
            return True  # The root is an empty string. So it is always present
        if word is None:
            return False
        node = self.root
        for i in range(0, len(word)):
            letter = word[i]
            if letter in node.children:
                node = node[letter]
                if node.eow and i == len(word) - 1:
                    return True
        return False

    def __contains_prefix(self, prefix):
        """
        Description:
            Checks whether the prefix is present in the DAWG. If yes, returns (True, node) where the prefix ends else
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
            Returns a boolean indicating the presence of prefix in the DAWG data-structure

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
            This method uses backtracking to recursively traverse nodes in the DAWG for wildcard characters '?' and '*'

        Args:
            :arg node(lexpy.dawg.DAWG): Current Node in the DAWG
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
                and len(currentWord) != 0:
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
                new_word = currentWord + child
                childwords = FSA.__words_with_wildcard(childnode, wildcard, index + 1, new_word)
                if childwords is not None and len(childwords) > 0:
                    words.extend(childwords)
        elif letter == '*':
            words_at_current_level = FSA.__words_with_wildcard(node, wildcard, index + 1, currentWord)
            if words_at_current_level is not None and len(words_at_current_level) > 0:
                words.extend(words_at_current_level)
            if node.children:
                for child in node.children:
                    childnode = node[child]
                    new_word = currentWord + child
                    childwords = FSA.__words_with_wildcard(childnode, wildcard, index, new_word)
                    if childwords is not None and len(childwords) > 0:
                        words.extend(childwords)
            elif node.eow and index == len(wildcard) - 1:
                return [currentWord]
        else:
            if letter in node.children:
                childnode = node[letter]
                new_word = currentWord + childnode.val
                childwords = FSA.__words_with_wildcard(childnode, wildcard, index + 1, new_word)
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
        result = FSA.__words_with_wildcard(self.root, wildcard, 0, None)
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
        return FSA.__words_with_wildcard(node, '*', 0, prefix)

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

        if type(source) in [list, set, tuple]:
            source = sorted(source)

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
        return max(0, self._num_of_words - 1)







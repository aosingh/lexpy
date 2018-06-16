from __future__ import unicode_literals
from __future__ import absolute_import


from lexpy._base.node import FSANode
from lexpy._base.automata import FSA


class _TrieNode(FSANode):

    def add_child(self, letter, _id=None):
        """
        Description:
            To add a child edge to the current Node.

        Args:
            :arg letter (str) The character label that the child node will have.
            :arg id (int) Unique numerical ID assigned to this node.

        """
        self.children[letter] = _TrieNode(_id, letter)


class Trie(FSA):

    """
    Description:
        To create a Trie instance, create an object of this class.

    Attributes:
        root: (_TrieNode) The Top level node which is created every time you create a Trie instance

    """
    def __init__(self):
        """
        Description:
            This method initializes the Trie instance by creating the root node.
            By default, the id of the root node is 1 and number of words in the Trie is also 1.
            The label of the root node is an empty string ''.
        """
        root = _TrieNode(1, '')
        FSA.__init__(self, root)

    def __len__(self):
        """
        Description:
            Returns the number of nodes in the Trie Data Structure

        Returns:
            :returns (int) Number of Nodes in the trie data structure
        :return:
        """
        return self._id

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
                self._id += 1
                node.add_child(letter, _id=self._id)
            node = node[letter]
            if i == len(word)-1:
                node.eow = True
                self._num_of_words += 1
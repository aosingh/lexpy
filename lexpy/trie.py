from lexpy._base.node import FSANode
from lexpy._base.automata import FSA

__all__ = ['Trie']


class Trie(FSA):

    __slots__ = 'root'

    def __init__(self):
        """Initialize a Trie

        Description:
            This method initializes a Trie instance by adding the root node.
            By default, the id of the root node is 1 and number of words in the Trie is also 1.
            The label of the root node is an empty string ''
        """
        root = FSANode(0, '')
        super(Trie, self).__init__(root)

    def __len__(self):
        """Returns the number of nodes in the Trie

        Returns:
            length (int) -> Number of Nodes in the trie data structure
        """
        return self._id

    def add(self,
            word: str,
            count: int = 1):
        """Adds a word in the trie

        Description:
            Add a word and optionally specify the count

        Args:
            word (str) : The word that you want to insert in the trie.
            count (int): Count of the word. Default value is 1.

        Raises:
            ValueError if the word is None

        """
        if word is None:
            raise ValueError("Input word cannot be None")

        node = self.root
        for i, letter in enumerate(word):
            if letter not in node.children:
                self._id += 1
                node.add_child(letter, _id=self._id)
            node = node[letter]
            if i == len(word)-1:
                node.eow = True
                node.count += count
                self._num_of_words += count

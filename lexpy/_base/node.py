class FSANode:
    """
    Class for Finite State Automaton(FSA) Node. Both Trie and Directed Acyclic Word Graph (DAWG) node definitions
    inherit from this class.

    """

    __slots__ = 'id', 'val', 'children', 'eow', 'count'

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
        self.count = 0

    def add_child(self, letter, _id=None):
        """
        Description:
            To add a child edge to the current Node.

        Args:
            :arg letter (str) The character label that the child node will have.
            :arg id (int) Unique numerical ID assigned to this node.

        """
        self.children[letter] = FSANode(_id, letter)

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

    def __str__(self):
        """
        Description:
            Outputs a string representation of the FSA node. This is invoked when str(`FSANode`) is called.

        :return:
        """
        strarr = [self.val, str(self.count)]

        if self.eow:
            strarr.append("1")
        else:
            strarr.append("0")

        for letter, node in self.children.items():
            strarr.append(letter)
            strarr.append(str(node.id))

        return "".join(strarr)

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
            Returns a nicely formatted string of the FSA node. This is invoked when `repr()` is called.
        :return:
        """
        return "{0}(id={1}, label={2}, EOW={3}, count={4})".format(self.__class__.__name__, self.id, self.val, self.eow, self.count)

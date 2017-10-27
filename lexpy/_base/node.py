from collections import deque

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

    '''
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
    '''

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
            Returns a nicely formatted string of the FSA node. This is invoked when `repr()` is called.
        :return:
        """
        return "{0}(id={1}, label={2}, EOW={3})".format(self.__class__.__name__, self.id, self.val, self.eow)

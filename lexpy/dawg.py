from lexpy._base.node import FSANode
from lexpy._base.automata import FSA

__all__ = ['DAWG']


class DAWG(FSA):

    __slots__ = 'root', '__prev_word', '__prev_node', '__minimized_nodes', '__unchecked_nodes'

    def __init__(self):
        root = FSANode(1, '')
        super(DAWG, self).__init__(root=root)
        self.__prev_word = ''
        self.__prev_node = root
        self.__minimized_nodes = {}
        self.__unchecked_nodes = []

    def add(self, word, count=1):
        if word < self.__prev_word:
            raise ValueError(f"Words should be inserted in alphabetical order\n"
                             f"Previous word was '{self.__prev_word}' and current word is '{word}'")
        elif word == self.__prev_word:
            self.__prev_node.count += count
        else:
            # find common prefix between word and previous word
            common_prefix_index = 0
            for i, letters in enumerate(zip(word, self.__prev_word), start=1):
                if letters[0] != letters[1]:
                    break
                common_prefix_index = i

            self._reduce(common_prefix_index)

            if len(self.__unchecked_nodes) == 0:
                node = self.root
            else:
                node = self.__unchecked_nodes[-1][2]

            for letter in word[common_prefix_index:]:
                _id = self._id + 1
                node.add_child(letter, _id)
                self.__unchecked_nodes.append((node, letter, node.children[letter]))
                node = node.children[letter]
                self._id = _id

            node.eow = True
            node.count += count
            self.__prev_node = node

        self._num_of_words += count
        self.__prev_word = word

    def reduce(self):
        self._reduce(0)

    def _reduce(self, to):
        for i in reversed(range(to, len(self.__unchecked_nodes))):
            parent, letter, child = self.__unchecked_nodes[i]
            # If there are children
            if child.children and child in self.__minimized_nodes:
                parent.children[letter] = self.__minimized_nodes[child]
            else:
                self.__minimized_nodes[child] = child

            self.__unchecked_nodes.pop()

    def add_all(self, source):
        """Add all words from a Sequence datatype or File like object

        Args:
            source: Sequence datatype (list, set, tuple) or a file like object

        """
        if isinstance(source, (list, set, tuple)):
            source = sorted(source)
        super(DAWG, self).add_all(source=source)

    def __len__(self):
        """Returns the number of nodes in DAWG instance

        """
        return len(self.__minimized_nodes)

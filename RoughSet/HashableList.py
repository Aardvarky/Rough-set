class HashableList(list):
    def __key(self):
        return tuple(k for k in self)

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()
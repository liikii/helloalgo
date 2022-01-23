"""
reference:
implemented by list
"""


class Stack:
    def __init__(self):
        self._items = list()

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)

    def push(self, element):
        self._items.append(element)

    def pop(self):
        assert not self.is_empty()
        return self._items.pop()

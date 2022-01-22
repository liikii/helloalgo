# -*- coding: utf-8 -*-
"""
simple binary tree example.
from tutorials point.
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    # recursion
                    self.left.insert(data)
            # TODO: ignore equality.
            # symmetry.
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            # root
            self.data = Node(data)

    def inorder_traversal(self, root):
        # left -> root -> right.
        # recursion.
        r = []
        if root:
            # add left then add root , then add right.
            r += self.inorder_traversal(root.left)
            r += [root.data]
            r += self.inorder_traversal(root.right)
        return r

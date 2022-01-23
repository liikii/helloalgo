# -*- coding: utf8 -*-
"""
generic binary search tree
======================================
"""


class BSTNode:
    """
    Node
    """
    def __init__(self):
        self.element = None
        self.left = None
        self.right = None

    # __lt__, __le__, __eq__, __ne__, __gt__, __ge__
    # def __lt__(self, other):
    #     return self.element >
    #     pass


class BST:
    """
    __delete__ func
    """
    def __init__(self):
        # implemented by linked element.
        self.root = None

    def insert(self, element):
        """
        from root find the place for inserting new node.
        """
        current_node: BSTNode = self.root
        previous = None
        while current_node is not None:
            previous = current_node
            if element < current_node.element:
                current_node = current_node.left
            else:
                current_node = current_node.right

        

        pass

    def is_empty(self) -> bool:
        return self.root is None

    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def search(self, element):
        pass

    def breadth_first(self):
        pass

    def iterative_preorder(self):
        pass

    def iterative_inorder(self):
        pass

    def iterative_postorder(self):
        pass

    def morris_inorder(self):
        pass

    def delete_by_merging(self):
        pass

    def find_and_delete_by_merging(self):
        pass

    def delete_by_coping(self):
        pass

    def balance(self):
        pass

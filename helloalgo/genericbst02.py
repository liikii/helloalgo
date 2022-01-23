# -*- coding: utf8 -*-
"""
generic binary search tree
======================================
"""
from typing import Union
from helloalgo.stack03 import Stack


class BSTNode:
    """
    Node
    """
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

    def visit(self):
        print(self.element)
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
        non-recursion.
        """
        current_node: BSTNode = self.root
        previous: Union[BSTNode, None] = None
        direction = 0
        while current_node is not None:
            previous = current_node
            if element < current_node.element:
                current_node = current_node.left
                direction = 0  # left
            elif element > current_node.element:
                current_node = current_node.right
                direction = 1  # right
            else:
                # element already in tree, do nothing.
                return
        new_node = BSTNode(element)
        if self.root is None:
            self.root = new_node
        elif direction == 0:
            previous.left = new_node
        else:
            previous.right = new_node

    def recursive_insert(self):
        pass

    def is_empty(self) -> bool:
        return self.root is None

    @staticmethod
    def preorder(node: BSTNode):
        # root -> left -> right.
        # recursion.
        if node is not None:
            node.visit()
            BST.preorder(node.left)
            BST.preorder(node.right)

    def iterative_preorder(self):
        # root -> left -> right.
        traversal_stack = Stack()
        bst_node: BSTNode = self.root
        if bst_node is not None:
            traversal_stack.push(bst_node)
            while not traversal_stack.is_empty():
                print('stack len --> ', len(traversal_stack))
                n = traversal_stack.pop()
                n.visit()
                if n.right is not None:
                    traversal_stack.push(n.right)
                # left on the pop of stack.
                if n.left is not None:
                    traversal_stack.push(n.left)

    def inorder(self):
        pass

    def postorder(self):
        pass

    def search(self, element):
        """
        non recursion.
        """
        current_node: BSTNode = self.root
        while current_node is not None:
            if current_node.element == element:
                return current_node.element
            elif current_node.element < element:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None

    def recursive_search(self, element):
        pass

    def breadth_first(self):
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

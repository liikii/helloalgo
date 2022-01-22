# -*- coding:utf8 -*-
from unittest import TestCase
from helloalgo.binarytree01 import Node


class Test01(TestCase):
    def test_1(self):
        n = Node(3)
        n.insert(4)
        n.insert(2)
        n.print_tree()
        self.assertTrue(True)

    def test_inorder(self):
        n = Node(3)
        n.insert(4)
        n.insert(2)
        print(n.inorder_traversal(n))
        self.assertTrue(True)

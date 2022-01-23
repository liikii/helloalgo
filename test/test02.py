# -*- coding: utf-8 -*-
from unittest import TestCase

from helloalgo.genericbst02 import BST


class Test02(TestCase):
    def test_insert(self):
        b = BST()
        b.insert(9)
        b.insert(8)
        b.insert(10)
        BST.preorder(b.root)
        self.assertTrue(True)

    def test_list(self):
        a = list()
        a.append(3)
        a.append(4)
        b = a.pop()
        print(b)
        print(a)
        self.assertTrue(True)

    def test_iterative_preorder(self):
        b = BST()
        b.insert(9)
        b.insert(8)
        b.insert(10)

        b.insert(5)
        b.insert(15)

        b.insert(6)
        b.insert(16)

        b.iterative_preorder()
        self.assertTrue(True)

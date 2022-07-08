import pytest

from trees.trees import *
tree1 = BinaryTree()

tree2 = BinaryTree()
tree2.root = Node(2)
tree2.root.left = Node(7)
tree2.root.left.left = Node(2)
tree2.root.left.right = Node(6)
tree2.root.left.right.left = Node(5)
tree2.root.left.right.right = Node(11)
tree2.root.right = Node(5)
tree2.root.right.right = Node(9)
tree2.root.right.right.left = Node(4)

def test_empty_stack():
    actual = tree1.find_max()
    expected = None
    assert actual == expected


def test_find_max_in_tree():
    """
    this test for finding the max value in a tree
    """
    actual = tree2.find_max()
    expected = 11
    assert actual == expected


def test_find_max_in_tree_two():
    """
    this test for finding the max value in a tree
    """
    tree2.root.right.right.right = Node(100)
    actual = tree2.find_max()
    expected = 100
    assert actual == expected






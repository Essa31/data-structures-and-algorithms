import pytest
from trees import *

import pytest
from trees.trees import *


def test_exists():
    assert BinarySearchTree


def test_instantiate_empty():
    """
    instantiate BinarySearchTree instances
    """
    tree = BinarySearchTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_add_to_empty():
    """
    add node to empty tree
    """
    tree = BinarySearchTree()
    tree.add(10)
    actual = tree.root.value
    expected = 10
    assert actual == expected


def test_add_left():
    """
    can successfully add a left child
    """
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    actual = tree.root.left.value
    expected = 5
    assert actual == expected


def test_add_right():
    """
     can successfully add a right child
    """
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(15)
    actual = tree.root.right.value
    expected = 15
    assert actual == expected


def test_add_in_deep_right(tree):
    """
     can successfully add in deep right child
    """
    tree.add(30)
    actual = tree.root.right.right.value
    expected = 30
    assert actual == expected


def test_add_in_deep_left(tree):
    """
    can successfully add in deep left child
    """
    tree.add(1)
    actual = tree.root.left.left.left.value
    expected = 1
    assert actual == expected


def test_contains(tree):
    """
    Returns True if the value exists in the tree
    """
    actual = tree.contains(3)
    expected = True
    assert actual == expected


def test_not_contains(tree):
    """
    Returns False if the value not exists in the tree
    """
    actual = tree.contains(100)
    expected = False
    assert actual == expected

def test_exists():
    assert Node


def test_create_node():
    """
    check if the node is created and it's pointers
    """
    node = Node(100)
    assert node
    assert node.left is None
    assert node.right is None


def test_tree_exists():
    """
    Can successfully instantiate a tree with a single root node
    """
    tree = BinaryTree()
    tree.root = Node(50)
    actual = tree.root.left
    expected = None
    actual2 = tree.root.right
    expected2 = None


def test_tree_root_exists():
    """
    Can successfully instantiate an empty tree
    """
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected


def test_post_order(tree):
    """
    Can successfully return a collection from a postorder traversal
    """
    actual = tree.post_order()   # left, right, root
    expected = [1, 20, 5, 15, 10]
    assert actual == expected


def test_pre_order(tree):
    """
    Can successfully return a collection from a preorder traversal
    """
    actual = tree.pre_order()   # root,left, right
    expected = [10, 5, 1, 20, 15]
    assert actual == expected


def test_in_order(tree):
    """
    Can successfully return a collection from an inorder traversal
    """
    actual = tree.in_order()
    expected = [1, 5, 20, 10, 15]  # left, root, right
    assert actual == expected



@pytest.fixture
def tree():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(20)
    return tree


@pytest.fixture
def tree():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    tree.add(3)
    return
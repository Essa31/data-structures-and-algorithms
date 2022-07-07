import pytest
from trees.tree_breadth_first import *

#root1-----------------------------------------
trees=BinaryTree()
root1 = Node(1)
root1.left = Node(6)
root1.right = Node(3)
root1.left.left = Node(7)
root1.left.right = Node(5)
#root2-----------------------------------------
root2 = Node(1)
root2.left = Node(5)
root2.right = Node(3)
root2.left.left = Node(10)
root2.left.right = Node(9)
#root3-----------------------------------------
root3 = Node(1)
root3.left = Node(5)
root3.right = Node(3)
root3.left.left = Node(7)
root3.left.right = Node(13)
#root4---------------------------------------------
root4=BinarySearchTree()

def test_breadth_first():


    actual = trees.breadth_first(root1)
    expected = [1,6,3,7,5]
    assert actual == expected

def test_empty_tree():
    with pytest.raises(Exception) as exc:
        trees.breadth_first(root4)

        raise Exception( "tree is empty")

def test_breadth_first2():
    actual = trees.breadth_first(root2)
    expected = [1, 5, 3, 10, 9]
    assert actual == expected


def test_breadth_first3():
    actual = trees.breadth_first(root3)
    expected = [1, 5, 3, 7, 13]
    assert actual == expected
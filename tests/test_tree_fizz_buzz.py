import pytest
from trees.tree_fizz_buzz   import *

#root1-----------------------------------------

trees=K_Tree()
root1 = K_Node(1)
root1.left = K_Node(6)
root1.right = K_Node(3)
root1.left.left = K_Node(7)
root1.left.right = K_Node(5)
#root2-----------------------------------------
root2 = K_Node(1)
root2.left = K_Node(5)
root2.right = K_Node(3)
root2.left.left = K_Node(10)
root2.left.right = K_Node(9)
#root3-----------------------------------------
root3 = K_Node(1)
root3.left = K_Node(5)
root3.right = K_Node(3)
root3.left.left = K_Node(11)
root3.left.right = K_Node(15)
#root4---------------------------------------------
root4=K_Node(None)

def test_breadth_first():
    trees.fizz_buzz_tree(root1)


    actual = trees.print_tree_as_arr(root1)
    expected = [1,"Fizz","Fizz",7,"Buzz"]
    assert actual == expected

def test_empty_tree():
    with pytest.raises(Exception) as exc:
        trees.print_tree_as_arr(root4)

        raise Exception( "tree is empty")

def test_breadth_first2():
    trees.fizz_buzz_tree(root2)


    actual = trees.print_tree_as_arr(root2)
    expected = [1, "Buzz", "Fizz", "Buzz", "Fizz"]
    assert actual == expected


def test_breadth_first3():
    trees.fizz_buzz_tree(root3)


    actual = trees.print_tree_as_arr(root3)
    expected = [1, "Buzz", "Fizz", 11, "FizzBuzz"]
    assert actual == expected
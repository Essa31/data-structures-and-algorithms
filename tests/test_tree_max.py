import pytest

from trees.trees import *

t = BinarySearchTree()
t.add(10)
t.add(5)
t.add(8)
t.add(3)
t.add(20)
t.add(25)
t.add(15)

b=BinarySearchTree()
b.add(5)
b.add(80)
b.add(90)
b.add(20)
b.add(30)
b.add(15)

c = BinarySearchTree()
def test_max_value():

    actual = t.maxValue()
    expected = 25
    assert actual == expected

def test_empty_tree():
    with pytest.raises(Exception) as exc:
        c.dequeue()

        raise Exception( "tree is empty")

def test_max_value1():
    t.add(30)
    actual = t.maxValue()
    expected = 30
    assert actual == expected


def test_max_value2():

    actual = b.maxValue()
    expected = 90
    assert actual == expected
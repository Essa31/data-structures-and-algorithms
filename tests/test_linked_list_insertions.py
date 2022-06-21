import pytest
from linked_list_insertions.linked_list_insertions  import Node,linkedlist
a=linkedlist()

a.append(1)
a.append(3)
a.append(2)
b=linkedlist()
b.append(1)
b.append(3)
b.append(2)
#Can successfully add a node to the end of the linked list
def test_append():
    b.append(4)
    actual=a.to_string()
    expected="<1> -- ><3> -- ><2> -- ><4> -- >Null"
    return actual==expected
#Can successfully add multiple nodes to the end of a linked list
def test_append1():
    b.append(1)
    b.append(3)
    b.append(2)
    actual = a.to_string()
    expected = "<1> -- ><3> -- ><2> -- ><4> -- ><1> -- ><3> -- ><2> -- >Null"
    return actual == expected

#Can successfully insert a node before a node located i the middle of a linked list
def test_Insert_Before():


    a.Insert_Before(3,5)
    actual = a.to_string()
    expected="<1> -- ><5> -- ><3> -- ><2> -- >Null"
    return actual == expected


# Can successfully insert a node before the first node of a linked list
def test_Insert_Before2():

    a.Insert_Before(1,5)
    actual = a.to_string()
    expected="<5> -- ><1> -- ><3> -- ><2> -- >Null"
    return actual == expected


#Can successfully insert after a node in the middle of the linked list
def test_Insert_After():

    a.Insert_After(3, 5)
    actual = a.to_string()
    expected = "<1> -- ><3> -- ><5> -- ><2> -- >Null"
    return actual == expected


#Can successfully insert a node after the last node of the linked list
def test_Insert_After2():
    a.Insert_After(2, 5)
    actual = a.to_string()
    expected = "<1> -- ><3> -- ><2> -- ><5> -- >Null"
    return actual == expected














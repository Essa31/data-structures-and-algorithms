import pytest
from linked_list_insertions.linked_list_insertions import Node,linkedlist

a=linkedlist()
a.append(1)
a.append(3)
a.append(2)
<<<<<<< HEAD
b=linkedlist()
b.append(1)
b.append(3)
b.append(2)
=======

d=linkedlist()
d.append(1)
d.append(3)
d.append(2)
>>>>>>> 4b04085dd4207c94cd289095777614946b4b061f

c=linkedlist()
c.append(1)
c.append(3)
c.append(2)
<<<<<<< HEAD
#Can successfully add a node to the end of the linked list
def test_append():
    b.append(4)
    actual=b.to_string()
    expected="<1> -- ><3> -- ><2> -- ><4> -- >Null"
    assert actual==expected
#Can successfully add multiple nodes to the end of a linked list
def test_append1():
    b.append(1)
    b.append(3)
    b.append(2)
    actual = b.to_string()
=======



#Can successfully add a node to the end of the linked list
def test_append():
    a.append(4)
    actual=a.to_string()
    expected="<1> -- ><3> -- ><2> -- ><4> -- >Null"
    assert actual==expected
# Can successfully add multiple nodes to the end of a linked list
def test_append1():
    a.append(1)
    a.append(3)
    a.append(2)
    actual = a.to_string()
>>>>>>> 4b04085dd4207c94cd289095777614946b4b061f
    expected = "<1> -- ><3> -- ><2> -- ><4> -- ><1> -- ><3> -- ><2> -- >Null"
    assert actual == expected
#
#Can successfully insert a node before a node located i the middle of a linked list
def test_Insert_Before():


    a.Insert_Before(3,5)
    actual = a.to_string()
<<<<<<< HEAD
    expected="<1> -- ><5> -- ><3> -- ><2> -- >Null"
    assert actual == expected
# Can successfully insert a node before the first node of a linked list
def test_Insert_Before2():

    a.Insert_Before(1,5)
    actual = a.to_string()
    expected="<5> -- ><1> -- ><5> -- ><3> -- ><2> -- >Null"
    assert actual == expected
# Can successfully insert after a node in the middle of the linked list
=======
    expected="<1> -- ><5> -- ><3> -- ><2> -- ><4> -- ><1> -- ><3> -- ><2> -- >Null"
    assert actual == expected
#
#
# Can successfully insert a node before the first node of a linked list
def test_Insert_Before2():

    d.Insert_Before(1,5)
    actual = d.to_string()
    expected="<5> -- ><1> -- ><3> -- ><2> -- >Null"
    assert actual == expected


#
#
#Can successfully insert after a node in the middle of the linked list
>>>>>>> 4b04085dd4207c94cd289095777614946b4b061f
def test_Insert_After():
    d.Insert_After(1, 5)
    actual = d.to_string()
    expected = "<5> -- ><1> -- ><5> -- ><3> -- ><2> -- >Null"
    assert actual == expected


    assert actual == expected


<<<<<<< HEAD
    c.Insert_After(3, 5)
    actual = c.to_string()
    expected = "<1> -- ><3> -- ><5> -- ><2> -- >Null"
    assert actual == expected
#Can successfully insert a node after the last node of the linked list
def test_Insert_After2():
    a.Insert_After(2, 5)
    actual = a.to_string()
    expected = "<5> -- ><1> -- ><5> -- ><3> -- ><2> -- ><5> -- >Null"
=======
#Can successfully insert a node after the last node of the linked list
def test_Insert_After2():
    c.Insert_After(2, 5)
    actual = c.to_string()
    expected = "<1> -- ><3> -- ><2> -- ><5> -- >Null"
>>>>>>> 4b04085dd4207c94cd289095777614946b4b061f
    assert actual == expected














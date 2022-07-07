import pytest
from linked_list_zip.link_list_zip import Node,linkedlist



a=linkedlist()

a.append(1)
a.append(3)
a.append(2)

b=linkedlist()
b.append(5)
b.append(9)
#----------------------------------------------------------
d=linkedlist()
d.append(5)
d.append(9)
d.append(4)

c=linkedlist()
c.append(1)
c.append(3)
c.append(2)
#-----------------------------------------------------------
e=linkedlist()

e.append(1)
e.append(3)

f=linkedlist()
f.append(5)
f.append(9)
f.append(4)

def test_zip():

    a.zipLists(a, b)

    actual=a.to_string()
    expected="<1> -- ><5> -- ><3> -- ><9> -- ><2> -- >Null"
    assert actual==expected

def test_zip2():

    c.zipLists(c, d)

    actual=c.to_string()
    expected="<1> -- ><5> -- ><3> -- ><9> -- ><2> -- ><4> -- >Null"
    assert actual==expected

def test_zip3():
    e.zipLists(e,f)

    actual=e.to_string()
    expected="<1> -- ><5> -- ><3> -- ><9> -- ><4> -- >Null"
    assert actual==expected
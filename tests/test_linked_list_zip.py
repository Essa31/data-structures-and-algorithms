import pytest
from linked_list_zip.linked_list_zip  import (Node,linkedlist)



a=linkedlist()

a.append(1)
a.append(3)
a.append(2)

b=linkedlist()
b.append(5)
b.append(9)


c=linkedlist()
c.append(1)
c.append(3)
def test_zip():
    a.zipLists(a, b)

    actual=a.to_string()
    expected="<1> -- ><5> -- ><3> -- ><9> -- ><2> -- >Null"
    return actual==expected

def test_zip2():
    b.append(4)
    a.zipLists(a, b)

    actual=a.to_string()
    expected="<1> -- ><5> -- ><3> -- ><9> -- ><2> -- ><4> -- >Null"
    return actual==expected

def test_zip3():
    a.zipLists(c,b)

    actual=a.to_string()
    expected=""
    return actual==expected
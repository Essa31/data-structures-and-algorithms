import pytest
from linked_list_kth.linked_list_kth  import Node,linkedlist
a=linkedlist()

a.append(1)
a.append(3)
a.append(2)



d=linkedlist()

d.append(3)


#Where k is greater than the length of the linked list
def test_kth_From_End():
    k=4
    actual=a.kth_From_End(k)
    expected="Exception"
    return actual==expected
# Where k and the length of the list are the same
def test_kth_From_End2():
    k = 3
    actual = a.kth_From_End(k)
    expected = "Exception"
    return actual == expected
#Where k is not a positive integer
def test_kth_From_End3():
    k = -3
    actual = a.kth_From_End(k)
    expected = "Exception"
    return actual == expected
#“Happy Path” where k is not at the end, but somewhere in the middle of the linked list
def test_kth_From_End4():
    k = 1
    actual = a.kth_From_End(k)
    expected = "3"
    return actual == expected
#Where the linked list is of a size 1
def test_kth_From_End5():
    k = 0
    actual = d.kth_From_End(k)
    expected = "3"
    return actual == expected




import pytest
from stack_and_queue.stack_queue_pseudo import *
stack1=Pseudo_queue()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

stack2=Pseudo_queue()
# Can successfully enqueue onto a stack
def test_enqueue():
    stack1.enqueue(5)
    actual=str(stack1)
    expected="5->4->3->2->1->"
    assert actual == expected


# Can successfully enqueue multiple values into a stack
def test_enqueue2():
    stack1.enqueue(6)
    stack1.enqueue(7)
    stack1.enqueue(8)
    actual=str(stack1)
    expected="8->7->6->5->4->3->2->1->"
    assert actual == expected

# Can successfully dequeue1 onto a stack
def test_dequeue1():
    stack1.dequeue()
    actual = str(stack1)
    expected = "8->7->6->5->4->3->2->"
    assert actual == expected
#
# Can successfully dequeue multiple values into a stack
def test_dequeue2():
    stack1.dequeue()
    stack1.dequeue()
    stack1.dequeue()
    actual = str(stack1)
    expected = "8->7->6->5->"
    assert actual == expected
# can successfully dequeue into a empty stack
def test_empty_stack():
    with pytest.raises(Exception) as exc:
        stack2.dequeue()

        raise Exception( "Peeking from an empty stack")

# Can successfully enqueue onto a empty stack
def test_enqueue3():
    stack2.enqueue(5)
    actual = str(stack2)
    expected = "5->"
    assert actual == expected
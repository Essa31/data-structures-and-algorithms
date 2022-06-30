import pytest
from stack_and_queue.stack_and_queue1 import *
#Stack-------------------------------------------------
stack1=Stack()

stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)

stack2=Stack()
stack2.push(1)
stack2.push(2)
stack2.push(3)
stack2.push(4)

stack3=Stack()
#Queue-------------------------------------------------
queue1=Queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.enqueue(3)

queue2=Queue()




# Can successfully push onto a stack
def test_Stack1():
    stack1.push(5)
    actual=stack1.peek()
    expected=5

    assert actual == expected

def test_Stack2():
    stack1.push(6)
    stack1.push(7)
    stack1.push(8)
    actual=str(stack1)
    expected="8->7->6->5->4->3->2->1->"

    assert actual == expected
#Can successfully pop off the stack
def test_Stack3():
    stack1.pop()
    actual=str(stack1)
    expected="7->6->5->4->3->2->1->"

    assert actual == expected
#Can successfully empty a stack after multiple pops
def test_Stack4():
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()
    stack1.pop()

    actual=str(stack1)
    expected=""

    assert actual == expected
#Can successfully peek the next item on the stack
def test_Stack5():


    actual=stack2.peek()
    expected=4

    assert actual == expected

#Can successfully instantiate an empty stack
def test_Stack6():
    actual = str(stack3)
    expected = ""
    assert actual == expected

# Calling pop or peek on empty stack raises exception
def test_Stack7():
    with pytest.raises(Exception) as exc:
        stack1.peek()

    assert str(exc.value) == "Peeking from an empty stack"

def test_Queue1():
    queue1.enqueue(4)
    actual = str(queue1)
    expected ="1->2->3->4->"
    assert actual == expected
#Can successfully enqueue multiple values into a queue
def test_Queue2():
    queue1.enqueue(5)
    queue1.enqueue(6)
    queue1.enqueue(7)

    actual = str(queue1)
    expected ="1->2->3->4->5->6->7->"
    assert actual == expected

#Can successfully dequeue out of a queue the expected value
def test_Queue3():
    queue1.dequeue()

    actual = str(queue1)
    expected ="2->3->4->5->6->7->"
    assert actual == expected
# Can successfully peek into a queue, seeing the expected value


def test_Queue4():

    actual = queue1.peek()
    expected = 2
    assert actual == expected
#Can successfully empty a queue after multiple dequeues
def test_Queue5():
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()
    queue1.dequeue()

    actual = str(queue1)
    expected = ""
    assert actual == expected


# Can successfully instantiate an empty queue
def test_Queue6():
    actual = str(queue2)
    expected = ""
    assert actual == expected


# Calling dequeue or peek on empty queue raises exception
def test_Queue7():
    with pytest.raises(Exception)as exc:
        queue1.peek()

    assert str(exc.value) == "Peeking from an empty stack"




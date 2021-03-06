from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:


    def __init__(self):
        self.head = Node("head")
        self.size = 0


    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out


    def getSize(self):
        return self.size


    def isEmpty(self):
        return self.size == 0

    def peek(self):


        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value


    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1


    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


class Queue:

    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

    # Method to add an item to the queue
    def enqueue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def dequeue(self):

        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        temp = self.front
        self.front = temp.next

        if (self.front == None):

            self.rear = None

        return self.front.value



    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.front.value

    def __str__(self):
        cur = self.front
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next

        return out


#stack-----------------------------------------------------------------
stack = Stack()

stack.push(10)
stack.push(5)
stack.push(3)
stack.push(7)
print(f"Stack: {stack}")


print(stack.isEmpty())
print(stack.peek())
print(stack.Max_stack())

#Queue--------------------------------------------------------------------

# queue1=Queue()
# queue1.enqueue(1)
# queue1.enqueue(2)
# queue1.enqueue(3)
# queue1.enqueue(4)
# queue1.enqueue(5)
# queue1.enqueue(6)
# queue1.enqueue(7)
# #
# print(queue1.isEmpty())
# queue1.dequeue()
# queue1.peek()
# print(str(queue1))

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Pseudo_queue:


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


    def enqueue(self,value):
        self.push(value)


    def dequeue(self):
        if not self.isEmpty():
            lst=[]
            while not self.isEmpty():
                x=self.pop()
                lst+=[x]

            x=lst.pop()
            print(x)
            lst=lst[::-1]
            for i in lst:
                self.push(i)
            return x

        else:
            raise Exception("Popping from an empty stack")


stack = Pseudo_queue()
for i in range(1, 9):
    stack.push(i)
print(f"Stack: {stack}")



stack.dequeue()

print(f"Stack: {stack}")
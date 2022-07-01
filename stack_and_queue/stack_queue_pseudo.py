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


#Write a function called  dequeue
    def dequeue(self):
        #Set a condition if the stack is not empty, start executing the code, but if it is empty, give a warning

        if not self.isEmpty():
            lst=[]
            #3.I'm making a while loop that goes through each element in stack1 and deletes it and then puts it in stack2

            while not self.isEmpty():
                x=self.pop()
                lst+=[x]
            # delete the latest items added to Stack 2
            x=lst.pop()
            print(x)
            #I reverse the order of stack and then re-enter the elements in stack2 into stack 1
            lst=lst[::-1]
            for i in lst:
                self.push(i)
            #return dequeue value
            return x

        else:
            raise Exception("Popping from an empty stack")




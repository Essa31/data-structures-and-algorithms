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


#Create a class named Dog that takes the name and type of the dog
class Dog:
    def __init__(self,name,type="dog"):
        self.name=name
        self.type=type
#Create a class named Cat that takes the name and type of the cat
class Cat:
    def __init__(self,name,type="cat"):
        self.name=name
        self.type=type

#Create a class named AnimalShelter
class AnimalShelter():
    def __init__(self):
        self.dog=Queue()
        self.cat=Queue()

    #Declare Enqueue That Take Animal_obj
    def enqueue(self, animal):
        # If animal type is a cat, it is added to the Cat queue.
        if animal.type.lower()=="cat":
            self.cat.enqueue(animal)
        # If animal type is a dog, it is added to the Dog queue.
        elif animal.type.lower()=="dog":
            self.dog.enqueue(animal)
        # return animal type
        return animal.type




    #Declare Dnqueue That Take pref
    def dequeue(self,pref):
        # If pref is a cat,Delete the first item income to Cat Queue and return string cat
        if pref=="cat":
            self.cat.dequeue()
            return "cat"
        # If pref is a dog,Delete the first item income to Dog Queue and return string dog
        elif pref=="dog":
            self.dog.dequeue()
            return "dog"

        #If pref is not a dog or cat, return None
        else:
            return None


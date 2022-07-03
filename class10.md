# Stacks and Queues
Read: Stacks & Queues
Stacks
Some basic information about stacks:
A stack is a data structure that consist of nodes that hold values and point to the next one in line.
Stacks follow the following concepts:
FILO(First In Last Out), Which means that the first element added will be the last to be popped.
LIFO(Last In First Out), which means that the last added element will be the first to be popped.
As you just saw I used the term “popped”, what does that mean?

In order to understand what does that mean, lets list some common terminologies for stack:

Term	Meaning
Push	add an element to stack
Pop	remove an element to stack, popping an empty stack will return an exception
Top	Points to the top of the stack
Peek	View the top node of the stack, peeking an empty stack will return an exception
isEmpty	Return true if empty
Queues
Some basic information about queues:
A queue is a data structure that consist of nodes that hold values and point to the next one in line.
Queues follow the concept of FIFO(First In First Out), Which means that the first element in added will be the first to be dequeued.
And as you saw I used the term “dequeued” here for queues, which means that, just like stacks there are some common terms we need to know, which are the following:

Term	Meaning
Enqueue	Add an element to queue
Dequeue	Remove an element to queue, dequeuing an empty queue will return an exception
Front	point to the first node
Rear	point to the last point
Peek	view the value of the front node, peeking an empty queue will return an exception
IsEmpty	Return true if empty
Note: Each of the stack terms and the queue terms represent a method of the of it’s data structure methods, and each of them have a time and space complexity of O(1).

## Challenge
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:

## push

* Arguments: value

* adds a new node with that value to the top of the stack with an O(1) Time performance.

## pop

* Arguments: none

* Returns: the value from node from the top of the stack

* Removes the node from the top of the stack

* Should raise exception when called on empty stack

## peek

* Arguments: none

* Returns: Value of the node located at the top of the stack

* Should raise exception when called on empty stack
## is empty

* Arguments: none

* Returns: Boolean indicating whether or not the stack is empty.

## Queue
* Create a Queue class that has a front property. It creates an empty Queue when instantiated.
* This object should be aware of a default empty value assigned to front when the queue is created.
* The class should contain the following methods:
## enqueue

* Arguments: value
* adds a new node with that value to the back of the queue with an O(1) Time performance.
## dequeue

* Arguments: none
* Returns: the value from node from the front of the queue
* Removes the node from the front of the queue
* Should raise exception when called on empty queue
## peek
* Arguments: none
* Returns: Value of the node located at the front of the queue
* Should raise exception when called on empty stack
## is empty

Arguments: none
Returns: Boolean indicating whether or not the queue is empty

## Approach & Efficiency

I followed the approach that the code takes the least time and space, where B(o) takes space and time and be simple to be easy to understand

## API


## Stack
Create a Stack class that has a top property. It creates an empty Stack when instantiated.
This object should be aware of a default empty value assigned to top when the stack is created.
The class should contain the following methods:

* Arguments: value

* adds a new node with that value to the top of the stack with an O(1) Time performance.

## pop

* Arguments: none

* Returns: the value from node from the top of the stack

* Removes the node from the top of the stack

* Should raise exception when called on empty stack

## peek

* Arguments: none

* Returns: Value of the node located at the top of the stack

* Should raise exception when called on empty stack
## is empty

* Arguments: none

* Returns: Boolean indicating whether or not the stack is empty.

## Queue
* Create a Queue class that has a front property. It creates an empty Queue when instantiated.
* This object should be aware of a default empty value assigned to front when the queue is created.
* The class should contain the following methods:
## enqueue

* Arguments: value
* adds a new node with that value to the back of the queue with an O(1) Time performance.
## dequeue

* Arguments: none
* Returns: the value from node from the front of the queue
* Removes the node from the front of the queue
* Should raise exception when called on empty queue
## peek
* Arguments: none
* Returns: Value of the node located at the front of the queue
* Should raise exception when called on empty stack
## is empty

Arguments: none
Returns: Boolean indicating whether or not the queue is empty

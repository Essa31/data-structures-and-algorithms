# Trees
A tree is a popular data structure that is non-linear in nature. Unlike other data structures like array, stack, queue, and linked list which are linear in nature, a tree represents a hierarchical structure. The ordering information of a tree is not important. A tree contains nodes and 2 pointers. These two pointers are the left child and the right child of the parent node. Let us understand the terms of tree in detail.

Root: The root of a tree is the topmost node of the tree that has no parent node. There is only one root node in every tree.
Edge: Edge acts as a link between the parent node and the child node.
Leaf: A node that has no child is known as the leaf node. It is the last node of the tree. There can be multiple leaf nodes in a tree.
Depth: The depth of the node is the distance from the root node to that particular node.
Height: The height of the node is the distance from that node to the deepest node of the tree.
Height of tree: The Height of the tree is the maximum height of any node.
      tree
      —-
           j    <– root
       /   \
     f      k  
  /   \      \
a     h      z    <– leaves

Why Use Trees? 

1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer: 

file system

———–

       user <– root
    /       \
 . . .      home
         /          \
   ugrad        course
    /            /      |     \
. . .      cs101  cs112  cs113

2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays). 
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists). 
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on the number of nodes as nodes are linked using pointers.





## Challenge
# Node
* Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
# Binary Tree
* Create a Binary Tree class
* Define a method for each of the depth first traversals:
1. pre order
2. in order
3. post order which returns an array of the values, ordered appropriately.
# Binary Search Tree
* Create a Binary Search Tree class
* This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
* Add
  * Arguments: value
  * Return: nothing
  * Adds a new node with that value in the correct location in the binary search tree.
* Contains
  * Argument: value
  * Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
I followed the approach that the code takes the least time and space, where B(o) takes space and time and be simple to be easy to understand

## API

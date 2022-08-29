# Depth First Traversal
<!-- Short summary or background information -->

Depth-first search is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

## Challenge
<!-- Description of the challenge -->
**Write the following method for the Graph class:**

- Name: Depth first
- Arguments: Node (Starting point of search)
- Return: A collection of nodes in their pre-order depth-first traversal order
- Program output: Display the collection

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
I took an iterative approach, the traversal technique used is pre-order, as for the Big O:
- Time:  O(V + E)
- Space: O(n)

## Solution
<!-- Embedded whiteboard image -->


## How to run:

In order to run the code enter "**python .\graph_depth_first\graph_depth_first.py**"

In order to run the tests enter "**pytest .\tests\test_graph_depth_first.py**"
# Graphs
<!-- Short summary or background information -->

Graph: is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.
## Challenge
<!-- Description of the challenge -->
**Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:**

- add node
  - Arguments: value
  - Returns: The added node
  - Add a node to the graph
- add edge
  - Arguments: 2 nodes to be connected by the edge, weight (optional)
  - Returns: nothing
  - Adds a new edge between two nodes in the graph
  - If specified, assign a weight to the edge
  - Both nodes should already be in the Graph
- get nodes
  - Arguments: none
  - Returns all of the nodes in the graph as a collection (set, list, or similar)
- get neighbors
  - Arguments: node
  - Returns a collection of edges connected to the given node
  - Include the weight of the connection in the returned collection
- size
  - Arguments: none
  - Returns the total number of nodes in the graph

## Approach & Efficiency

I took a linear approach throughout all methods, as for the Big O:

- add node:
  - **Time**: O(1)
  - **Space**: O(1)

- add edge:
  - **Time**: O(1)
  - **Space**: O(1)

- get nodes:
  - **Time**: O(1)
  - **Space**: O(1)

- get neighbors:
  - **Time**: O(1)
  - **Space**: O(1)

- size:
  - **Time**: O(1)
  - **Space**: O(1)

## API
<!-- Description of each method publicly available in your Graph -->

- **add_node()**: Add a node to the graph.
- **add_edge()**: Adds a new edge between two nodes in the graph.
- **get nodes()**: Returns all of the nodes in the graph as a collection (set, list, or similar).
- **get neighbors()**: Returns a collection of edges connected to the given node Include the weight of the connection in the returned collection.
- **size()**: Returns the total number of nodes in the graph
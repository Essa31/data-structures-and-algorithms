
## Challenge

Write the following method for the Binary Tree class

* find maximum value
* Arguments: none
* Returns: number

Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
## whiteboard images : 

![find_max image](code%20challenge%2017%20.png)
### Approach & Efficiency
- in the pre-order , in-order and post-order i used the recursive function to traverse through the 
- tree nodes and takes the preferred node into list 
- after the end of the tree return the list 
- 
- Big o notation : 
  - Time complexity :
    - findMax : O(n)
  - space complexity :
    - findMax : O(n)
#### API

- findMax method : 
  - in this method i 
  - check if the tree is empty return none 
  - declare a function with root value and the max with zero
  - check if the root is less than the max , if yes max will equal the value of the root
  - else do the function again ( recursive function ) with the left node of the root 
  - else do the function again ( recursive function ) with the right node of the root
  - return the maximum value 
  - return the recursive function with the root node of the tree
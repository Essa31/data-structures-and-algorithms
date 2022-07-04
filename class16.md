# Challenge Summary
Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

![](ch16.png)


## visualization

![](https://whiteboardcoders.com/user/pages/03.home/01.problems/trees/21jan2020_checkSubtree/whiteboard.png)



## Approach & Efficiency
I followed the approach that the code takes the least time and space, where B(o) takes space and time and be simple to be easy to understand

## Solution
```

    def maxValue(self):
        current = self.root


        while (current.right):
            current = current.right
        return current.value

```